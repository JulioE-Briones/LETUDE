# Anuncio → WhatsApp → calificación A/B/C

Método para negocios donde la venta se cierra conversando, y especialmente cuando no conviene que entre cualquiera (ticket alto, admisión, servicios profesionales).

## El camino

Anuncio segmentado → WhatsApp con mensaje inicial → 3 a 6 preguntas (en el chat o en un formulario breve) → puntaje A, B o C → acción según el tipo → registro en planilla.

## 1. Mensaje inicial del anuncio

El texto que el usuario envía al tocar el botón ya dice de qué anuncio viene. Uno distinto por conjunto:
- "Hola, vi el anuncio de [tema/público] y quiero más información."

Así se sabe qué público trae mejores interesados sin depender de Meta.

## 2. Respuesta automática (saludo)

Corta, humana y con una pregunta:
> ¡Hola! Gracias por escribir a [negocio]. Para ayudarte mejor, ¿me contás [pregunta 1]?

Si el filtro es largo, se manda un formulario (Google Forms o el formulario instantáneo de Meta) en lugar de preguntar todo por chat.

## 3. Preguntas de calificación

Entre 3 y 6, de opción múltiple, en este orden:
1. **Necesidad:** qué busca o qué problema tiene.
2. **Encaje:** zona, tipo de cliente, si cumple el requisito básico.
3. **Momento:** para cuándo lo necesita.
4. **Capacidad:** rango de presupuesto o si conoce el precio (sin incomodar).
5. **Origen:** cómo conoció al negocio.
6. **Contacto y consentimiento:** "Acepto que [negocio] use estos datos solo para responder mi consulta."

Nunca preguntes por religión, ideas, salud (salvo que sea un servicio de salud y sea necesario), origen ni otros datos sensibles.

## 4. Puntaje

| Tipo | Cuándo | Qué se hace |
|---|---|---|
| **A** | Encaja, lo necesita pronto, conoce el precio | Contacto personal en menos de 24-48 h: llamada, visita o turno |
| **B** | Encaja pero no es para ahora, o tiene dudas | Mensaje de valor periódico y seguimiento a los 7 días |
| **C** | No encaja | Agradecimiento amable y, si corresponde, derivación |

Define con el cliente qué respuestas suman para A antes de lanzar. Escríbelo.

## 5. Seguimiento

- A sin respuesta: segundo mensaje a las 24 h, tercero a los 3 días.
- Visita o consulta sin decisión: mensaje a las 24 h y a los 7 días.
- Nunca más de 3 intentos sin respuesta.

## 6. Planilla

Una fila por interesado: fecha, anuncio/público de origen, respuestas, puntaje, próximo paso, resultado (cliente sí/no), monto. Es la fuente para el reporte y para decidir el presupuesto: **la plata va a los públicos que traen más A, no más mensajes.**

## 7. Automatización

- Manual con WhatsApp Business (respuestas rápidas y etiquetas A/B/C) alcanza para empezar.
- Para automatizar el flujo de botones, usa `manychat-flows`. Para responder a mano conversaciones difíciles, `dm-closer`.
