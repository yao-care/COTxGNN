---
layout: default
title: Cabozantinib
parent: Evidencia Moderada (L3-L4)
nav_order: 126
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-14
description: "Cabozantinib: nueva indicación predicha, Liposarcoma (nivel de evidencia L3). Indicación original: Cabozantinib"
monitor_inn: "CABOZANTINIB"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "amyotrophic lateral sclerosis", "bilateral parasagittal parieto-occipital polymicrogyria", "angiolipoma"]
---

# Cabozantinib
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **10** 
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

## Cabozantinib: De Indicación Registrada (sin texto descriptivo) a Liposarcoma
{: .text-alpha }

## Resumen en Una Frase

Cabozantinib es un inhibidor oral de múltiples cinasas que se comercializó en Colombia como CABOMETYX 40 mg, aunque su único registro sanitario está cancelado y no incluye un texto de indicación descriptivo.
El modelo TxGNN predice que podría ser efectivo para **liposarcoma**, con **1 ensayo clínico** (no específico de liposarcoma) y **1 publicación** que respaldan esta dirección de forma indirecta.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cabozantinib (el registro solo indica el nombre del principio activo, sin texto de indicación) |
| Nueva Indicación Predicha | Liposarcoma |
| Puntaje de Predicción TxGNN | 99.83% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

> **Nota:** La evaluación de liposarcoma se clasifica como pregunta de investigación. Entre las predicciones del modelo, la indicación con mayor respaldo clínico es el carcinoma renal (ver más abajo), pero corresponde a un uso ya establecido y no a un reposicionamiento genuino.

---

## ¿Por qué es Razonable esta Predicción?

Cabozantinib inhibe varias cinasas, entre ellas MET, VEGFR2, AXL y RET. Estas vías participan en la angiogénesis y en la progresión tumoral de los sarcomas. Actualmente no se dispone de datos detallados de mecanismo de acción en la fuente principal del fármaco, por lo que esta descripción se apoya en el análisis mecanístico compilado para este informe.

La relación con la indicación original es indirecta: el registro colombiano no detalla una indicación, pero cabozantinib es un antineoplásico dirigido. Los sarcomas de tejidos blandos, entre ellos el liposarcoma, comparten dependencia de la angiogénesis y de la señalización por cinasas, lo que haría plausible su actividad. Además, su combinación con inhibidores de puntos de control inmunitario podría modular el microambiente tumoral.

Sin embargo, la evidencia directa específica para liposarcoma es limitada. El ensayo disponible incluye sarcomas de tejidos blandos en general, y el estudio publicado es de fase 1 con radioterapia en sarcomas de extremidades.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT05836571](https://clinicaltrials.gov/study/NCT05836571) | Fase 2 | Activo, sin reclutamiento | 66 | Ensayo aleatorizado que compara ipilimumab + nivolumab con la misma combinación más cabozantinib en sarcoma de tejidos blandos avanzado. No es específico de liposarcoma y aún no tiene resultados. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [41770651](https://pubmed.ncbi.nlm.nih.gov/41770651/) | 2026 | Ensayo fase 1 | American Journal of Clinical Oncology | Evalúa la seguridad de cabozantinib neoadyuvante concurrente con radioterapia en sarcomas de tejidos blandos de extremidades, dado el temor a fístulas o perforaciones. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20172869 (cancelado) | CABOMETYX 40 MG (IPSEN PHARMA) | Tableta recubierta | CABOZANTINIB |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina cinasas múltiples) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma, función hepática y renal, electrolitos, presión arterial |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas:** Se identificaron 100 interacciones en total. Entre las de nivel **Mayor** destacan: ácido acetilsalicílico, cisaprida, claritromicina, dolasetrón, granisetrón y levofloxacino. Entre las de nivel **Moderado**: loperamida, aprepitant, dexametasona, bisacodilo, aceite de ricino, clotrimazol, fenfluramina, lactulosa y citrato de magnesio. Fidaxomicina es de nivel **Menor**.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para liposarcoma solo existe un ensayo de fase 2 no específico y un estudio de fase 1 centrado en seguridad, sin resultados de eficacia. Además, el único registro sanitario en Colombia está cancelado y faltan datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Datos de eficacia específicos en liposarcoma (subanálisis del NCT05836571 o estudios dedicados)
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones)
- Datos detallados del mecanismo de acción
- Aclarar la situación regulatoria en Colombia (registro cancelado) y la compatibilidad de la vía de administración

---

## Otras Predicciones Relevantes

| Indicación | Puntaje TxGNN | Nivel | Recomendación |
|------|------|------|------|
| Carcinoma renal | 99.66% | L1 | Proceed with Guardrails (uso ya establecido; respaldado por ensayos de fase 3 como CheckMate 9ER, METEOR y CONTACT-03) |
| Carcinoma renal de células no clasificado | 99.75% | L2 | Proceed with Guardrails (varios ensayos de fase 2 en CCR no células claras) |
| Carcinoma renal asociado a translocaciones Xp11.2/TFE3 | 99.75% | L2 | Proceed with Guardrails (evidencia de fase 2 en poblaciones mixtas) |
| Carcinoma renal infantil | 99.68% | L2 | Research Question |
| Liposarcoma mixoide ovárico, carcinoma renal asociado a neuroblastoma, esclerosis lateral amiotrófica, polimicrogiria parieto-occipital parasagital bilateral, angiolipoma | 99.62%–99.80% | L5 | Hold (solo predicción computacional, sin evidencia) |
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

