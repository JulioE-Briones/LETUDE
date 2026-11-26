# Lote 7 en estilo pop (US Letter): Texas A&M Citizens for Good, State Tech Missouri y RTD Denver.
# Uso: python3 gen7.py  -> escribe <slug>.html en esta carpeta.
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "../lote5/v2"))
import gen_us as G

PUBLIC = [("traza","TRAZA","Urban accessories"),("ayven","AYVEN","Performance apparel"),("atelier-lorenzo","Atelier Lorenzo","Leather atelier"),
          ("paleta-loca","Paleta Loca","Ice cream"),("el-taco-club","El Taco Club","Restaurant"),("serena-ritual","Serena Ritual","Spa and wellness")]
QA_PAY = G.COMMON_QA_PAY

# ---------------- mockups ----------------
TAMU_CONCEPT = '''<div style="display:grid;grid-template-columns:1fr 1.75in 1.85in;gap:20px;align-items:start">
<div class="browser"><div class="bar"><i></i><i></i><i></i><span>tamu.edu · citizens for good</span></div>
<div style="background:linear-gradient(120deg,#500000,#8a1c2b);color:#fff;padding:16px 16px 14px"><div style="font:700 7pt IT;letter-spacing:.16em;color:#f4c9a8">CITIZENS FOR GOOD</div><div style="font:800 17pt/1.02 ID;margin-top:6px">Find your way to serve this week.</div><p style="font-size:7.4pt;color:#f3dede;margin:6px 0 0">Events, service projects and the badge you can earn, in one place.</p></div>
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px;padding:10px 12px">
<div style="border:1px solid #eee;border-radius:9px;padding:8px;font-size:7pt;text-align:center"><b style="display:block;font:800 8.6pt ID;color:#500000">Character</b>Lead with integrity</div>
<div style="border:1px solid #eee;border-radius:9px;padding:8px;font-size:7pt;text-align:center"><b style="display:block;font:800 8.6pt ID;color:#500000">Knowledge</b>Know how it works</div>
<div style="border:1px solid #eee;border-radius:9px;padding:8px;font-size:7pt;text-align:center"><b style="display:block;font:800 8.6pt ID;color:#500000">Skills</b>Dialogue and action</div>
<div style="border:1px solid #eee;border-radius:9px;padding:8px;font-size:7pt;text-align:center"><b style="display:block;font:800 8.6pt ID;color:#500000">Service</b>Show up for others</div></div>
<div style="display:flex;justify-content:space-between;align-items:center;margin:0 12px 12px;background:#fbf3f3;border-radius:10px;padding:8px 10px;font-size:7.4pt"><span><b>Earn your Citizen for Good badge</b> · 3 steps left</span><span style="background:#500000;color:#fff;border-radius:8px;padding:3px 9px;font-weight:700">Start</span></div></div>
<div class="phone"><div class="scr" style="padding:10px">
<div style="font:800 7.6pt ID;margin-bottom:6px">@citizensforgood</div>
<div style="height:1.55in;border-radius:10px;background:linear-gradient(150deg,#500000,#d9822b);position:relative"><div style="position:absolute;left:10px;bottom:10px;color:#fff;font:800 13pt/1.05 ID">Service<br>Saturday</div><div style="position:absolute;right:10px;top:10px;background:#fff;color:#500000;border-radius:8px;font:800 6.6pt IT;padding:2px 6px">REEL</div></div>
<div style="font-size:7pt;color:#555;margin-top:8px">3 projects this weekend. Sign up in 1 minute. Link in bio.</div>
<div style="margin-top:8px;background:#500000;color:#fff;border-radius:8px;text-align:center;font:800 7.4pt ID;padding:6px">Sign up</div></div></div>
<div class="card" style="padding:14px 14px"><div style="font:800 7.4pt IT;letter-spacing:.14em;color:var(--p1)">NEWSLETTER · EVERY OTHER WEEK</div>
<div style="font:800 12pt/1.1 ID;margin-top:8px">This week, 340 Aggies served.</div>
<div style="height:7px;border-radius:4px;background:#eee;margin:10px 0 5px"></div><div style="height:7px;width:80%;border-radius:4px;background:#eee;margin-bottom:5px"></div><div style="height:7px;width:60%;border-radius:4px;background:#eee;margin-bottom:10px"></div>
<div style="display:flex;gap:6px;flex-wrap:wrap"><span class="chip">Upcoming events</span><span class="chip">Student story</span><span class="chip">Badge progress</span></div></div></div>'''

STC_CONCEPT = '''<div style="display:grid;grid-template-columns:1.25fr 1fr;gap:22px;align-items:start">
<div class="browser"><div class="bar"><i></i><i></i><i></i><span>statetechmo.edu · find your program</span></div>
<div style="background:linear-gradient(120deg,#0b3f8c,#1f8f5b);color:#fff;padding:16px"><div style="font:800 17pt/1.02 ID">Find your career. We'll train you for it.</div>
<div style="display:flex;gap:8px;margin-top:10px"><div style="flex:1;background:#fff;border-radius:8px;padding:6px 10px;font-size:7.6pt;color:#6b7480">I want to work in… electrical, aviation, health…</div><div style="background:#ffc23d;color:#13213a;border-radius:8px;padding:6px 12px;font:800 7.6pt ID">Search</div></div></div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px;padding:10px 12px 12px">
<div style="border:1px solid #eceef2;border-radius:9px;padding:8px;font-size:7pt"><b style="display:block;font:800 8.2pt ID;color:#0b3f8c">Electrical Distribution</b>2-year program · hands-on<br><span style="color:#1f8f5b;font-weight:700">Career outcomes →</span></div>
<div style="border:1px solid #eceef2;border-radius:9px;padding:8px;font-size:7pt"><b style="display:block;font:800 8.2pt ID;color:#0b3f8c">Aviation Maintenance</b>2-year program · hands-on<br><span style="color:#1f8f5b;font-weight:700">Career outcomes →</span></div>
<div style="border:1px solid #eceef2;border-radius:9px;padding:8px;font-size:7pt"><b style="display:block;font:800 8.2pt ID;color:#0b3f8c">Physical Therapist Asst.</b>2-year program · hands-on<br><span style="color:#1f8f5b;font-weight:700">Career outcomes →</span></div></div>
<div style="display:flex;justify-content:space-between;margin:0 12px 12px;background:#eef6ff;border-radius:10px;padding:8px 10px;font-size:7.4pt"><span><b>Ready to apply?</b> It takes about 15 minutes.</span><span style="background:#0b3f8c;color:#fff;border-radius:8px;padding:3px 9px;font-weight:700">Apply</span></div></div>
<div class="card" style="padding:16px 18px"><div style="font:800 7.6pt IT;letter-spacing:.14em;color:var(--p1)">ENROLLMENT FUNNEL DASHBOARD</div>
<div style="margin-top:10px;display:grid;gap:7px;font-size:8.4pt">
<div><div style="display:flex;justify-content:space-between"><span>Site visits</span><b>100%</b></div><div style="height:12px;border-radius:6px;background:#0b3f8c"></div></div>
<div><div style="display:flex;justify-content:space-between"><span>Program pages</span><b>48%</b></div><div style="height:12px;width:48%;border-radius:6px;background:#2a63b8"></div></div>
<div><div style="display:flex;justify-content:space-between"><span>Apply started</span><b>9%</b></div><div style="height:12px;width:22%;border-radius:6px;background:#1f8f5b"></div></div>
<div><div style="display:flex;justify-content:space-between"><span>Applications</span><b>5%</b></div><div style="height:12px;width:15%;border-radius:6px;background:#2fb27a"></div></div>
<div><div style="display:flex;justify-content:space-between"><span>Enrolled</span><b>2%</b></div><div style="height:12px;width:9%;border-radius:6px;background:#ffc23d"></div></div></div>
<p style="font-size:7.6pt;color:var(--mut);margin-top:10px">Example figures. Each step tracked by program and by channel.</p></div></div>'''

RTD_CONCEPT = '''<div style="display:grid;grid-template-columns:1.35in 1fr;gap:18px;align-items:start">
<div class="card" style="padding:14px 14px"><div style="font:800 7.4pt IT;letter-spacing:.14em;color:var(--p1)">WHAT RIDERS SAY · 2026</div>
<div style="font:800 24pt/1 ID;color:var(--p1);margin-top:8px">87%</div><div style="font-size:7.8pt;color:var(--mut)">rail customers satisfied</div>
<div style="font:800 24pt/1 ID;color:var(--p1);margin-top:10px">86%</div><div style="font-size:7.8pt;color:var(--mut)">say RTD is valuable to the region</div>
<div style="font:800 15pt/1 ID;color:#e5533d;margin-top:10px">Trust gap</div><div style="font-size:7.8pt;color:var(--mut)">what we research first</div></div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px">
<div style="border-radius:16px;overflow:hidden;box-shadow:0 12px 26px rgba(20,20,60,.15);background:#fff"><div style="height:1.5in;background:linear-gradient(150deg,#0b3d91,#1aa7ec);position:relative"><div style="position:absolute;left:10px;bottom:10px;color:#fff;font:800 14pt/1 ID">Here for<br>your city.</div></div><div style="padding:9px 10px;font-size:7.6pt"><b style="display:block;font:800 8.6pt ID">Route A · Service</b>Real people who keep Denver moving, every day.</div></div>
<div style="border-radius:16px;overflow:hidden;box-shadow:0 12px 26px rgba(20,20,60,.15);background:#fff"><div style="height:1.5in;background:linear-gradient(150deg,#ffc72c,#ff8a3d);position:relative"><div style="position:absolute;left:10px;bottom:10px;color:#13213a;font:800 14pt/1 ID">What we<br>fixed this month.</div></div><div style="padding:9px 10px;font-size:7.6pt"><b style="display:block;font:800 8.6pt ID">Route B · Proof</b>Visible, measurable progress, told plainly.</div></div>
<div style="border-radius:16px;overflow:hidden;box-shadow:0 12px 26px rgba(20,20,60,.15);background:#fff"><div style="height:1.5in;background:linear-gradient(150deg,#1f9d6a,#7fe0b4);position:relative"><div style="position:absolute;left:10px;bottom:10px;color:#fff;font:800 14pt/1 ID">Your trip.<br>Our promise.</div></div><div style="padding:9px 10px;font-size:7.6pt"><b style="display:block;font:800 8.6pt ID">Route C · Commitment</b>Clear promises riders can hold us to.</div></div></div></div>'''

CLIENTS = [
dict(slug="tamu-citizens-for-good", out=HERE, htitle="Make Good Visible — TWO&HUMAN × Texas A&M", foot="Texas A&M University · TAMU-RFP-27-5142",
 vars="--bg:#fbf6f4;--ink:#2a1214;--mut:#6b5556;--p1:#7a1426;--p2:#d9822b;--t1:#f6e3e5;--hl:#f7d9b8;--hl2:#ffc24b;--b1:#f1d3d7;--b2:#fbe2c8;--g1:#500000;--g2:#9a2436;--g3:#e0963a;",
 icons={"heard":"chat-bubble","asks":"file-text","scope":"cube","time":"calender","inv":"money-bag","close":"medal"}, spark=("#ffc24b","#7a1426"), tex_light="paper", tex_grad="halftone-orange", tapes=[2,5,1],
 kick="Proposal · TAMU-RFP-27-5142 · Marketing and Communications Services",
 cover_icons=[("heart","width:3in;right:0.6in;top:1.0in"),("megaphone","width:1.6in;right:2.9in;top:5.0in"),("mail","width:1.5in;right:0.7in;top:5.2in")],
 title='Make good <span class="mk">visible.</span>',
 sub="Website, social media, newsletters and student engagement for Citizens for Good, run every week by a team that also builds the tools behind them.",
 **{"for": "Texas A&M University · Procurement Services<br>Citizenship and Service · Citizens for Good"}, date="December 2026",
 heard_h='A university-wide promise <span class="mk">that students should feel every week.</span>',
 stats=[("4 pillars","character, knowledge, skills and service"),("Fall 2024","initiative introduced by President Mark Welsh"),("Badge","a Citizen for Good credential students can earn"),("Dec 2","proposals due, December 2, 2026")],
 asked="Marketing and communications support for Citizens for Good: maintain and grow the website, run the social media channels, produce newsletters and drive student engagement.",
 success="More Aggies know the program, join a project and earn the badge, and the team sees every week which posts, emails and pages moved students to act.",
 sources="Sources: TAMU-RFP-27-5142 (Texas A&M procurement, posted 9 Nov 2026); tamu.edu, Building Citizens for Good; Texas A&M Today, Citizenship and Service Initiative (Feb 2025).",
 asks_h='Four channels, <span class="mk">one rhythm.</span>',
 asks=[("Website","The home of the program: current, fast, accessible and easy for staff to update.","Weekly updates",False),
       ("Social media","Short video and stories that show real students serving, not just announcements.","Reels-first calendar",False),
       ("Newsletters","A regular email students actually open: what's on, who served, what's next.","Every other week",False),
       ("Student engagement","Every channel ends in one action: sign up, attend, or earn the badge.","Measured by sign-ups",True)],
 confirm="current channels and accounts · brand and approval process · event calendar and priority audiences",
 sol_h='The Citizens for Good studio: <span class="mk">plan, make, publish, measure.</span>',
 steps=[("calender","Plan","A semester calendar built around the pillars and the academic year."),("video-camera","Make","Reels, stories, posts and emails in the university's voice."),
        ("computer","Publish","Website updates, social posting and newsletter sends."),("chart","Measure","Sign-ups and badge progress, reported monthly.")],
 sol_chips=["Texas A&M brand standards","WCAG 2.1 AA web content","Student voices, with consent","One weekly rhythm"],
 concept_h='One action, <span class="mk">on every channel.</span>', concept=TAMU_CONCEPT,
 concept_note="Preliminary concept prepared for this proposal, not an official Texas A&M design. Final work follows the university's brand standards; names and figures are illustrative.",
 brands=PUBLIC, brand_h='Every client gets <span class="mk">a brand world, not just a logo.</span>',
 brand_side="We design every touchpoint a brand needs. For Citizens for Good, that standard shapes the social templates, the newsletter and every event graphic, all within the university's brand.",
 scope_h='Everything the program needs, <span class="mk">every month.</span>',
 scope=[("Website","Content updates, new pages, events and stories; accessibility checks on every update.","Weekly"),("Social media","Calendar, reels, stories and posts; community replies during business hours.","Weekly"),
        ("Newsletters","Design, writing and sending, with open and click reports.","Every other week"),("Student engagement","Campaigns around sign-ups, events and the badge; student story features.","Each semester"),
        ("Templates","Editable templates staff can use for quick posts and flyers.","Month 1"),("Reporting","Monthly report on reach, sign-ups and badge progress.","Monthly")],
 assume="university accounts and tools stay in Texas A&M's name · paid advertising, if any, billed at cost · two revision rounds per item · content approved by the program team before publishing.",
 time_h='Running in 30 days, <span class="mk">measured every month.</span>',
 phases=[("Weeks 1–2","Onboard",["Access, brand and approvals","Channel and website audit","Spring semester calendar"]),
         ("Weeks 3–4","Launch",["First campaign live","Newsletter template","Templates for staff"]),
         ("Month 2 on","Run",["Weekly publishing","Newsletter every other week","Monthly report"]),
         ("Each semester","Grow",["Badge campaign","Student stories","Semester review"])],
 time_note="Start date follows award. All publishing goes through the program's approval step; Central Time is 3 hours behind us, so we cover the full morning.",
 kpis=["Event and project sign-ups","Badge starts and completions","Newsletter opens and clicks","Website visits to sign-up pages"],
 team_h='Founder-led, <span class="mk">and ready for hard questions.</span>',
 julio_role="Strategy and content lead", julio_bio="Single point of contact. Plans the calendar and writes the content; coordinates deliverables, revisions and QA for international marketing clients.",
 mariam_bio="Leads the website, accessibility, newsletter setup and the tracking that ties each post to sign-ups.",
 qa=[("Can a remote team capture student life?","Students and staff send photos and clips through a simple shared form; we turn them into reels and stories, always with consent."),
     ("Who approves what goes out?","The program team. Nothing is published without approval, and urgent posts have a same-day path."),
     ("Who owns the accounts and content?","Texas A&M. Every account, file and asset stays in the university's name."), QA_PAY],
 inv_h='One setup, <span class="mk">three monthly levels.</span>',
 opts=[("Essential","$1,450","/month","+ $2,400 one-time setup",["Website updates","12 social posts a month","1 newsletter a month","Monthly report"],False),
       ("Citizens for Good studio","$2,450","/month","+ $2,400 one-time setup",["Weekly website updates","20 posts a month, reels first","2 newsletters a month","Semester engagement campaign","Monthly report"],True),
       ("Full program","$3,600","/month","+ $2,400 one-time setup",["Everything in the studio","Student story video series","Event promotion kits","Quarterly strategy review"],False)],
 guarantee="<b>30-day guarantee.</b> If the calendar, the templates and the first campaign are not live within 30 days of kickoff, the second month is free.",
 inv_note="Setup: audit, calendar, templates and newsletter design. Year-1 cost, recommended option: $31,800. Monthly fees invoiced in arrears · extra work $60 per hour, quoted in writing · prices valid 90 days · also entered in the university's pricing form.",
 close_h='Ready to make <span class="mk">good visible.</span>',
 compliance=[("Website maintenance and growth","Yes"),("Social media channels","Yes"),("Newsletters","Yes"),("Student engagement","Yes"),("Reporting","Monthly"),("Accessibility","WCAG 2.1 AA"),("Required forms","Included"),("Insurance","As required")],
 next=[("Submission","By December 2, 2026."),("Interview","A video walk-through of the plan."),("Kickoff","First campaign live in 30 days.")]),

dict(slug="state-tech-website", out=HERE, htitle="From First Click to First Day — TWO&HUMAN × State Tech", foot="State Technical College of Missouri · RFP-03-0-2026/BM",
 vars="--bg:#f2f7ff;--ink:#0f1d33;--mut:#53617a;--p1:#0b4aa8;--p2:#1f9d6a;--t1:#e1ecff;--hl:#c9f0da;--hl2:#ffc23d;--b1:#cfe0ff;--b2:#cdf1df;--g1:#0b3f8c;--g2:#1f8f5b;--g3:#ffc23d;",
 icons={"heard":"chat-bubble","asks":"file-text","scope":"cube","time":"calender","inv":"money-bag","close":"rocket"}, spark=("#ffc23d","#1f9d6a"), tex_light="concrete", tex_grad="halftone-teal", tapes=[4,7,5],
 kick="Proposal · RFP-03-0-2026/BM · Website Redesign",
 cover_icons=[("computer","width:3.1in;right:0.55in;top:1.0in"),("tool","width:1.6in;right:2.9in;top:5.0in"),("chart","width:1.5in;right:0.7in;top:5.2in")],
 title='From first click <span class="mk">to first day.</span>',
 sub="A mobile-first, accessible website that helps future students find their program, see the career it leads to and apply, with analytics that follow every step to enrollment.",
 **{"for": "State Technical College of Missouri<br>Business Office · Linn, Missouri"}, date="December 2026",
 heard_h='A record-breaking college <span class="mk">deserves a website that keeps up.</span>',
 stats=[("2,422","full-time students in fall 2025, a new record"),("#1","WalletHub 2026 ranking, as reported by the College"),("Fastest","growing college in Missouri (2026)"),("2.1 AA","WCAG level the redesign must meet")],
 asked="Redesign the College website so every page is mobile responsive and meets WCAG 2.1 Level AA, and improve analytics to track visitors, digital communications, engagement, applications and enrollment.",
 success="A student on a phone finds a program, sees where it leads and applies in minutes, and the College sees which pages and channels produce applications and enrolled students.",
 sources="Sources: RFP-03-0-2026/BM (posted 2 Nov 2026, responses due 4 Dec 2026); News Tribune (record enrollment, Oct 2025 and Aug 2026); statetechmo.edu (rankings).",
 asks_h='Three requirements, <span class="mk">one enrollment journey.</span>',
 asks=[("Mobile responsive","Most prospects arrive on a phone. Every page, program and form must work there first.","Mobile-first templates",False),
       ("WCAG 2.1 AA","Every page and document accessible, at launch and as staff keep adding content.","Tested and monitored",False),
       ("Analytics to enrollment","Follow a visitor from the first click to application and enrollment, by program and channel.","Funnel dashboard",False),
       ("Our focus","The journey from curiosity to application is where we put the most design and measurement effort.","",True)],
 confirm="current platform and integrations · application and student-information systems · number of pages and documents to migrate",
 sol_h='Find, trust, apply, enroll: <span class="mk">a website built as a journey.</span>',
 steps=[("zoom","Program finder","Search by career interest, with clear program pages."),("medal","Career proof","Outcomes, employers and student stories on every program page."),
        ("tick","Easy apply","Short, accessible path to the application, on any phone."),("chart","Measured to enrollment","GA4 events and a dashboard by program and channel.")],
 sol_chips=["Mobile-first","WCAG 2.1 AA","Open-source WordPress, no license fees","The College owns everything"],
 concept_h='A program finder <span class="mk">and a funnel you can see.</span>', concept=STC_CONCEPT,
 concept_note="Preliminary concept prepared for this proposal, not an official State Tech design. Programs and funnel figures are illustrative; final work follows the College's brand.",
 brands=PUBLIC, brand_h='The same craft <span class="mk">on every page.</span>',
 brand_side="We design every touchpoint a brand needs. For State Tech, that standard shapes the program pages, photography direction and the templates staff use after launch.",
 scope_h='Everything to redesign, <span class="mk">migrate and measure.</span>',
 scope=[("Discovery","Stakeholder interviews, analytics review, content inventory and top tasks.","Approved plan"),("Architecture","Sitemap, program finder, navigation and content model.","Approved sitemap"),
        ("Design","Design system, mobile-first templates, clickable prototype.","Milestone 1"),("Build","WordPress build, program finder, forms, search, CMS roles.","Milestone 2"),
        ("Migration and accessibility","Content migration, document remediation plan, WCAG 2.1 AA testing.","Test report"),("Analytics","GA4, events, application tracking and an enrollment funnel dashboard.","Milestone 3")],
 assume="up to 400 approved pages migrated (confirmed by the inventory) · up to 14 page templates · two revision rounds per design deliverable · anything outside scope quoted in writing before work starts.",
 time_h='Live in 20 weeks, <span class="mk">ahead of fall recruiting.</span>',
 phases=[("Weeks 1–4","Discover",["Interviews and inventory","Top tasks and sitemap","Analytics baseline"]),
         ("Weeks 5–9","Design",["Design system","Clickable prototype","Milestone 1"]),
         ("Weeks 10–17","Build and migrate",["WordPress and finder","Content migration","Milestone 2"]),
         ("Weeks 18–20","Test and launch",["WCAG 2.1 AA testing","Funnel dashboard","Launch and training"])],
 time_note="Start date follows award. Central Time is 3 hours behind us; weekly status in writing and calls in the College's morning.",
 kpis=["Application starts and completions by program","Mobile task completion","Zero critical accessibility errors at launch","Enrollment attributed by channel"],
 team_h='Founder-led, <span class="mk">and ready for hard questions.</span>',
 julio_role="Strategy and project lead", julio_bio="Single point of contact. Leads discovery, content and the program story; coordinates deliverables, revisions and QA for international clients.",
 mariam_bio="Leads the WordPress build, accessibility, integrations and the analytics that follow students to enrollment.",
 qa=[("Will we be locked in?","No. Open-source WordPress, no proprietary builder, no license fees. Code, content and accounts belong to the College."),
     ("Can our staff keep it accessible?","Yes. Locked templates, an in-editor accessibility checker and a short guide for every editor role."),
     ("How do you track enrollment?","GA4 events on every step, connected to the application where the College's systems allow it, in one dashboard."), QA_PAY],
 inv_h='One fixed build price, <span class="mk">three ways to care for it.</span>',
 opts=[("Launch","$48,500","one time","College-provided hosting",["Design, build and migration","WCAG 2.1 AA test report","Enrollment funnel dashboard","Training and 60-day stabilization"],False),
       ("Launch + Care","$450","/month","+ $48,500 fixed build",["Everything in Launch","Managed U.S. hosting","Updates, backups and security","Monthly accessibility scan","Up to 4 hours of changes"],True),
       ("Launch + Care + Grow","$1,100","/month","+ $48,500 fixed build",["Everything in Care","Monthly funnel review","One conversion test a month","Up to 10 hours of changes"],False)],
 guarantee="<b>Accessibility guarantee.</b> Zero critical errors in automated WCAG 2.1 AA scans at launch, and anything flagged in the first 60 days is fixed at no cost.",
 inv_note="Build: discovery 3,600 · architecture 3,000 · design 7,200 · build 15,600 · migration and accessibility 12,000 · analytics 4,800 · training and launch 2,300. Payments 30/40/30 on approved milestones · third-party costs at cost · valid 90 days · also entered in the College's pricing form.",
 close_h='Ready to take students <span class="mk">from first click to first day.</span>',
 compliance=[("Website redesign, all pages","Yes"),("Mobile responsive","Yes"),("WCAG 2.1 Level AA","Yes"),("Analytics: visitors, engagement","Yes"),("Analytics: applications, enrollment","Yes"),("Content migration","Yes"),("Required forms","Included"),("Insurance","As required")],
 next=[("Submission","By December 4, 2026."),("Interview","A walk-through of the prototype approach."),("Kickoff","Discovery starts in week 1.")]),

dict(slug="rtd-brand-reputation", out=HERE, htitle="Earn the Ride — TWO&HUMAN × RTD", foot="Regional Transportation District · 026MB004",
 vars="--bg:#f2f7fd;--ink:#0d1b33;--mut:#526079;--p1:#0b4ab0;--p2:#ff8a3d;--t1:#e1ecff;--hl:#ffe08a;--hl2:#ffc72c;--b1:#cfe0ff;--b2:#ffe0c8;--g1:#0b3d91;--g2:#1aa7ec;--g3:#ffc72c;",
 icons={"heard":"chat-bubble","asks":"file-text","scope":"cube","time":"calender","inv":"money-bag","close":"star"}, spark=("#ffc72c","#1aa7ec"), tex_light="paper", tex_grad="halftone-teal", tapes=[1,5,3],
 kick="Quote · RFQ 026MB004 · Brand Reputation Campaign",
 cover_icons=[("location","width:3in;right:0.6in;top:1.0in"),("chat-bubble","width:1.6in;right:2.9in;top:5.0in"),("bulb","width:1.4in;right:0.8in;top:5.2in")],
 title='Earn the ride, <span class="mk">every day.</span>',
 sub="Research first, then positioning, then three campaign concepts built to close the gap between how RTD performs and how the region feels about it.",
 **{"for": "Regional Transportation District (RTD)<br>Attn. Marla Bainbridge"}, date="December 2026",
 heard_h='Satisfaction is up. <span class="mk">Perception has not caught up.</span>',
 stats=[("87%","of rail customers satisfied in RTD's 2026 survey"),("82%","of bus customers satisfied"),("86%","say RTD is valuable to the region"),("Trust","the gap reported alongside these gains")],
 asked="A brand reputation campaign: sentiment research, focus groups and benchmarking against other transit agencies, then a positioning and messaging framework and three campaign concepts.",
 success="RTD knows exactly why perception lags performance, has one positioning the whole agency can use, and three tested concepts ready to produce.",
 sources="Sources: RFQ 026MB004 (O'Dwyer's, 19 Nov 2026); RTD 2026 Customer and Community Survey, ETC Institute (released 1 June 2026); CBS Colorado and Denver Gazette coverage of the results.",
 asks_h='Three phases, <span class="mk">in the right order.</span>',
 asks=[("Research and assessment","Sentiment research, focus groups and peer benchmarking before any creative.","150 hours",False),
       ("Positioning and messaging","One clear positioning and a message framework for every audience.","100 hours",False),
       ("Campaign development","Three distinct campaign concepts, ready for RTD to choose and produce.","225 hours",False),
       ("Why this order works","Creative built on research is creative the public believes. We keep that order.","",True)],
 confirm="existing research and survey data · priority audiences and corridors · approval process and decision-makers",
 sol_h='Listen, frame, create: <span class="mk">a campaign the region believes.</span>',
 steps=[("zoom","Listen","Survey and social sentiment review, focus groups, peer benchmarking."),("target","Frame","Positioning, proof points and a message house by audience."),
        ("paint-kit","Create","Three campaign concepts with headlines, key visuals and channel ideas."),("chart","Test","Concepts tested with riders and non-riders before RTD chooses.")],
 sol_chips=["Riders and non-riders","English and Spanish","Benchmarked against peer agencies","Tested before production"],
 concept_h='Three routes, <span class="mk">one promise.</span>', concept=RTD_CONCEPT,
 concept_note="Preliminary concepts prepared for this proposal, not official RTD material. Final concepts come out of the research phase; survey figures are from RTD's public 2026 results.",
 brands=PUBLIC, brand_h='Campaigns with <span class="mk">a brand world behind them.</span>',
 brand_side="We design every touchpoint a brand needs. For RTD, that standard means concepts that work on a bus wrap, a station poster, a social video and a rider email.",
 scope_h='Everything in the RFQ, <span class="mk">in 8 weeks.</span>',
 scope=[("Sentiment research","Review of RTD surveys, social and media sentiment, community feedback.","Week 2"),("Focus groups","Riders and non-riders across the district, English and Spanish.","Weeks 2–3"),
        ("Peer benchmarking","How peer transit agencies rebuilt trust: what worked and why.","Week 3"),("Strategic assessment","Findings report and workshop with RTD.","Week 3"),
        ("Positioning and messaging","Positioning statement, proof points, message house by audience.","Week 5"),("Three campaign concepts","Headlines, key visuals, channel ideas and concept testing.","Week 8")],
 assume="focus group recruitment and incentives billed at cost · focus groups run online with participants from the RTD district; in-person sessions at a Denver facility available at cost · two revision rounds per deliverable.",
 time_h='Eight weeks, <span class="mk">three decisions.</span>',
 phases=[("Weeks 1–3","Research and assessment",["Sentiment review","Focus groups","Peer benchmarking and workshop"]),
         ("Weeks 4–5","Positioning",["Positioning options","Message house","RTD approval"]),
         ("Weeks 6–8","Campaign concepts",["Three concepts","Testing with riders and non-riders","Final presentation"])],
 time_note="Eight weeks from kickoff, within the 120-day period of performance. Mountain Time is 4 hours behind us, so we cover RTD's full morning.",
 kpis=["Clear drivers of trust and distrust","One approved positioning","Three tested concepts","Baseline metrics for the campaign"],
 team_h='Founder-led, <span class="mk">and ready for hard questions.</span>',
 julio_role="Strategy and research lead", julio_bio="Single point of contact. Leads the research, positioning and campaign concepts; coordinates deliverables and QA for international marketing clients.",
 mariam_bio="Leads data and analysis: survey and sentiment analysis, benchmarking structure and campaign measurement plans.",
 qa=[("How do you know Denver?","By asking Denver. Focus groups recruited across the district, RTD's own survey data and local media coverage are the foundation, not our assumptions."),
     ("Can focus groups run remotely?","Yes, online with district residents, which also reaches people who rarely attend in person. In-person sessions are available at cost."),
     ("What do we get at the end?","A findings report, an approved positioning and three tested concepts, ready to produce."), QA_PAY],
 inv_h='One fixed price, <span class="mk">built on the RFQ\'s hours.</span>',
 opts=[("Research + positioning","$15,000","fixed","Phases 1 and 2 · 250 hours",["Sentiment research","Focus groups and benchmarking","Positioning and message house"],False),
       ("Full scope","$28,500","fixed","Phases 1–3 · 475 hours · 8 weeks",["Everything in Research + positioning","Three campaign concepts","Concept testing","Final presentation"],True),
       ("Full scope + launch kit","$34,900","fixed","Phases 1–3 plus launch kit",["Everything in Full scope","Production-ready assets for the chosen concept","Launch measurement plan"],False)],
 guarantee="<b>Concept guarantee.</b> If RTD does not approve any of the three concepts after the agreed revisions, we develop a fourth at no cost.",
 inv_note="Full scope: research and assessment 9,000 (150 h) · positioning and messaging 6,000 (100 h) · campaign development 13,500 (225 h). Focus group recruitment and incentives at cost · payments on approved phases · valid 90 days · also entered in RTD's cost form.",
 close_h='Ready to help the region <span class="mk">see what RTD delivers.</span>',
 compliance=[("Sentiment research","Yes"),("Focus groups","Yes"),("Benchmarking vs. peer agencies","Yes"),("Positioning and messaging","Yes"),("Three campaign concepts","Yes"),("Cost estimate, 8 weeks","Yes"),("Required forms","Included"),("Insurance","As required")],
 next=[("Submission","Through RTD's procurement portal."),("Interview","A walk-through of the research plan."),("Kickoff","Research starts in week 1.")]),
]

if __name__ == "__main__":
    for c in CLIENTS:
        G.build(c)
        fp = os.path.join(HERE, c["slug"] + ".html")
        t = open(fp).read().replace("../../assets/", "../assets/"); open(fp, "w").write(t)   # lote7 está un nivel más arriba que lote5/v2
        print("ok", c["slug"])
