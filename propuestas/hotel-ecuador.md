# Hotel en Ecuador · Respuesta y oferta
**TWO&HUMAN · Octubre 2026 · Versión 1 (borrador para revisar)**

---

## 1. Diagnóstico

Hacen tres preguntas, pero el problema real es uno: **las campañas no tienen suficientes resultados para que Meta aprenda.**

Las causas más comunes en un hotel:

1. **Optimizan por reservas, que son pocas.** Meta necesita unos 50 resultados por semana en cada conjunto de anuncios para salir de la fase de aprendizaje. Un hotel rara vez consigue 50 reservas por semana desde anuncios.
2. **Presupuesto repartido en muchos conjuntos.** Cada uno recibe muy poco y ninguno llega a 50.
3. **Medición incompleta.** El motor de reservas suele estar en otro dominio, y el píxel pierde las reservas. Meta "no ve" lo que sí pasa.
4. **Cambios seguidos.** Tocar el presupuesto, el público o los anuncios a cada rato reinicia el aprendizaje.

Lo bueno: mostrarles este diagnóstico en la primera respuesta es la mejor prueba de que sabemos lo que hacemos.

## 2. Plan técnico para salir de la fase de aprendizaje

| Palanca | Qué hacemos |
|---|---|
| **Consolidar** | Una campaña por objetivo, uno o dos conjuntos de anuncios con públicos amplios y ubicaciones automáticas, presupuesto a nivel campaña. |
| **Optimizar por un evento con volumen** | En lugar de "reserva", optimizar por conversación iniciada (WhatsApp), formulario o inicio de reserva en el motor. La reserva se mide aparte. |
| **Arreglar la medición** | Píxel y API de conversiones en la web y en el motor de reservas, con el valor de cada reserva. Subir a Meta las reservas confirmadas (también las que se cierran por WhatsApp o teléfono). |
| **Presupuesto mínimo realista** | Presupuesto diario por conjunto ≈ 50 × costo por resultado ÷ 7. |
| **No tocar de más** | Cambios de presupuesto de hasta 20 % cada 3 o 4 días. Nada de editar públicos a diario. |
| **Juzgar por el negocio** | "Aprendizaje limitado" no siempre es malo. Si el costo por reserva da los números, se sigue. |

**Ejemplo con supuestos** (los reales salen del diagnóstico):

| Optimizando por… | Costo por resultado (supuesto) | Presupuesto diario mínimo por conjunto |
|---|---|---|
| Reserva | USD 40 | ≈ USD 285 (inalcanzable para muchos hoteles) |
| Inicio de reserva | USD 8 | ≈ USD 57 |
| Conversación por WhatsApp | USD 2 | ≈ USD 14 |

Por eso la campaña "nunca sale": con presupuesto de hotel, optimizar por reservas no llega a 50 por semana.

## 3. La oferta

**Nombre:** Sistema Reservas Directas · 90 días

**Resultado que buscan:** más reservas directas, sin depender de Booking y las agencias online, y saber qué anuncio trae cada reserva.

**Cuentas claras para el hotel** (supuestos a confirmar): si una estadía promedio es de USD 300 y la agencia online cobra 15 a 20 % de comisión, cada reserva directa le ahorra USD 45 a 60. Con el número real de reservas por mes calculamos cuántas reservas directas pagan el servicio.

### Cómo trabajamos

| Etapa | Qué incluye | Precio sugerido |
|---|---|---|
| **1. Diagnóstico de medición y campañas** (7 días) | Revisión de la cuenta publicitaria, el píxel, el motor de reservas y las campañas actuales. Informe con lo que falla y el plan para salir de la fase de aprendizaje. | **USD 250**, una sola vez. Se descuenta del primer mes si siguen con nosotros. |
| **2a. Acompañamiento** (su equipo maneja las campañas) | Armado de la medición, nueva estructura de campañas, revisión semanal de 30 minutos y ajustes por WhatsApp. | **USD 450 por mes** |
| **2b. Gestión completa** (nosotros manejamos las campañas) | Medición, estructura, gestión diaria de Meta Ads, textos y edición de anuncios con material del hotel, planilla de reservas por campaña y reporte mensual. | **USD 800 por mes** |
| **Opcional** | Bono por reserva directa atribuida a las campañas | A definir |

- **Mínimo:** el diagnóstico (USD 250). Para los planes mensuales, 3 meses, pagados mes por adelantado.
- **El presupuesto de anuncios lo paga el hotel directo a Meta,** en su cuenta. Lo definimos en el diagnóstico con la fórmula del punto 2.
- **No incluye:** producción de fotos o video en el hotel (el material lo envía el hotel o un fotógrafo local), Google Ads (se cotiza aparte), cambios en la web o en el motor de reservas que requieran a su proveedor.
- **Garantía de cumplimiento:** si a los 30 días la medición no está funcionando (reservas llegando a Meta y a la planilla), el segundo mes no se cobra hasta completarla.
- **Todo queda a nombre del hotel:** cuentas, píxel, planillas y anuncios.

> Precios sugeridos a partir de lo que cobramos en Argentina, ajustados para trabajo remoto y en dólares. Confirmarlos antes de enviar.

## 4. Respuesta lista para enviar

Tono neutro, con "ustedes" (no voseo), para cliente de Ecuador.

```
Asunto: TWO&HUMAN · Respuesta a sus consultas y próximos pasos

Hola, [NOMBRE]:

Gracias por escribirnos. Respondo sus tres consultas.

1) Presupuesto y costos

Trabajamos en dos etapas:

• Diagnóstico de medición y campañas (7 días): revisamos la cuenta publicitaria, el píxel, el motor de reservas y las campañas actuales, y les entregamos un informe con lo que falla y cómo resolverlo. Valor: USD 250, una sola vez. Si después siguen con nosotros, se descuenta del primer mes.

• Plan mensual, desde el segundo mes:
  – Acompañamiento (su equipo maneja las campañas y nosotros armamos la medición, la estructura y revisamos todo cada semana): USD 450 por mes.
  – Gestión completa (nosotros manejamos las campañas, los textos y la edición de anuncios con el material del hotel, y entregamos un reporte mensual): USD 800 por mes.

El mínimo para empezar es el diagnóstico. Los planes mensuales son por 3 meses, con pago mes por adelantado. El presupuesto de anuncios lo paga el hotel directamente a Meta y lo definimos juntos en el diagnóstico. Si a los 30 días la medición no está funcionando, el segundo mes no se cobra hasta completarla.

2) Medición y fase de aprendizaje

Es un problema muy común en hoteles. Meta necesita unos 50 resultados por semana en cada conjunto de anuncios para salir de la fase de aprendizaje, y un hotel rara vez consigue 50 reservas semanales desde anuncios. Por eso las campañas quedan estancadas.

Lo resolvemos con tres cambios:
• Menos campañas y conjuntos, con el presupuesto concentrado.
• Optimizar por un resultado con más volumen (por ejemplo, conversaciones por WhatsApp o inicios de reserva) y medir las reservas aparte.
• Completar la medición: píxel y API de conversiones en la web y el motor de reservas, y cargar en Meta las reservas confirmadas con su valor, también las que se cierran por WhatsApp o teléfono.

Así Meta aprende con más datos y ustedes saben qué anuncio trae cada reserva.

3) Comunicación y equipo

Somos TWO&HUMAN, una agencia de marketing y tecnología de Tucumán, Argentina. Trabajamos campañas, contenido, sitios web y automatizaciones, para que la tecnología ayude a atender mejor a las personas.

Trabajamos de forma remota:
• Grupo de WhatsApp para el día a día.
• Videollamada semanal de 30 minutos.
• Correo para aprobaciones y documentos.
• Reporte mensual con los números.

Estamos 2 horas adelante de Ecuador continental, así que coordinamos dentro de su horario laboral.

¿Les parece una videollamada de 30 minutos esta semana? Me gustaría conocer el hotel, ver cómo tienen armadas las campañas hoy y contarles cómo sería la colaboración. Si me indican dos o tres horarios, lo agendo.

Saludos,
Julio
TWO&HUMAN · Donde la tecnología se vuelve humana
```

## 5. Preguntas para la videollamada

**Quiénes son:**
- ¿Son el equipo del hotel, una empresa que lo administra o una agencia?
- ¿Qué tipo de colaboración buscan: que manejemos todo, que acompañemos a su equipo o trabajar para sus clientes con nuestra marca o la suya?

**El hotel:**
- Ubicación, cantidad de habitaciones y tipo de huésped (turismo, negocios, familias, extranjeros).
- Tarifa promedio por noche y estadía promedio.
- Ocupación por temporada.
- Qué parte de las reservas llega por Booking u otras agencias online y qué comisión pagan.
- Qué motor de reservas usan y en qué dominio está.

**Las campañas:**
- Objetivo, cantidad de campañas y conjuntos, y presupuesto mensual.
- Por qué evento optimizan.
- Costo por resultado y cuántas reservas atribuyen a los anuncios.
- Si tienen píxel, API de conversiones y Google Analytics.
- Qué material de fotos y video tienen.

**La relación:**
- Quién decide y quién aprueba.
- Cómo prefieren pagar desde Ecuador.

## 6. Decisiones antes de enviar

1. Confirmar los precios sugeridos (USD 250, 450 y 800).
2. Si ofrecemos el bono por reserva directa y cómo se calcularía.
3. Cómo cobramos desde el exterior y cómo facturamos (consultar con el contador: exportación de servicios).
4. Si mencionamos clientes actuales: pedirles permiso antes de nombrarlos.
