---
layout: default
title: Formoterol
parent: Solo Predicción del Modelo (L5)
nav_order: 303
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Formoterol: nueva indicación predicha, Malformación respiratoria (nivel de evidencia L5). Indicación original: Formoterol y budesonida (combinación inhalada)"
---

# Formoterol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Formoterol: De Combinaciones Inhaladas para Asma/EPOC a Malformación Respiratoria

## Resumen en Una Frase

Formoterol es un agonista beta2-adrenérgico de acción prolongada, registrado en Colombia únicamente en combinación con budesonida o beclometasona (productos hoy con registro cancelado).
El modelo TxGNN predice que podría ser efectivo para **malformación respiratoria**, pero sin ensayos clínicos específicos y con literatura que no trata esta enfermedad, por lo que la evidencia directa es nula (nivel L5).

> **Nota importante:** de las seis predicciones del modelo, la de mayor puntaje TxGNN para la que existe evidencia sólida es **enfermedad pulmonar obstructiva** (nivel L1), seguida de asma (L1) y bronquitis (L1, inferida a partir de EPOC). La primera predicción (malformación respiratoria) es la que se toma como indicación principal del título, pero los hallazgos más útiles se encuentran en las alternativas que se resumen en la conclusión.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Formoterol y budesonida (combinación inhalada) |
| Nueva Indicación Predicha | Malformación respiratoria |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 3 (todos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, formoterol es un agonista selectivo de los receptores beta2-adrenérgicos que relaja el músculo liso bronquial; los datos farmacológicos disponibles lo vinculan con los receptores beta1 y beta2, y lo describen como tratamiento sintomático del asma y de la EPOC.

La relación con la nueva indicación es débil. Una malformación respiratoria es un defecto estructural congénito, y un broncodilatador no puede corregirlo. En el mejor de los casos aliviaría de forma sintomática una obstrucción secundaria de la vía aérea. Las 9 publicaciones recuperadas tratan sobre asma, EPOC, enfermedad de la vía aérea pequeña pos-COVID y micosis broncopulmonar alérgica, no sobre malformaciones respiratorias.

Por ello, el puntaje elevado probablemente refleja la cercanía en el grafo de conocimiento con enfermedades obstructivas de la vía aérea, y no un vínculo terapéutico genuino.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para malformación respiratoria.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [40840693](https://pubmed.ncbi.nlm.nih.gov/40840693/) | 2026 | ECA (metaanálisis) | J Am Pharm Assoc | Seguridad y eficacia de budesonida/glicopirrolato/formoterol frente a glicopirrolato/formoterol en EPOC |
| [35115339](https://pubmed.ncbi.nlm.nih.gov/35115339/) | 2022 | ECA | Eur Respir J | Budesonida/formoterol repetido frente a salbutamol en asma estable: efectos broncodilatadores, sistémicos y cardiovasculares |
| [22541245](https://pubmed.ncbi.nlm.nih.gov/22541245/) | 2012 | ECA | J Allergy Clin Immunol | Seguridad a largo plazo de budesonida/formoterol en pacientes afroamericanos con asma |
| [14738234](https://pubmed.ncbi.nlm.nih.gov/14738234/) | 2004 | ECA | Eur Respir J | Formoterol protege frente a los efectos del factor activador de plaquetas en asma |
| [20528601](https://pubmed.ncbi.nlm.nih.gov/20528601/) | 2010 | Revisión | J Asthma | Budesonida/formoterol en inhalador presurizado para asma persistente |
| [24842803](https://pubmed.ncbi.nlm.nih.gov/24842803/) | 2014 | Revisión | Prog Neuropsychopharmacol Biol Psychiatry | Estrategias basadas en neurotransmisores para la disfunción cognitiva en síndrome de Down (relevancia indirecta) |
| [35034195](https://pubmed.ncbi.nlm.nih.gov/35034195/) | 2022 | Cohorte | Eur J Appl Physiol | Respuestas compensatorias a anomalías mecánicas en EPOC durante el sueño |
| [37691104](https://pubmed.ncbi.nlm.nih.gov/37691104/) | 2023 | Reporte de caso | J Med Case Rep | Enfermedad de la vía aérea pequeña en COVID prolongado |
| [41686546](https://pubmed.ncbi.nlm.nih.gov/41686546/) | 2026 | Reporte de caso | Medicine | Micosis broncopulmonar alérgica por *Schizophyllum commune* en paciente con cáncer de pulmón |

Ninguna de estas publicaciones evalúa formoterol en malformaciones respiratorias.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 19978720 | BUSTEROL® INHALADOR | Suspensión para inhalación | Formoterol y budesonida | Cancelado |
| 20161093 | FOSTER NEXTHALER | Polvo para inhalación | Formoterol + beclometasona | Cancelado |
| 20102025 | COMPLEBREZ 6MCG/100 MCG INHALACIÓN PRESURIZADA | Aerosoles | Formoterol y budesonida | Cancelado |

---

## Consideraciones de Seguridad

- **Interacciones farmacológicas / farmacología:** formoterol actúa sobre los receptores beta1-adrenérgico (ADRB1) y beta2-adrenérgico (ADRB2). No hay interacciones con otros fármacos con nivel clasificado en los datos compilados.
- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** el modelo asocia formoterol con contraindicación en trastorno hipertensivo e hipertensión, síndrome de QT largo (incluida la forma familiar), epilepsia, enfermedad hepática, enfermedad de la vesícula biliar, sarampión, queratitis por herpes simple, y múltiples formas de hipopituitarismo y deficiencia de hormona de crecimiento (incluido el síndrome de Kallmann y el de Sheehan). Estos datos deben verificarse contra el prospecto.
- **Alertas contextuales (de la evidencia en asma y EPOC):** no usar LABA como monoterapia en asma, y vigilar el riesgo cardiovascular y de neumonía con combinaciones que contienen corticosteroide inhalado.

Para advertencias y contraindicaciones oficiales, consultar el prospecto; los datos del prospecto de INVIMA no estaban disponibles para este informe.

---

## Conclusión y Próximos Pasos

**Decisión: Hold** (para malformación respiratoria)

**Justificación:**
No existen ensayos clínicos ni literatura que respalden formoterol en malformaciones respiratorias, y el mecanismo broncodilatador no puede corregir un defecto estructural. El puntaje TxGNN alto parece un artefacto de proximidad en el grafo con enfermedades obstructivas.

**Otras predicciones del modelo (para priorizar):**

| Indicación predicha | Puntaje TxGNN | Nivel | Decisión del análisis |
|------|------|------|------|
| Enfermedad pulmonar obstructiva | 99.90% | L1 | Proceed with Guardrails |
| Asma | 99.74% | L1 | Proceed with Guardrails (uso ya establecido, no es reposicionamiento novedoso) |
| Bronquitis | 99.92% | L1 (inferido de EPOC) | Pregunta de investigación: definir el fenotipo exacto |
| Síndrome de Rienhoff | 99.90% | L5 | Hold |
| Rasgos relacionados con asma, susceptibilidad | 99.50% | L5 | Hold (mejor abordar mediante la indicación de asma) |

En enfermedad pulmonar obstructiva hay ECA de Fase 3 grandes y completados (por ejemplo, NCT04320342 con 3406 pacientes y NCT03162055 con 1119), con beneficio en exacerbaciones y mortalidad, aunque casi siempre con combinaciones fijas, lo que impide aislar la contribución de formoterol solo.

**Para avanzar se necesita:**
- Descartar formalmente malformación respiratoria como candidata, salvo que surja una hipótesis mecanística específica.
- Descargar y analizar el prospecto de INVIMA para completar advertencias y contraindicaciones oficiales (dato bloqueante pendiente).
- Obtener datos del mecanismo de acción desde DrugBank.
- Verificar el estado regulatorio actual: los tres registros colombianos están cancelados, por lo que cualquier uso depende de nuevos registros o de la disponibilidad de otros productos.
- Para las indicaciones con L1 (EPOC/enfermedad obstructiva, asma), definir si el interés es el fármaco solo o sus combinaciones, y establecer el fenotipo exacto en bronquitis.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

