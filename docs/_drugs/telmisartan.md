---
layout: default
title: Telmisartan
parent: Solo Predicción del Modelo (L5)
nav_order: 609
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-12
description: "Telmisartan: nueva indicación predicha, Prinzmetal angina (angina de Prinzmetal) (nivel de evidencia L5). Indicación original: Telmisartán y diuréticos (hipertensión arterial)"
monitor_inn: "TELMISARTAN"
predicted_indications: ["Prinzmetal angina", "brain stem infarction", "ABri amyloidosis", "cerebral artery occlusion", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant hypertensive renal disease", "intracerebral hemorrhage", "Braddock syndrome"]
---

# Telmisartan
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

## Telmisartán: De Telmisartán (antihipertensivo) a Prinzmetal angina
{: .text-alpha }

## Resumen en Una Frase

Telmisartán es un antagonista del receptor de angiotensina II, registrado en Colombia para el tratamiento de la hipertensión (solo o con diuréticos).
El modelo TxGNN predice que podría ser efectivo para **angina de Prinzmetal**, pero hasta ahora **no hay ensayos clínicos ni publicaciones** que respalden esta predicción específica; la indicación con mayor respaldo entre las candidatas es la **hemorragia intracerebral** (1 ensayo de Fase 3 completado, con una combinación de tres fármacos).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Telmisartán y diuréticos (hipertensión arterial) |
| Nueva Indicación Predicha | Prinzmetal angina (angina de Prinzmetal) |
| Puntaje de Predicción TxGNN | 0.9998 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 18) |
| Número de Registros Sanitarios | al menos 20 |
| Decisión Recomendada | Hold |

> **Nota:** El puntaje más alto corresponde a la angina de Prinzmetal, pero esta carece de evidencia. Entre todas las candidatas evaluadas, la de mayor evidencia es la hemorragia intracerebral (L2), descrita en la sección de conclusión.

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Telmisartan (traducción no oficial): «La angiotensina II se forma a partir de la angiotensina I en una reacción catalizada por la enzima convertidora de angiotensina (ECA, cininasa II). La angiotensina II es el principal agente presor del sistema renina-angiotensina, con efectos que incluyen vasoconstricción, estimulación de la síntesis y liberación de aldosterona, estimulación cardíaca y reabsorción renal de sodio. […] El telmisartán bloquea los efectos vasoconstrictores y secretores de aldosterona de la angiotensina II al bloquear selectivamente la unión de la angiotensina II al receptor AT 1 en muchos tejidos, como el músculo liso vascular y la glándula suprarrenal.» Texto original en inglés: "Angiotensin II is formed from angiotensin I in a reaction catalyzed by angiotensin-converting enzyme (ACE, kininase II). Angiotensin II is the principal pressor agent of the reninangiotensin system, with effects that include vasoconstriction, stimulation of synthesis and release of aldosterone, cardiac stimulation, and renal reabsorption of sodium. […] Telmisartan blocks the vasoconstrictor and aldosterone-secreting effects of angiotensin II by selectively blocking the binding of angiotensin II to the AT 1 receptor in many tissues, such as vascular smooth muscle and the adrenal gland." ([DailyMed: telmisartan prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=56a72ddf-c2a2-45ce-91b1-1fcfbff52c10), versión del 2026-11-02; consultado el 2026-11-19). Según la información conocida, telmisartán pertenece a la clase de los bloqueadores del receptor de angiotensina II (ARA-II), su eficacia en hipertensión está establecida y, mecanísticamente, podría ser aplicable a enfermedades vasculares.

Para la angina de Prinzmetal, un vínculo plausible sería la vasodilatación por bloqueo del receptor AT1 y efectos endoteliales relacionados con PPARγ. Sin embargo, esto es especulativo y no está respaldado por ningún dato aportado: no hay ensayos ni literatura para esta indicación.

La relación entre la indicación original (hipertensión) y la nueva (espasmo vasoespástico coronario) es de tipo vascular, pero esta cercanía no sustituye la evidencia clínica. La predicción debe considerarse solo una hipótesis generada por el modelo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para angina de Prinzmetal.

Como referencia, la candidata con mayor evidencia (hemorragia intracerebral) tiene los siguientes ensayos:

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02699645](https://clinicaltrials.gov/study/NCT02699645) | Fase 3 | Completado | 1671 | Píldora única con tres antihipertensivos a dosis bajas (incluye telmisartán) para prevenir recurrencia de ictus tras hemorragia intracerebral; el efecto corresponde a la combinación, no a telmisartán solo |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | No aplica | Terminado | 4 | Subestudio de RM de TRIDENT; terminado con 4 participantes, sin datos interpretables |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Fase 3 | Terminado | 1 | Subestudio cognitivo de TRIDENT; terminado con 1 participante, sin datos interpretables |

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para angina de Prinzmetal.

Como referencia, publicaciones destacadas de la candidata con mayor evidencia (hemorragia intracerebral):

<!-- review:begin co-lic-20261105-telmisartan-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Ambos registros están cancelados; actualmente no hay registros vigentes en Colombia." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-telmisartan-1 -->

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [42019018](https://pubmed.ncbi.nlm.nih.gov/42019018/) | 2026 | ECA | N Engl J Med | Píldora única con tres antihipertensivos a dosis bajas tras hemorragia intracerebral; el resumen disponible no muestra los resultados |
| [34994269](https://pubmed.ncbi.nlm.nih.gov/34994269/) | 2022 | Diseño de ensayo | Int J Stroke | Justificación y diseño del ensayo TRIDENT para prevención secundaria |
| [17538008](https://pubmed.ncbi.nlm.nih.gov/17538008/) | 2007 | Preclínico | J Pharmacol Exp Ther | El bloqueo de AT1 con telmisartán reduce apoptosis, inflamación y estrés oxidativo en ratas con hemorragia intracerebral |
| [27078703](https://pubmed.ncbi.nlm.nih.gov/27078703/) | 2016 | Preclínico | Neurol Res | Telmisartán mejora el estrés oxidativo y el vasoespasmo cerebral tras hemorragia subaracnoidea |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20103719 | TEMILTAR H® 80 MG/12.5 MG | Tableta | Telmisartán y diuréticos |
| 20056044 | RENANGIO 80 MG | Tableta | Telmisartán |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** insuficiencia hepática, enfermedad renal, anuria, colestasis, pancreatitis, enfermedad de la vesícula biliar, lupus eritematoso sistémico, diabetes mellitus y cetoacidosis diabética, deficiencia de potasio, gota e hiperuricemia, hipercalcemia, hiperparatiroidismo, trastornos hipotensivos, obstrucción de la arteria renal y encefalopatía/coma hepático, entre otras.
- **Interacciones farmacológicas (100 registradas; se listan las más relevantes):**
  - *Mayores:* citrato de potasio y bicarbonato de potasio (riesgo de hiperpotasemia).
  - *Moderadas:* corticoides (hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona), ácido acetilsalicílico, bupropión, morfina, inhibidores de SGLT2 (canagliflozina, dapagliflozina, empagliflozina), exenatida, insulinas, dronabinol y laxantes/preparaciones intestinales (ácido picosulfúrico, polietilenglicol, sulfato de sodio).
- **Consideración específica:** para la hipertensión renovascular maligna, los ARA-II exigen una evaluación cuidadosa (por ejemplo, en estenosis bilateral de arteria renal).

Para advertencias y contraindicaciones oficiales, consultar el prospecto, ya que no se dispuso de ese texto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La angina de Prinzmetal tiene un puntaje alto (0.9998), pero solo es una predicción del modelo (L5), sin ensayos ni literatura. Entre las alternativas, la hemorragia intracerebral (L2) es la mejor respaldada, aunque su ensayo de Fase 3 evaluó una combinación triple y no telmisartán solo; podría considerarse como pregunta de investigación.

<!-- review:begin co-lic-20261105-telmisartan-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, el producto no tiene registros vigentes en Colombia. Entre las alternativas, la hemorragia intracerebral (L2) es la mejor respaldada, aunque su ensayo de Fase 3 evaluó una combinación triple y no telmisartán solo; podría considerarse como pregunta de investigación." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-telmisartan-2 -->

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) y del prospecto (advertencias y contraindicaciones oficiales).
- Revisión de la literatura sobre ARA-II en vasoespasmo coronario para generar evidencia específica de angina de Prinzmetal.
- Para hemorragia intracerebral: resultados detallados de TRIDENT (PMID 42019018) y análisis del aporte individual de telmisartán.
- Definir la vía regulatoria en Colombia, dado que el medicamento está comercializado y cuenta con al menos 18 licencias vigentes.
- Plan de monitoreo de seguridad (potasio, función renal y hepática, hipotensión).

<!-- review:begin co-lic-20261112-telmisartan-1 -->

> **Corrección de revisión (2026-11-12)**: Texto original: "2 licencias vigentes" Corregido según los datos del INVIMA (Código Único de Medicamentos, datos al 2026-11-05): al menos 18 registros sanitarios vigentes (la lista de los datos está limitada a 20 registros). Las cifras actuales están en el Resumen rápido. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261112-telmisartan-1 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Ambos registros están cancelados; actualmente no hay registros vigentes en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Además, el producto no tiene registros vigentes en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-12 | Número de registros vigentes: 2 → al menos 18 | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: telmisartan prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=56a72ddf-c2a2-45ce-91b1-1fcfbff52c10) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

