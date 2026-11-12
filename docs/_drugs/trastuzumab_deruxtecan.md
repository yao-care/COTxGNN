---
layout: default
title: Trastuzumab Deruxtecan
parent: Solo Predicción del Modelo (L5)
nav_order: 638
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
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

## Trastuzumab Deruxtecan: De Indicación No Especificada a Osteoporosis Inducida por Fármacos
{: .text-alpha }

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
| Puntaje de Predicción TxGNN | 0.9931 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, trastuzumab deruxtecan es un conjugado anticuerpo-fármaco: la parte de anticuerpo (trastuzumab) se dirige a HER2 y la carga útil (deruxtecan) inhibe la topoisomerasa I, lo que produce citotoxicidad en células tumorales.

**Con los datos disponibles, no se identifica un vínculo mecanístico sólido.** No se conoce una vía que conecte la señalización de HER2 o la inhibición de la topoisomerasa I con la remodelación ósea ni con la prevención o el tratamiento de la osteoporosis inducida por fármacos. Los tratamientos habituales en este contexto (por ejemplo, bisfosfonatos y denosumab) actúan inhibiendo los osteoclastos, un mecanismo distinto.

El puntaje alto del modelo (0.9931) puede reflejar proximidad en la red de conocimiento, por ejemplo asociaciones compartidas con fármacos oncológicos o con la pérdida ósea como efecto adverso de tratamientos. Esto no equivale a potencial terapéutico real. Además, un conjugado citotóxico podría empeorar, y no mejorar, la salud ósea en un contexto de cuidado de soporte.

<!-- review:begin co-lic-20261105-trastuzumab_deruxtecan-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "El único registro (ASTRAZENECA COLOMBIA S.A.S.) figura como cancelado, por lo que actualmente no hay registros vigentes." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-trastuzumab_deruxtecan-1 -->

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20240733 | ENHERTU® | Polvo para solución inyectable | TRASTUZUMAB DERUXTECAN |

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
La predicción se apoya solo en el puntaje del modelo (L5), sin ensayos clínicos ni literatura, y no hay un vínculo mecanístico plausible con la osteoporosis inducida por fármacos. Además, no hay datos de seguridad del prospecto.

<!-- review:begin co-lic-20261105-trastuzumab_deruxtecan-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, el único registro sanitario en Colombia está cancelado y no hay datos de seguridad del prospecto." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-trastuzumab_deruxtecan-2 -->

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank.
- Un racional biológico que conecte el fármaco con la remodelación ósea, o estudios preclínicos que lo sustenten.
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones), requisito previo para cualquier evaluación de seguridad.
- Evaluar si el puntaje refleja la pérdida ósea como efecto adverso de tratamientos oncológicos y no un beneficio terapéutico.

<!-- review:begin co-lic-20261105-trastuzumab_deruxtecan-3 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Aclarar la situación regulatoria del registro cancelado y la indicación aprobada real. / Evaluar si el puntaje refleja la pérdida ósea como efecto adverso de tratamientos oncológicos y no un beneficio terapéutico." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-trastuzumab_deruxtecan-3 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "El único registro (ASTRAZENECA COLOMBIA S.A.S.) figura como cancelado, por lo que actualmente no hay registros vigentes" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "el único registro sanitario en Colombia está cancelado y" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Aclarar la situación regulatoria del registro cancelado y la indicación aprobada real" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

