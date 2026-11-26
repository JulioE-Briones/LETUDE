import numpy as np, json, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
S = 3  # image px per CSS px
D = '/tmp/claude-0/-home-user-LETUDE/5c12a43c-7272-5065-b0ba-682f9a1fdc36/scratchpad/oicv2/'
rng = np.random.default_rng(7)

def load(n): return np.asarray(Image.open(f'{D}pages/p-{n-1:03d}.jpg').convert('RGB')).astype(np.float32)

def fill(a, x0, y0, x1, y1, ring=4, sides='lrtb', flat=False):
    """Replace rect with a smooth surface fitted on a ring around it, plus matching grain."""
    X0, Y0, X1, Y1 = int(x0*S), int(y0*S), int(x1*S), int(y1*S)
    R = ring*S
    pts, vals = [], []
    for side in sides:
        if side == 't': ys, xs = np.mgrid[Y0-R:Y0, X0:X1]
        if side == 'b': ys, xs = np.mgrid[Y1:Y1+R, X0:X1]
        if side == 'l': ys, xs = np.mgrid[Y0:Y1, X0-R:X0]
        if side == 'r': ys, xs = np.mgrid[Y0:Y1, X1:X1+R]
        pts.append(np.stack([xs.ravel(), ys.ravel()], 1)); vals.append(a[ys.ravel(), xs.ravel()])
    P = np.concatenate(pts).astype(np.float64); V = np.concatenate(vals).astype(np.float64)
    M = np.c_[np.ones(len(P)), P[:, 0]-X0, P[:, 1]-Y0]
    keep = np.ones(len(P), bool)
    for _ in range(3):
        coef, *_ = np.linalg.lstsq(M[keep], V[keep], rcond=None)
        res = V - M @ coef
        sd = res[keep].std(0) + 1e-6
        keep = (np.abs(res) < 2.5*sd).all(1)
    noise_sd = res[keep].std(0)
    yy, xx = np.mgrid[0:Y1-Y0, 0:X1-X0]
    surf = coef[0] + coef[1]*xx[..., None] + coef[2]*yy[..., None]
    if not flat and noise_sd.mean() > 0.8:
        n = rng.normal(0, 1, (Y1-Y0, X1-X0, 1))
        surf = surf + n*noise_sd
    a[Y0:Y1, X0:X1] = np.clip(surf, 0, 255)
    return coef[0]  # base color


def fill_v(a, x0, y0, x1, y1, ring=3):
    """Per-column vertical interpolation between the bands above and below (keeps vertical edges)."""
    X0, Y0, X1, Y1 = int(x0*S), int(y0*S), int(x1*S), int(y1*S); R = ring*S
    top = a[Y0-R:Y0, X0:X1].mean(0); bot = a[Y1:Y1+R, X0:X1].mean(0)
    from scipy.ndimage import gaussian_filter1d as g1
    top = g1(top, 2.0, axis=0); bot = g1(bot, 2.0, axis=0)
    sd = np.concatenate([a[Y0-R:Y0, X0:X1]-top, a[Y1:Y1+R, X0:X1]-bot]).std(0, keepdims=True)
    t = np.linspace(0, 1, Y1-Y0)[:, None, None]
    v = top[None]*(1-t) + bot[None]*t
    v = v + rng.normal(0, 1, (Y1-Y0, X1-X0, 1))*sd.mean(2, keepdims=True)
    a[Y0:Y1, X0:X1] = np.clip(v, 0, 255)

def lum(p): return p @ np.array([0.299, 0.587, 0.114])

def matte(a, x0, y0, x1, y1, bg, ink):
    """Extract alpha of text (ink over bg) in a rect."""
    X0, Y0, X1, Y1 = int(x0*S), int(y0*S), int(x1*S), int(y1*S)
    p = a[Y0:Y1, X0:X1]
    lb, li = lum(np.array(bg, float)), lum(np.array(ink, float))
    al = np.clip((lum(p)-lb)/(li-lb), 0, 1)
    al[al < 0.08] = 0
    return al

def comp(a, x, y, al, ink):
    X, Y = int(round(x*S)), int(round(y*S))
    h, w = al.shape
    reg = a[Y:Y+h, X:X+w]
    ink = np.array(ink, float)
    a[Y:Y+h, X:X+w] = reg*(1-al[..., None]) + ink*al[..., None]

def digit_swap(a, line, src, one, rest_end, bg, ink, dx):
    """'2.1' -> '2.2': src=(x0,x1) of '2', one=(x0,x1) of '1', rest from one[1] to rest_end shifts by dx."""
    y0, y1 = line
    g = matte(a, src[0], y0, src[1], y1, bg, ink)
    rest = matte(a, one[1], y0, rest_end, y1, bg, ink)
    fill(a, one[0], y0, rest_end+dx+1, y1)
    comp(a, one[0]+0.3, y0, g, ink)
    comp(a, one[1]+dx, y0, rest, ink)

def glyph(a, ch, font, size, color, left, bottom, clear=None, bgfill=True):
    if clear: fill(a, *clear)
    f = ImageFont.truetype(font, int(round(size*S)))
    l, t, r, b = f.getbbox(ch)
    W, H = r-l+8, b-t+8
    m = Image.new('L', (W, H), 0); ImageDraw.Draw(m).text((4-l, 4-t), ch, font=f, fill=255)
    al = np.asarray(m).astype(np.float32)/255
    X = int(round(left*S))-4; Y = int(round(bottom*S))-(H-4)
    reg = a[Y:Y+H, X:X+W]
    a[Y:Y+H, X:X+W] = reg*(1-al[..., None]) + np.array(color, float)*al[..., None]

def H(c): c = c.lstrip('#'); return tuple(int(c[i:i+2], 16) for i in (0, 2, 4))

FD = '/usr/share/fonts/opentype/inter/'
out = {}

# ---------- S2
a = load(2)
fill(a, 700, 418, 926, 441, flat=True)                         # card 3, line 2
cream = (238, 231, 220)
digit_swap(a, (480, 501), (708.8, 716.6), (720.6, 725.9), 1180, cream, H('#5c646f'), 2.7)
glyph(a, '5', FD+'Inter-Regular.otf', 15.6, H('#a64f10'), 664.3, 517.0, clear=(663.5, 504.5, 673.2, 519.5))
out[2] = a

# ---------- S4
a = load(4)
fill(a, 80, 116, 545, 251, sides='lrt')  # title block (junk overlaps)
fill(a, 936, 188, 984, 251, sides='lrt')  # junk above donors card
fill(a, 374, 258, 628, 484, flat=True)  # employers card content
fill(a, 658, 386, 908, 482, flat=True)  # alumni body
fill(a, 936, 260, 1188, 470, flat=True)  # donors card content
out[4] = a

# ---------- S8 chevron gaps
a = load(8)
for cx, cl in ((296.5, 314), (525.5, 543), (754.5, 772), (983.5, 1001)):
    fill_v(a, cx-14, 372, cl+12.6, 452, ring=8)
out[8] = a

# ---------- S9
a = load(9)
digit_swap(a, (237, 260), (655.8, 664.8), (668.2, 674.6), 1140, (237, 230, 219), H('#5c646f'), 2.7)
out[9] = a

# ---------- S10 hosting chip
a = load(10)
fill(a, 768, 504, 966, 578, flat=True)
out[10] = a

# ---------- S13 options rows
a = load(13)
fill(a, 96, 446, 584, 606, flat=True)
out[13] = a

# ---------- S14
a = load(14)
glyph(a, '5', FD+'Inter-Bold.otf', 15.5, H('#ac4d08'), 473.9, 100.3, clear=(472.5, 87.5, 483.5, 102))
glyph(a, '5', FD+'InterDisplay-ExtraBold.otf', 64, H('#162436'), 646.9, 174.3, clear=(644, 123, 686.5, 177))
out[14] = a

# ---------- S15 W20 card line 2
a = load(15)
fill(a, 1036, 368, 1188, 391, flat=True)
out[15] = a

# ---------- S16
a = load(16)
digit_swap(a, (504, 531), (196.4, 208.5), (211.2, 217.6), 300, (251, 248, 243), H('#325880'), 5.6)
fill(a, 660, 547, 906, 603, flat=True)
out[16] = a

# ---------- S17 tables
a = load(17)
fill(a, 78, 284, 1204, 592)
out[17] = a

for n, arr in out.items():
    Image.fromarray(arr.astype(np.uint8)).save(f'{D}pages_fix/p-{n-1:03d}.png')
print('done', sorted(out))
