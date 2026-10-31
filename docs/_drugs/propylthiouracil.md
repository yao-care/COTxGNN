---
layout: default
title: Propylthiouracil
parent: Evidencia Moderada (L3-L4)
nav_order: 541
evidence_level: L4
indication_count: 2
last_modified_at: 2026-10-31
description: "Propylthiouracil: nueva indicación predicha, Resistencia a la hormona tiroidea por mutación del receptor beta de la hormona tiroidea (nivel de evidencia L4). Indicación original: Propiltiouracilo"
monitor_inn: "propylthiouracil"
predicted_indications: ["resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "hyperthyroxinemia"]
---

# Propylthiouracil
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **2** 
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

## Propiltiouracilo: De Propiltiouracilo (antitiroideo) a Resistencia a la hormona tiroidea por mutación del receptor beta de la hormona tiroidea
{: .text-alpha }

## Resumen en Una Frase

El propiltiouracilo es un fármaco antitiroideo que inhibe la síntesis de hormonas tiroideas; en Colombia sus registros sanitarios aparecen únicamente con el nombre del principio activo como indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **resistencia a la hormona tiroidea por mutación del receptor beta de la hormona tiroidea**, pero **no hay ensayos clínicos** y las **4 publicaciones** recuperadas son modelos en ratón y reportes de caso, ninguna evalúa el propiltiouracilo como tratamiento.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Propiltiouracilo (el registro no detalla una indicación clínica) |
| Nueva Indicación Predicha | Resistencia a la hormona tiroidea por mutación del receptor beta de la hormona tiroidea |
| Puntaje de Predicción TxGNN | 0.9966 |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 2 de 2) |
| Número de Registros Sanitarios | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

El propiltiouracilo inhibe la tiroperoxidasa y reduce la síntesis de hormonas tiroideas. Además bloquea la conversión periférica de T4 a T3 mediante la desyodasa tipo 1. Estos datos de mecanismo provienen del análisis de la predicción, ya que no se dispone de datos detallados de mecanismo de acción en la ficha del fármaco.

En la resistencia a la hormona tiroidea beta (RTH-beta) las hormonas circulantes (T4/T3) están elevadas y la TSH es normal o alta de forma inapropiada. En teoría, reducir la producción hormonal podría disminuir los efectos impulsados por la TSH.

Sin embargo, el razonamiento tiene una limitación importante: por el defecto del receptor, bajar las hormonas puede **aumentar aún más la TSH**, favoreciendo bocio y estimulación tirotropa, y puede empeorar síntomas de hipotiroidismo en tejidos que dependen del receptor TRα o de la función residual de TRβ. Un caso descrito (PMID 10724359) muestra que una paciente tratada con propiltiouracilo por un diagnóstico erróneo de tirotoxicosis presentó mayor aumento del bocio. El puntaje alto del modelo es una predicción computacional, no evidencia clínica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [12201835](https://pubmed.ncbi.nlm.nih.gov/12201835/) | 2002 | Reporte de caso | Clinical Endocrinology | Tirotoxicosis neonatal e infertilidad materna en RTH por mutación M313T de TRβ; no evalúa propiltiouracilo |
| [10724359](https://pubmed.ncbi.nlm.nih.gov/10724359/) | 1999 | Reporte de caso | Endocrine Journal | Mujer tailandesa con mutación L330S de novo; el bocio aumentó tras 9 meses de propiltiouracilo por diagnóstico erróneo de tirotoxicosis |
| [22919057](https://pubmed.ncbi.nlm.nih.gov/22919057/) | 2012 | Preclínico (ratón) | Endocrinology | Papel de la TSH en el desarrollo de carcinoma tiroideo asimétrico en ratones con mutación de TRβ |
| [21909131](https://pubmed.ncbi.nlm.nih.gov/21909131/) | 2012 | Preclínico (ratón) | Oncogene | Activación de la proliferación tumoral por hormona tiroidea en un modelo murino de carcinoma folicular de tiroides |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19952712 (cancelado) | TIROSTAT 100 | Tableta | Propiltiouracilo |
| 30968 (cancelado) | TIROSTAT 50 | Tableta | Propiltiouracilo |

Ambos productos son de Laboratorios Siegfried S.A.S. y los 2 registros están vigentes actualmente.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no texto de prospecto):** trombocitopenia, hipotiroidismo, mixedema, hipotiroidismo congénito, hiperbilirrubinemia (incluido el síndrome de Gilbert), enfermedad pulmonar intersticial, lesión hepática inducida por fármacos, y múltiples formas de reducción de células sanguíneas (leucopenia, pancitopenia, agranulocitosis y neutropenias congénitas y adquiridas).
- **Interacciones farmacológicas:** se identificaron 83 interacciones. Entre las principales:
  - Mayor: deferiprona.
  - Moderadas: naltrexona, yoduro I-131, yoduro I-123, macimorelina, warfarina, dicumarol, teofilina, aminofilina y oxtrifilina.
- **Advertencia relevante en la literatura:** el propiltiouracilo conlleva una advertencia de hepatotoxicidad en recuadro negro.

No se dispone del texto de advertencias y contraindicaciones del prospecto aprobado en INVIMA; debe consultarse.

---

## Otras Predicciones Evaluadas

| Indicación Predicha | Puntaje TxGNN | Nivel | Recomendación |
|------|------|------|------|
| Hipertiroxinemia | 0.9908 | L4 | Hold |

- **Tirotoxicosis neonatal:** la literatura (revisiones y un estudio de cohorte, PMID 25747892) trata sobre todo la enfermedad de Graves materna, donde el propiltiouracilo se usa en el primer trimestre. La relevancia para el recién nacido es indirecta; el tratamiento neonatal directo suele usar metimazol. No hay ensayos clínicos.
- **Hipertiroxinemia:** es un hallazgo de laboratorio heterogéneo. En la hipertiroxinemia disalbuminémica familiar el paciente es eutiroideo y el tratamiento antitiroideo no está indicado y podría dañar. Solo hay un reporte de caso con propiltiouracilo más L-tiroxina (PMID 18334584).

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal se apoya únicamente en el puntaje del modelo y en literatura preclínica y de casos que no evalúa el propiltiouracilo; además, el mecanismo sugiere un posible perjuicio en RTH-beta (aumento de TSH y bocio). El fármaco tampoco tiene registro vigente en Colombia.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA con advertencias y contraindicaciones (vacío bloqueante para el cribado de seguridad).
- Completar los datos de mecanismo de acción desde DrugBank.
- Análisis de la plausibilidad fisiopatológica y de seguridad frente a la RTH-beta, con revisión sistemática de la experiencia clínica con antitiroideos en esta condición.
- Evaluar la tirotoxicosis neonatal como pregunta de investigación separada, frente al metimazol.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

