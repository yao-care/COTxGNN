---
layout: default
title: Doxorubicin
parent: Evidencia Alta (L1-L2)
nav_order: 235
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Doxorubicin: nueva indicación predicha, Sarcoma de Ewing (nivel de evidencia L1). Indicación original: DOXORUBICINA"
---

# Doxorubicin
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

# Doxorrubicina: De Doxorrubicina (indicación no detallada en el registro) a Sarcoma de Ewing

## Resumen en Una Frase

Doxorrubicina es un antineoplásico de la clase de las antraciclinas; en el registro sanitario colombiano su indicación figura solo como "DOXORUBICINA", sin detalle de la enfermedad tratada. El modelo TxGNN predice que podría ser efectivo para **Sarcoma de Ewing**, con **29 ensayos clínicos** y **20 publicaciones** que respaldan esta dirección. Cabe aclarar que se trata de un uso que ya forma parte del tratamiento estándar, más que de un reposicionamiento novedoso.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | DOXORUBICINA (el registro no detalla la enfermedad) |
| Nueva Indicación Predicha | Sarcoma de Ewing |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | Solo cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 3 (los 3 cancelados) |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la ficha del fármaco. Según el conocimiento general y el análisis de la predicción, la doxorrubicina es un inhibidor de la topoisomerasa II y un agente intercalante del ADN. Actúa dañando el material genético de las células que se dividen rápidamente.

El sarcoma de Ewing es un tumor de células de proliferación rápida, impulsado por la fusión génica EWS-FLI1, y es quimiosensible. La doxorrubicina es un componente central de los esquemas estándar multifármaco (VDC/IE, VAC/VAI), respaldado por guías de consenso y ensayos aleatorizados grandes.

Por lo tanto, la predicción refleja un uso ya establecido en la práctica oncológica. Las precauciones principales no son de eficacia, sino de seguridad: la cardiotoxicidad acumulada (uso de dexrazoxano y límite de dosis de por vida) y la programación de la intensidad de dosis.

---

## Evidencia de Ensayos Clínicos

Se muestran los ensayos más relevantes (de 29 registrados).

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00006734](https://clinicaltrials.gov/study/NCT00006734) | Fase 3 | Completado | 587 | Compara regímenes de quimioterapia con intensificación por compresión de intervalos en sarcoma de Ewing y tumores relacionados |
| [NCT01231906](https://clinicaltrials.gov/study/NCT01231906) | Fase 3 | Completado | 642 | Añade vincristina-topotecán-ciclofosfamida al esquema estándar de 5 fármacos (incluye doxorrubicina) en Ewing no metastásico |
| [NCT02063022](https://clinicaltrials.gov/study/NCT02063022) | Fase 3 | Completado | 278 | Intensificación de dosis frente a tratamiento estándar en Ewing no metastásico |
| [NCT02306161](https://clinicaltrials.gov/study/NCT02306161) | Fase 3 | Activo, sin reclutar | 312 | Ganitumab añadido a quimioterapia multifármaco en Ewing metastásico recién diagnosticado |
| [NCT00020566](https://clinicaltrials.gov/study/NCT00020566) | Fase 3 | Desconocido | 1200 | Estudio EURO-E.W.I.N.G.99: quimioterapia con o sin radioterapia o cirugía |
| [NCT00002516](https://clinicaltrials.gov/study/NCT00002516) | Fase 3 | Desconocido | N/D | Estudio cooperativo europeo EICESS 92: compara regímenes de quimioterapia más cirugía y radioterapia |
| [NCT00002466](https://clinicaltrials.gov/study/NCT00002466) | Fase 2 | Completado | N/D | Ciclofosfamida, doxorrubicina, vincristina, etopósido e ifosfamida seguidos de resección y radioterapia |
| [NCT00003667](https://clinicaltrials.gov/study/NCT00003667) | Fase 2 | Completado | N/D | VAC con dexrazoxano, con o sin ImmTher, en Ewing de alto riesgo |
| [NCT00038142](https://clinicaltrials.gov/study/NCT00038142) | Fase 2 | Terminado | 46 | Versión del mismo estudio VAC con dexrazoxano; terminado con pocos pacientes, lo que limita sus conclusiones |
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Fase 1/2 | Completado | 24 | Temsirolimus más doxorrubicina liposomal en sarcomas recurrentes |

---

## Evidencia de Literatura

Se muestran las publicaciones más relevantes (de 20 recuperadas), priorizando ensayos aleatorizados y revisiones.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [12594313](https://pubmed.ncbi.nlm.nih.gov/12594313/) | 2003 | ECA | N Engl J Med | Evalúa añadir ifosfamida y etopósido a la quimioterapia estándar en Ewing y PNET óseo recién diagnosticados |
| [36522207](https://pubmed.ncbi.nlm.nih.gov/36522207/) | 2022 | ECA Fase 3 | Lancet | Estudio EE2012: compara dos regímenes de quimioterapia en Ewing recién diagnosticado |
| [36669140](https://pubmed.ncbi.nlm.nih.gov/36669140/) | 2023 | ECA Fase 3 | J Clin Oncol | Ganitumab con quimioterapia de intervalo comprimido en Ewing metastásico |
| [23091096](https://pubmed.ncbi.nlm.nih.gov/23091096/) | 2012 | ECA | J Clin Oncol | Quimioterapia de intervalo comprimido en Ewing localizado (Children's Oncology Group) |
| [31952545](https://pubmed.ncbi.nlm.nih.gov/31952545/) | 2020 | Protocolo de ECA | Trials | Protocolo EURO EWING 2012 para Ewing de nuevo diagnóstico |
| [37403815](https://pubmed.ncbi.nlm.nih.gov/37403815/) | 2023 | Revisión | Cancer | Recomendaciones de consenso del National Ewing Sarcoma Tumor Board |
| [26304893](https://pubmed.ncbi.nlm.nih.gov/26304893/) | 2015 | Revisión | J Clin Oncol | Manejo actual del sarcoma de Ewing y enfoques futuros |
| [20152770](https://pubmed.ncbi.nlm.nih.gov/20152770/) | 2010 | Revisión | Lancet Oncol | Supervivencia de ~75% en enfermedad localizada; la enfermedad metastásica sigue con mal pronóstico |
| [1833556](https://pubmed.ncbi.nlm.nih.gov/1833556/) | 1991 | Análisis de intensidad de dosis | J Natl Cancer Inst | Influencia de la intensidad de dosis de doxorrubicina en la respuesta y el desenlace en osteosarcoma y sarcoma de Ewing |
| [30231396](https://pubmed.ncbi.nlm.nih.gov/30231396/) | 2018 | Revisión | ASCO Educ Book | Predicción y prevención de la cardiotoxicidad por antraciclinas |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20155365 | GRANA (cancelado) | Solución inyectable | DOXORUBICINA |
| 20241643 | DOXO SPAL 2MG/ML SOLUCION INYECTABLE (cancelado) | Solución inyectable | DOXORUBICINA |
| 19969115 | DOXOPEG ® 2 MG/ML (cancelado) | Suspensión inyectable | DOXORUBICINA |

Ninguno de los tres registros está vigente actualmente.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (antraciclina; inhibidor de topoisomerasa II) |
| Riesgo de Mielosupresión | Alto. Las asociaciones de contraindicación de la base de conocimiento incluyen neutropenia, leucopenia, trombocitopenia y anemia |
| Clasificación de Emetogenicidad | Moderada a alta, según la clase del fármaco |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal, bilirrubina, función cardíaca (fracción de eyección, troponina y péptidos natriuréticos), dosis acumulada |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en la base de conocimiento (no provienen del prospecto):** insuficiencia y enfermedad hepática, enfermedad de la vesícula biliar, hiperbilirrubinemia (incluido el síndrome de Gilbert), trombocitopenia, neutropenia, agranulocitosis, leucopenia, anemia, enfermedad cardíaca y cardiovascular, miocardiopatías, insuficiencia cardíaca congestiva, enfermedad de conducción cardíaca, paro cardíaco súbito, deficiencia de G6PD y enfermedades infecciosas (incluidas las fúngicas).
- **Interacciones farmacológicas:** se identificaron 665 interacciones. Entre las de nivel **mayor** están dolasetrón, cisaprida y papaverina. Entre las de nivel moderado figuran ondansetrón, granisetrón, palonosetrón, aprepitant, rolapitant, dexametasona, claritromicina, levofloxacino y famotidina. Entre las de nivel menor, el ácido ascórbico y el metronidazol.
- Se debe consultar el prospecto para las advertencias y contraindicaciones oficiales, que no están disponibles en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Para el sarcoma de Ewing existen varios ensayos de Fase 3 completados y ECA publicados en revistas de alto nivel, y la doxorrubicina es parte del esquema estándar. La evidencia es suficiente (L1), pero el perfil de toxicidad, sobre todo cardíaca y hematológica, exige salvaguardas. Además, no hay registros sanitarios vigentes en Colombia.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto oficial (INVIMA) para confirmar advertencias y contraindicaciones.
- Confirmar el mecanismo de acción en DrugBank.
- Definir un plan de cardioprotección (dexrazoxano, límite de dosis acumulada de por vida) y monitoreo cardíaco.
- Verificar la disponibilidad regulatoria: ningún registro vigente en Colombia, por lo que habría que gestionar uno nuevo o la importación.
- Definir el esquema y la intensidad de dosis según los protocolos establecidos.

**Otras indicaciones predichas (no priorizadas):** rabdomiosarcoma y sarcomas de tejidos blandos (L1 a nivel de sarcoma de tejidos blandos, aplicabilidad directa parcial; pregunta de investigación), blastoma pleuropulmonar (L3; pregunta de investigación), y otras con evidencia indirecta o preclínica (L4-L5; Hold).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

