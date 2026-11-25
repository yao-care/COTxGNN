---
layout: default
title: Nebivolol
parent: Solo Predicción del Modelo (L5)
nav_order: 464
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-25
monitor_inn: "nebivolol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
description: "Nebivolol: nueva indicación predicha, Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) (nivel de evidencia L5). Indicación original: NEBIVOLOL"
---

# Nebivolol
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

## Nebivolol: Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)
{: .text-alpha }

## Resumen en Una Frase

Nebivolol es un betabloqueante selectivo beta-1 con efecto vasodilatador mediado por óxido nítrico, registrado en Colombia en tabletas orales (por ejemplo, NABILA® 10 mg), cuyo texto de indicación registrado no detalla la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **enfermedad renal hipertensiva maligna**, pero sin **ningún ensayo clínico** ni **publicaciones** directamente relacionadas con esta indicación.
La predicción se apoya únicamente en el modelo computacional (nivel de evidencia L5).

<!-- review:begin co-lic-20261105-nebivolol-1 -->

> **Corrección de revisión (2026-11-25)**: Texto original: "Nebivolol es un betabloqueante selectivo beta-1 con efecto vasodilatador mediado por óxido nítrico, registrado en Colombia como tableta oral (NABILA® 10 mg), aunque el registro sanitario consta como cancelado y no detalla la indicación aprobada." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Actualizado el 2026-11-25: se reformuló el texto que quedó tras la eliminación para que la frase se lea completa. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-nebivolol-1 -->

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | NEBIVOLOL |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) |
| Puntaje de Predicción TxGNN | 0.9942 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 11 de 13) |
| Número de Registros Sanitarios | 13 (vigentes: 11) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Nebivolol (traducción no oficial): «El mecanismo de acción de la respuesta antihipertensiva de BYSTOLIC no se ha establecido de forma definitiva. Entre los posibles factores que pueden estar implicados se incluyen: disminución de la frecuencia cardíaca, disminución de la contractilidad miocárdica, disminución del flujo simpático tónico hacia la periferia desde los centros vasomotores cerebrales, supresión de la actividad de la renina y vasodilatación y disminución de la resistencia vascular periférica.» Texto original en inglés: "The mechanism of action of the antihypertensive response of BYSTOLIC has not been definitively established. Possible factors that may be involved include: decreased heart rate, decreased myocardial contractility, diminution of tonic sympathetic outflow to the periphery from cerebral vasomotor centers, suppression of renin activity and vasodilation and decreased peripheral vascular resistance." ([DailyMed: Bystolic (nebivolol hydrochloride) prescribing information, Allergan, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8b8ad213-1dc8-454e-a524-075685c0e1a8), versión del 2024-08-01; consultado el 2026-11-19). Según la información conocida, nebivolol es un betabloqueante selectivo beta-1 que además activa la óxido nítrico sintasa endotelial (eNOS), lo que produce vasodilatación. Esto da un fundamento plausible para un efecto hipotensor y, de forma teórica, renoprotector.

La relación con la indicación original es indirecta: el registro local solo menciona el nombre del principio activo, sin texto de indicación. Por su clase farmacológica, el uso esperado es en enfermedades cardiovasculares como la hipertensión, por lo que una enfermedad hipertensiva con compromiso renal es cercana en lo conceptual.

Sin embargo, la hipertensión maligna con afectación renal es una emergencia que normalmente se maneja con fármacos intravenosos, por lo que nebivolol oral no tiene un papel establecido. El puntaje alto del modelo (0.9942) no cuenta con validación clínica.

Otras predicciones del modelo (con el mismo nivel de evidencia bajo) fueron: hipertensión renovascular maligna (0.9942), hipertensión pulmonar por enfermedad pulmonar o hipoxia (0.9939, nivel L4 por literatura preclínica indirecta), hipertensión pulmonar de mecanismo multifactorial poco claro (0.9939) y síndrome de Braddock (0.9914, sin vínculo mecanístico identificable).

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

<!-- review:begin co-lic-20261105-nebivolol-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "El fabricante es MONTE VERDE S.A. No hay registros vigentes en el país." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-nebivolol-2 -->

---

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 19915315 | NEBILET® COMPRIMIDOS 5 MG | TABLETA | NEBIVOLOL | Vigente |
| 20001377 | NABILA® 5 MG COMPRIMIDOS | COMPRIMIDO | NEBIVOLOL | Vigente |
| 20009025 | NEVITEN® 5 MG TABLETAS | TABLETA | NEBIVOLOL | Vigente |
| 20009035 | NABILA® 10 MG COMPRIMIDOS | TABLETA | NEBIVOLOL | Vigente |
| 20009036 | NABILA® 2.5 MG COMPRIMIDOS | TABLETA | NEBIVOLOL | Vigente |

Se muestran 5 de 13 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** insuficiencia hepática, enfermedad hepática, enfermedad de la vesícula biliar, diabetes mellitus, cetoacidosis diabética, enfermedad vascular periférica, claudicación intermitente, enfermedad arterial periférica, hipoglucemia, bloqueo auriculoventricular, enfermedad bronquial, síndrome del seno enfermo (incluida su forma familiar).
- **Interacciones farmacológicas:** se identificaron 174 interacciones. Entre las listadas, la mayoría son de nivel moderado: epinefrina, hidrocortisona, hiosciamina, bupropión, triamcinolona, morfina, atropina, dexametasona, lorcaserina, betametasona, fosfato de calcio, budesonida, glicopirronio, acetato de calcio, canagliflozina, clorpropamida, dapagliflozina y diciclomina. Son de nivel menor el ácido acetilsalicílico y el óxido de magnesio.
- Los betabloqueantes requieren cautela en enfermedad pulmonar o hipoxia y en hipertensión pulmonar arterial, por el posible deterioro de la función del ventrículo derecho.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción solo se sustenta en el modelo TxGNN, sin ensayos clínicos ni literatura directa. Además, la hipertensión maligna con compromiso renal se trata con agentes intravenosos.

<!-- review:begin co-lic-20261105-nebivolol-3 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, la hipertensión maligna con compromiso renal se trata con agentes intravenosos, y el único registro sanitario local está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-nebivolol-3 -->

**Para avanzar se necesita:**
- Datos del mecanismo de acción confirmados (por ejemplo, desde DrugBank).
- Prospecto del INVIMA con advertencias y contraindicaciones, que hoy no están disponibles y bloquean el análisis de seguridad.
- Estudios clínicos o literatura específicos de nebivolol en enfermedad renal hipertensiva maligna.
- Evaluación de compatibilidad de vía de administración (oral frente a la vía intravenosa que requiere la emergencia hipertensiva).
- Aclarar la situación regulatoria en Colombia.

<!-- review:begin co-lic-20261105-nebivolol-4 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Aclarar la situación regulatoria en Colombia, dado que no hay registros vigentes." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-nebivolol-4 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-25 | «Nebivolol es un betabloqueante selectivo beta-1 con efecto v…» → «Nebivolol es un betabloqueante selectivo beta-1 con efecto v…» | Corregido (revisado el 2026-11-25; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "El fabricante es MONTE VERDE S.A. No hay registros vigentes en el país" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "y el único registro sanitario local está cancelado" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "dado que no hay registros vigentes" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Bystolic (nebivolol hydrochloride) prescribing information, Allergan, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8b8ad213-1dc8-454e-a524-075685c0e1a8) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

