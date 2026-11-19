---
layout: default
title: Moxifloxacin
parent: Solo Predicción del Modelo (L5)
nav_order: 457
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-12
description: "Moxifloxacin: nueva indicación predicha, Síndrome de hiperviscosidad policlonal (nivel de evidencia L5). Indicación original: Dexametasona y antiinfecciosos"
monitor_inn: "moxifloxacin"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "congenital hematological disorder", "hematopoietic and lymphoid system neoplasm"]
---

# Moxifloxacin
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

## Moxifloxacino: De Dexametasona y Antiinfecciosos (Moxifloxacina) a Síndrome de Hiperviscosidad Policlonal
{: .text-alpha }

## Resumen en Una Frase

Moxifloxacino es un antibiótico fluoroquinolónico, registrado en Colombia en una solución oftálmica combinada con dexametasona y en tabletas recubiertas de 400 mg.
El modelo TxGNN predice que podría ser efectivo para **síndrome de hiperviscosidad policlonal**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta indicación; se trata únicamente de una predicción del modelo TxGNN (aprendizaje profundo).
Entre las demás predicciones, solo la **peste bubónica** muestra evidencia preclínica plausible (estudios in vitro y en animales).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dexametasona y antiinfecciosos (registro de la solución oftálmica); moxifloxacina (tabletas) |
| Nueva Indicación Predicha | Síndrome de hiperviscosidad policlonal |
| Puntaje de Predicción TxGNN | 0.9998 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 16 de 18) |
| Número de Registros Sanitarios | 18 (vigentes: 16) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según las secciones «Mechanism of Action» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Moxifloxacin (traducción no oficial): «Moxifloxacino Tableta es un miembro de la clase de agentes antibacterianos de las fluoroquinolonas. […] La acción bactericida del moxifloxacino resulta de la inhibición de la topoisomerasa II (DNA girasa) y de la topoisomerasa IV, necesarias para la replicación, la transcripción, la reparación y la recombinación del DNA bacteriano.» Texto original en inglés: "Moxifloxacin Tablet is a member of the fluoroquinolone class of antibacterial agents. […] The bactericidal action of moxifloxacin results from inhibition of the topoisomerase II (DNA gyrase) and topoisomerase IV required for bacterial DNA replication, transcription, repair, and recombination." ([DailyMed: Moxifloxacin (moxifloxacin hydrochloride) prescribing information, Kesin Pharma Corportation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5a6d3ff1-e853-a3d8-e063-6394a90a18f5), versión del 2026-11-06; consultado el 2026-11-19). Según la información conocida, moxifloxacino es una fluoroquinolona antibacteriana que inhibe la ADN girasa y la topoisomerasa IV bacterianas. Su eficacia está establecida en infecciones bacterianas, no en trastornos de la viscosidad sanguínea.

La hiperviscosidad policlonal surge por un aumento de las inmunoglobulinas séricas. No se identifica un vínculo mecanístico plausible con un antibacteriano; el puntaje alto del modelo TxGNN (aprendizaje profundo) puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

Otras indicaciones hematológicas predichas por el modelo (gammapatía monoclonal, trastornos hematológicos congénitos) solo tienen relación indirecta, como prevención o tratamiento de infecciones en pacientes con neutropenia o trasplante.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para síndrome de hiperviscosidad policlonal.

*Nota: para otras indicaciones predichas existen ensayos solo indirectamente relacionados (por ejemplo, [NCT00324324](https://clinicaltrials.gov/study/NCT00324324), Fase 3, terminado, 240 participantes, profilaxis antibacteriana tras trasplante alogénico de progenitores hematopoyéticos; y [NCT00062231](https://clinicaltrials.gov/study/NCT00062231), terminado, 351 participantes, terapia oral empírica de la fiebre en pacientes oncológicos neutropénicos). Ninguno evalúa la indicación principal.*

---

## Informacion de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20165941 | TQ OFTAMOX® D UD | Solución oftálmica | Dexametasona y antiinfecciosos |
| 20133598 | MOXFACIN® 400 MG TABLETA RECUBIERTA | Tableta recubierta | Moxifloxacina |

---

## Consideraciones de Seguridad

- **Contraindicaciones o condiciones de riesgo (según el grafo de conocimiento, no según el prospecto):** síndrome de QT largo (incluido el familiar), torsades de pointes, paro cardíaco súbito, enfermedades de la conducción cardíaca, isquemia miocárdica y enfermedad coronaria; epilepsia; miastenia gravis y enfermedades de la unión neuromuscular; neuropatía periférica y enfermedades del sistema nervioso periférico; tendinitis, periartritis y exostosis; cirrosis hepática y lesión hepática inducida por fármacos; deficiencia de potasio; colitis por *Clostridium difficile* y enterocolitis necrosante perinatal.
- **Interacciones farmacológicas:** se identificaron 336 interacciones. Entre las de nivel **mayor** figuran corticoesteroides (hidrocortisona, triamcinolona, dexametasona, betametasona), bupropión y clorpropamida. Entre las de nivel moderado: antidiabéticos (acarbosa, metformina, pioglitazona, alogliptina, canagliflozina, albiglutida), famotidina, loperamida, ácido acetilsalicílico, balsalazida, bisacodilo y sales de calcio y potasio.
- **Aviso relevante:** la predicción para "enfermedad hematológica asociada a neuropatía periférica adquirida" plantea una preocupación de seguridad, pues las fluoroquinolonas se asocian con neuropatía periférica.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para síndrome de hiperviscosidad policlonal es solo un resultado del modelo (L5), sin ensayos ni literatura, y sin mecanismo plausible. Además, no existen registros sanitarios vigentes en Colombia y el perfil de seguridad del fármaco es considerable.

**Para avanzar se necesita:**
- Obtener el prospecto del INVIMA para completar advertencias y contraindicaciones oficiales (brecha bloqueante).
- Obtener datos del mecanismo de acción desde DrugBank.
- Reorientar el análisis hacia la **peste bubónica**, la única indicación con respaldo preclínico plausible (L4), evaluando si hay interés clínico y regulatorio local.

<!-- review:begin co-lic-20261031-moxifloxacin-1 -->

> **Corrección de revisión (2026-10-31)**: Texto original: "Reorientar el análisis hacia la **peste bubónica**, la única indicación con respaldo preclínico plausible (L4), evaluando si hay interés clínico y regulatorio local. / Confirmar la situación regulatoria (registros cancelados) antes de cualquier desarrollo en Colombia." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-10-31. El medicamento tiene 18 registros sanitarios (vigentes: 16); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261031-moxifloxacin-1 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-10-31 | Eliminado: "Confirmar la situación regulatoria (registros cancelados) antes de cualquier desarrollo en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Moxifloxacin (moxifloxacin hydrochloride) prescribing information, Kesin Pharma Corportation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5a6d3ff1-e853-a3d8-e063-6394a90a18f5) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

