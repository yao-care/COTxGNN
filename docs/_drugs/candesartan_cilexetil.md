---
layout: default
title: Candesartan Cilexetil
parent: Solo Predicción del Modelo (L5)
nav_order: 131
evidence_level: L5
indication_count: 4
monitor_inn: "CANDESARTAN CILEXETIL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
last_modified_at: 2026-11-20
description: "Candesartan Cilexetil: nueva indicación predicha, enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) (nivel de evidencia L5). Indicación original: CANDESARTAN"
---

# Candesartan Cilexetil
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

## Candesartán cilexetilo: antagonista del receptor de angiotensina II (ARA-II) → enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)
{: .text-alpha }

## Resumen en Una Frase

Candesartán cilexetilo es un antagonista del receptor de angiotensina II, comercializado en Colombia bajo registro sanitario local.
El modelo TxGNN predice que podría ser útil para **enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata de una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | CANDESARTAN |
| Nueva Indicación Predicha | enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) |
| Puntaje de Predicción TxGNN | 0,9968 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 4 de 6) |
| Número de Registros Sanitarios | 6 (vigentes: 4) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Candesartan Cilexetil (traducción no oficial): «La angiotensina II se forma a partir de la angiotensina I en una reacción catalizada por la enzima convertidora de angiotensina (ECA, cininasa II). La angiotensina II es el principal agente presor del sistema renina-angiotensina, con efectos que incluyen vasoconstricción, estimulación de la síntesis y liberación de aldosterona, estimulación cardíaca y reabsorción renal de sodio. […] El candesartán bloquea los efectos vasoconstrictores y secretores de aldosterona de la angiotensina II al bloquear selectivamente la unión de la angiotensina II al receptor AT 1 en muchos tejidos, como el músculo liso vascular y la glándula suprarrenal.» Texto original en inglés: "Angiotensin II is formed from angiotensin I in a reaction catalyzed by angiotensin-converting enzyme (ACE, kininase II). Angiotensin II is the principal pressor agent of the renin-angiotensin system, with effects that include vasoconstriction, stimulation of synthesis and release of aldosterone, cardiac stimulation, and renal reabsorption of sodium. […] Candesartan blocks the vasoconstrictor and aldosterone-secreting effects of angiotensin II by selectively blocking the binding of angiotensin II to the AT 1 receptor in many tissues, such as vascular smooth muscle and the adrenal gland." ([DailyMed: Atacand (candesartan cilexetil) prescribing information, ANI Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=94a59260-d2b6-464a-b5b9-bbc599e57e10), versión del 2025-12-22; consultado el 2026-11-19). Por su clase, candesartán cilexetilo bloquea el receptor de angiotensina II, una vía que participa en la regulación de la presión arterial y del tono vascular.

En la nefroesclerosis maligna, la angiotensina II favorece el daño vascular y la hipertensión glomerular. Los ARA-II tienen un papel renoprotector establecido en otras enfermedades renales crónicas, lo que hace mecanísticamente plausible la predicción.

Sin embargo, no se aportaron ensayos ni literatura para esta indicación concreta, por lo que la plausibilidad se basa solo en el razonamiento mecanístico y en el puntaje del modelo. Antes de cualquier avance, debe evaluarse la seguridad renal (hiperpotasemia, lesión renal aguda).

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

## Información de Mercado en Colombia

El estado de mercado en Colombia figura como comercializado. Los registros pueden ser parciales.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19995395 | CANDEPREX® 16 MG TABLETAS | Tableta | CANDESARTAN |

## Consideraciones de Seguridad

- **Contraindicaciones de la literatura de relaciones fármaco-enfermedad (no provienen del prospecto)**: no se listan aquí por no corresponder a texto de etiqueta; consultar el prospecto para la información de seguridad.
- **Interacciones Farmacológicas**: no se encontraron interacciones en la consulta realizada.

Consultar el prospecto para información de seguridad. Para esta indicación en particular, vigilar potasio y función renal.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no cuenta con ensayos clínicos ni publicaciones que estudien directamente la enfermedad renal hipertensiva maligna; solo existe plausibilidad mecanística y un puntaje del modelo (0,9968).

**Para avanzar se necesita:**
- Búsqueda de estudios clínicos o preclínicos que evalúen candesartán en esta enfermedad
- Datos del mecanismo de acción del fármaco
- Obtención y análisis del prospecto aprobado (advertencias y contraindicaciones)
- Evaluación de seguridad renal (hiperpotasemia, lesión renal aguda) en hipertensión maligna

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Atacand (candesartan cilexetil) prescribing information, ANI Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=94a59260-d2b6-464a-b5b9-bbc599e57e10) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

