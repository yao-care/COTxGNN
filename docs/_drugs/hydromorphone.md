---
layout: default
title: Hydromorphone
parent: Solo Predicción del Modelo (L5)
nav_order: 329
evidence_level: L5
indication_count: 6
monitor_inn: "hydromorphone"
predicted_indications: ["pharyngitis", "allergic urticaria", "nasal cavity disease", "acute laryngopharyngitis", "headache disorder", "trigeminal autonomic cephalalgia"]
last_modified_at: 2026-11-24
description: "Hydromorphone: nueva indicación predicha, faringitis (pharyngitis) (nivel de evidencia L5). Indicación original: HIDROMORFONA"
---

# Hydromorphone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Hidromorfona: agonista del receptor opioide mu → faringitis (pharyngitis)
{: .text-alpha }

## Resumen en Una Frase

Hidromorfona es un analgésico opioide que actúa como agonista del receptor opioide mu.
El modelo TxGNN predice que podría ser útil para **faringitis (pharyngitis)**, pero la evidencia directa es muy limitada: solo **3 ensayos clínicos** relacionados con dolor tras amigdalectomía, sin publicaciones que estudien la faringitis en sí.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | HIDROMORFONA |
| Nueva Indicación Predicha | faringitis (pharyngitis) |
| Puntaje de Predicción TxGNN | 0,9981 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 2 de 2) |
| Número de Registros Sanitarios | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Hydromorphone (traducción no oficial): «La hidromorfona es un agonista opioide completo y es relativamente selectiva para el receptor opioide mu, aunque puede unirse a otros receptores opioides a dosis más altas. La principal acción terapéutica de la hidromorfona es la analgesia.» Texto original en inglés: "Hydromorphone is a full opioid agonist and is relatively selective for the mu-opioid receptor, although it can bind to other opioid receptors at higher doses. The principal therapeutic action of hydromorphone is analgesia." ([DailyMed: Dilaudid (hydromorphone hydrochloride) prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9eebd88a-5632-460f-b7b6-26c8a180540d), versión del 2026-07-15; consultado el 2026-11-19). Según la información conocida, la hidromorfona es un agonista del receptor opioide mu con acción analgésica central y periférica, por lo que podría aliviar el dolor faríngeo de forma sintomática.

Los ensayos recuperados estudian el dolor posoperatorio tras amigdalectomía, un modelo de dolor quirúrgico, y no la faringitis infecciosa o inflamatoria. Solo uno de ellos (NCT04230681) involucra a la hidromorfona, como comparador de fentanilo; los otros dos evalúan metadona. Ningún estudio citado aborda directamente la faringitis, por lo que el nivel de evidencia se limita a L5.

El puntaje de 0,9981 es una predicción computacional, no evidencia clínica. Además, los opioides no son tratamiento estándar de la faringitis y sus riesgos (depresión respiratoria, sobre todo en niños) superan el posible beneficio en una condición autolimitada.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04230681](https://clinicaltrials.gov/study/NCT04230681) | Fase 1 temprana | Completado | 189 | Hidromorfona vs fentanilo para control del dolor en niños tras amigdalectomía; evidencia indirecta |
| [NCT05244226](https://clinicaltrials.gov/study/NCT05244226) | Fase 2 | Completado | 66 | Opioides de acción corta (fentanilo/hidromorfona) vs metadona en dolor tras amigdalectomía pediátrica |
| [NCT06576830](https://clinicaltrials.gov/study/NCT06576830) | Fase 4 | Reclutando | 440 | Metadona intraoperatoria en dosis única vs opioides de acción corta en amigdalectomía pediátrica; sin resultados aún |

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 19989418 | HIDROMORFONA CLORHIDRATO 2.5 MG TABLETAS | TABLETA | HIDROMORFONA | Vigente |
| 20008612 | HIDROMORFONA CLORHIDRATO 2 MG/ML | SOLUCION INYECTABLE | HIDROMORFONA | Vigente |

Se muestran los 2 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en relaciones de enfermedad del modelo (no provienen del prospecto)**: insuficiencia hepática, epilepsia, enfermedad renal, hipotiroidismo, enfermedad inflamatoria intestinal, insuficiencia respiratoria, insuficiencia suprarrenal, hiperplasia prostática benigna, estreñimiento, trastornos por consumo de sustancias y dependencia de fármacos, entre otras.
- **Interacciones Farmacológicas**: se registraron 207 interacciones. Entre las de nivel mayor figuran alvimopán, bupropión, morfina y naltrexona. Entre las de nivel moderado: hiosciamina, loperamida, atropina, glicopirronio, cimetidina, naloxona y eluxadolina.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún estudio que evalúe la hidromorfona en la faringitis; los ensayos disponibles tratan dolor posquirúrgico y no son extrapolables. Los riesgos de los opioides superan el beneficio en una condición autolimitada.

**Para avanzar se necesita:**
- Estudios clínicos que evalúen directamente la hidromorfona en faringitis, si hubiera una justificación clínica
- Datos del mecanismo de acción y del prospecto (advertencias y contraindicaciones)
- Evaluación comparativa frente a analgésicos no opioides estándar y análisis de riesgo-beneficio, especialmente en población pediátrica

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Dilaudid (hydromorphone hydrochloride) prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9eebd88a-5632-460f-b7b6-26c8a180540d) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

