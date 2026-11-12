---
layout: default
title: Phenytoin
parent: Solo Predicción del Modelo (L5)
nav_order: 514
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-12
description: "Phenytoin: nueva indicación predicha, Neoplasia del nervio trigémino (nivel de evidencia L5). Indicación original: Fenitoína"
monitor_inn: "phenytoin"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia", "beta-ketothiolase deficiency"]
---

# Phenytoin
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

## Fenitoína: De Fenitoína (registro INVIMA) a Neoplasia del Nervio Trigémino
{: .text-alpha }

## Resumen en Una Frase

La fenitoína es un fármaco anticonvulsivante, registrado en Colombia bajo el nombre EPAMIN® PARENTERICO (solución inyectable).
El modelo TxGNN predice que podría ser efectivo para **neoplasia del nervio trigémino**, pero **no hay ensayos clínicos** y solo **2 publicaciones** relacionadas, ninguna sobre tratamiento de tumores.
La predicción debe considerarse con mucha cautela: el puntaje proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, como la neuralgia del trigémino, no evidencia biológica de un efecto antitumoral.

<!-- review:begin co-lic-20261105-phenytoin-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La fenitoína es un fármaco anticonvulsivante, registrado en Colombia bajo el nombre EPAMIN® PARENTERICO (solución inyectable), cuyo registro sanitario figura actualmente como cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 7 registros sanitarios (vigentes: 6); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-phenytoin-1 -->

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Fenitoína (el texto del registro INVIMA no detalla la indicación) |
| Nueva Indicación Predicha | Neoplasia del nervio trigémino |
| Puntaje de Predicción TxGNN | 0.9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 6 de 7) |
| Número de Registros Sanitarios | 7 (vigentes: 6) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, la fenitoína es un anticonvulsivante que bloquea los canales de sodio dependientes de voltaje, lo que reduce la descarga neuronal repetitiva y la propagación de las crisis.

La relación con la nueva indicación es débil. La fenitoína se usa en dolor del nervio trigémino (neuralgia), pero no hay evidencia de que actúe sobre tejido tumoral. El puntaje alto proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, como la neoplasia del nervio trigémino y la neuralgia del trigémino, no evidencia biológica de un efecto antineoplásico. Las dos publicaciones recuperadas tratan sobre neuralgia del trigémino y síndrome de Sturge-Weber, no sobre el tratamiento de neoplasias.

Por ello, desde el punto de vista mecanístico, esta predicción no está respaldada. Dentro de las predicciones del modelo, la **neuralgia del trigémino** (puntaje 0.9997, nivel L3) es la candidata con evidencia más sólida y coherente con el mecanismo del fármaco.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Revisión | Expert Review of Neurotherapeutics | Revisión de los múltiples tratamientos médicos y quirúrgicos de la neuralgia del trigémino; no aborda neoplasias |
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Serie de casos | Anales Españoles de Pediatría | Experiencia con 14 casos de síndrome de Sturge-Weber; no trata neoplasias del trigémino |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 24335 | EPAMIN® PARENTERICO 50 MG/ML X 5 ML | Solución inyectable | Fenitoína |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): síndrome de QT largo (incluido el familiar), torsades de pointes, insuficiencia y enfermedad hepática, encefalopatía y coma hepático, enfermedad renal, porfiria (incluida la hereditaria), enfermedad de la vesícula biliar, trombocitopenia, neutropenia, agranulocitosis, hiperglucemia, diabetes mellitus y cetoacidosis diabética, lupus eritematoso sistémico, trastornos hipotensivos, trastornos de ansiedad y neuróticos, trastorno distímico, abuso o dependencia de sustancias, apnea del sueño y síndromes de hipoventilación.
- **Interacciones farmacológicas**: se identificaron 390 interacciones. Entre las listadas, la mayoría son de nivel moderado: acarbosa, famotidina, ranitidina, doxiciclina, hidrocortisona, albiglutida, colecalciferol, alogliptina, metformina, pioglitazona, bupropión, aprepitant, triamcinolona, morfina, omeprazol, dexametasona, betametasona, metronidazol y calcifediol. La interacción con ácido acetilsalicílico es de nivel menor.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos y la literatura recuperada no aborda el tratamiento de neoplasias del nervio trigémino. No hay vínculo mecanístico plausible con un efecto antitumoral, por lo que el puntaje del modelo TxGNN (aprendizaje profundo) puede reflejar similitudes aprendidas entre enfermedades relacionadas, no evidencia biológica. Además, el medicamento está comercializado en Colombia y cuenta con 6 registros sanitarios vigentes.

<!-- review:begin co-lic-20261112-phenytoin-1 -->

> **Corrección de revisión (2026-11-12)**: Texto original: "1 registro sanitario vigente" Corregido según los datos del INVIMA (Código Único de Medicamentos, datos al 2026-11-05): 7 registros sanitarios, de los cuales 6 vigentes y 1 vigentes pero temporalmente no comercializados. Las cifras actuales están en el Resumen rápido. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261112-phenytoin-1 -->

**Para avanzar se necesita:**
- Priorizar la evaluación de **neuralgia del trigémino** (nivel L3), que es la indicación mejor respaldada, en lugar de la neoplasia.
- Datos del mecanismo de acción confirmados desde DrugBank.
- Prospecto de INVIMA con advertencias y contraindicaciones oficiales, necesario para cualquier evaluación de seguridad.
- Evidencia directa (preclínica o clínica) de actividad de la fenitoína en tumores del nervio trigémino, si se desea mantener esta hipótesis.

<!-- review:begin co-lic-20261105-phenytoin-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Aclarar la situación regulatoria: no hay registro vigente de fenitoína inyectable en los datos compilados. / Evidencia directa (preclínica o clínica) de actividad de la fenitoína en tumores del nervio trigémino, si se desea mantener esta hipótesis." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 7 registros sanitarios (vigentes: 6); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-phenytoin-2 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "cuyo registro sanitario figura actualmente como cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Aclarar la situación regulatoria: no hay registro vigente de fenitoína inyectable en los datos compilados" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-12 | Número de registros vigentes: 1 → 6 | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

