---
layout: default
title: Hydroxyurea
parent: Evidencia Moderada (L3-L4)
nav_order: 331
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Hydroxyurea: nueva indicación predicha, Carcinoma de mama femenino (nivel de evidencia L4). Indicación original: Hidroxicarbamida"
monitor_inn: "hydroxyurea"
predicted_indications: ["female breast carcinoma", "sickle cell-hemoglobin c disease syndrome", "sickle cell-hemoglobin E disease syndrome", "sickle cell-hemoglobin d disease syndrome", "sickle cell-beta-thalassemia disease syndrome", "cervical adenosarcoma", "colon mucinous adenocarcinoma", "rectum mucinous adenocarcinoma", "gallbladder mucinous adenocarcinoma"]
---

# Hydroxyurea
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
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

# Hidroxiurea: De Indicación No Especificada en el Registro (Hidroxicarbamida) a Carcinoma de Mama Femenino

## Resumen en Una Frase

La hidroxiurea (hidroxicarbamida) es un fármaco antineoplásico oral. En Colombia sus registros sanitarios solo consignan el nombre del principio activo, sin una indicación detallada.
El modelo TxGNN predice que podría ser efectivo para **carcinoma de mama femenino**, pero actualmente hay **0 ensayos clínicos** registrados y la literatura disponible (20 publicaciones) es en su mayoría preclínica o de fases tempranas.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hidroxicarbamida (el registro solo menciona el principio activo, sin indicación detallada) |
| Nueva Indicación Predicha | Carcinoma de mama femenino |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos detallados de mecanismo de acción en la información compilada para este informe. Según el conocimiento farmacológico general, la hidroxiurea inhibe la enzima ribonucleótido reductasa. Esto reduce las reservas de desoxirribonucleótidos (dNTP) y genera estrés de replicación del ADN en las células que se dividen rápidamente.

Ese mecanismo es biológicamente plausible en tumores que dependen de tolerar el estrés de replicación, por ejemplo mediante la vía ATR/RPA2. En la literatura sobre cáncer de mama, la hidroxiurea se usa sobre todo como herramienta experimental para inducir estrés de replicación y estudiar la reparación del ADN. También hay trabajos que la combinan con otros agentes, como el ácido valproico, para sensibilizar células de mama.

Es importante ser claro: el puntaje del modelo es muy alto, pero es solo una predicción. No hay ensayos clínicos registrados ni datos de eficacia específicos en cáncer de mama. La relación con la indicación original tampoco puede evaluarse bien, porque el registro colombiano no detalla para qué se aprobó el fármaco.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Se seleccionaron las 10 publicaciones más pertinentes. Ninguna es un ensayo aleatorizado y la mayoría es preclínica. Los resúmenes disponibles están truncados, por lo que los hallazgos se resumen de forma prudente.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [1957839](https://pubmed.ncbi.nlm.nih.gov/1957839/) | 1991 | Fase 1 (combinación) | Am J Clin Oncol | Estudio de 20 pacientes con cáncer avanzado (colorrectal, páncreas, estómago y mama) con 5-FU, leucovorina y alopurinol seguidos de hidroxiurea |
| [1733549](https://pubmed.ncbi.nlm.nih.gov/1733549/) | 1992 | Fase 1/2 (combinación) | Cancer Chemother Pharmacol | Cisplatino en dosis escalonadas con 5-FU, hidroxiurea y radioterapia en tumores sólidos avanzados (no específico de mama) |
| [38211596](https://pubmed.ncbi.nlm.nih.gov/38211596/) | 2024 | In silico/Preclínico | Drug Research | Diseño de conjugados lipídicos de hidroxiurea dirigidos a la vía PI3K/AKT/mTOR para mejorar la captación celular en cáncer de mama |
| [28837865](https://pubmed.ncbi.nlm.nih.gov/28837865/) | 2017 | Preclínico | DNA Repair | El ácido valproico sensibiliza células de cáncer de mama a la hidroxiurea al inhibir la reparación del ADN mediada por RPA2 |
| [32795962](https://pubmed.ncbi.nlm.nih.gov/32795962/) | 2020 | Preclínico | DNA Repair | El ácido 2-hexil-4-pentinoico, como alternativa al valproico, actúa sobre la reparación del ADN en carcinoma de mama |
| [25814515](https://pubmed.ncbi.nlm.nih.gov/25814515/) | 2015 | Preclínico | Mol Pharmacol | El inhibidor de ribonucleótido reductasa COH29 (misma diana que la hidroxiurea) inhibe la reparación del ADN en células de mama con BRCA-1 defectuoso |
| [34661718](https://pubmed.ncbi.nlm.nih.gov/34661718/) | 2022 | Preclínico | Naunyn-Schmiedeberg's Arch Pharmacol | Nanopartículas cargadas con hidroxiurea, con liberación dependiente del pH, arresto del ciclo celular y cambios en p53 |
| [27504932](https://pubmed.ncbi.nlm.nih.gov/27504932/) | 2017 | Preclínico | J Cell Physiol | Quimiorresistencia de células de pulmón y mama sometidas a privación prolongada de suero |
| [30159181](https://pubmed.ncbi.nlm.nih.gov/30159181/) | 2018 | Reporte de caso | Case Rep Hematol | Paciente con cáncer de mama y trombocitemia esencial concurrentes, con los retos terapéuticos de ambas condiciones |
| [9060546](https://pubmed.ncbi.nlm.nih.gov/9060546/) | 1997 | Serie clínica | J Clin Oncol | Esquema TPDC-FuHu (incluye hidroxiurea) en tumores cerebrales metastásicos recurrentes, no específico de mama |

---

## Información de Mercado en Colombia

Ambos registros figuran como **cancelados**, por lo que actualmente no hay productos vigentes con este principio activo.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 42034 | HYDREA CAPSULAS 500 MG (Cheplapharm Arzneimittel GmbH) | Cápsula dura | HIDROXICARBAMIDA |
| 20257687 | HIDROXIUREA 500 MG CAPSULA DURA (Blau Farmacéutica Colombia S.A.S.) | Cápsula dura | HIDROXICARBAMIDA |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (antimetabolito, inhibidor de la ribonucleótido reductasa) |
| Riesgo de Mielosupresión | Alto. El grafo de conocimiento asocia el fármaco con leucopenia, trombocitopenia y anemia (incluida la macrocítica) |
| Clasificación de Emetogenicidad | Baja (según la categoría general del fármaco) |
| Items de Monitoreo | Hemograma con diferencial y plaquetas, función renal y hepática |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos. Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Condiciones de riesgo según el grafo de conocimiento TxGNN** (relaciones fármaco-enfermedad, no texto de prospecto): enfermedad renal, piouréter, trombocitopenia, anemia, anemia macrocítica, leucopenia y vasculitis cutánea.
- **Interacciones farmacológicas:** se identificaron 309 interacciones potenciales. Entre las que aparecen en el listado están levofloxacino (menor), doxiciclina, anfotericina B, hidrocortisona, famotidina, ácido acetilsalicílico, pantoprazol, metformina, omeprazol, morfina, vancomicina, prednisona y simvastatina. La mayoría no tiene nivel de gravedad clasificado, por lo que se requiere revisión farmacéutica antes de cualquier uso combinado.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de carcinoma de mama tiene un puntaje muy alto del modelo, pero no hay ensayos clínicos registrados y la literatura es mayoritariamente preclínica o de fase 1 antigua en tumores mixtos (nivel de evidencia L4). Además, en Colombia no hay productos vigentes, lo que complica cualquier acceso local.

**Para avanzar se necesita:**
- Datos de eficacia clínica específicos en cáncer de mama, por ejemplo estudios de fase 2 que justifiquen continuar.
- Datos oficiales del prospecto (advertencias y contraindicaciones) y del mecanismo de acción confirmado en una fuente farmacológica.
- Aclarar el estatus regulatorio actual del fármaco en Colombia y la indicación aprobada originalmente.
- Un plan de monitoreo hematológico dado el alto riesgo de mielosupresión.
- Como referencia, entre las demás predicciones de este fármaco, la enfermedad de hemoglobina SC (anemia falciforme) tiene mayor respaldo (nivel L2, con un ensayo de fase 2 y publicaciones recientes). Podría ser una línea de investigación más sólida que el cáncer de mama.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

