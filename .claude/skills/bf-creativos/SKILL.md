---
name: bf-creativos
description: 'Define y escribe las piezas de una campaña de Black Friday (o Cyber Monday, Hot Sale y otras fechas de descuentos) para Meta Ads y redes: lista de piezas por fase (se viene, revelación, venta, cuenta regresiva, últimas horas, se terminó), formatos 4:5 y 9:16, reglas de diseño para que no parezca plantilla ni IA, textos de anuncio, ganchos, guion de reel de 15 segundos y prompts para generar flyers con IA. Úsala cuando el usuario pida "flyers de Black Friday", "piezas para el Black Friday", "textos para los anuncios del Black Friday", "prompt para el flyer", "qué pongo en el flyer" o "reel para el Black Friday".'
---

# Piezas de Black Friday

Cada pieza tiene un trabajo según la fase: avisar, mostrar la oferta, empujar a decidir o cerrar. Si una pieza intenta hacer todo, no hace nada.

## Paso 1: Lista de piezas por fase

| Fase | Pieza | Formato | Mensaje |
|---|---|---|---|
| Calentamiento | "Se viene" | Video corto 9:16 + estático 4:5 | Fecha y adelanto, más la invitación a la lista VIP ("Respondé BLACK") |
| Cuenta regresiva | Revelación de ofertas, una por pieza | 4:5 y stories | Un producto o combo con su precio real y el ahorro |
| Venta | Flyer de precios "desde" | 4:5 | 3 a 7 productos con su precio, sin tabla amontonada |
| Venta | Combo o beneficio por monto | 4:5 + 9:16 | Una sola promo grande y su condición |
| Venta | Video de productos | Reel de 15 s | Gancho, producto, oferta y CTA |
| Retargeting | Objeción principal | 4:5 | Envío, pago, garantía o "cómo se compra" |
| Retargeting | Cuenta regresiva | Stories | Días u horas que quedan hasta el cierre real |
| Cierre | Últimas horas | 9:16 | Hora exacta del cierre |
| Posventa | Se terminó + gracias | Stories | Agradecimiento y cupón para después |

## Paso 2: Formatos

- **Feed:** 4:5, 1080 × 1350 px.
- **Stories y reels:** 9:16, 1080 × 1920 px. En stories, deja libres unos 250 px arriba y abajo; en reels, más espacio abajo, donde van el texto y los botones.
- Haz cada pieza en los dos formatos cuando vaya a anuncios: Meta la muestra mejor en cada ubicación.

## Paso 3: Reglas de diseño (para que no parezca plantilla ni IA)

1. **Una sola jerarquía:** primero el título, después la oferta y el resto chico. Si todo es grande, nada se lee.
2. **Poco texto:** entre 4 y 6 bloques. Lo que sobra va al texto del anuncio o a una segunda imagen del carrusel.
3. **Fotos reales de los productos.** Los productos inventados, con etiquetas que no existen, se notan y bajan la confianza.
4. **Precios reales y legibles.** Sin precios anteriores tachados que no se cobraron.
5. **Espacio vacío:** al menos un cuarto de la pieza sin elementos.
6. **Pocas tipografías:** una gruesa para el título y los precios, una simple para el resto y, si hace falta, una a mano para una sola palabra.
7. **Colores planos y de la marca:** sin brillos, degradés ni sombras en las letras.
8. **Coherencia con el chat:** lo que dice la pieza es lo mismo que se responde por WhatsApp.

## Paso 4: Textos del anuncio

**Estructura del texto principal** (los primeros 125 caracteres son los que se ven antes del "ver más"):
1. Gancho con la oferta.
2. Qué incluye.
3. Condición y fecha real.
4. Llamado a la acción.

**Plantillas de gancho** (adaptarlas al negocio, siempre con datos reales):
- "[Producto] desde $[precio]. Solo hasta el [día] [fecha]."
- "Combo [nombre]: por separado $[A], este Black Friday $[B]."
- "Comprá más de $[monto] y [beneficio], solo por Black Friday."
- "Lo que esperabas para comprar [producto]: [oferta]."
- "Quedan [N] [productos] al precio de Black Friday." (solo si el número es real y se actualiza)
- "Escribinos por WhatsApp y te pasamos todos los precios."

**Título:** corto, de hasta unos 40 caracteres, con la oferta o la fecha.
**Botón:** "Enviar mensaje" si se cierra por WhatsApp; "Comprar" si se cierra en la web.

Para más variaciones, usa `ads-copy` y `ads-hooks`.

## Paso 5: Guion de reel de 15 segundos

| Segundos | Imagen | Texto en pantalla | Voz o subtítulo |
|---|---|---|---|
| 0-2 | Producto o combo en primer plano | Gancho con la oferta | "[Producto] desde $[precio]" |
| 2-8 | Productos en uso o cómo se arma el combo | Qué incluye | "Llevás [A], [B] y [C]" |
| 8-12 | Condición o prueba (pedidos que salen, local) | Fecha y condición | "Solo hasta el [fecha]" |
| 12-15 | Logo y botón | CTA | "Escribinos por WhatsApp" |

Subtítulos siempre: la mayoría lo ve sin sonido. Para guiones más largos, usa `ads-video`.

## Paso 6: Prompt para generar un flyer con IA

```
Te adjunto [N] fotos de mis productos y [1 o 2] imágenes de referencia.
- De la referencia [describirla] copiá SOLO [la estructura / los colores / el estilo]. No copies sus textos, fotos, códigos QR ni marcas de agua.
Formato: vertical 4:5 (1080 x 1350 px).
Productos: tienen que verse 100 % iguales a las fotos: misma forma, colores, envase y etiqueta. No inventes productos ni textos en los envases.
Estilo: pocos elementos y mucho espacio vacío; una sola jerarquía (el título es lo más grande, después la oferta); colores planos, sin degradés, brillos ni sombras en las letras.
Textos, solo estos y escritos exactamente así:
1. [Ubicación]: "[texto]"
2. ...
No agregues ningún otro texto, ni precios tachados, ni nada en inglés. Revisá letra por letra la ortografía, las tildes y cada precio.
```

Cómo usarlo:
- **Un flyer por mensaje.** El segundo, en el mismo chat, con "mismo estilo, solo cambian estos textos".
- **Corrige de a una cosa:** "Corregí solo [X], sin cambiar nada más del diseño".
- **Si los productos o las letras no quedan bien después de dos intentos,** genera la base sin productos y agrega las fotos reales y los textos en Canva.

## Checklist antes de subir

- [ ] Precios, fechas y condiciones confirmados por el negocio.
- [ ] Ortografía y tildes revisadas letra por letra.
- [ ] Se entiende en 2 segundos y sin sonido.
- [ ] Versión 4:5 y 9:16, con el texto fuera de las zonas que tapan los botones.
- [ ] La oferta coincide con el chat, la web y el local.

Para un brief a diseñador o editor, usa `ads-creative`. Para cargar las piezas en las campañas, sigue con `bf-meta-campana`.
