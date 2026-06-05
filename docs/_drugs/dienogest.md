---
layout: default
title: Dienogest
parent: 僅模型預測 (L5)
nav_order: 100
evidence_level: L5
indication_count: 10
---

# Dienogest
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

# Dienogest: De Endometriosis a Amenorrea

## Resumen en Una Frase

Dienogest es un progestágeno de cuarta generación (conocido comercialmente como Visanne®), utilizado a nivel internacional para el tratamiento de la endometriosis, aunque actualmente no cuenta con registros sanitarios en Colombia.
El modelo TxGNN predice que podría ser relevante para el manejo de la **Amenorrea**, con **4 ensayos clínicos** que actualmente respaldan esta dirección.
Cabe señalar que la amenorrea figura como un efecto farmacológico esperado del Dienogest en el contexto de endometriosis, lo que otorga una interpretación mecanística particular —y paradójica— a esta predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Endometriosis (referencial; sin registros aprobados en Colombia) |
| Nueva Indicación Predicha | Amenorrea |
| Puntaje de Predicción TxGNN | 99.71% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción desde DrugBank. Según la información conocida por los ensayos clínicos disponibles, Dienogest es un progestágeno de cuarta generación con alta selectividad por el receptor de progesterona y actividad antiandrogénica moderada. En su uso validado para endometriosis, actúa suprimiendo la ovulación y la proliferación endometrial mediante la inhibición del eje hipotálamo-hipófisis-ovario, lo que frecuentemente resulta en amenorrea como efecto farmacológico deseado y marcador de eficacia terapéutica.

La relación entre Dienogest y amenorrea es, por tanto, bidireccional y mecanísticamente compleja: el fármaco **induce** amenorrea como parte de su eficacia en endometriosis, en lugar de **tratar** la amenorrea primaria como condición independiente. El ensayo NCT07204093 aborda directamente este fenómeno al evaluar estrategias de add-back de estradiol transdérmico para gestionar la sintomatología hipoestrógénica derivada de la amenorrea inducida por Dienogest, lo que representa la línea de evidencia más directamente relacionada con la predicción.

Es crucial distinguir el subtipo de amenorrea al interpretar esta predicción: (1) como indicador de eficacia terapéutica en endometriosis, la asociación está bien respaldada; (2) como tratamiento de amenorrea primaria o funcional de origen diferente, la dirección farmacológica es opuesta y carece de sustento mecanístico. El TxGNN probablemente captura esta asociación bidireccional en el grafo de conocimiento, lo que requiere una validación clínica dirigida antes de cualquier decisión de desarrollo.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT07204093](https://clinicaltrials.gov/study/NCT07204093) | N/A | Activo (no reclutando) | 138 | Compara estradiol transdérmico + Dienogest vs. drospirenona en endometriosis; evalúa directamente la gestión de síntomas hipoestrógénicos —incluyendo amenorrea inducida— como endpoint principal de satisfacción del paciente |
| [NCT07164183](https://clinicaltrials.gov/study/NCT07164183) | Fase 3 | Reclutando | 290 | RCT de no inferioridad: Indinol Forto® 200 mg vs. Visanne® 2 mg en endometriosis; si los endpoints menstruales son primarios, este estudio podría escalar la evidencia a nivel L1 |
| [NCT04495855](https://clinicaltrials.gov/study/NCT04495855) | N/A | Completado | 968 | Estudio observacional real-world de Visanne® en endometriosis (n=968); la amenorrea figura como resultado secundario y provee datos de incidencia en práctica clínica habitual |
| [NCT02425462](https://clinicaltrials.gov/study/NCT02425462) | N/A | Completado | 895 | Cohorte prospectiva en mujeres asiáticas con endometriosis; foco en calidad de vida y seguridad a largo plazo; datos de amenorrea como variable derivada secundaria |

---

## Información de Mercado en Colombia

Dienogest no cuenta con registros sanitarios vigentes ante el INVIMA. El fármaco no está comercializado en Colombia en ninguna de sus formas farmacéuticas.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de TxGNN refleja una asociación farmacológica real pero de dirección paradójica — Dienogest induce amenorrea como efecto terapéutico en endometriosis y no la trata como condición primaria. Sumado a la ausencia de registros sanitarios en Colombia y a la falta de evidencia directa para amenorrea como indicación independiente, no es posible avanzar en el desarrollo de este candidato en la etapa actual.

**Para avanzar se necesita:**
- Clarificación del subtipo de amenorrea objetivo: inducida por progestágenos (amenorrea terapéutica) vs. amenorrea primaria vs. amenorrea funcional hipotalámica
- Datos completos de mecanismo de acción (MOA) desde DrugBank API
- Información de seguridad completa: advertencias, contraindicaciones y perfil de interacciones del prospecto oficial
- Estrategia regulatoria para registro inicial en Colombia ante el INVIMA
- Resultados del ensayo NCT07164183 (Fase 3, actualmente en reclutamiento) para confirmar si los endpoints menstruales son incluidos como criterios de evaluación primarios
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

