---
layout: default
title: Propylthiouracil
parent: Evidencia Moderada (L3-L4)
nav_order: 541
evidence_level: L4
indication_count: 2
last_modified_at: 2026-11-25
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

El propiltiouracilo inhibe la tiroperoxidasa y reduce la síntesis de hormonas tiroideas. Además bloquea la conversión periférica de T4 a T3 mediante la desyodasa tipo 1. Según la sección «Clinical Pharmacology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Propylthiouracil (traducción no oficial): «El propiltiouracilo inhibe la síntesis de las hormonas tiroideas y, por lo tanto, es eficaz en el tratamiento del hipertiroidismo. El fármaco no inactiva la tiroxina ni la triyodotironina existentes que están almacenadas en la tiroides o que circulan en la sangre, ni interfiere con la eficacia de las hormonas tiroideas administradas por vía oral o por inyección.» Texto original en inglés: "Propylthiouracil inhibits the synthesis of thyroid hormones and thus is effective in the treatment of hyperthyroidism. The drug does not inactivate existing thyroxine and triiodothyronine that are stored in the thyroid or circulating in the blood, nor does it interfere with the effectiveness of thyroid hormones given by mouth or by injection." ([DailyMed: propylthiouracil prescribing information, American Health Packaging](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d819e532-09ac-434a-84a6-636c4204c7aa), versión del 2026-08-27; consultado el 2026-11-19).

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

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 19952712 | TIROSTAT 100 | TABLETA | PROPILTIOURACILO | Vigente |
| 30968 | TIROSTAT 50 | TABLETA | PROPILTIOURACILO | Vigente |

Se muestran los 2 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

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
La predicción principal se apoya únicamente en el puntaje del modelo y en literatura preclínica y de casos que no evalúa el propiltiouracilo; además, el mecanismo sugiere un posible perjuicio en RTH-beta (aumento de TSH y bocio).

<!-- review:begin co-lic-20261125b-propylthiouracil-1 -->

> **Corrección de revisión (2026-11-25)**: Texto original: "El fármaco tampoco tiene registro vigente en Colombia." Corregido según los datos del INVIMA: el medicamento cuenta con registros sanitarios vigentes; se quitó la premisa de que no hay registros vigentes o de que habría que reactivar o volver a solicitar el registro. Las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261125b-propylthiouracil-1 -->

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA con advertencias y contraindicaciones (vacío bloqueante para el cribado de seguridad).
- Completar los datos de mecanismo de acción desde DrugBank.
- Análisis de la plausibilidad fisiopatológica y de seguridad frente a la RTH-beta, con revisión sistemática de la experiencia clínica con antitiroideos en esta condición.
- Evaluar la tirotoxicosis neonatal como pregunta de investigación separada, frente al metimazol.

<!-- review:begin co-lic-20261031-propylthiouracil-1 -->

> **Corrección de revisión (2026-10-31)**: Texto original: "Evaluar la tirotoxicosis neonatal como pregunta de investigación separada, frente al metimazol. / Aclarar la situación regulatoria (registros cancelados) y la disponibilidad real del producto en Colombia." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-10-31. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261031-propylthiouracil-1 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-10-31 | Eliminado: "Aclarar la situación regulatoria (registros cancelados) y la disponibilidad real del producto en Colombia" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: propylthiouracil prescribing information, American Health Packaging](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d819e532-09ac-434a-84a6-636c4204c7aa) |
| 2026-11-25 | Eliminado: «El fármaco tampoco tiene registro vigente en Colombia.» | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

