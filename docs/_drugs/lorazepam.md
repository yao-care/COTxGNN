---
layout: default
title: Lorazepam
parent: Solo Predicción del Modelo (L5)
nav_order: 410
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-29
description: "Lorazepam: nueva indicación predicha, Neoplasia del nervio trigémino (nivel de evidencia L5). Indicación original: No especificada en el registro (el texto aprobado solo indica \"LORAZE…"
monitor_inn: "LORAZEPAM"
predicted_indications: ["trigeminal nerve neoplasm"]
---

# Lorazepam
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

## Lorazepam: De Indicación No Especificada a Neoplasia del Nervio Trigémino
{: .text-alpha }

## Resumen en Una Frase

Lorazepam es una benzodiazepina registrada en Colombia (productos Ativan), cuyo texto de indicación aprobada solo menciona el nombre del principio activo. El modelo TxGNN predice como primera opción **neoplasia del nervio trigémino**, pero sin ensayos clínicos ni publicaciones que la respalden (nivel de evidencia L5). Entre las 10 predicciones evaluadas, la de **insomnio** es la mejor respaldada, con 18 publicaciones, aunque corresponde a un uso ya establecido de la clase y no a un reposicionamiento novedoso.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto aprobado solo indica "LORAZEPAM") |
| Nueva Indicación Predicha | Neoplasia del nervio trigémino |
| Puntaje de Predicción TxGNN | 0.9987 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 1) |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Por conocimiento farmacológico general, lorazepam es un modulador alostérico positivo del receptor GABA-A, con efectos ansiolíticos, sedantes y anticonvulsivantes.

**Para la neoplasia del nervio trigémino no se identifica una justificación mecanística.** Lorazepam no tiene actividad antineoplásica conocida. El puntaje tan alto (0.9987) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica ni un efecto terapéutico demostrado. No hay ensayos ni literatura que lo apoyen.

Otras predicciones del modelo tienen una base mecanística más plausible:

- **Insomnio** (nivel L3): potenciar la señal GABA-A acorta la latencia del sueño y las benzodiazepinas son una clase hipnótica establecida. Sin embargo, las guías actuales desaconsejan su uso prolongado por dependencia, tolerancia y deterioro cognitivo.
- **Epilepsias reflejas** (convulsiones de lectura, por pensamiento, por micción, audiogénicas, epilepsia de sobresalto, entre otras): la potenciación GABAérgica es un mecanismo anticonvulsivante plausible, y lorazepam es tratamiento de primera línea en estado epiléptico. No obstante, la evidencia es indirecta y extrapolada de las convulsiones en general.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para ninguna de las indicaciones predichas.

---

## Evidencia de Literatura

Para la indicación principal (neoplasia del nervio trigémino) no hay literatura disponible. A continuación se presenta la literatura más relevante de la segunda predicción, **insomnio**, la mejor respaldada:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [3280615](https://pubmed.ncbi.nlm.nih.gov/3280615/) | 1988 | Ensayo clínico comparativo (cruzado, doble ciego) | J Clin Pharmacol | Lorazepam 2 mg frente a flurazepam 30 mg durante 3 semanas en 8 insomnes crónicos; lorazepam obtuvo mejores resultados en la mayoría de los parámetros de sueño |
| [10220122](https://pubmed.ncbi.nlm.nih.gov/10220122/) | 1999 | Estudio clínico | Int Clin Psychopharmacol | Lorazepam 0.5 mg tres veces al día frente a 1.5 mg al acostarse en insomnio primario, con énfasis en los síntomas diurnos |
| [30625122](https://pubmed.ncbi.nlm.nih.gov/30625122/) | 2018 | Revisión | Med Lett Drugs Ther | Revisión de fármacos para el insomnio crónico |
| [35087274](https://pubmed.ncbi.nlm.nih.gov/35087274/) | 2022 | Revisión | J Multidiscip Healthc | Eficacia, seguridad e interacciones de las terapias para el insomnio en pacientes con COVID-19 |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Revisión (farmacocinética) | Expert Opin Drug Metab Toxicol | Farmacocinética de los fármacos ansiolíticos |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | Metaanálisis/observacional | Acta Pharm | Efectos de los tranquilizantes en ancianos con enfermedades crónicas no transmisibles |

Para las epilepsias reflejas, la literatura disponible consiste sobre todo en revisiones y guías sobre estado epiléptico y estudios preclínicos en ratas sobre abstinencia de lorazepam. Ninguna aborda directamente estas indicaciones específicas. Destaca el ensayo RAMPART ([22335736](https://pubmed.ncbi.nlm.nih.gov/22335736/), *N Engl J Med*, 2012), que comparó midazolam intramuscular con tratamiento intravenoso en estado epiléptico prehospitalario y es aplicable a convulsiones en general, no a convulsiones reflejas.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 19902389 | ATIVAN 2 MG TABLETAS | Tableta | LORAZEPAM | Vigente |
| 19902391 | ATIVAN® 1 MG TABLETAS | Tableta | LORAZEPAM | Temp. no comerc - Vigente |

Ambos registros pertenecen a PFIZER S.A.S. y están cancelados, por lo que actualmente no hay comercialización autorizada en Colombia.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad del grafo PrimeKG, no texto de prospecto): insuficiencia hepática y enfermedad hepática, encefalopatía y coma hepáticos, enfermedad renal, enfermedad de la vesícula biliar, porfiria (hereditaria y de metabolismo de porfirinas), glaucoma de ángulo abierto y de ángulo cerrado, síndrome de apnea del sueño (incluida la obstructiva), síndrome de hipoventilación central congénita, insuficiencia respiratoria, trastornos relacionados con sustancias y dependencia, así como trastornos de ansiedad, neuróticos y distímicos.
- **Interacciones farmacológicas**: se identificaron 100 interacciones. Las más relevantes:
  - **Mayores**: morfina y morfina liposomal (depresión del sistema nervioso central y respiratoria).
  - **Moderadas**: bupropión, dronabinol, nabilona, teduglutida, metoclopramida, opio y sibutramina.
  - **Menores**: antiácidos como óxido, hidróxido y carbonato de magnesio, hidróxido de aluminio, carbonato de calcio y magaldrato.
- **Señales adicionales de la literatura**: riesgo de toxicidad por propilenglicol con formulaciones parenterales, y dependencia y síndrome de abstinencia (con riesgo de convulsiones) en estudios preclínicos.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación principal (neoplasia del nervio trigémino) carece de ensayos, literatura y justificación mecanística, y su puntaje alto proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes aprendidas entre enfermedades relacionadas, no evidencia biológica. Además, el medicamento está comercializado en Colombia con 2 registros sanitarios vigentes y los datos de seguridad del prospecto no están disponibles.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto del INVIMA (advertencias y contraindicaciones), un vacío crítico que impide el tamizaje de seguridad.
- Obtener datos del mecanismo de acción desde DrugBank.
- Si se desea explorar alternativas, tratar **insomnio** como pregunta de investigación (nivel L3, sin ensayos registrados y con uso a largo plazo desaconsejado), y las **epilepsias reflejas** (nivel L4) como extrapolación desde el uso en convulsiones generales, con medidas de control para depresión respiratoria e interacciones.
- Aclarar la situación regulatoria: los registros están cancelados, por lo que cualquier uso nuevo exigiría un nuevo registro o reactivación.
- Definir la ruta de administración requerida para cada indicación; actualmente solo existe la forma oral (tableta).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

