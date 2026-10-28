---
layout: default
title: Primidone
parent: Solo Predicción del Modelo (L5)
nav_order: 535
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Primidone: nueva indicación predicha, Neoplasia del nervio trigémino (nivel de evidencia L5). Indicación original: PRIMIDONA"
monitor_inn: "primidone"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia", "beta-ketothiolase deficiency"]
---

# Primidone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Primidona: De Indicación No Especificada a Neoplasia del Nervio Trigémino
{: .text-alpha }

## Resumen en Una Frase

Primidona es un anticonvulsivo cuyo registro sanitario en Colombia (tabletas de 250 mg) figura solo con el nombre del principio activo, sin una indicación detallada.
El modelo TxGNN predice como primera opción **neoplasia del nervio trigémino** (puntaje 0.9999), pero **sin ensayos clínicos ni publicaciones** que la respalden; es una predicción puramente computacional y mecanísticamente poco plausible.
Entre las demás predicciones, la **neuralgia del trigémino** es la más verosímil clínicamente, aunque con evidencia solo indirecta.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | PRIMIDONA (el registro no detalla una indicación específica) |
| Nueva Indicación Predicha | Neoplasia del nervio trigémino |
| Puntaje de Predicción TxGNN | 0.9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, la primidona es un antiepiléptico que se metaboliza a fenobarbital y feniletilmalonamida (PEMA). El fenobarbital potencia la inhibición mediada por el receptor GABA-A, y la primidona también modula canales de sodio. Su eficacia en epilepsia está bien establecida.

Para la neoplasia del nervio trigémino **no existe un vínculo mecanístico plausible**: no hay un mecanismo antineoplásico conocido para la primidona. El puntaje (0.9999) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, como la neuralgia del trigémino, y no evidencia biológica. Este puntaje tan alto debe interpretarse con cautela.

Otras predicciones del modelo sí guardan relación con la acción antiepiléptica: epilepsias reflejas (convulsiones por pensamiento, sobresalto, alimentación, micción, estímulos sonoros, lectura u orgasmo) y neuralgia del trigémino. Ahí el mecanismo es plausible, pero la evidencia es indirecta (ver más abajo). La deficiencia de beta-cetotiolasa, en cambio, es un trastorno metabólico sin conexión conocida con la primidona.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para ninguna de las indicaciones predichas.

---

## Evidencia de Literatura

Para la indicación principal (neoplasia del nervio trigémino) actualmente no hay literatura relacionada disponible. A modo de referencia, estas son las publicaciones asociadas a la predicción más plausible clínicamente, **neuralgia del trigémino** (puesto 9 del modelo):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [15246950](https://pubmed.ncbi.nlm.nih.gov/15246950/) | 2004 | Revisión | Epileptic Disorders | Uso de antiepilépticos en indicaciones distintas de la epilepsia; la evidencia proviene sobre todo de series de casos y estudios pequeños |
| [3092407](https://pubmed.ncbi.nlm.nih.gov/3092407/) | 1986 | Revisión | Ther Drug Monit | Interacciones de la carbamazepina, incluido su efecto sobre primidona y fenobarbital |
| [8877250](https://pubmed.ncbi.nlm.nih.gov/8877250/) | 1996 | Revisión | Clin Pharmacokinet | Interacciones farmacocinéticas de la carbamazepina, usada también en neuralgia del trigémino |
| [26018946](https://pubmed.ncbi.nlm.nih.gov/26018946/) | 2015 | Revisión | Clin Biochem | Monitoreo del metabolito activo de la carbamazepina |
| [13480440](https://pubmed.ncbi.nlm.nih.gov/13480440/) | 1957 | Revisión | Gazette médicale de France | Tratamiento médico de la neuralgia esencial del trigémino con diversos antiepilépticos |
| [41806836](https://pubmed.ncbi.nlm.nih.gov/41806836/) | 2026 | Estudio animal | Cell Rep Med | Papel de TRPM3 en dolor neuropático orofacial en ratón |

La literatura es mayoritariamente sobre carbamazepina; **no se encontró ningún estudio clínico específico de primidona** en neuralgia del trigémino.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20132767 (cancelado) | PRIMIDONA 250 MG TABLETAS | Tableta | PRIMIDONA |

El producto estaba a cargo del Fondo Nacional de Estupefacientes (Ministerio de Salud y Protección Social). No hay registros vigentes.

---

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no del prospecto):** porfirias (incluida la porfiria hereditaria), enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, trastornos hematológicos (trombocitopenia, neutropenia, agranulocitosis, leucopenia, pancitopenia, anemias), abuso o dependencia de sustancias, apnea del sueño y síndromes de hipoventilación central, y trastornos de ansiedad, neuróticos o distímicos.
- **Interacciones farmacológicas:** se identificaron 273 interacciones. Entre las principales:
  - **Mayores:** morfina y eliglustat.
  - **Moderadas:** doxiciclina, hidrocortisona, dexametasona, betametasona, triamcinolona, colecalciferol, calcifediol, calcitriol, pioglitazona, bupropión, aprepitant, metronidazol, canagliflozina, saxagliptina, difenoxina, difenoxilato y dronabinol.
  - **Menores:** cimetidina.

La información de advertencias del prospecto de INVIMA no estaba disponible; consultar el prospecto para confirmar la seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación principal (neoplasia del nervio trigémino) carece de ensayos, literatura y plausibilidad mecanística, por lo que su puntaje alto es solo un artefacto del modelo. El único registro sanitario en Colombia está cancelado y el perfil de seguridad es exigente (contraindicaciones hematológicas, hepáticas y renales, y numerosas interacciones).

**Para avanzar se necesita:**
- Replantear la prioridad: la **neuralgia del trigémino** (nivel L4, etapa S1, "pregunta de investigación") es la candidata más razonable, aunque la carbamazepina y la oxcarbazepina ya tienen eficacia establecida, lo que limita la necesidad no cubierta.
- Revisión sistemática de primidona en neuralgia del trigémino y epilepsias reflejas, ya que la evidencia actual es indirecta (reportes de caso, revisiones generales y modelos animales).
- Obtener el prospecto de INVIMA con advertencias y contraindicaciones, y los datos del mecanismo de acción desde DrugBank.
- Aclarar la situación regulatoria: no hay registros vigentes en Colombia, por lo que cualquier uso requeriría un nuevo registro o importación.
- Plan de monitoreo de seguridad (hemograma, función hepática y renal, interacciones) antes de cualquier estudio.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

