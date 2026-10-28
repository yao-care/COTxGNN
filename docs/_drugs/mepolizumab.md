---
layout: default
title: Mepolizumab
parent: Solo Predicción del Modelo (L5)
nav_order: 429
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
description: "Mepolizumab: nueva indicación predicha, Trombocitopenia por destrucción inmune (nivel de evidencia L4). Indicación original: No especificada en el registro sanitario (el texto solo indica \"Mepol…"
monitor_inn: "MEPOLIZUMAB"
predicted_indications: ["thrombocytopenia due to immune destruction", "primary release disorder of platelets", "pseudo-von Willebrand disease", "autoimmune thrombocytopenic", "Glanzmann thrombasthenia"]
---

# Mepolizumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Mepolizumab: De Indicación Original (no especificada en el registro) a Trombocitopenia por Destrucción Inmune
{: .text-alpha }

## Resumen en Una Frase

Mepolizumab es un anticuerpo monoclonal anti-IL-5 comercializado en Colombia como Nucala®; el registro sanitario disponible no detalla la indicación aprobada (solo repite el nombre del principio activo).
El modelo TxGNN predice que podría ser efectivo para **trombocitopenia por destrucción inmune**, pero no hay ensayos clínicos registrados y solo existe **1 publicación** (un reporte de caso) con relación indirecta.
La predicción es, por ahora, una señal computacional con evidencia muy limitada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro sanitario (el texto solo indica "Mepolizumab") |
| Nueva Indicación Predicha | Trombocitopenia por destrucción inmune |
| Puntaje de Predicción TxGNN | 0.9966 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Mepolizumab es un anticuerpo monoclonal dirigido contra la interleucina-5 (IL-5), una citocina clave para la maduración y supervivencia de los eosinófilos, por lo que reduce su número. Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción, por lo que esta descripción se basa en el conocimiento general del fármaco.

La única publicación vinculada describe un caso de diátesis inmune hipereosinofílica resistente a esteroides que se resolvió con mepolizumab, junto con una mejoría de una microangiopatía trombótica mixta. Esto sugiere que, cuando una citopenia inmunomediada es impulsada por una desregulación eosinofílica, el bloqueo de IL-5 podría ayudar.

Sin embargo, esta es evidencia indirecta. En la trombocitopenia inmune primaria los eosinófilos no son un factor causal establecido, y el puntaje alto de TxGNN (0.9966) es únicamente una predicción computacional. La plausibilidad mecanística es limitada y especulativa.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [28648630](https://pubmed.ncbi.nlm.nih.gov/28648630/) | 2018 | Reporte de caso | Blood Cells, Molecules & Diseases | Un síndrome inmune hipereosinofílico resistente a esteroides se resolvió con mepolizumab, con mejoría concomitante de una microangiopatía trombótica mixta. No es evidencia directa en trombocitopenia inmune primaria. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20188045 (cancelado) | NUCALA® 100MG/ML SOLUCIÓN INYECTABLE (GlaxoSmithKline Colombia S.A.) | Solución inyectable | Mepolizumab (sin detalle de indicación) |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas en la consulta realizada.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en un puntaje computacional y un reporte de caso con relación indirecta; no hay ensayos clínicos. Además, el único registro sanitario en Colombia está cancelado y no se dispone de información de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto del INVIMA (advertencias y contraindicaciones), requisito previo para cualquier evaluación de seguridad
- Confirmar la indicación aprobada y el mecanismo de acción detallado desde fuentes como DrugBank
- Buscar evidencia clínica directa en trombocitopenia inmune, o identificar subgrupos con componente eosinofílico donde el bloqueo de IL-5 tenga sentido
- Aclarar la situación regulatoria y la disponibilidad del producto en Colombia, dado que el registro está cancelado
- Evaluar la compatibilidad de vía de administración y la relación con la indicación original, hoy pendientes
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

