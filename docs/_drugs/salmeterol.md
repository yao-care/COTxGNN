---
layout: default
title: Salmeterol
parent: Solo Predicción del Modelo (L5)
nav_order: 580
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-20
monitor_inn: "SALMETEROL"
predicted_indications: ["respiratory malformation", "Rienhoff syndrome", "atopic eczema"]
description: "Salmeterol: nueva indicación predicha, malformación respiratoria (respiratory malformation) (nivel de evidencia L5). Indicación original: SALMETEROL Y FLUTICASONA"
---

# Salmeterol
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

## Salmeterol: malformación respiratoria (respiratory malformation)
{: .text-alpha }

## Resumen en Una Frase

Salmeterol es un broncodilatador agonista beta2 de acción prolongada, registrado en Colombia en productos inhalados combinados con fluticasona.
El modelo TxGNN predice que podría ser útil para **malformación respiratoria (respiratory malformation)**, pero actualmente no hay estudios que evalúen directamente esta enfermedad: solo hay 2 ensayos clínicos y 8 publicaciones de condiciones relacionadas (fibrosis quística, EPOC, asma, discinesia ciliar), por lo que la evidencia es muy limitada.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | SALMETEROL Y FLUTICASONA |
| Nueva Indicación Predicha | malformación respiratoria (respiratory malformation) |
| Puntaje de Predicción TxGNN | 0.9991 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 19 de 20) |
| Número de Registros Sanitarios | 20 (vigentes: 19) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Salmeterol (traducción no oficial): «El salmeterol es un LABA selectivo. Los estudios in vitro muestran que el salmeterol es al menos 50 veces más selectivo por los adrenorreceptores beta 2 que el albuterol. Aunque los adrenorreceptores beta 2 son los receptores adrenérgicos predominantes en el músculo liso bronquial y los adrenorreceptores beta 1 son los receptores predominantes en el corazón, también existen adrenorreceptores beta 2 en el corazón humano, que constituyen entre el 10% y el 50% del total de adrenorreceptores beta.» Texto original en inglés: "Salmeterol is a selective LABA. In vitro studies show salmeterol to be at least 50 times more selective for beta 2 -adrenoceptors than albuterol. Although beta 2 -adrenoceptors are the predominant adrenergic receptors in bronchial smooth muscle and beta 1 -adrenoceptors are the predominant receptors in the heart, there are also beta 2 -adrenoceptors in the human heart comprising 10% to 50% of the total beta-adrenoceptors." ([DailyMed: Serevent Diskus (salmeterol xinafoate) prescribing information, GlaxoSmithKline LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=12d9728e-6b5c-4aee-bfb0-745e542ed2e4), versión del 2022-10-10; consultado el 2026-11-19). Por su clase farmacológica, salmeterol es un agonista beta2 de acción prolongada que produce broncodilatación sostenida.

"Malformación respiratoria" es una categoría muy amplia, sin un vínculo mecanístico específico. Se podrían plantear posibles efectos sobre la función ciliar o el alivio de la obstrucción de la vía aérea en condiciones como la fibrosis quística o la discinesia ciliar, pero la evidencia es indirecta.

El puntaje alto probablemente refleja la cercanía de esta categoría con las enfermedades de la vía aérea, más que un mecanismo demostrado. Por ello, la predicción debe considerarse una hipótesis de investigación.

## Evidencia de Ensayos Clínicos

Ningún ensayo estudia directamente la malformación respiratoria.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00005110](https://clinicaltrials.gov/study/NCT00005110) | N/A | Suspendido | No reportada | Salmeterol vs. albuterol o placebo, dos veces al día durante 6 meses, en fibrosis quística; señal relacionada pero indirecta |
| [NCT01681979](https://clinicaltrials.gov/study/NCT01681979) | N/A | Completado | 1 | Resultados adversos del tratamiento del asma en el embarazo; poco informativo para esta predicción |

## Evidencia de Literatura

Ninguna publicación estudia directamente la malformación respiratoria.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [34902004](https://pubmed.ncbi.nlm.nih.gov/34902004/) | 2022 | ECA | JAMA Pediatrics | Corticosteroides inhalados solos o con agonistas beta2 de acción prolongada para la función pulmonar reducida en niños nacidos prematuros |
| [15293609](https://pubmed.ncbi.nlm.nih.gov/15293609/) | 2004 | ECA | Eur Respir J | Efecto de salmeterol sobre la respuesta ventilatoria al ejercicio en EPOC (23 pacientes, diseño cruzado) |
| [22608352](https://pubmed.ncbi.nlm.nih.gov/22608352/) | 2012 | Cohorte | Respiratory Medicine | Reducción de la frecuencia de batido ciliar nasal en sujetos con EPOC |
| [20703071](https://pubmed.ncbi.nlm.nih.gov/20703071/) | 2010 | Reporte de caso | Arerugi | Caso de discinesia ciliar primaria tratada inicialmente como asma |
| [20528601](https://pubmed.ncbi.nlm.nih.gov/20528601/) | 2010 | Revisión | J Asthma | Revisión de budesonida/formoterol en asma persistente |
| [26229457](https://pubmed.ncbi.nlm.nih.gov/26229457/) | 2015 | Revisión | Int J COPD | Doble broncodilatación con indacaterol-glicopirronio en EPOC |
| [30021361](https://pubmed.ncbi.nlm.nih.gov/30021361/) | 2018 | Preclínico | Biomed Pharmacother | Extracto de tomillo y frecuencia de batido mucociliar en células de pacientes con EPOC |
| [37327273](https://pubmed.ncbi.nlm.nih.gov/37327273/) | 2023 | Reporte de caso | Medicine | Infección pulmonar por Aspergillus tratada con omalizumab |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20128097 | SEROHALE 125 SYNCHROBREATHE SB | Suspensión para inhalación | Salmeterol y fluticasona |
| 20128029 | SEROHALE 250 SYNCHROBREATHE SB | Suspensión para inhalación | Salmeterol y fluticasona |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (100 interacciones registradas; se destacan las principales):
  - **Mayor:** claritromicina.
  - **Moderada:** acarbosa, isometepteno, famotidina, epinefrina, albiglutida, alogliptina, canagliflozina, clorpropamida, dapagliflozina, dietilpropión, dolasetrón, dulaglutida, empagliflozina.
  - **Menor:** hidrocortisona, triamcinolona, dexametasona, beclometasona, betametasona, budesonida.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún estudio que evalúe directamente la malformación respiratoria; el puntaje alto del modelo no está respaldado por un mecanismo identificado ni por evidencia clínica, por lo que el nivel es L5.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de salmeterol.
- Definir un subtipo concreto de malformación respiratoria con una hipótesis mecanística clara.
- Estudios preclínicos o clínicos que evalúen directamente esta enfermedad.
- Información de seguridad completa del prospecto (advertencias y contraindicaciones).

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Serevent Diskus (salmeterol xinafoate) prescribing information, GlaxoSmithKline LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=12d9728e-6b5c-4aee-bfb0-745e542ed2e4) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

