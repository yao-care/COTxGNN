---
layout: default
title: Propafenone
parent: Solo Predicción del Modelo (L5)
nav_order: 538
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Propafenone: nueva indicación predicha, Trastorno afectivo bipolar maníaco (nivel de evidencia L4). Indicación original: Propafenona"
monitor_inn: "propafenone"
predicted_indications: ["manic bipolar affective disorder", "periodic paralysis with transient compartment-like syndrome", "Prinzmetal angina", "arrhythmogenic right ventricular cardiomyopathy", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania"]
---

# Propafenone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Propafenona: De Antiarrítmico (Propafenona) a Trastorno Afectivo Bipolar Maníaco
{: .text-alpha }

## Resumen en Una Frase

La propafenona es un antiarrítmico de clase IC, registrado en Colombia como RYTMONORM® 300 mg tabletas (el registro sanitario consta solo con el nombre del principio activo, sin texto de indicación detallado).
El modelo TxGNN predice que podría ser efectivo para **trastorno afectivo bipolar maníaco**, pero **no hay ensayos clínicos** y solo hay **3 publicaciones** (una revisión y dos reportes de caso), que describen la propafenona como posible causa de manía y de interacciones adversas, no como tratamiento.
Esta predicción no cuenta con respaldo terapéutico; la evidencia disponible apunta a una señal de seguridad.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Propafenona (el registro no detalla la indicación; se trata de un antiarrítmico) |
| Nueva Indicación Predicha | Trastorno afectivo bipolar maníaco |
| Puntaje de Predicción TxGNN | 0.9980 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 1) |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la propafenona es un antiarrítmico de clase IC que bloquea los canales de sodio, y su eficacia en arritmias está comprobada. Sin embargo, no existe un vínculo mecanístico plausible con el manejo de la manía bipolar.

La literatura disponible va en dirección contraria a la predicción: un reporte de caso de 1985 describe un episodio de manía secundario a la propafenona (los autores especulan que, por su parecido químico con el bupropión, podría tener efectos afectivos), un reporte de 2001 describe una psicosis orgánica por interacción venlafaxina-propafenona en un paciente bipolar, y una revisión de 2020 aborda las interacciones adversas entre antipsicóticos y fármacos cardiovasculares.

Por ello, el alto puntaje proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica ni un efecto terapéutico real. Esta predicción debe considerarse una señal de seguridad, no una hipótesis de eficacia.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [32124390](https://pubmed.ncbi.nlm.nih.gov/32124390/) | 2020 | Revisión | Pharmacological Reports | Evalúa interacciones dañinas entre antipsicóticos y fármacos cardiovasculares en pacientes con trastorno bipolar o esquizofrenia y comorbilidad cardiovascular |
| [11949740](https://pubmed.ncbi.nlm.nih.gov/11949740/) | 2001 | Reporte de caso | International Journal of Psychiatry in Medicine | Psicosis orgánica por interacción venlafaxina-propafenona en un paciente con trastorno bipolar |
| [2579063](https://pubmed.ncbi.nlm.nih.gov/2579063/) | 1985 | Reporte de caso | Journal of Clinical Psychiatry | Caso de manía secundaria a propafenona; complicación potencial no reconocida previamente |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 45821 (cancelado) | RYTMONORM® 300 MG TABLETAS | Tableta cubierta (gragea) | Propafenona |

---

## Consideraciones de Seguridad

- **Contraindicaciones sugeridas por el grafo de conocimiento** (relaciones fármaco-enfermedad del grafo de conocimiento, no texto de prospecto):
  - Cardiovasculares: síndrome de QT largo (incluida la forma familiar), torsades de pointes, infarto de miocardio, trombosis coronaria, enfermedad arterial coronaria, aterosclerosis, trastornos hipotensivos.
  - Hematológicas: agranulocitosis, neutropenia (incluidas formas congénitas), hemoglobinopatía.
  - Otras: enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, deficiencia de potasio, miastenia gravis y enfermedades de la unión neuromuscular.
- **Interacciones Farmacológicas**: se identificaron 190 interacciones; entre las mostradas destacan las de nivel **mayor** con dolasetrón y eliglustat. Entre las de nivel moderado figuran ondansetrón, palonosetrón, claritromicina, levofloxacino, bupropión, cimetidina, famotidina, aprepitant, alosetrón y loperamida, entre otras. Metronidazol es de nivel menor.
- **Señal de seguridad psiquiátrica**: la literatura reporta manía inducida por propafenona y psicosis por interacción con venlafaxina.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos y la literatura disponible describe a la propafenona como posible desencadenante de manía y de interacciones adversas, no como tratamiento. Además, el único registro sanitario en Colombia está cancelado, y el puntaje alto del modelo no tiene respaldo mecanístico ni clínico.

**Para avanzar se necesita:**
- No se recomienda avanzar con esta indicación a menos que aparezca evidencia preclínica o clínica que sustente un efecto terapéutico.
- Datos del mecanismo de acción y del prospecto (advertencias y contraindicaciones oficiales del INVIMA) para completar el análisis de seguridad.
- Si se busca reposicionamiento de la propafenona, considerar candidatas con mejor respaldo, como la **taquicardia ventricular polimórfica catecolaminérgica** (nivel L3, con evidencia preclínica sobre inhibición del receptor de rianodina RyR2 y un reporte de 35 años de tratamiento eficaz), que merece evaluación como pregunta de investigación, teniendo en cuenta el riesgo proarrítmico de los fármacos de clase IC y la cardiopatía estructural.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

