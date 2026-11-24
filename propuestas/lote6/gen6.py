# Lote 6 en estilo pop: ESVBA (US Letter), UNDP Jordan CCEC y UNICEF Ghana AGOO (A4).
# Cada propuesta sale en dos archivos: técnica (<slug>.html) y económica (<slug>-financial.html).
# Uso: python3 gen6.py
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "../lote5/v2"))
import gen_us as G
from gen_us import V, page, ic, spark, P

A4 = "@page{size:297mm 210mm;margin:0}.pg{width:297mm;height:210mm}"
TABLE = (".ft2{width:100%;border-collapse:separate;border-spacing:0;background:#fff;border-radius:18px;overflow:hidden;box-shadow:0 10px 30px rgba(20,20,60,.08)}"
         ".ft2 th{background:var(--p1);color:#fff;text-align:left;padding:9px 14px;font:700 9pt IT}"
         ".ft2 td{padding:8px 14px;border-bottom:1px solid #eee;font-size:10pt;vertical-align:top}"
         ".ft2 td.r,.ft2 th.r{text-align:right;white-space:nowrap}.ft2 td small{color:var(--mut);display:block;font-size:8.6pt}"
         ".ft2 tr.tot td{font-weight:800;background:var(--t1);border:none}")
AR = "font-family:'DejaVu Sans',sans-serif"

def build_fin(d):
    """Propuesta económica en archivo aparte: portada + tabla de precios + condiciones."""
    G.CUR.clear(); G.CUR.update(d)
    f = d["foot"]
    h = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{d["htitle"]} — Financial</title>'
         f'<link rel="stylesheet" href="../../assets/pop.css"><link rel="stylesheet" href="../../assets/pop-us.css">'
         f'<style>body{{{d["vars"]}}}{d.get("css","")}{TABLE}</style></head><body>\n')
    s1, s2 = d["spark"]
    h += page(ic("money-bag", "width:2.8in;right:0.9in;top:0.9in") + ic("calculator", "width:1.5in;right:0.9in;top:5.3in") +
              spark("sh00", "#ffffff", "0.7in", "left:5.6in;top:0.75in;opacity:.85") +
              f'<div class="kick">{d["fin_kick"]}</div><h1 style="max-width:6.2in">{d["fin_title"]}</h1><p class="sub" style="max-width:5in">{d["fin_sub"]}</p>'
              f'<div class="meta"><div><b>Prepared for</b>{d["for"]}</div><div><b>Prepared by</b>TWO&amp;HUMAN<br>Julio Briones · Mariam Neme</div><div><b>Date</b>{d["date"]}</div></div>',
              f, "pg grad")
    rows = "".join(f'<tr><td><b>{a}</b><small>{b}</small></td><td class="r">{c}</td></tr>' for a, b, c in d["fin_rows"])
    tot = "".join(f'<tr class="tot"><td>{a}</td><td class="r">{c}</td></tr>' for a, c in d["fin_tot"])
    body = (ic("dollar", "width:1.4in;right:0.75in;top:0.4in", "i3 r2") +
            f'<div class="kick">01 · Price (USD)</div><h2>{d["fin_h"]}</h2>'
            f'<table class="ft2"><tr><th>Deliverable</th><th class="r">USD</th></tr>{rows}{tot}</table>')
    if d.get("fin_opts"):
        body += f'<div style="margin-top:14px">{G.opts(d["fin_opts"])}</div>'
    h += page(body, f)
    h += page(ic("tick", "width:1.4in;right:0.75in;top:0.45in", "i3 r2") +
              f'<div class="kick">02 · Terms</div><h2>{d["terms_h"]}</h2>' + G.minis(d["terms"], 3) +
              f'<div class="gar" style="margin-top:16px"><img src="{P("tick")}"><div>{d["guarantee"]}</div></div>', f)
    h += "<script>var p=document.querySelectorAll('.pg');p.forEach(function(e,i){var n=e.querySelector('.pgn');if(n)n.textContent=(i+1)+' / '+p.length;});</script></body></html>"
    open(os.path.join(HERE, d["slug"] + "-financial.html"), "w").write(h)

PUBLIC = [("traza","TRAZA","Urban accessories"),("ayven","AYVEN","Performance apparel"),("atelier-lorenzo","Atelier Lorenzo","Leather atelier"),
          ("paleta-loca","Paleta Loca","Ice cream"),("el-taco-club","El Taco Club","Restaurant"),("serena-ritual","Serena Ritual","Spa and wellness")]
QA_PAY = G.COMMON_QA_PAY

# ---------------- mockups ----------------
ESVBA_CONCEPT = '''<div style="display:grid;grid-template-columns:1.55in 1fr 1.9in;gap:20px;align-items:start">
<div style="background:linear-gradient(170deg,#0b2a5c,#1462e0);border-radius:18px;padding:14px 12px;color:#fff;height:3.9in;position:relative;box-shadow:0 18px 36px rgba(20,20,60,.25)">
<div style="width:0.5in;height:0.5in;border-radius:50%;background:#f3f7ff;margin:0 auto 10px"></div>
<div style="font:700 6.6pt IT;letter-spacing:.16em;color:#7ff0de">DOOR HANGER</div>
<div style="font:800 17pt/1 ID;margin-top:8px;letter-spacing:-.02em">Fiber is coming to your road.</div>
<p style="font-size:7.4pt;color:#cfe0ff;margin-top:8px">Crews will work on your street soon. See dates, ask questions and sign up.</p>
<div style="position:absolute;left:12px;right:12px;bottom:14px;display:flex;gap:8px;align-items:center"><div style="width:0.55in;height:0.55in;background:repeating-linear-gradient(45deg,#fff 0 4px,#0b2a5c 4px 8px);border-radius:6px"></div><div style="font-size:7pt;font-weight:700">Scan to check<br>your address</div></div></div>
<div class="browser"><div class="bar"><i></i><i></i><i></i><span>esvba.com · check my address</span></div>
<div style="padding:16px 18px"><div style="font:800 15pt ID;color:#0b2a5c">Is fiber at my address?</div>
<div style="display:flex;gap:8px;margin:10px 0"><div style="flex:1;border:1px solid #dfe3ea;border-radius:8px;padding:6px 10px;font-size:8pt;color:#6b7480">123 Main St, Exmore</div><div style="background:#1462e0;color:#fff;border-radius:8px;padding:6px 12px;font:800 8pt ID">Check</div></div>
<div style="background:#e3fbf6;border-radius:10px;padding:10px 12px;font-size:8.2pt;color:#0d4d44"><b>Good news.</b> Your road is in the next build phase. We'll text you when crews arrive.</div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:10px;font-size:7.4pt;text-align:center">
<div style="border:1px solid #eceef2;border-radius:8px;padding:8px"><b style="display:block;font:800 10pt ID;color:#1462e0">1</b>Check address</div>
<div style="border:1px solid #eceef2;border-radius:8px;padding:8px"><b style="display:block;font:800 10pt ID;color:#1462e0">2</b>Choose a plan</div>
<div style="border:1px solid #eceef2;border-radius:8px;padding:8px"><b style="display:block;font:800 10pt ID;color:#1462e0">3</b>Get connected</div></div></div></div>
<div class="phone"><div class="scr" style="padding:12px 10px">
<div style="font:800 8pt ID;margin-bottom:8px">ESVBA · build update</div>
<div style="height:1.2in;border-radius:10px;background:linear-gradient(150deg,#00d1b2,#1462e0);position:relative"><div style="position:absolute;left:10px;bottom:8px;color:#fff;font:800 12pt/1.05 ID">This week<br>on the Shore</div></div>
<div style="font-size:7pt;margin:8px 0 4px;color:#516173">Build progress</div>
<div style="height:8px;border-radius:4px;background:#e1ecff"><div style="width:64%;height:100%;border-radius:4px;background:#1462e0"></div></div>
<div style="font-size:7pt;color:#516173;margin-top:8px">Roads finished this week · next roads · how to sign up</div>
<div style="margin-top:10px;background:#1462e0;color:#fff;border-radius:8px;text-align:center;font:800 7.6pt ID;padding:6px">Check my address</div></div></div></div>'''

UNDP_CONCEPT = f'''<div style="display:grid;grid-template-columns:1fr 1.95in;gap:22px;align-items:start">
<div class="browser"><div class="bar"><i></i><i></i><i></i><span>ccec-aqaba · marketplace</span></div>
<div class="nav"><b style="color:#0b5e4a">CCEC · AQABA</b><div><span>Shop</span><span>Makers</span><span>Training</span><span>About</span><span class="pill" style="background:#0f8a6a">English</span><span style="{AR};color:#0b5e4a">العربية</span></div></div>
<div style="background:linear-gradient(120deg,#0b5e4a,#13a37f);color:#fff;padding:16px 16px 14px"><div style="font:800 17pt/1.02 ID">Made in Aqaba. Made to last.</div><p style="font-size:7.4pt;color:#d9f5ea;margin:6px 0 0">Products with a second life, made by the Centre's artisans, trainees and start-ups.</p></div>
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px;padding:10px 12px 12px">
<div style="border:1px solid #eceef2;border-radius:9px;overflow:hidden;font-size:6.8pt"><div style="height:0.62in;background:linear-gradient(135deg,#e8743b,#ffcf9e)"></div><div style="padding:5px 6px"><b style="display:block;font:800 7.4pt ID">Upcycled tote</b>by a CCEC artisan<br><b style="color:#0f8a6a">JD —</b></div></div>
<div style="border:1px solid #eceef2;border-radius:9px;overflow:hidden;font-size:6.8pt"><div style="height:0.62in;background:linear-gradient(135deg,#8a5a3b,#d9b38c)"></div><div style="padding:5px 6px"><b style="display:block;font:800 7.4pt ID">Reclaimed-wood tray</b>by an incubated start-up<br><b style="color:#0f8a6a">JD —</b></div></div>
<div style="border:1px solid #eceef2;border-radius:9px;overflow:hidden;font-size:6.8pt"><div style="height:0.62in;background:linear-gradient(135deg,#1aa0b8,#bfeaf1)"></div><div style="padding:5px 6px"><b style="display:block;font:800 7.4pt ID">Glass candle holder</b>by a trainee<br><b style="color:#0f8a6a">JD —</b></div></div>
<div style="border:1px solid #eceef2;border-radius:9px;overflow:hidden;font-size:6.8pt"><div style="height:0.62in;background:linear-gradient(135deg,#0f8a6a,#b8e6d2)"></div><div style="padding:5px 6px"><b style="display:block;font:800 7.4pt ID">Textile cushion</b>by a CCEC artisan<br><b style="color:#0f8a6a">JD —</b></div></div></div></div>
<div class="phone"><div class="scr" style="padding:12px 10px;direction:rtl;{AR}">
<div style="font-weight:700;font-size:8pt;color:#0b5e4a;margin-bottom:8px">CCEC</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:6px">
<div style="background:#dcf2e8;border-radius:8px;padding:10px 6px;text-align:center;font-size:8pt;font-weight:700;color:#0b5e4a">المنتجات</div>
<div style="background:#ffe6d6;border-radius:8px;padding:10px 6px;text-align:center;font-size:8pt;font-weight:700;color:#8a3d14">الطلبات</div></div>
<div style="height:0.9in;border-radius:10px;background:linear-gradient(150deg,#e8743b,#ffcf9e);margin:8px 0"></div>
<div style="height:7px;border-radius:4px;background:#eceef2;margin-bottom:5px"></div><div style="height:7px;width:70%;border-radius:4px;background:#eceef2;margin-bottom:10px"></div>
<div style="background:#0f8a6a;color:#fff;border-radius:8px;text-align:center;font-size:8pt;font-weight:700;padding:6px">السلة</div>
<div style="direction:ltr;font-family:IT;font-size:6.4pt;color:#6b7480;margin-top:8px;text-align:center">Arabic right-to-left preview</div></div></div></div>'''

AGOO_CONCEPT = '''<div style="display:grid;grid-template-columns:1.8in 1.9in 1fr;gap:22px;align-items:start">
<div style="background:linear-gradient(165deg,#e5533d,#ff9f1c);border-radius:18px;padding:16px 14px;color:#fff;height:3.9in;position:relative;box-shadow:0 18px 36px rgba(20,20,60,.25)">
<div style="font:700 6.6pt IT;letter-spacing:.16em;color:#fff3c4">POSTER · BUS STOP</div>
<div style="font:800 30pt/0.95 ID;margin-top:10px;letter-spacing:-.03em">Agoo!</div>
<p style="font-size:8.4pt;margin-top:8px;color:#fff6e8">Got a question you can't ask out loud?</p>
<div style="position:absolute;left:14px;right:14px;bottom:16px"><div style="font:800 26pt/1 ID">5100</div><div style="font-size:7.4pt;color:#fff3c4">Free on MTN · other networks 054 011 8999</div></div></div>
<div class="phone"><div class="scr" style="background:#1b1b2b;color:#fff;padding:16px 12px;text-align:center">
<div style="font-size:7pt;color:#b9b9cf">Calling…</div><div style="font:800 22pt ID;margin:6px 0 2px">5100</div><div style="font-size:7.4pt;color:#ffd166">AGOO</div>
<div style="text-align:left;margin-top:16px;font-size:7.6pt;line-height:1.7;background:rgba(255,255,255,.07);border-radius:10px;padding:8px 10px">Press 1 · Your body<br>Press 2 · Staying safe<br>Press 3 · Your mind<br>Press 4 · Your language</div>
<div style="margin:16px auto 0;width:0.42in;height:0.42in;border-radius:50%;background:#e5533d"></div></div></div>
<div class="card" style="padding:16px 18px"><div style="font:800 7.6pt IT;letter-spacing:.14em;color:var(--p1)">RADIO SPOT · 30 S</div>
<p style="font-size:9.2pt;margin-top:8px;color:var(--ink)"><b>SFX:</b> knock, knock.<br><b>Youth 1:</b> Agoo!<br><b>Youth 2:</b> Amee! Come in.<br><b>Youth 1:</b> I need to ask something, but not out loud…<br><b>Voice:</b> AGOO answers. Free, private, in your language. Dial 5100 on MTN.</p>
<div style="display:flex;gap:6px;margin-top:10px;flex-wrap:wrap"><span class="chip">Twi</span><span class="chip">Ewe</span><span class="chip">Dagbani</span><span class="chip">English</span><span class="chip">+ AGOO languages</span></div></div></div>'''

CLIENTS = [
dict(slug="esvba", out=HERE, htitle="Every Home Connected — TWO&HUMAN × ESVBA", foot="ESVBA · RFP No. 2026-006 · Draft pending validation",
 vars="--bg:#f1f7ff;--ink:#0d1f33;--mut:#516173;--p1:#1462e0;--p2:#00b5a3;--t1:#e1ecff;--hl:#b7f0e8;--hl2:#ffc24b;--b1:#cfe0ff;--b2:#c9f3ec;--g1:#0b2a5c;--g2:#1462e0;--g3:#00d1b2;",
 icons={"heard":"chat-bubble","asks":"file-text","scope":"cube","time":"calender","inv":"money-bag","close":"tick"}, spark=("#00d1b2","#1462e0"), tex_light="paper", tex_grad="halftone-teal", tapes=[1,3,5], no_inv=True,
 kick="Volume 1 · Technical proposal · RFP No. 2026-006",
 cover_icons=[("megaphone","width:3.1in;right:0.55in;top:1.0in"),("wifi","width:1.6in;right:2.9in;top:5.0in"),("map-pin","width:1.5in;right:0.7in;top:5.2in")],
 title='Every home connected, <span class="mk">every neighbor informed.</span>',
 sub="PR, community awareness and marketing that turn ESVBA's fiber build into sign-ups, support and local pride across the Eastern Shore.",
 **{"for": "Eastern Shore of Virginia Broadband Authority<br>Attn. Robert Bridgham, Executive Director"}, date="December 2026",
 heard_h='A public network, <span class="mk">built for the whole Shore.</span>',
 stats=[("Open access","network serving education, government, healthcare, business and wholesale"),("$8.8M","BEAD award (Aug 2025) to reach about 4,100 more locations"),("Universal","fiber-to-the-home coverage of the Shore is the stated goal"),("Dec 8","proposals due at 2:00 PM EST, via eVA only")],
 asked="Public relations and marketing services under RFP No. 2026-006: branding, community awareness, digital and print campaigns, web optimization and graphic design, for a three-year term with two possible annual renewals " + V + ".",
 success="Residents know when fiber reaches their road and how to sign up, partners and officials hear one clear story, and every campaign is measured by inquiries and sign-ups, not impressions.",
 sources="Sources: RFP No. 2026-006 and Addendum 1 (eVA sourcing project BPM095978, RFx 131042; email from the Executive Director, 17 Nov 2026); Shore Daily News (BEAD award, Aug 2025; universal-coverage plan, Jan 2025); ESVBA's public description of its open-access network.",
 asks_h='Five services, <span class="mk">one story to tell.</span>',
 asks=[("Branding","A consistent voice and look for a public authority that also sells a service.","Refresh + guidelines",False),
       ("Community awareness","Residents need to know what is coming to their road, when, and what to do next.","Road-by-road updates",False),
       ("Digital and print campaigns","Many residents are best reached offline: mailers, door hangers, radio and events.","Print-first where it matters",False),
       ("Web optimization and design","The website is where every campaign lands: address check and sign-up in a few taps.","Measured from day one",True)],
 confirm="evaluation criteria and cost format (Volume 2) " + V + " · answers in Addendum 1 and Addendum 2 " + V + " · eVA registration and any Virginia registration requirements " + V,
 sol_h='The Connected Shore program: <span class="mk">tell it, show it, measure it.</span>',
 steps=[("chat-bubble","One clear story","Messages for residents, businesses, partners and officials."),("paint-kit","A brand that sells service","Refresh, templates and graphic design."),
        ("megaphone","Campaigns on and offline","Digital, print, radio and community events."),("chart","Measured sign-ups","Web optimization and a monthly report.")],
 sol_chips=["Road-by-road construction updates","Print and digital in one calendar","Press releases and media kit","Plain-language, accessible content"],
 concept_h='From a door hanger <span class="mk">to a sign-up in one minute.</span>', concept=ESVBA_CONCEPT,
 concept_note="Preliminary concept prepared for this proposal, not an official ESVBA design. Addresses, phases and the web address are illustrative.",
 brands=PUBLIC, brand_h='Every client gets <span class="mk">a brand world, not just a logo.</span>',
 brand_side="We design every touchpoint a brand needs. For ESVBA, that standard shapes the campaign look: yard signs, door hangers, trucks, social posts and the website.",
 scope_h='Everything the RFP asks, <span class="mk">in one team.</span>',
 scope=[("Brand refresh","Logo review, palette, type, voice and a short brand guide.","Month 1"),("Message framework","Key messages for residents, businesses, partners and officials.","Month 1"),
        ("Community awareness","Road-by-road availability updates, FAQs and event kits.","Ongoing"),("Digital campaigns","Social, email, search and paid social, measured by sign-ups.","Ongoing"),
        ("Print and media","Mailers, door hangers, flyers, press releases and a media kit.","Ongoing"),("Web optimization","Speed, accessibility, address check and the sign-up path, with analytics.","Months 1–2")],
 assume="media buying, printing and postage paid by ESVBA at cost, no markup · two revision rounds per deliverable · monthly hours as listed in each option · anything outside scope quoted in writing before work starts.",
 time_h='Visible results <span class="mk">in the first 30 days.</span>',
 phases=[("Days 1–30","Listen and launch",["Kickoff and stakeholder interviews","Message framework","Quick-win web fixes"]),
         ("Days 31–60","Brand and campaign",["Brand refresh and templates","First awareness campaign","Media kit"]),
         ("Days 61–90","Scale and measure",["Road-by-road updates","First monthly report","Next-quarter plan"]),
         ("Ongoing","Monthly program",["Content calendar","Press and community events","Quarterly review"])],
 time_note="Start date depends on award " + V + ". Campaigns follow ESVBA's construction schedule, so residents are never promised a date before crews are ready.",
 kpis=["Inquiries and sign-ups by campaign","Address checks on the website","Press mentions and event reach","Monthly report to the Executive Director"],
 team_h='Founder-led, <span class="mk">and ready for hard questions.</span>',
 julio_role="Strategy and PR lead", julio_bio="Single point of contact. Coordinates deliverables, revisions and QA for international B2B and B2C marketing clients, including a consolidated audit of 13 accounts.",
 mariam_bio="Leads web optimization, analytics, accessibility and the tools that connect each campaign to sign-ups.",
 qa=[("Can a team outside Virginia run local PR?","Strategy, design, digital and writing work remotely; printing and events use Shore vendors approved by ESVBA. Eastern Time is 2 hours behind us, so we cover your full morning."),
     ("What evidence do we have before we sign?","The concepts in this proposal and a 30-day plan with visible results. Monthly invoices follow approved work."),
     ("Have you worked on broadband before?","Not as an account yet. This plan is built from ESVBA's public record, and the 30-day guarantee in Volume 2 puts the risk on us, not on the Authority."), QA_PAY],
 close_h='Ready to tell <span class="mk">the Shore\'s fiber story.</span>',
 compliance=[("Branding and community awareness","Yes"),("Digital and print campaigns","Yes"),("Web optimization and graphic design","Yes"),("Attachment C · Addenda 1 and 2","With Volume 1 " + V),("eVA registration","Before submission " + V),("Virginia SCC registration","To confirm " + V),("Documented broadband experience","See page 9 " + V),("Insurance","As required " + V)],
 next=[("Submission via eVA","By December 8, 2:00 PM EST."),("Oral presentation","If the Authority invites finalists."),("Kickoff","Visible results in 30 days.")],
 fin_kick="Volume 2 · Cost proposal · RFP No. 2026-006", fin_title='One launch kit, <span class="mk">three monthly levels.</span>',
 fin_sub="Fixed prices in U.S. dollars. Media, printing and postage are paid by ESVBA at cost, with no markup.",
 fin_h='The launch kit, <span class="mk">itemized.</span>',
 fin_rows=[("Discovery and interviews","Kickoff, stakeholder interviews, audit of current materials","1,400"),("Message framework","Messages by audience, FAQ bank, press boilerplate","1,300"),
           ("Brand refresh and guide","Logo review, palette, type, voice, templates","2,400"),("Web quick wins","Speed, accessibility, address check and sign-up path, analytics","1,800")],
 fin_tot=[("Launch kit, one time","6,900")],
 fin_opts=[("Essential","$1,250","/month","+ launch kit",["2 campaigns a quarter","Press releases as needed","Monthly report"],False),
           ("Connected Shore","$1,950","/month","+ launch kit",["Monthly awareness campaign","Social content and paid social","Print design: mailers, door hangers","Web optimization and analytics"],True),
           ("Full program","$2,900","/month","+ launch kit",["Weekly road-by-road updates","Event kits and local media relations","Quarterly creative refresh"],False)],
 terms_h='Clear terms, <span class="mk">no surprises.</span>',
 terms=[("Contract cost","Recommended option: $30,300 in year 1 and $77,100 over the three-year term (36 × $1,950 + $6,900).",""),("Extra work","$60 per hour, quoted in writing before work starts.",""),("Invoicing","Launch kit 50% at kickoff and 50% on delivery; monthly fees in arrears.",""),
        ("Third-party costs","Media, printing, postage and event costs at cost, no markup.",""),("Validity","Prices valid for 90 days from the submission date " + V + ".",""),("Format","Also entered in the RFP's cost form if one is provided " + V + ".","")],
 guarantee="<b>30-day guarantee.</b> If the message framework, the web quick wins and the first campaign are not delivered ready to launch within 30 days of kickoff, the second month is free."),

dict(slug="undp-ccec", out=HERE, htitle="Made in Aqaba — TWO&HUMAN × UNDP Jordan", foot="UNDP Jordan · UNDP-JOR-00757 · Draft pending validation",
 vars="--bg:#f3faf5;--ink:#10261f;--mut:#4f675d;--p1:#0f8a6a;--p2:#e8743b;--t1:#dcf2e8;--hl:#ffd9b8;--hl2:#ffc24b;--b1:#c7ecdc;--b2:#ffe0cc;--g1:#0b5e4a;--g2:#13a37f;--g3:#ffb072;",
 css=A4, icons={"heard":"chat-bubble","asks":"file-text","scope":"cube","time":"calender","close":"tick"}, spark=("#ffb072","#0f8a6a"), tex_light="concrete", tex_grad="halftone-teal", tapes=[4,7,5], no_inv=True,
 kick="Technical proposal · UNDP-JOR-00757",
 cover_icons=[("bag","width:3in;right:0.6in;top:1.0in"),("computer","width:1.6in;right:2.9in;top:5.0in"),("card","width:1.5in;right:0.7in;top:5.2in")],
 title='Made in Aqaba, <span class="mk">found and bought online.</span>',
 sub="A bilingual Arabic and English website and marketplace for the Creative Circular Economy Centre, with hosting and support for 36 months.",
 **{"for": "UNDP Jordan Country Office<br>Creative Circular Economy Centre (CCEC), Aqaba"}, date="November 2026",
 heard_h='A first for Jordan <span class="mk">deserves a first-class storefront.</span>',
 stats=[("5,000+ m²","site for Jordan's first circular economy centre"),("JD 1.2M+","investment led by ASEZA with UNDP and the EU"),("~90,000 t","of waste landfilled in Aqaba each year"),("36 months","of hosting and support requested")],
 asked="Design, develop, implement, host and maintain an integrated digital platform with an e-commerce marketplace to display, promote, order, pay for and sell products made at the Centre and by artisans, trainees and incubated enterprises, using the CCEC branding package.",
 success="Artisans list products in minutes, buyers can find, trust and pay for them, and the Centre's team runs it all in Arabic and English without depending on a developer.",
 sources="Sources: UNDP-JOR-00757 on procurement-notices.undp.org (deadline 1 Dec 2026, 05:00 New York time); Petra News Agency, 11 June 2026 (groundbreaking, site area, investment and waste figures).",
 asks_h='Four things this platform <span class="mk">has to get right.</span>',
 asks=[("Bilingual by design","Arabic right-to-left and English with equal quality, not a translated afterthought.","RTL layouts + bilingual CMS",False),
       ("A real marketplace","Many sellers, one storefront: listings, orders, payouts and commission rules.","Multi-vendor e-commerce",False),
       ("Payments that work locally","Local payment methods and delivery options, with clear terms for buyers.","Gateway confirmed at inception " + V,False),
       ("Built on the CCEC brand","The branding package from the separate assignment, applied consistently everywhere.","",True)],
 confirm="hosting location and data requirements " + V + " · payment gateway and banking setup " + V + " · qualification criteria and required forms in the RFP " + V,
 sol_h='One platform, <span class="mk">four connected parts.</span>',
 steps=[("computer","Institutional website","Programs, training, incubation and the Centre's impact."),("bag","Multi-vendor marketplace","Seller dashboards, orders, payouts and reviews."),
        ("card","Payments and delivery","Local gateway, delivery rules and clear buyer terms."),("chart","Impact dashboard","Sales, sellers and products, ready for UNDP and ASEZA reporting.")],
 sol_chips=["Arabic RTL and English","Open-source stack, no license fees","WCAG 2.1 AA","Training for staff and sellers"],
 concept_h='A storefront for products <span class="mk">with a second life.</span>', concept=UNDP_CONCEPT,
 concept_note="Preliminary concept prepared for this proposal, not an official CCEC or UNDP design. Final work applies the CCEC branding package; products and sellers are illustrative.",
 brands=[PUBLIC[2],PUBLIC[0],PUBLIC[5],PUBLIC[3],PUBLIC[4],PUBLIC[1]], brand_h='The same care <span class="mk">for every maker\'s product.</span>',
 brand_side="We design every touchpoint a brand needs. For the CCEC, that standard shapes how each artisan's product is photographed, described and presented online.",
 scope_h='Everything to launch, <span class="mk">and 36 months of care.</span>',
 scope=[("Inception","Workshops with UNDP, ASEZA and the Centre; requirements, sitemap, seller journey.","Inception report"),("Design","Bilingual UX and UI applying the CCEC brand; clickable prototype.","Prototype"),
        ("Build","Website and multi-vendor marketplace, payments, delivery rules, CMS.","Staging"),("Content and onboarding","Seller onboarding kit, product photo guide, first catalogue loaded.","Pilot sellers"),
        ("Testing and launch","Security, accessibility, load and payment tests; go-live.","Launch"),("36-month care","Hosting, updates, backups, security, support, quarterly improvements.","Monthly")],
 assume="hosting on infrastructure approved by UNDP " + V + " · payment-gateway fees paid by the Centre · Arabic content reviewed by a native-speaking partner approved by UNDP · two revision rounds per deliverable.",
 time_h='Live in 14 weeks, <span class="mk">cared for over 36 months.</span>',
 phases=[("Weeks 1–3","Inception",["Workshops and requirements","Sitemap and seller journey","Inception report"]),("Weeks 4–7","Design",["Bilingual UX and UI","Clickable prototype","Design approval"]),
         ("Weeks 8–12","Build and onboard",["Marketplace and payments","Pilot sellers loaded","Staging review"]),("Week 13 on","Launch and care",["Tests and go-live","Staff and seller training","36 months of care"])],
 time_note="Schedule aligned to the RFP once confirmed " + V + ". Jordan is 6 hours ahead of Argentina; we keep a fixed daily overlap with working hours in Amman and Aqaba.",
 kpis=["Sellers onboarded and active","Orders and sales per month","Page speed and uptime","Staff publishing on their own"],
 team_h='Founder-led, <span class="mk">and ready for hard questions.</span>',
 julio_role="Team leader, strategy and content", julio_bio="Single point of contact for UNDP. Coordinates deliverables, revisions and QA for international marketing clients; works in English and Spanish.",
 mariam_bio="Leads the marketplace build, payments, security, hosting and the 36-month technical care.",
 qa=[("Who handles Arabic?","A native Arabic-speaking content and QA partner, named and approved by UNDP before work starts, reviews every Arabic page and template."),
     ("Can the Centre run it alone?","Yes. Staff and sellers are trained, and the open-source stack has no license fees or vendor lock-in."),
     ("Where is the data hosted?","On infrastructure approved by UNDP and ASEZA, with daily backups and security monitoring " + V + "."),
     ("Who owns the platform?","UNDP and the Centre own domain, code, content and accounts, per UNDP's General Terms and Conditions " + V + ".")],
 close_h='Ready to open <span class="mk">the Centre\'s storefront.</span>',
 compliance=[("Bilingual institutional website","Yes"),("Integrated e-commerce marketplace","Yes"),("Ordering, payment and sales","Yes"),("CCEC branding package applied","Yes"),("Hosting and maintenance, 36 months","Yes"),("Financial proposal","Separate file"),("Qualification criteria and forms","Mapped " + V),("Years in operation and similar projects","As required " + V),("Registration and financial documents","As required " + V)],
 next=[("Submission","Technical and financial files as instructed, before 1 Dec, 05:00 New York time."),("Clarifications","We answer any question in writing."),("Inception","Workshops start in week 1.")],
 fin_kick="Financial proposal · UNDP-JOR-00757", fin_title='One fixed price, <span class="mk">36 months included.</span>',
 fin_sub="All-inclusive lump sum in U.S. dollars, paid against deliverables approved by UNDP.",
 fin_h='Build and care, <span class="mk">itemized.</span>',
 fin_rows=[("Inception","Workshops, requirements, sitemap, seller journey, inception report","2,400"),("Bilingual UX and UI design","Arabic RTL and English, CCEC brand applied, clickable prototype","3,800"),
           ("Website and marketplace development","Multi-vendor e-commerce, CMS, search, seller dashboards","9,600"),("Payments, delivery and integrations","Local gateway, delivery rules, notifications","2,400"),
           ("Arabic content review","Native-speaking partner approved by UNDP","1,500"),("Content, onboarding and training","Seller kit, first catalogue, staff and seller training","1,800"),
           ("Testing and launch","Security, accessibility, load and payment tests","1,200"),("Hosting and care, 36 months","$390 a month: hosting, updates, backups, security, support","14,040")],
 fin_tot=[("Total lump sum","36,740")],
 terms_h='Clear terms, <span class="mk">no surprises.</span>',
 terms=[("Payments","Against approved deliverables: inception, design, staging, launch, then quarterly for care " + V + ".",""),("Exclusions","Payment-gateway transaction fees and paid advertising, if any.",""),
        ("Ceiling","If UNDP publishes a budget ceiling, this price is adjusted to stay within it " + V + ".",""),("Taxes","Per UNDP's tax-exemption terms " + V + ".",""),
        ("Validity","As required in the RFP " + V + ".",""),("Format","Also entered in UNDP's Financial Proposal Form " + V + ".","")],
 guarantee="<b>Launch guarantee.</b> Any defect found in the first 90 days after go-live is fixed at no cost, on top of the 36 months of care."),

dict(slug="unicef-agoo", out=HERE, htitle="Agoo! — TWO&HUMAN × UNICEF Ghana", foot="UNICEF Ghana · LRPS-2026-9207316 · Draft pending validation",
 vars="--bg:#fff7ef;--ink:#2a1a12;--mut:#6b5a4f;--p1:#e5533d;--p2:#1aa0d8;--t1:#ffe6dc;--hl:#ffe08a;--hl2:#ffc23d;--b1:#ffd8c7;--b2:#cdeefb;--g1:#e5533d;--g2:#ff9f1c;--g3:#1aa0d8;",
 css=A4, icons={"heard":"chat-bubble","asks":"file-text","scope":"cube","time":"calender","close":"tick"}, spark=("#ffd166","#1aa0d8"), tex_light="paper", tex_grad="halftone-orange", tapes=[5,3,1], no_inv=True,
 kick="Technical proposal · LRPS-2026-9207316",
 cover_icons=[("phone-ringing","width:3in;right:0.6in;top:1.0in"),("megaphone","width:1.6in;right:2.9in;top:5.0in"),("heart","width:1.4in;right:0.8in;top:5.2in")],
 title='Agoo! <span class="mk">Dial 5100, get the answer.</span>',
 sub="A campaign that puts AGOO's free information in every young person's pocket, designed with young Ghanaians and measured by calls, not impressions.",
 **{"for": "UNICEF Ghana Country Office<br>AGOO platform team"}, date="November 2026",
 heard_h='A platform young Ghanaians <span class="mk">already use.</span>',
 stats=[("2015","launched with Ghana Health Service and MTN Ghana"),("10M+","engagements on AGOO, per Viamo"),("5100","free short code on MTN; 054 011 8999 for other networks"),("6","widely spoken languages at launch")],
 asked="A creative agency to design and lead the implementation of a promotional campaign for the AGOO platform (full scope as defined in the RFP " + V + ").",
 success="More young people, in every region and language, know AGOO, dial it and come back, and UNICEF can see which messages and channels drove the calls.",
 sources="Sources: UNGM notice LRPS-2026-9207316 (published 13 Nov 2026, deadline 4 Dec 2026); UNICEF Innovation, \"Agoo: An Interactive Mobile Platform\"; Viamo, \"UNICEF Agoo 5100 reaches 10 million engagements\"; UNICEF Ghana stories on AGOO.",
 asks_h='What a campaign for AGOO <span class="mk">has to get right.</span>',
 asks=[("Reach beyond smartphones","AGOO works on any phone, so the campaign must too: radio, outdoor, schools, SMS and community voices.","Offline-first media mix",False),
       ("Speak youth, in local languages","Messages co-created with young people, in the languages AGOO serves.","Youth co-creation sessions",False),
       ("Protect children","Every image and story follows UNICEF's child safeguarding and ethical reporting rules.","Safeguarding built in",False),
       ("Drive calls, not likes","Success is measured in calls to 5100 and returning callers.","Tracked by channel",True)],
 confirm="eligibility for firms registered outside Ghana " + V + " · media budget and who buys it " + V + " · campaign regions, languages and dates " + V,
 sol_h='Listen, create, launch, learn: <span class="mk">a campaign young people shape.</span>',
 steps=[("chat-bubble","Listen","Youth sessions and AGOO data to find what young people ask."),("paint-kit","Create","Concept, key visual, radio and social assets in local languages."),
        ("megaphone","Launch","Radio, outdoor, schools, SMS and creators, with local partners."),("chart","Learn","Calls by channel and region, fed back into the next wave.")],
 sol_chips=["Works on any phone","Local languages","Child safeguarding","Measured in calls"],
 concept_h='"Agoo!" <span class="mk">The knock that brings answers.</span>', concept=AGOO_CONCEPT,
 concept_note="Preliminary concept prepared for this proposal, not official UNICEF or AGOO material. Final creative is co-created with young people, tested in each language and approved by UNICEF; menu options and languages are illustrative.",
 brands=[PUBLIC[3],PUBLIC[4],PUBLIC[0],PUBLIC[1],PUBLIC[5],PUBLIC[2]], brand_h='Creative people <span class="mk">want to look at.</span>',
 brand_side="We design every touchpoint of a brand. For AGOO, that standard means a campaign young people recognise on a bus stop, a radio jingle and a school wall.",
 scope_h='Design it, then <span class="mk">lead it on the ground.</span>',
 scope=[("Insight","Desk review, AGOO data and youth co-creation sessions.","Insight brief"),("Concept","Campaign idea, key visual and taglines tested with young people.","Concept approval"),
        ("Production","Radio spots, posters, social, SMS and school kits in local languages.","Asset library"),("Launch","Media and activation plan with local partners approved by UNICEF.","Launch plan"),
        ("Lead implementation","Weekly coordination, creator partnerships and content calendar.","Weekly reports"),("Evaluation","Calls by channel and region, lessons and a next-wave plan.","Final report")],
 assume="media buying, printing and field activations paid at cost through partners approved by UNICEF " + V + " · translations by native speakers · two revision rounds per deliverable · safeguarding consent for every participant.",
 time_h='Insight in week 3, <span class="mk">on air by week 8.</span>',
 phases=[("Weeks 1–3","Insight",["Desk review and AGOO data","Youth co-creation sessions","Insight brief"]),("Weeks 4–6","Concept and production",["Concept tested with youth","Key visual and scripts","Asset library"]),
         ("Weeks 7–8","Launch",["Media and partners booked","Launch wave","Daily monitoring"]),("Weeks 9–16","Run, learn, report",["Weekly optimization","Mid-term review","Final report"])],
 time_note="Schedule aligned to the RFP once confirmed " + V + ". Ghana is 3 hours ahead of Argentina; we cover the full Accra morning.",
 kpis=["Calls to 5100 and the long number","Returning callers","Reach by region and language","Cost per call by channel"],
 team_h='Founder-led, <span class="mk">and ready for hard questions.</span>',
 julio_role="Team leader and creative strategy", julio_bio="Single point of contact. Leads strategy, concept and campaign management; coordinates deliverables and QA for international marketing clients.",
 mariam_bio="Leads data and measurement: call tracking by channel, dashboards and the digital assets.",
 qa=[("Can a team outside Ghana lead this?","Strategy, creative and campaign management run remotely; field production and activations go through Ghanaian partners approved by UNICEF " + V + "."),
     ("How do you keep children safe?","Consent, safeguarding and ethical reporting rules apply to every session, photo and story, and UNICEF approves each asset."),
     ("How will we know it worked?","Calls and returning callers by channel and region, reported weekly, not just reach."),
     ("Who owns the creative?","UNICEF, per its General Terms and Conditions " + V + ".")],
 close_h='Ready to make AGOO <span class="mk">the number everyone knows.</span>',
 compliance=[("Campaign design","Yes"),("Lead implementation","Yes · with local partners"),("Creative production","Yes"),("Monitoring and reporting","Yes"),("Child safeguarding","Yes"),("Financial proposal","Separate file"),("Eligibility, firms outside Ghana","To confirm " + V),("Forms and registration","As required " + V)],
 next=[("Submission","As instructed in the RFP, before 4 Dec 2026."),("Clarifications","We answer any question in writing."),("Insight","Youth sessions start in week 1.")],
 fin_kick="Financial proposal · LRPS-2026-9207316", fin_title='One fixed fee, <span class="mk">media at cost.</span>',
 fin_sub="Fixed agency fee in U.S. dollars. Media, printing and field activations are paid at cost through partners approved by UNICEF.",
 fin_h='Agency fee, <span class="mk">itemized.</span>',
 fin_rows=[("Insight","Desk review, AGOO data analysis, youth co-creation sessions, insight brief","3,200"),("Concept and testing","Campaign idea, key visual, taglines, testing with young people","3,800"),
           ("Production","Radio spots, posters, social, SMS and school kits; native-speaker translations","6,400"),("Launch planning","Media and activation plan, partner briefing and onboarding","2,400"),
           ("Lead implementation, 8 weeks","Weekly coordination, creators, content calendar, optimization","4,000"),("Evaluation","Calls by channel and region, final report, next-wave plan","1,200")],
 fin_tot=[("Total agency fee","21,000")],
 terms_h='Clear terms, <span class="mk">no surprises.</span>',
 terms=[("Payments","Against approved deliverables: insight, concept, asset library, launch, final report " + V + ".",""),("Not included","Media buying, printing, field activations and talent fees, at cost with no markup.",""),
        ("Ceiling","If UNICEF publishes a budget ceiling, this fee is adjusted to stay within it " + V + ".",""),("Taxes","Per UNICEF's tax-exemption terms " + V + ".",""),
        ("Validity","As required in the RFP " + V + ".",""),("Format","Also entered in UNICEF's price schedule " + V + ".","")],
 guarantee="<b>Concept guarantee.</b> If the concept does not pass the youth testing sessions, we develop a new one at no cost before production starts."),
]

if __name__ == "__main__":
    for c in CLIENTS:
        G.build(c); build_fin(c)
        for fn in (c["slug"] + ".html", c["slug"] + "-financial.html"):   # lote6 está un nivel más arriba que lote5/v2
            fp = os.path.join(HERE, fn); t = open(fp).read().replace("../../assets/", "../assets/"); open(fp, "w").write(t)
        print("ok", c["slug"])
