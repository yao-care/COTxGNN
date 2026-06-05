---
layout: default
title: Brigatinib
parent: 僅模型預測 (L5)
nav_order: 72
evidence_level: L5
indication_count: 10
---

# Brigatinib
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

El skill confirma el contexto del pipeline TxGNN. Procedo ahora a generar el informe de evaluación completo para BRIGATINIB siguiendo el formato del sistema.

---

# Brigatinib: De CPNM ALK-Positivo a Fibromatosis Gingival

## Resumen en Una Frase

Brigatinib es un inhibidor de tirosina quinasa de segunda generación, utilizado internacionalmente para el tratamiento del cáncer de pulmón de células no pequeñas (CPNM) con reordenamiento ALK-positivo, con eficacia demostrada en los ensayos pivotales de la serie ALTA. El modelo TxGNN predice que podría ser efectivo para **Fibromatosis Gingival**, con **0 ensayos clínicos** y **0 publicaciones** que actualmente respaldan esta dirección específica. El análisis mecanístico indica que esta predicción corresponde con alta probabilidad a un falso positivo del modelo de grafos, sin base biológica real entre brigatinib y esta enfermedad.

---

## Resumen Rápido

| Ítem | Contenido |
|------|-----------|
| Indicación Original | CPNM ALK-positivo (no registrado en Colombia) |
| Nueva Indicación Predicha | Fibromatosis Gingival |
| Puntaje de Predicción TxGNN | 99.89% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de brigatinib en los registros regulatorios colombianos. Según la información publicada en la literatura científica, brigatinib es un inhibidor selectivo de múltiples tirosinas quinasas —principalmente ALK (anaplastic lymphoma kinase), ROS1 y EGFR con mutaciones de resistencia— cuya eficacia en CPNM ALK-positivo ha sido demostrada en los ensayos clínicos de Fase 3 ALTA-1L, logrando una supervivencia libre de progresión superior frente a crizotinib tanto en primera línea como en pacientes resistentes.

La fibromatosis gingival, sin embargo, es una condición de proliferación fibroblástica del tejido gingival causada principalmente por mutaciones en genes como **GTSE1, SOS1 y SOS2**. Se trata de una anomalía estructural del tejido conectivo sin intersección conocida con la vía de señalización ALK ni con los otros objetivos farmacológicos de brigatinib.

El puntaje alto del modelo TxGNN (99.89%, rango #1343 global) para esta indicación refleja muy probablemente una señal de **propagación distante en el grafo de conocimiento médico** a través de nodos compartidos de tejido conectivo, y no una conexión mecanística real. No existe evidencia clínica, preclínica ni publicaciones científicas que respalden el uso de brigatinib en fibromatosis gingival, por lo que esta predicción se clasifica como falso positivo del sistema en el análisis actual.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Citotoxicidad

| Ítem | Contenido |
|------|-----------|
| Clasificación de Citotoxicidad | Terapia dirigida — inhibidor de tirosina quinasa ALK/ROS1 de segunda generación |
| Riesgo de Mielosupresión | Moderado (anemia, neutropenia y trombocitopenia reportadas en estudios clínicos de CPNM ALK+) |
| Clasificación de Emetogenicidad | Baja a moderada |
| Ítems de Monitoreo | Hemograma completo con diferencial, transaminasas (ALT/AST), bilirrubina, creatinina sérica, perfil lipídico, glucosa en ayunas, amilasa y lipasa |
| Protección en Manejo | Requiere seguir protocolos de manejo seguro de antineoplásicos orales (inhibidores de tirosina quinasa) |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción TxGNN para fibromatosis gingival carece completamente de respaldo mecanístico y evidencia científica: la enfermedad está causada por mutaciones en vías (GTSE1/SOS1/SOS2) sin relación con ALK, no existe ningún ensayo clínico ni publicación que respalde esta dirección, y el rango global (#1343) sugiere que el modelo no identifica una señal de reposicionamiento genuina. Adicionalmente, brigatinib no cuenta con registro sanitario INVIMA en Colombia, lo que representa una barrera regulatoria adicional para cualquier uso clínico.

**Para avanzar se necesita:**
- Obtener el prospecto oficial (TFDA/FDA) para completar los datos de MOA, advertencias y contraindicaciones (actualmente no disponibles en el sistema)
- Iniciar gestión de registro INVIMA si se contempla comercialización o uso compasivo en Colombia
- Evaluar de forma independiente las indicaciones con mayor potencial mecanístico: la indicación de **rango #8** (tumores con ALK+ / neuroendocrinos pulmonares, evidencia **L4**) presenta base mecanística más sólida para exploración como pregunta de investigación
- Investigar el perfil emergente en **schwannomatosis relacionada con NF2** (detectado en análisis de rango #10): ensayo clínico prospectivo publicado en NEJM ([PMID 38904277](https://pubmed.ncbi.nlm.nih.gov/38904277/)) evidencia respuesta tumoral vía inhibición de FAK por brigatinib, independiente de ALK — este hallazgo merece una evaluación independiente con nivel de evidencia **L3**
- Considerar la señal de seguridad de **síndrome de lisis tumoral fatal** reportada con brigatinib ([PMID 34987411](https://pubmed.ncbi.nlm.nih.gov/34987411/)) en la evaluación de riesgo para cualquier indicación nueva
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

