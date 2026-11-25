---
layout: default
title: Isosorbide Dinitrate
parent: Solo Predicción del Modelo (L5)
nav_order: 358
evidence_level: L5
indication_count: 10
monitor_inn: "isosorbide dinitrate"
predicted_indications: ["alopecia", "congenital hypotrichosis milia", "hypotrichosis simplex of the scalp", "pulmonary hypertension", "diffuse alopecia areata", "vascular disease", "hypertrichosis (disease)", "kyphoscoliotic heart disease", "visceral calciphylaxis", "arterial thoracic outlet syndrome"]
last_modified_at: 2026-11-25
description: "Isosorbide Dinitrate: nueva indicación predicha, Alopecia (nivel de evidencia L5). Indicación original: Isosorbida dinitrato"
---

# Isosorbide Dinitrate
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Dinitrato de isosorbida: De "Isosorbida dinitrato" (indicación no detallada en el registro) a Alopecia
{: .text-alpha }

## Resumen en Una Frase

El dinitrato de isosorbida es un nitrato vasodilatador que cuenta con un registro sanitario vigente en Colombia (INVIMA), cuyo texto solo menciona el nombre del principio activo y no detalla la indicación.
El modelo TxGNN predice que podría ser efectivo para **alopecia**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Isosorbida dinitrato (el registro solo indica el principio activo, sin detalle de indicación) |
| Nueva Indicación Predicha | Alopecia |
| Puntaje de Predicción TxGNN | 0.9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 2) |
| Número de Registros Sanitarios | 2 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para hydralazine hydrochloride and isosorbide dinitrate (combinación que contiene Isosorbide Dinitrate) (traducción no oficial): «El dinitrato de isosorbida es un vasodilatador que actúa tanto sobre las arterias como sobre las venas.» Texto original en inglés: "Isosorbide dinitrate is a vasodilator affecting both arteries and veins." ([DailyMed: Bidil (hydralazine hydrochloride and isosorbide dinitrate) prescribing information, Azurity Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e1e63cd5-d1e4-4af5-bad5-1ad41ea46b00), versión del 2025-11-30; consultado el 2026-11-19). Según la información conocida, el dinitrato de isosorbida es un nitrato orgánico que libera óxido nítrico y relaja el músculo liso vascular. Sus registros en Colombia corresponden a tabletas (sublingual y oral) de un solo principio activo.

<!-- review:begin co-lic-20261125-isosorbide_dinitrate-1 -->

> **Corrección de revisión (2026-11-25)**: Texto original: "Su registro en Colombia corresponde a una tableta sublingual de un solo principio activo." Corregido según los datos del INVIMA: además de la tableta sublingual hay un registro de tableta oral (ISOCORD COMPRIMIDOS). Las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261125-isosorbide_dinitrate-1 -->

La única hipótesis que vincula el fármaco con la alopecia es especulativa: la vasodilación mediada por óxido nítrico podría mejorar la perfusión del cuero cabelludo. Esta inferencia no tiene respaldo en estudios clínicos ni en literatura recuperada.

El puntaje de 0.9999 proviene únicamente del modelo y no equivale a evidencia clínica. No se pudo establecer una similitud formal entre la indicación original y la alopecia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 37246 | ISOCORD ® SUBLINGUAL | TABLETA SUBLINGUAL | ISOSORBIDE DINITRATO | Vigente |
| 37247 | ISOCORD COMPRIMIDOS | TABLETA | ISOSORBIDE DINITRATO | Temp. no comerc - Vigente |

Se muestran los 2 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

<!-- review:begin co-lic-20261124b-isosorbide_dinitrate-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "La lista puede ser parcial: los datos reportan al menos un registro." Eliminado: advertía que la lista de registros podría ser parcial. La tabla de Información de Mercado en Colombia se genera a partir de los datos del INVIMA (Código Único de Medicamentos, datos al 2026-11-23) e indica cuántos registros muestra del total. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261124b-isosorbide_dinitrate-1 -->

## Consideraciones de Seguridad

- **Contraindicaciones registradas en el grafo de conocimiento** (no provienen del texto del prospecto): trastorno hipotensivo, miocardiopatía hipertrófica, acetilación lenta, enfermedad coronaria, trastornos cerebrovasculares y accidente cerebrovascular, infarto cerebral, infarto de miocardio, trombosis coronaria, hemoglobinopatía, anemias, hipertiroidismo, enfermedad de Graves, tirotoxicosis, pseudotumor cerebral, hipertensión intracraneal, hemorragia intracerebral y síndrome de Rowell.
- **Interacciones farmacológicas**: se identificaron 141 interacciones. Entre las principales, de nivel moderado, están bupropión, morfina, opio, dronabinol, nabilona, sapropterina, rosiglitazona y los inhibidores de SGLT2 (canagliflozina, dapagliflozina, empagliflozina y ertugliflozina). El omeprazol figura como interacción menor.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún ensayo clínico ni publicación que estudie el dinitrato de isosorbida en alopecia, por lo que la predicción queda en nivel L5. Además, el vínculo mecanístico propuesto es especulativo.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y del prospecto de INVIMA (advertencias y contraindicaciones).
- Estudios preclínicos o exploratorios que evalúen la perfusión folicular y el efecto del fármaco en alopecia.
- Evaluar la viabilidad de una vía de administración adecuada.
- Considerar otras indicaciones predichas en los mismos datos que cuentan con más estudios, como la hipertensión pulmonar y la enfermedad vascular, antes de priorizar la alopecia.

<!-- review:begin co-lic-20261125-isosorbide_dinitrate-2 -->

> **Corrección de revisión (2026-11-25)**: Texto original: "Evaluar la viabilidad de una vía de administración adecuada, ya que la única forma registrada es sublingual." Corregido según los datos del INVIMA: la forma sublingual no es la única registrada (hay también tableta oral); se quitó la premisa. Las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261125-isosorbide_dinitrate-2 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Bidil (hydralazine hydrochloride and isosorbide dinitrate) prescribing information, Azurity Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e1e63cd5-d1e4-4af5-bad5-1ad41ea46b00) |
| 2026-11-24 | Eliminado: "La lista puede ser parcial: los datos reportan al menos un registro." | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-25 | «Su registro en Colombia corresponde a una tableta sublingual» → «Sus registros en Colombia corresponden a tabletas (sublingual y oral)» | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-25 | «adecuada, ya que la única forma registrada es sublingual» → «adecuada» | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

