---
layout: default
title: Phenytoin
parent: Solo Predicción del Modelo (L5)
nav_order: 514
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-25
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

> **Corrección de revisión (2026-11-05)**: Texto original: "La fenitoína es un fármaco anticonvulsivante, registrado en Colombia bajo el nombre EPAMIN® PARENTERICO (solución inyectable), cuyo registro sanitario figura actualmente como cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-phenytoin-1 -->

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Fenitoína (el texto del registro INVIMA no detalla la indicación) |
| Nueva Indicación Predicha | Neoplasia del nervio trigémino |
| Puntaje de Predicción TxGNN | 0.9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 6 de 8) |
| Número de Registros Sanitarios | 8 (vigentes: 6) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Phenytoin (traducción no oficial): «No se ha establecido el mecanismo preciso por el cual la fenitoína ejerce su efecto terapéutico, pero se cree que implica el bloqueo dependiente del voltaje de los canales de sodio de la membrana, lo que produce una reducción de las descargas neuronales sostenidas de alta frecuencia.» Texto original en inglés: "The precise mechanism by which phenytoin exerts its therapeutic effect has not been established but is thought to involve the voltage-dependent blockade of membrane sodium channels resulting in a reduction in sustained high-frequency neuronal discharges." ([DailyMed: Extended Phenytoin Sodium (phenytoin sodium) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=363cd347-d25e-42b9-9ce7-30642f3cb353), versión del 2026-06-25; consultado el 2026-11-19). Según la información conocida, la fenitoína es un anticonvulsivante que bloquea los canales de sodio dependientes de voltaje, lo que reduce la descarga neuronal repetitiva y la propagación de las crisis.

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

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 19956452 | FENATEN®250 MG/5ML SOLUCION INYECTABLE. I.V. | SOLUCION INYECTABLE | FENITOINA | Vigente |
| 19990588 | FENITOINA SODICA 250 MG/5 ML | SOLUCION INYECTABLE | FENITOINA | Vigente |
| 20019155 | FENITOINA SODICA SOLUCION INYECTABLE 250 MG/5ML | SOLUCION INYECTABLE | FENITOINA | Vigente |
| 20028809 | BLASK® SOLUCION INYECTABLE | SOLUCION INYECTABLE | FENITOINA | Vigente |
| 20097693 | FENITOINA 100 MG | CAPSULA DURA | FENITOINA | Vigente |

Se muestran 5 de 8 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

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

**Para avanzar se necesita:**
- Priorizar la evaluación de **neuralgia del trigémino** (nivel L3), que es la indicación mejor respaldada, en lugar de la neoplasia.
- Datos del mecanismo de acción confirmados desde DrugBank.
- Prospecto de INVIMA con advertencias y contraindicaciones oficiales, necesario para cualquier evaluación de seguridad.
- Evidencia directa (preclínica o clínica) de actividad de la fenitoína en tumores del nervio trigémino, si se desea mantener esta hipótesis.

<!-- review:begin co-lic-20261105-phenytoin-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Aclarar la situación regulatoria: no hay registro vigente de fenitoína inyectable en los datos compilados. / Evidencia directa (preclínica o clínica) de actividad de la fenitoína en tumores del nervio trigémino, si se desea mantener esta hipótesis." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-phenytoin-2 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "cuyo registro sanitario figura actualmente como cancelado" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Aclarar la situación regulatoria: no hay registro vigente de fenitoína inyectable en los datos compilados" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-12 | Número de registros vigentes: 1 → 6 | Ya no aparece tras una corrección del programa (2026-11-24: el número de registros sanitarios de esta frase lo actualiza ahora un programa según los datos del INVIMA (scripts/rewrite_license_counts.py), por lo que esta corrección puntual ya no se muestra; antes: Corregido) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Extended Phenytoin Sodium (phenytoin sodium) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=363cd347-d25e-42b9-9ce7-30642f3cb353) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

