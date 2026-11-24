---
layout: default
title: Milrinone
parent: Solo Predicción del Modelo (L5)
nav_order: 445
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
description: "Milrinone: nueva indicación predicha, Alopecia (nivel de evidencia L5). Indicación original: MILRINONA"
monitor_inn: "milrinone"
predicted_indications: ["alopecia", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "headache disorder", "migraine disorder", "migraine with brainstem aura", "trigeminal autonomic cephalalgia", "acute pulmonary heart disease"]
---

# Milrinone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Milrinona: De Insuficiencia Cardiaca Congestiva a Alopecia
{: .text-alpha }

## Resumen en Una Frase

La milrinona es un inhibidor de la fosfodiesterasa 3 (PDE3) de uso intravenoso, utilizado en cardiología para la insuficiencia cardiaca congestiva (el registro sanitario colombiano solo indica el nombre del principio activo, sin detallar la indicación).
El modelo TxGNN predice que podría ser efectiva para **alopecia**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | MILRINONA (el registro no detalla la indicación; uso clínico conocido: insuficiencia cardiaca congestiva) |
| Nueva Indicación Predicha | Alopecia |
| Puntaje de Predicción TxGNN | 0.9991 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 3 de 4) |
| Número de Registros Sanitarios | 4 (vigentes: 3) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

La milrinona inhibe principalmente la PDE3 (isoformas 3A y 3B), con interacción registrada también con PDE2A y PDE5A. Al inhibir la PDE3 aumenta el AMPc en el músculo cardiaco y en el músculo liso vascular, lo que produce efecto inotrópico positivo y vasodilatación (efecto "inodilatador"). Según la sección «Clinical Pharmacology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Milrinone (traducción no oficial): «La milrinona es un inotrópico positivo y vasodilatador, con escasa actividad cronotrópica, de estructura y modo de acción diferentes de los de los glucósidos digitálicos o de las catecolaminas.» Texto original en inglés: "Milrinone is a positive inotrope and vasodilator, with little chronotropic activity different in structure and mode of action from either the digitalis glycosides or catecholamines." ([DailyMed: Milrinone Lactate In Dextrose (milrinone lactate) prescribing information, Gland Pharma Limited](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=838da14b-c070-4c09-b088-99e7c64d9964), versión del 2021-08-25; consultado el 2026-11-19).

La relación entre la indicación original y la alopecia es indirecta. Una hipótesis teórica es que la vasodilatación podría aumentar la perfusión del cuero cabelludo, de forma conceptualmente similar al minoxidil. Sin embargo, esta hipótesis no cuenta con ningún estudio que la respalde, y el puntaje alto del modelo no equivale a evidencia clínica.

Se debe tener cautela: la milrinona es un fármaco de uso hospitalario, por vía inyectable y con riesgos cardiovasculares relevantes. Una enfermedad dermatológica crónica y no mortal como la alopecia tendría una relación beneficio-riesgo poco favorable con una administración sistémica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

<!-- review:begin co-lic-20261105-milrinone-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Los cuatro registros sanitarios están cancelados; actualmente no hay presentaciones vigentes." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 4 registros sanitarios (vigentes: 3); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-milrinone-1 -->

---

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 20003652 | MILRINONA 10 MG / 10 ML SOLUCION INYECTABLE. VIAL POR 10 ML | SOLUCION INYECTABLE | MILRINONA | Vigente |
| 20060004 | MILRINONA 10MG/10ML | SOLUCION INYECTABLE | MILRINONA | Vigente |
| 40198 | COROTROPE® 10 MG | SOLUCION INYECTABLE | MILRINONA | Vigente |
| 20200726 | MILRINONA 10 MG / 10 ML SOLUCION INYECTABLE | SOLUCION INYECTABLE | MILRINONA | Temp. no comerc - Vigente |

Se muestran los 4 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

No se dispone del texto de advertencias y contraindicaciones del prospecto; consultar el prospecto para esa información. Con los datos compilados se puede señalar lo siguiente:

- **Condiciones asociadas a contraindicación según el grafo de conocimiento** (relaciones fármaco-enfermedad de TxGNN/PrimeKG, no texto de prospecto): enfermedad renal, piouréter, trastornos hipotensivos, infarto de miocardio, trombosis coronaria, hemoglobinopatía, paro cardiaco súbito, enfermedad del sistema de conducción cardiaco, estenosis de la válvula pulmonar y miocardiopatía hipertrófica (incluida la familiar).
- **Interacciones farmacológicas** (9 registros en total; las 5 interacciones con otros fármacos son de nivel moderado): amifostina, diatrizoato, anagrelida, ozanimod y procarbazina.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para alopecia es solo computacional (nivel L5): no hay ensayos clínicos ni literatura, el mecanismo propuesto es especulativo y el perfil de seguridad cardiovascular de la milrinona sistémica es poco compatible con esta indicación.

<!-- review:begin co-lic-20261105-milrinone-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción para alopecia es solo computacional (nivel L5): no hay ensayos clínicos ni literatura, el mecanismo propuesto es especulativo y el perfil de seguridad cardiovascular de la milrinona sistémica es poco compatible con esta indicación. Además, actualmente no hay ningún registro sanitario vigente en Colombia." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 4 registros sanitarios (vigentes: 3); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-milrinone-2 -->

**Para avanzar se necesita:**
- Estudios preclínicos (por ejemplo, modelos de folículo piloso o de perfusión del cuero cabelludo) que sustenten la hipótesis de la PDE3.
- Evaluar si una vía tópica o localizada sería viable, ya que la presentación disponible es solo inyectable.
- Obtener y revisar el prospecto oficial para completar la información de advertencias y contraindicaciones.
- Confirmar el estado regulatorio en Colombia; el medicamento está comercializado y tiene 4 registros vigentes de 4.
- Como referencia, otras indicaciones predichas para este fármaco tienen más respaldo que la alopecia, en particular la insuficiencia cardiaca congestiva (nivel L2, "Proceed with Guardrails") y el síndrome de vasoconstricción cerebral reversible asociado a cefalea (reportes de casos). Podrían priorizarse antes que la alopecia.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Los cuatro registros sanitarios están cancelados; actualmente no hay presentaciones vigentes" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Además, actualmente no hay ningún registro sanitario vigente en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Milrinone Lactate In Dextrose (milrinone lactate) prescribing information, Gland Pharma Limited](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=838da14b-c070-4c09-b088-99e7c64d9964) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

