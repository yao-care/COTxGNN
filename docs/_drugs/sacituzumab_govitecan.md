---
layout: default
title: Sacituzumab Govitecan
parent: 僅模型預測 (L5)
nav_order: 211
evidence_level: L5
indication_count: 4
---

# Sacituzumab Govitecan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Sacituzumab Govitecan: De Cáncer de Mama Triple Negativo a Osteoporosis Inducida por Fármacos

## Resumen en Una Frase

Sacituzumab govitecan (Trodelvy®) es un conjugado anticuerpo-fármaco (ADC) anti-Trop-2 aprobado en múltiples países para el tratamiento del cáncer de mama triple negativo (TNBC) y el carcinoma urotelial avanzado.
El modelo TxGNN predice que podría ser efectivo para **osteoporosis inducida por fármacos**, con un puntaje de confianza del 99.78%.
Sin embargo, actualmente **no existe ningún ensayo clínico ni publicación científica** que respalde esta nueva dirección, lo que limita severamente la solidez de la predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer de mama triple negativo (TNBC); carcinoma urotelial avanzado |
| Nueva Indicación Predicha | Osteoporosis inducida por fármacos |
| Puntaje de Predicción TxGNN | 99.78% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información disponible en la literatura médica, Sacituzumab govitecan es un ADC (antibody-drug conjugate) que combina un anticuerpo monoclonal anti-Trop-2 con SN-38 (el metabolito activo del irinotecan). La fracción anticuerpo se une específicamente al antígeno Trop-2, que se sobreexpresa en múltiples tumores sólidos, mientras que el SN-38 inhibe la topoisomerasa I provocando daño en el ADN y muerte celular tumoral.

La osteoporosis inducida por fármacos es una condición metabólica ósea secundaria, típicamente causada por corticosteroides, inhibidores de aromatasa, inhibidores de la bomba de protones o antiepilépticos. Estos agentes actúan sobre el metabolismo del calcio, la función de los osteoblastos y osteoclastos, o sobre la absorción intestinal de minerales — mecanismos completamente ajenos a la vía Trop-2/SN-38.

La relación mecanística entre sacituzumab govitecan y la osteoporosis inducida por fármacos es **extremadamente débil**. El tejido óseo no expresa Trop-2 de forma significativa, y el SN-38 no tiene ningún efecto conocido sobre la densidad ósea, la diferenciación osteoblástica ni la regulación del metabolismo mineral. La predicción del modelo TxGNN probablemente refleja conexiones indirectas en el grafo de conocimiento (knowledge graph) más que una relación biológica real.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

Sacituzumab govitecan no cuenta con ningún registro sanitario activo en Colombia (INVIMA). El fármaco no está comercializado en el país.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | ADC citotóxico convencional (anti-Trop-2 + SN-38, inhibidor de topoisomerasa I) |
| Riesgo de Mielosupresión | Alto (neutropenia severa es la toxicidad limitante de dosis; se requiere G-CSF profiláctico en muchos protocolos) |
| Clasificación de Emetogenicidad | Moderada a alta (componente SN-38 con potencial emetogénico significativo) |
| Ítems de Monitoreo | Hemograma completo con diferencial (antes de cada ciclo), función hepática (ALT/AST/bilirrubinas), función renal, electrolitos, glucosa |
| Protección en Manejo | Requiere manejo bajo normativas de fármacos citotóxicos: cabina de bioseguridad, EPP completo, eliminación como residuo citotóxico especial |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de TxGNN carece de respaldo empírico (nivel L5: solo predicción del modelo, sin estudios reales) y el análisis mecanístico indica una relación extremadamente débil entre el perfil farmacológico de sacituzumab govitecan (ADC anti-Trop-2/SN-38 para oncología) y la fisiopatología de la osteoporosis inducida por fármacos (condición metabólica ósea sin expresión relevante de Trop-2). Se recomienda no avanzar en esta indicación sin evidencia experimental que demuestre un nexo biológico plausible.

**Para reconsiderar se necesitaría:**
- Datos de expresión de Trop-2 en osteoblastos u osteoclastos en contexto de osteoporosis inducida
- Estudios preclínicos (in vitro/in vivo) que demuestren efecto de SN-38 o del ADC sobre el metabolismo óseo
- Justificación alternativa para la señal del modelo (p. ej., artefacto de co-ocurrencia en el KG con fármacos que causan osteoporosis como efecto adverso)
- Datos completos de MOA (DrugBank) para descartar efectos secundarios óseos no documentados
- Perfil de seguridad completo (INVIMA/TFDA package insert) antes de cualquier evaluación clínica
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

