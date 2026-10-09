# LETUDE

Sitio web estático (`index.html`, `letude-abogados.html`) más un kit de skills de negocio en `.claude/skills/`.

## Idioma

Responde siempre en español. Los documentos que generen las skills (OFFER.md, PITCH.md, plan de negocio, etc.) también van en español, aunque las instrucciones de la skill estén en inglés.

## Skills de negocio (Hormozi + founder pack)

Se pueden invocar a mano con `/nombre-de-la-skill`, o usarse solas cuando el pedido encaje. Guía para pedidos en español:

| Si el usuario pide… | Usa |
|---|---|
| crear una oferta, "oferta irresistible", "grand slam offer" | `hormozi-offer` (desde cero) o `founder-offer` (mejorar una existente) |
| revisar por qué una oferta no vende | `audit-offer` |
| ángulos, posicionamiento, enfoques de mensaje | `offer-angles` |
| bonos, garantía, apilar valor | `bonus-stack` |
| que la oferta parezca más valiosa | `value-perception` |
| resultados más rápidos, onboarding, "quick win" | `value-accelerator` |
| simplificar, reducir fricción o esfuerzo del cliente | `effort-reduction` |
| hecho para ti / contigo / por ti mismo | `dfy-dwy-diy` |
| cuánto cobrar, precios, niveles | `pricing-strategy` (o `founder-pricing` después del panel de consumidores) |
| márgenes, punto de equilibrio, números, rentabilidad | `founder-cfo` |
| qué modelo de negocio usar | `business-model` |
| objeciones, "el cliente duda" | `objection-destroyer` |
| pitch de venta | `hormozi-pitch` |
| ganchos / hooks para posts, anuncios o emails | `hormozi-hooks` |
| página de ventas, landing page | `landing-page-copy` |
| plan de marketing, canales, campaña | `founder-marketing` |
| nombre, marca, eslogan, voz | `founder-brand` |
| plan de lanzamiento | `founder-launch` |
| evaluar una idea de negocio, "¿funcionaría?" | `founder-board` |
| encontrar mercado o nicho, validar demanda | `market-research` |
| competencia | `founder-competitors` |
| "¿la gente lo compraría?", simular clientes | `founder-consumer` |
| de idea a oferta y pitch en un solo flujo | `idea-to-product` |
| convertir servicios en productos, escalera de ofertas | `productize` |
| operaciones, proveedores, procedimientos, permisos | `founder-ops` |
| plan de negocio completo | `founder-plan` (al final del founder pack) |

Orden sugerido del founder pack: `founder-board` → `founder-competitors` → `founder-consumer` → `founder-pricing` → `founder-offer` → `founder-cfo` → `founder-marketing` → `founder-brand` → `founder-ops` → `founder-launch` → `founder-plan`.

Fuentes (licencia MIT): github.com/alexsmedile/hormozi-skills y github.com/Jakeschincariol/founder-skill. Índice original en `.claude/skills/INDICE.md`.

## Skills de anuncios pagados (media buyer)

Para todo lo de publicidad pagada (Meta, Google, LinkedIn, TikTok) usa estas skills del repo antes que las skills genéricas de anuncios.

| Si el usuario pide… | Usa |
|---|---|
| revisión rápida, "¿estoy listo para anunciar?" | `ads-quick` |
| auditar campañas existentes, "mis anuncios no rinden" | `ads-audit` |
| a quién dirigir los anuncios, personas, segmentación | `ads-audience` |
| embudo de anuncios, retargeting, estrategia completa | `ads-funnel` |
| textos de anuncios, variaciones de copy | `ads-copy` |
| ganchos para anuncios pagados | `ads-hooks` (para contenido orgánico, `hormozi-hooks`) |
| guion de video para anuncio, Reels, TikTok | `ads-video` |
| brief para diseñador o editor | `ads-creative` |
| revisar una landing que recibe tráfico de anuncios | `ads-landing` (para escribir una página de ventas desde una oferta, `landing-page-copy`) |
| cuánto invertir y cómo repartir el presupuesto | `ads-budget` |
| plan de pruebas A/B | `ads-testing` |
| anuncios de la competencia | `ads-competitors` (para mapear competidores del negocio, `founder-competitors`) |
| palabras clave de Google Ads | `ads-keywords` |

Orden sugerido para una campaña nueva: `ads-quick` → `ads-audience` → `ads-competitors` → `ads-funnel` → `ads-copy` / `ads-hooks` / `ads-video` → `ads-creative` → `ads-landing` → `ads-budget` → `ads-testing`.

## Skills de VSL (cartas de ventas en video)

| Si el usuario pide… | Usa |
|---|---|
| guion de VSL, video de ventas para cualquier producto, servicio o curso; reescribir o auditar un guion | `vsl-scriptwriter` |
| VSL de software o producto digital donde la demo convence; videos de upsell (OTO); storyboard, narración y animación | `video-sales-letter` |
| guion corto para un anuncio en video (15, 30 o 60 s) | `ads-video` |

Antes de escribir un VSL conviene tener la oferta clara (`hormozi-offer` o `founder-offer`) y las objeciones (`objection-destroyer`). Fuentes (MIT): github.com/ai-saas-wizard/vsl-scriptwriter y github.com/bertrand-do/video-sales-letter. Índice original en `.claude/skills/INDICE-vsl.md`.

## Skills de Reels y video corto orgánico (Reels, TikTok, Shorts)

Para contenido orgánico de video corto usa estas skills del repo antes que las skills genéricas de redes sociales o video.

| Si el usuario pide… | Usa |
|---|---|
| un guion, un reel, un tiktok, "guion en mi voz", un tema para grabar | `reels-en-mi-voz` (por defecto) |
| guion con estructura de retención o un carrusel, sin necesidad de su voz | `viral-short-form` |
| ganchos / hooks para video orgánico, criticar un hook | `viral-hooks` (para anuncios pagados, `ads-hooks`; para posts y emails con estilo Hormozi, `hormozi-hooks`) |
| ideas de contenido, "no sé qué publicar", pilares, calendario de ideas | `viral-short-form-ideas` |
| algo específico de Instagram: Trial Reels, envíos, por qué falló un reel | `viral-instagram-reels` |
| algo específico de TikTok: FYP, sonidos, TikTok Shop | `viral-tiktok-content` |
| algo específico de YouTube Shorts o llevar de Shorts a videos largos | `viral-youtube-shorts` |
| caption, texto en pantalla, hashtags, CTA, comentario fijado | `viral-captions-and-ctas` |

Flujo típico: `viral-short-form-ideas` → `reels-en-mi-voz` (con `viral-hooks` si se quieren más hooks) → la skill de la plataforma para ajustar → `viral-captions-and-ctas`.

`reels-en-mi-voz` aprende la voz del usuario de `.claude/skills/reels-en-mi-voz/references/mis-guiones.md`. Si ese archivo sigue con el texto de ejemplo, pide al usuario de 3 a 10 de sus mejores guiones y guárdalos ahí, separados por `---`.

Fuente de las skills `viral-*` (licencia MIT): github.com/vyralcontent/content-skills. Índice original en `.claude/skills/INDICE-reels.md`.

## Skills de carruseles e Instagram

| Si el usuario pide… | Usa |
|---|---|
| un carrusel para vender, generar leads o llamadas, "Comentá PALABRA", DMs automáticos | `carrusel-cta-palabra-clave` (por defecto para carruseles, también LinkedIn) |
| un carrusel de valor para guardados, compartidos o seguidores (lista, antes/después, mito, framework) | `ig-carousel-planner` |
| caption para una imagen o un Reel de Instagram | `ig-caption-writer` (para captions de video en TikTok o Shorts, `viral-captions-and-ctas`) |
| analizar un post ajeno que funcionó y sacar la fórmula del hook | `ig-hook-extractor` |
| convertir un artículo, video, post de LinkedIn o hilo en contenido de Instagram | `ig-repurposer` |

Notas sobre las `ig-*`:
- Mencionan `ig-humanizer` e `ig-hashtag-strategist`, que **no están instaladas**. En su lugar, aplica `references/voice-rules.md` (limpieza de tics de IA) y `references/hashtag-strategy.md` de la propia skill.
- Pueden publicar vía Publora, pero eso **no está configurado** (no hay `PUBLORA_API_KEY` ni `lib/publora_client.py`). Entrega siempre el texto listo para copiar y recuerda adjuntar las imágenes en Instagram. Nunca publiques sin que el usuario lo pida.
- Leen `references/voice-profile.md` (hay una copia en cada skill `ig-*`). Si el usuario comparte su voz, completa los cuatro archivos igual y pon `filled: yes`. Los guiones de `reels-en-mi-voz/references/mis-guiones.md` sirven como fuente.

Fuente de las `ig-*` (licencia MIT): github.com/sergebulaev/instagram-skills. Índice original en `.claude/skills/INDICE-carruseles.md`.

## Skill de Stories

| Si el usuario pide… | Usa |
|---|---|
| stories, historias, secuencia de stories, stories para vender o generar DMs, o dice el objetivo de sus historias de hoy | `secuencia-stories` |

Arma 8 stories (intro, dolor, solución, prueba social, beneficio, CTA suave, aporte de valor, CTA final "Respondé INFO") más 2 DMs de seguimiento. Aprende de `.claude/skills/secuencia-stories/references/mi-historial.md`. Cuando el usuario cuente cuántos DMs, llamadas o ventas generó una secuencia, guárdalo ahí. Índice original en `.claude/skills/INDICE-stories.md`.

Las tres skills de DMs (`carrusel-cta-palabra-clave`, `secuencia-stories` y `objection-destroyer` para responder dudas en el chat) forman un mismo embudo: contenido → palabra clave → DM → llamada.

## Skills de calendario y planificación de contenido

| Si el usuario pide… | Usa |
|---|---|
| calendario de contenido, plan del mes, parrilla, "qué publico este mes" | `calendario-contenido` (por defecto; 30 días en Autoridad / Testimonio / Conversión, desde la oferta y el avatar) |
| plan semanal de Instagram con mezcla de formatos, horarios y meta de guardados y envíos | `ig-content-planner` |
| ideas sueltas, "no sé qué publicar", pilares de contenido | `viral-short-form-ideas` |

Para todo lo de planificación de contenido usa estas skills del repo antes que las genéricas de estrategia de contenido o redes sociales.

Cada fila del calendario se desarrolla con la skill de su formato: Reel → `reels-en-mi-voz`, carrusel → `carrusel-cta-palabra-clave` o `ig-carousel-planner`, stories → `secuencia-stories`, caption → `ig-caption-writer`. Para el mapa de objeciones del calendario, `objection-destroyer`. Índice original en `.claude/skills/INDICE-calendario.md`.

Fuente de las skills de anuncios (licencia MIT): github.com/zubair-trabzada/ai-ads-claude. Índice original en `.claude/skills/INDICE-ads.md`. A las descripciones de estas skills se les añadieron frases de activación ("Use when…") para que se activen con pedidos naturales.
