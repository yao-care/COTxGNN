---
layout: default
title: Clofarabine
parent: Solo Predicción del Modelo (L5)
nav_order: 133
evidence_level: L5
indication_count: 10
---

# Clofarabine
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

# Clofarabina: De Leucemia Linfoblástica Aguda Pediátrica Recidivante/Refractaria a Leucemia Mieloide

## Resumen en Una Frase

Clofarabina es un análogo de nucleósidos de purina, usado originalmente en pacientes pediátricos con leucemia linfoblástica aguda (LLA) recidivante o refractaria.
El modelo TxGNN predice que podría ser efectivo para **leucemia mieloide**,
con **50 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | El texto del registro INVIMA solo dice "CLOFARABINA", sin indicación explícita. Según la farmacología: LLA pediátrica recidivante/refractaria |
| Nueva Indicación Predicha | Leucemia mieloide |
| Puntaje de Predicción TxGNN | 99.88% |
| Nivel de Evidencia | L1 (por regla: 2 ensayos Fase 3 completados; el Evidence Pack asigna L2, ver nota abajo) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 10 |
| Decisión Recomendada | Proceed with Guardrails |

> **Nota sobre el nivel de evidencia:** los ensayos Fase 3 completados NCT01471444 y NCT02085408 cumplen el criterio L1, pero su relevancia aún está pendiente de revisión manual en el Evidence Pack, que por eso asigna L2. Conviene confirmar los resultados antes de sostener L1.

## ¿Por qué es Razonable esta Predicción?

El campo original de mecanismo de acción viene vacío en el Evidence Pack. Aun así, la farmacología y la literatura permiten describirlo. Clofarabina es un análogo de nucleósidos de purina de segunda generación, diseñado para reunir las mejores cualidades de fludarabina y cladribina. Inhibe la ribonucleótido reductasa (blancos RRM1 y RRM2) y la ADN polimerasa. Esto reduce los desoxinucleótidos disponibles para replicar el ADN, e induce apoptosis.

La LLA y la leucemia mieloide son leucemias agudas de células blásticas en proliferación rápida. Un fármaco que bloquea la síntesis de ADN debería actuar sobre ambas. Esto es coherente con la evidencia: clofarabina se ha estudiado en leucemia mieloide aguda (LMA) y síndromes mielodisplásicos, sola o combinada con citarabina, idarrubicina, daunorrubicina y regímenes de acondicionamiento para trasplante.

Este razonamiento mecanístico se apoya en farmacología conocida y en la literatura, no en el campo MOA de la fuente. El puntaje TxGNN (0.9988) coincide con la señal clínica observada.

## Evidencia de Ensayos Clínicos

Se muestran 10 de 50 ensayos, priorizando Fase 3 y los relacionados directamente con LMA.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02085408](https://clinicaltrials.gov/study/NCT02085408) | Fase 3 | Completado | 727 | Clofarabina como inducción y postremisión vs. daunorrubicina + citarabina, seguido de decitabina oNo, en LMA de novo en mayores de 60 años |
| [NCT01471444](https://clinicaltrials.gov/study/NCT01471444) | Fase 3 | Completado | 256 | Aleatorizado: fludarabina-clofarabina vs. fludarabina sola con busulfán IV antes de trasplante alogénico en LMA/SMD |
| [NCT05477589](https://clinicaltrials.gov/study/NCT05477589) | Fase 3 | Reclutando | 170 | CloFluBu vs. BuCyMel como acondicionamiento en niños con LMA sometidos a trasplante alogénico |
| [NCT00932412](https://clinicaltrials.gov/study/NCT00932412) | Fase 2 | Completado | 735 | Clofarabina/citarabina intermedia (CLARA) vs. citarabina en dosis altas como consolidación en LMA de novo en jóvenes |
| [NCT01252667](https://clinicaltrials.gov/study/NCT01252667) | Fase 2 | Completado | 44 | Clofarabina con TBI en dosis baja para reducir recaídas tras trasplante en LMA |
| [NCT00814164](https://clinicaltrials.gov/study/NCT00814164) | Fase 2 | Terminado | 21 | Clofarabina + daunorrubicina en LMA nueva en ≥60 años, con evaluación de mecanismos de resistencia |
| [NCT00088218](https://clinicaltrials.gov/study/NCT00088218) | Fase 2 | Completado | 95 | Clofarabina sola vs. combinada con citarabina en dosis baja en LMA y SMD de alto riesgo sin tratamiento previo, ≥60 años |
| [NCT00042354](https://clinicaltrials.gov/study/NCT00042354) | Fase 2 | Completado | 40 | Clofarabina en LMA pediátrica recidivante o refractaria |
| [NCT00299156](https://clinicaltrials.gov/study/NCT00299156) | Fase 2 | Completado | 65 | Clofarabina oral semanal en síndrome mielodisplásico (neoplasia mieloide relacionada) |
| [NCT01041508](https://clinicaltrials.gov/study/NCT01041508) | Fase 1 | Completado | 18 | Viabilidad de clofarabina con TBI en dosis baja como acondicionamiento no mieloablativo |

## Evidencia de Literatura

Se muestran 10 de 20 publicaciones. Hay un ECA Fase 3 y no se recuperaron reportes de caso relevantes.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31246522](https://pubmed.ncbi.nlm.nih.gov/31246522/) | 2019 | ECA Fase 3 | J Clin Oncol | Ensayo AML08: clofarabina puede sustituir antraciclinas y etopósido en la inducción de LMA infantil, con menor exposición a estos fármacos |
| [32187883](https://pubmed.ncbi.nlm.nih.gov/32187883/) | 2020 | Estudio Fase 2 | Cancer Med | Clofarabina + citarabina + mitoxantrona (CLAM) en LMA refractaria/recidivante: altas tasas de respuesta y buen puente al trasplante |
| [31637757](https://pubmed.ncbi.nlm.nih.gov/31637757/) | 2020 | Fase I/II | Am J Hematol | Clofarabina con TBI de 2 Gy como acondicionamiento no mieloablativo en adultos con LMA no aptos para regímenes intensos |
| [36336258](https://pubmed.ncbi.nlm.nih.gov/36336258/) | 2023 | Cohorte | Transplant Cell Ther | Clofarabina + busulfán (acondicionamiento mieloablativo) en neoplasias mieloides activas |
| [40746302](https://pubmed.ncbi.nlm.nih.gov/40746302/) | 2025 | Fase I/II | Br J Haematol | Bisantreno + fludarabina + clofarabina como rescate en 21 pacientes con LMA refractaria o recidivante |
| [22957815](https://pubmed.ncbi.nlm.nih.gov/22957815/) | 2013 | Revisión | Leuk Lymphoma | Papel de clofarabina en LMA; inhibe ribonucleótido reductasa y ADN polimerasa, con mayor estabilidad que sus precursores |
| [25457773](https://pubmed.ncbi.nlm.nih.gov/25457773/) | 2015 | Revisión | Crit Rev Oncol Hematol | Clofarabina en adultos con LMA: desarrollo en monoterapia y estrategias de combinación en primera y segunda línea |
| [19852733](https://pubmed.ncbi.nlm.nih.gov/19852733/) | 2009 | Revisión | Future Oncol | Actividad significativa en LMA del adulto; podría integrarse a regímenes de inducción y consolidación |
| [17852710](https://pubmed.ncbi.nlm.nih.gov/17852710/) | 2007 | Revisión | Leuk Lymphoma | Tres mecanismos propuestos (inhibición de la ribonucleótido reductasa, incorporación al ADN, apoptosis) y sinergia esperada con otros agentes |
| [16316309](https://pubmed.ncbi.nlm.nih.gov/16316309/) | 2005 | Revisión | Expert Opin Pharmacother | Actividad como agente único en leucemias agudas (LMA y LLA) |

## Información de Mercado en Colombia

El Evidence Pack lista 5 entradas, todas idénticas, del mismo registro. Se presentan una sola vez.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20137192 | RELUKA® Solución Concentrada para Infusión Inyectable (MSN Laboratories Private Limited) | Solución concentrada para infusión | Solo figura "CLOFARABINA" (sin texto de indicación) |

También se registra la forma "solución inyectable" entre las presentaciones disponibles.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (antimetabolito, análogo de nucleósidos de purina) |
| Riesgo de Mielosupresión | Alto, esperable en este tipo de antimetabolito. Un estudio español (PMID 22431002) reporta toxicidades hematológicas e infecciosas de grado >3 |
| Clasificación de Emetogenicidad | Sin datos en el Evidence Pack. Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal (monitoreo general para citotóxicos) |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la consulta de DDI se completó, pero las 2 entradas son blancos farmacológicos (RRM1 y RRM2), no interacciones con otros medicamentos. Un estudio de farmacocinética (NCT01169012) evaluó el efecto de cimetidina sobre el aclaramiento de clofarabina.
- **Otras señales de la literatura**: se reportó un caso pediátrico de hipersensibilidad con desensibilización exitosa (PMID 34907607).

Consultar el prospecto para advertencias y contraindicaciones. El prospecto de INVIMA aún no se ha revisado.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay abundante evidencia clínica en leucemia mieloide, incluidos dos ensayos Fase 3 completados, un ECA Fase 3 publicado en LMA infantil y múltiples estudios Fase 2. Además, el mecanismo es coherente y el fármaco ya está comercializado en Colombia. Sin embargo, la mayoría de los estudios son combinaciones o regímenes de acondicionamiento, y no se dispone de los datos de seguridad del prospecto local.

**Para avanzar se necesita:**
- Descargar y revisar el prospecto de INVIMA (advertencias y contraindicaciones), el vacío que hoy bloquea el tamizaje de seguridad.
- Confirmar la indicación efectivamente aprobada en el registro 20137192, porque el texto solo dice "CLOFARABINA".
- Revisar los resultados de NCT02085408 y NCT01471444 para consolidar el nivel de evidencia (L1 o L2).
- Definir la población objetivo (adultos mayores, pediátrica o acondicionamiento pre-trasplante) y un plan de monitoreo hematológico.
- Tener en cuenta que la LLA, otra indicación predicha, ya está en la indicación original del fármaco, así que su novedad como reposicionamiento es limitada.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

