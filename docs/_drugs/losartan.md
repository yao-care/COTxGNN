---
layout: default
title: Losartan
parent: Solo Predicción del Modelo (L5)
nav_order: 412
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-24
description: "Losartan: nueva indicación predicha, Enfermedad renal hipertensiva maligna (nivel de evidencia L5). Indicación original: Losartán"
monitor_inn: "LOSARTAN"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "Prinzmetal angina", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "brain small vessel disease 1 with or without ocular anomalies"]
---

# Losartan
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

## Losartán: De Hipertensión (registro sanitario vigente) a Enfermedad Renal Hipertensiva Maligna
{: .text-alpha }

## Resumen en Una Frase

Losartán es un antagonista del receptor AT1 de la angiotensina II, registrado en Colombia como losartán solo y combinado con diuréticos, y usado de forma establecida contra la hipertensión.
El modelo TxGNN predice que podría ser efectivo para **enfermedad renal hipertensiva maligna**, pero actualmente no hay ensayos clínicos y solo **1 publicación** (un estudio en modelo animal) respalda esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Losartán (el registro sanitario solo indica "Losartán"; no detalla la enfermedad) |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna |
| Puntaje de Predicción TxGNN | 0.9973 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 20) |
| Número de Registros Sanitarios | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Losartan (traducción no oficial): «La angiotensina II [formada a partir de la angiotensina I en una reacción catalizada por la enzima convertidora de angiotensina (ECA, cininasa II)] es un potente vasoconstrictor, la principal hormona vasoactiva del sistema renina-angiotensina y un componente importante en la fisiopatología de la hipertensión. También estimula la secreción de aldosterona por la corteza suprarrenal. […] El losartán y su principal metabolito activo bloquean los efectos vasoconstrictores y secretores de aldosterona de la angiotensina II al bloquear selectivamente la unión de la angiotensina II al receptor AT 1 presente en muchos tejidos (p. ej., músculo liso vascular, glándula suprarrenal).» Texto original en inglés: "Angiotensin II [formed from angiotensin I in a reaction catalyzed by angiotensin converting enzyme (ACE, kininase II)] is a potent vasoconstrictor, the primary vasoactive hormone of the renin-angiotensin system, and an important component in the pathophysiology of hypertension. It also stimulates aldosterone secretion by the adrenal cortex. […] Losartan and its principal active metabolite block the vasoconstrictor and aldosterone-secreting effects of angiotensin II by selectively blocking the binding of angiotensin II to the AT 1 receptor found in many tissues, (e.g., vascular smooth muscle, adrenal gland)." ([DailyMed: Losartan Potassium 50 Mg (losartan potassium) prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=498f26a1-5030-4f9b-9599-07d50e912d41), versión del 2026-09-15; consultado el 2026-11-19). Según la información conocida, losartán es un bloqueador del receptor AT1 de la angiotensina II. Su eficacia en hipertensión y su efecto protector sobre el riñón están bien establecidos, y mecanísticamente podría ser aplicable a la enfermedad renal hipertensiva maligna.

La única publicación disponible (PMID 30809002) describe, en un modelo de rata, que la angiotensina II y la vía NF-κB participan en la nefroesclerosis hipertensiva maligna. Esto es coherente con bloquear el receptor AT1, pero el respaldo es solo preclínico.

La novedad del reposicionamiento es baja, porque losartán ya se usa en hipertensión. Además, no se ha verificado que la indicación aprobada cubra este fenotipo grave.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [30809002](https://pubmed.ncbi.nlm.nih.gov/30809002/) | 2019 | Estudio en modelo animal | Hypertension Research | En ratas, la angiotensina II y el sistema NF-κB participan en la nefroesclerosis hipertensiva maligna; la uninefrectomía con sobrecarga de sal agravó la hipertensión y el daño renal |

---

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 19900484 | SATOREN ® H TABLETAS | TABLETA | LOSARTAN Y DIURETICOS | Vigente |
| 19908404 | HYZAAR® FORTE 100 / 25MG | TABLETA CUBIERTA CON PELICULA | LOSARTAN Y DIURETICOS | Vigente |
| 19929989 | ARAPRES-ANZG | TABLETA CUBIERTA CON PELICULA | LOSARTAN | Vigente |
| 19931835 | LOSARTAN POTÁSICO 50MG TABLETAS RECUBIERTAS | TABLETA RECUBIERTA | LOSARTAN | Vigente |
| 19932984 | LOSARTAN 50 MG | TABLETA CUBIERTA CON PELICULA | LOSARTAN | Vigente |

Se muestran 5 de al menos 20 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes. Los datos de este informe solo incluyen parte de los registros.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no según el prospecto)**: pancreatitis, enfermedad hepática, enfermedad de la vesícula biliar, lupus eritematoso sistémico (incluido el pediátrico), deficiencia de potasio, diabetes mellitus, cetoacidosis diabética, hiperuricemia, trastornos hipotensivos, hiperparatiroidismo, osteítis fibrosa, coma hepático, encefalopatía hepática, ictericia neonatal, anuria, gota, hipercalcemia, nefrocalcinosis, trastornos del metabolismo del fósforo, obstrucción de la arteria renal y función renal deteriorada.
- **Interacciones farmacológicas**: se encontraron 100 interacciones. Las de nivel **mayor** incluyen citrato de potasio y bicarbonato de potasio (riesgo de hiperpotasemia). Las de nivel **moderado** incluyen corticoides (hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida), inhibidores de SGLT2 (canagliflozina, dapagliflozina, empagliflozina), insulinas, ácido acetilsalicílico, morfina, bupropión, aprepitant y dronabinol.
- **Consideración específica**: para la hipertensión renovascular, la estenosis bilateral de la arteria renal es un riesgo reconocido de los ARA-II (lesión renal aguda), por lo que se requeriría monitoreo cuidadoso.

Para las advertencias del prospecto, consultar el prospecto del producto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto, pero solo la respalda un estudio en animales (L5), sin ensayos clínicos. Además, no hay datos de mecanismo ni de seguridad según el prospecto.

<!-- review:begin co-lic-20261105-losartan-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, los dos registros sanitarios en Colombia están cancelados, y no hay datos de mecanismo ni de seguridad según el prospecto." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-losartan-1 -->

**Para avanzar se necesita:**
- Datos clínicos en humanos (ensayos o estudios observacionales) de losartán en enfermedad renal hipertensiva maligna
- Datos detallados del mecanismo de acción (MOA)
- Advertencias y contraindicaciones del prospecto de INVIMA
- Confirmar la situación regulatoria
- Plan de monitoreo de función renal y potasio, sobre todo si hay estenosis de arteria renal

<!-- review:begin co-lic-20261105-losartan-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Confirmar la situación regulatoria, dado que no hay registros vigentes en Colombia" Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-losartan-2 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "los dos registros sanitarios en Colombia están cancelados, y" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "dado que no hay registros vigentes en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Losartan Potassium 50 Mg (losartan potassium) prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=498f26a1-5030-4f9b-9599-07d50e912d41) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

