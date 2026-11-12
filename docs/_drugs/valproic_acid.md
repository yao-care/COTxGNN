---
layout: default
title: Valproic Acid
parent: Solo Predicción del Modelo (L5)
nav_order: 652
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-12
description: "Valproic Acid: nueva indicación predicha, Neoplasia del nervio trigémino (nivel de evidencia L5). Indicación original: Ácido valproico"
monitor_inn: "valproic acid"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia"]
---

# Valproic Acid
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Ácido valproico: De Indicación Registrada (sin descripción específica) a Neoplasia del Nervio Trigémino
{: .text-alpha }

## Resumen en Una Frase

El ácido valproico es un fármaco antiepiléptico de amplio espectro; en Colombia sus registros sanitarios solo indican el nombre del principio activo, sin detallar la indicación. El modelo TxGNN predice que podría ser efectivo para **neoplasia del nervio trigémino**, pero sin ensayos clínicos y con solo **1 publicación** (una serie de casos sobre síndrome de Sturge-Weber, que no aborda esta indicación), por lo que la evidencia real es prácticamente nula.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Ácido valproico (el registro no detalla una indicación específica) |
| Nueva Indicación Predicha | Neoplasia del nervio trigémino |
| Puntaje de Prediccion TxGNN | 0.9997 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 5 de 5) |
| Número de Registros Sanitarios | 5 (vigentes: 5) |
| Decision Recomendada | Hold |

---

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, el ácido valproico es un antiepiléptico establecido que potencia la transmisión GABAérgica y modula los canales de sodio y de calcio tipo T. Además, se le atribuye actividad como inhibidor de histona desacetilasas (HDAC), con posible efecto antineoplásico.

La relación entre la indicación original y la nueva es débil. El uso antiepiléptico no se relaciona directamente con una neoplasia del nervio trigémino. El único vínculo plausible sería la actividad antineoplásica por inhibición de HDAC, o el control de crisis en síndromes neurocutáneos, pero ambos son indirectos y no específicos para esta indicación.

El análisis de los datos concluye que no se ha establecido un vínculo mecanístico creíble. El puntaje alto del modelo no está respaldado por evidencia clínica y debe interpretarse como una hipótesis computacional.

---

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Serie de casos | Anales españoles de pediatría | Revisión de 14 casos de síndrome de Sturge-Weber en 25 años (características clínicas, evolución y respuesta terapéutica). Es un trastorno vascular neurocutáneo, no una neoplasia del trigémino; relevancia indirecta. |

---

## Informacion de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmaceutica | Indicacion Aprobada |
|---------|------|------|-----------|
| 40284 | DEPAKENE® JARABE | Jarabe | Ácido valproico (sin indicación detallada) |
| 20016549 | FERBIN® C.L. 250 MG CAPSULA | Cápsula dura | Ácido valproico (sin indicación detallada) |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no del prospecto):** el grafo de conocimiento del modelo asocia el fármaco con contraindicación en trastorno de ansiedad, trastorno neurótico, trastorno distímico, deficiencia de carbamoil fosfato sintetasa I, porfiria hereditaria y otros trastornos del metabolismo de las porfirinas, enfermedad renal, hiperargininemia, citrulinemia, enfermedad hematológica, pancreatitis, trastorno cognitivo, enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia y piouréter. Estas relaciones no provienen del texto del prospecto y deben verificarse.
- **Interacciones Farmacológicas:** se identificaron 248 interacciones. La de mayor gravedad es con **glicerol fenilbutirato (Mayor)**. Entre las moderadas figuran bupropión, morfina, ácido acetilsalicílico, claritromicina, difenoxina, difenoxilato, carbón activado, dronabinol, metoclopramida y nabilona. Entre las menores figuran cimetidina, esomeprazol y antiácidos (hidróxido de aluminio, carbonato de calcio, óxido e hidróxido de magnesio, magaldrato).

No se dispone de las advertencias ni contraindicaciones del prospecto de INVIMA; consultar el prospecto para información de seguridad completa.

---

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
No hay ensayos clínicos, la única publicación recuperada no trata la indicación predicha y no se ha establecido un vínculo mecanístico creíble. El puntaje de 0.9997 no basta por sí solo para justificar avanzar.

<!-- review:begin co-lic-20261105-valproic_acid-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, los dos registros sanitarios en Colombia están cancelados. El puntaje de 0.9997 no basta por sí solo para justificar avanzar." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 5 registros sanitarios (vigentes: 5); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-valproic_acid-1 -->

**Para avanzar se necesita:**
- Evidencia preclínica o clínica específica del ácido valproico en tumores del nervio trigémino (por ejemplo, estudios sobre inhibición de HDAC en esas neoplasias).
- Datos del mecanismo de acción (consultar DrugBank).
- Advertencias y contraindicaciones del prospecto de INVIMA.
- Aclarar la situación regulatoria en Colombia.
- Evaluar si otras indicaciones predichas con mayor respaldo (p. ej., neuralgia del trigémino o epilepsias reflejas como la epilepsia por sobresalto) son prioridades más viables.

<!-- review:begin co-lic-20261105-valproic_acid-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Aclarar la situación regulatoria en Colombia, ya que no hay registros vigentes." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 5 registros sanitarios (vigentes: 5); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-valproic_acid-2 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Además, los dos registros sanitarios en Colombia están cancelados" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "ya que no hay registros vigentes" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

