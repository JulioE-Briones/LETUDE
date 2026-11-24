# Lote 5 en estilo pop (US Letter apaisado): Laguna Beach, PURA y Brazosport.
# Uso: python3 gen_us.py  -> escribe <slug>.html en esta carpeta.
import os
A = "../../assets/3d/"
HERE = os.path.dirname(os.path.abspath(__file__))
V = '<span class="vf">verify</span>'

def ic(n, style, cls="i3"):
    return f'<img class="{cls}" src="{A}{n}.png" style="{style}">'

def page(body, foot, cls="pg"):
    return (f'<section class="{cls}"><div class="draftn">Draft · pending validation</div>{body}'
            f'<div class="foot"><span><b>TWO&amp;HUMAN</b> · {foot}</span><span class="pgn"></span></div></section>\n')

def stats(items):
    return '<div class="row c4">' + "".join(f'<div class="card"><div class="big s">{v}</div><div class="lbl">{t}</div></div>' for v, t in items) + "</div>"

def asks(items, cols=4):
    return f'<div class="row c{cols}">' + "".join(
        f'<div class="card{" solid" if solid else ""}"><div class="num"{" style=background:#fff;color:var(--p1)" if solid else ""}>{i+1}</div><h3>{h}</h3><p>{p}</p>' + (f'<span class="chip">{c}</span>' if c else "") + "</div>"
        for i, (h, p, c, solid) in enumerate(items)) + "</div>"

def steps(items):
    return '<div class="steps">' + "".join(f'<div class="card"><img class="ic" src="{A}{n}.png"><h3>{h}</h3><p>{p}</p></div>' for n, h, p in items) + "</div>"

def chips(items, center=True):
    return f'<p style="margin-top:18px{";text-align:center" if center else ""}">' + " ".join(f'<span class="chip">{c}</span>' for c in items) + "</p>"

def minis(items, cols=3):
    return f'<div class="row c{cols}">' + "".join(f'<div class="mini"><h3>{h}</h3><p>{p}</p>' + (f'<span class="chip">{c}</span>' if c else "") + "</div>" for h, p, c in items) + "</div>"

def phases(items):
    return f'<div class="row c{len(items)}">' + "".join(f'<div class="mes"><div class="m">{m}</div><h3>{h}</h3><ul>' + "".join(f"<li>{x}</li>" for x in li) + "</ul></div>" for m, h, li in items) + "</div>"

def opts(items):
    out = '<div class="row c3" style="align-items:start">'
    for nm, pr, unit, pm, li, rec in items:
        out += (f'<div class="opt{" rec" if rec else ""}">' + ('<div class="badge">Recommended</div>' if rec else "") +
                f'<div class="nm">{nm}</div><div class="pr">{pr}<small> {unit}</small></div><div class="pm">{pm}</div><ul>' + "".join(f"<li>{x}</li>" for x in li) + "</ul></div>")
    return out + "</div>"

def qas(items):
    return '<div class="row c2" style="gap:12px">' + "".join(f'<div class="qa"><div class="q">{q}</div><p>{a}</p></div>' for q, a in items) + "</div>"


def brands_page(d, f):
    tiles = "".join(f'<div class="bb"><img src="../../assets/brands/{b}.jpg"><span>{n}<small>{c}</small></span></div>' for b, n, c in d["brands"])
    apps = "".join(f'<span class="chip">{x}</span> ' for x in ["Logo system", "Palette and type", "Signage", "Apparel and merch", "Packaging", "Social templates"])
    return page(f'<div class="kick">05 · Brand presence</div><h2>{d["brand_h"]}</h2>'
                f'<div class="bw"><div class="bgrid">{tiles}</div>'
                f'<div class="card"><h3>Presence, not just a logo</h3><p>{d["brand_side"]}</p><div style="margin-top:6px">{apps}</div></div></div>'
                f'<p class="small" style="margin-top:12px">Concept brands created by TWO&amp;HUMAN to show our art direction and standard of execution. Fictional brands, not client projects.</p>', f)

def build(d):
    f = d["foot"]
    h = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{d["htitle"]}</title>'
         f'<link rel="stylesheet" href="../../assets/pop.css"><link rel="stylesheet" href="../../assets/pop-us.css">'
         f'<style>body{{{d["vars"]}}}{d.get("css","")}</style></head><body>\n')
    # 1 cover
    h += page("".join(ic(n, s) for n, s in d["cover_icons"]) +
              f'<div class="kick">{d["kick"]}</div><h1 style="max-width:6.2in">{d["title"]}</h1><p class="sub" style="max-width:4.9in">{d["sub"]}</p>'
              f'<div class="meta"><div><b>Prepared for</b>{d["for"]}</div><div><b>Prepared by</b>TWO&amp;HUMAN<br>Julio Briones · Mariam Neme</div><div><b>Date</b>{d["date"]}</div></div>',
              f, "pg grad")
    # 2 what we heard
    h += page(ic("magnifier", "width:1.8in;right:0.7in;top:0.5in") +
              f'<div class="kick">01 · What we heard</div><h2>{d["heard_h"]}</h2>' + stats(d["stats"]) +
              f'<div class="row c2" style="margin-top:16px"><div class="card tint"><h3>What you asked for</h3><p>{d["asked"]}</p></div>'
              f'<div class="card solid"><h3>What success looks like</h3><p>{d["success"]}</p></div></div>'
              f'<p class="small" style="margin-top:12px">{d["sources"]}</p>', f)
    # 3 what the RFP really asks
    h += page(ic("target", "width:1.6in;right:0.75in;top:0.45in", "i3 r2") +
              f'<div class="kick">02 · What the RFP really asks</div><h2>{d["asks_h"]}</h2>' + asks(d["asks"], d.get("asks_cols", 4)) +
              f'<div class="card" style="margin-top:16px;padding:14px 20px"><p style="font-size:10pt"><b style="color:var(--ink)">To confirm in discovery:</b> {d["confirm"]}</p></div>', f)
    # 4 solution
    h += page(f'<div class="kick">03 · Our solution</div><h2>{d["sol_h"]}</h2>' + steps(d["steps"]) + chips(d["sol_chips"]), f)
    # 5 concept
    h += page(f'<div class="kick">04 · Preliminary concept</div><h2>{d["concept_h"]}</h2><div class="zm">' + d["concept"] + '</div>' +
              f'<p class="concept">{d["concept_note"]}</p>', f)
    # 5b brand presence
    if d.get("brands"):
        h += brands_page(d, f)
    # 6 scope
    h += page(ic("boxes", "width:1.5in;right:0.75in;top:0.45in", "i3 r1") +
              f'<div class="kick">06 · Scope and deliverables</div><h2>{d["scope_h"]}</h2>' + minis(d["scope"], d.get("scope_cols", 3)) +
              f'<div class="card tint" style="margin-top:14px;padding:12px 18px"><p style="font-size:9.8pt"><b style="color:var(--ink)">Assumptions that protect your budget:</b> {d["assume"]}</p></div>', f)
    # 7 timeline
    h += page(ic("calendar", "width:1.5in;right:0.75in;top:0.45in", "i3 r1") +
              f'<div class="kick">07 · Timeline and success measures</div><h2>{d["time_h"]}</h2>' + phases(d["phases"]) +
              f'<p class="small" style="margin-top:12px">{d["time_note"]}</p>' + chips(d["kpis"], False), f)
    # 8 team + questions
    h += page(f'<div class="kick">08 · Team and the questions you should ask</div><h2>{d["team_h"]}</h2>'
              f'<div style="display:grid;grid-template-columns:3.6in 1fr;gap:20px;align-items:start">'
              f'<div style="display:grid;gap:12px">'
              f'<div class="card who"><div class="face" style="background-image:url(../../assets/img5/julio.jpg)"></div><div><h3 style="margin:0">Julio Briones</h3><p style="font-size:9pt;color:var(--p1);font-weight:700;margin:2px 0 4px">Co-founder · {d["julio_role"]}</p><p style="font-size:9pt">{d["julio_bio"]}</p></div></div>'
              f'<div class="card who"><div class="face" style="background-image:url(../../assets/img5/mariam.jpg)"></div><div><h3 style="margin:0">Mariam Neme</h3><p style="font-size:9pt;color:var(--p1);font-weight:700;margin:2px 0 4px">Co-founder · Software engineer</p><p style="font-size:9pt">{d["mariam_bio"]}</p></div></div>'
              f'<p class="small">Established 2026 · Tucumán, Argentina · remote, in English and Spanish · founder-led: the people in this proposal do the work.</p></div>'
              + qas(d["qa"]) + "</div>", f)
    # 9 investment
    h += page(ic("piggy", "width:1.6in;right:0.7in;top:0.4in", "i3 r2") +
              f'<div class="kick">09 · Investment (USD)</div><h2>{d["inv_h"]}</h2>' + opts(d["opts"]) +
              f'<div class="gar" style="margin-top:16px"><img src="{A}check.png"><div>{d["guarantee"]}</div></div>'
              f'<p class="small" style="margin-top:9px">{d["inv_note"]}</p>', f)
    # 10 compliance + next steps
    rows = "".join(f'<div class="cl"><span>{r}</span><b>{s}</b></div>' for r, s in d["compliance"])
    nxt = "".join(f'<div class="card" style="background:rgba(255,255,255,.14);box-shadow:none;color:#fff;padding:12px 16px;margin-bottom:10px"><div style="font:800 10pt ID">{i+1} · {t}</div><p style="color:rgba(255,255,255,.86);font-size:9.4pt">{p}</p></div>' for i, (t, p) in enumerate(d["next"]))
    h += page(ic("check", "width:1.5in;right:0.8in;top:0.5in", "i3 r2") +
              f'<div class="kick">10 · Compliance and next steps</div><h2 style="color:#fff">{d["close_h"]}</h2>'
              f'<div style="display:grid;grid-template-columns:1.25fr 1fr;gap:26px;align-items:start;max-width:9.2in"><div>{rows}</div><div>{nxt}</div></div>'
              f'<p style="margin-top:16px;font-size:9.6pt;opacity:.92">Julio Briones · julio@twoandhuman.com · +54 381 509 8972 · twoandhuman.com</p>',
              f, "pg grad")
    h += "<script>var p=document.querySelectorAll('.pg');p.forEach(function(e,i){var n=e.querySelector('.pgn');if(n)n.textContent=(i+1)+' / '+p.length;});</script></body></html>"
    open(os.path.join(HERE, d["slug"] + ".html"), "w").write(h)

# ---------- mockups ----------
LAGUNA_CONCEPT = '''<div style="display:grid;grid-template-columns:1.35fr 1fr;gap:22px;align-items:start">
<div class="browser"><div class="bar"><i></i><i></i><i></i><span>lagunabeachcity.net</span></div>
<div style="background:#e8684a;color:#fff;font-size:6.8pt;font-weight:700;padding:4px 12px">Emergency banner · staff can switch it on across the site in seconds</div>
<div class="nav"><b style="color:#0b4f6c">CITY OF LAGUNA BEACH</b><div><span>Residents</span><span>Visitors</span><span>Business</span><span>Government</span><span class="pill" style="background:#e8684a">Report a problem</span></div></div>
<div style="height:1.55in;position:relative;overflow:hidden"><svg viewBox="0 0 700 200" preserveAspectRatio="xMidYMid slice" style="position:absolute;inset:0;width:100%;height:100%"><defs><linearGradient id="hs" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1d7fa3"/><stop offset=".55" stop-color="#f3a27a"/><stop offset=".62" stop-color="#ffd3a8"/></linearGradient></defs><rect width="700" height="200" fill="url(#hs)"/><circle cx="520" cy="122" r="34" fill="#ffe1bd"/><rect y="124" width="700" height="76" fill="#1aa3b8"/><path d="M0 95 C80 80 130 70 190 88 C240 102 260 118 300 124 L0 124Z" fill="#0b4f6c"/><path d="M700 80 C640 90 610 104 570 124 L700 124Z" fill="#0b4f6c"/><g stroke="#fff" stroke-opacity=".45" fill="none"><path d="M0 150 Q50 142 100 150 T200 150 T300 150 T400 150 T500 150 T600 150 T700 150"/></g></svg>
<div style="position:absolute;left:16px;bottom:34px;color:#fff;font:800 19pt/1 ID">Welcome to Laguna Beach</div>
<div style="position:absolute;left:16px;bottom:10px;width:3in;background:#fff;border-radius:14px;font-size:7pt;color:#6b7480;padding:4px 10px">Search services, meetings and documents</div></div>
<div class="tasks"><div><i style="background:#cdeff5"></i>Pay</div><div><i style="background:#cdeff5"></i>Apply</div><div><i style="background:#cdeff5"></i>Report</div><div><i style="background:#cdeff5"></i>Parking</div><div><i style="background:#cdeff5"></i>Meetings</div><div><i style="background:#cdeff5"></i>Alerts</div></div>
<div class="lst" style="padding:2px 14px 12px"><div><span>City Council meeting</span><b style="color:#e8684a">Agenda</b></div><div><span>Beach and marine safety update</span><b style="color:#e8684a">Read</b></div></div></div>
<div class="browser"><div class="bar"><i></i><i></i><i></i><span>Editing · Public Works</span></div>
<div class="ed"><div class="cv"><div style="font:800 12pt ID;margin-bottom:6px">Street sweeping schedule</div><div class="ln" style="width:92%"></div><div class="ln" style="width:80%"></div><div style="height:0.7in;border-radius:8px;background:linear-gradient(135deg,#7fd0dd,#ffd3a8);outline:2px solid #ffb703;outline-offset:2px;margin:8px 0"></div><div class="ln" style="width:70%"></div></div>
<div class="sb"><div style="font:800 8pt ID;margin-bottom:6px">Accessibility check</div><div class="is" style="background:#fff1c2;color:#7a5600"><b>Image needs alt text.</b> Describe the photo.</div><div class="is" style="background:#fff1c2;color:#7a5600"><b>Heading skipped.</b> Use Heading 2.</div><div class="is" style="background:#dcf5e7;color:#1d6b42"><b>Contrast passes.</b></div><div style="background:#c9ced6;color:#fff;border-radius:8px;text-align:center;font-size:7pt;font-weight:700;padding:5px;margin-top:6px">Fix 2 issues to publish</div></div></div></div>
</div>'''

PURA_CONCEPT = '''<div style="display:grid;grid-template-columns:1.3fr 1fr;gap:22px;align-items:start">
<div class="browser"><div class="bar"><i></i><i></i><i></i><span>puebloura.org</span></div>
<div class="nav"><b style="color:#24313c">PUEBLO <span style="color:#d9532b;margin:0">URBAN RENEWAL</span></b><div><span>Projects</span><span>Opportunities</span><span>Records</span><span class="pill" style="background:#2f8fbf">Español</span></div></div>
<div style="display:grid;grid-template-columns:1fr 1.15fr;background:#24313c;color:#fff"><div style="padding:16px 14px"><div style="font:800 16pt/1.02 ID">Renewal you can see.</div><p style="font-size:7.2pt;color:#c9d3da;margin:8px 0 10px">Projects PURA supports, opportunities open today and the record behind every decision.</p><span style="display:inline-block;background:#d9532b;font-size:7pt;font-weight:700;padding:4px 10px;border-radius:12px">See open opportunities</span></div>
<svg viewBox="0 0 360 200" preserveAspectRatio="xMidYMid slice" style="display:block;width:100%;height:100%"><rect width="360" height="200" fill="#1d2832"/><g stroke="#2e3d4a"><path d="M0 40H360M0 80H360M0 120H360M0 160H360M45 0V200M90 0V200M135 0V200M180 0V200M225 0V200M270 0V200M315 0V200"/></g><path d="M-10 170 C60 160 90 120 140 110 C190 100 210 70 250 55 C290 40 320 38 370 30" fill="none" stroke="#2f8fbf" stroke-width="14" stroke-linecap="round"/><g fill="#ff7a4d"><circle cx="140" cy="96" r="7"/><circle cx="200" cy="62" r="7"/><circle cx="252" cy="104" r="7"/><circle cx="96" cy="58" r="7"/><circle cx="300" cy="150" r="7"/></g></svg></div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px;padding:10px 12px 12px">
<div style="border:1px solid #eceef2;border-radius:9px;padding:7px;font-size:6.8pt;color:#5b6670"><b style="display:block;font:800 7.8pt ID;color:#24313c">Central Main St. parcels</b>Request for proposals</div>
<div style="border:1px solid #eceef2;border-radius:9px;padding:7px;font-size:6.8pt;color:#5b6670"><b style="display:block;font:800 7.8pt ID;color:#24313c">LAUNCH grants</b>Up to $25,000</div>
<div style="border:1px solid #eceef2;border-radius:9px;padding:7px;font-size:6.8pt;color:#5b6670"><b style="display:block;font:800 7.8pt ID;color:#24313c">Board meeting</b>Agenda and packet</div></div></div>
<div class="browser"><div class="bar"><i></i><i></i><i></i><span>Dashboard · Add opportunity</span></div>
<div style="padding:12px 14px;font-size:7.2pt">
<div style="font-weight:700;margin-bottom:2px">Title</div><div style="border:1px solid #dfe3ea;border-radius:6px;padding:4px 7px;color:#5b6670;margin-bottom:7px">Central Main Street parcels</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px"><div><div style="font-weight:700;margin-bottom:2px">Type</div><div style="border:1px solid #dfe3ea;border-radius:6px;padding:4px 7px;color:#5b6670">RFP ▾</div></div><div><div style="font-weight:700;margin-bottom:2px">Deadline</div><div style="border:1px solid #dfe3ea;border-radius:6px;padding:4px 7px;color:#5b6670">Date picker</div></div></div>
<div style="font-weight:700;margin:7px 0 2px">Documents</div><div style="border:1px solid #dfe3ea;border-radius:6px;padding:4px 7px;color:#5b6670">RFP.pdf · tagged ✓</div>
<div style="display:flex;gap:6px;justify-content:flex-end;margin-top:10px"><span style="background:#fff1c2;color:#7a5600;border-radius:6px;padding:4px 8px;font-weight:700">1 accessibility note</span><span style="background:#24313c;color:#fff;border-radius:6px;padding:4px 10px;font-weight:700">Publish</span></div></div></div>
</div>'''

BRAZ_CONCEPT = '''<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:18px;align-items:stretch">
<div class="board" style="text-align:center"><div style="font:800 7.6pt IT;letter-spacing:.14em;color:var(--p1);margin-bottom:10px">ROUTE A · INSTITUTIONAL "HORIZON"</div>
<svg width="104" height="104" viewBox="0 0 120 120"><rect width="120" height="120" rx="26" fill="#12306b"/><path d="M24 66 A36 36 0 0 1 96 66 Z" fill="#ffc23d"/><g stroke="#fff" stroke-width="6" stroke-linecap="round" fill="none"><path d="M18 78 C34 72 46 84 60 78 C74 72 86 84 102 78"/><path d="M24 92 C38 87 48 97 60 92 C72 87 82 97 96 92" opacity=".6"/></g></svg>
<div style="font:800 21pt/1 ID;color:#12306b;margin-top:10px;letter-spacing:-.03em">Brazosport</div><div style="font:700 8.6pt IT;letter-spacing:.42em;color:#1f9d6a;margin-top:4px">COLLEGE</div>
<p style="font-size:9.2pt;color:var(--mut);margin-top:10px">A sun rising over the Gulf: a place and a beginning. Works in one color and at small sizes.</p></div>
<div class="board" style="text-align:center;background:#12306b;color:#fff"><div style="font:800 7.6pt IT;letter-spacing:.14em;color:#ffc23d;margin-bottom:8px">ROUTE B · ATHLETICS "GATOR SCALE"</div>
<svg width="112" height="124" viewBox="0 0 170 190"><defs><pattern id="sc" width="20" height="14" patternUnits="userSpaceOnUse"><path d="M0 7 L10 0 L20 7 L10 14 Z" fill="none" stroke="#8fe3b8" stroke-width="1.4" opacity=".55"/></pattern><clipPath id="sh"><path d="M85 6 L160 26 L160 96 C160 140 126 170 85 184 C44 170 10 140 10 96 L10 26 Z"/></clipPath></defs><path d="M85 6 L160 26 L160 96 C160 140 126 170 85 184 C44 170 10 140 10 96 L10 26 Z" fill="#1f9d6a"/><rect width="170" height="190" fill="url(#sc)" clip-path="url(#sh)"/><path d="M85 6 L160 26 L160 96 C160 140 126 170 85 184 C44 170 10 140 10 96 L10 26 Z" fill="none" stroke="#ffc23d" stroke-width="6"/><text x="85" y="128" text-anchor="middle" font-family="ID" font-weight="800" font-size="110" fill="#fff" transform="skewX(-8) translate(16 0)">G</text></svg>
<div style="font:800 20pt/1 ID;transform:skewX(-8deg);margin-top:6px">GATORS</div>
<p style="font-size:9.2pt;color:#c9d6f2;margin-top:10px">Shield and scale pattern for uniforms, courts and game-day social, in the masterbrand's colors.</p></div>
<div class="board" style="text-align:center"><div style="font:800 7.6pt IT;letter-spacing:.14em;color:var(--p1);margin-bottom:10px">ROUTE C · 60TH "BUILT HERE"</div>
<svg width="150" height="92" viewBox="0 0 250 150"><text x="8" y="128" font-family="ID" font-weight="800" font-size="150" fill="#12306b" letter-spacing="-8">6</text><circle cx="168" cy="76" r="54" fill="none" stroke="#12306b" stroke-width="22"/><path d="M128 84 A40 40 0 0 1 208 84 Z" fill="#ffc23d"/><path d="M132 96 C146 91 156 101 168 96 C180 91 190 101 204 96" stroke="#1f9d6a" stroke-width="5" stroke-linecap="round" fill="none"/></svg>
<div style="font:800 13pt ID;color:#12306b;margin-top:8px">Built here. For sixty years.</div><div style="font:700 7.4pt IT;letter-spacing:.3em;color:#1f9d6a;margin-top:4px">SINCE 1968</div>
<p style="font-size:9.2pt;color:var(--mut);margin-top:10px">A year-long campaign told by the alumni, employers and students the College built.</p></div>
</div>'''

COMMON_QA_PAY = ("Contracts, insurance and payments?", "Invoices in U.S. dollars, IRS Form W-8BEN-E as a foreign vendor, and certificates of insurance as required " + V + ".")

CLIENTS = [
dict(slug="laguna", brands=[('serena-ritual', 'Serena Ritual', 'Spa and wellness'), ('atelier-lorenzo', 'Atelier Lorenzo', 'Leather atelier'), ('traza', 'TRAZA', 'Urban accessories'), ('ayven', 'AYVEN', 'Performance apparel'), ('paleta-loca', 'Paleta Loca', 'Ice cream'), ('el-taco-club', 'El Taco Club', 'Restaurant')], brand_h='Laguna has a strong identity. <span class="mk">We design at that level.</span>', brand_side="We design every touchpoint a brand needs. For Laguna, that same standard shapes the website\'s visual system: color, type, photography and templates every department can use.",
  htitle="Many Departments, One Laguna — TWO&HUMAN", foot="City of Laguna Beach · CM-26-013 · Draft pending validation",
 vars="--bg:#f0fafb;--ink:#0f2a36;--mut:#4f6670;--p1:#0b8aa8;--p2:#ff7a59;--t1:#d9f2f6;--hl:#ffd4c4;--hl2:#ffc94d;--b1:#bdebf2;--b2:#ffe0d3;--g1:#0b6f9c;--g2:#19b6c9;--g3:#ff9a76;",
 kick="Proposal · RFP CM-26-013 · Website Redesign and Replacement",
 cover_icons=[("target","width:3in;right:0.6in;top:0.9in"),("calendar","width:1.6in;right:2.9in;top:5.1in"),("check","width:1.3in;right:0.8in;top:5.3in")],
 title='Many departments, <span class="mk">one Laguna.</span>',
 sub="A distinctive, accessible city website where every department publishes with confidence, launched before April 30, 2027.",
 **{"for": "City of Laguna Beach<br>City Manager's Office · Attn. Louie Lacasella"}, date="December 2026",
 heard_h='A small city with a <span class="mk">very big audience.</span>',
 stats=[("~23,000","residents, per the City's website"),("~6 million","visitors a year, by the City's own count"),("Apr 30","2027 launch deadline in the RFP"),("2.1 AA","WCAG level, with automated accessibility checks")],
 asked="Redesign and replace the City's website, let each department edit its own content, meet WCAG 2.1 AA with automated checks, and launch before April 30, 2027.",
 success="Residents and visitors finish their task in a few clicks, every department publishes on its own, and accessibility still holds on an ordinary Tuesday six months after launch.",
 sources="Sources: RFP CM-26-013 notice; lagunabeachcity.net (About Laguna Beach). Audience priorities are confirmed with staff and analytics in discovery.",
 asks_h='Four requirements, <span class="mk">and what each really means.</span>',
 asks=[("Redesign and replace","A new platform, a clean move of the content worth keeping, no broken links.","Inventory + redirect map",False),
       ("Departmental editing","Many editors with different skills. Without guardrails, pages drift within months.","Roles, locked patterns, approvals",False),
       ("WCAG 2.1 AA, automated","Every new page and PDF must keep the standard, not just launch day.","Checker inside the editor",False),
       ("Launch before Apr 30","A fixed public date with approvals and holidays on the way.","Launch Apr 16, 2 weeks early",True)],
 confirm="current platform and hosting " + V + " · number of pages and documents to migrate " + V + " · integrations with payments, permits and agendas " + V,
 sol_h='The Laguna Publishing System: <span class="mk">four parts, one website.</span>',
 steps=[("magnifier","Task-first architecture","Built around what residents and visitors come to do."),("megaphone","Departments publish","Roles, locked patterns and an approval step."),
        ("check","Accessibility built in","An open-source checker in the editor, plus monthly scans."),("growth","Monitor and improve","Analytics and scan reports that keep it right.")],
 sol_chips=["Design system with Laguna's character","Open-source WordPress","No platform license fees","The City owns everything"],
 concept_h='A homepage for both audiences, <span class="mk">an editor that prevents errors.</span>',
 concept=LAGUNA_CONCEPT,
 concept_note="Preliminary concept prepared for this proposal, not an official City design. Final work follows the City's brand standards and approved content.",
 scope_h='Everything to launch, <span class="mk">and to keep it right.</span>',
 scope=[("Discovery","Kickoff, department interviews, analytics review and content inventory.","Approved inventory"),
        ("Architecture","Task-first sitemap, navigation, content model and department roles.","Approved sitemap"),
        ("Design","Clickable homepage prototype in week 4, design system and page templates.","Milestone 1"),
        ("Build","WordPress with roles, approvals, search, calendars, alerts and the accessibility checker.","Milestone 2"),
        ("Migration","Approved pages and documents moved, with a tested 301 redirect map.","Content sign-off"),
        ("Quality and launch","WCAG 2.1 AA report, device testing, role-based training, 60-day stabilization.","Milestone 3")],
 assume="up to 300 approved pages (confirmed by the inventory) · up to 12 page templates · two revision rounds per design deliverable · anything outside scope quoted in writing before work starts.",
 time_h='Fourteen weeks to launch, <span class="mk">two weeks of margin.</span>',
 phases=[("Jan 11 – Feb 5","Discover and prototype",["Inventory and interviews","Sitemap and roles","Clickable prototype, week 4"]),
         ("Feb – Mar","Design and build",["Design system · Milestone 1","WordPress build and checker","Staging review · Milestone 2"]),
         ("Mar – Apr","Migrate, test, train",["Content and redirects","WCAG 2.1 AA testing","Training by role"]),
         ("Apr 16, 2027","Launch",["Milestone 3","60-day stabilization","Monthly scans start"])],
 time_note="Assumes award by early January 2027 " + V + ". City reviews within 5 business days; launch only moves if content or approvals arrive later.",
 kpis=["Zero critical errors in automated scans at launch","Top tasks in three clicks or fewer","Every department publishing within 30 days","Every changed address redirected"],
 team_h='Founder-led, <span class="mk">and ready for hard questions.</span>',
 julio_role="Strategy and project lead", julio_bio="Single point of contact. Coordinates deliverables, revisions and QA for international B2B and B2C marketing clients, including a consolidated audit of 13 accounts.",
 mariam_bio="Leads WordPress development, accessibility, integrations, hosting and security, and the documentation the City keeps.",
 qa=[("Can a team outside the U.S. keep a City deadline?","Argentina is 5 hours ahead of Pacific Time, so our afternoon covers your morning. Weekly written status, and launch is planned two weeks early."),
     ("What evidence do we have before we sign?","The concepts in this proposal, a working session with your team and a clickable prototype in week 4. Payments follow approved milestones."),
     ("Will we be locked in?","No. Standard open-source WordPress, no proprietary builder and no platform license. Domain, code and content belong to the City."),
     COMMON_QA_PAY],
 inv_h='One fixed build price, <span class="mk">three ways to care for it.</span>',
 opts=[("Launch","$18,500","one time","City-provided hosting",["Design, build and migration","WCAG 2.1 AA test report","Training by role","60-day stabilization"],False),
       ("Launch + Care","$300","/month","+ $18,500 fixed build",["Everything in Launch","Managed U.S. hosting","Updates, backups, security","Monthly accessibility scan","Up to 3 hours of changes"],True),
       ("Launch + Care + Evolve","$650","/month","+ $18,500 fixed build",["Everything in Care","Quarterly UX and content review","Up to 8 hours of changes","Editor refreshers twice a year"],False)],
 guarantee="<b>Accessibility guarantee.</b> Zero critical errors in automated WCAG 2.1 AA scans at launch, and anything flagged in the first 60 days is fixed at no cost.",
 inv_note="Build: discovery 2,200 · architecture 1,800 · design 4,200 · build 5,400 · migration 2,600 · QA, training and launch 2,300. 3-year cost: $18,500 + City hosting · $29,300 · $41,900. Payments 30/40/30 on approved milestones · care cancellable with 60 days' notice · third-party costs at cost · valid 90 days · also entered in the City's price format " + V + ".",
 close_h='Ready for the questions, <span class="mk">ready for January.</span>',
 compliance=[("Website redesign and replacement","Yes"),("Decentralized departmental editing","Yes"),("WCAG 2.1 AA","Yes"),("Automated accessibility checks","Yes"),("Launch before April 30, 2027","Yes · Apr 16"),("Training and documentation","Included"),("Official forms and criteria","Mapped " + V),("Insurance","As required " + V)],
 next=[("Questions","We answer any clarification in writing."),("Working session","A video walk-through of the concepts and plan."),("Kickoff · January 11","Prototype in week 4.")]),

dict(slug="pura", brands=[('serena-ritual', 'Serena Ritual', 'Spa and wellness'), ('atelier-lorenzo', 'Atelier Lorenzo', 'Leather atelier'), ('traza', 'TRAZA', 'Urban accessories'), ('ayven', 'AYVEN', 'Performance apparel'), ('paleta-loca', 'Paleta Loca', 'Ice cream'), ('el-taco-club', 'El Taco Club', 'Restaurant')], brand_h='Every client gets <span class="mk">a brand world, not just a logo.</span>', brand_side="We design every touchpoint a brand needs. For PURA, that standard gives the new website a clear, confident public face that matches the scale of what renewal builds.",
  htitle="Renewal You Can See — TWO&HUMAN", foot="Pueblo Urban Renewal Authority · Website RFP · Draft pending validation",
 vars="--bg:#fff6f1;--ink:#1f2a33;--mut:#5b6670;--p1:#d9532b;--p2:#2f8fbf;--t1:#ffe3d8;--hl:#ffd6a8;--hl2:#ffc94d;--b1:#ffd7c7;--b2:#cbe9f7;--g1:#c9472a;--g2:#ff8a4c;--g3:#2f8fbf;",
 kick="Proposal · Website Redevelopment, Hosting and Maintenance",
 cover_icons=[("growth","width:3.2in;right:0.5in;top:1.1in"),("megaphone","width:1.8in;right:2.9in;top:5.1in"),("check","width:1.3in;right:0.8in;top:5.3in")],
 title='Renewal <span class="mk">you can see.</span>',
 sub="A public website that shows Pueblo where renewal is happening, what it delivers and how to take part, and that staff can update without a programmer.",
 **{"for": "Pueblo Urban Renewal Authority<br>Attn. Shawn Carlson"}, date="November 2026",
 heard_h='Renewal is built in public. <span class="mk">The website should show it.</span>',
 stats=[("17","urban renewal areas administered by PURA"),("$25,000","maximum LAUNCH grant in 2026"),("52,000 sq ft","convention center expansion owned by PURA"),("48%","of Pueblo residents are Hispanic or Latino")],
 asked="Redevelop the website, host and maintain it, meet WCAG 2.1 AA, and let staff update content without specialized programming.",
 success="A resident, a developer and a reporter each find what they came for in under a minute, and staff post a meeting or opportunity in five minutes.",
 sources="Sources: PURA RFP; PURA release on LAUNCH grants (July 2026); ENR on the convention center expansion; U.S. Census QuickFacts (2019–2023) for Pueblo city.",
 asks_h='Four requirements, <span class="mk">and what each really means.</span>',
 asks=[("Redevelopment","A structure built around projects, opportunities and records, with the content worth keeping moved cleanly.","Project map + 4 building blocks",False),
       ("Hosting and maintenance","One accountable team after launch: uptime, security, updates and backups.","U.S. hosting + monthly care",False),
       ("WCAG 2.1 AA","Every page and every PDF staff add later, not only launch day.","Accessible templates + scans",False),
       ("No programming needed","A small team must post in minutes, with no developer in the loop.","Simple forms per content type",True)],
 confirm="current platform and hosting " + V + " · number of pages and documents to migrate " + V + " · posting or retention rules for board records " + V,
 sol_h='Four building blocks, <span class="mk">one public face for renewal.</span>',
 steps=[("target","Project map and pages","Every renewal area and project, with status, photos and documents."),("megaphone","Opportunities hub","RFPs, LAUNCH grants and sites, with deadlines and how to apply."),
        ("boxes","Public records center","Agendas, minutes, budgets and plans, searchable by year."),("check","Accessible CMS, cared for","Simple forms, U.S. hosting and monthly care.")],
 sol_chips=["English and Spanish key pages","Opportunities close automatically","Staff publish in 5 minutes","PURA owns everything"],
 concept_h='A homepage that shows renewal, <span class="mk">a form staff can use.</span>',
 concept=PURA_CONCEPT,
 concept_note="Preliminary concept prepared for this proposal, not an official PURA design. Map and content are illustrative; programs shown are public PURA programs.",
 scope_h='Everything to launch, <span class="mk">host and maintain it.</span>',
 scope=[("Discovery","Kickoff, staff and board interviews, analytics review and content inventory.","Approved inventory"),
        ("Architecture and design","Sitemap, content model and a clickable prototype in week 3.","Milestone 1"),
        ("Build","Staff forms, project map, opportunities hub, records center and search.","Milestone 2"),
        ("Spanish pages","Five key pages written by native speakers, chosen with staff and analytics.","Included"),
        ("Quality and launch","WCAG 2.1 AA report, device testing, staff training and guide.","Milestone 3"),
        ("Hosting and care","U.S. hosting, updates, backups, uptime and monthly accessibility scans.","Monthly")],
 assume="up to 60 approved pages (confirmed by the inventory) · up to 8 templates · two revision rounds per design deliverable · anything outside scope quoted in writing before work starts.",
 time_h='Ten weeks to launch, <span class="mk">a prototype in week three.</span>',
 phases=[("Weeks 1–3","Discover and prototype",["Inventory and interviews","Sitemap and content model","Clickable prototype"]),
         ("Weeks 4–7","Design and build",["Design system · Milestone 1","Map, hub, records, forms","Staging · Milestone 2"]),
         ("Weeks 8–10","Migrate, test, launch",["Content, redirects, Spanish pages","WCAG 2.1 AA testing, training","Launch · Milestone 3"])],
 time_note="Kickoff targeted for January 11, 2027 if PURA awards in December " + V + ", which puts launch the week of March 15, 2027.",
 kpis=["Staff publish in 5 minutes or less","Zero critical errors at launch","99.9% monthly uptime","Key items in three clicks or fewer"],
 team_h='Founder-led, <span class="mk">from launch to care.</span>',
 julio_role="Strategy, content and Spanish pages", julio_bio="Single point of contact. Coordinates deliverables, revisions and QA for international B2B and B2C marketing clients. Native Spanish speaker.",
 mariam_bio="Leads WordPress development, the project map, accessibility, hosting, security and the monthly care work.",
 qa=[("Can a team outside the U.S. support us day to day?","Argentina is 4 hours ahead of Mountain Time in winter. Replies within one business day, live hours every weekday, site-down issues acknowledged within 4 hours."),
     ("Where is the site hosted?","Managed hosting in U.S. data centers, with daily backups and security monitoring. Accounts are opened in PURA's name."),
     ("Can we leave if we want to?","Yes. Open-source WordPress, no proprietary builder, care cancellable with 60 days' notice and a full handover package at no cost."),
     COMMON_QA_PAY],
 inv_h='One fixed build price, <span class="mk">care sized to your team.</span>',
 opts=[("Build only","$9,800","one time","PURA arranges hosting",["Design, build and migration","Spanish versions of 5 pages","WCAG 2.1 AA test report","Staff training and guide"],False),
       ("Build + Essential Care","$160","/month","+ $9,800 fixed build",["Everything in Build","Managed U.S. hosting","Updates, backups, security, uptime","Monthly accessibility scan","Up to 1 hour of changes"],True),
       ("Build + Care + Content","$420","/month","+ $9,800 fixed build",["Everything in Essential Care","Up to 5 hours of content updates","We post opportunities and records","Quarterly analytics review"],False)],
 guarantee="<b>Staff independence guarantee.</b> If after training your staff cannot publish a meeting or an opportunity on their own in five minutes, we keep training and adjusting at no cost until they can.",
 inv_note="Build: discovery 1,200 · architecture 900 · design 2,200 · build 3,600 · migration 800 · QA, training and launch 1,100. 3-year cost: $9,800 + PURA hosting · $15,560 · $24,920. Payments 30/40/30 on approved milestones · care cancellable with 60 days' notice · third-party costs at cost · valid 90 days · also entered in PURA's price format " + V + ".",
 close_h='Ready to show Pueblo <span class="mk">what renewal builds.</span>',
 compliance=[("Website redevelopment","Yes"),("Hosting","Yes · U.S. data centers"),("Maintenance","Yes · monthly care"),("WCAG 2.1 AA","Yes"),("Staff updates without programming","Yes"),("Training and documentation","Included"),("Official forms and criteria","Mapped " + V),("Insurance","As required " + V)],
 next=[("Questions","We answer any clarification in writing."),("Working session","A video walk-through of the concepts."),("Kickoff · January 11","Prototype in week 3.")]),

dict(slug="brazosport", brands=[('ayven', 'AYVEN', 'Performance apparel'), ('traza', 'TRAZA', 'Urban accessories'), ('atelier-lorenzo', 'Atelier Lorenzo', 'Leather atelier'), ('paleta-loca', 'Paleta Loca', 'Ice cream'), ('el-taco-club', 'El Taco Club', 'Restaurant'), ('serena-ritual', 'Serena Ritual', 'Spa and wellness')], brand_h='The brand presence we build: <span class="mk">a world, not just a logo.</span>', brand_side="This is the level of application we deliver: signage, apparel, merchandise, packaging and social. For Brazosport, it applies to the College, the Gators and the 60th anniversary, as one family.",
  htitle="Sixty Years, One Brazosport — TWO&HUMAN", foot="Brazosport College · RFP 2026.07 · Draft pending validation",
 vars="--bg:#f3f6ff;--ink:#12213d;--mut:#55607a;--p1:#1f4fd1;--p2:#1f9d6a;--t1:#e2e9ff;--hl:#ffe08a;--hl2:#ffc23d;--b1:#cfdbff;--b2:#cdf1df;--g1:#12306b;--g2:#1f9d6a;--g3:#ffc23d;",
 kick="Proposal · RFP 2026.07 · Brand Identity Services",
 cover_icons=[("megaphone","width:3.1in;right:0.5in;top:1.1in"),("target","width:1.6in;right:2.9in;top:5.1in"),("check","width:1.3in;right:0.8in;top:5.3in")],
 title='Sixty years, <span class="mk">one Brazosport.</span>',
 sub="One brand family for the College, its Gators and its 60th anniversary, built from what students, staff and the community already believe.",
 **{"for": "Brazosport College · Purchasing<br>Attn. Cara Green, MBA"}, date="December 2026",
 heard_h='A once-in-a-generation moment <span class="mk">to say who Brazosport is.</span>',
 stats=[("1968","year founded, per the College's 2019 RFQ " + V),("60","years to celebrate, with a year-long campaign"),("3","identities to unify: College, Gators, anniversary"),("2027","Gators baseball targeted for spring " + V)],
 asked="Brand identity services covering the institutional brand, an athletics identity for the Gators and a campaign for the College's 60th anniversary.",
 success="Six months after launch, a flyer from any department looks like Brazosport without a call to Marketing, and the Gators marks are on uniforms and game-day posts.",
 sources="Sources: RFP 2026.07 notice on IonWave; Brazosport College 2019 RFQ; public athletics listings (to confirm with the College).",
 asks_h='Three requests, <span class="mk">one risk to avoid.</span>',
 asks=[("Institutional brand","A clear position and a system that works from a diploma to a social post.","Research, platform, system",False),
       ("Athletics identity","Gators marks that energize fans, reproduce on uniforms and still read as Brazosport.","Primary, secondary, wordmarks",False),
       ("60th anniversary","More than a commemorative logo: a year of stories that bring alumni back.","Signature, theme, campaign kit",False),
       ("The risk to avoid","Three good identities that look like three different institutions. We design them as one family from the first sketch.","",True)],
 confirm="current marks and any registered trademarks " + V + " · athletics conference, NJCAA or vendor requirements " + V + " · anniversary dates and events " + V,
 sol_h='Listen first, <span class="mk">then design one family.</span>',
 steps=[("magnifier","Listen","Audit, up to 12 interviews, 2 student sessions and a survey."),("target","Define","Position, promise, voice and messages by audience."),
        ("megaphone","Design","Three routes in week 7, then two refinement rounds."),("check","Deliver and adopt","Guidelines, 25 templates, brand library and training.")],
 sol_chips=["Masterbrand + linked athletics + time-limited 60th","Fonts and photos licensed in the College's name","Every source file","Full ownership"],
 concept_h='Three preliminary routes, <span class="mk">one family.</span>',
 concept=BRAZ_CONCEPT,
 concept_note="Preliminary concepts created for this proposal. Exploratory palette and type, not the College's current standards. Final routes come from the research in weeks 1 to 6.",
 scope_h='What the College receives, <span class="mk">in every format.</span>', scope_cols=4,
 scope=[("Research","Audit, interviews, student sessions, survey and findings report.",""),("Brand platform","Positioning, promise, pillars, voice and key messages.",""),
        ("Institutional identity","Symbol, wordmark, unit lockups, color, type and photo direction.",""),("Athletics identity","Primary and secondary marks, wordmarks, uniform and social uses.",""),
        ("60th anniversary","Signature, theme line, campaign guide, calendar and templates.",""),("Guidelines and files","Brand guidelines and source files: AI, EPS, SVG, PNG.",""),
        ("Templates","Up to 25 editable templates: slides, letterhead, flyers, social, email.",""),("Launch","Internal launch kit and a brand training session.","")],
 assume="three routes in week 7 and one choice · two refinement rounds on the chosen route · fonts and photos licensed in the College's name at cost · anything outside scope quoted in writing before work starts.",
 time_h='Sixteen weeks, <span class="mk">three approvals.</span>',
 phases=[("Weeks 1–4","Discover",["Brand audit","Interviews and student sessions","Findings workshop"]),
         ("Weeks 4–6","Define",["Brand platform","Messages by audience","Milestone 1"]),
         ("Weeks 6–11","Design",["Three routes in week 7","Two refinement rounds","Milestone 2"]),
         ("Weeks 11–16","Develop and deliver",["Athletics and 60th systems","Guidelines and templates","Milestone 3 · training"])],
 time_note="Kickoff targeted for mid-January 2027 " + V + "; final delivery in May 2027 leaves the summer to prepare for fall and the anniversary year.",
 kpis=["Committee approves platform and route","Every department trained or with the launch kit in 60 days","Brand-use review at month 6","Gators marks in use for the first season"],
 team_h='Founder-led, <span class="mk">from research to final file.</span>',
 julio_role="Brand strategy and project lead", julio_bio="Single point of contact. Leads research, the brand platform and the campaign. Coordinates deliverables and QA for international marketing clients.",
 mariam_bio="Leads the digital side of the brand: shared brand library, editable templates, social and web applications, and file production.",
 qa=[("Can a studio outside Texas capture our community?","Only by listening, which is why research comes first. The brand will come from your students, staff and partners, not from us."),
     ("Who owns the marks?","The College. Copyright in all final artwork transfers on final payment, with every source file."),
     ("What about trademark risk?","All marks are original. We run a preliminary conflict search before finalizing; registration is handled by the College's counsel."),
     COMMON_QA_PAY],
 inv_h='Three ways to invest, <span class="mk">one fixed price each.</span>',
 opts=[("Foundation","$11,900","fixed","14 weeks",["Research and brand platform","Institutional identity system","Athletics primary mark","Anniversary signature","Core guidelines, 10 templates"],False),
       ("One Brazosport","$16,800","fixed","16 weeks",["Everything in Foundation, full research","Complete athletics identity","Full 60th campaign","Full guidelines, 25 templates","Launch kit and month-6 review"],True),
       ("One Brazosport + Rollout","$22,800","total","$16,800 + $6,000 for six months",["Everything in One Brazosport","Up to 16 hours a month for six months","New applications and merchandise art","Review of materials before they go out"],False)],
 guarantee="<b>Route guarantee.</b> If the committee does not approve any of the three routes after the two refinement rounds, we develop a fourth route at no cost.",
 inv_note="One Brazosport: research 2,400 · platform 1,800 · institutional 3,600 · athletics 3,400 · 60th campaign 2,400 · guidelines and templates 2,400 · launch 800. Payments 30/40/30 on approved milestones · rollout billed monthly, cancellable with 30 days' notice · fonts, photos and printing at cost · valid 90 days · also entered in the College's price format " + V + ".",
 close_h='Let\'s make the next sixty years <span class="mk">unmistakably Brazosport.</span>',
 compliance=[("Institutional brand identity","Yes"),("Athletics identity","Yes"),("60th-anniversary campaign","Yes"),("Guidelines and source files","Yes"),("Timeline and methodology","Yes"),("Pricing","Yes"),("Official forms via IonWave","On submission " + V),("Insurance","As required " + V)],
 next=[("Questions","We answer any clarification in writing."),("Presentation","A video presentation of the routes."),("Kickoff · mid-January","Research starts in week 1.")]),
]

if __name__ == "__main__":
    for c in CLIENTS:
        build(c)
        print("ok", c["slug"])
