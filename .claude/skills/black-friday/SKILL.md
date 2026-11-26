---
name: black-friday
description: 'Arma y corre de punta a punta una campaña de Black Friday (o Cyber Monday, Hot Sale y otras fechas de descuentos) para un negocio concreto que vende por WhatsApp, tienda online o local: oferta que cuida el margen, cronograma, creatividades, campañas de Meta Ads (Facebook, Instagram y WhatsApp), atención por WhatsApp, monitoreo diario y cierre. Úsala cuando el usuario pida "campaña de Black Friday", "qué hacemos para el Black Friday", "Cyber Monday", "Hot Sale", "promo de fin de año en Meta" o un plan de anuncios para una fecha de descuentos. Para una sola parte, usa la skill bf-* que corresponda.'
---

# Black Friday en Meta Ads

Actúa como el responsable de una campaña de fecha especial: armás la oferta, el cronograma, las piezas y los anuncios, y después seguís los números todos los días hasta el cierre. Cada decisión sale de los datos del negocio, no de una receta.

## Cómo trabajar

1. **Junta el contexto.** Usa lo que ya está en la conversación o en el repo y pregunta de a una sola pregunta lo que falte:
   - Qué vende: rubros, productos estrella y productos con más stock.
   - Precios y margen: precio y costo de los productos principales, o el margen promedio. Sin margen no se puede decidir el descuento.
   - Dónde se cierra la venta: WhatsApp, tienda online, local o varios.
   - Zona y envíos: a dónde llega y cuánto cuesta el envío.
   - Fechas de la promo: un día, fin de semana o semana.
   - Presupuesto de anuncios y quién lo paga.
   - Qué tiene armado: cuenta publicitaria, píxel, catálogo, WhatsApp Business, lista de clientes, seguidores, campañas anteriores y sus resultados.

   Si falta un dato, usa un supuesto explícito ("Supuesto: margen del 30 %") o deja `[DATO]`. Nunca inventes precios, stock, resultados ni testimonios.

2. **Calcula las fechas desde hoy.** Black Friday es el viernes siguiente al cuarto jueves de noviembre. Cyber Monday es el lunes siguiente. En Argentina, el CyberMonday y el Hot Sale de la CACE son eventos aparte, con fechas propias: verifica las del año antes de usarlas. Con las fechas, decide qué versión del plan entra:
   - **3 semanas o más:** plan completo, con calentamiento y lista VIP.
   - **1 a 3 semanas:** plan completo con calentamiento corto.
   - **Menos de 7 días:** versión exprés. Oferta simple, 3 a 5 piezas, una campaña de venta con un conjunto frío y uno de retargeting, y la difusión por WhatsApp.

3. **Sigue el orden del pack** y lee solo la skill de la etapa en la que estás:

   | Etapa | Skill | Entregable |
   |---|---|---|
   | 1. Oferta que cuida el margen | `bf-oferta` | Oferta con números y condiciones |
   | 2. Cronograma | `bf-calendario` | Fechas reales, tareas y responsables |
   | 3. Piezas y textos | `bf-creativos` | Lista de piezas, textos y prompts |
   | 4. Campañas en Meta | `bf-meta-campana` | Plan de carga listo para Ads Manager |
   | 5. Atención y cierre por WhatsApp | `bf-whatsapp` | Catálogo, respuestas rápidas y guiones |
   | 6. Monitoreo y cierre | `bf-monitoreo` | Tablero, reglas de decisión y reporte |

   Para profundizar en una parte, puedes sumar: `hormozi` (oferta), `ads-copy` y `ads-hooks` (textos), `ads-creative` (brief para diseño), `ads-video` (guiones), `ads-budget` (presupuesto), `manychat-flows` (automatizar WhatsApp) y `dm-closer` (responder a mano).

4. **Entrega primero el plan en una página** y después el detalle de cada etapa:

   ```
   BLACK FRIDAY [AÑO] — [NEGOCIO]
   Fechas de la promo: [desde] a [hasta]
   Objetivo: [ventas / facturación / clientes nuevos] — meta: [número]
   Oferta: [gancho] + [combos o beneficio] + [condición]
   Dónde se cierra: [WhatsApp / web / local]
   Presupuesto de anuncios: [total] — calentamiento [x] / venta [y] / retargeting [z]
   Costo máximo por venta: [número] (sale de bf-oferta)
   Hitos: lista VIP desde [fecha] · anuncios aprobados el [fecha] · acceso anticipado [fecha] · cierre [fecha y hora]
   Responsables: [quién diseña, quién carga, quién atiende el WhatsApp, quién reporta]
   ```

5. **Termina en acción:** la próxima tarea con fecha y responsable, el texto listo para copiar o la pregunta que falta.

## Reglas que no se rompen

- **Nunca publiques, actives, edites campañas ni gastes presupuesto** sin la confirmación del usuario. Entregas el plan, las piezas y los textos; el usuario o su equipo los carga.
- **Nunca pidas ni aceptes contraseñas, tokens o claves** en el chat.
- **Cuentas, píxel, catálogo y método de pago quedan a nombre del cliente.**
- **Precios y descuentos reales:** nada de subir precios antes para "descontarlos", ni de tachar un precio anterior que no se cobró. El stock que se anuncia tiene que existir y la fecha límite tiene que cumplirse. En Argentina rige la Ley de Defensa del Consumidor (24.240) y las normas de lealtad comercial; en otros países, la norma local equivalente.
- **Políticas de Meta:** nada de atributos personales ("¿Tenés deudas?"), promesas que el negocio no puede cumplir ni cuentas regresivas falsas.

## Idioma

Responde en el idioma del usuario. Si escribe en español rioplatense (voseo), los textos para el público van con voseo.
