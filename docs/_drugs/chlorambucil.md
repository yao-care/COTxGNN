---
layout: default
title: Chlorambucil
parent: Solo Predicción del Modelo (L5)
nav_order: 150
evidence_level: L5
indication_count: 5
monitor_inn: "chlorambucil"
predicted_indications: ["ALK-positive large B-cell lymphoma", "primary pulmonary lymphoma", "well-differentiated fetal adenocarcinoma of the lung", "pulmonary blastoma", "small cell lung carcinoma"]
last_modified_at: 2026-11-24
description: "Chlorambucil: nueva indicación predicha, ALK-positive large B-cell lymphoma (nivel de evidencia L5). Indicación original: CLORAMBUCIL"
---

# Chlorambucil
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

## Chlorambucil: ALK-positive large B-cell lymphoma
{: .text-alpha }

## Resumen en Una Frase

Clorambucilo es un agente alquilante del ADN (mostaza nitrogenada) con uso histórico en neoplasias hematológicas.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | CLORAMBUCIL |
| Nueva Indicación Predicha | ALK-positive large B-cell lymphoma |
| Puntaje de Predicción TxGNN | 0.9961 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Chlorambucil (traducción no oficial): «El clorambucilo, un derivado aromático de la mostaza nitrogenada, es un agente alquilante. El clorambucilo interfiere en la replicación del ADN e induce la apoptosis celular mediante la acumulación de p53 citosólica y la posterior activación de Bax, un promotor de la apoptosis.» Texto original en inglés: "Chlorambucil, an aromatic nitrogen mustard derivative, is an alkylating agent. Chlorambucil interferes with DNA replication and induces cellular apoptosis via the accumulation of cytosolic p53 and subsequent activation of Bax, an apoptosis promoter." ([DailyMed: Leukeran (chlorambucil) prescribing information, Waylis Therapeutics LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=58a3c995-5ad6-465d-8437-5970c9088213), versión del 2025-01-08; consultado el 2026-11-19). Según la información conocida, el clorambucilo es una mostaza nitrogenada que alquila el ADN e impide la replicación de células en proliferación, lo que lo hace activo en neoplasias linfoides.

Este subtipo (CLL/SLL con genes IGHV sin mutar, de origen pregerminal) forma parte de la categoría más amplia de la leucemia linfocítica crónica. Por proximidad biológica, la actividad del fármaco es plausible por extensión. El puntaje elevado probablemente refleja esa cercanía entre enfermedades.

Conviene ser prudente: la única publicación disponible es una revisión de 2003 sobre un enfoque adaptado al riesgo en la LLC, sin datos de clorambucilo específicos para este subtipo. Además, los estándares actuales (inhibidores de BTK y BCL2) han desplazado al clorambucilo, en particular en la enfermedad con IGHV sin mutar. Por ello se asigna el nivel L5: ningún estudio citado evalúa directamente este subtipo con el fármaco.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [12577769](https://pubmed.ncbi.nlm.nih.gov/12577769/) | 2003 | Revisión | Nederlands tijdschrift voor geneeskunde | Describe dos subtipos de LLC (pregerminal y poscentro germinal) según mutación de los genes de la región variable de inmunoglobulinas, y plantea un abordaje adaptado al riesgo; no aporta datos de clorambucilo específicos del subtipo |

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 46264 | LEUKERAN TABLETAS RECUBIERTAS 2 MG | TABLETA RECUBIERTA | CLORAMBUCIL | Vigente |

Se muestra el único registro sanitario de este principio activo en los datos del INVIMA, Código Único de Medicamentos.

<!-- licenses:end -->

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
Además, los tratamientos modernos han desplazado al fármaco en la enfermedad con IGHV sin mutar, por lo que el interés es sobre todo de investigación.

**Para avanzar se necesita:**
- Datos de eficacia del clorambucilo específicos para CLL/SLL con IGHV sin mutar, comparados con los estándares actuales
- Datos del mecanismo de acción detallados
- Advertencias y contraindicaciones del prospecto aprobado en Colombia
- Plan de monitoreo hematológico y de seguridad, incluido el riesgo de segundas neoplasias

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Leukeran (chlorambucil) prescribing information, Waylis Therapeutics LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=58a3c995-5ad6-465d-8437-5970c9088213) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

