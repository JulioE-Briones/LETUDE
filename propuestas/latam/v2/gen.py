# Genera las 4 propuestas LatAm en estilo "pop" (A4 apaisado, íconos 3D).
# Uso: python3 gen.py  -> escribe <slug>.html en esta carpeta.
import os
A = "../../assets/3dicons/"
OLD = {"magnifier":"zoom","target":"target","megaphone":"megaphone","calendar":"calender","growth":"chart","check":"tick","boxes":"cube","piggy":"money-bag",
       "calculator":"calculator","prohibited":"thumb-down","p-bank":"chat-bubble","p-browser":"computer","p-computer":"computer","g-shield":"sheild",
       "b-chart":"chart","b-clipboard":"file-text","g-box":"cube","g-calendar":"calender","b-coins":"dollar","b-moneybag":"money-bag","b-pin":"map-pin",
       "p-megaphone":"megaphone","p-trophy":"trophy","p-paint":"paint-kit","p-certificate":"medal"}
STYLE = "color-dynamic"
def P(n, style=None):
    n = OLD.get(n, n)
    if "/" not in n:
        n = (style or globals().get("CUR", {}).get("icon_style") or STYLE) + "/" + n
    return A + n + ".png"

HERE = os.path.dirname(os.path.abspath(__file__))

def icon(n, style, cls="i3"):
    return f'<img class="{cls}" src="{P(n)}" style="{style}">'

def stats(items):
    return '<div class="row c4">' + "".join(f'<div class="card"><div class="big">{v}</div><div class="lbl">{t}</div></div>' for v, t in items) + "</div>"

def fugas(items):
    return '<div class="row c3">' + "".join(f'<div class="card"><div class="num">{i+1}</div><h3>{h}</h3><p>{p}</p><span class="chip">{c}</span></div>' for i, (h, p, c) in enumerate(items)) + "</div>"

def bars(title, rows):
    out = f'<div class="card" style="margin-top:16px"><h3 style="font-size:11pt;margin-bottom:10px">{title}</h3><div class="bars">'
    for lab, w, v, me in rows:
        out += f'<div class="b{" me" if me else ""}"><span>{lab}</span><div class="tr"><i style="width:{w}%"></i></div><span class="v">{v}</span></div>'
    return out + "</div></div>"

def steps(items):
    return '<div class="steps">' + "".join(f'<div class="card"><img class="ic" src="{P(ic)}"><h3>{h}</h3><p>{p}</p></div>' for ic, h, p in items) + "</div>"

def chips(items, center=False):
    return f'<p style="margin-top:20px{";text-align:center" if center else ""}">' + " ".join(f'<span class="chip">{c}</span>' for c in items) + "</p>"

def meses(items):
    return '<div class="row c3">' + "".join(f'<div class="mes"><div class="m">Mes {i+1}</div><h3>{h}</h3><ul>' + "".join(f"<li>{x}</li>" for x in li) + "</ul></div>" for i, (h, li) in enumerate(items)) + "</div>"

def opts(items):
    out = '<div class="row c3" style="align-items:start">'
    for nm, pr, unit, pm, li, rec in items:
        out += f'<div class="opt{" rec" if rec else ""}">' + ('<div class="badge">Recomendada</div>' if rec else "") + f'<div class="nm">{nm}</div><div class="pr">{pr}<small> {unit}</small></div><div class="pm">{pm}</div><ul>' + "".join(f"<li>{x}</li>" for x in li) + "</ul></div>"
    return out + "</div>"

def page(body, foot, cls="pg"):
    return f'<section class="{cls}">{body}<div class="foot"><span><b>TWO&amp;HUMAN</b> · {foot}</span><span class="pgn"></span></div></section>\n'


def brands_page(d, f):
    tiles = "".join(f'<div class="bb"><img src="../../assets/brands/{b}.jpg"><span>{n}<small>{c}</small></span></div>' for b, n, c in d["brands"])
    apps = "".join(f'<span class="chip">{x}</span> ' for x in ["Logo y sistema", "Paleta y tipografía", "Cartelería", "Indumentaria", "Packaging", "Plantillas para redes"])
    bh = d.get("brand_h") or 'Cada cliente tiene <span class="mk">un mundo de marca, no solo un logo.</span>'
    bs = d.get("brand_side") or "Diseñamos cada punto de contacto: logo, paleta, cartelería, indumentaria, packaging y redes, con el mismo nivel de cuidado."
    return page(f'<div class="kick">05 · Presencia de marca</div><h2>{bh}</h2>'
                f'<div class="bw"><div class="bgrid">{tiles}</div>'
                f'<div class="card"><h3>Presencia, no solo un logo</h3><p>{bs}</p><div style="margin-top:6px">{apps}</div></div></div>'
                f'<p class="small" style="margin-top:12px">Marcas conceptuales creadas por TWO&amp;HUMAN para mostrar nuestra dirección de arte. Son marcas ficticias, no proyectos de clientes.</p>', f)

def build(d):
    f = d["foot"]
    h = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Propuesta — {d["name"]}</title>
<link rel="stylesheet" href="../../assets/pop.css"><style>body{{{d["vars"]}}}</style></head><body>\n'''
    # 1 portada
    h += page("".join(icon(n, s) for n, s in d["cover_icons"]) +
              f'<div class="kick">Propuesta para {d["name"]}</div><h1 style="max-width:6.2in">{d["title"]}</h1><p class="sub">{d["sub"]}</p>'
              f'<div class="meta"><div><b>Para</b>{d["para"]}</div><div><b>De</b>TWO&amp;HUMAN</div><div><b>Fecha</b>Noviembre 2026</div></div>',
              f, "pg grad")
    # 2 lo que vimos
    h += page(icon("magnifier", "width:1.9in;right:0.7in;top:0.45in") +
              f'<div class="kick">01 · Lo que vimos</div><h2>{d["vimos_h"]}</h2>' + stats(d["stats"]) +
              f'<div class="row c2" style="margin-top:16px"><div class="card tint"><h3>Lo bueno</h3><p>{d["bueno"]}</p></div><div class="card solid"><h3>La oportunidad</h3><p>{d["oport"]}</p></div></div>'
              f'<p class="small" style="margin-top:12px">{d["fuentes"]}</p>', f)
    # 3 fugas
    h += page(icon("prohibited", "width:1.7in;right:0.75in;top:0.4in", "i3 r2") +
              f'<div class="kick">02 · {d["fugas_k"]}</div><h2>{d["fugas_h"]}</h2>' + fugas(d["fugas"]) + bars(*d["bars"]) +
              (f'<p class="small" style="margin-top:10px">{d["fugas_nota"]}</p>' if d.get("fugas_nota") else ""), f)
    # 4 propuesta
    h += page(f'<div class="kick">03 · La propuesta</div><h2>{d["prop_h"]}</h2>' + steps(d["steps"]) + chips(d["prop_chips"], True), f)
    # 5 así se vería
    h += page(f'<div class="kick">04 · Así se vería</div><h2>{d["mock_h"]}</h2>' + d["mock"] +
              f'<p class="concept">{d["mock_note"]}</p>', f)
    k = 1 if d.get("brands") else 0
    if k:
        h += brands_page(d, f)
    # 6 90 días
    h += page(icon(d["plan_icon"], "width:1.6in;right:0.75in;top:0.4in", "i3 r1") +
              f'<div class="kick">{5+k:02d} · Primeros 90 días</div><h2>{d["plan_h"]}</h2>' + meses(d["meses"]) + chips(d["plan_chips"]), f)
    # 7 inversión
    h += page(icon(d["inv_icon"], "width:1.7in;right:0.7in;top:0.35in", "i3 r2") +
              f'<div class="kick">{6+k:02d} · Inversión (USD)</div><h2>{d["inv_h"]}</h2>' + opts(d["opts"]) +
              f'<div class="gar" style="margin-top:18px"><img src="{P('tick')}"><div>{d["garantia"]}</div></div>'
              f'<p class="small" style="margin-top:10px">{d["inv_nota"]}</p>', f)
    # 8 empecemos
    pasos = "".join(f'<div class="card" style="background:rgba(255,255,255,.14);box-shadow:none;color:#fff"><div class="num" style="background:#fff;color:{d["p1"]}">{i+1}</div><h3>{t}</h3><p style="color:rgba(255,255,255,.86)">{p}</p></div>' for i, (t, p) in enumerate(d["pasos"]))
    h += page(icon("check", "width:1.8in;right:0.8in;top:0.6in", "i3 r2") +
              f'<div class="kick">{7+k:02d} · Empecemos</div><h2 style="color:#fff">Tres pasos <span class="mk">y arrancamos.</span></h2><div class="row c3" style="max-width:8.2in">{pasos}</div>'
              f'<div style="display:flex;gap:28px;align-items:center;margin-top:30px">'
              f'<div style="display:flex;gap:12px;align-items:center"><div class="face" style="background-image:url(../../assets/img5/julio.jpg)"></div><div><b>Julio Briones</b><br><span style="font-size:9.4pt;opacity:.85">{d["rol_julio"]}</span></div></div>'
              f'<div style="display:flex;gap:12px;align-items:center"><div class="face" style="background-image:url(../../assets/img5/mariam.jpg)"></div><div><b>Mariam Neme</b><br><span style="font-size:9.4pt;opacity:.85">Ingeniera de software</span></div></div>'
              f'<div style="font-size:9.6pt;opacity:.92;margin-left:auto">julio@twoandhuman.com<br>WhatsApp +54 381 509 8972</div></div>',
              f'Estudio de marketing, diseño y software · {d["horario"]}', "pg grad")
    h += "<script>var p=document.querySelectorAll('.pg');p.forEach(function(e,i){var n=e.querySelector('.pgn');if(n)n.textContent=(i+1)+' / '+p.length;});</script></body></html>"
    open(os.path.join(HERE, d["slug"] + ".html"), "w").write(h)

def phone(grad, brand, t1, t2, fields, btn, btncol, pf):
    return (f'<div class="phone"><div class="scr lp"><div class="top" style="background:{grad}"><div class="brand">{brand}</div><div class="t1">{t1}</div><div class="t2">{t2}</div></div>'
            f'<div class="fm">' + "".join(f'<div class="f">{x}</div>' for x in fields) + f'<div class="btn" style="background:{btncol}">{btn}</div></div><div class="pf">{pf}</div></div></div>')

def wa(title, msgs, label="WhatsApp", bg=""):
    out = f'<div class="wa"{(" style=" + chr(34) + bg + chr(34)) if bg else ""}><div class="hd">{title} <span>{label}</span></div>'
    for who, txt, tm in msgs:
        if who == "auto":
            out += f'<div class="au">{txt}</div>'
        else:
            out += f'<div class="m{" me" if who == "me" else ""}">{txt}<small>{tm}</small></div>'
    return out + "</div>"

def pipe(cols, note):
    out = '<div><div class="pipe">'
    for h, cards in cols:
        out += f'<div class="col"><div class="h">{h}</div>' + "".join(f'<div class="c"><b>{a}</b>{b}</div>' for a, b in cards) + "</div>"
    return out + f'</div><p style="font-size:10.4pt;margin-top:14px">{note}</p></div>'

def mockrow(*parts, cols="2in 2.7in 1fr"):
    return f'<div style="display:grid;grid-template-columns:{cols};gap:26px;align-items:center">' + "".join(parts) + "</div>"

CLIENTS = [
dict(slug="biolaser", name="Biolaser Medicina Estética", foot="Biolaser", p1="#6c3cff",
 vars="--bg:#f6f2ff;--ink:#1b1338;--mut:#5f5a78;--p1:#6c3cff;--p2:#ff4f8b;--t1:#efe8ff;--hl:#ffc9dc;--hl2:#ffc94d;--b1:#d9c8ff;--b2:#ffd0e0;--g1:#6c3cff;--g2:#ff4f8b;--g3:#ffb37a;",
 cover_icons=[("megaphone","width:3.6in;right:0.5in;top:1.3in"),("calculator","width:1.7in;right:3.4in;top:4.3in;transform:rotate(-8deg)"),("target","width:1.5in;right:0.9in;top:4.6in")],
 title='De 82 mil seguidores a <span class="mk">turnos medibles.</span>',
 sub="Anuncios que se miden, landings por tratamiento y una agenda que responde sola.",
 para="Dra. Viviana Villalba y<br>Dr. Carlos Oliveira e Silva",
 vimos_h='Tienen lo más difícil: <span class="mk">audiencia y reputación.</span>',
 stats=[("82,3 mil","seguidores en Instagram"),("4,9 ★","en Google, con 87 reseñas"),("5","anuncios activos en Meta"),("12+","años de trayectoria")],
 bueno="Médicos visibles, tecnología aprobada por la FDA y pacientes que llegan hasta del exterior.",
 oport="Los anuncios terminan en un número de teléfono y sin medición: hoy no se sabe cuánto cuesta un paciente.",
 fuentes="Datos públicos del 24/11/2026: Instagram, Facebook, Biblioteca de anuncios de Meta, Google y biolaser.com.py.",
 fugas_k="Dónde se pierden pacientes", fugas_h='Tres fugas <span class="mk">entre el anuncio y el turno.</span>',
 fugas=[("Anuncian a ciegas","Sin Píxel ni GA4, Meta no aprende quién termina agendando.","0 conversiones medidas"),
        ("Todo termina en un número","Sin landing ni agenda, quien escribe de noche espera hasta el otro día.","Web: 10,2 s en el celular"),
        ("Una audiencia dormida","Unos 19 likes por post sobre 82 mil seguidores.","0,02 % de interacción")],
 bars=("Reseñas en Google",[("Velours",100,"1.278",False),("BL DermoEstética",11.5,"147",False),("Biolaser",6.8,"87",True)]),
 prop_h='Un sistema que <span class="mk">convierte anuncios en turnos.</span>',
 steps=[("megaphone","Anuncio por tratamiento","Botox, labios, hiperhidrosis y láser."),("target","Landing que convierte","Una página por tratamiento, rápida y con formulario."),
        ("calendar","Turno agendado","Respuesta automática por WhatsApp y recordatorios."),("growth","Todo medido","Costo por consulta y por turno, cada semana.")],
 prop_chips=["Píxel + API de Conversiones","GA4","CRM con agenda","Pedido de reseñas automático"],
 mock_h='Del anuncio al turno, <span class="mk">sin perder a nadie.</span>',
 mock=mockrow(phone("linear-gradient(150deg,#6c3cff,#ff4f8b)","BIOLASER","Hiperhidrosis: dejá de pensar en el sudor","Evaluación con la Dra. Villalba. Tecnología aprobada por la FDA.",["Nombre","WhatsApp","¿Qué día te queda mejor? ▾"],"Agendar mi evaluación","#6c3cff","★ 4,9 en Google · Asunción"),
   wa("Biolaser",[("me","Hola, vi el anuncio de hiperhidrosis 🙂","22:14"),("auto","Respuesta automática",""),("them","¡Hola, Ana! Te paso horarios para tu evaluación: ¿martes 10:00 o jueves 17:30?","22:14"),("me","Jueves 17:30","22:16"),("them","¡Listo! Te agendamos ✓ Te recordamos el miércoles.","22:16")]),
   pipe([("Nuevas · 12",[("Ana G.","Hiperhidrosis"),("Lucía R.","Labios")]),("Turno · 9",[("Ana G.","Jue 17:30"),("Sofía L.","Vie 10:00")]),("Contactadas · 7",[("María P.","Pidió precio")]),("Asistieron · 21",[("Carla M.","Reseña pedida ✓")])],
        "El equipo ve cada mañana quién escribió, quién falta agendar y a quién pedirle la reseña.")),
 mock_note="Concepto preliminar. Textos finales según las políticas de salud de Meta y la aprobación de la clínica.",
 plan_icon="calendar", plan_h='En 90 días, <span class="mk">números reales.</span>',
 meses=[("Medir y conectar",["Píxel, GA4 y eventos","Landings de 3 tratamientos","CRM, WhatsApp y recordatorios"]),
        ("Anuncios que aprenden",["Campañas optimizadas hacia turnos","Pedido de reseñas automático","Primer informe con costo por turno"]),
        ("Escalar lo que funciona",["Más inversión en lo que agenda","Reactivación de pacientes","Reunión de resultados"])],
 plan_chips=["Costo por turno, cada semana","Respuesta inmediata, también de noche","Landings en menos de 2,5 s"],
 inv_icon="piggy", inv_h='Elijan <span class="mk">cuánto acompañamiento</span> quieren.',
 opts=[("Medir y agendar","450","/mes","+ USD 1.800 de implementación",["Medición, landings y CRM","Automatizaciones al día","Informe mensual"],False),
       ("Anuncios que agendan","750","/mes","+ USD 1.800 de implementación",["Todo lo anterior","Gestión de anuncios en Meta","6 creatividades por mes","Informe semanal"],True),
       ("Clínica completa","1.250","/mes","+ USD 1.800 de implementación",["Todo lo anterior","12 publicaciones por mes, sobre todo reels","Campaña de reseñas"],False)],
 garantia="<b>Garantía de medición.</b> Si a los 30 días del lanzamiento no ven cuánto cuesta cada consulta y cada turno, el segundo mes no se cobra.",
 inv_nota="Ejemplo: con un ticket promedio de USD 150, 5 pacientes nuevos por mes cubren la opción recomendada. Implementación 50 % al inicio y 50 % al entregar · mínimo 3 meses · CRM incluido · anuncios pagados directo a Meta (sugerido desde USD 300/mes).",
 pasos=[("Llamada de 20 min","Revisamos juntos los anuncios actuales."),("Accesos","Meta, web y WhatsApp, todo a nombre de Biolaser."),("Medición en 2 semanas","Primer informe real al final del mes 1.")],
 rol_julio="Estrategia y anuncios", horario="mismo horario que Paraguay"),

dict(slug="odontoandrauss", name="Clínica Odontoandrauss", foot="Odontoandrauss", p1="#00a99d",
 vars="--bg:#effbf8;--ink:#0c2a3a;--mut:#4f6672;--p1:#00a99d;--p2:#2f6bff;--t1:#dcf6f1;--hl:#ffe58a;--hl2:#ffc93c;--b1:#bfeee6;--b2:#cfe0ff;--g1:#00b3a6;--g2:#2f6bff;--g3:#ffc93c;",
 cover_icons=[("calendar","width:3in;right:0.8in;top:1.1in;transform:rotate(6deg)"),("megaphone","width:2.2in;right:3.5in;top:4.2in"),("check","width:1.4in;right:0.9in;top:4.7in")],
 title='Cinco sedes, <span class="mk">una sola agenda.</span>',
 sub="Anuncios por ciudad, turnos por sede y una puerta en portugués para los pacientes de Brasil.",
 para="Dra. Gabriela González y<br>Dr. César Fiori",
 vimos_h='25 años de confianza, <span class="mk">casi sin marketing.</span>',
 stats=[("5","sedes en Gran Asunción y Tobatí"),("4,8 ★","en Google, con unas 169 reseñas"),("25+","años, desde 2000"),("0","anuncios en Meta")],
 bueno="Red familiar con radiología propia y pacientes que los recomiendan solos, también en portugués.",
 oport="No publican desde el 13/10, la web no deja agendar y un solo WhatsApp atiende a cinco sedes.",
 fuentes="Datos públicos del 24/11/2026: Instagram, Facebook, TikTok, Biblioteca de anuncios de Meta, directorios que replican Google y odontoandrauss.com.py.",
 fugas_k="Oportunidades", fugas_h='Tres oportunidades <span class="mk">sobre la mesa.</span>',
 fugas=[("Cero anuncios con 5 sedes","Cada sede podría tener su propia campaña por ciudad.","0 anuncios en Meta"),
        ("Una web que no agenda","Promos de 2023 y, para pedir turno, solo WhatsApp o teléfono.","Última promo: febrero 2023"),
        ("Brasil sin puerta","Según BBC News Brasil, más de la mitad de las residencias de 2025 fueron para brasileños.","Nada en portugués")],
 bars=("Likes por post en su cuenta: las colaboraciones rinden hasta 7 veces más",[("Con @josenoparaguay",100,"81",False),("Con @dhenyferlovato",70,"57",False),("Posts propios",14,"11,4",True)]),
 prop_h='Cada paciente, <span class="mk">en la sede correcta.</span>',
 steps=[("megaphone","Anuncio por ciudad","Ortodoncia e implantes en cada zona."),("target","Página de sede","Dirección, horarios, especialistas y reseñas."),
        ("calendar","Turno en su sede","El WhatsApp pregunta la sede y agenda solo."),("growth","Seguimiento","Recordatorios y presupuestos que no se enfrían.")],
 prop_chips=["5 agendas en un CRM","WhatsApp que deriva","Landing en portugués","Fichas de Google por sede"],
 mock_h='Del anuncio al sillón, <span class="mk">en español o en portugués.</span>',
 mock=mockrow(phone("linear-gradient(150deg,#00b3a6,#2f6bff)","ODONTOANDRAUSS","Dentista em Assunção para toda a família","Ortodontia, implantes e estética. 25 anos cuidando de sorrisos no Paraguai.",["Nome","WhatsApp","Unidade mais próxima ▾"],"Agendar minha avaliação","#00a99d","★ 4,8 no Google · 5 unidades"),
   wa("Odontoandrauss",[("me","Hola, quiero consultar por ortodoncia","21:40"),("auto","Respuesta automática",""),("them","¡Hola! ¿En qué sede te queda mejor?<br>1 Asunción · 2 San Lorenzo · 3 Luque · 4 Ñemby · 5 Tobatí","21:40"),("me","3","21:41"),("them","En Luque tenemos lugar el martes 16:00 o el miércoles 10:30. ¿Cuál preferís?","21:41")]),
   pipe([("Asunción · 14",[("Ortodoncia","8 turnos"),("Implantes","6 turnos")]),("San Lorenzo · 9",[("Ortodoncia","9 turnos")]),("Luque · 7",[("Implantes","7 turnos")]),("Em português · 5",[("Todas las sedes","5 consultas")])],
        "Turnos nuevos de la semana por sede, tratamiento y canal. Números de ejemplo.")),
 mock_note="Concepto preliminar. Textos finales en español y portugués según la aprobación de la clínica y las políticas de salud de Meta.",
 plan_icon="growth", plan_h='En 90 días, <span class="mk">cada sede con su agenda llena.</span>',
 meses=[("Agendas en marcha",["5 calendarios y WhatsApp que deriva","Recordatorios de turno","Medición en la web"]),
        ("Anuncios por ciudad",["Ortodoncia e implantes por zona","Campaña en portugués","Web por sede y tratamiento"]),
        ("Más pacientes por sede",["Más inversión donde agenda","Seguimiento de presupuestos","Informe por sede"])],
 plan_chips=["Turnos por sede, cada semana","Menos ausentismo","Consultas en portugués, medidas aparte"],
 inv_icon="calculator", inv_h='Elijan <span class="mk">cuánto acompañamiento</span> quieren.',
 opts=[("Agenda por sede","450","/mes","+ USD 2.400 de implementación",["CRM con 5 agendas","Web por sede y landing en portugués","Informe mensual por sede"],False),
       ("Pacientes nuevos por sede","850","/mes","+ USD 2.400 de implementación",["Todo lo anterior","Anuncios por ciudad y tratamiento","Campaña en portugués","8 creatividades por mes"],True),
       ("Red completa","1.400","/mes","+ USD 2.400 de implementación",["Todo lo anterior","8 reels por mes","Una colaboración mensual con creadores"],False)],
 garantia="<b>Garantía de puesta en marcha.</b> Si a los 30 días de recibir los accesos las cinco agendas no están recibiendo turnos, el primer mes no se cobra.",
 inv_nota="Ejemplo: con un tratamiento promedio de USD 500, dos pacientes nuevos por mes en toda la red cubren la opción recomendada. Implementación 50 % al inicio y 50 % al entregar · mínimo 3 meses · CRM incluido · anuncios pagados directo a Meta (sugerido desde USD 500/mes para 5 ciudades) · honorarios de creadores aparte.",
 pasos=[("Llamada de 20 min","Cómo agenda hoy cada sede."),("Accesos","WhatsApp, web, Meta y Google, todo a nombre de la clínica."),("Agendas en 30 días","Primer informe por sede al final del mes 1.")],
 rol_julio="Estrategia y anuncios", horario="mismo horario que Paraguay"),

dict(slug="unilaser", name="Clínica Unilaser", foot="Clínica Unilaser", p1="#2948ff",
 vars="--bg:#f4f6ff;--ink:#0d1b2e;--mut:#55607a;--p1:#2948ff;--p2:#ffb703;--t1:#e4e9ff;--hl:#ffe29a;--hl2:#ffb703;--b1:#c9d3ff;--b2:#ffe7b0;--g1:#0d1b4c;--g2:#2948ff;--g3:#ffb703;",
 cover_icons=[("growth","width:3.6in;right:0.5in;top:1.4in"),("target","width:1.8in;right:3.6in;top:4.2in;transform:rotate(-6deg)"),("check","width:1.3in;right:0.9in;top:4.8in")],
 title='Que su inversión <span class="mk">rinda más pacientes.</span>',
 sub="Velocidad, medición completa y seguimiento bilingüe dentro de su GoHighLevel.",
 para="Dr. Juan Fidel Díez y equipo<br>Clínica Unilaser, Medellín",
 vimos_h='Ya hacen lo difícil. <span class="mk">Falta que nada se escape.</span>',
 stats=[("4,9 ★","en Google, con 208 reseñas, varias en inglés"),("~13","anuncios activos en Meta"),("32,2 mil","seguidores en Instagram"),('<span style="font-size:30pt">GA4 + GHL</span>',"ya instalados")],
 bueno="Web bilingüe, valoración virtual y pacientes de EE. UU. que también llegan por Bookimed y WhatClinic.",
 oport="La web tarda 7,1 s en el celular y no vemos el Píxel de Meta: los anuncios de WhatsApp optimizan a ciegas.",
 fuentes="Datos públicos del 24/11/2026: perfiles sociales, Biblioteca de anuncios de Meta, Google, código y Lighthouse móvil de clinicaunilaser.com. El píxel podría estar fuera de la home: lo confirmamos con ustedes.",
 fugas_k="Dónde se escapa la inversión", fugas_h='No les falta marketing. <span class="mk">Les sobran segundos.</span>',
 fugas=[("Una web pesada","La home pesa 11,7 MB y tarda 7,1 s en el celular.","Objetivo: 2,5 s"),
        ("Meta sin píxel visible","Meta optimiza hacia conversaciones, no hacia valoraciones.","A confirmar con ustedes"),
        ("Un viaje largo","Valoración, presupuesto, seña y viaje, sin un seguimiento bilingüe visible.","4 etapas por paciente")],
 bars=("Home en el celular: hoy y objetivo",[("Carga hoy",100,"7,1 s",True),("Objetivo",35,"2,5 s",False),("Peso hoy",100,"11,7 MB",True),("Objetivo",26,"3 MB",False)]),
 fugas_nota="Según Google, más de la mitad de las visitas desde el celular se abandonan si la página tarda más de 3 segundos.",
 prop_h='Optimizar lo que tienen, <span class="mk">no empezar de cero.</span>',
 steps=[("megaphone","Anuncio","Meta y Google, como hoy."),("target","Landing en 2,5 s","Liviana, en español e inglés."),
        ("calendar","Valoración virtual","Respuesta en menos de 5 minutos, en su idioma."),("check","Seña y viaje","Secuencia automática hasta que llega.")],
 prop_chips=["Píxel + API de Conversiones","Eventos de WhatsApp en GA4","Flujos en su GoHighLevel","Junto a su equipo o agencia"],
 mock_h='Un paciente en Texas, <span class="mk">atendido a las 11 de la noche.</span>',
 mock=mockrow('<div style="display:grid;gap:14px"><div class="card" style="text-align:center;background:#ffe3dc"><div class="big" style="color:#c0392b;font-size:34pt">7,1 s</div><div class="lbl">carga en el celular, hoy</div></div><div class="card" style="text-align:center;background:#dcf5e7"><div class="big" style="color:#1d7a4a;font-size:34pt">≤ 2,5 s</div><div class="lbl">objetivo de las landings</div></div></div>',
   wa("Unilaser",[("me","Hi! I saw your ad. How much are veneers?","23:08"),("auto","Automatic reply · English",""),("them","Hi Jessica! Prices depend on your case, so we start with a virtual consultation. Does Tuesday 9:00 or Wednesday 15:00 (Colombia time) work?","23:08"),("me","Wednesday works 🙌","23:11"),("them","Booked ✓ We'll send a reminder and a short guide about traveling to Medellín.","23:11")]),
   pipe([("Lead · EN/ES",[("Jessica T.","Texas · carillas"),("Andrés M.","Medellín · implantes")]),("Valoración",[("Jessica T.","Mié 15:00 · virtual")]),("Presupuesto",[("Mark R.","Enviado · día 2 de 5")]),("Seña y viaje",[("Linda K.","Seña ✓ · llega 12/01")])],
        "Cada paciente avanza con mensajes en su idioma; el equipo interviene donde hace falta."), cols="2.3in 2.7in 1fr"),
 mock_note="Concepto preliminar. Nombres y mensajes de ejemplo; textos finales según la aprobación de la clínica.",
 plan_icon="calendar", plan_h='En 90 días, <span class="mk">más rápido y mejor medido.</span>',
 meses=[("Medir y acelerar",["Píxel, API y eventos en GA4","Home y landings más livianas","Informe antes y después"]),
        ("Seguimiento bilingüe",["Respuesta automática 24/7","Secuencia para pacientes internacionales","Recordatorios y cobro de seña"]),
        ("Convertir más",["Una prueba A/B por mes","Embudo medido por idioma","Ajustes junto a su equipo"])],
 plan_chips=["Landings en 2,5 s o menos","Respuesta en menos de 5 min","Costo por valoración, por campaña"],
 inv_icon="piggy", inv_h='Desde una mejora puntual <span class="mk">hasta setting bilingüe.</span>',
 opts=[("Velocidad y medición","1.800","único","Sin mensualidad",["Home y landings optimizadas","Píxel, API y eventos en GA4","Informe antes y después"],False),
       ("Velocidad + seguimiento","650","/mes","+ USD 2.600 de implementación",["Todo lo anterior","Flujos bilingües en su GoHighLevel","Una prueba A/B por mes","Informe del embudo por idioma"],True),
       ("+ Setting bilingüe","1.600","/mes","+ USD 2.600 de implementación",["Todo lo anterior","Atención de leads en inglés y español","Agenda de valoraciones y seguimiento"],False)],
 garantia="<b>Garantía de velocidad.</b> Si las landings de anuncios no bajan de 3,5 s en el celular (Lighthouse móvil), devolvemos la parte de velocidad: USD 1.200.",
 inv_nota="Ejemplo: con un diseño de sonrisa de USD 3.000, un paciente internacional más cada cuatro meses cubre la opción recomendada. Implementación 50 % al inicio y 50 % al entregar · mínimo 3 meses · trabajamos en su GoHighLevel · la inversión en anuncios no cambia.",
 pasos=[("Llamada de 20 min","Confirmamos el píxel y el recorrido actual."),("Accesos de lectura","GA4, Meta, GoHighLevel y la web."),("Primer informe","Medición y velocidad al final de la semana 1.")],
 rol_julio="Estrategia y seguimiento bilingüe", horario="cubrimos el horario de Colombia"),

dict(slug="ava7", name="AVA7 Propiedades", foot="AVA7 Propiedades", p1="#0b7fb3",
 vars="--bg:#fff6ef;--ink:#13232f;--mut:#5c6670;--p1:#ff6b4a;--p2:#0094c6;--t1:#ffe6dc;--hl:#ffd6a5;--hl2:#ffc145;--b1:#ffd2c2;--b2:#c6ecf7;--g1:#0b7fb3;--g2:#00b8a9;--g3:#ffc145;",
 cover_icons=[("boxes","width:3.2in;right:0.7in;top:1.2in"),("calendar","width:1.8in;right:3.6in;top:4.2in;transform:rotate(-8deg)"),("megaphone","width:1.9in;right:0.7in;top:4.7in")],
 title='Que los propietarios <span class="mk">lleguen solos.</span>',
 sub="Anuncios para captar propietarios en Viña, Reñaca y Concón, y un CRM que no deja escapar a nadie.",
 para="Peterson Laguerre y equipo<br>AVA7 Propiedades",
 vimos_h='Tienen la promesa y el rostro. <span class="mk">Falta capturarlo.</span>',
 stats=[("39 mil","seguidores de Peterson"),("5,0 ★","en Google, con 45 reseñas"),("43+","propiedades en stock"),("0","anuncios para captar propietarios")],
 bueno="“Venta garantizada en 90 días”, reels semanales que funcionan y un equipo de 10 personas con 9 años en el rubro.",
 oport="La audiencia vive en la cuenta personal de Peterson y los interesados se responden a mano: no quedan en ningún CRM.",
 fuentes="Datos públicos del 24/11/2026: Instagram, Facebook, TikTok, Biblioteca de anuncios de Meta, Google, ava7propiedades.cl y perfil en 2x3.cl.",
 fugas_k="Dónde se pierde el valor", fugas_h='El alcance ya lo tienen. <span class="mk">Falta retenerlo.</span>',
 fugas=[("Todo en una cuenta","39 mil seguidores en @asesor.peterson y 3,2 mil en la marca.","Los contactos dependen de una persona"),
        ("Sin anuncios a propietarios","La promesa de vender en 90 días no se está pautando.","0 anuncios activos"),
        ("Comentarios que se pierden","Un post del 7/11 sumó 547 comentarios, respondidos a mano.","547 en un solo post")],
 bars=("Seguidores en Instagram: ya son la marca más seguida de su zona",[("@asesor.peterson",100,"39 mil",False),("@ava7propiedades",8.2,"3.179",True),("Ajelvez",7.1,"2.755",False),("LW Propiedades",6,"2.352",False),("Ciany",3,"1.174",False)]),
 prop_h='Un sistema para captar <span class="mk">propietarios todos los días.</span>',
 steps=[("megaphone","Anuncio a propietarios","Viña del Mar, Reñaca y Concón."),("target","Landing de 90 días","Formulario de tasación en un minuto."),
        ("calendar","Tasación agendada","Respuesta, calificación y recordatorio automáticos."),("check","Captación firmada","Y seguimiento hasta vender o arrendar.")],
 prop_chips=["CRM con 4 tableros","«Comenta INFO» automático","Agenda conectada","Una sola página de Facebook"],
 mock_h='Del reel a la tasación, <span class="mk">sin que nadie quede sin respuesta.</span>',
 mock=mockrow(phone("linear-gradient(150deg,#0b7fb3,#00b8a9)","AVA7 PROPIEDADES","Vende o arrienda tu propiedad en 90 días","Viña del Mar, Reñaca y Concón. Déjanos tus datos y coordinamos la tasación.",["Comuna ▾","Tipo de propiedad ▾","Teléfono"],"Quiero mi tasación","#ff6b4a","★ 5,0 en Google · 45 reseñas"),
   wa("Mensaje directo",[("them","<b>camila.v</b> comentó INFO en tu reel 🙌",""),("auto","Respuesta automática",""),("them","¡Hola, Camila! Te dejo la ficha del depto 👉 ¿Lo buscas para comprar o para arrendar?","21:02"),("me","Para comprar","21:03"),("them","¡Genial! ¿Te agendo una visita esta semana? 📅","21:03")],"Instagram","background:#f1eefb"),
   pipe([("Propietario nuevo",[("Pedro S.","Casa · Concón · venta"),("Ana L.","Depto · Viña · arriendo")]),("Tasación agendada",[("Pedro S.","Jue 11:00")]),("Tasado",[("Luis M.","Propuesta enviada")]),("Captado",[("Marta R.","Firmado ✓ · 90 días")])],
        "Tablero de propietarios. Compradores y arrendatarios tienen el suyo.")),
 mock_note="Concepto preliminar. Nombres y mensajes de ejemplo; textos finales según la aprobación de AVA7. Automatización con herramientas oficiales de Meta.",
 plan_icon="growth", plan_h='En 90 días, <span class="mk">tasaciones que llegan cada semana.</span>',
 meses=[("CRM y landing",["4 tableros: propietarios, compradores y arrendatarios","Instagram automatizado","Landing de 90 días con medición"]),
        ("Anuncios de captación",["Campañas por comuna","Creatividades con los reels de Peterson","Informe semanal de tasaciones"]),
        ("Marca que crece",["Más inversión en lo que capta","Colaboraciones que suman a la marca","Facebook unificado"])],
 plan_chips=["Tasaciones por comuna, cada semana","Respuesta inmediata a comentarios","Costo por tasación medido"],
 inv_icon="calculator", inv_h='Elijan <span class="mk">cuánto acompañamiento</span> quieren.',
 opts=[("CRM y automatización","400","/mes","+ USD 1.900 de implementación",["CRM con 4 tableros","Instagram automatizado","Landing de propietarios"],False),
       ("Propietarios que llegan solos","750","/mes","+ USD 1.900 de implementación",["Todo lo anterior","Anuncios de captación por comuna","Creatividades con los reels de Peterson","Informe semanal"],True),
       ("Marca que crece","1.200","/mes","+ USD 1.900 de implementación",["Todo lo anterior","8 reels por mes","Plan de colaboraciones para la marca"],False)],
 garantia="<b>Ustedes garantizan 90 días; nosotros, los primeros 60.</b> Con al menos USD 400/mes en anuncios, si en 60 días no llegan 15 solicitudes de tasación de propietarios, el tercer mes no se cobra.",
 inv_nota="Ejemplo con su propia publicación: una casa de UF 6.099 con honorarios de 2 % + IVA deja UF 122 + IVA, unos USD 5.100: más de seis meses de la opción recomendada (UF y dólar aproximados). Implementación 50 % al inicio y 50 % al entregar · mínimo 3 meses · CRM incluido · anuncios pagados directo a Meta.",
 pasos=[("Llamada de 20 min","Qué comunas y propiedades priorizar."),("Accesos","Meta, Instagram, web y agenda, todo a nombre de AVA7."),("Primeras tasaciones","Anuncios en marcha desde la semana 3.")],
 rol_julio="Estrategia y anuncios", horario="cubrimos el horario de Chile"),
]

if __name__ == "__main__":
    for c in CLIENTS:
        build(c)
        print("ok", c["slug"])
