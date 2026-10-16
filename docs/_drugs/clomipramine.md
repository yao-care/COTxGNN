---
layout: default
title: Clomipramine
parent: Evidencia Alta (L1-L2)
nav_order: 171
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Clomipramine: nueva indicación predicha, Trastorno de ansiedad (nivel de evidencia L1). Indicación original: CLOMIPRAMINA"
---

# Clomipramine
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **10** 
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

# Clomipramina: De Clomipramina (indicación no detallada en el registro) a Trastorno de Ansiedad

## Resumen en Una Frase

Clomipramina es un antidepresivo tricíclico con registro sanitario en Colombia (actualmente cancelado), cuyo texto de indicación aprobada solo menciona el nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para **trastorno de ansiedad**,
con **8 ensayos clínicos** (la mayoría en trastorno obsesivo-compulsivo) y **20 publicaciones** que respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | CLOMIPRAMINA (el registro no detalla una indicación específica) |
| Nueva Indicación Predicha | Trastorno de ansiedad |
| Puntaje de Predicción TxGNN | 99.93% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registro vigente) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, clomipramina es un inhibidor potente de la recaptación de serotonina, con actividad noradrenérgica a través de su metabolito activo, la desmetilclomipramina. Esta modulación serotoninérgica es la base de su eficacia en el trastorno obsesivo-compulsivo (TOC) y el trastorno de pánico.

La relación entre la indicación original y la nueva es estrecha: tanto la depresión como los trastornos de ansiedad comparten vías serotoninérgicas y noradrenérgicas. El TOC y el pánico se consideran dentro del espectro ansioso, y las guías de la WFSBP y los metaanálisis en red respaldan su uso, en especial en pánico y TOC.

Conviene señalar que el registro sanitario colombiano no especifica una indicación original más allá del nombre del fármaco, por lo que la comparación con la nueva indicación se basa en el uso clínico conocido de la clase y no en el texto del registro.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00004310](https://clinicaltrials.gov/study/NCT00004310) | Fase 2 | Desconocido | 76 | Clomipramina intravenosa vs oral en TOC, seguida de 12 semanas de mantenimiento |
| [NCT00564564](https://clinicaltrials.gov/study/NCT00564564) | Fase 4 | Completado | 21 | Aumento con quetiapina vs clomipramina sobre ISRS en TOC sin respuesta (ensayo abierto) |
| [NCT00074815](https://clinicaltrials.gov/study/NCT00074815) | Fase 3 | Completado | 124 | Terapia cognitivo-conductual como refuerzo de inhibidores de recaptación de serotonina en TOC pediátrico |
| [NCT00466609](https://clinicaltrials.gov/study/NCT00466609) | Fase 4 | Completado | 54 | Estrategias de aumento (fluoxetina, quetiapina o clomipramina) en TOC sin respuesta al tratamiento inicial |
| [NCT00254735](https://clinicaltrials.gov/study/NCT00254735) | Fase 3 | Completado | 44 | Quetiapina vs placebo añadida a ISRS/clomipramina en TOC grave |
| [NCT01404871](https://clinicaltrials.gov/study/NCT01404871) | N/A | Completado | 26 | Predicción de respuesta a clomipramina o escitalopram en TOC |
| [NCT05737511](https://clinicaltrials.gov/study/NCT05737511) | Fase 4 | Aún no reclutando | 80 | Hidroxizina vs tratamiento habitual en trastorno de pánico (clomipramina no es la intervención) |
| [NCT02374567](https://clinicaltrials.gov/study/NCT02374567) | Fase 3 | Terminado | 407 | Farmacovigilancia en pacientes gerontopsiquiátricos; sin datos de eficacia en ansiedad |

Solo dos ensayos evalúan directamente clomipramina (NCT00004310 y NCT00564564); en los demás el fármaco es tratamiento de base o comparador.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38014714](https://pubmed.ncbi.nlm.nih.gov/38014714/) | 2023 | Metaanálisis en red | Cochrane Database Syst Rev | Tratamientos farmacológicos del trastorno de pánico en adultos |
| [40788541](https://pubmed.ncbi.nlm.nih.gov/40788541/) | 2026 | Metaanálisis en red | Eur Arch Psychiatry Clin Neurosci | Eficacia y aceptabilidad comparativa de ansiolíticos en trastornos de ansiedad |
| [40946318](https://pubmed.ncbi.nlm.nih.gov/40946318/) | 2026 | Revisión sistemática | Psychother Psychosom | Opciones farmacológicas, psicoterapéuticas y de neuroestimulación en ansiedad resistente |
| [35900217](https://pubmed.ncbi.nlm.nih.gov/35900217/) | 2023 | Guía clínica | World J Biol Psychiatry | Guías WFSBP para ansiedad, TOC y TEPT (parte II: TOC y TEPT) |
| [41978943](https://pubmed.ncbi.nlm.nih.gov/41978943/) | 2026 | Revisión sistemática y metaanálisis | Acta Neuropsychiatrica | Clomipramina parenteral frente a oral en depresión o TOC |
| [27663940](https://pubmed.ncbi.nlm.nih.gov/27663940/) | 2016 | Revisión sistemática y metaanálisis | J Am Acad Child Adolesc Psychiatry | Respuesta temprana a ISRS y clomipramina en TOC pediátrico |
| [18849910](https://pubmed.ncbi.nlm.nih.gov/18849910/) | 2008 | Revisión | CNS Spectrums | Clomipramina eficaz en TOC pero con más eventos adversos que los ISRS |
| [2178909](https://pubmed.ncbi.nlm.nih.gov/2178909/) | 1990 | Revisión | Drugs | Propiedades farmacológicas y uso de clomipramina en TOC y pánico |
| [2021107](https://pubmed.ncbi.nlm.nih.gov/2021107/) | 1991 | Revisión | Am Fam Physician | Clomipramina en TOC; incidencia de convulsiones de 0.4% |
| [3887445](https://pubmed.ncbi.nlm.nih.gov/3887445/) | 1985 | Ensayo doble ciego | Psychiatry Res | Clomipramina vs imipramina en TOC (muestra pequeña) |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 227031 (cancelado) | ANAFRANIL® RETARD 75 MG TABLETAS RECUBIERTAS DE LIBERACIÓN PROLONGADA | Tableta de liberación prolongada | CLOMIPRAMINA |

## Consideraciones de Seguridad

- **Contraindicaciones sugeridas por el grafo de conocimiento** (relaciones fármaco-enfermedad del modelo, no texto del prospecto): epilepsia, trastorno bipolar en fase maníaca, enfermedad hepática, enfermedad de la vesícula biliar, abuso o dependencia de sustancias, hipertermia maligna, feocromocitoma, glaucoma, hipertiroidismo (incluida la enfermedad de Graves y la tirotoxicosis), neuroblastoma y varios cánceres (duodeno, intestino delgado, corazón, glándula suprarrenal) y paraganglioma simpático.
- **Interacciones farmacológicas:** se identificaron 318 interacciones. Entre las de nivel mayor figuran epinefrina, bupropión, lorcaserina, citrato de potasio y cisaprida. Entre las moderadas, famotidina, cimetidina, claritromicina, morfina, ácido acetilsalicílico y varios anticolinérgicos (atropina, hiosciamina, glicopirronio).
- **Riesgos adicionales descritos en la literatura:** efectos anticolinérgicos y cardíacos, reducción del umbral convulsivo, riesgo de síndrome serotoninérgico, interacciones por CYP2D6/CYP1A2, cautela en adultos mayores, y un reporte de caso de pancitopenia.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La evidencia es sólida en TOC y trastorno de pánico (metaanálisis en red, guías y ensayos), lo que respalda la predicción para trastornos de ansiedad en sentido amplio. Sin embargo, el único registro sanitario colombiano está cancelado y el perfil de seguridad exige precauciones.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), ya que hoy no hay datos de etiqueta.
- Confirmar el mecanismo de acción en DrugBank.
- Definir la subindicación de ansiedad objetivo (TOC, pánico, agorafobia) y comparar con los ISRS, mejor tolerados.
- Evaluar la vía regulatoria, dado que no hay registro vigente en Colombia.
- Establecer un plan de monitoreo de seguridad (ECG, riesgo convulsivo, interacciones, farmacogenética de CYP2D6) y restricciones en adultos mayores y niños.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

