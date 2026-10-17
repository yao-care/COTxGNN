---
layout: default
title: Everolimus
parent: Evidencia Alta (L1-L2)
nav_order: 273
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-14
description: "Everolimus: nueva indicación predicha, Liposarcoma (nivel de evidencia L2). Indicación original: No especificada en el registro (el texto de indicación solo indica \"E…"
monitor_inn: "EVEROLIMUS"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "dermatofibrosarcoma protuberans", "parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "embryonal extrahepatic bile duct rhabdomyosarcoma", "rhabdomyosarcoma (disease)", "prostate embryonal rhabdomyosarcoma"]
---

# Everolimus
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **10** 
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

# Everolimus: De Indicación Original No Especificada a Liposarcoma

## Resumen en Una Frase

Everolimus es un inhibidor de mTOR que contó con registros sanitarios en Colombia (Afinitor® y Evascend®), aunque el texto de indicación registrado solo repite el nombre del principio activo y no detalla la indicación original.
El modelo TxGNN predice que podría ser efectivo para **liposarcoma**, con **1 ensayo clínico** y **4 publicaciones** que actualmente respaldan esta dirección (una sola de ellas es un reporte de ensayo clínico directamente relacionado).
La evidencia disponible proviene de un ensayo de Fase 2 de un solo brazo que combina everolimus con ribociclib, por lo que el aporte del everolimus por sí solo no puede aislarse.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto de indicación solo indica "EVEROLIMUS") |
| Nueva Indicación Predicha | Liposarcoma |
| Puntaje de Predicción TxGNN | 99.88% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según el conocimiento general del fármaco, everolimus inhibe mTORC1, una vía situada aguas abajo de la señalización PI3K/AKT que regula la proliferación y el crecimiento celular.

En el liposarcoma desdiferenciado (con amplificación de CDK4/MDM2), la inhibición combinada de CDK4/6 (ribociclib) y de mTOR (everolimus) actúa sobre dos vías proliferativas complementarias. Los modelos tumorales han mostrado sinergia en la inhibición del crecimiento con esta combinación, lo que ofrece una base biológica plausible.

Sin embargo, el puntaje de TxGNN es muy alto, pero la señal clínica descansa en un único ensayo de Fase 2 de un solo brazo con una combinación de fármacos, cuyos resultados no están claramente establecidos en los datos compilados. La relación con la indicación original no puede evaluarse porque el registro local no la detalla.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Fase 2 | Activo, sin reclutamiento | 48 | Ribociclib + everolimus en liposarcoma desdiferenciado (DDL) avanzado y leiomiosarcoma (LMS) tras al menos una terapia sistémica previa; evalúa la actividad antitumoral de la combinación. Finalización prevista: diciembre de 2026 |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Reporte de ensayo clínico Fase 2 | Clin Cancer Res | Ribociclib + everolimus en DDL y LMS avanzados; la combinación mostró sinergia en múltiples modelos tumorales |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Revisión (modelos preclínicos) | Front Oncol | Modelos PDOX de sarcoma para identificar combinaciones con palbociclib; no es específico de everolimus |
| [41991999](https://pubmed.ncbi.nlm.nih.gov/41991999/) | 2026 | Preclínico | Oncogene | El inhibidor de XPO1 KPT-330 afecta la viabilidad celular en liposarcoma desdiferenciado; no es específico de everolimus |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Preclínico | Anticancer Res | Actividad antitumoral de eribulina en combinación con otros agentes; no es específico de everolimus |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20015207 | AFINITOR® 10 MG TABLETAS (Novartis Pharma AG) | Tableta | EVEROLIMUS (estado: cancelado) |
| 20263581 | EVASCEND® 1 MG TABLETA DE LIBERACIÓN INMEDIATA (Alkem Laboratories Limited) | Tableta de liberación modificada | EVEROLIMUS (estado: cancelado) |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de mTOR), usada en oncología |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto. El grafo de conocimiento asocia el fármaco con neutropenia, leucopenia, trombocitopenia y anemia |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma, función hepática y renal, glucosa y perfil lipídico |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Condiciones asociadas en el grafo de conocimiento (no provienen del texto del prospecto):** insuficiencia y enfermedad hepática, enfermedad renal, trombocitopenia, neutropenia, leucopenia, anemia, agranulocitosis, hiperglucemia, diabetes mellitus, cetoacidosis diabética, hipertrigliceridemia, hiperlipidemia, enfermedad pulmonar intersticial, insuficiencia cardíaca congestiva, estomatitis, derrame pericárdico y síndrome hemolítico urémico, entre otras.
- **Interacciones Farmacológicas** (se identificaron 100; se listan las principales):
  - **Mayores:** anfotericina B (incluida la formulación de complejo lipídico), aprepitant, dexametasona y claritromicina.
  - **Moderadas:** antidiabéticos como acarbosa, metformina, glimepirida, clorpropamida, linagliptina, alogliptina, canagliflozina, dapagliflozina, empagliflozina, albiglutida y dulaglutida; también cimetidina, eliglustat y eluxadoline.
  - **Menores:** sulfato de zinc.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El puntaje de TxGNN es muy alto (99.88%), pero la evidencia clínica se limita a un ensayo de Fase 2 de un solo brazo con una combinación (ribociclib + everolimus) y sus resultados no están claramente establecidos. Además, no hay registros sanitarios vigentes en Colombia y falta la información de seguridad del prospecto.

**Para avanzar se necesita:**
- Resultados publicados de eficacia del ensayo NCT03114527 que permitan estimar el aporte del everolimus.
- Obtener y analizar el prospecto del INVIMA (advertencias y contraindicaciones) para completar el tamizaje de seguridad.
- Datos del mecanismo de acción desde DrugBank para fortalecer el análisis mecanístico.
- Aclarar la indicación original aprobada, ya que el registro solo muestra el nombre del principio activo.
- Evaluar la situación regulatoria: ambos registros están cancelados, por lo que sería necesario un nuevo registro o una vía de acceso alternativa.
- Plan de monitoreo de seguridad hematológica, metabólica, hepática y renal, y revisión de interacciones (especialmente inhibidores o inductores de CYP3A4/P-gp y antidiabéticos).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

