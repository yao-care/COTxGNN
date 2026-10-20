---
layout: default
title: Duloxetine
parent: Solo Predicción del Modelo (L5)
nav_order: 240
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Duloxetine: nueva indicación predicha, Tortícolis paroxístico benigno de la infancia (nivel de evidencia L5). Indicación original: DULOXETINA"
monitor_inn: "duloxetine"
predicted_indications: ["benign paroxysmal torticollis of infancy", "agoraphobia", "obsessive-compulsive disorder", "schizotypal personality disorder", "histrionic personality disorder (disease)", "schizoid personality disorder", "paranoid personality disorder", "Ohdo syndrome and variants", "ligneous conjunctivitis", "blepharophimosis - intellectual disability syndrome, Ohdo type"]
---

# Duloxetine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Duloxetina: De Duloxetina (indicación sin detallar) a Trastorno Paroxístico Benigno de Tortícolis de la Infancia

## Resumen en Una Frase

La duloxetina es un inhibidor de la recaptación de serotonina y noradrenalina (IRSN), cuyos registros sanitarios en Colombia solo mencionan "duloxetina" como indicación, sin detallar la enfermedad aprobada.
El modelo TxGNN predice como primera opción el **tortícolis paroxístico benigno de la infancia**, pero **sin ensayos clínicos ni publicaciones** que respalden esta predicción.
Entre las predicciones evaluadas, la mejor respaldada es el **trastorno obsesivo-compulsivo (TOC)**, con **3 ensayos clínicos** y **19 publicaciones**.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | DULOXETINA (el registro no detalla la enfermedad aprobada) |
| Nueva Indicación Predicha | Tortícolis paroxístico benigno de la infancia |
| Puntaje de Predicción TxGNN | 99.85% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este reporte. Según la información conocida, la duloxetina es un IRSN: aumenta la disponibilidad de serotonina y noradrenalina en el sistema nervioso central.

Para la primera predicción (tortícolis paroxístico benigno de la infancia) **no hay respaldo clínico ni bibliográfico**. Se trata de un trastorno pediátrico relacionado con la migraña, a menudo vinculado al gen CACNA1A, y la plausibilidad de la inhibición de recaptación de serotonina-noradrenalina es débil. Además, la duloxetina no está establecida para uso en lactantes. El puntaje elevado refleja únicamente una predicción basada en grafos de conocimiento.

Como referencia, entre las 10 predicciones principales, la que tiene mayor respaldo es el **TOC** (puesto 3; puntaje 99.84%). La inhibición de la recaptación de serotonina es el mecanismo central de los tratamientos eficaces del TOC. La **agorafobia** (puesto 2) tiene respaldo indirecto a través del trastorno de pánico. Las demás predicciones (trastornos de personalidad, síndrome de Ohdo, conjuntivitis leñosa) carecen de evidencia y de vínculo mecanístico plausible.

---

## Evidencia de Ensayos Clínicos

Para la predicción principal:

Actualmente no hay ensayos clínicos relacionados registrados.

**Referencia: TOC (predicción alternativa con mayor evidencia)**

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00464698](https://clinicaltrials.gov/study/NCT00464698) | Fase 4 | Completado | 20 | Eficacia de duloxetina en TOC; directamente relevante, pero pequeño y probablemente abierto |
| [NCT01404871](https://clinicaltrials.gov/study/NCT01404871) | N/A | Completado | 26 | Predicción de respuesta a medicamentos en TOC (clomipramina o escitalopram; duloxetina para quienes ya los habían probado) |
| [NCT02476136](https://clinicaltrials.gov/study/NCT02476136) | N/A | Desconocido | 8800 | Metaanálisis de datos individuales sobre gravedad inicial y eficacia de antidepresivos en trastornos de ansiedad; evidencia indirecta |

---

## Evidencia de Literatura

Para la predicción principal:

Actualmente no hay literatura relacionada disponible.

**Referencia: TOC (principales publicaciones)**

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [27811556](https://pubmed.ncbi.nlm.nih.gov/27811556/) | 2016 | ECA | J Clin Psychopharmacol | Ensayo doble ciego controlado de potenciación con duloxetina en TOC resistente |
| [25637377](https://pubmed.ncbi.nlm.nih.gov/25637377/) | 2015 | Estudio abierto | Int J Neuropsychopharmacol | Eficacia de duloxetina en TOC |
| [31749717](https://pubmed.ncbi.nlm.nih.gov/31749717/) | 2019 | Revisión sistemática | Front Psychiatry | Uso de duloxetina en trastornos psiquiátricos más allá de depresión y ansiedad generalizada |
| [16669725](https://pubmed.ncbi.nlm.nih.gov/16669725/) | 2006 | Revisión | J Clin Psychiatry | Revisión crítica de IRSN en TOC |
| [28477500](https://pubmed.ncbi.nlm.nih.gov/28477500/) | 2017 | Metaanálisis | J Affect Disord | Menor respuesta a placebo y antidepresivos en TOC frente a otros trastornos de ansiedad |
| [18208931](https://pubmed.ncbi.nlm.nih.gov/18208931/) | 2008 | Serie de casos | J Psychopharmacol | Cambio de inhibidores de recaptación de serotonina a duloxetina en TOC resistente |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20112029 (cancelado) | DUXETERO® 60 MG CÁPSULAS DE LIBERACIÓN RETARDADA | Cápsula dura | Duloxetina |
| 20015009 (cancelado) | ALACIR® 60 | Tableta de liberación retardada | Duloxetina |

---

## Consideraciones de Seguridad

- **Contraindicaciones y condiciones de riesgo (según el grafo de conocimiento, no el prospecto):** hipertensión, hipotensión ortostática, atrofia multisistémica, síndrome de taquicardia postural ortostática, epilepsia, trastorno bipolar y trastornos afectivos mayores, enfermedad hepática (cirrosis, hígado graso, hepatitis), enfermedad de la vesícula biliar, hiperglucemia, abuso/dependencia de sustancias, trastornos de la coagulación, glaucoma de ángulo cerrado, síndrome neuroléptico maligno, síndrome de secreción inadecuada de ADH (incluida la forma nefrogénica) y síndrome serotoninérgico.
- **Interacciones farmacológicas:** se identificaron 329 interacciones. Entre las de nivel **mayor** figuran bupropión, lorcaserina, dietilpropión, dolasetrón y dexfenfluramina. Entre las de nivel **moderado**: epinefrina, morfina, ácido acetilsalicílico, cimetidina, difenoxina, difenoxilato, dronabinol, ácido picosúlfurico y polietilenglicol con electrolitos. Entre las **menores**: famotidina, ranitidina, rabeprazol, dexlansoprazol, hidróxido de aluminio y carbonato de calcio.

Para advertencias y contraindicaciones del prospecto, consultar el prospecto oficial.

---

## Conclusión y Próximos Pasos

**Decisión: Hold** (para la predicción principal: tortícolis paroxístico benigno de la infancia)

**Justificación:**
La predicción carece de ensayos clínicos y literatura (nivel L5), no hay vínculo mecanístico plausible, y la duloxetina no está establecida en población infantil. Además, los dos registros sanitarios colombianos están cancelados.

**Para avanzar se necesita:**
- Reorientar la evaluación hacia el **TOC refractario** (nivel L2; ECA pequeño de potenciación, estudio abierto y ensayo de Fase 4), o hacia la agorafobia/trastorno de pánico como línea de investigación (L3), según prioridades.
- Un ECA de Fase 3 con muestra adecuada para respaldar cualquier nueva indicación.
- Descargar y analizar el prospecto de INVIMA para completar el cribado de seguridad (advertencias y contraindicaciones; brecha bloqueante).
- Datos detallados del mecanismo de acción (consulta a DrugBank).
- Aclarar la indicación original aprobada, ya que el registro solo indica "duloxetina".
- Verificar la situación regulatoria: ningún registro vigente en Colombia, por lo que se requeriría un nuevo registro o reactivación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

