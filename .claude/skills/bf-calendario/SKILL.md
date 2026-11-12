---
name: bf-calendario
description: 'Arma el cronograma de una campaña de Black Friday (o Cyber Monday, Hot Sale y otras fechas de descuentos) con fechas reales calculadas desde hoy: preparación, calentamiento con lista VIP, cuenta regresiva, acceso anticipado, días de venta, cierre y posventa, con tareas, responsables y entregables por día, en orgánico, anuncios y WhatsApp. Úsala cuando el usuario pregunte "cuándo arranco", "armame el cronograma del Black Friday", "qué hago cada día", "plan día por día" o "me quedan pocos días para el Black Friday".'
---

# Cronograma de Black Friday

Convierte la oferta en un plan con fechas reales. Cada día tiene una tarea, un responsable y algo que se entrega.

## Paso 1: Fechas

- **D** = primer día de la promo. Black Friday es el viernes siguiente al cuarto jueves de noviembre; Cyber Monday, el lunes siguiente. En Argentina, el CyberMonday y el Hot Sale de la CACE tienen fechas propias: verifícalas.
- **Cierre** = último día y hora de la promo.
- **Hoy:** cuenta los días que faltan hasta D y elige la versión del plan.

Escribe siempre la fecha real y el día de la semana (por ejemplo, "jueves 19/11"), no solo "D−8". Verifica el día de la semana antes de entregar.

## Paso 2: Fases (plan completo, desde 3 semanas antes)

| Fase | Cuándo | Qué se hace | Orgánico | Anuncios | WhatsApp |
|---|---|---|---|---|---|
| **Preparación** | D−21 a D−15 | Oferta cerrada con números (`bf-oferta`), stock y precios confirmados, checklist técnico de Meta, producción de piezas | — | Revisar cuenta, píxel, catálogo, método de pago y límite de gasto | Catálogo, respuestas rápidas, etiquetas |
| **Calentamiento** | D−14 a D−4 | Anunciar que se viene y armar la lista VIP | "Se viene", detrás de escena, encuesta de qué producto quieren | Video o pieza "Se viene" para sumar público de retargeting | Anotar a quien responde "BLACK" y pedirle que agende el número |
| **Cuenta regresiva** | D−3 a D−1 | Mostrar las ofertas de a una | Una oferta por día, cuenta regresiva en stories | Anuncios de venta cargados, aprobados y programados | D−1: acceso anticipado a la lista VIP, si se ofrece |
| **Venta** | D hasta el cierre | Vender y atender rápido | Stories con stock real, pedidos que salen, preguntas frecuentes | Campaña de venta y retargeting encendidas; monitoreo 3 veces al día (`bf-monitoreo`) | Atención con refuerzo de personal |
| **Cierre** | Último día | Últimas horas, sin estirar la fecha | "Últimas horas", "se terminó" al cierre | Anuncio de últimas horas en retargeting; apagar todo a la hora de cierre | Un solo recordatorio a quienes preguntaron y no compraron |
| **Posventa** | D+1 a D+7 | Agradecer, fidelizar y medir | "Gracias", pedidos entregados | Guardar públicos de compradores e interesados para las fiestas | Gracias + cupón para después + pedido de reseña |

## Paso 3: Versiones según el tiempo que queda

- **1 a 3 semanas:** junta preparación y calentamiento. Lista VIP desde ya, aunque sea corta.
- **Menos de 7 días (exprés):**
  1. Día 1: oferta simple (un gancho y un beneficio) y 3 a 5 piezas.
  2. Día 2: cargar una campaña de venta con un conjunto frío y uno de retargeting, y mandarla a revisión.
  3. Hasta D: stories diarias con la oferta y la cuenta regresiva; difusión a los contactos que tienen agendado el número.
  4. D hasta el cierre: igual que el plan completo.
- **Menos de 48 horas:** solo retargeting y difusión por WhatsApp a los contactos que ya tiene el negocio. Con tan poco tiempo, el público frío no suele llegar a rendir.

## Paso 4: Reglas del cronograma

- **Los anuncios se mandan a revisión al menos 3 días antes de D.** La mayoría se revisa en menos de 24 horas, pero a veces tarda más o hay que corregir algo.
- **Ninguna pieza sale sin el precio confirmado** por el negocio.
- **Todo anuncio de la promo tiene fecha y hora de fin,** para que nada siga corriendo cuando la oferta ya no existe.
- **Un responsable por tarea,** con nombre. Si el negocio es chico y lo hace todo una persona, el cronograma tiene que entrar en sus horas reales.

## Entregable

```
CRONOGRAMA BLACK FRIDAY — [NEGOCIO]
Promo: [día y fecha] [hora] a [día y fecha] [hora]

| Fecha | Fase | Tarea | Canal | Responsable | Entregable |
|---|---|---|---|---|---|
| lun 09/11 | Preparación | Confirmar costos y stock | — | [nombre] | Planilla de oferta |
| ... | ... | ... | ... | ... | ... |

Hitos: lista VIP abierta [fecha] · anuncios en revisión [fecha] · acceso anticipado [fecha] · cierre [fecha y hora] · reporte final [fecha]
```

Termina con lo que hay que hacer hoy y quién lo hace. Para las piezas de cada fase, sigue con `bf-creativos`.
