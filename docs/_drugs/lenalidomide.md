---
layout: default
title: Lenalidomide
parent: Evidencia Alta (L1-L2)
nav_order: 388
evidence_level: L2
indication_count: 6
last_modified_at: 2026-10-14
description: "Lenalidomide: nueva indicación predicha, Leucemia mieloide (nivel de evidencia L2). Indicación original: LENALIDOMIDA"
monitor_inn: "Lenalidomide"
predicted_indications: ["myeloid leukemia", "unclassified myelodysplastic syndrome", "refractory cytopenia of childhood", "aregenerative anemia", "severe congenital hypochromic anemia with ringed sideroblasts", "partial deletion of the long arm of chromosome 5"]
---

# Lenalidomide
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **6** 
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

# Lenalidomida: De Indicación Registrada (Lenalidomida) a Leucemia Mieloide

## Resumen en Una Frase

Lenalidomida es un inmunomodulador oral derivado de la talidomida, registrado en Colombia bajo el nombre del propio principio activo, sin que el registro detalle una indicación específica. El modelo TxGNN predice que podría ser efectivo para **leucemia mieloide**, con **43 ensayos clínicos** y **19 publicaciones** vinculados, aunque la literatura es mayormente sobre síndromes mielodisplásicos (SMD) y la evidencia específica en leucemia mieloide aguda (LMA) es más limitada de lo que sugiere el número de ensayos.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | LENALIDOMIDA (el registro sanitario no detalla la indicación) |
| Nueva Indicación Predicha | Leucemia mieloide |
| Puntaje de Predicción TxGNN | 99.49% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 4 (todos cancelados) |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este reporte no incluyen el mecanismo de acción registrado en la base de datos. Según la farmacología conocida, lenalidomida se une a cereblón (CRBN) y redirige la ligasa E3 CRL4-CRBN para degradar los factores de transcripción IKZF1 e IKZF3 y la caseína quinasa 1 alfa (CK1α). Esta última explica la respuesta en el SMD con deleción 5q. Además, tiene efectos inmunomoduladores (activación de células NK y T) que podrían respaldar su uso como mantenimiento tras la remisión en LMA.

Lenalidomida está aprobada en otros países para mieloma múltiple, SMD con del(5q) y ciertos linfomas. El SMD y la LMA son neoplasias mieloides estrechamente relacionadas: cerca de un tercio de los SMD evoluciona a LMA, y varios ensayos prueban lenalidomida en ambas enfermedades a la vez, lo que respalda la plausibilidad de la predicción.

El puntaje TxGNN muy alto (0.995) concuerda con la gran cantidad de ensayos en neoplasias mieloides. Sin embargo, la literatura aportada es en su mayoría revisiones de SMD, por lo que el mecanismo y la eficacia en LMA deben confirmarse con estudios específicos.

---

## Evidencia de Ensayos Clínicos

Se identificaron 43 ensayos; se muestran los 10 más relevantes (ensayos de fase 2 o superior y los calificados con mayor relevancia).

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02126553](https://clinicaltrials.gov/study/NCT02126553) | Fase 2 | Completado | 29 | Mantenimiento con lenalidomida en LMA de alto riesgo en remisión; la señal de agente único más directa del conjunto |
| [NCT00360672](https://clinicaltrials.gov/study/NCT00360672) | Fase 2 | Completado | 27 | Lenalidomida en LMA recidivante/refractaria o SMD de alto riesgo con anomalías del cromosoma 5; estudio de un solo brazo |
| [NCT00831766](https://clinicaltrials.gov/study/NCT00831766) | Fase 1/2 | Completado | 51 | Idarrubicina + citarabina seguidas de lenalidomida en SMD (RAEB-2) o LMA sin tratamiento previo |
| [NCT00352001](https://clinicaltrials.gov/study/NCT00352001) | Fase 1/2 | Completado | 37 | Lenalidomida + azacitidina en SMD avanzado y neoplasias mieloides |
| [NCT01038635](https://clinicaltrials.gov/study/NCT01038635) | Fase 1/2 | Completado | 94 | Azacitidina + lenalidomida en SMD de alto riesgo y LMA; dosis máxima tolerada y respuesta |
| [NCT01301820](https://clinicaltrials.gov/study/NCT01301820) | Fase 2 | Completado | 120 | Mantenimiento alternando lenalidomida y azacitidina en LMA de pronóstico adverso en adultos mayores tras inducción |
| [NCT01358734](https://clinicaltrials.gov/study/NCT01358734) | Fase 2 | Completado | 88 | Aleatorizado: lenalidomida en dosis altas, azacitidina secuencial + lenalidomida, o azacitidina sola, en LMA de adultos ≥65 años |
| [NCT00352365](https://clinicaltrials.gov/study/NCT00352365) | Fase 2 | Completado | 41 | Lenalidomida en LMA con del(5q) en mayores de 60 años que rechazan quimioterapia de inducción |
| [NCT00843882](https://clinicaltrials.gov/study/NCT00843882) | Fase 3 | Activo, sin reclutar | 247 | Lenalidomida con o sin epoetina alfa en SMD de bajo riesgo con anemia sintomática (no es LMA) |
| [NCT04490707](https://clinicaltrials.gov/study/NCT04490707) | Fase 3 | Desconocido | 60 | Azacitidina + lenalidomida como mantenimiento guiado por EMR en LMA de adultos mayores o no aptos |

**Nota:** los ensayos de fase 3 del conjunto no están completados (uno activo sin reclutar y otro de estado desconocido), y la mayoría de los estudios son pequeños, de fase 1 o 2 y de un solo brazo.

---

## Evidencia de Literatura

Se muestran las publicaciones más relevantes (prioridad: revisiones específicas de lenalidomida/LMA y estudios mecanísticos).

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [23316859](https://pubmed.ncbi.nlm.nih.gov/23316859/) | 2013 | Revisión | Expert Opin Investig Drugs | Lenalidomida como tratamiento novedoso de la LMA; resume los ensayos en SMD de alto riesgo y LMA |
| [32899586](https://pubmed.ncbi.nlm.nih.gov/32899586/) | 2020 | Revisión | Cancers | Fármacos inmunomoduladores en LMA: propiedades inmunomoduladoras, antiangiogénicas y proapoptóticas |
| [39881283](https://pubmed.ncbi.nlm.nih.gov/39881283/) | 2025 | Estudio preclínico | Cell Mol Biol Lett | KDM5C aumenta la sensibilidad de células de LMA a lenalidomida al estabilizar cereblón |
| [37288607](https://pubmed.ncbi.nlm.nih.gov/37288607/) | 2023 | Revisión | Am J Hematol | Actualización 2023 sobre diagnóstico, estratificación de riesgo y manejo de SMD |
| [37874917](https://pubmed.ncbi.nlm.nih.gov/37874917/) | 2023 | Revisión | Blood | Toma de decisiones clínicas y tratamiento de SMD |
| [29795386](https://pubmed.ncbi.nlm.nih.gov/29795386/) | 2018 | Revisión | Blood Cancer J | Algoritmo de tratamiento de SMD 2018 |
| [17488990](https://pubmed.ncbi.nlm.nih.gov/17488990/) | 2007 | Revisión | J Clin Oncol | LMA y SMD en pacientes mayores; respalda el uso de terapias en investigación |
| [22483153](https://pubmed.ncbi.nlm.nih.gov/22483153/) | 2012 | Revisión | Curr Cancer Drug Targets | Fármacos nuevos y emergentes para la LMA |
| [20416083](https://pubmed.ncbi.nlm.nih.gov/20416083/) | 2010 | Revisión | J Hematol Oncol | Nuevos agentes y regímenes para LMA (reunión anual ASH 2009) |
| [41348013](https://pubmed.ncbi.nlm.nih.gov/41348013/) | 2025 | Revisión | Hematology ASH Educ Program | Actualización en SMD de riesgo bajo e intermedio |

**Nota:** no hay ensayos aleatorizados entre las publicaciones aportadas para esta indicación; predominan las revisiones sobre SMD.

---

## Información de Mercado en Colombia

Los cuatro registros sanitarios están cancelados; actualmente no hay productos con lenalidomida vigentes en el mercado colombiano según los datos compilados.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20115050 | LADEVINA® 25 MG | Cápsula dura | LENALIDOMIDA (cancelado) |
| 20164374 | ALIDA® 25 MG | Cápsula dura | LENALIDOMIDA (cancelado) |
| 20199477 | CIFEROL® 10 MG | Cápsula dura | LENALIDOMIDA (cancelado) |
| 20137942 | LENOSIDE 15 | Cápsula dura | LENALIDOMIDA (cancelado) |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Inmunomodulador/agente dirigido (degradador de proteínas mediado por cereblón); no es un citotóxico convencional |
| Riesgo de Mielosupresión | Alto: el grafo de conocimiento asocia el fármaco con contraindicaciones por trombocitopenia, neutropenia y agranulocitosis |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial y recuento de plaquetas, función renal y hepática |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto; por su relación estructural con la talidomida, requiere precauciones de manejo y programas de prevención de embarazo |

---

## Consideraciones de Seguridad

- **Condiciones asociadas a contraindicación o precaución (grafo de conocimiento TxGNN, no texto del prospecto):** trombocitopenia, neutropenia, agranulocitosis, embolia pulmonar, insuficiencia renal, cáncer y embrioma.
- **Interacciones farmacológicas:** no se registraron interacciones fármaco-fármaco; solo consta la interacción farmacológica con su diana, cereblón (CRBN).

Las advertencias y contraindicaciones del prospecto no están disponibles en los datos compilados; consultar el prospecto para información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen varios ensayos de fase 2 completados con lenalidomida en LMA (por ejemplo NCT02126553, NCT00360672), junto con un mecanismo coherente y un puntaje TxGNN muy alto. Sin embargo, son estudios pequeños y de un solo brazo, sin ECA de fase 3 completados, y la literatura es mayormente sobre SMD; por eso se recomienda avanzar solo con salvaguardas.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA con advertencias y contraindicaciones (bloqueante para el tamizaje de seguridad).
- Completar los datos de mecanismo de acción desde DrugBank.
- Revisar literatura específica de LMA (ensayos publicados, no solo revisiones de SMD).
- Aclarar la situación regulatoria: los cuatro registros están cancelados, por lo que habría que evaluar un nuevo registro o importación.
- Plan de monitoreo hematológico (citopenias), riesgo tromboembólico y programa de prevención de embarazo.
- Hay otras predicciones de menor soporte (SMD no clasificado, citopenia refractaria de la infancia, anemia aregenerativa, anemia sideroblástica congénita y deleción parcial del brazo largo del cromosoma 5). La más cercana es el SMD con del(5q), que debería evaluarse como línea de trabajo propia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

