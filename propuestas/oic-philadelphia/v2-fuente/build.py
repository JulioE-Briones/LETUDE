import os, re, subprocess, html
from PIL import Image
D = '/tmp/claude-0/-home-user-LETUDE/5c12a43c-7272-5065-b0ba-682f9a1fdc36/scratchpad/oicv2/'
SRC = '/root/.claude/uploads/5c12a43c-7272-5065-b0ba-682f9a1fdc36/139677f6-From_Legacy_to_Opportunity___TWOHUMAN___OIC_Philadelphia.pdf'
os.makedirs(D+'bg', exist_ok=True)

# ---------- backgrounds (2560x1440 JPEG)
for n in range(1, 19):
    fx = f'{D}pages_fix/p-{n-1:03d}.png'
    im = Image.open(fx if os.path.exists(fx) else f'{D}pages/p-{n-1:03d}.jpg').convert('RGB')
    im.resize((2560, 1440), Image.LANCZOS).save(f'{D}bg/s{n:02d}.jpg', quality=84, optimize=True, progressive=True)

# ---------- styles (ink offsets measured: top, left)
ST = {
 'body': ("font-family:'IT';font-weight:400;font-size:15.5px;letter-spacing:-0.03em", 1.67, 1.33, 15.5),
 'sub':  ("font-family:'IT';font-weight:800;font-size:15.5px;letter-spacing:-0.03em", 2.25, 1.0, 15.5),
 'head': ("font-family:'ID';font-weight:800;font-size:20.5px;letter-spacing:-0.02em", 1.67, 1.0, 20.5),
 'chip': ("font-family:'IT';font-weight:600;font-size:16.5px;letter-spacing:-0.02em", 2.0, 1.0, 16.5),
 'opt':  ("font-family:'IT';font-weight:600;font-size:16px;letter-spacing:-0.03em", 2.33, 1.0, 16),
 'num':  ("font-family:'IT';font-weight:700;font-size:16.5px;letter-spacing:-0.02em", 2.0, 1.0, 16.5),
 'b17':  ("font-family:'IT';font-weight:700;font-size:17px;letter-spacing:-0.02em", 0.67, 1.0, 17),
 't1':   ("font-family:'ID';font-weight:800;font-size:64px;letter-spacing:-0.038em", 7.33, 3.0, 64),
 'is':   ("font-family:'Instrument Serif';font-style:italic;font-size:69px;letter-spacing:-0.006em", 5.75, 0.35, 69),
}
def T(style, ink_left, ink_top, text, color, lh=None, extra=''):
    css, ot, ol, fs = ST[style]
    lh = lh or fs
    top = ink_top - (ot + (lh-fs)/2)
    left = ink_left - ol
    return f'<div class="t" style="{css};line-height:{lh}px;left:{left:.2f}px;top:{top:.2f}px;color:{color};{extra}">{text}</div>'

NAVY, GREY, BLUE = '#192434', '#5c6470', '#2b5988'

ICON = {
 'briefcase': '<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2.5" y="7" width="19" height="13" rx="2"/><path d="M8.5 7V5a2 2 0 0 1 2-2h3a2 2 0 0 1 2 2v2"/><path d="M2.5 13h19"/></svg>',
 'heart': '<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="#295b8e" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20s-7-4.4-9.2-8.6C1.4 8.6 3 5 6.6 5c2 0 3.4 1.1 4.2 2.4h2.4C14 6.1 15.4 5 17.4 5 21 5 22.6 8.6 21.2 11.4 19 15.6 12 20 12 20z"/></svg>',
 'server': '<svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="#fbf8f3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="8" rx="2"/><rect x="3" y="13" width="18" height="8" rx="2"/><path d="M7 7h.01M7 17h.01"/></svg>',
 'chev': '<svg viewBox="0 0 12 20" width="11" height="18" fill="none" stroke="#e8862a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M2 2l8 8-8 8"/></svg>',
}
def circle(cx, cy, r, color, icon):
    return (f'<div class="t" style="left:{cx-r}px;top:{cy-r}px;width:{2*r}px;height:{2*r}px;border-radius:50%;'
            f'background:{color};display:flex;align-items:center;justify-content:center">{ICON[icon]}</div>')

OV = {n: [] for n in range(1, 19)}

# S2 — card 3, second line
OV[2].append(T('body', 704.7, 421.7, 'then a 60-day warranty', NAVY))

# S4 — title, employers card, alumni body, donors card
OV[4] += [
 T('t1', 88.0, 124.7, 'Four audiences,', '#162436'),
 T('is', 87.0, 188.3, 'four clear tasks.', BLUE),
 circle(397.5, 283, 13.5, '#f28a1e', 'briefcase'),
 T('head', 384.3, 307.0, 'Employers', '#172436'),
 T('sub', 384.7, 340.0, 'Hire graduates or partner<br>on training', '#172334', lh=22.3),
 T('body', 384.7, 393.3, 'An employer page with hiring<br>and partnership options and<br>an inquiry form routed to<br>employer relations.', GREY, lh=22.3),
 T('body', 665.7, 393.3, 'An alumni section with<br>services, events, stories<br>and an alumni update form,<br>included in the core scope.', GREY, lh=22.3),
 circle(959.5, 283, 13.5, '#fbf8f3', 'heart'),
 T('head', 946.3, 307.0, 'Donors and funders', '#f5f1f9'),
 T('sub', 946.7, 339.7, 'Understand impact and give', '#f5f1f9'),
 T('body', 946.7, 370.7, 'An impact and legacy story,<br>published outcomes, a clear<br>donate link and a dedicated<br>donation page, all in the core.', '#d7e8fb', lh=22.3),
]

# S8 — chevrons between steps
for cx in (296.5, 525.5, 754.5, 983.5):
    OV[8].append(f'<div class="t" style="left:{cx-5.5}px;top:401px">{ICON["chev"]}</div>')

# S10 — hosting chip
OV[10] += [f'<div class="t" style="left:776px;top:532.5px">{ICON["server"]}</div>',
           T('chip', 806.0, 535.0, 'Hosting', '#f5f0ee')]

# S13 — options rows
OV[13] += [
 '<div class="t" style="left:104px;top:446px;width:469px;height:1px;background:#35475f"></div>',
 T('opt', 104.3, 458.5, 'Care plan after the 60-day<br>warranty: updates, backups,<br>monitoring and small changes', '#f2efec', lh=20.5),
 f'<div class="t" style="{ST["num"][0]};line-height:16.5px;right:{1280-573.3}px;top:{458.5-2.0}px;color:#f08b21">450 / month</div>',
 '<div class="t" style="left:104px;top:527px;width:469px;height:1px;background:#35475f"></div>',
 T('opt', 104.3, 540.0, 'Alumni section and donation page', '#f2efec'),
 f'<div class="t" style="font-family:IT;font-weight:400;font-size:14px;letter-spacing:-0.02em;line-height:14px;left:103.4px;top:{562-1.5}px;color:#abb8cb">Part of the core scope, at no extra cost</div>',
 f'<div class="t" style="{ST["num"][0]};line-height:16.5px;right:{1280-573.3}px;top:{540-2.0}px;color:#f08b21">Included</div>',
]

# S14 — 5-year table card
rows14 = [
 ('Core website, fixed (alumni and donation pages included)', '17,800', 'None', '17,800', False),
 ('60-day warranty, reviews at 30, 60 and 90 days', 'Included', 'None', 'Included', False),
 ('Hosting, paid directly by OIC (estimate)', 'Setup included', '400–1,200', '2,000–6,000', False),
 ('Care plan after the warranty, optional', 'None', '5,400', '27,000', False),
 ('Total with care plan', '17,800', '5,800–6,600', '46,800–50,800', True),
 ('Total without care plan', '17,800', '400–1,200', '19,800–23,800', True),
]
tr = ''.join(f'<tr><td>{a}</td><td class="n">{b}</td><td class="n">{c}</td><td class="n{" o" if t else ""}">{d}</td></tr>' for a, b, c, d, t in rows14)
OV[14].append(f'''<div class="t card14"><table class="tb14"><tr><th>Item · USD</th><th class="n">One-time</th><th class="n">Per year after launch</th><th class="n">5-year total</th></tr>{tr}</table></div>''')

# S15 — W20 card, line 2
OV[15].append(T('body', 1042.3, 369.7, '60-day warranty', '#abb8cb'))

# S16 — card 3, row 2 (rotated like the card)
OV[16].append(f'<div class="t" style="{ST["b17"][0]};line-height:22px;left:663px;top:{554-(0.67+2.5):.2f}px;color:#172334;transform:rotate(-1.15deg);transform-origin:0 0;white-space:nowrap">'
              '<span style="color:#a64f10;font-weight:400">→</span> 60-day warranty, plus<br>reviews at 30, 60 and 90 days</div>')

# S17 — compliance tables
left17 = [('Mission and strategy (20%)', '3', 'Yes'), ('User journeys and enrollment features (20%)', '4 · 6 · 7 · 8', 'Yes'),
          ('Technical approach, accessibility and security (20%)', '9–10', 'Yes'), ('Portfolio and team (15%)', '11–12', 'Partial'),
          ('Total cost of ownership (15%)', '13 · 14', 'Yes'), ('Project management and handover (10%)', '15', 'Yes')]
right17 = [('Program directory with requirements and cohorts', '7', 'Yes'),
           ('Paths for students, employers, alumni and donors', '4', 'Yes'),
           ('Alumni and donation pages in the core scope', '4 · 13', 'Yes'),
           ('WCAG 2.2 AA accessibility', '2 · 9', 'Yes'),
           ('60-day warranty, reviews at 30, 60 and 90 days', '2 · 15 · 16', 'Yes'),
           ('Total cost of ownership projected over 5 years', '14', 'Yes'),
           ("Honor Rev. Dr. Sullivan's legacy and OIC's role today", '3 · 6', 'Yes'),
           ('OIC keeps control of domain, hosting and accounts', '10 · 15', 'Yes'),
           ('Three past projects with links, results and references', '12', 'Partial')]
def tb(rows, h1, w, cw=78):
    body = ''.join(f'<tr><td>{a}</td><td class="c">{b}</td><td class="m{" p" if m=="Partial" else ""}">{m}</td></tr>' for a, b, m in rows)
    return f'<table class="tb17" style="width:{w}px"><tr><th>{h1}</th><th class="c" style="width:{cw}px">Slide</th><th class="m">Meets</th></tr>{body}</table>'
OV[17] += [f'<div class="t" style="left:86px;top:290px">{tb(left17, "RFP criterion", 537, 104)}</div>',
           f'<div class="t" style="left:648px;top:290px">{tb(right17, "Requirement", 546)}</div>']

# ---------- hidden text layer (searchable / accessible text)
def page_text(n):
    t = subprocess.run(['pdftotext', '-f', str(n), '-l', str(n), SRC, '-'], capture_output=True, text=True).stdout
    t = re.sub(r'\[ic\S*|\bon\b\s*:\s*|\[icon:?\s*\w*\]?|\b(?:ChevronRight|Server)\]|Bri\s*ef\s*ca\s*se\s*\]|He\s*art\s*\]', ' ', t)
    rep = {'WCAG 2.1': 'WCAG 2.2', '3-year total cost': '5-year total cost', 'followed by 30 days of fixes': 'then a 60-day warranty',
           'over 3 years': 'over 5 years', 'OVER 3 YEARS': 'OVER 5 YEARS', '30 days of fixes': '60-day warranty',
           '30 days of post-launch fixes': '60-day warranty, plus reviews at 30, 60 and 90 days',
           'a fuller alumni hub is optional': 'included in the core scope', 'a dedicated donation page is optional': 'a dedicated donation page, all in the core',
           '3-year total': '5-year total'}
    for a, b in rep.items(): t = t.replace(a, b)
    return html.escape(re.sub(r'\s+', ' ', t).strip())


MANUAL = {
 4: "02 · User journeys 20%. Students and job seekers: find a program, check if they qualify, enroll. A filterable program directory (career area, schedule, eligibility, next cohort), an eligibility check and an inquiry form routed to enrollment. Alumni: stay connected and find support. Creative reference: University City District, as the RFP suggests, for its clarity and civic tone. We take the lessons, not the look: OIC's site will look and sound like OIC. TWO&HUMAN · OIC Philadelphia 4 / 18",
 13: "05 · Total cost of ownership 15%. $17,800 for the core scope, options priced up front. TWO&HUMAN · Core scope · USD. Research and task testing 2,400. Information architecture and journeys 1,800. Visual identity for the site and UI design 3,400. Development, including the program directory 5,600. Forms and inquiry routing 1,400. Content migration 1,400. Accessibility, security and analytics 1,200. Training and handover 600. Core total, fixed $17,800. Options · USD: Spanish version of key pages 2,400. Pay only for approved work: 20% directory prototype, 25% design approval, 30% staging site, 25% launch and handover. TWO&HUMAN · OIC Philadelphia 13 / 18",
 14: "05 · Total cost of ownership over 5 years. What OIC pays over 5 years, with no surprises. Hosting: managed WordPress hosting in OIC's name, paid directly to the provider with no markup; the range depends on the plan OIC chooses. No license fees: no proprietary software, so there is nothing to renew with us. Out-of-scope work: $60 per hour, quoted and approved in advance. Payment in U.S. dollars by international bank transfer; IRS Form W-8BEN-E. Prices valid for 90 days. TWO&HUMAN · OIC Philadelphia 14 / 18",
 17: "Annex. Compliance matrix at a glance. Partial: we are a new firm. We offset it with concepts prepared for OIC, a working directory prototype in week 5 and payment against approved milestones. TWO&HUMAN · OIC Philadelphia 17 / 18",
}

secs = []
for n in range(1, 19):
    secs.append(f'<section class="slide" style="background-image:url(bg/s{n:02d}.jpg)"><div class="hid">{html.escape(MANUAL[n]) if n in MANUAL else page_text(n)}</div>{"".join(OV[n])}</section>')

HTML = f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>From Legacy to Opportunity — TWO&amp;HUMAN × OIC Philadelphia</title>
<style>
@page {{ size: 13.333in 7.5in; margin: 0; }}
@font-face {{ font-family: 'IT'; font-weight: 400; src: url(Inter-400.ttf); }}
@font-face {{ font-family: 'IT'; font-weight: 500; src: url(Inter-500.ttf); }}
@font-face {{ font-family: 'IT'; font-weight: 600; src: url(Inter-600.ttf); }}
@font-face {{ font-family: 'IT'; font-weight: 700; src: url(Inter-700.ttf); }}
@font-face {{ font-family: 'IT'; font-weight: 800; src: url(Inter-800.ttf); }}
@font-face {{ font-family: 'ID'; font-weight: 700; src: url(ID-700.ttf); }}
@font-face {{ font-family: 'ID'; font-weight: 800; src: url(ID-800.ttf); }}
@font-face {{ font-family: 'Instrument Serif'; font-style: italic; src: url(fonts/InstrumentSerif-Italic.ttf); }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
.slide {{ width: 1280px; height: 720px; position: relative; overflow: hidden; background-size: 1280px 720px; page-break-after: always; zoom: 0.9999; }}
.slide:last-child {{ page-break-after: auto; }}
.t {{ position: absolute; white-space: nowrap; font-feature-settings: "kern"; -webkit-font-smoothing: antialiased; }}
.hid {{ position: absolute; left: 0; top: 0; width: 1280px; height: 720px; overflow: hidden; color: transparent; font: 6px 'IT'; }}
.card14 {{ left: 83.6px; top: 283.8px; width: 1110px; height: 230.5px; background: #fefdf8; border-radius: 4px; padding: 14px 22px 0; transform: rotate(-0.58deg); transform-origin: 0 0; }}
.tb14 {{ width: 100%; border-collapse: collapse; font-family: 'IT'; font-weight: 500; font-size: 15px; letter-spacing: -0.03em; color: #192434; }}
.tb14 th {{ background: #ecebe6; font-weight: 700; text-align: left; padding: 6px 10px; border: 1px solid #d4d0c8; }}
.tb14 td {{ padding: 5px 10px; border: 1px solid #d4d0c8; line-height: 17px; }} .tb14 th {{ line-height: 17px; }}
.tb14 .n {{ text-align: right; width: 190px; }}
.tb14 .o {{ color: #a64f10; }}
.tb17 {{ border-collapse: collapse; font-family: 'IT'; font-weight: 500; font-size: 14px; letter-spacing: -0.03em; color: #192434; }}
.tb17 th {{ background: #e5e1db; font-weight: 700; font-size: 15px; text-align: left; padding: 7px 10px; border: 1px solid #bfbcb6; }}
.tb17 td {{ background: #f6f1eb; padding: 4px 10px; border: 1px solid #bfbcb6; line-height: 18px; white-space: normal; }}
.tb17 .c {{ text-align: center; width: 78px; }}
.tb17 .m {{ text-align: right; width: 66px; color: #31587f; }} .tb17 th.m {{ color: #192434; }}
.tb17 .p {{ color: #a64f10; }}
</style></head><body>
{"".join(secs)}
</body></html>'''
open(D+'oic_v3.html', 'w').write(HTML)
print('ok')
