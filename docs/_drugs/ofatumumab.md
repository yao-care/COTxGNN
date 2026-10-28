---
layout: default
title: Ofatumumab
parent: Evidencia Alta (L1-L2)
nav_order: 478
evidence_level: L1
indication_count: 4
monitor_inn: "OFATUMUMAB"
predicted_indications: ["follicular lymphoma", "metastatic neoplasm", "malignant spiradenoma", "Langerhans cell histiocytosis"]
last_modified_at: 2026-10-23
description: "Ofatumumab: nueva indicación predicha, Linfoma folicular (nivel de evidencia L1). Indicación original: No especificada en el registro (el texto solo indica \"OFATUMUMAB\")"
---

# Ofatumumab
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **4** 
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

## Ofatumumab: De la indicación registrada en INVIMA a Linfoma Folicular
{: .text-alpha }

## Resumen en Una Frase

Ofatumumab es un anticuerpo monoclonal anti-CD20 totalmente humano, comercializado en Colombia como KESIMPTA (solución inyectable). El texto de indicación del registro local solo repite el nombre del principio activo, por lo que no precisa un uso aprobado concreto.
El modelo TxGNN predice que podría ser efectivo para el **linfoma folicular**, con **11 ensayos clínicos** y **20 publicaciones** compilados que respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto solo indica "OFATUMUMAB") |
| Nueva Indicación Predicha | Linfoma folicular |
| Puntaje de Predicción TxGNN | 0.9970 |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Proceed with Guardrails |

**Nota sobre el nivel de evidencia:** hay varios ensayos de Fase 2 completados que estudian directamente el linfoma folicular. El único ensayo de Fase 3 (NCT01077518) está terminado, no completado, y se centra en linfoma indolente no Hodgkin refractario a rituximab, por lo que no se cumple el criterio de dos ECA de Fase 3 completados. Por criterio estricto, el nivel sería L2, que coincide con la clasificación interna de los datos compilados. Se adopta **L2**.

> Corrección de la tabla: **Nivel de Evidencia: L2**.

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la ficha del fármaco. Según la información conocida, ofatumumab es un anticuerpo monoclonal humano dirigido contra CD20, una proteína de la superficie de los linfocitos B. Se une a un epítopo cercano a la membrana y puede destruir las células B mediante citotoxicidad dependiente del complemento y citotoxicidad celular dependiente de anticuerpos.

El linfoma folicular es un tumor de linfocitos B que expresa CD20, de modo que la diana es directamente relevante. Los datos compilados señalan actividad en enfermedad refractaria a rituximab, otro anticuerpo anti-CD20 que es parte del tratamiento estándar de esta enfermedad.

La relación con la indicación local no puede evaluarse con precisión, porque el registro colombiano no detalla el uso aprobado. Cabe señalar que el linfoma folicular figura aquí como una predicción del modelo respaldada por ensayos, y no como una indicación aprobada en Colombia.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01286272](https://clinicaltrials.gov/study/NCT01286272) | Fase 2 | Completado | 135 | Ensayo aleatorizado: ofatumumab + bendamustina con o sin bortezomib en linfoma folicular sin tratamiento previo |
| [NCT00494780](https://clinicaltrials.gov/study/NCT00494780) | Fase 2 | Completado | 59 | Ofatumumab con CHOP a dos dosis en linfoma folicular sin tratamiento previo |
| [NCT01190449](https://clinicaltrials.gov/study/NCT01190449) | Fase 2 | Completado | 51 | Ofatumumab en monoterapia en linfoma folicular no Hodgkin sin tratamiento previo |
| [NCT00394836](https://clinicaltrials.gov/study/NCT00394836) | Fase 2 | Completado | 116 | Ofatumumab de un solo brazo en linfoma folicular refractario a rituximab |
| [NCT02710643](https://clinicaltrials.gov/study/NCT02710643) | Fase 2 | Completado | 110 | Estudio MIRO: radioterapia local con o sin ofatumumab en linfoma folicular en estadio I/II |
| [NCT01239394](https://clinicaltrials.gov/study/NCT01239394) | Fase 2 | Completado | 43 | Tratamiento sistémico inicial de linfoma de células B indolente |
| [NCT00823719](https://clinicaltrials.gov/study/NCT00823719) | Fase 2 | Completado | 61 | Ofatumumab con quimioterapia ICE o DHAP en linfoma agresivo recaído/refractario (población mixta) |
| [NCT01077518](https://clinicaltrials.gov/study/NCT01077518) | Fase 3 | Terminado | 346 | Ofatumumab + bendamustina frente a bendamustina sola en linfoma indolente de células B refractario a rituximab |
| [NCT00742144](https://clinicaltrials.gov/study/NCT00742144) | Fase 1 | Completado | 6 | Seguridad y farmacocinética en pacientes japoneses con linfoma folicular o LLC |
| [NCT01119794](https://clinicaltrials.gov/study/NCT01119794) | Fase 2 | Terminado | 10 | Ofatumumab + bortezomib en linfoma no Hodgkin de bajo grado; valor limitado |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31174236](https://pubmed.ncbi.nlm.nih.gov/31174236/) | 2019 | ECA (Fase 2) | Cancer | Ofatumumab + bendamustina con o sin bortezomib en linfoma folicular de alto riesgo sin tratamiento previo (CALGB 50904) |
| [22389254](https://pubmed.ncbi.nlm.nih.gov/22389254/) | 2012 | Ensayo Fase 2 | Blood | Monoterapia con ofatumumab en linfoma folicular refractario a rituximab (N=116); tasa de respuesta global baja (alrededor de 10-13%) |
| [22409295](https://pubmed.ncbi.nlm.nih.gov/22409295/) | 2012 | Ensayo Fase 2 | Br J Haematol | Ofatumumab con CHOP (O-CHOP) como tratamiento de primera línea en linfoma folicular |
| [30723894](https://pubmed.ncbi.nlm.nih.gov/30723894/) | 2019 | Ensayo Fase 2 | Br J Haematol | Ofatumumab en monoterapia en linfoma folicular sin tratamiento previo (CALGB 50901) |
| [38937025](https://pubmed.ncbi.nlm.nih.gov/38937025/) | 2024 | Ensayo clínico | Lancet Haematol | Resultados finales de FIL MIRO: radioterapia local e inmunoterapia guiada por enfermedad residual medible en linfoma folicular temprano |
| [18390837](https://pubmed.ncbi.nlm.nih.gov/18390837/) | 2008 | Ensayo Fase 1/2 | Blood | Primer uso clínico de ofatumumab en linfoma folicular recaído o refractario |
| [26043777](https://pubmed.ncbi.nlm.nih.gov/26043777/) | 2015 | Revisión | Expert Opin Biol Ther | Ofatumumab en linfomas no Hodgkin |
| [29934061](https://pubmed.ncbi.nlm.nih.gov/29934061/) | 2018 | Revisión | Clin Lymphoma Myeloma Leuk | Revisión de regímenes con anticuerpos anti-CD20 en LLC, LDCBG y linfoma folicular recaídos o refractarios |
| [35663281](https://pubmed.ncbi.nlm.nih.gov/35663281/) | 2022 | Revisión | Leuk Res Rep | Inmunoterapia en linfomas no Hodgkin indolentes |
| [22830942](https://pubmed.ncbi.nlm.nih.gov/22830942/) | 2012 | Revisión | Ann N Y Acad Sci | Ofatumumab como primer anticuerpo anti-CD20 humano en neoplasias de células B |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20190663 | KESIMPTA | Solución inyectable | OFATUMUMAB (el registro no detalla la indicación) |

## Citotoxicidad

Ofatumumab es un anticuerpo monoclonal anti-CD20 usado en neoplasias de células B, por lo que se incluye esta sección.

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Inmunoterapia (anticuerpo monoclonal anti-CD20); no es un citotóxico convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma, función hepática y renal; vigilancia de infecciones |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas:** se registran 80 interacciones. Entre las de nivel **mayor** figuran deferiprona, samario (153Sm) lexidronam, adalimumab, baricitinib, certolizumab pegol, cladribina y clozapina. Entre las de nivel **moderado** figuran alemtuzumab, azatioprina, anakinra, canakinumab, cloranfenicol, zidovudina y varias vacunas (carbunco, cólera, toxoide tetánico). Predomina el riesgo de inmunosupresión y de mielosupresión aditiva, y conviene tener cuidado con las vacunas.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Varios ensayos de Fase 2 completados, incluidos aleatorizados, estudian directamente ofatumumab en linfoma folicular y la diana CD20 es biológicamente adecuada. Sin embargo, la respuesta en enfermedad refractaria a rituximab fue modesta, no hay dos ECA de Fase 3 completados y no consta un uso aprobado concreto en Colombia.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA con advertencias y contraindicaciones, y confirmar la indicación autorizada de KESIMPTA.
- Completar los datos del mecanismo de acción desde DrugBank.
- Comparar con rituximab y otros anti-CD20 ya establecidos en linfoma folicular.
- Definir un plan de monitoreo de seguridad (infecciones, citopenias, interacciones inmunosupresoras y vacunas).
- Evaluar la viabilidad de la vía de administración y la presentación frente al uso oncológico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

