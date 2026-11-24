---
layout: default
title: Temozolomide
parent: Solo Predicción del Modelo (L5)
nav_order: 610
evidence_level: L5
indication_count: 1
monitor_inn: "Temozolomide"
predicted_indications: ["cauda equina neoplasm"]
last_modified_at: 2026-11-24
description: "Temozolomide: nueva indicación predicha, Neoplasia de la cauda equina (nivel de evidencia L5). Indicación original: No especificada en el registro (el texto indica únicamente \"TEMOZOLOM…"
---

# Temozolomide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Temozolomida: De TEMOZOLOMIDA (indicación sin detalle en el registro) a Neoplasia de la cauda equina
{: .text-alpha }

## Resumen en Una Frase

Temozolomida es un agente alquilante oral con registros sanitarios vigentes en Colombia; el texto de indicación de esos registros solo repite el nombre del principio activo, sin detallar el uso aprobado.
El modelo TxGNN predice que podría ser efectivo para **neoplasia de la cauda equina**, pero no hay ensayos clínicos registrados y solo se dispone de **3 publicaciones** (reportes de caso), de las cuales solo una trata directamente un tumor de esta región.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto indica únicamente "TEMOZOLOMIDA") |
| Nueva Indicación Predicha | Neoplasia de la cauda equina |
| Puntaje de Predicción TxGNN | 0,9930 |
| Nivel de Evidencia | L5 (un reporte de caso sobre ependimoma mixopapilar espinal, tumor típico de la cauda equina) |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 14 de 16) |
| Número de Registros Sanitarios | 16 (vigentes: 14) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Temozolomide (traducción no oficial): «La temozolomida no es directamente activa, sino que experimenta una rápida conversión no enzimática a pH fisiológico en el compuesto reactivo 5-(3-metiltriazen-1-il)-imidazol-4-carboxamida (MTIC). Se cree que la citotoxicidad del MTIC se debe principalmente a la alquilación del ADN, sobre todo en las posiciones O 6 y N 7 de la guanina, lo que provoca roturas de doble cadena del ADN y da lugar a muerte celular programada.» Texto original en inglés: "Temozolomide is not directly active but undergoes rapid nonenzymatic conversion at physiologic pH to the reactive compound 5-(3-methyltriazen-1-yl)-imidazole-4-carboxamide (MTIC). The cytotoxicity of MTIC is thought to be primarily due to DNA alkylation, mainly at the O 6 and N 7 positions of guanine, which causes DNA double strand breaks and results in programmed cell death." ([DailyMed: Temodar (temozolomide) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=046a9011-3911-4d3f-a15f-fbb56d5aad56), versión del 2026-02-20; consultado el 2026-11-19). Según el conocimiento general del fármaco, la temozolomida es un agente alquilante oral que metila el ADN (posiciones O6-guanina, N7-guanina y N3-adenina), lo que causa daño citotóxico y apoptosis en células tumorales en división. Esta descripción proviene de conocimiento general y no de los datos compilados.

Las neoplasias de la cauda equina son, con mayor frecuencia, ependimomas mixopapilares, tumores del sistema nervioso central de linaje glial. Esto establece un vínculo plausible con el uso conocido de la temozolomida en gliomas. La sensibilidad probablemente depende del estado de metilación del promotor de MGMT (baja expresión favorece la respuesta), dato que no está disponible aquí.

El puntaje de 0,993 es una predicción computacional y no constituye evidencia clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [29270703](https://pubmed.ncbi.nlm.nih.gov/29270703/) | 2018 | Reporte de caso | European Spine Journal | Eficacia notable de temozolomida en un ependimoma mixopapilar espinal recidivante, con recurrencias múltiples y diseminación por líquido cefalorraquídeo; incluye revisión de literatura |
| [42760727](https://pubmed.ncbi.nlm.nih.gov/42760727/) | 2026 | Reporte de caso | Medicine | Carcinoma NUT nasal con respuestas repetidas a tratamiento multimodal con radioterapia; no estudia directamente la neoplasia de la cauda equina |
| [18706663](https://pubmed.ncbi.nlm.nih.gov/18706663/) | 2009 | Reporte de caso | Neuro-Chirurgie | Criptococosis neuromeníngea atípica en un niño inmunocomprometido tratado por glioma pontino; no evalúa eficacia en esta indicación |

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 19907388 | TEMODAL® CAPSULAS 100 MG | CAPSULA DURA | TEMOZOLOMIDA | Vigente |
| 19907390 | TEMODAL®CAPSULAS 20 MG | CAPSULA DURA | TEMOZOLOMIDA | Vigente |
| 20061379 | DRALITEM ® 250 MG | CAPSULA DURA | TEMOZOLOMIDA | Vigente |
| 20061382 | DRALITEM ® 100MG CÁPSULAS | CAPSULA DURA | TEMOZOLOMIDA | Vigente |
| 20061383 | DRALITEM ® 20 MG | CAPSULA DURA | TEMOZOLOMIDA | Vigente |

Se muestran 5 de 16 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

<!-- review:begin co-lic-20261124b-temozolomide-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "La lista puede ser parcial." Eliminado: advertía que la lista de registros podría ser parcial. La tabla de Información de Mercado en Colombia se genera a partir de los datos del INVIMA (Código Único de Medicamentos, datos al 2026-11-23) e indica cuántos registros muestra del total. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261124b-temozolomide-1 -->

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (agente alquilante) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto. Las relaciones registradas en el grafo de conocimiento (trombocitopenia, neutropenia, pancitopenia, anemia aplásica) apuntan a toxicidad hematológica |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma completo con diferencial, función hepática y renal |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

## Consideraciones de Seguridad

- **Relaciones de contraindicación registradas en el grafo de conocimiento** (no provienen del texto del prospecto): insuficiencia hepática, trombocitopenia, neutropenia, agranulocitosis, anemia, anemia macrocítica, neumocistosis, pancitopenia, linfopenia, síndrome mielodisplásico, anemia aplásica idiopática y anemia aplásica.
- **Interacciones farmacológicas**: se identificaron 100 interacciones en total (se muestran las principales). De nivel moderado: naltrexona. De nivel menor: levofloxacino. Con nivel no clasificado, entre otras: pantoprazol, omeprazol, lansoprazol, morfina, metformina, prednisona, hidrocortisona y anfotericina B.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia directa es un único reporte de caso sobre un ependimoma mixopapilar espinal, sin ensayos clínicos. El puntaje alto de TxGNN es solo una predicción computacional. Además, el texto del registro sanitario no detalla la indicación aprobada y faltan los datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), que es un vacío bloqueante para el tamizaje de seguridad.
- Confirmar la indicación aprobada en los registros sanitarios.
- Completar los datos del mecanismo de acción desde DrugBank.
- Revisar sistemáticamente la literatura sobre ependimomas mixopapilares y neoplasias de la cauda equina tratados con temozolomida.
- Evaluar el estado de metilación de MGMT como posible biomarcador de respuesta.
- Definir un plan de monitoreo hematológico y hepático.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Temodar (temozolomide) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=046a9011-3911-4d3f-a15f-fbb56d5aad56) |
| 2026-11-24 | Eliminado: "La lista puede ser parcial." | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

