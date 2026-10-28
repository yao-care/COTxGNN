---
layout: default
title: Famotidine
parent: Solo Predicción del Modelo (L5)
nav_order: 277
evidence_level: L5
indication_count: 4
monitor_inn: "Famotidine"
predicted_indications: ["duodenal obstruction", "abnormality of glucagon secretion", "multiple endocrine neoplasia", "acne (disease)"]
last_modified_at: 2026-10-28
description: "Famotidine: nueva indicación predicha, obstrucción duodenal (duodenal obstruction) (nivel de evidencia L5). Indicación original: FAMOTIDINA"
---

# Famotidine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

## Famotidina: antagonista de los receptores H2 de histamina → obstrucción duodenal (duodenal obstruction)
{: .text-alpha }

## Resumen en Una Frase

Famotidina es un antagonista de los receptores H2 de histamina, utilizado para reducir la secreción de ácido gástrico.
El modelo TxGNN predice que podría ser útil para **obstrucción duodenal (duodenal obstruction)**, pero actualmente **no hay ensayos clínicos** y solo hay **2 publicaciones** (dos reportes de caso) que no demuestran eficacia de la famotidina en esta condición.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | FAMOTIDINA |
| Nueva Indicación Predicha | obstrucción duodenal (duodenal obstruction) |
| Puntaje de Predicción TxGNN | 0,9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 2) |
| Número de Registros Sanitarios | al menos 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Famotidina actúa bloqueando el receptor H2 de histamina (gen HRH2), con lo que disminuye la producción de ácido gástrico. Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción; la información farmacológica disponible confirma el receptor H2 como diana y su uso en úlceras gástricas y duodenales, reflujo gastroesofágico y estados de hipersecreción ácida.

Sin embargo, no se identifica un vínculo mecanístico plausible con la obstrucción duodenal. Esta es un problema mecánico o estructural que se trata con cirugía o endoscopia; la supresión ácida, como mucho, sería un complemento. Las dos publicaciones recuperadas (una sobre úlcera marginal gigante y otra sobre cirugía por compromiso duodenal en enfermedad de Crohn) no constituyen evidencia de eficacia de la famotidina.

El puntaje alto del modelo parece reflejar la cercanía en la red con la enfermedad ulcerosa más que evidencia clínica. Por ello, esta predicción debe considerarse solo una hipótesis del modelo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [8165479](https://pubmed.ncbi.nlm.nih.gov/8165479/) | 1994 | Reporte de caso | Surgical Endoscopy | Úlcera marginal gigante como complicación de la gastroenterostomía; no evalúa famotidina |
| [9306611](https://pubmed.ncbi.nlm.nih.gov/9306611/) | 1997 | Reporte de caso | Surgery Today | Tratamiento quirúrgico de compromiso duodenal por enfermedad de Crohn con obstrucción de salida gástrica; no evalúa famotidina |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19959810 | GASTRUM® 10 MG TABLETA | Tableta | Famotidina |
| 20249954 | PEPTOFAN® 40 MG | Tableta recubierta | Famotidina |

La lista de registros puede ser parcial.

## Consideraciones de Seguridad

- **Interacciones farmacológicas / farmacología**: los datos registran la unión de famotidina al receptor H2 (HRH2) y al receptor del gusto amargo TAS2R31; no se dispone de interacciones con otros fármacos clasificadas por nivel de gravedad.

Para información sobre advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos ni estudios que evalúen la famotidina en obstrucción duodenal, y no se identifica un vínculo mecanístico plausible; el puntaje del modelo (0,9999) no está respaldado por evidencia clínica.

**Para avanzar se necesita:**
- Evidencia clínica o preclínica que estudie directamente la famotidina en obstrucción duodenal
- Una justificación mecanística que vaya más allá de la supresión ácida
- Datos de seguridad del prospecto (advertencias y contraindicaciones) de los registros de INVIMA
- Datos detallados del mecanismo de acción
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

