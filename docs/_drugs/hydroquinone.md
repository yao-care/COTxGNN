---
layout: default
title: Hydroquinone
parent: Solo Predicción del Modelo (L5)
nav_order: 330
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
description: "Hydroquinone: nueva indicación predicha, Queratosis seborreica (nivel de evidencia L5). Indicación original: Hidroquinona"
monitor_inn: "hydroquinone"
predicted_indications: ["seborrheic keratosis", "vulvar inverted follicular keratosis", "exanthem (disease)", "lichen disease"]
---

# Hydroquinone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

## Hidroquinona: De Hidroquinona (uso tópico despigmentante) a Queratosis Seborreica
{: .text-alpha }

## Resumen en Una Frase

La hidroquinona es un agente despigmentante tópico, registrado en Colombia en forma de crema al 5% (CREMOQUINONA 5% CREMA).
El modelo TxGNN predice que podría ser efectiva para **queratosis seborreica**,
pero hasta ahora solo hay **0 ensayos clínicos** y **1 publicación** (un estudio observacional prospectivo sobre trastornos pigmentarios faciales) con relación indirecta a esta predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hidroquinona (el registro no detalla una indicación específica) |
| Nueva Indicación Predicha | Queratosis seborreica |
| Puntaje de Predicción TxGNN | 0,9973 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 14 de 14) |
| Número de Registros Sanitarios | 14 (vigentes: 14) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

La hidroquinona es un inhibidor de la tirosinasa que reduce la síntesis de melanina. Según la sección «Clinical Pharmacology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Hydroquinone (traducción no oficial): «La aplicación tópica de hidroquinona produce una despigmentación reversible de la piel mediante la inhibición de la oxidación enzimática de la tirosina a 3,4-dihidroxifenilalanina (dopa) (Denton, C. et al., 1952)1 y la supresión de otros procesos metabólicos de los melanocitos (Jimbow, K. et al., 1974)2. La exposición a la luz solar o a la luz ultravioleta causará la repigmentación de las zonas despigmentadas (Parrish, L.A. et al., 1978)3.» Texto original en inglés: "Topical application of hydroquinone produces a reversible depigmentation of the skin by inhibition of the enzymatic oxidation of tyrosine to 3,4-dihydroxyphenylalanine (dopa) (Denton, C. et al., 1952)1 and suppression of other melanocyte metabolic processes (Jimbow, K. et al., 1974)2. Exposure to sunlight or ultraviolet light will cause repigmentation of bleached areas (Parrish, L.A. et al., 1978)3." ([DailyMed: Hydroquinone 4% (hydroquinone) prescribing information, Acella Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=595dfc50-ee6f-41b5-ab5b-4c293aee342b), versión del 2026-07-10; consultado el 2026-11-19).

Las lesiones de queratosis seborreica suelen estar hiperpigmentadas, por lo que un agente despigmentante podría aclararlas con fines cosméticos. Sin embargo, esto no trataría la proliferación subyacente de los queratinocitos. El puntaje elevado de TxGNN probablemente refleja características de red compartidas relacionadas con la pigmentación, y no un mecanismo que modifique la enfermedad.

Por lo tanto, la predicción es plausible solo como beneficio sintomático/estético y no como tratamiento de la enfermedad en sí.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para queratosis seborreica.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33046430](https://pubmed.ncbi.nlm.nih.gov/33046430/) | 2021 | Estudio observacional prospectivo | J Plast Reconstr Aesthet Surg | Algoritmo de tratamiento combinado para trastornos pigmentarios faciales en pacientes asiáticos; la mayoría presenta varios trastornos a la vez y no existía un algoritmo definitivo |

---

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 15826 | FILTROQUINONA ® CREMA | CREMA TOPICA | HIDROQUINONA | Vigente |
| 19931579 | TRI-LUMA® CREMA | CREMA TOPICA | COMBINACIONES DE CORTICOSTEROIDES | Vigente |
| 19953067 | BETARRETIN® H CREMA | CREMA TOPICA | HIDROQUINONA | Vigente |
| 20010389 | CREMOQUINONA® | CREMA TOPICA | HIDROQUINONA | Vigente |
| 20038659 | RELIFE SKIN®. | LOCION | HIDROQUINONA | Vigente |

Se muestran 5 de 14 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

- **Posibles contraindicaciones según el grafo de conocimiento (PrimeKG, no provienen del prospecto):** quemadura solar, insuficiencia suprarrenal, enfermedad de Addison, atrofia cutánea, telangiectasia, enfermedad capilar, telangiectasia hemorrágica hereditaria, enfermedad vascular periférica, claudicación vascular intermitente, enfermedad arterial periférica, eccema atópico y dermatitis.
- **Interacciones farmacológicas:** no se encontraron interacciones registradas en la consulta realizada.

Consultar el prospecto para obtener información completa sobre advertencias y contraindicaciones.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia es de nivel L4: no hay ensayos clínicos y la única publicación trata de trastornos pigmentarios en general, no de queratosis seborreica. Además, el mecanismo solo respaldaría un efecto cosmético, no una acción sobre la enfermedad.

<!-- review:begin co-lic-20261105-hydroquinone-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, el único registro sanitario en Colombia está cancelado, y el mecanismo solo respaldaría un efecto cosmético, no una acción sobre la enfermedad." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-hydroquinone-1 -->

**Para avanzar se necesita:**
- Estudios clínicos específicos de hidroquinona en queratosis seborreica que midan resultados clínicos y estéticos
- Obtener y revisar el prospecto (advertencias y contraindicaciones), pues faltan datos de seguridad de la etiqueta
- Datos detallados del mecanismo de acción
- Evaluar la seguridad de uso prolongado y sobre piel con atrofia, dermatitis o telangiectasias, dadas las contraindicaciones señaladas en el grafo de conocimiento

<!-- review:begin co-lic-20261105-hydroquinone-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Aclarar la situación regulatoria en Colombia (registro cancelado; evaluar un nuevo registro o alternativas vigentes) / Evaluar la seguridad de uso prolongado y sobre piel con atrofia, dermatitis o telangiectasias, dadas las contraindicaciones señaladas en el grafo de conocimiento" Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-hydroquinone-2 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "el único registro sanitario en Colombia está cancelado, y" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Aclarar la situación regulatoria en Colombia (registro cancelado; evaluar un nuevo registro o alternativas vigentes)" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Hydroquinone 4% (hydroquinone) prescribing information, Acella Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=595dfc50-ee6f-41b5-ab5b-4c293aee342b) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

