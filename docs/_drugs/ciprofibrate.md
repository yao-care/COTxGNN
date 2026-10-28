---
layout: default
title: Ciprofibrate
parent: Solo Predicción del Modelo (L5)
nav_order: 158
evidence_level: L5
indication_count: 2
monitor_inn: "Ciprofibrate"
predicted_indications: ["cholesterol-ester transfer protein deficiency", "fibroma of prostate"]
last_modified_at: 2026-10-23
description: "Ciprofibrate: nueva indicación predicha, Deficiencia de la proteína de transferencia de ésteres de colesterol (nivel de evidencia L5). Indicación original: Ciprofibrato"
---

# Ciprofibrate
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Ciprofibrato: De Dislipidemia a Deficiencia de la Proteína de Transferencia de Ésteres de Colesterol
{: .text-alpha }

## Resumen en Una Frase

Ciprofibrato es un fibrato utilizado para tratar la dislipidemia (hipertrigliceridemia severa o hiperlipidemia mixta), y en Colombia cuenta con registros sanitarios vigentes para productos de un solo principio activo.
El modelo TxGNN predice que podría ser efectivo para la **deficiencia de la proteína de transferencia de ésteres de colesterol (CETP)**, pero sin ensayos clínicos y con **1 publicación** preclínica indirecta que no estudia directamente esta enfermedad.
La evidencia actual corresponde, en la práctica, solo a una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Ciprofibrato (el texto del registro sanitario no detalla la indicación; según la información farmacológica compilada, se usa en dislipidemia) |
| Nueva Indicación Predicha | Deficiencia de la proteína de transferencia de ésteres de colesterol |
| Puntaje de Predicción TxGNN | 0.9991 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 4) |
| Número de Registros Sanitarios | Al menos 4 (la lista puede ser parcial) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción dentro de los datos compilados para este informe. Según la información farmacológica conocida, ciprofibrato es un agonista del receptor activado por proliferadores de peroxisomas alfa (PPAR-alfa), que reduce los triglicéridos y modula el metabolismo de las lipoproteínas, incluido el HDL.

La deficiencia de CETP se caracteriza por HDL-colesterol marcadamente elevado y un transporte inverso de colesterol alterado. Existe una conexión mecanística plausible, porque los fibratos influyen en las vías del metabolismo lipoproteico (por ejemplo, la señalización relacionada con apoA-I y SR-BI).

Sin embargo, la lógica terapéutica es poco clara: un fibrato no corregiría un defecto genético de CETP, y esta condición se presenta principalmente con HDL alto, no con necesidad de reducir lípidos. El puntaje de 0.9991 es solo una predicción computacional y no demuestra beneficio clínico.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [14570884](https://pubmed.ncbi.nlm.nih.gov/14570884/) | 2003 | Preclínico (modelo animal, transferencia génica) | The Journal of Biological Chemistry | En ratones deficientes en apolipoproteína E, el tratamiento con ciprofibrato agrava la hipercolesterolemia; la sobreexpresión de SR-BI mediante vector adenoviral revierte este efecto. Es evidencia indirecta y no estudia la deficiencia de CETP. |

## Información de Mercado en Colombia

La lista puede ser parcial: se muestran los 4 registros identificados.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19986691 | CIPROFIBRATO 100 MG TABLETAS (Laboratorios La Santé S.A.) | Tableta | CIPROFIBRATO |
| 20028347 | CIPROFIBRATO TABLETAS X 100 MG (Genfar S.A.) | Tableta | CIPROFIBRATO |
| 20013191 | FIBROLIP® 100 MG TABLETAS (Megalabs Colombia S.A.S) | Tableta | CIPROFIBRATO |
| 20010476 | GIABRI® 100 MG TABLETAS (Merck S.A.) | Tableta | CIPROFIBRATO |

## Consideraciones de Seguridad

**Interacciones Farmacológicas**: La consulta se completó y registró una relación farmacológica, no una interacción medicamentosa clínica: ciprofibrato actúa sobre su diana, el receptor PPAR-alfa (gen PPARA). No se registraron niveles de gravedad.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni estudios que evalúen directamente la deficiencia de CETP; la única publicación es un estudio preclínico indirecto en otro modelo. Además, el racional terapéutico es débil, porque esta condición cursa con HDL elevado. Por ello el nivel de evidencia es L5.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) y un análisis mecanístico que justifique el beneficio en la deficiencia de CETP
- Advertencias y contraindicaciones del prospecto del INVIMA para completar el análisis de seguridad
- Estudios preclínicos o clínicos que evalúen directamente ciprofibrato en esta enfermedad
- Definir primero si existe una necesidad clínica real, dado que la condición se caracteriza por HDL alto

*Nota: la segunda predicción, fibroma de próstata (puntaje 0.9971), no tiene ensayos, literatura ni vínculo mecanístico identificado (nivel L5, Hold), por lo que no se desarrolla en este informe.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

