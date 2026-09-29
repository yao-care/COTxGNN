---
layout: default
title: Sunitinib
parent: Solo Predicción del Modelo (L5)
nav_order: 369
evidence_level: L5
indication_count: 10
---

# Sunitinib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Sunitinib: De Indicación No Especificada en el Registro a Liposarcoma

## Resumen en Una Frase

Sunitinib es un inhibidor multidiana de tirosina quinasas. Se conoce sobre todo por su uso en cáncer renal, tumores del estroma gastrointestinal (GIST) y tumores neuroendocrinos de páncreas. El registro de INVIMA no detalla su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **liposarcoma**, con **3 ensayos clínicos** (todos de Fase 2, uno con un fármaco distinto) y **9 publicaciones**. La evidencia proviene de estudios de Fase 2 no aleatorizados en poblaciones mixtas de sarcoma.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el campo de INVIMA solo dice "SUNITINIB") |
| Nueva Indicación Predicha | Liposarcoma |
| Puntaje de Predicción TxGNN | 99.87% |
| Nivel de Evidencia | L2 (según el Evidence Pack; los ensayos de Fase 2 completados son de brazo único, no aleatorizados) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 8 (el detalle disponible muestra 3 números de registro únicos) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información del análisis de reposicionamiento, sunitinib inhibe VEGFR, PDGFR, KIT y FLT3. Esto bloquea la angiogénesis y la señalización de factores de crecimiento que impulsan el crecimiento tumoral.

El fármaco tiene eficacia comprobada en tumores donde estas vías son centrales, como el GIST resistente a imatinib y el carcinoma renal. La angiogénesis y la señalización de PDGFR son impulsores plausibles en los sarcomas de tejidos blandos, incluido el liposarcoma. Por eso, mecanísticamente, el fármaco podría ser aplicable.

Sin embargo, la predicción del modelo es mucho más fuerte que la evidencia clínica. Los datos disponibles son de Fase 2 no aleatorizados, en poblaciones mixtas de sarcoma, con actividad limitada reportada en liposarcoma. No existen datos de Fase 3 ni aleatorizados. Por lo tanto, el puntaje tan alto de TxGNN no está respaldado por eficacia clínica demostrada.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00474994](https://clinicaltrials.gov/study/NCT00474994) | Fase 2 | Completado | 53 | Sunitinib en dosificación continua en sarcomas no GIST metastásicos, localmente avanzados o recurrentes. Es la población más relevante, e incluye histologías de liposarcoma. |
| [NCT00400569](https://clinicaltrials.gov/study/NCT00400569) | Fase 2 | Completado | 48 | Estudio abierto de un solo centro con sunitinib oral en sarcoma de tejidos blandos metastásico o irresecable (leiomiosarcoma, liposarcoma, fibrosarcoma, histiocitoma fibroso maligno). Los datos disponibles no confirman una cohorte definida de liposarcoma. |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Fase 2 | Completado | 131 | Protocolo SARC024 con **regorafenib** (no sunitinib) en subtipos seleccionados de sarcoma. Es relevante solo como comparación dentro de la misma clase de fármacos. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [21154746](https://pubmed.ncbi.nlm.nih.gov/21154746/) | 2011 | Fase 2 de brazo único | Int J Cancer | Estudio unicéntrico de seguridad y eficacia de sunitinib en sarcomas de tejidos blandos recaídos o refractarios, centrado en leiomiosarcoma, liposarcoma e histiocitoma fibroso maligno. |
| [38254762](https://pubmed.ncbi.nlm.nih.gov/38254762/) | 2024 | Revisión | Cancers | Alteraciones genéticas, epigenéticas y transcriptómicas del liposarcoma para la selección de terapias dirigidas. |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Revisión | Magyar Onkologia | El tratamiento médico de los sarcomas de tejidos blandos se orienta cada vez más por el subtipo histológico. |
| [24555529](https://pubmed.ncbi.nlm.nih.gov/24555529/) | 2014 | Revisión | Expert Rev Anticancer Ther | Terapias emergentes para sarcoma de tejidos blandos en adultos. |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Revisión | Ann Oncol | Terapia guiada por histología. Menciona trabectedina como activa en liposarcoma, con actividad muy alta en el mixoide. |
| [23482782](https://pubmed.ncbi.nlm.nih.gov/23482782/) | 2013 | Reporte de caso | Anticancer Res | Beneficio clínico prolongado con sunitinib en un caso de liposarcoma metastásico muy pretratado. |
| [38717131](https://pubmed.ncbi.nlm.nih.gov/38717131/) | 2024 | Serie de casos | Am J Surg Pathol | Análisis clinicopatológico de 25 casos de sarcoma miofibroblástico inflamatorio mixoide. Relevancia indirecta. |
| [28423517](https://pubmed.ncbi.nlm.nih.gov/28423517/) | 2017 | Cohorte genómica | Oncotarget | Secuenciación de condrosarcoma mixoide extraesquelético. Evalúa factores predictivos de beneficio con sunitinib. Relevancia indirecta. |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | Protocolo de ensayo (regorafenib) | BMC Cancer | Protocolo REGOSARC de Fase 2 aleatorizado con regorafenib en sarcoma avanzado. No evalúa sunitinib. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20196041 | RENISUN® 12.5MG CÁPSULAS DURAS | Cápsula dura | No especifica indicación (solo indica "SUNITINIB") |
| 20193310 | RENISUN® 50MG CÁPSULAS DURAS | Cápsula dura | No especifica indicación (solo indica "SUNITINIB") |
| 20194945 | RENISUN® 37.5MG CÁPSULAS DURAS | Cápsula dura | No especifica indicación (solo indica "SUNITINIB") |

Todos los registros pertenecen a HB HUMAN BIOSCIENCE S.A.S. El sistema reporta 8 registros en total, pero el detalle disponible muestra solo 3 números únicos (5 filas, con duplicados).

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor multiquinasa de tirosina quinasas: VEGFR, PDGFR, KIT, FLT3) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma, función hepática y renal. Según los estudios revisados, también presión arterial, función tiroidea (hipotiroidismo) y función cardíaca, por la toxicidad cardiovascular descrita. |
| Protección en Manejo | Consultar el prospecto y las regulaciones locales de manejo de fármacos antineoplásicos |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Los estudios revisados describen hipertensión, toxicidad cardíaca, toxicidad cutánea e hipotiroidismo asociados a sunitinib. No hay datos estructurados de advertencias, contraindicaciones ni interacciones farmacológicas en el Evidence Pack.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Los estudios de Fase 2 disponibles son de brazo único, con poblaciones mixtas de sarcoma y actividad limitada reportada en liposarcoma. No hay datos aleatorizados ni de Fase 3. El alto puntaje de TxGNN (99.87%) no está respaldado por eficacia clínica. Además, falta la información de seguridad del prospecto de INVIMA, que impide avanzar al tamizaje de seguridad.

**Para avanzar se necesita:**
- Obtener las advertencias y contraindicaciones del prospecto de INVIMA (brecha bloqueante).
- Completar los datos del mecanismo de acción desde DrugBank.
- Confirmar si NCT00400569 y NCT00474994 incluyeron cohortes de liposarcoma y cuáles fueron los resultados por subtipo.
- Aclarar la indicación aprobada en el registro colombiano, que hoy solo dice "SUNITINIB".
- Contar con evidencia prospectiva o aleatorizada específica en liposarcoma antes de reconsiderar la decisión.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

