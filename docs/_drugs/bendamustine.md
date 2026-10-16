---
layout: default
title: Bendamustine
parent: Evidencia Alta (L1-L2)
nav_order: 98
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Bendamustine: nueva indicación predicha, Linfoma de células del manto (nivel de evidencia L1). Indicación original: BENDAMUSTINE"
monitor_inn: "Bendamustine"
predicted_indications: ["mantle cell lymphoma", "chronic myelogenous leukemia, BCR-ABL1 positive", "Hodgkins lymphoma", "small intestinal Burkitt lymphoma", "small intestinal mucosa-associated lymphoid tissue lymphoma", "thyroid gland mucosa-associated lymphoid tissue lymphoma", "breast mucosa-associated lymphoid tissue lymphoma", "tonsillar lymphoma", "MALT lymphoma", "relapsing-remitting multiple sclerosis"]
---

# Bendamustine
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **10** 
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

# Bendamustina: De Indicación Original No Especificada a Linfoma de Células del Manto

## Resumen en Una Frase

Bendamustina es un agente alquilante citotóxico que cuenta con un registro sanitario en Colombia (actualmente cancelado), cuyo texto de indicación aprobada solo menciona el nombre del fármaco, sin detallar una enfermedad específica.
El modelo TxGNN predice que podría ser efectivo para **Linfoma de Células del Manto**,
con **44 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | BENDAMUSTINE (el registro no detalla una enfermedad específica) |
| Nueva Indicación Predicha | Linfoma de células del manto |
| Puntaje de Predicción TxGNN | 99.63% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registro vigente) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según la información conocida, la bendamustina es un agente alquilante con una estructura similar a la de los análogos de purinas: provoca entrecruzamiento del ADN y roturas de cadena, con actividad tanto en células en división como en células quiescentes.

Este mecanismo es coherente con su actividad en neoplasias de células B como el linfoma de células del manto (LCM). La combinación de bendamustina con rituximab (BR) es un esquema base establecido en LCM, y los programas de fase 3 más recientes la combinan con inhibidores de BTK (ibrutinib, acalabrutinib, orelabrutinib, zanubrutinib).

Cabe señalar que el registro colombiano no especifica la indicación original, por lo que no es posible establecer una relación formal entre ésta y la nueva indicación. La razonabilidad de la predicción se apoya en el mecanismo y en la evidencia clínica con regímenes basados en bendamustina.

## Evidencia de Ensayos Clínicos

Se listan los ensayos más relevantes (de un total de 44 identificados para esta indicación):

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00991211](https://clinicaltrials.gov/study/NCT00991211) | Fase 3 | Completado | 549 | Bendamustina + rituximab vs. CHOP + rituximab en primera línea de linfomas indolentes y LCM (no inferioridad en supervivencia libre de progresión) |
| [NCT00877006](https://clinicaltrials.gov/study/NCT00877006) | Fase 3 | Completado | 447 | Estudio BRIGHT: BR vs. R-CVP/R-CHOP en linfoma no Hodgkin indolente o LCM sin tratamiento previo |
| [NCT01776840](https://clinicaltrials.gov/study/NCT01776840) | Fase 3 | Completado | 523 | Ibrutinib + BR vs. placebo + BR en LCM recién diagnosticado (≥65 años) |
| [NCT02972840](https://clinicaltrials.gov/study/NCT02972840) | Fase 3 | Activo, sin reclutar | 635 | Acalabrutinib + BR vs. placebo + BR en LCM sin tratamiento previo |
| [NCT06363994](https://clinicaltrials.gov/study/NCT06363994) | Fase 3 | Reclutando | 476 | Orelabrutinib + BR vs. BR en LCM sin tratamiento previo; resultados aún no disponibles |
| [NCT06084936](https://clinicaltrials.gov/study/NCT06084936) | Fase 3 | Reclutando | 182 | Glofitamab vs. elección del investigador (BR o R-lenalidomida) en LCM en recaída/refractario |
| [NCT00891839](https://clinicaltrials.gov/study/NCT00891839) | Fase 2 | Completado | 45 | Bendamustina + rituximab en LCM en recaída/refractario |
| [NCT04115631](https://clinicaltrials.gov/study/NCT04115631) | Fase 2 | Activo, sin reclutar | 360 | Tres esquemas con BR, citarabina y acalabrutinib en LCM sin tratamiento previo (≤70 años) |
| [NCT03834688](https://clinicaltrials.gov/study/NCT03834688) | Fase 2 | Completado | 33 | Venetoclax + BR en LCM sin tratamiento previo, mayores de 60 años |
| [NCT00740415](https://clinicaltrials.gov/study/NCT00740415) | Fase 2 | Completado | 39 | Bortezomib con quimioinmunoterapia en primera línea de LCM en pacientes mayores (n pequeño) |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [23433739](https://pubmed.ncbi.nlm.nih.gov/23433739/) | 2013 | ECA | Lancet | BR frente a R-CHOP en primera línea de linfomas indolentes y LCM: ensayo de fase 3 de no inferioridad |
| [35657079](https://pubmed.ncbi.nlm.nih.gov/35657079/) | 2022 | ECA | N Engl J Med | Ibrutinib añadido a BR y seguido de mantenimiento con rituximab en LCM sin tratamiento previo en pacientes mayores |
| [40311141](https://pubmed.ncbi.nlm.nih.gov/40311141/) | 2025 | ECA | J Clin Oncol | Acalabrutinib + BR en LCM sin tratamiento previo; busca mejorar resultados con menor toxicidad que ibrutinib |
| [41052510](https://pubmed.ncbi.nlm.nih.gov/41052510/) | 2025 | ECA | Lancet | ENRICH: ibrutinib + rituximab vs. inmunoquimioterapia (R-CHOP o BR) en LCM, ≥60 años |
| [32985902](https://pubmed.ncbi.nlm.nih.gov/32985902/) | 2021 | ECA (protocolo) | Future Oncol | Fase 3 de zanubrutinib + rituximab vs. BR en LCM sin tratamiento previo y no candidatos a trasplante |
| [24591201](https://pubmed.ncbi.nlm.nih.gov/24591201/) | 2014 | ECA | Blood | Estudio BRIGHT: BR frente a R-CHOP/R-CVP en linfoma no Hodgkin indolente o LCM |
| [30811293](https://pubmed.ncbi.nlm.nih.gov/30811293/) | 2019 | Fase 2/seguimiento | J Clin Oncol | Seguimiento a 5 años del estudio BRIGHT |
| [32126141](https://pubmed.ncbi.nlm.nih.gov/32126141/) | 2020 | Fase 2 | Blood Adv | Inducción con rituximab/bendamustina y rituximab/citarabina en LCM elegible para trasplante |
| [40975105](https://pubmed.ncbi.nlm.nih.gov/40975105/) | 2025 | Fase 2 | Lancet Haematol | R-BAC seguido de venetoclax en pacientes mayores con LCM de alto riesgo |
| [41132246](https://pubmed.ncbi.nlm.nih.gov/41132246/) | 2025 | Guía | HemaSphere | Guías EHA-EU MCL Network para el diagnóstico y tratamiento del LCM |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20154170 (cancelado) | Bendamustina Clorhidrato 100 mg polvo liofilizado para inyección (Laboratorio Kemex S.A.) | Polvo liofilizado para reconstituir a solución inyectable | BENDAMUSTINE |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (agente alquilante) |
| Riesgo de Mielosupresión | Alto: el grafo de conocimiento asocia el fármaco con contraindicación en trombocitopenia, neutropenia, agranulocitosis y anemia. Consultar las advertencias del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

## Consideraciones de Seguridad

- **Contraindicaciones / condiciones de riesgo (según el grafo de conocimiento TxGNN, no texto de prospecto)**: insuficiencia hepática, enfermedad renal, piouréter, enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia, neutropenia, agranulocitosis, anemia y anemia macrocítica.
- **Interacciones farmacológicas** (100 interacciones registradas; se destacan las de mayor gravedad):
  - **Mayor**: deferiprona, samario (153Sm) lexidronam.
  - **Moderada** (ejemplos): omeprazol, esomeprazol, cimetidina, cafeína, deferasirox, ticlopidina, mercaptopurina, cloranfenicol, roflumilast, osilodrostat, ácido obeticólico, palifermina, albendazol, primaquina.

Para advertencias y contraindicaciones formales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen múltiples ensayos de fase 3 completados (incluidos NCT00991211 y NCT00877006) y varias publicaciones en ECA que respaldan el uso de bendamustina más rituximab en LCM, por lo que el nivel de evidencia es L1. Sin embargo, el único registro sanitario colombiano está cancelado, faltan datos de seguridad del prospecto, y el perfil hematológico es de alto riesgo, por lo que se requieren salvaguardas.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), actualmente no disponible.
- Completar los datos del mecanismo de acción desde DrugBank.
- Aclarar la situación regulatoria: el registro 20154170 está cancelado y no hay registro vigente en Colombia.
- Definir un plan de monitoreo hematológico, hepático y renal, y manejo de interacciones (en especial deferiprona y samario).
- Verificar si la indicación de LCM está cubierta en un registro vigente o requiere una nueva solicitud ante INVIMA.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

