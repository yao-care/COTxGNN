---
layout: default
title: Hydromorphone
parent: Evidencia Moderada (L3-L4)
nav_order: 329
evidence_level: L4
indication_count: 6
last_modified_at: 2026-10-14
description: "Hydromorphone: nueva indicación predicha, Faringitis (nivel de evidencia L4). Indicación original: HIDROMORFONA"
monitor_inn: "hydromorphone"
predicted_indications: ["pharyngitis", "allergic urticaria", "nasal cavity disease", "acute laryngopharyngitis", "headache disorder", "trigeminal autonomic cephalalgia"]
---

# Hydromorphone
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **6** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Hidromorfona: De Hidromorfona (indicación no detallada en el registro) a Faringitis

## Resumen en Una Frase

La hidromorfona es un opioide agonista del receptor mu que en Colombia contó con registros sanitarios como analgésico, aunque el texto de indicación registrado solo dice "HIDROMORFONA".
El modelo TxGNN predice que podría ser efectiva para **faringitis**, con **3 ensayos clínicos** (solo uno con hidromorfona, en dolor posoperatorio tras amigdalectomía) y **ninguna publicación** que respalden directamente esta dirección.
La evidencia es indirecta y débil, por lo que la predicción debe considerarse una hipótesis computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | HIDROMORFONA (el registro no detalla una indicación clínica específica) |
| Nueva Indicación Predicha | Faringitis |
| Puntaje de Predicción TxGNN | 99.81% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este reporte. Según la información conocida, la hidromorfona es un agonista del receptor opioide mu con acción analgésica central y periférica, y su eficacia como analgésico potente está bien establecida.

La relación con la faringitis es solo de tipo sintomático: un analgésico opioide podría aliviar el dolor faríngeo. Sin embargo, los ensayos recuperados no estudian faringitis infecciosa o inflamatoria, sino el dolor posquirúrgico tras amigdalectomía, que es un modelo de dolor quirúrgico distinto.

El puntaje TxGNN (99.81%) es una predicción computacional, no evidencia clínica. Además, los opioides no son tratamiento estándar de la faringitis, una condición generalmente autolimitada, y sus riesgos (en especial la depresión respiratoria en niños) superan el posible beneficio.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04230681](https://clinicaltrials.gov/study/NCT04230681) | Fase 1 temprana | Completado | 189 | Hidromorfona vs. fentanilo para el control del dolor en niños sometidos a amigdalectomía; evidencia indirecta (dolor perioperatorio) |
| [NCT05244226](https://clinicaltrials.gov/study/NCT05244226) | Fase 2 | Completado | 66 | Estudio piloto doble ciego de metadona frente a opioides de acción corta (fentanilo/hidromorfona) en dolor tras amigdalectomía pediátrica; el fármaco evaluado es metadona |
| [NCT06576830](https://clinicaltrials.gov/study/NCT06576830) | Fase 4 | Reclutando | 440 | Metadona intraoperatoria en dosis única frente a opioides de acción corta en amigdalectomía pediátrica; sin resultados aún |

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para faringitis.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19989418 | Hidromorfona Clorhidrato 2.5 mg tabletas | Tableta | HIDROMORFONA (cancelado) |
| 20008612 | Hidromorfona Clorhidrato 2 mg/ml | Solución inyectable | HIDROMORFONA (cancelado) |

---

## Consideraciones de Seguridad

- **Contraindicaciones sugeridas por el grafo de conocimiento** (relaciones fármaco-enfermedad, no texto de prospecto): insuficiencia hepática y renal, epilepsia, insuficiencia respiratoria, hipotiroidismo y mixedema, insuficiencia suprarrenal (incluida enfermedad de Addison e hiperplasia suprarrenal congénita), enfermedad inflamatoria intestinal y colitis ulcerosa, hiperplasia prostática benigna, trastornos hipotensivos, paro cardíaco súbito, enfermedades de la conducción cardíaca, enfermedad de la vesícula biliar, estreñimiento, deficiencia de butirilcolinesterasa, y trastornos por uso o dependencia de sustancias.
- **Interacciones farmacológicas**: se identificaron 207 interacciones. Entre las de gravedad mayor figuran alvimopán, bupropión, morfina y naltrexona. Entre las moderadas se encuentran anticolinérgicos (atropina, hioscina, glicopirronio, diciclomina, trospio), loperamida, naloxona, cimetidina, dronabinol, nabilona y varios antieméticos (dolasetrón, palonosetrón).

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia se limita a ensayos de dolor posoperatorio tras amigdalectomía, no a faringitis, y no hay literatura de respaldo. Además, el perfil de riesgo de un opioide es desfavorable para una condición autolimitada y los registros sanitarios en Colombia están cancelados.

**Para avanzar se necesita:**
- Datos del mecanismo de acción confirmados (por ejemplo, desde DrugBank)
- Prospecto de INVIMA con advertencias y contraindicaciones oficiales
- Evidencia clínica directa en faringitis, no en dolor quirúrgico
- Evaluación de la viabilidad regulatoria, dado que ambos registros están cancelados y se trata de una sustancia controlada

---

### Nota sobre otras indicaciones predichas

Ninguna otra indicación mejora el panorama:
- **Cefalea / migraña (puntaje 99.65%, L3):** es la que tiene más respaldo, con un ensayo de Fase 4 completado que comparó hidromorfona con proclorperazina más difenhidramina en urgencias (NCT02389829). Sin embargo, las guías de la American Headache Society desaconsejan el uso rutinario de opioides en migraña. Se sugiere evaluarla como línea de investigación secundaria.
- **Urticaria alérgica, enfermedad de la cavidad nasal, laringofaringitis aguda y cefalalgia trigémino-autonómica:** solo predicción computacional (L5), sin ensayos ni literatura. En urticaria, los opioides pueden liberar histamina y empeorar el cuadro.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

