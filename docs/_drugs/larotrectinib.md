---
layout: default
title: Larotrectinib
parent: Solo Predicción del Modelo (L5)
nav_order: 382
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-12
description: "Larotrectinib: nueva indicación predicha, Neoplasia endocrina múltiple (nivel de evidencia L5). Indicación original: LAROTRECTINIB"
monitor_inn: "larotrectinib"
predicted_indications: ["multiple endocrine neoplasia", "HER2 positive breast carcinoma"]
---

# Larotrectinib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Larotrectinib: De Tumores con Fusión NTRK a Neoplasia Endocrina Múltiple
{: .text-alpha }

## Resumen en Una Frase

Larotrectinib es un inhibidor selectivo de las quinasas TRK (NTRK1/2/3), registrado en Colombia por INVIMA como principio activo único (VITRAKVI®), sin un texto de indicación detallado en los registros.
El modelo TxGNN predice que podría ser efectivo para **neoplasia endocrina múltiple**, con **1 ensayo clínico** (un ensayo de cesta no específico de la enfermedad) y **2 publicaciones** (una revisión y un estudio preclínico/mecanístico) que actualmente respaldan esta dirección de forma indirecta.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | LAROTRECTINIB (el registro de INVIMA solo menciona el nombre del principio activo, sin detallar la indicación) |
| Nueva Indicación Predicha | Neoplasia endocrina múltiple |
| Puntaje de Predicción TxGNN | 0.9924 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 2 de 2) |
| Número de Registros Sanitarios | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, larotrectinib es un inhibidor selectivo de las quinasas TRK (NTRK1/2/3) y no es un inhibidor primario de RET. Su eficacia está establecida en tumores con fusiones NTRK, y mecanísticamente podría ser aplicable a la neoplasia endocrina múltiple solo de forma indirecta.

La neoplasia endocrina múltiple tipo 2 (MEN2) está causada por mutaciones germinales activadoras de RET, que también sustentan el carcinoma medular de tiroides. TRK y RET son ambas tirosina quinasas receptoras que señalizan a través de vías MAPK/PI3K que se solapan. La literatura de 2024 sobre resistencia fuera de la diana a la inhibición selectiva de RET sugiere comunicación cruzada entre vías de escape en cánceres dependientes de RET.

Es importante subrayar que no existe evidencia directa de que la inhibición de TRK controle los tumores de MEN dependientes de RET. Un nicho plausible, aunque no establecido, sería un tumor con fusión NTRK coexistente con enfermedad asociada a MEN. El puntaje TxGNN muy alto (0.9924) es una predicción computacional y no debe interpretarse como evidencia clínica.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02465060](https://clinicaltrials.gov/study/NCT02465060) | Fase 2 | Activo, sin reclutamiento | 6452 | Ensayo de cesta NCI-MATCH guiado por biomarcadores en tumores sólidos, linfomas o mielomas avanzados y refractarios; incluye un brazo con larotrectinib para fusiones NTRK. No es específico de neoplasia endocrina múltiple y no demuestra que pacientes con MEN hayan sido tratados ni beneficiados. Evidencia indirecta (no aleatorizado). |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31322645](https://pubmed.ncbi.nlm.nih.gov/31322645/) | 2019 | Revisión | Endocrine Reviews | Revisa la terapia dirigida con inhibidores de quinasas en cáncer de tiroides avanzado; la mayoría de los fármacos aprobados son multiquinasa antiangiogénicos y existen indicaciones específicas por mutación. |
| [38438731](https://pubmed.ncbi.nlm.nih.gov/38438731/) | 2024 | Estudio preclínico/mecanístico | NPJ Precision Oncology | Describe mecanismos de resistencia fuera de la diana a inhibidores selectivos de RET (selpercatinib, pralsetinib) en un paciente con carcinoma medular de tiroides con mutación de RET. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20200411 | VITRAKVI® SOLUCIÓN ORAL DE 20 MG/ML (estado: vigente) | Solución oral | LAROTRECTINIB |
| 20201285 | VITRAKVI® CÁPSULAS DE 100 MG (estado: vigente) | Cápsula dura | LAROTRECTINIB |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de quinasas TRK), no citotóxico convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar el prospecto; en general, hemograma y función hepática y renal |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: Se identificaron 427 interacciones en total. Entre las listadas:
  - **Mayor**: claritromicina.
  - **Moderadas**: corticoesteroides (hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida), omeprazol, cimetidina, aprepitant, pioglitazona, saxagliptina, dolasetrón, dronabinol, eliglustat, naldemedina, naltrexona, cisaprida y clotrimazol.
  - **Menor**: naloxegol.

<!-- review:begin co-lic-20261105-larotrectinib-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Ambos registros pertenecen a BAYER AG y se encuentran cancelados; actualmente no hay registros vigentes en Colombia." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 2 registros sanitarios (vigentes: 2); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-larotrectinib-2 -->

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia es solo indirecta: un ensayo de cesta no específico, una revisión y un estudio mecanístico, sin datos que muestren beneficio en neoplasia endocrina múltiple. El vínculo mecanístico (TRK frente a RET) es débil y el puntaje TxGNN es únicamente una predicción computacional.

<!-- review:begin co-lic-20261105-larotrectinib-3 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "El vínculo mecanístico (TRK frente a RET) es débil y el puntaje TxGNN es únicamente una predicción computacional. Además, no hay registro vigente en Colombia." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 2 registros sanitarios (vigentes: 2); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-larotrectinib-3 -->

**Para avanzar se necesita:**
- Datos del mecanismo de acción y del prospecto (advertencias y contraindicaciones) de larotrectinib.
- Evidencia preclínica o clínica que vincule la inhibición de TRK con tumores de MEN, por ejemplo casos con fusión NTRK coexistente.
- Análisis específico de los resultados de pacientes con MEN dentro de NCI-MATCH, si están disponibles.
- Evaluar el manejo de las interacciones, en particular con inhibidores potentes del CYP3A4 como la claritromicina.

<!-- review:begin co-lic-20261031-larotrectinib-1 -->

> **Corrección de revisión (2026-10-31)**: Texto original: "Aclarar la situación regulatoria en Colombia (registros cancelados) y la disponibilidad real del fármaco. / Evaluar el manejo de las interacciones, en particular con inhibidores potentes del CYP3A4 como la claritromicina." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-10-31. El medicamento tiene 2 registros sanitarios (vigentes: 2); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261031-larotrectinib-1 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-10-31 | Eliminado: "Aclarar la situación regulatoria en Colombia (registros cancelados) y la disponibilidad real del fármaco" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Ambos registros pertenecen a BAYER AG y se encuentran cancelados; actualmente no hay registros vigentes en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Además, no hay registro vigente en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

