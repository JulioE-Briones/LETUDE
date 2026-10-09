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

Fuente de las skills de anuncios (licencia MIT): github.com/zubair-trabzada/ai-ads-claude. Índice original en `.claude/skills/INDICE-ads.md`. A las descripciones de estas skills se les añadieron frases de activación ("Use when…") para que se activen con pedidos naturales.
