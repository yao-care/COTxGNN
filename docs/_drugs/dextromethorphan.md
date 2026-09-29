---
layout: default
title: Dextromethorphan
parent: Solo Predicción del Modelo (L5)
nav_order: 160
evidence_level: L5
indication_count: 6
---

# Dextromethorphan
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Dextromethorphan: De Tos (Supresores y Expectorantes) a Enfermedad de la Cavidad Nasal

## Resumen en Una Frase

Dextromethorphan es un antitusivo de acción central, usado originalmente como supresor de la tos en jarabes.
El modelo TxGNN predice que podría ser efectivo para **enfermedad de la cavidad nasal**, pero **no hay ensayos clínicos directamente relacionados ni publicaciones** que respalden esta indicación.
El único ensayo asociado estudia depresión mayor, no enfermedad nasal.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Tos: supresores y expectorantes |
| Nueva Indicación Predicha | Enfermedad de la cavidad nasal (nasal cavity disease) |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 8 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Dextromethorphan actúa sobre el sistema nervioso central. Es antagonista del receptor NMDA, agonista del receptor sigma-1 e inhibidor del transportador de serotonina (SERT). Las bases farmacológicas lo vinculan con GRIN2C, SIGMAR1 y el receptor de sabor amargo TAS2R1. No se dispone de un campo de mecanismo de acción curado en DrugBank para este farmaco.

No existe un mecanismo establecido que relacione estas acciones con la patología de la cavidad nasal. Si hubiera algún beneficio, lo más probable es que fuera sintomático, por ejemplo sobre la tos o la hipersensibilidad de la vía aérea superior. El fármaco no tiene acción antiinfecciosa ni antiinflamatoria sobre la enfermedad en sí.

El puntaje TxGNN (0.9998) es solo una predicción computacional. La cercanía entre tos y enfermedades de vías respiratorias altas en el grafo de conocimiento explica plausiblemente la predicción, pero no la demuestra. Por eso la relación con la indicación original sigue pendiente de análisis.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT06958692](https://clinicaltrials.gov/study/NCT06958692) | Fase 3 | Reclutando | 388 | Dextromethorphan + bupropion de liberación sostenida vs. placebo en adultos chinos con trastorno depresivo mayor. Aleatorizado, doble ciego, sin resultados aún. |

**Nota:** este ensayo no evalúa enfermedad de la cavidad nasal. Solo confirma que dextromethorphan se investiga en Fase 3 para otra indicación, así que no cuenta como evidencia directa (no alcanza L1).

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20116677 | NOGLUPEC® JARABE (Comercializadora Monserrath S.A.S.) | Jarabe | Tos: supresores y expectorantes |

El resumen regulatorio informa 8 registros sanitarios. El detalle recibido solo contiene entradas repetidas del mismo número (20116677), por lo que aquí se muestra una sola fila.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Las tres entradas de "interacciones" del Evidence Pack son dianas farmacológicas (GRIN2C, TAS2R1, SIGMAR1), no interacciones medicamentosas clínicas. No deben usarse para evaluar riesgo de interacciones.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos ni publicaciones sobre enfermedad de la cavidad nasal, y el mecanismo del fármaco no explica un efecto sobre la enfermedad. El puntaje alto del modelo, por sí solo, no basta para avanzar. El nivel L5 aplica según las reglas del informe, aunque el Evidence Pack lo había clasificado como L4. No hay estudios preclínicos que respalden L4.

**Para avanzar se necesita:**
- Verificar el campo de condiciones y los brazos de intervención del ensayo NCT06958692 para confirmar si tiene alguna relación con enfermedad nasal.
- Definir con precisión qué condición nasal se pretende tratar y si el objetivo sería solo sintomático (tos, hipersensibilidad de vía aérea superior).
- Revisar la literatura sobre dextromethorphan en vías respiratorias altas.
- Obtener el prospecto de INVIMA con advertencias y contraindicaciones, información de seguridad bloqueante hasta ahora.
- Completar los datos de mecanismo de acción desde DrugBank.
- Analizar la compatibilidad de vía de administración; el jarabe es la única forma registrada y ese análisis aún está pendiente.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

