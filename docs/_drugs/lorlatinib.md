---
layout: default
title: Lorlatinib
parent: 僅模型預測 (L5)
nav_order: 163
evidence_level: L5
indication_count: 10
---

# Lorlatinib
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

# Lorlatinib: De Carcinoma Pulmonar ALK-positivo a Fibromatosis Gingival

## Resumen en Una Frase

Lorlatinib es un inhibidor de tirosina quinasa de tercera generación dirigido contra ALK y ROS1, ampliamente utilizado a nivel mundial para el tratamiento del carcinoma de pulmón de células no pequeñas (CPCNP) con reordenamiento ALK-positivo.
El modelo TxGNN predice que podría ser efectivo para **Fibromatosis Gingival**,
con **0 ensayos clínicos** y **0 publicaciones** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No registrado en Colombia (INVIMA); indicación global reconocida: CPCNP ALK-positivo |
| Nueva Indicación Predicha | Fibromatosis Gingival |
| Puntaje de Predicción TxGNN | 99.81% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No Comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, lorlatinib es un inhibidor de tercera generación de ALK (*anaplastic lymphoma kinase*) y ROS1, con capacidad de atravesar la barrera hematoencefálica. Su eficacia en CPCNP ALK-positivo ha sido comprobada ampliamente mediante el ensayo CROWN de Fase 3, y actúa bloqueando la señalización intracelular mediada por la quinasa ALK, que es el motor oncogénico en tumores con reordenamiento genético de ALK.

La fibromatosis gingival es una condición de proliferación fibrosa benigna del tejido gingival, generalmente asociada a mutaciones en genes como *SOS1* o *RASA1*, o secundaria a medicamentos (fenitoína, ciclosporina, antagonistas del calcio). La predicción de TxGNN podría fundamentarse en conexiones distantes dentro del grafo de conocimiento que vinculan ALK con la proliferación de células mesenquimales, ya que existen reportes aislados de sobreexpresión de ALK en algunos subtipos de fibromatosis; sin embargo, no existe ninguna evidencia directa —clínica ni preclínica— que respalde esta asociación para fibromatosis gingival específicamente.

La señal del modelo se interpreta como un artefacto de vecindad en el grafo de conocimiento más que como una hipótesis biológica validada. La ausencia total de estudios publicados impide respaldar esta predicción más allá de su naturaleza especulativa.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Citotoxicidad

Lorlatinib es un agente antineoplásico de terapia dirigida (inhibidor de tirosina quinasa ALK/ROS1 de tercera generación). Se incluye esta sección dado su perfil oncológico establecido.

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida — Inhibidor de tirosina quinasa ALK/ROS1 de tercera generación |
| Riesgo de Mielosupresión | Bajo a moderado (anemia y trombocitopenia reportadas en ensayos clínicos CROWN) |
| Clasificación de Emetogenicidad | Baja |
| Items de Monitoreo | Hemograma completo con diferencial; perfil lipídico completo (hipercolesterolemia e hipertrigliceridemia son efectos adversos frecuentes y característicos de lorlatinib); función hepática y renal; presión arterial; evaluación neurológica/cognitiva (efectos sobre el SNC como confusión, cambios del estado de ánimo y alucinaciones son propios de lorlatinib por su alta penetración cerebral) |
| Protección en Manejo | Precauciones estándar para inhibidores de tirosina quinasa de administración oral; consultar la normativa institucional vigente para el manejo de fármacos antineoplásicos |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de TxGNN para fibromatosis gingival carece por completo de evidencia clínica y preclínica directa; la señal del modelo es atribuible a conexiones distantes en el grafo de conocimiento entre ALK y la proliferación de células mesenquimales, sin respaldo biológico validado para esta indicación específica, y lorlatinib no cuenta además con registro sanitario en Colombia.

**Para avanzar se necesita:**
- Obtener datos completos del mecanismo de acción (MOA) de DrugBank para confirmar la plausibilidad biológica
- Búsqueda bibliográfica específica sobre expresión de ALK en tejido gingival fibromatoso y modelos preclínicos de fibromatosis
- Tramitar el registro sanitario ante el INVIMA como prerrequisito para cualquier uso clínico en Colombia
- Revisar si la señal de TxGNN persiste al reconfigurar el grafo de conocimiento con datos más granulares sobre fibromatosis gingival
- Considerar si indicaciones de mayor evidencia (p. ej., CPCNP ALK-positivo, neuroblastoma ALK-driven) son prioritarias para una estrategia de entrada al mercado colombiano
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

