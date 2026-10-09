---
name: manychat-flows
description: 'Diseña automatizaciones de ManyChat para Instagram listas para armar paso a paso: palabra clave en Reel, carrusel o story → entrega de recurso → calificación del prospecto → agenda de llamada, más un loop de re-enganche para los no calificados. Úsala cuando el usuario pida "automatizar con ManyChat", "flujo de ManyChat", "automatizar la palabra clave", "respuesta automática a comentarios", "comment to DM" o "agendar llamadas automáticamente por DM".'
---

# Flujos de ManyChat

Entrega un plano completo del flujo y las instrucciones para construirlo en ManyChat. Claude no tiene acceso a la cuenta de ManyChat del usuario: él lo arma siguiendo el plano. Nunca digas que el flujo quedó creado o activado.

## Paso 1: Datos
- Palabra(s) clave y dónde se usan (Reel, carrusel, story, live).
- Recurso a entregar (link o archivo).
- Oferta y quién califica (2 o 3 criterios concretos).
- Link de agenda (Calendly, Google Calendar, etc.).
- Recurso o contenido para los no calificados.
Si falta algo, pregúntalo en un solo mensaje y usa marcadores `[LINK]` para lo demás.

## Paso 2: Plano del flujo
Lee `references/arquitectura.md` y entrega:

1. **Disparadores**: un trigger por formato (comentario en publicación con la palabra, respuesta a story con la palabra, DM con la palabra) y la respuesta pública al comentario (3 variantes para que no parezca bot).
2. **Mensaje de entrega**: saludo + botón con el recurso. Si se usa "seguir para recibir", indica cómo configurarlo.
3. **Calificación**: 2 o 3 preguntas con botones de respuesta rápida (no texto libre), con la etiqueta (tag) y el campo personalizado que guarda cada respuesta.
4. **Condición**: calificado / no calificado según las respuestas.
5. **Calificado**: mensaje con el beneficio de la llamada + botón al link de agenda + recordatorio si no agenda en 24 h.
6. **No calificado**: mensaje amable + recurso alternativo + tag para el loop de re-enganche.
7. **Re-enganche**: secuencia de 2 o 3 mensajes con valor en los días siguientes, que respeten la ventana de 24 h de Instagram (fuera de esa ventana, solo mensajes permitidos por Meta).
8. **Paso a humano**: cuándo avisar al usuario (palabras como "precio", "hablar con alguien", respuestas fuera del guion).

Escribe cada mensaje completo, en tono humano, de 1 a 3 líneas, en el idioma y estilo del usuario.

## Paso 3: Guía de construcción
Después del plano, da los pasos en orden para crearlo en ManyChat (Automatizaciones → nueva automatización → disparador → bloques de mensaje → condiciones → acciones de etiqueta). Si la interfaz cambió, indica qué buscar por nombre y pide una captura para ajustar.

## Paso 4: Prueba
Checklist: probar cada palabra clave desde otra cuenta, revisar que los tags se apliquen, que los botones abran bien y que el no calificado no reciba el link de agenda.

## Reglas
- Respeta las políticas de Instagram/Meta: nada de mensajes masivos fuera de la ventana permitida ni prometer resultados.
- No inventes funciones de ManyChat; si no estás seguro de que algo exista en el plan del usuario, dilo.
