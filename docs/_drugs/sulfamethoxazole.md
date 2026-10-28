---
layout: default
title: Sulfamethoxazole
parent: Solo Predicción del Modelo (L5)
nav_order: 596
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
description: "Sulfamethoxazole: nueva indicación predicha, Conjuntivitis contagiosa aguda (nivel de evidencia L4). Indicación original: Sulfametoxazol y trimetoprim"
monitor_inn: "Sulfamethoxazole"
predicted_indications: ["acute contagious conjunctivitis"]
---

# Sulfamethoxazole
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Sulfametoxazol: De Sulfametoxazol y Trimetoprim a Conjuntivitis Contagiosa Aguda
{: .text-alpha }

## Resumen en Una Frase

Sulfametoxazol es un antibacteriano del grupo de las sulfonamidas, registrado en Colombia en combinación con trimetoprim.
El modelo TxGNN predice que podría ser efectivo para **conjuntivitis contagiosa aguda**,
con **0 ensayos clínicos** y **1 publicación** que actualmente respaldan esta dirección (un estudio de bacteriología y susceptibilidad antimicrobiana, no de eficacia del fármaco).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sulfametoxazol y trimetoprim |
| Nueva Indicación Predicha | Conjuntivitis contagiosa aguda |
| Puntaje de Predicción TxGNN | 0.9963 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 2) |
| Número de Registros Sanitarios | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, sulfametoxazol es una sulfonamida que inhibe la enzima bacteriana dihidropteroato sintetasa, bloqueando la síntesis de folato. Su uso como antibacteriano (habitualmente combinado con trimetoprim) está bien establecido, y mecanísticamente podría ser aplicable a infecciones bacterianas oculares.

La conjuntivitis aguda contagiosa es con frecuencia de origen bacteriano (por ejemplo, *Haemophilus influenzae*, *Streptococcus pneumoniae* y *Staphylococcus aureus*), por lo que un mecanismo antibacteriano es biológicamente plausible. Además, las sulfonamidas se han usado históricamente por vía tópica en infecciones oculares (por ejemplo, sulfacetamida), lo que respalda la verosimilitud de la predicción.

Sin embargo, conviene ser cautos: el sulfametoxazol sistémico no es un tratamiento establecido para la conjuntivitis, la única publicación disponible es un estudio de susceptibilidad y no evalúa la eficacia de este fármaco, y el puntaje alto de TxGNN es una predicción computacional que no sustituye la evidencia clínica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31788487](https://pubmed.ncbi.nlm.nih.gov/31788487/) | 2019 | Cohorte (retrospectivo) | Medical Hypothesis, Discovery & Innovation Ophthalmology Journal | Análisis retrospectivo de la bacteriología y los patrones de susceptibilidad antimicrobiana en conjuntivitis bacteriana aguda infantil en el oeste de Grecia. No evalúa directamente la eficacia del sulfametoxazol. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20077704 | MEDIPRIM F SUSPENSION (vigente) | Suspensión oral | Sulfametoxazol y trimetoprim |
| 19985112 | MEDIPRIM F (R) TABLETA (vigente) | Tableta | Sulfametoxazol y trimetoprim |

Ambos registros figuran como cancelados; no hay registros vigentes.

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas por el grafo de conocimiento (no provienen del prospecto):** porfiria (incluida la hereditaria y los trastornos del metabolismo de porfirinas), enfermedad renal, insuficiencia renal, uremia, glomerulonefritis, piuria/pioureter, enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia, neutropenia, agranulocitosis, anemia por deficiencia de ácido fólico, deficiencia de G6PD, colitis por *Clostridium difficile*, enterocolitis necrosante perinatal, enfermedad por almacenamiento de glucógeno, cistinuria y galactosemia.
- **Interacciones farmacológicas:** se identificaron 100 interacciones en total; las principales visibles son:
  - *Moderadas:* sulfonilureas (clorpropamida, glimepirida, acetohexamida, glipizida, glibenclamida), insulinas (humana, aspart, degludec, detemir, glargina, glulisina), balsalazida y ácido picosulfúrico (posible riesgo de hipoglucemia con antidiabéticos).
  - *Leves:* famotidina, claritromicina, dolasetrón, palonosetrón, cisaprida y granisetrón.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el modelo y en un estudio de susceptibilidad sin evaluación directa del fármaco (nivel L4), sin ensayos clínicos. Además, el medicamento está comercializado en Colombia, con 2 registros sanitarios vigentes.

**Para avanzar se necesita:**
- Datos del mecanismo de acción confirmados (por ejemplo, desde DrugBank)
- Advertencias y contraindicaciones del prospecto de INVIMA
- Evidencia clínica directa sobre la eficacia de sulfametoxazol (o su combinación) en conjuntivitis bacteriana
- Evaluación de la compatibilidad de vías de administración (probable formulación oftálmica tópica frente a las formas orales registradas)
- Análisis de viabilidad regulatoria y comercial dado que no hay registros vigentes
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

