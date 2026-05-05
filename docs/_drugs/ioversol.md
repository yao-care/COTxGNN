---
layout: default
title: Ioversol
parent: 僅模型預測 (L5)
nav_order: 97
evidence_level: L5
indication_count: 10
---

# Ioversol
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

El skill de TxGNN-pipeline cubre gestión de pipeline multi-país y no modifica las instrucciones de generación de informes. Procedo directamente con el informe basado en el Evidence Pack.

---

# Ioversol: De Agente de Contraste Radiológico a Susceptibilidad a Osteoartritis

## Resumen en Una Frase

Ioversol es un agente de contraste yodado no iónico utilizado en procedimientos de radiología diagnóstica (tomografía computarizada, angiografía y urografía). El modelo TxGNN predice que podría ser efectivo para **Susceptibilidad a Osteoartritis**, aunque con **0 ensayos clínicos** y **0 publicaciones** que respalden directamente esta dirección. La predicción se fundamenta exclusivamente en la proximidad topológica dentro del grafo de conocimiento del modelo, sin respaldo biológico o clínico identificable.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Agente de contraste radiológico (inferido; sin registros sanitarios en Colombia) |
| Nueva Indicación Predicha | Susceptibilidad a Osteoartritis |
| Puntaje de Predicción TxGNN | 99.67% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de Ioversol. Según la información conocida, Ioversol es un agente de contraste yodado no iónico de baja osmolalidad (clase triyodobenceno), cuya función consiste en aumentar la atenuación de rayos X en los tejidos para mejorar la visualización en procedimientos diagnósticos. No posee actividad farmacológica intrínseca conocida sobre tejido cartilaginoso, sinoviocitos ni sobre las vías moleculares asociadas a la osteoartritis (MMP, IL-1β, TNF-α, TGF-β).

La susceptibilidad a osteoartritis está mediada por la predisposición genética y fenotípica a la degradación del cartílago articular, la inflamación sinovial y la remodelación ósea subcondral. No existe ninguna hipótesis mecanística publicada que conecte las propiedades químicas de Ioversol con la modulación de estos procesos. La única relación identificable es que Ioversol puede emplearse como medio de contraste en artrogramas (inyección intraarticular para imagen diagnóstica), lo que genera co-ocurrencia con nodos de "osteoartritis" en el grafo de conocimiento de TxGNN sin implicar causalidad terapéutica.

El alto puntaje TxGNN (99.67%) probablemente refleja esta proximidad topológica en el grafo, no una acción terapéutica sobre el tejido articular. Esta interpretación se refuerza al observar que los ensayos clínicos disponibles para la indicación relacionada "osteoartritis" (rank 2) corresponden a procedimientos de embolización de arterias geniculares (GAE) que utilizan Lipiodol —un compuesto distinto con actividad embólica— donde Ioversol aparece únicamente como agente de contraste auxiliar para guía vascular intraprocedimiento, y no como sustancia terapéutica.

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
La predicción de TxGNN para susceptibilidad a osteoartritis carece de cualquier respaldo clínico o preclínico; la asociación en el grafo de conocimiento se origina en el uso diagnóstico de Ioversol en procedimientos articulares —no en una acción farmacológica sobre el tejido— y no existe hipótesis mecanística biológicamente plausible que justifique avanzar hacia etapas de investigación.

**Para avanzar se necesita:**
- Confirmar el mecanismo de acción oficial mediante consulta a la API de DrugBank (brecha DG002)
- Obtener el prospecto oficial para revisar advertencias, contraindicaciones e indicación aprobada (brecha DG001)
- Establecer una hipótesis mecanística plausible que conecte Ioversol con la fisiopatología de la osteoartritis de forma independiente al efecto de embolización de otros agentes yodados
- Estudios preclínicos in vitro/in vivo sobre efectos de Ioversol en cartílago, sinoviocitos o mediadores inflamatorios articulares, previos a cualquier consideración clínica
- Revisión sistemática del contexto de aparición de Ioversol en la literatura de osteoartritis para confirmar si se trata exclusivamente de uso diagnóstico auxiliar
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

