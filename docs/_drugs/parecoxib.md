---
layout: default
title: Parecoxib
parent: Evidencia Moderada (L3-L4)
nav_order: 500
evidence_level: L3
indication_count: 3
last_modified_at: 2026-10-28
description: "Parecoxib: nueva indicación predicha, Trastorno de migraña (migraine disorder) (nivel de evidencia L3). Indicación original: No especificada en el registro sanitario (el texto solo indica \"PAREC…"
monitor_inn: "parecoxib"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "pulmonary hypertension"]
---

# Parecoxib
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **3** 
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

## Parecoxib: De Indicación Original No Especificada a Trastorno de Migraña
{: .text-alpha }

## Resumen en Una Frase

Parecoxib es un inhibidor selectivo de la COX-2 administrado por vía inyectable. Su registro sanitario en Colombia no detalla una indicación específica (solo repite el nombre del fármaco), y actualmente está cancelado.
El modelo TxGNN predice que podría ser efectivo para **trastorno de migraña**, con **0 ensayos clínicos registrados** y **1 publicación clínica** (un estudio piloto comparativo) que respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro sanitario (el texto solo indica "PARECOXIB") |
| Nueva Indicación Predicha | Trastorno de migraña (migraine disorder) |
| Puntaje de Predicción TxGNN | 0.9955 |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 1) |
| Número de Registros Sanitarios | 1 (0 vigentes, 1 cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Parecoxib es un profármaco de valdecoxib, un inhibidor selectivo de la COX-2. Los datos compilados para este informe no incluyen una descripción oficial del mecanismo de acción, por lo que lo siguiente se basa en el conocimiento farmacológico general y en el análisis mecanístico asociado a la predicción.

La COX-2 impulsa la síntesis de prostaglandina E2 (PGE2), que sensibiliza los nociceptores del trigémino y favorece la liberación del péptido relacionado con el gen de la calcitonina (CGRP) y la inflamación neurogénica. Al inhibir la COX-2, es plausible reducir estos procesos durante una crisis aguda de migraña. Esto es coherente con el puntaje muy alto de TxGNN (0.9955).

Existe apoyo mecanístico preclínico indirecto: en células de ganglio trigeminal de rata, la IL-1β estimula la síntesis de PGE2 dependiente de COX-2 y la liberación de CGRP (PMID 21394197), y parecoxib modifica la extravasación de proteínas plasmáticas y la expresión de c-fos en un modelo animal de activación trigeminovascular (PMID 16492237). Sin embargo, al ser un fármaco solo inyectable y con registro cancelado, su aplicabilidad práctica es limitada.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [21996647](https://pubmed.ncbi.nlm.nih.gov/21996647/) | 2011 | Estudio clínico piloto (comparativo) | Clinical Neuropharmacology | Compara parecoxib intravenoso 40 mg, rizatriptán oral 10 mg y sumatriptán subcutáneo en crisis agudas de migraña; el diseño y tamaño no pudieron confirmarse |
| [21394197](https://pubmed.ncbi.nlm.nih.gov/21394197/) | 2011 | Preclínico in vitro | PLoS One | La IL-1β estimula la síntesis de PGE2 dependiente de COX-2 y la liberación de CGRP en células de ganglio trigeminal de rata |
| [16492237](https://pubmed.ncbi.nlm.nih.gov/16492237/) | 2006 | Preclínico in vivo (rata) | Headache | Efectos de parecoxib sobre la extravasación de proteínas plasmáticas y la expresión de c-fos en un modelo de activación trigeminovascular |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20255458 (cancelado) | Parecoxib 40 mg polvo estéril para reconstituir a solución inyectable | Polvo liofilizado para reconstituir a solución inyectable | PARECOXIB (sin indicación detallada) |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como referencia general (no proviene de la etiqueta): los inhibidores selectivos de la COX-2 se asocian a preocupaciones de seguridad cardiovascular y trombótica, un aspecto relevante en la evaluación de cualquier nueva indicación.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia clínica se limita a un estudio piloto comparativo cuyo diseño y tamaño no están verificados, sin ensayos registrados. Además, el producto es solo inyectable y su único registro sanitario en Colombia está cancelado, lo que limita la aplicabilidad práctica.

**Para avanzar se necesita:**
- Verificar el diseño, tamaño y resultados del estudio PMID 21996647
- Obtener el prospecto en INVIMA para conocer advertencias y contraindicaciones
- Obtener datos detallados del mecanismo de acción desde DrugBank
- Evaluar la viabilidad de la vía inyectable para el tratamiento de la migraña y la situación regulatoria (registro cancelado)
- Considerar ensayos clínicos controlados que confirmen la eficacia y seguridad en crisis agudas de migraña

---

### Otras Indicaciones Predichas (Referencia)

| Indicación | Puntaje TxGNN | Nivel de Evidencia | Recomendación |
|------|------|------|------|
| Migraña con aura de tronco encefálico | 0.9946 | L5 | Hold (solo predicción; evidencia extrapolada de migraña general) |
| Hipertensión pulmonar | 0.9909 | L5 | Hold (solo un estudio animal en lechones; sugiere ausencia de beneficio o posible daño, no eficacia) |
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

