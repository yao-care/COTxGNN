---
layout: default
title: Perindopril
parent: Solo Predicción del Modelo (L5)
nav_order: 509
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Perindopril: nueva indicación predicha, enfermedad renal hipertensiva maligna (nivel de evidencia L4). Indicación original: Perindopril y amlodipino"
monitor_inn: "PERINDOPRIL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
---

# Perindopril
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

## Perindopril: De Perindopril y Amlodipino a enfermedad renal hipertensiva maligna
{: .text-alpha }

## Resumen en Una Frase

Perindopril es un inhibidor de la enzima convertidora de angiotensina (IECA), registrado en Colombia en una combinación con amlodipino (Coveram®) para el tratamiento de la hipertensión.
El modelo TxGNN predice que podría ser efectivo para **enfermedad renal hipertensiva maligna**, pero actualmente hay **0 ensayos clínicos** y solo **1 publicación** con relevancia muy limitada, por lo que la predicción carece de respaldo real.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Perindopril y amlodipino |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna |
| Puntaje de Predicción TxGNN | 0.9977 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, perindopril pertenece a la clase de los IECA, que reducen la presión arterial y la presión intraglomerular mediante el bloqueo del sistema renina-angiotensina-aldosterona (SRAA). Su eficacia en hipertensión está establecida, y mecanísticamente podría ser aplicable a la lesión renal de origen hipertensivo.

La relación entre la indicación original (hipertensión, en combinación con amlodipino) y la nueva indicación (daño renal por hipertensión maligna) es biológicamente plausible: ambas comparten la sobreactivación del SRAA y el daño vascular renal por presión elevada.

Sin embargo, el puntaje alto del modelo se apoya solo en un razonamiento general de clase. La única publicación recuperada trata sobre la función del riñón solitario tras nefrectomía por cáncer renal, no sobre nefropatía hipertensiva maligna ni sobre perindopril. Además, en hipertensión grave con posible estenosis de la arteria renal, los IECA conllevan riesgo de lesión renal aguda.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36382821](https://pubmed.ncbi.nlm.nih.gov/36382821/) | 2022 | Cohorte | Urologiia (Moscú) | Estado funcional del riñón solitario tras nefrectomía por cáncer renal; no aborda perindopril ni nefropatía hipertensiva maligna |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20007274 (cancelado) | COVERAM® 10 MG / 5MG COMPRIMIDOS | Tableta | Perindopril y amlodipino |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no del prospecto):** enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, angioedema (incluido el hereditario, el adquirido y el inducido por bloqueadores del SRAA), neutropenia, agranulocitosis, trastornos hipotensivos, enfermedades del tejido conectivo, enfermedades óseas y del cartílago, y obstrucción de la arteria renal.
- **Interacciones farmacológicas:** se identificaron 100 interacciones. Entre las listadas, las de nivel **mayor** son con **citrato de potasio** y **bicarbonato de potasio** (riesgo de hiperpotasemia). Las de nivel moderado incluyen corticoides (hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona), antidiabéticos (metformina, alogliptina, saxagliptina, canagliflozina, dapagliflozina, empagliflozina, clorpropamida), ácido acetilsalicílico, morfina, bupropión, dronabinol, ácido picosulfúrico y polietilenglicol con electrolitos.
- **Alerta específica para esta indicación:** en hipertensión grave o maligna con posible estenosis de la arteria renal, los IECA pueden precipitar insuficiencia renal aguda. Esto coincide con la contraindicación por obstrucción de la arteria renal indicada arriba.
- **Reacción adversa documentada en la literatura:** angioedema inducido por IECA, con reportes de casos asociados a perindopril.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El puntaje de TxGNN es muy alto (0.9977), pero no existen ensayos clínicos y la única publicación recuperada no es pertinente al fármaco ni a la enfermedad. Además, el perfil de seguridad en daño renal y estenosis de la arteria renal es una preocupación importante, y no hay registros sanitarios vigentes en Colombia.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank.
- Advertencias y contraindicaciones del prospecto de INVIMA, que no están disponibles y bloquean el tamizaje de seguridad.
- Búsqueda dirigida de literatura clínica sobre IECA en nefropatía hipertensiva maligna.
- Evaluación del riesgo de lesión renal aguda en pacientes con estenosis de la arteria renal.
- Confirmar la situación regulatoria del producto, dado que el único registro está cancelado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

