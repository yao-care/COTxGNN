---
layout: default
title: Irbesartan
parent: Solo Predicción del Modelo (L5)
nav_order: 355
evidence_level: L5
indication_count: 3
monitor_inn: "IRBESARTAN"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism"]
last_modified_at: 2026-11-20
description: "Irbesartan: nueva indicación predicha, enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) (nivel de evidencia L5). Indicación original: IRBESARTAN"
---

# Irbesartan
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

## Irbesartán: antagonista del receptor AT1 de angiotensina II → enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)
{: .text-alpha }

## Resumen en Una Frase

Irbesartán es un antagonista del receptor de angiotensina II tipo 1 (AT1) que cuenta con registro sanitario local en Colombia.
El modelo TxGNN predice que podría ser efectivo para **enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden directamente esta predicción; se trata solo de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | IRBESARTAN |
| Nueva Indicación Predicha | enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) |
| Puntaje de Predicción TxGNN | 0,9931 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 19) |
| Número de Registros Sanitarios | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Irbesartan (traducción no oficial): «La angiotensina II es un potente vasoconstrictor que se forma a partir de la angiotensina I en una reacción catalizada por la enzima convertidora de angiotensina (ECA, cininasa II). La angiotensina II es la principal hormona vasoactiva del sistema renina-angiotensina y un componente importante de la fisiopatología de la hipertensión. […] El irbesartán bloquea los efectos vasoconstrictores y secretores de aldosterona de la angiotensina II al unirse selectivamente al receptor AT 1 de la angiotensina II, presente en muchos tejidos (p. ej., músculo liso vascular, glándula suprarrenal).» Texto original en inglés: "Angiotensin II is a potent vasoconstrictor formed from angiotensin I in a reaction catalyzed by angiotensin-converting enzyme (ACE, kininase II). Angiotensin II is the primary vasoactive hormone of the renin-angiotensin system, and an important component in the pathophysiology of hypertension. […] Irbesartan blocks the vasoconstrictor and aldosterone-secreting effects of angiotensin II by selectively binding to the AT 1 angiotensin II receptor found in many tissues (e.g., vascular smooth muscle, adrenal gland)." ([DailyMed: Avapro (irbesartan) prescribing information, Sanofi-Aventis U.S. LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7885b2a8-be4e-48ab-8113-4e6ab791eb98), versión del 2026-08-24; consultado el 2026-11-19). Según la información conocida, irbesartán es un bloqueador del receptor AT1 de angiotensina II, con efectos antihipertensivos y renoprotectores establecidos.

El bloqueo del sistema renina-angiotensina es biológicamente plausible en la lesión renal de origen hipertensivo, y el puntaje elevado del modelo (0,9931) refleja esa cercanía con el uso conocido del fármaco.

Sin embargo, no se aportaron ensayos clínicos ni literatura sobre este fenotipo específico. Además, la hipertensión maligna es una emergencia aguda que suele manejarse con fármacos parenterales de acción rápida, por lo que la monoterapia oral con un ARA-II difícilmente sería el tratamiento principal.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20048718 | CORIONAL® 300 MG TABLETAS RECUBIERTAS | Tableta recubierta | IRBESARTAN |

La lista de registros puede ser parcial.

## Consideraciones de Seguridad

- **Contraindicaciones o condiciones de precaución registradas en bases de datos de relaciones fármaco-enfermedad (no provienen del texto del prospecto)**: pancreatitis, angioedema (incluidas formas adquirida, hereditaria y asociada a bloqueadores del sistema renina-angiotensina-aldosterona), lupus eritematoso sistémico, miopatía y enfermedades musculares, parálisis periódica familiar, deficiencia de potasio, diabetes mellitus y cetoacidosis diabética, hipotensión, hiperparatiroidismo, encefalopatía hepática, anuria, gota, hipercalcemia, nefrocalcinosis, obstrucción de la arteria renal y rabdomiólisis.
- **Interacciones Farmacológicas** (100 interacciones registradas; se muestran las principales):
  - Mayor: citrato de potasio, bicarbonato de potasio.
  - Moderada: hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida, ácido acetilsalicílico, morfina, bupropión, aprepitant, canagliflozina, dapagliflozina, empagliflozina, insulinas (aspart, degludec), dronabinol, ácido picosulfúrico, sulfato de sodio y polietilenglicol con electrolitos.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto, pero no existe ningún estudio clínico ni publicación que evalúe directamente esta enfermedad, por lo que el nivel de evidencia es L5. Además, el contexto de emergencia hipertensiva limita la plausibilidad de un tratamiento oral.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y del prospecto (advertencias y contraindicaciones) de las autoridades sanitarias.
- Revisión de literatura clínica específica sobre ARA-II en nefroesclerosis hipertensiva maligna.
- Evaluación de la viabilidad de la vía oral frente al manejo habitual de la emergencia hipertensiva.
- Estudios observacionales o ensayos que evalúen directamente esta indicación.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Avapro (irbesartan) prescribing information, Sanofi-Aventis U.S. LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7885b2a8-be4e-48ab-8113-4e6ab791eb98) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

