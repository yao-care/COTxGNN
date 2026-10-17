---
layout: default
title: Pegaspargase
parent: Evidencia Alta (L1-L2)
nav_order: 503
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Pegaspargase: nueva indicación predicha, Leucemia/linfoma linfoblástico de precursores (nivel de evidencia L1). Indicación original: PEGASPARGASA"
monitor_inn: "pegaspargase"
predicted_indications: ["pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma", "chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation", "follicular lymphoma", "methylcobalamin deficiency type cblE", "lymphoid neoplasm", "Hodgkins lymphoma", "blast phase chronic myelogenous leukemia, BCR-ABL1 positive"]
---

# Pegaspargase
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

# Pegaspargasa: De PEGASPARGASA (registro INVIMA) a Leucemia/Linfoma Linfoblástico de Precursores

## Resumen en Una Frase

Pegaspargasa es una forma pegilada de la L-asparaginasa, registrada en Colombia bajo el nombre ONCASPAR®; el texto de indicación del registro solo repite el nombre del principio activo ("PEGASPARGASA"). El modelo TxGNN predice que podría ser efectiva para **leucemia/linfoma linfoblástico de precursores**, con **38 ensayos clínicos** y **19 publicaciones** asociados a esta predicción. Se trata de un uso establecido (en leucemia linfoblástica aguda) más que de un reposicionamiento propiamente dicho.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | PEGASPARGASA (el registro no detalla la indicación; solo repite el nombre del principio activo) |
| Nueva Indicación Predicha | Leucemia/linfoma linfoblástico de precursores |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la fuente de fármacos consultada. Según la información compilada para este informe, pegaspargasa es una L-asparaginasa pegilada que depleta la asparagina circulante. Los linfoblastos tienen poca expresión de asparagina sintetasa y dependen de la asparagina exógena. Su depleción produce inhibición selectiva de la síntesis de proteínas y apoptosis.

La indicación original no está descrita en el registro, pero la predicción coincide con el uso clínico establecido del fármaco: componente de esquemas de quimioterapia multiagente en leucemia linfoblástica aguda (LLA) y linfoma linfoblástico. Por ello, la predicción refleja una indicación ya conocida y no un hallazgo nuevo.

Otras predicciones del modelo (leucemia linfocítica crónica, linfoma folicular, deficiencia de metilcobalamina cblE) carecen de ensayos o literatura y de una base mecanística plausible; deben considerarse artefactos del modelo o proximidad ontológica. La predicción de linfoma de Hodgkin parece una etiqueta desajustada: la literatura asociada trata del linfoma NK/T extranodal, que debería evaluarse como indicación independiente.

---

## Evidencia de Ensayos Clínicos

Se muestran los ensayos más relevantes de un total de 38 asociados (priorizando los que incluyen pegaspargasa de forma explícita y los de Fase 3 completados):

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00905034](https://clinicaltrials.gov/study/NCT00905034) | Fase 2 | Completado | 37 | Esquema MOAD (metotrexato, vincristina, asparaginasa pegilada, dexametasona) en rescate de LLA |
| [NCT00967057](https://clinicaltrials.gov/study/NCT00967057) | Fase 3 | Completado | 470 | ALLR3: quimioterapia multiagente en LLA recaída/refractaria en jóvenes |
| [NCT00103285](https://clinicaltrials.gov/study/NCT00103285) | Fase 3 | Completado | 5377 | Regímenes de quimioterapia en LLA B-precursora de riesgo estándar recién diagnosticada |
| [NCT01190930](https://clinicaltrials.gov/study/NCT01190930) | Fase 3 | Completado | 9350 | Quimioterapia adaptada al riesgo en LLA-B de riesgo estándar o linfoma linfoblástico B localizado |
| [NCT02003222](https://clinicaltrials.gov/study/NCT02003222) | Fase 3 | Activo, sin reclutar | 488 | Blinatumomab añadido a quimioterapia (con pegaspargasa de base) en LLA-B recién diagnosticada |
| [NCT00890656](https://clinicaltrials.gov/study/NCT00890656) | Fase 2 | Completado | 90 | Hyper-CVAD aumentado en rescate de LLA; pegaspargasa como un componente |
| [NCT01005914](https://clinicaltrials.gov/study/NCT01005914) | Fase 2 | Terminado | 11 | Adición de PEG-asparaginasa a Hyper-CVAD en LLA adulta recién diagnosticada |
| [NCT05602194](https://clinicaltrials.gov/study/NCT05602194) | Fase 3 | Activo, sin reclutar | 440 | Levocarnitina para prevenir hepatotoxicidad asociada a asparaginasa (enfoque de seguridad) |
| [NCT03643276](https://clinicaltrials.gov/study/NCT03643276) | Fase 3 | Reclutando | 5000 | Protocolo AIEOP-BFM ALL 2017 en niños y adolescentes con LLA |
| [NCT03914625](https://clinicaltrials.gov/study/NCT03914625) | Fase 3 | Activo, sin reclutar | 6720 | Blinatumomab con quimioterapia (incluye pegaspargasa) en LLA-B de riesgo estándar o síndrome de Down |

En la mayoría de estos ensayos pegaspargasa forma parte del esquema de base y no es la variable evaluada.

---

## Evidencia de Literatura

Se muestran las publicaciones más relevantes (priorizando ECA y revisiones):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35271306](https://pubmed.ncbi.nlm.nih.gov/35271306/) | 2022 | ECA | J Clin Oncol | COG AALL1231: bortezomib en LLA-T y linfoma linfoblástico recién diagnosticados |
| [32813610](https://pubmed.ncbi.nlm.nih.gov/32813610/) | 2020 | ECA | J Clin Oncol | COG AALL0434: nelarabina en LLA-T recién diagnosticada |
| [27114587](https://pubmed.ncbi.nlm.nih.gov/27114587/) | 2016 | ECA | J Clin Oncol | AALL0232: dexametasona y metotrexato en dosis altas mejoran resultados en LLA-B de alto riesgo |
| [40109190](https://pubmed.ncbi.nlm.nih.gov/40109190/) | 2025 | Revisión (consenso de expertos) | Haematologica | Reconocimiento, prevención y manejo de eventos adversos de asparaginasa/pegaspargasa en adultos |
| [31030380](https://pubmed.ncbi.nlm.nih.gov/31030380/) | 2019 | Revisión | Drugs | Pegaspargasa (Oncaspar®) en LLA: mayor circulación y menor frecuencia de administración que la asparaginasa nativa |
| [37276451](https://pubmed.ncbi.nlm.nih.gov/37276451/) | 2023 | Cohorte | Blood Adv | Ensayo GIMEMA LAL1913: programa con pegaspargasa en LLA adulta Ph-negativa |
| [40858769](https://pubmed.ncbi.nlm.nih.gov/40858769/) | 2025 | Cohorte | Ann Hematol | Tolerabilidad de pegaspargasa en pacientes ≥55 años con LLA |
| [40492422](https://pubmed.ncbi.nlm.nih.gov/40492422/) | 2025 | Cohorte | Br J Haematol | Integración de blinatumomab en el régimen CALGB 10403 en adultos con LLA-B |
| [9161659](https://pubmed.ncbi.nlm.nih.gov/9161659/) | 1997 | Revisión | Ann Pharmacother | Revisión de química, farmacología, eficacia, efectos adversos y dosificación de pegaspargasa |
| [34228505](https://pubmed.ncbi.nlm.nih.gov/34228505/) | 2021 | No clasificado | J Clin Oncol | DFCI 11-001: eficacia y toxicidad de pegaspargasa frente a calaspargasa pegol en LLA infantil |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20105447 (cancelado) | ONCASPAR® 3750 UI | Solución inyectable | PEGASPARGASA |
| 20200646 (cancelado) | ONCASPAR® 750 U/ML polvo para solución inyectable | Polvo liofilizado para reconstituir a solución inyectable | PEGASPARGASA |

Ambos registros pertenecen a Les Laboratoires Servier y figuran como cancelados.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Agente antineoplásico enzimático (asparaginasa pegilada); no es un citotóxico convencional de tipo alquilante o antimetabolito |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Según la literatura compilada: función hepática, lipasa/amilasa (pancreatitis), triglicéridos, glucemia, parámetros de coagulación (trombosis) y signos de hipersensibilidad |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto y seguir las regulaciones institucionales de manejo de antineoplásicos |

---

## Consideraciones de Seguridad

- **Toxicidades descritas en la literatura:** hepatotoxicidad, pancreatitis, trombosis, hipertrigliceridemia, hiperglucemia (temporalmente ligada a la administración de pegaspargasa) y reacciones de hipersensibilidad. El riesgo de varias de estas toxicidades parece aumentar con la edad en adultos.
- **Interacciones farmacológicas:** se identificaron 378 interacciones, las mostradas son de nivel moderado. Entre ellas: corticoides (hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida), antidiabéticos (metformina, acarbosa, alogliptina, saxagliptina, canagliflozina, dapagliflozina, clorpropamida, albiglutida, dulaglutida), antibióticos (doxiciclina, tetraciclina, claritromicina), ácido acetilsalicílico, bupropión y ácido quenodesoxicólico.

No se dispone de datos de advertencias ni contraindicaciones del prospecto. Consultar el prospecto para esa información.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La evidencia es sólida (múltiples ensayos de Fase 3 completados, con pegaspargasa en el esquema de base) para leucemia/linfoma linfoblástico, pero corresponde a un uso ya establecido y no a un reposicionamiento. Las toxicidades conocidas exigen medidas de control, y el producto no tiene registro vigente en Colombia.

**Para avanzar se necesita:**
- Verificar la situación regulatoria: ambos registros están cancelados, por lo que habría que definir si se requiere un nuevo registro o importación.
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones) y los datos del mecanismo de acción.
- Establecer un plan de monitoreo de seguridad (hígado, páncreas, lípidos, glucosa, coagulación, hipersensibilidad), con atención a adultos mayores.
- Evaluar por separado el linfoma NK/T extranodal como indicación independiente.
- Mantener en espera (Hold) las demás predicciones sin evidencia (leucemia linfocítica crónica, linfoma folicular, deficiencia de metilcobalamina cblE, fase blástica de leucemia mieloide crónica).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

