---
layout: default
title: Trastuzumab Deruxtecan
parent: Solo Predicción del Modelo (L5)
nav_order: 638
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Trastuzumab Deruxtecan: nueva indicación predicha, Osteoporosis inducida por fármacos (nivel de evidencia L5). Indicación original: TRASTUZUMAB DERUXTECAN"
monitor_inn: "trastuzumab deruxtecan"
predicted_indications: ["drug-induced osteoporosis"]
---

# Trastuzumab Deruxtecan
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

# Trastuzumab Deruxtecan: De Indicación No Especificada a Osteoporosis Inducida por Fármacos

## Resumen en Una Frase

Trastuzumab deruxtecan (ENHERTU®) es un conjugado anticuerpo-fármaco dirigido a HER2 con una carga útil inhibidora de la topoisomerasa I; en el registro sanitario colombiano disponible solo figura el nombre del principio activo como indicación, sin detalle clínico.
El modelo TxGNN predice que podría ser efectivo para **osteoporosis inducida por fármacos**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.
La predicción se basa únicamente en el modelo computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | TRASTUZUMAB DERUXTECAN (el registro no detalla una indicación clínica) |
| Nueva Indicación Predicha | Osteoporosis inducida por fármacos |
| Puntaje de Predicción TxGNN | 99.31% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo cancelado (sin registros vigentes) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, trastuzumab deruxtecan es un conjugado anticuerpo-fármaco: la parte de anticuerpo (trastuzumab) se dirige a HER2 y la carga útil (deruxtecan) inhibe la topoisomerasa I, lo que produce citotoxicidad en células tumorales.

**Con los datos disponibles, no se identifica un vínculo mecanístico sólido.** No se conoce una vía que conecte la señalización de HER2 o la inhibición de la topoisomerasa I con la remodelación ósea ni con la prevención o el tratamiento de la osteoporosis inducida por fármacos. Los tratamientos habituales en este contexto (por ejemplo, bisfosfonatos y denosumab) actúan inhibiendo los osteoclastos, un mecanismo distinto.

El puntaje alto del modelo (0.993) puede reflejar proximidad en la red de conocimiento, por ejemplo asociaciones compartidas con fármacos oncológicos o con la pérdida ósea como efecto adverso de tratamientos. Esto no equivale a potencial terapéutico real. Además, un conjugado citotóxico podría empeorar, y no mejorar, la salud ósea en un contexto de cuidado de soporte.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20240733 (cancelado) | ENHERTU® | Polvo para solución inyectable | TRASTUZUMAB DERUXTECAN |

El único registro (ASTRAZENECA COLOMBIA S.A.S.) figura como cancelado, por lo que actualmente no hay registros vigentes.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Conjugado anticuerpo-fármaco (terapia dirigida con carga útil citotóxica, inhibidor de topoisomerasa I) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma, función hepática y renal; consultar el prospecto para parámetros adicionales |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 42 interacciones en total. Entre las que aparecen en los datos:
  - **Mayores**: deferiprona, samario (153Sm) lexidronam, adalimumab, baricitinib, certolizumab pegol, cladribina, leflunomida, natalizumab.
  - **Moderadas**: palifermina, cloruro de estroncio Sr-89, roflumilast, cloranfenicol (incluida la presentación oftálmica), alefacept, alemtuzumab, anakinra, azatioprina, canakinumab, fumarato de dimetilo, niraparib.

  Muchas de estas interacciones involucran fármacos inmunosupresores o mielosupresores, por lo que conviene revisar la combinación con cada uno.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (L5), sin ensayos clínicos ni literatura, y no hay un vínculo mecanístico plausible con la osteoporosis inducida por fármacos. Además, el único registro sanitario en Colombia está cancelado y no hay datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank.
- Un racional biológico que conecte el fármaco con la remodelación ósea, o estudios preclínicos que lo sustenten.
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones), requisito previo para cualquier evaluación de seguridad.
- Aclarar la situación regulatoria del registro cancelado y la indicación aprobada real.
- Evaluar si el puntaje refleja la pérdida ósea como efecto adverso de tratamientos oncológicos y no un beneficio terapéutico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

