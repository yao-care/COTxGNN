---
layout: default
title: Modafinil
parent: 僅模型預測 (L5)
nav_order: 174
evidence_level: L5
indication_count: 1
---

# Modafinil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Modafinil: De Somnolencia Excesiva a Insomnio

## Resumen en Una Frase

Modafinil es un agente promotor de vigilia aprobado internacionalmente para el tratamiento de la somnolencia excesiva asociada a narcolepsia, trastorno del sueño por trabajo en turnos y apnea obstructiva del sueño.
El modelo TxGNN predice que podría ser efectivo para **Insomnio (disease)**, con **29 ensayos clínicos** y **19 publicaciones** identificados en torno a esta dirección, aunque la gran mayoría evalúan modalidades relacionadas (fatiga, somnolencia diurna, ritmo circadiano) y no el insomnio primario de forma directa.
La plausibilidad mecanística es indirecta y controversial: el perfil promotor de vigilia del fármaco actúa en dirección opuesta al objetivo terapéutico del insomnio clásico por hiperactivación.

---

## Resumen Rápido

| Ítem | Contenido |
|------|-----------|
| Indicación Original | Sin registro sanitario en Colombia; internacionalmente: somnolencia excesiva (narcolepsia, SWSD, OSA) |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99.85% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Modafinil ejerce su efecto principal mediante la inhibición del transportador de dopamina (DAT), lo que eleva los niveles sinápticos de dopamina y activa de forma secundaria los sistemas noradrenérgico, histaminérgico y de orexina/hipocretina. Este perfil farmacológico explica su potente acción promotora de vigilia y su indicación consolidada en trastornos caracterizados por somnolencia diurna excesiva.

La relación entre la indicación original y el insomnio es paradójica pero computacionalmente plausible. TxGNN detecta solapamiento de rutas en el circuito de regulación sueño-vigilia: tanto el insomnio como los trastornos de hipersomnia comparten nodos en la red biológica (homeostasis circadiana, vías de orexina, modulación de la adenosina). El modelo asigna un puntaje elevado porque el fármaco "toca" ese circuito, no porque la dirección del efecto sea terapéutica para el insomnio. Posibles vínculos indirectos incluyen: (1) corrección del desalineamiento circadiano para consolidar la vigilia diurna y mejorar la regularidad del sueño nocturno; (2) tratamiento de la fatiga/somnolencia diurna en comorbilidades neurológicas u oncológicas, con mejora secundaria de la arquitectura del sueño; (3) normalización de la homeostasis sueño-vigilia vía orexina en subpoblaciones con disfunción circadiana.

Sin embargo, para el insomnio primario cuyo núcleo fisiopatológico es la **hiperactivación (hyperarousal)** cortical y autonómica, el efecto promotor de vigilia de modafinil actúa en dirección fundamentalmente opuesta al objetivo terapéutico. No se dispone de datos detallados sobre el mecanismo de acción completo en la base de datos consultada (Data Gap DG002). Esta limitación impide el análisis mecanístico completo y es un factor de riesgo crítico para este reposicionamiento.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|-----------------|------|--------|-------------|----------------------|
| [NCT01091974](https://clinicaltrials.gov/study/NCT01091974) | Fase 2 | Completado | 138 | CBT ± Armodafinil para insomnio y fatiga post-quimioterapia en cáncer de mama; insomnio como endpoint primario — **único ensayo con insomnio como objetivo directo y alta relevancia** |
| [NCT01019187](https://clinicaltrials.gov/study/NCT01019187) | Fase 2 | Completado | 226 | TCA ± Armodafinil para insomnio y fatiga en sobrevivientes de cáncer post-quimioterapia; evalúa eficacia de CBT y fármaco en reducción de insomnio |
| [NCT01011218](https://clinicaltrials.gov/study/NCT01011218) | Fase 2 | Completado | 70 | Terapia conductual breve ± Armodafinil 150 mg/día para insomnio en pacientes con cáncer de mama; 4 brazos de randomización |
| [NCT00124384](https://clinicaltrials.gov/study/NCT00124384) | Fase 4 | Completado | 40 | **Modafinil vs. placebo en insomnio primario** ± CBT-I; examina función diurna e intensidad del insomnio — única evidencia directa con Modafinil en insomnio primario |
| [NCT02552303](https://clinicaltrials.gov/study/NCT02552303) | NA | Completado | 39 | Armodafinil ± CBT-I para insomnio comórbido con trastorno respiratorio del sueño (OSA); evalúa continuidad del sueño y adherencia a CPAP |
| [NCT01965925](https://clinicaltrials.gov/study/NCT01965925) | Fase 4 | Completado | 18 | Modafinil para disfunción circadiana y cognitiva en trastorno bipolar estable; solapamiento entre desregulación circadiana e insomnio |
| [NCT06404086](https://clinicaltrials.gov/study/NCT06404086) | Fase 2 | Completado | 830 | RECOVER-SLEEP: plataforma de intervenciones para trastornos del sueño en secuelas post-COVID (PASC); protocolo flexible multiintervención |
| [NCT06404099](https://clinicaltrials.gov/study/NCT06404099) | Fase 2 | Activo (no recluta) | 361 | RECOVER-SLEEP continuación: evaluación comparativa de intervenciones para disturbios del sueño en PASC |
| [NCT01080807](https://clinicaltrials.gov/study/NCT01080807) | Fase 4 | Completado | 385 | Armodafinil 150 mg para somnolencia excesiva en trastorno del sueño por turnos (SWD); mejora de condición clínica al final del turno |
| [NCT00626210](https://clinicaltrials.gov/study/NCT00626210) | Fase 4 | Terminado | 2 | Modafinil para trastornos sueño-vigilia en adultos mayores; terminado prematuramente por reclutamiento insuficiente |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [18729534](https://pubmed.ncbi.nlm.nih.gov/18729534/) | 2008 | Revisión Basada en Evidencia | *Drugs* | Revisión comprehensiva de usos aprobados e investigacionales de modafinil; cubre ECA doble ciego en somnolencia excesiva, fatiga y cognición en múltiples condiciones |
| [27010071](https://pubmed.ncbi.nlm.nih.gov/27010071/) | 2016 | Revisión Sistemática y Metaanálisis | *Parkinsonism & Related Disorders* | Intervenciones farmacológicas para somnolencia diurna y trastornos del sueño en Parkinson; evalúa nivel de evidencia de modafinil vs. comparadores |
| [22021174](https://pubmed.ncbi.nlm.nih.gov/22021174/) | 2011 | Revisión Sistemática (MDS-EBM) | *Movement Disorders* | Actualización MDS sobre tratamientos de síntomas no motores en Parkinson, incluyendo insomnio y somnolencia; revisión de máxima jerarquía metodológica |
| [24312590](https://pubmed.ncbi.nlm.nih.gov/24312590/) | 2013 | Revisión / Metaanálisis | *PLoS ONE* | Eficacia de modafinil en fatiga y somnolencia excesiva en trastornos neurológicos; resultados inconsistentes entre estudios; señala perfil de seguridad favorable |
| [39535843](https://pubmed.ncbi.nlm.nih.gov/39535843/) | 2024 | Revisión | *Expert Opinion on Pharmacotherapy* | Manejo farmacológico y no farmacológico de trastornos del sueño en Parkinson; modafinil mencionado como opción para somnolencia diurna |
| [15824337](https://pubmed.ncbi.nlm.nih.gov/15824337/) | 2005 | ECA Aleatorizado | *Neurology* | Modafinil para fatiga en esclerosis múltiple; ECA doble ciego placebo-controlado; no mostró diferencia significativa en fatiga global aunque sí en fatiga subjetiva leve |
| [18219235](https://pubmed.ncbi.nlm.nih.gov/18219235/) | 2008 | ECA Aleatorizado | *J Head Trauma Rehabilitation* | Modafinil para fatiga y somnolencia excesiva en traumatismo craneoencefálico crónico; evidencia de efecto moderado sobre somnolencia objetiva |
| [24272458](https://pubmed.ncbi.nlm.nih.gov/24272458/) | 2014 | Revisión | *Neurotherapeutics* | Tratamiento de trastornos del sueño en Parkinson; CBT e iluminoterapia señalados para insomnio; modafinil evaluado indirectamente |
| [18805301](https://pubmed.ncbi.nlm.nih.gov/18805301/) | 2008 | Revisión | *Revue Neurologique* | Narcolepsia con cataplejía; modafinil como tratamiento estándar para somnolencia diurna; menciona insomnio de mantenimiento como síntoma comórbido |
| [17181377](https://pubmed.ncbi.nlm.nih.gov/17181377/) | 2006 | Revisión | *Drugs* | Trastorno del sueño por trabajo en turnos; modafinil como tratamiento de primera línea; discute la disrupción del ritmo circadiano como factor común con insomnio |

---

## Consideraciones de Seguridad

Actualmente no se dispone de datos de advertencias, contraindicaciones ni interacciones farmacológicas en este Evidence Pack (DG001: falta de prospecto oficial; DDI: no encontrado).

> Consultar el prospecto para información de seguridad.

**Nota de alerta mecanística:** Dado que modafinil es un agente promotor de vigilia, existe riesgo inherente de **agravar el insomnio** en pacientes con hiperactivación cortical, que es la presentación más frecuente del insomnio primario. Este riesgo debe evaluarse explícitamente en cualquier diseño de ensayo clínico antes de avanzar.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción TxGNN refleja solapamiento computacional en la red sueño-vigilia, pero la dirección farmacológica de modafinil (promotor de vigilia) es opuesta al objetivo terapéutico del insomnio primario por hiperactivación; la evidencia directa es escasa (un único ensayo Phase 4 con n=40 en insomnio primario, NCT00124384), y el fármaco no cuenta con registro sanitario en Colombia ni datos de seguridad validados localmente.

**Para avanzar se necesita:**

- **Datos de MOA completos (DG002):** Confirmar si existe subpoblación (p. ej., insomnio con somnolencia diurna comórbida, narcolepsia, insomnio post-COVID con disfunción circadiana) donde el efecto promotor de vigilia sea terapéuticamente coherente con el objetivo
- **Resultados de NCT00124384:** Obtener publicación primaria del ensayo Phase 4 sobre modafinil en insomnio primario para cuantificar eficacia real y dirección del efecto
- **Prospecto oficial (DG001):** Recuperar advertencias y contraindicaciones de INVIMA o FDA para completar evaluación de seguridad S1
- **Definición de subpoblación objetivo:** Distinguir insomnio primario (contraindicado mecanísticamente) de insomnio comórbido con fatiga/SDE (potencialmente viable), insomnio post-COVID, o insomnio en pacientes oncológicos post-quimioterapia
- **Revisión de datos de NCT06404086/NCT06404099 (RECOVER-SLEEP):** Extraer brazo de modafinil/armodafinil si aplica, dada la relevancia emergente del insomnio post-COVID
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

