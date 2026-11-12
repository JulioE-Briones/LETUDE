---
name: bf-monitoreo
description: 'Sigue y optimiza una campaña de Black Friday (o Cyber Monday, Hot Sale y otras fechas de descuentos) en Meta Ads mientras corre: números objetivo, tablero diario que cruza el gasto con las ventas reales de WhatsApp o la tienda, revisión tres veces al día, reglas para subir, mantener, rotar o apagar, reporte diario para el cliente, cierre ordenado y análisis final con aprendizajes. Úsala cuando el usuario pregunte "cómo va el Black Friday", "subo o bajo el presupuesto", "apago este anuncio", "reporte del Black Friday", "qué miro en los anuncios" o pegue resultados de la campaña durante la promo.'
---

# Monitoreo de Black Friday

En una promo de pocos días no hay tiempo de esperar una semana para decidir. Se miran los números varias veces por día y se actúa con reglas definidas antes de empezar.

## Paso 1: Números objetivo (antes de prender)

- **Costo máximo por venta:** sale de `bf-oferta`.
- **Tasa de cierre:** de cada 10 conversaciones, cuántas compran. Usa el dato histórico del negocio o un supuesto explícito.
- **Costo objetivo por conversación** (si se vende por WhatsApp) = costo máximo por venta × tasa de cierre.
- **Meta de la promo:** ventas o facturación totales.

## Paso 2: Tablero diario

Una planilla con una fila por día (y por campaña, si hay varias):

| Fecha | Gasto | Conversaciones o compras en Meta | Ventas reales | Facturación | Costo por venta | Facturación ÷ gasto | Ganancia después de anuncios |
|---|---|---|---|---|---|---|---|

- **Las ventas reales salen del negocio**, de las etiquetas "Compró" de WhatsApp (`bf-whatsapp`) o de la tienda, no solo de lo que dice Meta.
- **Ganancia después de anuncios** = ganancia de las ventas − gasto en anuncios. Es el número que importa. Facturar mucho con pérdida no es un buen Black Friday.

## Paso 3: Revisión durante la promo

Tres veces por día: a la mañana, al mediodía y a la noche. En cada revisión, en este orden:

1. **¿Está todo entregando?** Anuncios rechazados, conjuntos que no gastan, método de pago o límite de gasto.
2. **¿El gasto va según el plan?**
3. **Costo por resultado** de cada conjunto y anuncio, contra el objetivo.
4. **Porcentaje de clics y frecuencia** (cuántas veces vio el anuncio cada persona), sobre todo en el retargeting.
5. **Comentarios y mensajes:** dudas repetidas, quejas, stock agotado.
6. **El chat:** cuántas conversaciones quedaron sin responder o sin cerrar.

## Paso 4: Reglas de decisión

Son orientativas: ajústalas a los números del negocio y no decidas con muy pocos datos.

| Situación | Qué hacer |
|---|---|
| Anuncio rechazado | Corregir lo que marca Meta y reenviarlo en el momento |
| Un conjunto no gasta | Revisar el público (muy chico), el presupuesto y la fecha de inicio; si sigue, duplicarlo |
| Costo por resultado igual o menor al objetivo, con volumen | Subir el presupuesto 20-30 % o duplicar el conjunto |
| Costo por resultado hasta 1,5 veces el objetivo | Mantener y sumar una pieza nueva |
| Gastó 2 veces el costo objetivo sin resultados, o el costo es más de 1,5 veces el objetivo | Apagar ese anuncio o conjunto y pasar el presupuesto al que funciona |
| La frecuencia sube (por ejemplo, más de 3 en pocos días) y cae el porcentaje de clics | Rotar la pieza: misma oferta, otra imagen o gancho |
| Muchas conversaciones y pocas ventas | El problema está en el chat (demora, precio, condiciones), no en el anuncio: revisar con `bf-whatsapp` |
| Se agotó un producto | Apagar ya los anuncios de ese producto y avisar en el chat |
| Faltan pocas horas para el cierre | Pasar presupuesto al retargeting y a la pieza de últimas horas |

**Durante la promo, evita cambios grandes** de público o de creatividad en los conjuntos que funcionan: reinician el aprendizaje. Suma lo nuevo en un conjunto aparte.

## Paso 5: Reporte diario para el cliente

```
BLACK FRIDAY — [NEGOCIO] — [día y fecha]
Gasto de hoy: $[x] (acumulado $[y] de $[presupuesto])
Conversaciones/compras: [n] · Ventas reales: [n] · Facturación: $[x]
Costo por venta: $[x] (objetivo $[y])
Lo mejor de hoy: [pieza o público]
Qué cambiamos: [acción]
Para mañana: [acción]
```

## Paso 6: Cierre y análisis final

1. **A la hora del cierre:** verificar que todo quedó apagado o terminado.
2. **Guardar públicos** para las fiestas y la próxima fecha: compradores del Black Friday, personas que escribieron y no compraron, y quienes interactuaron.
3. **Reporte final:**

```
RESULTADO BLACK FRIDAY [AÑO] — [NEGOCIO]
Gasto total: $[x] · Ventas: [n] · Facturación: $[x] · Ganancia después de anuncios: $[x]
Costo por venta: $[x] (objetivo $[y])
Mejor oferta: [...] · Mejor pieza: [...] · Mejor público: [...]
Lo que no funcionó: [...]
Para la próxima: [3 cambios concretos]
Próximo paso: [campaña de fiestas / reactivación de compradores]
```

Nunca inventes métricas: si falta un dato, deja `[DATO]` y explica de dónde se saca.
