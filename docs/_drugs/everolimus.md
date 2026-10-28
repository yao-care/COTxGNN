---
layout: default
title: Everolimus
parent: Evidencia Alta (L1-L2)
nav_order: 273
evidence_level: L2
indication_count: 8
monitor_inn: "EVEROLIMUS"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "dermatofibrosarcoma protuberans", "parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "embryonal extrahepatic bile duct rhabdomyosarcoma", "rhabdomyosarcoma (disease)", "prostate embryonal rhabdomyosarcoma"]
last_modified_at: 2026-10-27
description: "Everolimus: nueva indicación predicha, liposarcoma (nivel de evidencia L2). Indicación original: EVEROLIMUS"
---

# Everolimus
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **8** 
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

## Everolimus: inhibidor de mTOR → liposarcoma (liposarcoma)
{: .text-alpha }

## Resumen en Una Frase

Everolimus es un inhibidor de la vía mTOR que cuenta con registros sanitarios en Colombia.
El modelo TxGNN predice que podría ser efectivo para **liposarcoma (liposarcoma)**,
con **1 ensayo clínico** de Fase 2 en combinación con ribociclib y **4 publicaciones** relacionadas, ninguna de las cuales evalúa everolimus solo en esta enfermedad.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | EVEROLIMUS |
| Nueva Indicación Predicha | liposarcoma (liposarcoma) |
| Puntaje de Predicción TxGNN | 0,9988 |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 2) |
| Número de Registros Sanitarios | al menos 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Por conocimiento general, everolimus inhibe mTORC1, una vía situada aguas abajo de la señalización PI3K/AKT que regula la proliferación celular.

En el liposarcoma desdiferenciado, los tumores suelen presentar amplificación de CDK4/MDM2. Combinar un inhibidor de CDK4/6 (ribociclib) con un inhibidor de mTOR (everolimus) apunta a dos vías proliferativas complementarias, y en modelos tumorales se ha descrito inhibición sinérgica del crecimiento con esta combinación.

Esto da una justificación biológica plausible, pero la señal clínica proviene de un único ensayo de Fase 2 de un solo brazo con una combinación, cuyos resultados no están claramente establecidos en los datos disponibles. No es posible aislar la contribución de everolimus por sí solo.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Fase 2 | Activo, sin reclutar | 48 | Ribociclib + everolimus en liposarcoma desdiferenciado y leiomiosarcoma avanzados tras al menos una terapia sistémica previa; evalúa la actividad antitumoral de la combinación |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Ensayo clínico Fase 2 | Clinical Cancer Research | Informe del ensayo de ribociclib + everolimus en liposarcoma desdiferenciado y leiomiosarcoma avanzados |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Revisión | Frontiers in Oncology | Modelos PDOX de sarcoma para identificar combinaciones con palbociclib; no específico de everolimus |
| [41991999](https://pubmed.ncbi.nlm.nih.gov/41991999/) | 2026 | Preclínico | Oncogene | El inhibidor de XPO1 KPT-330 afecta la viabilidad del liposarcoma desdiferenciado; no específico de everolimus |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Preclínico | Anticancer Research | Actividad antitumoral de eribulina en combinación con otros agentes; no específico de everolimus |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20015207 | AFINITOR® 10 MG TABLETAS | Tableta | EVEROLIMUS |
| 20263581 | EVASCEND® 1MG TABLETA DE LIBERACIÓN INMEDIATA | Tableta de liberación modificada | EVEROLIMUS |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de mTOR) |
| Riesgo de Mielosupresión | Medio; las relaciones de seguridad registradas incluyen trombocitopenia, neutropenia, leucopenia y anemia |
| Clasificación de Emetogenicidad | Baja |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal, glucosa y perfil lipídico |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Condiciones de riesgo registradas para everolimus** (no provienen del texto del prospecto): insuficiencia hepática, enfermedad renal, trombocitopenia, hiperglucemia, diabetes mellitus, neutropenia, hiperlipidemia, hipertrigliceridemia, anemia, enfermedad pulmonar intersticial, leucopenia, estomatitis, derrame pericárdico e insuficiencia cardíaca congestiva, entre otras.
- **Interacciones farmacológicas** (100 interacciones registradas; ejemplos):
  - Mayores: anfotericina B, aprepitant, dexametasona, claritromicina.
  - Moderadas: metformina, acarbosa, canagliflozina, dapagliflozina, empagliflozina, linagliptina, glimepirida, cimetidina, eliglustat, eluxadolina.
  - Menores: sulfato de zinc.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje TxGNN muy alto, pero la evidencia clínica se limita a un ensayo de Fase 2 con una combinación (ribociclib + everolimus) aún activo, sin resultados claramente establecidos para everolimus en liposarcoma. Ningún estudio evalúa everolimus solo en esta enfermedad, por lo que el nivel de evidencia debe considerarse L5 en lugar de L2.

**Para avanzar se necesita:**
- Resultados publicados y revisados del ensayo NCT03114527, con análisis de la contribución de everolimus.
- Datos del mecanismo de acción confirmados desde fuentes farmacológicas.
- Advertencias y contraindicaciones del prospecto aprobado en Colombia.
- Plan de monitoreo de seguridad hematológica, metabólica y pulmonar.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

