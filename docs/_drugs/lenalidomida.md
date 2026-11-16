---
layout: default
title: Lenalidomida
parent: Evidencia Alta (L1-L2)
nav_order: 387
evidence_level: L2
indication_count: 4
drugbank_id: DB00480
monitor_inn: "Lenalidomide"
predicted_indications: ["myeloid leukemia", "refractory cytopenia of childhood", "aregenerative anemia", "severe congenital hypochromic anemia with ringed sideroblasts"]
last_modified_at: 2026-11-16
description: "Lenalidomida: nueva indicación predicha, Leucemia mieloide (myeloid leukemia) (nivel de evidencia L2). Indicación original: LENALIDOMIDA"
---

# Lenalidomida
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **4** 
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

## Lenalidomida: Leucemia mieloide (myeloid leukemia)
{: .text-alpha }

## Resumen en Una Frase

Lenalidomida es un inmunomodulador oral que actúa sobre la proteína cereblón (CRBN) y cuenta con múltiples registros sanitarios vigentes en Colombia.
El modelo TxGNN predice que podría ser efectivo para **leucemia mieloide (myeloid leukemia)**,
con **40 ensayos clínicos** y **19 publicaciones** recuperados en los datos compilados para este informe; sin embargo, ninguna de las publicaciones evalúa directamente esta enfermedad con lenalidomida como intervención principal de forma concluyente (son sobre todo revisiones de síndromes mielodisplásicos).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | LENALIDOMIDA |
| Nueva Indicación Predicha | Leucemia mieloide (myeloid leukemia) |
| Puntaje de Predicción TxGNN | 0.9949 |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 20) |
| Número de Registros Sanitarios | al menos 20 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Lenalidomida se une a cereblón (CRBN) y redirige el complejo ubiquitina ligasa CRL4-CRBN para degradar los factores de transcripción IKZF1 e IKZF3 y la caseína quinasa 1 alfa (CK1α, codificada por CSNK1A1). La degradación de CK1α explica su actividad en el síndrome mielodisplásico con deleción 5q, y podría ejercer presión de letalidad sintética sobre clones mieloides con del(5q). Además, sus efectos inmunomoduladores (activación de linfocitos T y NK) podrían aportar actividad antileucémica, por ejemplo como mantenimiento tras trasplante.

La relación con la leucemia mieloide aguda (LMA) es biológicamente plausible por la cercanía con los síndromes mielodisplásicos, que pueden evolucionar a LMA. No obstante, la evidencia en LMA es más débil y menos definida por biomarcadores que en el SMD con del(5q).

Cabe señalar que los datos de mecanismo de acción no estaban disponibles en la ficha del fármaco; la explicación anterior proviene del análisis mecanístico de la predicción.

**Nivel de evidencia:** Los ensayos de fase 2 completados (por ejemplo, NCT00546897 y NCT01301820) estudian directamente la LMA, pero son de un solo brazo o no definitivos, y no hay dos ensayos de fase 3 completados en LMA. Se asigna L2 según el análisis de la predicción principal; se recomienda interpretarlo con cautela, ya que el único fase 3 de la lista (NCT00843882) es en SMD, y el otro (NCT04490707) tiene estado desconocido.

## Evidencia de Ensayos Clínicos

Se muestran los 10 ensayos más relevantes (de 40 recuperados):

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00546897](https://clinicaltrials.gov/study/NCT00546897) | Fase 2 | Completado | 48 | Lenalidomida en monoterapia en LMA no tratada, ≥60 años, sin anomalías del 5q |
| [NCT01301820](https://clinicaltrials.gov/study/NCT01301820) | Fase 2 | Completado | 120 | Mantenimiento alternando lenalidomida y azacitidina tras inducción en LMA de mal pronóstico en adultos mayores |
| [NCT01358734](https://clinicaltrials.gov/study/NCT01358734) | Fase 2 | Completado | 88 | Lenalidomida, azacitidina secuencial + lenalidomida, o azacitidina sola en LMA de reciente diagnóstico (≥65 años) |
| [NCT00352365](https://clinicaltrials.gov/study/NCT00352365) | Fase 2 | Completado | 41 | Lenalidomida en LMA con del(5q) en mayores de 60 años que rechazan quimioterapia |
| [NCT03118466](https://clinicaltrials.gov/study/NCT03118466) | Fase 2 | Completado | 41 | MEC más lenalidomida en LMA recaída o refractaria |
| [NCT02538965](https://clinicaltrials.gov/study/NCT02538965) | Fase 2 | Completado | 17 | Actividad y seguridad en pacientes pediátricos con LMA recaída/refractaria |
| [NCT02126553](https://clinicaltrials.gov/study/NCT02126553) | Fase 2 | Completado | 29 | Mantenimiento con lenalidomida en LMA de alto riesgo en remisión |
| [NCT01038635](https://clinicaltrials.gov/study/NCT01038635) | Fase 1/2 | Completado | 94 | Azacitidina + lenalidomida en SMD de alto riesgo y LMA |
| [NCT04490707](https://clinicaltrials.gov/study/NCT04490707) | Fase 3 | Desconocido | 60 | Azacitidina + lenalidomida como mantenimiento guiado por enfermedad residual medible en LMA de adultos mayores o no aptos |
| [NCT01132586](https://clinicaltrials.gov/study/NCT01132586) | Fase 1 | Completado | 61 | Lenalidomida con citarabina e idarrubicina en LMA: seguridad y dosis |

## Evidencia de Literatura

Las publicaciones recuperadas son en su mayoría revisiones sobre síndromes mielodisplásicos y no estudian directamente la leucemia mieloide con lenalidomida:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37288607](https://pubmed.ncbi.nlm.nih.gov/37288607/) | 2023 | Revisión | Am J Hematol | Actualización de diagnóstico, estratificación de riesgo y manejo de SMD |
| [42400116](https://pubmed.ncbi.nlm.nih.gov/42400116/) | 2026 | Revisión | Am J Hematol | Actualización 2026 de SMD |
| [37874917](https://pubmed.ncbi.nlm.nih.gov/37874917/) | 2023 | Revisión | Blood | Toma de decisiones clínicas y tratamiento de SMD |
| [24656536](https://pubmed.ncbi.nlm.nih.gov/24656536/) | 2014 | Revisión | Lancet | Revisión general de SMD y su progresión a leucemia mieloide aguda |
| [41348013](https://pubmed.ncbi.nlm.nih.gov/41348013/) | 2025 | Revisión | Hematology ASH Educ Program | Novedades en SMD de riesgo bajo/intermedio |
| [38066862](https://pubmed.ncbi.nlm.nih.gov/38066862/) | 2023 | Revisión | Hematology ASH Educ Program | Terapias de nueva generación en SMD de menor riesgo |
| [39721469](https://pubmed.ncbi.nlm.nih.gov/39721469/) | 2025 | Revisión | Leuk Res | Terapias combinadas con azacitidina en LMA no elegible para quimioterapia intensiva |
| [25644743](https://pubmed.ncbi.nlm.nih.gov/25644743/) | 2015 | Revisión | Leuk Lymphoma | Anemia hemolítica asociada a lenalidomida (señal de seguridad) |
| [34864823](https://pubmed.ncbi.nlm.nih.gov/34864823/) | 2021 | Revisión | Blood Cancer J | Terapia de diferenciación en neoplasias mieloides |
| [29795386](https://pubmed.ncbi.nlm.nih.gov/29795386/) | 2018 | Revisión | Blood Cancer J | Algoritmo de tratamiento de SMD 2018 |

## Información de Mercado en Colombia

Hay al menos 20 registros sanitarios de lenalidomida en Colombia, todos de producto único y vigentes; la lista puede ser parcial. Se muestran 5:

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19999700 | REVLIMID® 10 MG CAPSULAS | Cápsula dura | Indicación no registrada en los datos locales |
| 19999701 | REVLIMID® 5MG CAPSULAS | Cápsula dura | Indicación no registrada en los datos locales |
| 20115046 | LADEVINA® 15 MG CÁPSULAS | Cápsula dura | Indicación no registrada en los datos locales |
| 20130202 | DOMIDE 25 MG CAPSULAS | Cápsula dura | Indicación no registrada en los datos locales |
| 20136207 | LENOSIDE 10 | Cápsulas duras y blandas | Indicación no registrada en los datos locales |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Agente antineoplásico inmunomodulador (degradador de proteínas vía cereblón); no es un citotóxico convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto; los ensayos en LMA reportan toxicidad hematológica relevante en combinación con quimioterapia |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Advertencias de la literatura**: se describe anemia hemolítica asociada a lenalidomida (PMID 25644743) y un caso de miocarditis durante el tratamiento (PMID 20876827).

Consultar el prospecto para información de seguridad adicional; no se dispone de datos de advertencias, contraindicaciones ni interacciones en los datos compilados.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen numerosos ensayos de fase 1 y 2 en LMA, algunos completados con inscripción moderada, que respaldan la plausibilidad clínica, y el mecanismo es sólido en SMD con del(5q). Sin embargo, la evidencia en LMA es heterogénea, mayormente no aleatorizada, sin ensayos de fase 3 completados en esta enfermedad y sin literatura directa; por ello se recomienda avanzar solo con salvaguardas.

**Para avanzar se necesita:**
- Revisión de resultados publicados de los ensayos de fase 2 en LMA (NCT00546897, NCT01301820, NCT01358734) para valorar eficacia real.
- Definir subpoblaciones con biomarcadores (por ejemplo, del(5q)) donde la actividad sea más probable.
- Obtener el prospecto de INVIMA con advertencias y contraindicaciones, y datos del mecanismo de acción desde fuentes de referencia.
- Plan de monitoreo de seguridad hematológica y de riesgo tromboembólico y teratogénico.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Lenalidomida **no cuenta con ningun registro sanitario activo en Colombia** segun los datos consultados el 2026-03-29" | Ya no aparece tras regenerar el informe (2026-11-16: el informe se regeneró en noviembre de 2026 y ya no contiene esta afirmación; antes: Corregido) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

