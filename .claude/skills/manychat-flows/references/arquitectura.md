# Arquitectura del flujo

```
[Reel / Carrusel / Story] --palabra clave--> [Respuesta pública al comentario]
                                   |
                                   v
                          [DM: entrega del recurso]
                                   |
                                   v
                    [Calificar: 2-3 preguntas con botones]
                         |                         |
                    calificado               no calificado
                         |                         |
              [Agendar llamada (link)]   [Recurso alternativo]
                         |                         |
             [Recordatorio 24 h si no]   [Loop de re-enganche]
                         |
                  [Llamada agendada → tag + aviso al usuario]
```

## Nomenclatura sugerida
- Tags: `kw_[palabra]`, `calificado`, `no_calificado`, `agendo`, `reenganche`.
- Campos personalizados: `objetivo`, `situacion`, `presupuesto`.

## Preguntas de calificación (ejemplos con botones)
1. ¿Cuál es tu situación hoy? → [Recién empiezo] [Ya facturo] [Facturo y quiero escalar]
2. ¿Qué te frena más? → [Conseguir clientes] [Cerrar ventas] [Tiempo]
3. ¿Estás listo para invertir en resolverlo este mes? → [Sí] [Más adelante]

Regla típica: calificado = situación ≠ "Recién empiezo" Y respuesta 3 = "Sí". Ajustar a la oferta del usuario.

## Ventana de 24 h
Instagram permite mensajes libres hasta 24 h después del último mensaje del usuario. Para re-enganchar después, la persona debe volver a escribir o hay que usar los tipos de mensaje que Meta permite. Diseña el re-enganche dentro de la ventana o pidiendo una respuesta corta que la reabra.
