---
name: bf-oferta
description: 'Diseña la oferta de Black Friday (o Cyber Monday, Hot Sale y otras fechas de descuentos) sin regalar el margen: calcula cuánto descuento aguanta cada producto, cuánto más hay que vender para ganar lo mismo y arma la oferta con gancho, combos, beneficio por monto con tope, descuento por medio de pago y cupón para después, con condiciones claras y legales. Úsala cuando el usuario pregunte "qué descuento pongo", "cuánto puedo bajar", "armame la oferta del Black Friday", "conviene 10 % o un monto fijo", "combos para el Black Friday" o cuando el negocio tenga poco margen.'
---

# Oferta de Black Friday que no regala el margen

El error más caro en estas fechas es bajar precios a ciegas: se vende más y se gana menos. Esta skill arma una oferta que atrae, sube el ticket y deja ganancia.

## Paso 1: Datos

Para cada producto o categoría principal:
- Precio de venta.
- Costo del producto.
- Costos variables por venta: comisión del medio de pago, envío si lo paga el negocio, empaque.
- Stock disponible.

Además: ticket promedio, objetivo de la fecha (liquidar stock, clientes nuevos o subir el ticket) y si el negocio vende por mayor o por menor.

Si el usuario no tiene los costos, pide al menos el margen aproximado. Sin margen, no recomiendes un porcentaje: da la tabla del paso 2 y pide el dato.

## Paso 2: Cuánto descuento aguanta

**Margen** = (precio − costo − costos variables) ÷ precio.
Ejemplo: precio $10.000, costo $7.000, comisión $500 → ganancia $2.500 → margen 25 %.

**Descuento máximo sin perder plata** = el margen. Con un margen del 25 %, un descuento del 25 % deja la venta en cero.

**Cuántas veces más hay que vender para ganar lo mismo** = margen ÷ (margen − descuento):

| Margen \ Descuento | 5 % | 10 % | 15 % | 20 % | 25 % |
|---|---|---|---|---|---|
| 20 % | 1,33 veces | 2 veces | 4 veces | no queda ganancia | pierde plata |
| 30 % | 1,2 veces | 1,5 veces | 2 veces | 3 veces | 6 veces |
| 40 % | 1,14 veces | 1,33 veces | 1,6 veces | 2 veces | 2,67 veces |
| 50 % | 1,11 veces | 1,25 veces | 1,43 veces | 1,67 veces | 2 veces |

Muestra siempre esta cuenta con los números del negocio. Si para ganar lo mismo hay que vender 3 veces más, el descuento probablemente es demasiado alto.

## Paso 3: Arma la oferta con palancas que cuestan poco

Combina 2 o 3 de estas palancas, no todas:

| Palanca | Cómo funciona | Cuándo conviene |
|---|---|---|
| **Gancho** | 1 a 3 productos con descuento fuerte y unidades contadas | Para que la gente escriba o entre; la ganancia está en lo que suma después |
| **Combos o kits** | Varios productos juntos con descuento sobre el total ("por separado $X, en combo $Y") | Sube el ticket y mueve stock lento junto con productos que salen solos |
| **Regalo por monto** | Un producto de costo bajo y valor percibido alto, a partir de cierto monto | Margen chico: cuesta menos que un descuento y sube el ticket |
| **Beneficio por monto con tope** | Monto fijo en compras grandes ("$5.000 en compras de más de $100.000") | Mejor que un porcentaje sin tope, que crece con el pedido |
| **Descuento por medio de pago** | Porcentaje extra pagando en efectivo o por transferencia | Compensa la comisión que se ahorra el negocio |
| **Cuotas sin interés** | Financiación sin recargo | Solo si el negocio puede absorber el costo financiero |
| **Acceso anticipado** | La lista VIP ve los precios o compra antes que el resto | Arma demanda antes de la fecha, sin costo extra |
| **Cupón para después** | Cupón para usar en diciembre o en la próxima compra | Hace que vuelvan; el costo se paga solo si hay otra venta |
| **Suma en el chat** | Al cerrar: "Si querés, agregale [producto] por $[precio]" | Sube el ticket sin tocar la oferta principal |

Ubica el umbral del beneficio por monto un poco arriba del ticket promedio, para que la gente sume productos para llegar.

## Paso 4: Cómo comunicarla

- **Regla del 100:** en productos de precio bajo, el porcentaje suena más grande ("30 % off"). En montos altos, suena más grande el monto en pesos ("$5.000 menos").
- **"Desde $X" solo si existe** un producto a ese precio, con stock.
- **Muestra el ahorro real:** precio por separado contra precio del combo, nunca un precio anterior inventado.
- **Una promo grande por pieza.** Si el flyer tiene tres promos, no se entiende ninguna.
- **Condiciones en una línea:** fechas, tope, medios de pago y stock.

## Paso 5: Honestidad y ley

- No subas precios antes de la fecha para después "bajarlos".
- Muestra un precio anterior tachado solo si se cobró de verdad en los días previos.
- El stock que se anuncia tiene que existir: si se agota, se avisa y se apaga el anuncio de ese producto.
- La fecha límite se cumple: si la promo se estira, la próxima vez nadie cree en la urgencia.
- En Argentina rigen la Ley de Defensa del Consumidor (24.240) y las normas de lealtad comercial; en otros países, la norma local.

## Entregable

```
OFERTA BLACK FRIDAY — [NEGOCIO]
Vigencia: [desde fecha y hora] a [hasta fecha y hora]

| Pieza | Qué es | Costo para el negocio | Condición | Texto corto para anuncios |
|---|---|---|---|---|
| Gancho | ... | ... | Stock: [N] unidades | ... |
| Combo 1 | ... | ... | ... | "Por separado $X, en combo $Y" |
| Beneficio por monto | ... | Máximo $[tope] por compra | Compras de más de $[monto] | ... |

Margen promedio después de la oferta: [x %]
Ventas necesarias para ganar lo mismo que un mes normal: [número]
Costo máximo por venta que se puede pagar en anuncios: [número] (pasa a bf-meta-campana)
Condiciones (letra chica): [texto]
```

Termina con la próxima acción: confirmar costos, elegir los productos gancho o pasar a `bf-calendario`.
