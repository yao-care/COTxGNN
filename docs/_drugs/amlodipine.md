---
layout: default
title: Amlodipine
parent: Solo Predicción del Modelo (L5)
nav_order: 51
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-25
description: "Amlodipine: nueva indicación predicha, Infarto del tronco encefálico (brain stem infarction) (nivel de evidencia L5). Indicación original: Valsartán y amlodipino (combinación antihipertensiva)"
monitor_inn: "Amlodipine"
predicted_indications: ["brain stem infarction", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "cerebral artery occlusion", "Braddock syndrome", "MRI defined brain infarct", "ABri amyloidosis", "intracerebral hemorrhage"]
---

# Amlodipine
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

## Amlodipino: De Combinaciones Antihipertensivas a Infarto del Tronco Encefálico
{: .text-alpha }

## Resumen en Una Frase

Amlodipino es un bloqueador de canales de calcio utilizado para la hipertensión y la angina estable crónica; en Colombia sus registros sanitarios corresponden a combinaciones con valsartán (e hidroclorotiazida).
El modelo TxGNN predice que podría ser efectivo para **infarto del tronco encefálico** (la predicción con mayor puntaje), pero para esta indicación **no hay ensayos clínicos ni publicaciones** que la respalden.
La evidencia más sólida de todo el análisis corresponde a otra indicación predicha, la **hemorragia intracerebral** (ensayo de Fase 3 completado, TRIDENT), aunque se trata de una combinación triple y no de amlodipino solo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Valsartán y amlodipino (combinación antihipertensiva) |
| Nueva Indicación Predicha | Infarto del tronco encefálico (brain stem infarction) |
| Puntaje de Predicción TxGNN | 0.9994 |
| Nivel de Evidencia | L5 (solo predicción del modelo) |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 18) |
| Número de Registros Sanitarios | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Amlodipine (traducción no oficial): «La amlodipina es un antagonista del calcio de tipo dihidropiridínico (antagonista de los iones calcio o bloqueante de los canales lentos) que inhibe el flujo transmembrana de entrada de iones calcio al músculo liso vascular y al músculo cardíaco. Los datos experimentales sugieren que la amlodipina se une tanto a los sitios de unión dihidropiridínicos como a los no dihidropiridínicos.» Texto original en inglés: "Amlodipine is a dihydropyridine calcium antagonist (calcium ion antagonist or slow-channel blocker) that inhibits the transmembrane influx of calcium ions into vascular smooth muscle and cardiac muscle. Experimental data suggest that amlodipine binds to both dihydropyridine and nondihydropyridine binding sites." ([DailyMed: Sdamlo (amlodipine) prescribing information, Pangea Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=886a7f97-60a4-4206-a6c7-5206069ed487), versión del 2026-09-28; consultado el 2026-11-19). Según la información farmacológica conocida, amlodipino es un bloqueador de canales de calcio dihidropiridínico que modula los canales de calcio dependientes de voltaje (Ca<sub>v</sub>1.2 y Ca<sub>v</sub>1.3) y también aparece asociado al receptor P2X4. Reduce la resistencia vascular sistémica y la presión arterial.

La relación con el infarto del tronco encefálico es plausible de forma indirecta: el control de la presión arterial y los efectos vasoprotectores de este tipo de fármacos podrían influir en el riesgo de enfermedad cerebrovascular. Sin embargo, esta hipótesis no cuenta con respaldo de ningún estudio recuperado y debe considerarse solo una predicción del modelo.

Entre las otras indicaciones predichas, la más relevante es la **hemorragia intracerebral** (puntaje 0.9979). Allí el control de la presión arterial es la estrategia establecida de prevención secundaria, y amlodipino forma parte de la píldora triple evaluada en el ensayo TRIDENT. Esto no es un mecanismo nuevo, sino un uso antihipertensivo en una población específica.

---

## Evidencia de Ensayos Clínicos

Para la indicación principal (infarto del tronco encefálico): actualmente no hay ensayos clínicos relacionados registrados.

Para contextualizar, se presentan los ensayos de la indicación con mayor evidencia (hemorragia intracerebral):

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02699645](https://clinicaltrials.gov/study/NCT02699645) | Fase 3 | Completado | 1671 | TRIDENT: píldora única con tres antihipertensivos a dosis bajas frente a la atención estándar para prevenir ictus recurrente tras hemorragia intracerebral. Amlodipino es un componente |
| [NCT07458880](https://clinicaltrials.gov/study/NCT07458880) | No aplica | En reclutamiento | 140 | Triple medicación antihipertensiva tras hemorragia intracerebral guiada por el puntaje TRICH; aún sin resultados |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | No aplica | Terminado | 4 | Subestudio de resonancia magnética de TRIDENT; terminado con muy pocos participantes, sin datos útiles |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Fase 3 | Terminado | 1 | Subestudio cognitivo de TRIDENT; terminado con un participante, no informativo |

---

## Evidencia de Literatura

Para la indicación principal (infarto del tronco encefálico): actualmente no hay literatura relacionada disponible.

Publicaciones más relevantes de la indicación con mayor evidencia (hemorragia intracerebral):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [42019018](https://pubmed.ncbi.nlm.nih.gov/42019018/) | 2026 | ECA | N Engl J Med | Resultados principales de TRIDENT: píldora única con tres antihipertensivos a dosis bajas añadida al tratamiento estándar tras hemorragia intracerebral |
| [34994269](https://pubmed.ncbi.nlm.nih.gov/34994269/) | 2022 | Diseño del ensayo | Int J Stroke | Justificación y diseño de TRIDENT; la combinación en una sola píldora como estrategia de prevención secundaria |
| [19299323](https://pubmed.ncbi.nlm.nih.gov/19299323/) | 2009 | Reporte de caso | Ann Pharmacother | Probable angioedema inducido por amlodipino en un paciente con hemorragia talámica (señal de seguridad) |

---

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 19902457 | AMDIPIN H 5-12.5 | TABLETA | HIDROCLOROTIAZIDA Y AGENTES AHORRADORES DE POTASIO | Vigente |
| 19902458 | AMDIPIN H® 10 MG | TABLETA | HIDROCLOROTIAZIDA Y AGENTES AHORRADORES DE POTASIO | Vigente |
| 19915210 | AMLODIPINO 5MG TABLETAS | TABLETA | AMLODIPINO | Vigente |
| 19928328 | AMLODIPINO 10 MG TABLETAS | TABLETA | AMLODIPINO | Vigente |
| 19928630 | AMLODIPINO 5 MG TABLETAS | TABLETA | AMLODIPINO | Vigente |

Se muestran 5 de al menos 20 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes. Los datos de este informe solo incluyen parte de los registros.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: el grafo asocia al fármaco con enfermedades como insuficiencia hepática, enfermedad renal, pancreatitis, enfermedad de la vesícula biliar, hipotiroidismo, angioedema (incluido el hereditario y el inducido por bloqueadores del sistema renina-angiotensina-aldosterona), lupus eritematoso sistémico, miopatías, parálisis periódica familiar, deficiencia de potasio, diabetes mellitus y cetoacidosis diabética, neutropenia y agranulocitosis, trastornos hipotensivos e hiperparatiroidismo.
- **Señales de seguridad en la literatura**: casos de angioedema asociado a amlodipino y un reporte de sobredosis complicada con edema pulmonar no cardiogénico y hemorragia alveolar difusa.
- **Interacciones farmacológicas**: no se identificaron interacciones con otros fármacos; los datos disponibles describen solo dianas farmacológicas (P2X4, Ca<sub>v</sub>1.2, Ca<sub>v</sub>1.3).

Se debe consultar el prospecto para la información completa de advertencias y contraindicaciones.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para infarto del tronco encefálico solo existe la predicción del modelo (L5), sin ensayos ni literatura. La indicación con evidencia más fuerte, la hemorragia intracerebral (L1, TRIDENT), podría avanzar con salvaguardas, pero el efecto no se puede atribuir al amlodipino solo y se trata de un uso antihipertensivo ya establecido.

<!-- review:begin co-lic-20261105-amlodipine-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, en Colombia no hay registros vigentes de amlodipino. La indicación con evidencia más fuerte, la hemorragia intracerebral (L1, TRIDENT), podría avanzar con salvaguardas, pero el efecto no se puede atribuir al amlodipino solo y se trata de un uso antihipertensivo ya establecido." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-amlodipine-1 -->

**Para avanzar se necesita:**
- Revisar los resultados del desenlace primario de TRIDENT antes de formular cualquier recomendación sobre hemorragia intracerebral.
- Datos del mecanismo de acción consultando DrugBank.
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), actualmente no disponible.
- Aclarar la situación regulatoria local.
- Estudios preclínicos o clínicos específicos de amlodipino en infarto del tronco encefálico o enfermedad cerebrovascular isquémica.
- Plan de monitoreo de seguridad (angioedema, hipotensión).

<!-- review:begin co-lic-20261105-amlodipine-2 -->

> **Corrección de revisión (2026-11-25)**: Texto original: "Aclarar la situación regulatoria local, ya que ambos registros están cancelados y corresponden a combinaciones." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Actualizado el 2026-11-25: se reformuló el texto que quedó tras la eliminación para que la frase se lea completa. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-amlodipine-2 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Además, en Colombia no hay registros vigentes de amlodipino" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-25 | «Aclarar la situación regulatoria local, ya que ambos registr…» → «Aclarar la situación regulatoria local.…» | Corregido (revisado el 2026-11-25; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Sdamlo (amlodipine) prescribing information, Pangea Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=886a7f97-60a4-4206-a6c7-5206069ed487) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

