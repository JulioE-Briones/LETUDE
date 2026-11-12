---
name: bf-whatsapp
description: 'Prepara la atención y el cierre por WhatsApp para Black Friday (o Cyber Monday, Hot Sale y otras fechas de descuentos): perfil y catálogo de WhatsApp Business, mensaje de bienvenida y de ausencia, respuestas rápidas, etiquetas, lista VIP y difusión, guiones para precio, envío, pago y stock, suma de productos para subir el ticket, recordatorio de cierre y posventa con cupón. Úsala cuando el usuario pida "cómo atiendo el WhatsApp en el Black Friday", "respuestas rápidas", "mensaje de bienvenida para la promo", "lista VIP", "mensaje de difusión" o "qué le respondo a los que preguntan por la promo".'
---

# WhatsApp para Black Friday

Si la venta se cierra por WhatsApp, ahí se gana o se pierde la campaña. Un anuncio que trae conversaciones no sirve si nadie responde a tiempo o si cada respuesta se escribe desde cero.

## Paso 1: Preparación (5 días antes de la promo)

En WhatsApp Business:
- **Perfil:** logo, descripción con lo que vende, dirección, horario y link.
- **Catálogo:** los productos y combos de la promo, con foto real y precio.
- **Mensaje de bienvenida** (para quien escribe por primera vez):
  > ¡Hola! Gracias por escribirnos 🙌 Esta semana tenemos Black Friday: [oferta principal]. ¿Qué estás buscando? Así te paso precios y opciones.
- **Mensaje de ausencia** (fuera del horario):
  > ¡Hola! Ahora estamos fuera de horario. Te respondemos mañana desde las [hora], y la promo te la respetamos igual.
- **Respuestas rápidas,** con un atajo cada una:

  | Atajo | Para qué |
  |---|---|
  | `/precios` | Lista de precios de la promo o link al catálogo |
  | `/combo` | Combos con lo que incluyen y el ahorro real |
  | `/envio` | Zonas, costo y plazos de envío |
  | `/retiro` | Dirección, horario y beneficio por retiro, si lo hay |
  | `/pago` | Medios de pago y descuento por transferencia, si lo hay |
  | `/stock` | Cómo se reserva y por cuánto tiempo |
  | `/datos` | Resumen del pedido con total y datos para pagar |
  | `/gracias` | Confirmación del pago y cuándo llega o se retira |

- **Etiquetas:** VIP, Preguntó, Esperando pago, Compró, Entregado.
- **Equipo:** quién atiende y en qué horarios. En los días fuertes, suma una persona o amplía el horario.
- **Registro de pedidos:** una planilla simple con fecha, cliente, productos, total y estado. Sirve también para medir cuántas ventas trajo la campaña.

## Paso 2: Lista VIP y difusión

- **Cómo se arma:** en stories y publicaciones, "Respondé BLACK y te pasamos los precios antes que a nadie". A cada persona que responde, se le pide que agende el número del negocio.
- **Por qué agendar:** las listas de difusión de WhatsApp solo llegan a quienes tienen el número agendado.
- **Cuántos mensajes:** como mucho 3 o 4 en toda la campaña: aviso de que se viene, acceso anticipado, apertura de la promo y últimas horas.
- **Nunca le mandes mensajes masivos a gente que no te escribió o que no agendó el número.** Además de molestar, puede hacer que WhatsApp restrinja la cuenta.

## Paso 3: Guiones

**Llega alguien desde el anuncio:**
> ¡Hola [nombre]! Sí, la promo sigue hasta el [día] a las [hora]. ¿Qué estás buscando? Te paso lo que mejor te sirve.

**"¿Precio?":**
> [Producto] está a $[precio] por Black Friday. Si lo combinás con [producto 2], el combo queda en $[precio combo] (por separado serían $[suma]). ¿Te reservo alguno?

**"¿Hacen envíos?":**
> Sí, enviamos a [zonas]. El envío cuesta $[costo] y llega en [plazo]. Si preferís, podés retirarlo en [dirección].

**Para subir el ticket, cuando está cerca del monto del beneficio:**
> Te faltan $[diferencia] para llegar a los $[monto] y que te [beneficio]. ¿Querés sumar [producto sugerido]?

**Cierre:**
> Te paso el resumen: [productos] — Total: $[total]. Podés pagar por [medios]. Te reservo el pedido hasta [hora o día].

**Recordatorio, uno solo, el último día, a los que preguntaron y no compraron:**
> ¡Hola [nombre]! Te escribo porque hoy a las [hora] termina el Black Friday. Si todavía querés [producto], te lo reservo ahora.

**Posventa:**
> ¡Gracias por tu compra, [nombre]! Te dejamos un cupón de [beneficio] para usar hasta el [fecha]. Y si te gustó, nos ayuda mucho una reseña acá: [link].

## Reglas

- **Responde rápido.** Una consulta que llega por un anuncio se enfría pronto: si tarda horas, compra en otro lado.
- **No prometas stock que no hay.** Si se agota, avisa y ofrece otra opción.
- **Las condiciones, siempre por escrito** en el resumen del pedido.
- **Nunca pidas datos de tarjeta por chat.** Usa link de pago, transferencia o los medios formales del negocio.
- **Etiqueta cada venta como "Compró":** Meta no sabe cuántas conversaciones terminaron en venta, y ese dato lo necesita `bf-monitoreo`.

Si el volumen supera lo que se puede responder a mano, propón automatizar la bienvenida y la calificación con `manychat-flows`. Para responder un caso puntual que el usuario pega, usa `dm-closer`.
