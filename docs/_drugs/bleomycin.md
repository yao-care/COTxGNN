---
layout: default
title: Bleomycin
parent: Solo Predicción del Modelo (L5)
nav_order: 111
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-03
monitor_inn: "bleomycin"
predicted_indications: ["cauda equina neoplasm", "adult astrocytic tumour", "primary pulmonary lymphoma", "pulmonary blastoma", "well-differentiated fetal adenocarcinoma of the lung"]
description: "Bleomycin: nueva indicación predicha, neoplasia de la cauda equina (cauda equina neoplasm) (nivel de evidencia L5). Indicación original: BLEOMICINA"
---

# Bleomycin
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

## Bleomycin: neoplasia de la cauda equina (cauda equina neoplasm)
{: .text-alpha }

## Resumen en Una Frase

Bleomicina es un antineoplásico citotóxico que actúa fragmentando el ADN de las células tumorales y se utiliza en esquemas de quimioterapia como los de tumores de células germinales.
El modelo TxGNN predice que podría ser efectivo para **neoplasia de la cauda equina (cauda equina neoplasm)**, pero actualmente **no hay ensayos clínicos** y solo **1 publicación** relacionada de forma tangencial respalda esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | BLEOMICINA |
| Nueva Indicación Predicha | neoplasia de la cauda equina (cauda equina neoplasm) |
| Puntaje de Predicción TxGNN | 0.9930 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 2 de 2) |
| Número de Registros Sanitarios | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Bleomicina es un agente citotóxico que induce rupturas en las cadenas del ADN. Se emplea en tumores de células germinales y en otros esquemas de quimioterapia combinada. Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Bleomycin (traducción no oficial): «Aunque se desconoce el mecanismo de acción exacto de la bleomicina, la evidencia disponible indica que el principal modo de acción es la inhibición de la síntesis de ADN, con cierta evidencia de una inhibición menor de la síntesis de ARN y de proteínas. Se sabe que la bleomicina provoca roturas de cadena sencilla y, en menor medida, de doble cadena en el ADN.» Texto original en inglés: "Although the exact mechanism of action of bleomycin is unknown, available evidence indicates that the main mode of action is the inhibition of DNA synthesis with some evidence of lesser inhibition of RNA and protein synthesis. Bleomycin is known to cause single, and to a lesser extent, double-stranded breaks in DNA." ([DailyMed: Bleomycin (bleomycin sulfate) prescribing information, Meitheal Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=640602f9-a7df-46f0-a9b1-19c471008bee), versión del 2026-04-17; consultado el 2026-11-19).

La única publicación vinculada trata de radioterapia en germinoma del sistema nervioso central en recaída, tras quimioterapia primaria con carboplatino, etopósido y bleomicina. Este estudio guarda solo una relación tangencial con una neoplasia de la cauda equina: no estudia directamente esta enfermedad ni evalúa la eficacia de bleomicina en ella.

Por tanto, el puntaje elevado del modelo es una predicción sin respaldo clínico directo. Una posible vía plausible sería la actividad citotóxica de bleomicina sobre tumores del sistema nervioso central, pero esta hipótesis no está demostrada.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [9440744](https://pubmed.ncbi.nlm.nih.gov/9440744/) | 1998 | Cohorte (retrospectivo) | Journal of Clinical Oncology | Evalúa la radioterapia como rescate en germinoma del SNC en recaída tras quimioterapia primaria con carboplatino, etopósido y bleomicina; no estudia la neoplasia de la cauda equina |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20259728 | BLENA® 15 UI | Polvo liofilizado para reconstituir a solución inyectable | Bleomicina |
| 20092577 | BLEOMICINA 15 UI | Polvo liofilizado | Bleomicina |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (antibiótico glicopeptídico antitumoral) |
| Riesgo de Mielosupresión | Bajo en general; consultar el prospecto |
| Clasificación de Emetogenicidad | Baja a media |
| Items de Monitoreo | Función pulmonar (riesgo de toxicidad pulmonar), hemograma, función hepática y renal |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se registraron 205 interacciones potenciales. Entre las listadas figuran levofloxacino (menor) y, con nivel no clasificado, pantoprazol, palonosetrón, lactulosa, aprepitant, morfina, omeprazol, lansoprazol, vancomicina, prednisona, hidrocortisona, manitol, cloruro de potasio, prednisolona, ranitidina, granisetrón, ondansetrón, famotidina, claritromicina y metoclopramida.
- La literatura revisada para otras posibles indicaciones señala toxicidad pulmonar como limitación importante de bleomicina.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo: no hay ensayos clínicos y la única publicación vinculada no estudia directamente la neoplasia de la cauda equina, por lo que el nivel de evidencia es L5.

**Para avanzar se necesita:**
- Estudios (preclínicos o clínicos) que evalúen directamente bleomicina en neoplasias de la cauda equina
- Datos detallados del mecanismo de acción
- Advertencias y contraindicaciones del prospecto de INVIMA
- Evaluación de la penetración en el sistema nervioso central y de la toxicidad pulmonar

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Bleomycin (bleomycin sulfate) prescribing information, Meitheal Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=640602f9-a7df-46f0-a9b1-19c471008bee) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

