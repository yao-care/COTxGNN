---
layout: default
title: Temozolomide
parent: Solo Predicción del Modelo (L5)
nav_order: 610
evidence_level: L5
indication_count: 1
monitor_inn: "Temozolomide"
predicted_indications: ["cauda equina neoplasm"]
last_modified_at: 2026-10-31
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
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 3) |
| Número de Registros Sanitarios | al menos 4 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según el conocimiento general del fármaco, la temozolomida es un agente alquilante oral que metila el ADN (posiciones O6-guanina, N7-guanina y N3-adenina), lo que causa daño citotóxico y apoptosis en células tumorales en división. Esta descripción proviene de conocimiento general y no de los datos compilados.

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

La lista puede ser parcial.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20001038 | TEMODAL® CÁPSULAS 140 MG | Cápsula dura | TEMOZOLOMIDA |
| 19907390 | TEMODAL® CÁPSULAS 20 MG | Cápsula dura | TEMOZOLOMIDA |
| 20087083 | TEMITOMA 20 MG | Cápsula dura | TEMOZOLOMIDA |
| 20196779 | MOZOLA® 20 MG CÁPSULA | Cápsula dura | TEMOZOLOMIDA |

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
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

