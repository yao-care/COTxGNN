---
layout: default
title: Entacapone
parent: 僅模型預測 (L5)
nav_order: 111
evidence_level: L5
indication_count: 10
---

# Entacapone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Entacapone: De Enfermedad de Parkinson a PLA2G6-Associated Neurodegeneration

## Resumen en Una Frase

Entacapone es un inhibidor de la catecol-O-metiltransferasa (COMT), originalmente utilizado como terapia adyuvante al levodopa/carbidopa en el tratamiento de la Enfermedad de Parkinson.
El modelo TxGNN predice que podría ser efectivo para **PLA2G6-Associated Neurodegeneration (PLAN)**, una forma rara de neurodegeneración asociada a acumulación de hierro cerebral (NBIA tipo 2).
Actualmente **no se registran ensayos clínicos ni publicaciones** que respalden directamente esta dirección; la predicción se sustenta únicamente en el modelo computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Enfermedad de Parkinson (terapia adyuvante con levodopa/carbidopa) |
| Nueva Indicación Predicha | PLA2G6-Associated Neurodegeneration (PLAN) |
| Puntaje de Predicción TxGNN | 99.76% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No Comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. No obstante, Entacapone es ampliamente reconocido como un inhibidor selectivo, reversible y periférico de la COMT, enzima responsable de la degradación de la dopamina y del levodopa en plasma. Al bloquear la COMT, Entacapone prolonga la vida media del levodopa y aumenta su biodisponibilidad cerebral, potenciando la señal dopaminérgica en el estriado.

PLAN (PLA2G6-associated neurodegeneration) es una forma de NBIA causada por mutaciones en el gen PLA2G6, que codifica una fosfolipasa independiente de calcio. Clínicamente cursa con síntomas parkinsonianos prominentes —rigidez, bradicinesia, distonía— junto con deterioro cognitivo y neurodegeneración nigroestriatal progresiva, características que comparten una fisiopatología dopaminérgica semejante a la Enfermedad de Parkinson clásica.

La plausibilidad mecanística es teórica: si la pérdida de neuronas dopaminérgicas en PLAN compromete el sistema nigroestriatal de forma análoga a la EP, la inhibición de COMT podría prolongar el efecto de levodopa en los pacientes que responden a esta terapia. Sin embargo, como señala el propio Evidence Pack, el alto puntaje del modelo podría reflejar nodos compartidos entre PD y PLAN en el grafo de conocimiento más que evidencia farmacológica directa. La validación preclínica específica es indispensable antes de avanzar.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

Entacapone no cuenta con registros sanitarios activos en Colombia. No existen productos comercializados con este principio activo en el mercado colombiano a la fecha de corte de datos (2026-06-04).

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Aunque el puntaje TxGNN de 99.76% es elevado y existe una plausibilidad mecanística basada en la convergencia dopaminérgica entre PLAN y la Enfermedad de Parkinson, la ausencia total de evidencia clínica o preclínica directa —combinada con la posibilidad de que la predicción sea un artefacto del grafo de conocimiento— impide avanzar sin investigación confirmatoria previa.

**Para avanzar se necesita:**
- Estudios preclínicos en modelos animales de PLAN (knockout PLA2G6) para evaluar la respuesta a la inhibición de COMT
- Revisión sistemática de casos clínicos de PLAN tratados con levodopa, que permitan inferir el potencial beneficio adyuvante de Entacapone
- Completar el perfil de MOA y seguridad del fármaco (actualmente en Data Gap: DG001 y DG002)
- Evaluación de la expresión y actividad de COMT en tejido cerebral con patología PLA2G6
- Registro sanitario en Colombia como prerequisito regulatorio para cualquier uso clínico futuro
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

