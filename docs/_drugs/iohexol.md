---
layout: default
title: Iohexol
parent: 僅模型預測 (L5)
nav_order: 96
evidence_level: L5
indication_count: 2
---

# Iohexol
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

El skill de TxGNN cubre flujos de entrenamiento y despliegue. La tarea actual es generación de informe desde un Evidence Pack, regida por el prompt v5 del sistema. Procedo directamente.

---

# IOHEXOL: De Agente de Contraste Radiológico a Insomnio

## Resumen en Una Frase

Iohexol es un agente de contraste yodado no iónico utilizado exclusivamente en procedimientos de diagnóstico por imagen (tomografía computarizada, angiografía, mielografía), sin indicación terapéutica aprobada en Colombia.
El modelo TxGNN predice que podría ser efectivo para **Insomnio**, con un puntaje de **99.87%**.
Sin embargo, esta predicción cuenta con **0 ensayos clínicos** y **0 publicaciones** de respaldo, y representa con alta probabilidad un falso positivo del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Sin indicación terapéutica aprobada en Colombia |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99.87% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos formales sobre el mecanismo de acción provenientes de DrugBank. No obstante, iohexol es un agente de contraste yodado no iónico ampliamente conocido: su mecanismo es **estrictamente físico**, basado en la atenuación de rayos X para mejorar la visualización de estructuras anatómicas en estudios de imagen. No posee actividad farmacológica sobre el sistema nervioso central, no se une a receptores del sueño (GABA-A, histamina H₁, orexina, melatonina) ni modula ningún neurotransmisor relacionado con el ciclo sueño-vigilia.

El elevado puntaje TxGNN (0.9987) es un **falso positivo típico de redes neuronales sobre grafos de conocimiento**: iohexol aparece en una gran variedad de contextos clínicos (medición de tasa de filtración glomerular, procedimientos intervencionistas guiados por imagen, estudios cardiovasculares), lo que genera un nodo de muy alta conectividad en el grafo. Esta conectividad infla artificialmente la puntuación sin reflejar ningún vínculo biológico real con el insomnio.

En conclusión, no existe ningún fundamento mecanístico que justifique explorar iohexol como tratamiento del insomnio. La ausencia total de ensayos clínicos y literatura específica para esta indicación confirma que la predicción carece completamente de sustento empírico.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Iohexol es un agente de diagnóstico sin actividad farmacológica CNS demostrada; no existe ninguna base biológica que justifique su uso en el tratamiento del insomnio, y la evidencia disponible es exclusivamente la predicción del modelo (L5), sin respaldo en ensayos clínicos ni publicaciones. Adicionalmente, la segunda indicación predicha —**ansiedad** (rank 2, score 99.24%)— sigue el mismo patrón de falso positivo: los 6 ensayos clínicos identificados tienen todos relevancia Grado C (iohexol fue utilizado únicamente como herramienta de medición de GFR o medio de contraste para guía de imagen, no como agente terapéutico), y la única mención de ansiedad en la literatura corresponde a un evento adverso reportado *tras* la administración de iohexol, no a un efecto terapéutico.

**Para avanzar se necesitaría:**
- Identificar un mecanismo farmacológico activo sobre el SNC (actualmente inexistente para iohexol)
- Evidencia de efecto terapéutico directo sobre el insomnio en estudios preclínicos o estudios de mecanismo
- Revisión de seguridad para administración crónica o sistémica (iohexol actualmente se usa solo de forma aguda y puntual como contraste)
- Corrección del sesgo de alta conectividad nodal en el modelo TxGNN para evitar falsos positivos en agentes de diagnóstico
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

