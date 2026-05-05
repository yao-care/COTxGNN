---
layout: default
title: Galcanezumab
parent: 僅模型預測 (L5)
nav_order: 82
evidence_level: L5
indication_count: 3
---

# Galcanezumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Galcanezumab: De Indicacion No Registrada en Colombia a Deficiencia de Cofactor 2 de Heparina

## Resumen en Una Frase

Galcanezumab es un anticuerpo monoclonal anti-CGRP (péptido relacionado con el gen de la calcitonina) que actúa sobre la vía de regulación neurovascular; no cuenta con indicaciones registradas ni registros sanitarios activos en Colombia según los datos disponibles. El modelo TxGNN predice que podría ser efectivo para **Deficiencia de Cofactor 2 de Heparina**, sin embargo, actualmente no existen **ensayos clínicos ni publicaciones** que respalden esta dirección, y el análisis mecanístico revela una **ausencia de relación biológica plausible** entre el mecanismo del fármaco y las enfermedades predichas.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sin datos registrados en Colombia |
| Nueva Indicación Predicha | Deficiencia de Cofactor 2 de Heparina (*heparin cofactor 2 deficiency*) |
| Puntaje de Predicción TxGNN | 99.50% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

El campo de mecanismo de acción formal está marcado como dato faltante en este conjunto de datos; sin embargo, el análisis de racionalidad mecanística del Evidence Pack confirma que Galcanezumab se une y neutraliza el CGRP (péptido relacionado con el gen de la calcitonina), modulando la vía de regulación neurovascular. Esta es la base de su uso en la prevención de migraña y cefalea en racimos, aunque dicha indicación no aparece registrada en Colombia.

La Deficiencia de Cofactor 2 de Heparina (HC2) es un trastorno de la coagulación: HC2 es un inhibidor de serina proteasa que suprime la trombina a través de la vía del dermatán sulfato. Su fisiopatología pertenece íntegramente al sistema de coagulación, un dominio biológico completamente independiente de la señalización neuropeptídica del CGRP.

Según el análisis del Evidence Pack, la relación mecanística entre galcanezumab y las tres indicaciones predichas es **extremadamente baja o inexistente**: inhibir el CGRP no genera ningún efecto conocido sobre la actividad del cofactor 2 de heparina, sobre la función de antitrombina ni sobre la regulación del Factor V. Las vías biológicas son ortogonales entre sí, lo que sugiere que la puntuación alta del modelo TxGNN refleja posiblemente artefactos de la representación gráfica del conocimiento más que una relación farmacológica real.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para ninguna de las indicaciones predichas (*heparin cofactor 2 deficiency*, *antithrombin deficiency type 2*, *factor 5 excess with spontaneous thrombosis*).

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para ninguna de las indicaciones predichas.

---

## Información de Mercado en Colombia

Galcanezumab no cuenta con registros sanitarios activos en Colombia. El fármaco no ha sido aprobado ni comercializado en el país según los datos de INVIMA disponibles en este análisis.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Las tres indicaciones predichas por TxGNN corresponden a trastornos de la coagulación cuya fisiopatología es biológicamente orthogonal al mecanismo de acción de galcanezumab (inhibición de CGRP en la vía neurovascular). No existe ningún ensayo clínico, publicación científica ni fundamento mecanístico que respalde el reposicionamiento en esta dirección; la evidencia se limita únicamente a la predicción computacional del modelo (Nivel L5).

**Para avanzar se necesita:**
- Obtener el mecanismo de acción formal (MOA) desde DrugBank API para descartar efectos pleiotrópicos no documentados
- Obtener datos completos de seguridad y contraindicaciones desde el prospecto oficial (FDA/EMA/INVIMA)
- Revisar si existe alguna hipótesis publicada que conecte la señalización de CGRP con trastornos trombóticos o de la coagulación
- Considerar re-ejecutar el modelo TxGNN con datos de entrada enriquecidos (proteínas diana, rutas de señalización completas) para mejorar la especificidad de las predicciones y reducir falsos positivos en enfermedades biológicamente no relacionadas
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

