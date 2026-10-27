---
layout: default
title: Regorafenib
parent: Solo Predicción del Modelo (L5)
nav_order: 553
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
description: "Regorafenib: nueva indicación predicha, Liposarcoma (nivel de evidencia L5). Indicación original: REGORAFENIB"
monitor_inn: "regorafenib"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "clear cell renal carcinoma", "unclassified renal cell carcinoma", "renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions", "renal cell carcinoma associated with neuroblastoma", "childhood kidney cell carcinoma", "vulva sarcoma"]
---

# Regorafenib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

## Regorafenib: De Indicación Original (Cáncer Colorrectal/GIST) a Liposarcoma
{: .text-alpha }

## Resumen en Una Frase

Regorafenib es un inhibidor oral de múltiples quinasas, comercializado como Stivarga, cuyo registro sanitario en Colombia no detalla la indicación aprobada (solo figura el nombre del principio activo).
El modelo TxGNN predice que podría ser efectivo para **liposarcoma**,
con **1 ensayo clínico** y **9 publicaciones** relacionadas. Sin embargo, el ensayo de Fase 2 y el estudio aleatorizado de la cohorte de liposarcoma **no respaldan el uso rutinario** del fármaco en esta población.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | REGORAFENIB (el registro no especifica la indicación; la literatura lo describe como aprobado para cáncer colorrectal metastásico y GIST) |
| Nueva Indicación Predicha | Liposarcoma |
| Puntaje de Predicción TxGNN | 99.76% |
| Nivel de Evidencia | L1 (según la clasificación del análisis; ver nota en la conclusión) |
| Estado de Mercado en Colombia | Solo cancelado (sin registros vigentes) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Proceed with Guardrails (con reservas; ver conclusión) |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción registrado en DrugBank. Según la literatura revisada, regorafenib es un inhibidor oral de múltiples quinasas que actúa sobre receptores angiogénicos (VEGFR1-3, TIE2), del estroma (PDGFR-β, FGFR) y oncogénicos (KIT, RET y RAF). Fue el primer inhibidor de quinasas de molécula pequeña en mostrar beneficio de supervivencia en cáncer colorrectal metastásico refractario.

La relación con el liposarcoma se basa en que los sarcomas de tejidos blandos dependen en parte de la angiogénesis y de las vías de señalización de quinasas. Otros inhibidores de quinasas (sorafenib, sunitinib, pazopanib) han mostrado actividad en sarcomas de tejidos blandos, y regorafenib ya se evaluó en GIST y en otros sarcomas.

**Advertencia importante:** la evidencia depende del subtipo. En el ensayo REGOSARC, regorafenib mostró eficacia en leiomiosarcoma, sarcoma sinovial y otros sarcomas no adipocíticos, **pero no en liposarcoma**. La cohorte de liposarcoma de SARC024 confirmó este resultado y los autores concluyeron que no apoya el uso rutinario del fármaco en estos pacientes.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Fase 2 | Completado | 131 | Protocolo SARC024: regorafenib oral en subtipos seleccionados de sarcoma, con una cohorte de liposarcoma. Es directamente relevante, aunque el tamaño de muestra por subtipo es pequeño |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [32701199](https://pubmed.ncbi.nlm.nih.gov/32701199/) | 2020 | ECA (Fase II) | The Oncologist | Cohorte de liposarcoma de SARC024: regorafenib vs. placebo; los resultados no respaldan el uso rutinario en esta población |
| [27751846](https://pubmed.ncbi.nlm.nih.gov/27751846/) | 2016 | ECA (Fase II) | The Lancet Oncology | REGOSARC: eficacia y seguridad de regorafenib en sarcoma de tejidos blandos avanzado previamente tratado con antraciclinas |
| [29902612](https://pubmed.ncbi.nlm.nih.gov/29902612/) | 2018 | ECA (análisis actualizado) | European Journal of Cancer | Eficacia frente a placebo y tras el cruce en sarcoma no adipocítico; no se observó eficacia en liposarcoma |
| [29931504](https://pubmed.ncbi.nlm.nih.gov/29931504/) | 2018 | Revisión | Targeted Oncology | Papel creciente de regorafenib en sarcomas, con datos de Fase 2 y 3 según el subtipo |
| [40975452](https://pubmed.ncbi.nlm.nih.gov/40975452/) | 2025 | Revisión | Critical Reviews in Oncology/Hematology | Terapia de mantenimiento tras el tratamiento de primera línea del sarcoma de tejidos blandos avanzado |
| [28295221](https://pubmed.ncbi.nlm.nih.gov/28295221/) | 2017 | Cohorte (análisis post hoc) | Cancer | REGOSARC: análisis Q-TWiST del beneficio clínico en sarcoma no adipocítico |
| [33290314](https://pubmed.ncbi.nlm.nih.gov/33290314/) | 2021 | Estudio retrospectivo | Anti-Cancer Drugs | Anlotinib (otro inhibidor de quinasas) en liposarcoma bien/desdiferenciado; menciona a regorafenib solo como contexto |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | Protocolo de estudio | BMC Cancer | Protocolo del ensayo REGOSARC |
| [26266019](https://pubmed.ncbi.nlm.nih.gov/26266019/) | 2015 | Reporte de caso | Rare Tumors | Respuesta a pazopanib en sarcoma de Ewing extraóseo; justifica incluir una cohorte de Ewing en SARC024 |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20152989 (cancelado) | STIVARGA 40 MG TABLETA RECUBIERTA (BAYER A.G.) | Tableta recubierta | REGORAFENIB (sin texto de indicación específico) |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor oral de múltiples quinasas) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | La literatura compilada señala toxicidad hepática, reacción cutánea mano-pie, hipertensión, diarrea y proteinuria; se recomienda vigilar función hepática, presión arterial, función renal/proteinuria y hemograma |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas:** se identificaron 213 interacciones en total. Entre las mostradas, las de gravedad **mayor** incluyen: ácido acetilsalicílico, deferasirox, ibritumomab tiuxetán, tositumomab (incluido I-131), abciximab, alteplasa, antitrombina III humana y apixabán (en general, fármacos con efecto sobre la coagulación o el riesgo de sangrado). Entre las de gravedad **moderada** figuran dexametasona, claritromicina, naltrexona, rosuvastatina, cobicistat, fenfluramina, dexfenfluramina y sibutramina. Las de gravedad menor incluyen dapagliflozina, naloxegol y prucaloprida.
- **Perfil de toxicidad según la literatura:** toxicidad hepática, reacción cutánea mano-pie, hipertensión, diarrea y proteinuria, descritas en metaanálisis de inhibidores de quinasas antiangiogénicos.

No se dispone de advertencias ni contraindicaciones extraídas del prospecto; consultar el prospecto para esa información.

---

## Conclusión y Próximos Pasos

**Decisión: Hold (recomendación propia; el análisis automático indica Proceed with Guardrails)**

**Justificación:**
Aunque la clasificación automática asigna L1 por la presencia de ECA de Fase 2 y una predicción alta de TxGNN (99.76%), el contenido de esos ensayos es **negativo para liposarcoma**: REGOSARC no mostró beneficio y la cohorte de liposarcoma de SARC024 no respalda el uso rutinario. Además, no hay ECA de Fase 3 completados, el único registro sanitario en Colombia está cancelado y faltan datos de seguridad del prospecto. Por ello, recomiendo no avanzar como candidato directo en liposarcoma; si se desea explorar, solo con las salvaguardas indicadas abajo.

**Para avanzar se necesita:**
- Revisar la clasificación del nivel de evidencia: L1 sobreestima la evidencia, ya que los ECA disponibles son de Fase 2 y negativos para este subtipo.
- Obtener el prospecto de INVIMA (advertencias y contraindicaciones) y el mecanismo de acción desde DrugBank.
- Confirmar la situación regulatoria en Colombia, dado que el único registro está cancelado.
- Evaluar subpoblaciones o combinaciones (la cohorte de SARC024 sugiere explorar enfoques combinados) antes de cualquier ensayo.
- Plan de monitoreo de seguridad (función hepática, presión arterial, piel, proteinuria) y revisión de las interacciones de gravedad mayor, en especial con anticoagulantes y antiagregantes.
- Como alternativa, priorizar el **carcinoma renal de células claras** (rank 3, nivel L3, con estudio de Fase 2 en RCC no tratado previamente y fundamento mecanístico VEGF), aunque ya existen inhibidores de quinasas establecidos en ese campo. Las demás indicaciones predichas (rank 2 y 4–8) carecen de ensayos y literatura específicos (L5, Hold).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

