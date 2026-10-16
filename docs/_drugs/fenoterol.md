---
layout: default
title: Fenoterol
parent: Solo Predicción del Modelo (L5)
nav_order: 280
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
description: "Fenoterol: nueva indicación predicha, Atrofia multisistémica (nivel de evidencia L5). Indicación original: Fenoterol + bromuro de ipratropio"
monitor_inn: "fenoterol"
predicted_indications: ["multiple system atrophy", "postural orthostatic tachycardia syndrome", "variably protease-sensitive prionopathy", "open-angle glaucoma", "Raynaud disease", "primary hereditary glaucoma", "sinoatrial block", "sinoatrial node disease"]
---

# Fenoterol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

# Fenoterol: De Enfermedad Obstructiva de la Vía Aérea a Atrofia Multisistémica

## Resumen en Una Frase

Fenoterol es un agonista beta-2 adrenérgico, utilizado originalmente (solo o combinado con bromuro de ipratropio) para enfermedades obstructivas de la vía aérea.
El modelo TxGNN predice que podría ser efectivo para **atrofia multisistémica**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; es solo una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Fenoterol + bromuro de ipratropio |
| Nueva Indicación Predicha | Atrofia multisistémica |
| Puntaje de Predicción TxGNN | 99.70% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 3 (todos cancelados) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción. Según la información conocida, fenoterol es un agonista de los receptores beta-adrenérgicos (la farmacología registrada muestra interacción con los receptores β1, β2 y β3), con uso como broncodilatador y, en algunos países, para inhibir el parto prematuro. Su eficacia en la obstrucción de la vía aérea es conocida.

Sin embargo, la relación con la atrofia multisistémica (AMS) es débil. En la AMS, la falla autonómica con hipotensión ortostática es una característica central, y la vasodilatación periférica mediada por beta-2 tendería a empeorar, y no a aliviar, la hipotensión. No existe un fundamento mecanístico que respalde un efecto modificador de la enfermedad.

El alto puntaje de TxGNN debe interpretarse con cautela: es una asociación computacional sin ensayos ni literatura de apoyo y, en la dirección terapéutica, biológicamente poco plausible.

### Otras predicciones del modelo (todas L5, Hold)

| Enfermedad predicha | Puntaje TxGNN | Comentario |
|------|------|------|
| Síndrome de taquicardia postural ortostática | 99.61% | La vasodilatación y la taquicardia refleja probablemente agravarían los síntomas |
| Prionopatía variablemente sensible a proteasa | 99.54% | Sin vínculo mecanístico identificable; probable artefacto de la red |
| Glaucoma de ángulo abierto | 99.43% | Mecanismo parcialmente plausible (dinámica del humor acuoso), sin evidencia oftálmica |
| Enfermedad de Raynaud | 99.41% | Vasodilatación conceptualmente relevante, pero efecto periférico limitado a dosis inhaladas; hay alternativas mejor respaldadas |
| Glaucoma hereditario primario | 99.37% | Origen estructural del desarrollo, poco probable que responda |
| Bloqueo sinoauricular | 99.35% | El riesgo proarrítmico supera el beneficio especulativo |
| Enfermedad del nodo sinoauricular | 99.25% | No es terapia estándar; riesgo proarrítmico |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 19931241 | BERODUAL® HFA | Solución para inhalación | Fenoterol + bromuro de ipratropio | Cancelado |
| 54889 | BERODUAL® SOLUCION | Solución para inhalación | Fenoterol + bromuro de ipratropio | Cancelado |
| 19952369 | PULBRONC NF NIÑOS | Jarabe | Fenoterol y otros fármacos para enfermedad obstructiva de la vía aérea | Cancelado |

## Consideraciones de Seguridad

- **Interacciones farmacológicas / farmacología de receptores**: fenoterol actúa sobre los receptores β1-adrenérgico (ADRB1), β2-adrenérgico (ADRB2) y β3-adrenérgico (ADRB3). La actividad sobre β1 es relevante para los efectos cardíacos.
- **Riesgo cardiovascular**: según el análisis de las predicciones, los efectos cardíacos de fenoterol (taquiarritmia, isquemia) constituyen una preocupación de seguridad, en especial en las indicaciones cardiovasculares predichas.

No se dispone de datos de advertencias ni contraindicaciones del prospecto. Consultar el prospecto para esa información.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para atrofia multisistémica (y para las demás indicaciones propuestas) se basa solo en el modelo, sin ensayos ni literatura, y el mecanismo beta-2 agonista es contrario al beneficio esperado (podría empeorar la hipotensión ortostatica). Además, no hay registros sanitarios vigentes en Colombia.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto en INVIMA (advertencias y contraindicaciones), que es un vacío bloqueante para el tamizaje de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una revisión sistemática de la literatura y de registros de ensayos para confirmar la ausencia de evidencia.
- Evaluar la viabilidad regulatoria y de vía de administración, dado que todos los registros están cancelados.
- Si se continúa, priorizar indicaciones con mejor plausibilidad mecanística (por ejemplo, glaucoma de ángulo abierto) mediante estudios preclínicos antes de cualquier evaluación clínica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

