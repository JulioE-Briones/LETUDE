# Lote 8 en estilo pop (A4 apaisado): UK Sport DIG0911.
# Uso: python3 gen8.py  -> escribe <slug>.html en esta carpeta.
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "../lote5/v2"))
import gen_us as G

A4 = "@page{size:297mm 210mm;margin:0}.pg{width:297mm;height:210mm}"
PUBLIC = [("traza","TRAZA","Urban accessories"),("ayven","AYVEN","Performance apparel"),("atelier-lorenzo","Atelier Lorenzo","Leather atelier"),
          ("paleta-loca","Paleta Loca","Ice cream"),("el-taco-club","El Taco Club","Restaurant"),("serena-ritual","Serena Ritual","Spa and wellness")]

UKS_CONCEPT = '''<div style="display:grid;grid-template-columns:1.3fr 1fr;gap:22px;align-items:start">
<div class="browser"><div class="bar"><i></i><i></i><i></i><span>uksport.gov.uk</span></div>
<div class="nav"><b style="color:#0b1640">UK SPORT</b><div><span>Investment</span><span>Athletes</span><span>Events</span><span>About</span><span class="pill" style="background:#e11d48">News</span></div></div>
<div style="background:linear-gradient(120deg,#0b1640,#2440d8);color:#fff;padding:18px 16px 16px;position:relative;overflow:hidden">
<div style="position:absolute;right:-30px;top:-30px;width:150px;height:150px;border-radius:50%;background:radial-gradient(circle,#e11d48,transparent 70%);opacity:.6"></div>
<div style="font:700 7pt IT;letter-spacing:.16em;color:#ffb3c4">LA 2028 · ALPES 2030</div>
<div style="font:800 18pt/1.02 ID;margin-top:6px">Powering the next<br>medal moment.</div>
<p style="font-size:7.4pt;color:#d6dcff;margin:6px 0 0">How National Lottery and Exchequer investment turns into performance.</p></div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px;padding:10px 12px 12px">
<div style="border:1px solid #eceef2;border-radius:9px;padding:8px;font-size:7pt"><b style="display:block;font:800 8.2pt ID;color:#0b1640">Investment explorer</b>Awards by sport and cycle<br><span style="color:#2440d8;font-weight:700">Explore →</span></div>
<div style="border:1px solid #eceef2;border-radius:9px;padding:8px;font-size:7pt"><b style="display:block;font:800 8.2pt ID;color:#0b1640">Athlete stories</b>Olympic and Paralympic<br><span style="color:#2440d8;font-weight:700">Read →</span></div>
<div style="border:1px solid #eceef2;border-radius:9px;padding:8px;font-size:7pt"><b style="display:block;font:800 8.2pt ID;color:#0b1640">Major events</b>Hosting in the UK<br><span style="color:#2440d8;font-weight:700">See events →</span></div></div></div>
<div class="browser"><div class="bar"><i></i><i></i><i></i><span>Headless CMS · Athlete story</span></div>
<div style="padding:12px 14px;font-size:7.4pt">
<div style="display:grid;gap:6px">
<div style="border:1px solid #dfe3ea;border-radius:8px;padding:6px 8px"><b style="color:#2440d8">Hero</b> · image, headline, sport tag</div>
<div style="border:1px solid #dfe3ea;border-radius:8px;padding:6px 8px"><b style="color:#2440d8">Story body</b> · rich text, pull quote</div>
<div style="border:1px solid #dfe3ea;border-radius:8px;padding:6px 8px"><b style="color:#2440d8">Funding block</b> · linked award, cycle</div>
<div style="border:1px dashed #c9cfdb;border-radius:8px;padding:6px 8px;color:#6b7480">+ Add component</div></div>
<div style="display:flex;gap:6px;margin-top:10px"><span style="background:#dcf5e7;color:#1d6b42;border-radius:6px;padding:3px 7px;font-weight:700">Performance 95+</span><span style="background:#dcf5e7;color:#1d6b42;border-radius:6px;padding:3px 7px;font-weight:700">Accessibility 100</span></div>
<div style="display:flex;gap:6px;justify-content:flex-end;margin-top:10px"><span style="border:1px solid #c9cfdb;border-radius:6px;padding:4px 10px;font-weight:700">Preview</span><span style="background:#0b1640;color:#fff;border-radius:6px;padding:4px 10px;font-weight:700">Publish</span></div></div></div></div>'''

EDI_PAGE = '''<section class="pg">{tx}{icon}<div class="kick">Equality, diversity, inclusion and sustainability</div>
<h2>Inclusive by design, <span class="mk">light on the planet.</span></h2>
<div class="row c2" style="gap:14px">
<div class="mini"><h3>Accessible to everyone</h3><p>WCAG 2.2 AA on every template, tested with keyboard and screen readers. Plain English, captions and alt text built into the CMS so editors keep it accessible.</p><span class="chip">Accessibility statement and annual audit</span></div>
<div class="mini"><h3>Represent every athlete</h3><p>Olympic and Paralympic athletes given equal weight in navigation, stories and imagery. Content guidance for inclusive language and representation.</p><span class="chip">Inclusive content guide for editors</span></div>
<div class="mini"><h3>Low-carbon website</h3><p>Static generation where possible, optimised images and lean JavaScript cut data per page. A page-weight and carbon estimate is reported every quarter.</p><span class="chip">Quarterly carbon and performance report</span></div>
<div class="mini"><h3>A fair, diverse team</h3><p>A founder-led studio co-founded by a woman software engineer. Remote delivery with no business travel, and the same standards required of any subcontractor.</p><span class="chip">Standards apply to every subcontractor</span></div></div>
<div style="margin-top:14px;background:var(--g1);color:#fff;border-radius:14px;padding:12px 18px;display:flex;gap:18px;align-items:center;font-size:8.6pt">
<b style="font:800 10.5pt ID;white-space:nowrap">Reported every quarter</b><span>Accessibility issues found and fixed · Core Web Vitals · average page weight · carbon estimate per visit · actions for the next quarter</span></div>
<div class="foot"><span><b>TWO&amp;HUMAN</b> · {foot}</span><span class="pgn"></span></div></section>
'''

C = dict(slug="uk-sport-dig0911", out=HERE, htitle="Built for the Next Medal Moment — TWO&HUMAN × UK Sport", foot="UK Sport · DIG0911",
 vars="--bg:#f3f5fb;--ink:#0d1430;--mut:#535c78;--p1:#2440d8;--p2:#e11d48;--t1:#e3e8ff;--hl:#ffd1dc;--hl2:#ffc23d;--b1:#d3dbff;--b2:#ffd6e0;--g1:#0b1640;--g2:#2440d8;--g3:#e11d48;",
 css=A4, icons={"heard":"chat-bubble","asks":"file-text","scope":"cube","time":"calender","inv":"pound","close":"medal"}, spark=("#ff4d6d","#2440d8"), tex_light="concrete", tex_grad="liquid-bw", tapes=[1,3,5],
 kick="Tender response · DIG0911 · Digital development partner and headless CMS",
 cover_icons=[("medal","width:3in;right:0.6in;top:1.0in"),("computer","width:1.6in;right:2.9in;top:5.0in"),("rocket","width:1.5in;right:0.7in;top:5.2in")],
 title='Built for the <span class="mk">next medal moment.</span>',
 sub="A fast, accessible UK Sport website on a headless SaaS CMS and Next.js, built by a founder-led team and improved every quarter for four years.",
 **{"for": "UK Sport · Digital, Events &amp; External Affairs<br>Attn. James Gaukroger, Digital Manager"}, date="December 2026",
 heard_h='Four-year cycles, <span class="mk">one digital home.</span>',
 stats=[("4 years","award cycles that shape UK Sport's investment"),("£344m","government investment in Olympic and Paralympic sport for the cycle (2024)"),("£33m+","record winter sport investment for Alpes 2030 (Aug 2026)"),("11 Dec","tenders due by 3pm GMT, by email")],
 asked="A digital development partner to implement a headless SaaS CMS and a Next.js front end, design and develop the new website, migrate content and support it over a four-year term.",
 success="Editors publish funding news, athlete stories and results in minutes, the public finds investment data and stories fast on any device, and the platform keeps improving every quarter.",
 sources="Sources: DIG0911, Find a Tender notice 106227-2026; uksport.gov.uk: How UK Sport funding works, Current funding awards, news releases (May and August 2026).",
 asks_h='What a good partner <span class="mk">has to get right.</span>',
 asks=[("Headless SaaS CMS","A content model editors understand, with roles, workflows and live previews.","Editor-first content model",False),
       ("Next.js front end","Fast, accessible pages: static where possible, dynamic where it matters.","Core Web Vitals in the green",False),
       ("Migration","Every page and asset worth keeping moved, with redirects and no lost search visibility.","Tested redirect map",False),
       ("A four-year partnership","Support, security and continuous improvement, not a one-off build.","Quarterly roadmap",True)],
 confirm="content inventory and priority journeys · CMS shortlist and integrations · hosting, security and data-protection requirements",
 sol_h='Discover, model, build, <span class="mk">improve every quarter.</span>',
 steps=[("zoom","Discover","Stakeholder interviews, analytics, content audit and user journeys."),("puzzle","Model","Content model and CMS configuration, with editor roles and previews."),
        ("computer","Build","Next.js front end, design system and accessible components."),("chart","Improve","Monthly releases, analytics and a quarterly roadmap.")],
 sol_chips=["WCAG 2.2 AA","Core Web Vitals","UK GDPR by design","Code in UK Sport's repository"],
 concept_h='A home for athletes, <span class="mk">investment and impact.</span>', concept=UKS_CONCEPT,
 concept_note="Preliminary concept prepared for this tender, not an official UK Sport design. Final work follows UK Sport's brand guidelines; content and scores shown are illustrative targets.",
 brands=PUBLIC, brand_h='The same craft <span class="mk">on every component.</span>',
 brand_side="We design every touchpoint a brand needs. For UK Sport, that standard shapes the design system, the component library and every athlete story template.",
 scope_h='Build, migrate, <span class="mk">then four years of care.</span>',
 scope=[("Discovery","Interviews, analytics review, content audit, journeys and CMS shortlist.","Discovery report"),("CMS implementation","Content model, roles, workflows, previews and editor training.","Configured CMS"),
        ("Next.js build","Design system, accessible components, search and integrations.","Staging site"),("Migration","Approved content and assets moved, metadata and a tested redirect map.","Content sign-off"),
        ("Quality and launch","WCAG 2.2 AA audit, performance, security and cross-device testing.","Launch"),("Support and development","Service levels, security updates, monthly releases, quarterly roadmap.","Monthly")],
 assume="SaaS CMS licence and hosting contracted in UK Sport's name and billed at cost · content volume confirmed in discovery · two revision rounds per design deliverable · work outside scope quoted in writing first.",
 time_h='Live in 20 weeks, <span class="mk">better every quarter.</span>',
 phases=[("Weeks 1–4","Discover",["Interviews and content audit","Journeys and CMS shortlist","Discovery report"]),
         ("Weeks 5–9","Model and design",["Content model","Design system","Clickable prototype"]),
         ("Weeks 10–18","Build and migrate",["Next.js and CMS build","Content migration","Staging review"]),
         ("Weeks 19–20","Launch",["Accessibility and performance tests","Editor training","Go-live and hypercare"])],
 time_note="Start date follows contract award. After launch, a monthly release cycle and a quarterly roadmap run for the rest of the four-year term. The UK is 3 hours ahead of us, so we overlap UK working afternoons every day.",
 kpis=["Core Web Vitals passed on key templates","Zero critical accessibility issues at launch","Editor publishing time","Uptime and response within service levels"],
 team_h='Founder-led, <span class="mk">and ready for hard questions.</span>',
 julio_role="Account and delivery lead", julio_bio="Single point of contact. Runs discovery, content and delivery; coordinates deliverables, revisions and QA for international clients.",
 mariam_bio="Leads the Next.js build, CMS integration, accessibility, performance and the four-year technical roadmap.",
 qa=[("Can a remote team support UK Sport day to day?","Yes. Our working day overlaps UK afternoons, response times are written into the service levels, and calls run at UK-friendly hours."),
     ("What evidence do we see before the main build?","The concept in this response and a clickable prototype in week 9, approved before the build starts. Payments follow approved milestones."),
     ("Will we be locked in?","No. Code lives in UK Sport's repository, content in UK Sport's CMS account, and the stack is standard Next.js with documentation."),
     ("Contracts, insurance and invoicing?","Invoices in pounds sterling, prices exclusive of VAT, and insurance cover as required by the contract.")],
 inv_h='One build, <span class="mk">four years of continuous development.</span>',
 opts=[("Build","£52,800","one time","Discovery to launch · 20 weeks",["Discovery and content model","Design system and Next.js build","Migration and redirects","Accessibility and performance testing"],False),
       ("Support and development","£3,250","/month","from launch · 42 months",["Service levels and security updates","Monthly releases","About 8 development days a month","Quarterly roadmap and reports"],True),
       ("Rate card","£380","/day","additional work",["Quoted in writing first","Same team and standards","Only on request"],False)],
 guarantee="<b>Launch guarantee.</b> If key templates do not pass Core Web Vitals and WCAG 2.2 AA automated checks at launch, we fix them at no cost before final acceptance.",
 inv_note="Four-year services total: £189,300 (build £52,800 + 42 × £3,250). SaaS CMS licence and hosting in UK Sport's name at cost · prices exclusive of VAT · payments on approved milestones · valid 90 days · also entered in UK Sport's pricing schedule.",
 close_h='Ready to build UK Sport\'s <span class="mk">next digital chapter.</span>',
 compliance=[("Headless SaaS CMS implementation","Yes"),("Next.js front end","Yes"),("Design and development","Yes"),("Content migration","Yes"),("Support, four-year term","Yes"),("Accessibility, WCAG 2.2 AA","Yes"),("EDI and sustainability","Page 7"),("ITT forms and appendices","Included")],
 next=[("Submission","By email to digital@uksport.gov.uk before 3pm GMT, 11 December."),("Clarifications","Aligned with the consolidated Q&amp;A due by 30 November."),("Presentation","A walk-through of the prototype approach.")])

if __name__ == "__main__":
    G.build(C)
    fp = os.path.join(HERE, C["slug"] + ".html")
    t = open(fp).read()
    # página de igualdad, diversidad, inclusión y sostenibilidad, antes del alcance
    tx = f'<img class="tx l" src="../../assets/tex/{C["tex_light"]}.jpg">'
    icon = G.ic("heart", "width:1.5in;right:0.75in;top:0.45in", "i3 r2")
    edi = EDI_PAGE.format(tx=tx, icon=icon, foot=C["foot"])
    marker = '<div class="kick">06 · Scope and deliverables</div>'
    i = t.index(marker); j = t.rfind("<section", 0, i)
    t = t[:j] + edi + t[j:]
    # numeración con la página nueva, y términos del Reino Unido (ITT, libras)
    for a, b in [("10 · Compliance","11 · Compliance"),("09 · Investment (USD)","10 · Investment (GBP)"),("08 · Team","09 · Team"),
                 ("07 · Timeline","08 · Timeline"),("06 · Scope","07 · Scope"),
                 ('class="kick">Equality, diversity','class="kick">06 · Equality, diversity'),("What the RFP really asks","What the ITT really asks")]:
        assert a in t, a
        t = t.replace(a, b)
    t = t.replace("../../assets/", "../assets/")   # lote8 está un nivel más arriba que lote5/v2
    open(fp, "w").write(G.clean(t))
    print("ok", C["slug"])
