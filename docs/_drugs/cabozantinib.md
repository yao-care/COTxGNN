---
layout: default
title: Cabozantinib
parent: Solo Predicción del Modelo (L5)
nav_order: 126
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-12
description: "Cabozantinib: nueva indicación predicha, Liposarcoma (nivel de evidencia L5). Indicación original: Cabozantinib"
monitor_inn: "CABOZANTINIB"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "amyotrophic lateral sclerosis", "bilateral parasagittal parieto-occipital polymicrogyria", "angiolipoma"]
---

# Cabozantinib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

Cabozantinib es un inhibidor oral de múltiples cinasas que se comercializó en Colombia como CABOMETYX 40 mg, no incluye un texto de indicación descriptivo.
El modelo TxGNN predice que podría ser efectivo para **liposarcoma**, con **1 ensayo clínico** (no específico de liposarcoma) y **1 publicación** que respaldan esta dirección de forma indirecta.

<!-- review:begin co-lic-20261105-cabozantinib-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Cabozantinib es un inhibidor oral de múltiples cinasas que se comercializó en Colombia como CABOMETYX 40 mg, aunque su único registro sanitario está cancelado y no incluye un texto de indicación descriptivo." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-cabozantinib-2 -->

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cabozantinib (el registro solo indica el nombre del principio activo, sin texto de indicación) |
| Nueva Indicación Predicha | Liposarcoma |
| Puntaje de Predicción TxGNN | 0.9983 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
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
| 20172869 | CABOMETYX 40 MG (IPSEN PHARMA) | Tableta recubierta | CABOZANTINIB |

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
Para liposarcoma solo existe un ensayo de fase 2 no específico y un estudio de fase 1 centrado en seguridad, sin resultados de eficacia. Además, faltan datos de seguridad del prospecto.

<!-- review:begin co-lic-20261105-cabozantinib-3 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, el único registro sanitario en Colombia está cancelado y faltan datos de seguridad del prospecto." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-cabozantinib-3 -->

**Para avanzar se necesita:**
- Datos de eficacia específicos en liposarcoma (subanálisis del NCT05836571 o estudios dedicados)
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones)
- Datos detallados del mecanismo de acción

<!-- review:begin co-lic-20261031-cabozantinib-1 -->

> **Corrección de revisión (2026-10-31)**: Texto original: "Datos detallados del mecanismo de acción / Aclarar la situación regulatoria en Colombia (registro cancelado) y la compatibilidad de la vía de administración" Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-10-31. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261031-cabozantinib-1 -->

---

## Otras Predicciones Relevantes

| Indicación | Puntaje TxGNN | Nivel | Recomendación |
|------|------|------|------|
| Carcinoma renal | 0.9966 | L1 | Proceed with Guardrails (uso ya establecido; respaldado por ensayos de fase 3 como CheckMate 9ER, METEOR y CONTACT-03) |
| Liposarcoma mixoide ovárico, carcinoma renal asociado a neuroblastoma, esclerosis lateral amiotrófica, polimicrogiria parieto-occipital parasagital bilateral, angiolipoma | 0.9962–0.9980 | L5 | Hold (solo predicción computacional, sin evidencia) |

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-10-31 | Eliminado: "Aclarar la situación regulatoria en Colombia (registro cancelado) y la compatibilidad de la vía de administración" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "aunque su único registro sanitario está cancelado y" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "el único registro sanitario en Colombia está cancelado y" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

