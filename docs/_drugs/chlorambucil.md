---
layout: default
title: Chlorambucil
parent: Solo Predicción del Modelo (L5)
nav_order: 150
evidence_level: L5
indication_count: 7
monitor_inn: "chlorambucil"
predicted_indications: ["pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma", "chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation", "ALK-positive large B-cell lymphoma", "primary pulmonary lymphoma", "well-differentiated fetal adenocarcinoma of the lung", "pulmonary blastoma", "small cell lung carcinoma"]
last_modified_at: 2026-10-28
description: "Chlorambucil: nueva indicación predicha, Leucemia linfocítica crónica/linfoma linfocítico de células pequeñas pregerminal (pregerminal center chronic lymphocyti… (nivel de evidencia L5). Indicación o…"
---

# Chlorambucil
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

## Clorambucilo: agente alquilante tipo mostaza nitrogenada → leucemia linfocítica crónica/linfoma linfocítico de células pequeñas pregerminal (pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma)
{: .text-alpha }

## Resumen en Una Frase

Clorambucilo es un agente alquilante del ADN (mostaza nitrogenada) con uso histórico en neoplasias hematológicas.
El modelo TxGNN predice que podría ser efectivo para la **leucemia linfocítica crónica/linfoma linfocítico de células pequeñas pregerminal (pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma)**,
pero **no hay ensayos clínicos** y solo **1 publicación** (una revisión de 2003 sin datos específicos del fármaco para este subtipo) respalda esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | CLORAMBUCIL |
| Nueva Indicación Predicha | Leucemia linfocítica crónica/linfoma linfocítico de células pequeñas pregerminal (pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma) |
| Puntaje de Predicción TxGNN | 0,9972 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

No se dispone actualmente de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, el clorambucilo es una mostaza nitrogenada que alquila el ADN e impide la replicación de células en proliferación, lo que lo hace activo en neoplasias linfoides.

Este subtipo (CLL/SLL con genes IGHV sin mutar, de origen pregerminal) forma parte de la categoría más amplia de la leucemia linfocítica crónica. Por proximidad biológica, la actividad del fármaco es plausible por extensión. El puntaje elevado probablemente refleja esa cercanía entre enfermedades.

Conviene ser prudente: la única publicación disponible es una revisión de 2003 sobre un enfoque adaptado al riesgo en la LLC, sin datos de clorambucilo específicos para este subtipo. Además, los estándares actuales (inhibidores de BTK y BCL2) han desplazado al clorambucilo, en particular en la enfermedad con IGHV sin mutar. Por ello se asigna el nivel L5: ningún estudio citado evalúa directamente este subtipo con el fármaco.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [12577769](https://pubmed.ncbi.nlm.nih.gov/12577769/) | 2003 | Revisión | Nederlands tijdschrift voor geneeskunde | Describe dos subtipos de LLC (pregerminal y poscentro germinal) según mutación de los genes de la región variable de inmunoglobulinas, y plantea un abordaje adaptado al riesgo; no aporta datos de clorambucilo específicos del subtipo |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 46264 | LEUKERAN TABLETAS RECUBIERTAS 2 MG | Tableta recubierta | CLORAMBUCIL |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (agente alquilante, mostaza nitrogenada) |
| Riesgo de Mielosupresión | Alto (las relaciones de contraindicación registradas incluyen neutropenia, trombocitopenia, leucopenia y anemia) |
| Clasificación de Emetogenicidad | Baja a moderada |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se registran 167 interacciones. Entre las principales:
  - Gravedad mayor: deferiprona, samario (153Sm) lexidronam.
  - Gravedad moderada: anfotericina B (y sus formulaciones lipídicas y liposomal), palifermina, cloruro de estroncio Sr-89, mercaptopurina, roflumilast, cloranfenicol.
  - Gravedad menor: levofloxacino.
- **Condiciones asociadas a contraindicación en los datos del modelo (no provienen del prospecto)**: mielosupresión (neutropenia, trombocitopenia, leucopenia, anemia, linfopenia), enfermedad pulmonar intersticial y fibrosis pulmonar, daño hepático inducido por fármacos, síndrome nefrótico, epilepsia y leucemias agudas.

Consultar el prospecto para las advertencias y contraindicaciones oficiales.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto (0,9972), pero no hay ensayos ni estudios que evalúen el clorambucilo en este subtipo. Además, los tratamientos modernos han desplazado al fármaco en la enfermedad con IGHV sin mutar, por lo que el interés es sobre todo de investigación.

**Para avanzar se necesita:**
- Datos de eficacia del clorambucilo específicos para CLL/SLL con IGHV sin mutar, comparados con los estándares actuales
- Datos del mecanismo de acción detallados
- Advertencias y contraindicaciones del prospecto aprobado en Colombia
- Plan de monitoreo hematológico y de seguridad, incluido el riesgo de segundas neoplasias
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

