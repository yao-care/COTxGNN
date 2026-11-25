---
layout: default
title: Metoprolol
parent: Solo Predicción del Modelo (L5)
nav_order: 439
evidence_level: L5
indication_count: 6
monitor_inn: "metoprolol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "chronic pulmonary heart disease", "trichotillomania"]
last_modified_at: 2026-11-25
description: "Metoprolol: nueva indicación predicha, Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) (nivel de evidencia L5). Indicación original: METOPROLOL"
---

# Metoprolol
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

## Metoprolol: Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)
{: .text-alpha }

## Resumen en Una Frase

Metoprolol es un betabloqueante cardioselectivo (beta-1) con registros sanitarios vigentes en Colombia; el texto del registro solo menciona el nombre del principio activo, sin detallar una indicación.
El modelo TxGNN predice que podría ser efectivo para **enfermedad renal hipertensiva maligna**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección, por lo que se trata únicamente de una predicción computacional.

<!-- review:begin co-lic-20261112-metoprolol-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "cuatro registros sanitarios vigentes" Corregido: el número de registros sanitarios escrito en el texto no coincidía con los datos del INVIMA (Código Único de Medicamentos, datos al 2026-11-23); el texto ya no indica una cifra fija. Las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261112-metoprolol-1 -->

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | METOPROLOL |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) |
| Puntaje de Predicción TxGNN | 0.9991 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 16 de 18) |
| Número de Registros Sanitarios | 18 (vigentes: 16) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Metoprolol (traducción no oficial): «El metoprolol es un agente bloqueante de los receptores adrenérgicos beta 1 -selectivo (cardioselectivo). Sin embargo, este efecto preferente no es absoluto y, a concentraciones plasmáticas más altas, el metoprolol también inhibe los adrenorreceptores beta 2, ubicados principalmente en la musculatura bronquial y vascular.» Texto original en inglés: "Metoprolol is a beta 1 -selective (cardioselective) adrenergic receptor blocking agent. This preferential effect is not absolute, however, and at higher plasma concentrations, metoprolol also inhibits beta 2 -adrenoreceptors, chiefly located in the bronchial and vascular musculature." ([DailyMed: Toprol Xl (metoprolol succinate) prescribing information, Melinta Therapeutics, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=496ddfaa-7c9c-4888-b747-a210249b367a), versión del 2026-03-03; consultado el 2026-11-19). Según la información conocida, metoprolol es un bloqueador selectivo de receptores beta-1 que reduce la presión arterial, la frecuencia cardíaca y la liberación de renina.

Mecanísticamente, la reducción de renina y de la presión arterial podría ser relevante en hipertensión grave con afectación renal. Sin embargo, esto es una hipótesis: no existen ensayos ni literatura sobre esta indicación específica, y los betabloqueantes no son tratamiento de primera línea en la nefropatía hipertensiva.

Por ello esta predicción debe tratarse como una hipótesis de investigación.

Otras indicaciones predichas, todas sin respaldo clínico directo suficiente:
- **Hipertensión pulmonar de mecanismo multifactorial incierto** (0.9991): el bloqueo beta generalmente no es beneficioso en hipertensión arterial pulmonar y podría empeorar la función del ventrículo derecho.
- **Hipertensión pulmonar por enfermedad pulmonar o hipoxia** (0.9991): la literatura recuperada trata temas ajenos (intoxicación por betabloqueantes, taquicardia auricular multifocal, modelos animales); ninguna estudia esta indicación.
- **Síndrome de Braddock** (0.9989): enfermedad muy rara, sin datos.
- **Cor pulmonale crónico** (0.9940): hay ensayos y estudios sobre metoprolol en pacientes con EPOC e insuficiencia cardíaca, pero abordan seguridad y tolerabilidad, no tratamiento de esta enfermedad.
- **Tricotilomanía** (0.9905): sin datos ni fundamento mecanístico claro.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para la indicación principal predicha (enfermedad renal hipertensiva maligna).

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal predicha.

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 19901250 | BETALOC ZOK® 200 MG | TABLETA DE LIBERACION PROLONGADA | METOPROLOL | Vigente |
| 19927923 | BETALOC ZOK® 25 MG | TABLETA DE LIBERACION PROLONGADA | METOPROLOL | Vigente |
| 19943526 | METOPROLOL100 MG | TABLETA | METOPROLOL | Vigente |
| 19961415 | METOPROLOL TARTRATO 50 MG TABLETAS | TABLETA | METOPROLOL | Vigente |
| 19976470 | METOPROLOL 50 MG TABLETAS | TABLETA | METOPROLOL | Vigente |

Se muestran 5 de 18 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

<!-- review:begin co-lic-20261124b-metoprolol-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "La lista de registros puede ser parcial (se muestran al menos 4)." Eliminado: advertía que la lista de registros podría ser parcial. La tabla de Información de Mercado en Colombia se genera a partir de los datos del INVIMA (Código Único de Medicamentos, datos al 2026-11-23) e indica cuántos registros muestra del total. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261124b-metoprolol-1 -->

## Consideraciones de Seguridad

- **Relaciones de contraindicación registradas en el grafo de conocimiento** (no provienen del texto del prospecto): trastornos de ansiedad, trastorno neurótico, distimia, pancreatitis, enfermedad hepática, enfermedad de la vesícula biliar, lupus eritematoso sistémico, psoriasis, diabetes mellitus, cetoacidosis diabética, hipotensión, gota, miastenia gravis, feocromocitoma, encefalopatía hepática, hiperparatiroidismo, hipercalcemia, anuria, entre otras.
- **Interacciones farmacológicas**: se identificaron 338 interacciones registradas. Entre las de nivel moderado figuran epinefrina, corticosteroides (hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona), atropina, hiosciamina, glicopirronio, bupropión, morfina, cimetidina, canagliflozina, dapagliflozina, clorpropamida, lorcaserina y sales de calcio. Las de nivel leve incluyen ácido acetilsalicílico y óxido de magnesio.
- **Señales de la literatura**: en ratas, metoprolol redujo la tensión de oxígeno tisular cerebral tras hemodilución aguda (PMID 19809291), lo que constituye una alerta leve relacionada con hipoxia. En EPOC, el ensayo BLOCK-COPD (NCT02587351) fue terminado y la literatura citada indica un aumento de exacerbaciones que requirieron hospitalización con metoprolol.

No se dispone del texto de advertencias y contraindicaciones del prospecto; consultar el prospecto para información de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para enfermedad renal hipertensiva maligna no tiene ensayos clínicos ni literatura que la respalden (nivel L5), y los betabloqueantes no son de primera línea en esta condición. Las demás indicaciones predichas tampoco cuentan con evidencia directa que respalde una decisión favorable.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA para definir las indicaciones aprobadas, advertencias y contraindicaciones.
- Completar los datos del mecanismo de acción.
- Realizar una revisión sistemática de la literatura sobre betabloqueantes en nefropatía hipertensiva maligna.
- Si se prioriza una línea alternativa, evaluar cor pulmonale crónico como pregunta de investigación sobre seguridad y comanejo en EPOC con enfermedad cardiovascular (por ejemplo, NCT06825728), no como afirmación de eficacia.
- Evaluar el perfil de seguridad en poblaciones con contraindicaciones registradas (asma/EPOC, diabetes, hipotensión, feocromocitoma).

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-24 | Número de registros sanitarios corregido (sin cifra fija; ver Resumen rápido) | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Toprol Xl (metoprolol succinate) prescribing information, Melinta Therapeutics, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=496ddfaa-7c9c-4888-b747-a210249b367a) |
| 2026-11-24 | Eliminado: "La lista de registros puede ser parcial (se muestran al menos 4)." | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

