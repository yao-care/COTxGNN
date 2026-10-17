---
layout: default
title: Diazepam
parent: Evidencia Moderada (L3-L4)
nav_order: 217
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-14
description: "Diazepam: nueva indicación predicha, Insomnio (nivel de evidencia L3). Indicación original: Diazepam"
monitor_inn: "DIAZEPAM"
predicted_indications: ["insomnia (disease)", "cauda equina syndrome", "sleep disorder, initiating and maintaining sleep", "attention deficit hyperactivity disorder, inattentive type", "hallucinogen abuse", "antidepressant type abuse", "barbiturate abuse", "specific developmental disorder", "attention deficit-hyperactivity disorder", "obsolete neurogenic bladder (disease)"]
---

# Diazepam
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **10** 
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

# Diazepam: De Indicación Original (Diazepam) a Insomnio

## Resumen en Una Frase

Diazepam es una benzodiacepina cuyo único registro sanitario en Colombia (solución inyectable) figura solo con el nombre del principio activo como indicación, sin un uso terapéutico detallado.
El modelo TxGNN predice que podría ser efectivo para **insomnio**, pero actualmente no hay ensayos clínicos registrados y la literatura disponible consiste sobre todo en revisiones, estudios farmacológicos y trabajos de medicina herbal, por lo que la evidencia es limitada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Diazepam (el registro no detalla una indicación específica) |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción registrado. Según el conocimiento farmacológico general, el diazepam es un modulador alostérico positivo del receptor GABA-A: potencia la neurotransmisión inhibitoria y produce efectos sedantes, ansiolíticos, anticonvulsivantes y miorrelajantes.

Esa acción sedante-hipnótica explica por qué el insomnio es una indicación biológicamente plausible. Las benzodiacepinas se han usado durante décadas para el insomnio de corta duración, y los resultados de la literatura (por ejemplo, la comparación doble ciego de lormetazepam y diazepam en 100 pacientes ambulatorios, de 1981) son coherentes con esta línea.

Sin embargo, la plausibilidad mecanística no equivale a una ventaja demostrada. El uso prolongado se asocia con dependencia, tolerancia y alteración de la arquitectura del sueño, y las guías actuales recomiendan limitar su uso en insomnio. Además, no se dispone de datos sobre la similitud entre la indicación original y la nueva, porque la indicación registrada es inespecífica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Se muestran las publicaciones más relevantes para insomnio (se excluyeron trabajos sin relación directa con el fármaco o la indicación).

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39581171](https://pubmed.ncbi.nlm.nih.gov/39581171/) | 2024 | Revisión | Bioorganic Chemistry | Revisa los moduladores de GABA-A (incluido el diazepam) en trastornos neurológicos y psiquiátricos como epilepsia, ansiedad, insomnio y depresión; señala efectos secundarios como la sedación |
| [6113175](https://pubmed.ncbi.nlm.nih.gov/6113175/) | 1981 | Estudio doble ciego | J Int Med Res | Lormetazepam 1 mg fue superior a diazepam 5 mg en latencia del sueño y continuidad del sueño en 100 pacientes ambulatorios durante 7 días |
| [40583063](https://pubmed.ncbi.nlm.nih.gov/40583063/) | 2025 | Cohorte | Cell Mol Biol Lett | El uso prolongado de benzodiacepinas y fármacos Z, usados en insomnio y ansiedad, se asocia con mayor riesgo de cáncer de mama |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | Metaanálisis | Acta Pharm | Evalúa tranquilizantes en ancianos con enfermedades crónicas según dosis, resultados y efectos adversos |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Revisión | Expert Opin Drug Metab Toxicol | Farmacocinética de los ansiolíticos, ampliamente prescritos en ansiedad e insomnio |
| [31770357](https://pubmed.ncbi.nlm.nih.gov/31770357/) | 2019 | Revisión | Med Lett Drugs Ther | Revisión sobre cannabis y cannabinoides |
| [37984023](https://pubmed.ncbi.nlm.nih.gov/37984023/) | 2024 | Modelo predictivo | Value Health Reg Issues | El uso prolongado de benzodiacepinas se asocia con pérdida de memoria, dependencia, caídas y accidentes de tráfico |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20019151 (cancelado) | Diazepam solución inyectable 10 mg/2 mL (Laboratorio Biosano S.A.) | Solución inyectable | Diazepam |

---

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no texto del prospecto)**: el modelo asocia el diazepam con insuficiencia hepática y enfermedad hepática, enfermedad de la vesícula biliar, glaucoma de ángulo abierto y de ángulo cerrado, síndromes de apnea del sueño, insuficiencia respiratoria y enfermedad pulmonar, miastenia gravis y enfermedades de la unión neuromuscular, trastornos relacionados con sustancias y dependencia, y algunos trastornos de ansiedad y neuróticos.
- **Interacciones Farmacológicas**: se identificaron 100 interacciones. Entre las principales:
  - **Mayor**: morfina (depresión respiratoria y sedación aditivas).
  - **Moderada**: bupropión, aprepitant, omeprazol, esomeprazol, cimetidina, claritromicina, cisaprida, clotrimazol, miconazol, dronabinol y metoclopramida.
  - **Menor**: dexametasona, betametasona y antiácidos (hidróxido de magnesio, hidróxido de aluminio, carbonato de calcio, óxido de magnesio, magaldrato, carbonato de magnesio).
- **Otras señales de la literatura**: dependencia, tolerancia, deterioro cognitivo, caídas en adultos mayores, alteración de la arquitectura del sueño con el uso crónico y reacciones paradójicas en niños con autismo.

Consultar el prospecto para las advertencias y contraindicaciones oficiales, que no estuvieron disponibles en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El mecanismo GABAérgico es coherente con el insomnio, pero no hay ensayos clínicos registrados ni estudios que demuestren eficacia específica de diazepam; la literatura se orienta más a reducir el uso de benzodiacepinas. Además, el único registro sanitario en Colombia está cancelado y la indicación aprobada es inespecífica.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto del registro INVIMA (advertencias y contraindicaciones oficiales), una brecha de datos bloqueante.
- Obtener los datos del mecanismo de acción desde DrugBank.
- Realizar una revisión sistemática de eficacia y seguridad de diazepam frente a los hipnóticos actuales en insomnio, con atención a adultos mayores.
- Aclarar la situación regulatoria (registro cancelado) y la compatibilidad de la vía de administración, ya que la única presentación conocida es inyectable.

---

**Nota sobre otras predicciones:** las demás indicaciones predichas (síndrome de cauda equina, trastornos del inicio y mantenimiento del sueño, TDAH, abuso de alucinógenos, antidepresivos y barbitúricos, trastornos del desarrollo y vejiga neurogénica obsoleta) tienen evidencia L3 a L5 y recomendación Hold. No se recomienda avanzar con ninguna de ellas sin estudios clínicos directos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

