---
layout: default
title: Denosumab
parent: 僅模型預測 (L5)
nav_order: 97
evidence_level: L5
indication_count: 2
---

# Denosumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Denosumab: De Osteoporosis a Retinopatía Diabética Severa No Proliferativa

## Resumen en Una Frase

Denosumab es un anticuerpo monoclonal inhibidor de RANKL, aprobado internacionalmente para el tratamiento de la osteoporosis y la pérdida ósea asociada a terapias oncológicas.
El modelo TxGNN predice que podría ser efectivo para la **Retinopatía Diabética Severa No Proliferativa**,
sin embargo, actualmente **no existen ensayos clínicos ni publicaciones** que respalden directamente esta indicación específica (evidencia Nivel L5).

---

## Resumen Rápido

| Ítem | Contenido |
|------|------|
| Indicación Original | No disponible en registros colombianos (sin licencias INVIMA activas) |
| Nueva Indicación Predicha | Retinopatía Diabética Severa No Proliferativa |
| Puntaje de Predicción TxGNN | 99.63% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de Denosumab en el contexto de la patología retiniana. Según la información conocida, Denosumab es un inhibidor del ligando RANK (RANKL), y su eficacia en la preservación de la densidad ósea y la reducción de complicaciones esqueléticas ha sido ampliamente demostrada. La conexión con la retinopatía diabética se basa en la participación teórica del eje RANKL/RANK/OPG en la microvasculatura retiniana: la inhibición de RANKL podría reducir la apoptosis de pericitos retinianos y la inflamación mediada por macrófagos M1, ambos procesos clave en la progresión de la retinopatía diabética no proliferativa.

Un estudio observacional de mundo real publicado en 2024 (PMID 38899553) reportó que Denosumab reduce la incidencia de diabetes tipo 2 y sus complicaciones microvasculares —incluyendo retinopatía, neuropatía y nefropatía— en comparación con bifosfonatos. Este hallazgo sugiere un posible efecto protector sistémico sobre la vasculatura diabética, lo que podría sustentar indirectamente la hipótesis de beneficio retiniano. Sin embargo, este estudio no fue diseñado para evaluar retinopatía como desenlace primario.

Es fundamental subrayar que la conexión mecanística con la retinopatía diabética **severa no proliferativa** es puramente especulativa. No existe ningún estudio preclínico ni ensayo clínico que haya investigado directamente Denosumab en este subtipo específico de la enfermedad. La predicción de TxGNN debe interpretarse como una hipótesis generadora de investigación, no como evidencia de eficacia clínica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para Denosumab en retinopatía diabética severa no proliferativa.

> **Contexto de la indicación más amplia (Rank 2 — Retinopatía Diabética):** Se identificó 1 ensayo clínico cuyo desenlace incluye evaluación ocular en pacientes tratados con Denosumab. Su relevancia es indirecta (Grado C):

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00925600](https://clinicaltrials.gov/study/NCT00925600) | Fase 3 | Completado | 769 | Evaluación de opacidades del cristalino (seguridad ocular) en hombres con cáncer de próstata no metastásico que reciben Denosumab por pérdida ósea asociada a terapia de privación androgénica. No evalúa retinopatía diabética como desenlace primario; relevancia limitada a seguridad ocular periférica. |

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para retinopatía diabética severa no proliferativa.

> **Contexto de la indicación más amplia (Rank 2 — Retinopatía Diabética):** Se identificaron 2 publicaciones con relevancia indirecta:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38899553](https://pubmed.ncbi.nlm.nih.gov/38899553/) | 2024 | Cohorte / Meta-análisis | Diabetes, Obesity & Metabolism | Denosumab redujo la incidencia de T2DM, riesgo de úlcera de pie y mortalidad por todas las causas frente a bifosfonatos; incluyó evaluación de complicaciones microvasculares (retinopatía, neuropatía, nefropatía). Evidencia indirecta de protección microvascular sistémica. |
| [36960265](https://pubmed.ncbi.nlm.nih.gov/36960265/) | 2023 | Observacional | Cureus | Evaluación del riesgo de fractura mediante herramienta FRAX en adultos con T2DM. Contextualiza la osteoporosis en el paciente diabético; relevancia muy indirecta respecto a Denosumab y retinopatía. |

---

## Información de Mercado en Colombia

Denosumab no cuenta con ningún registro sanitario vigente en Colombia. No se identificaron licencias activas en la base de datos INVIMA consultada.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
A pesar de que el puntaje TxGNN es muy alto (99.63%), la ausencia total de evidencia clínica o preclínica directa para retinopatía diabética severa no proliferativa clasifica esta predicción en Nivel L5. La conexión mecanística es puramente teórica, y Denosumab no está comercializado en Colombia, lo que suma barreras regulatorias y de acceso significativas.

**Para avanzar se necesita:**
- Estudios preclínicos en modelos animales de retinopatía diabética que evalúen el papel del eje RANKL/RANK/OPG en pericitos y células endoteliales retinianas
- Análisis post-hoc de datos de retinopatía en los ensayos clínicos existentes de Denosumab, especialmente en subgrupos con diabetes tipo 2
- Datos completos de mecanismo de acción (MOA) desde DrugBank para fortalecer el análisis de plausibilidad biológica
- Ficha técnica y advertencias de seguridad oficiales (junta técnica INVIMA o FDA label) para completar la evaluación S1
- Evaluación de viabilidad regulatoria en Colombia (registro INVIMA) antes de cualquier desarrollo clínico local
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

