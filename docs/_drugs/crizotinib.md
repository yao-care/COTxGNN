---
layout: default
title: Crizotinib
parent: 僅模型預測 (L5)
nav_order: 92
evidence_level: L5
indication_count: 10
---

# Crizotinib
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

# Crizotinib: De Cáncer de Pulmón No Microcítico a Fibromatosis Gingival

## Resumen en Una Frase

Crizotinib es un inhibidor de tirosina quinasa dirigido contra los receptores ALK, ROS1 y c-MET, aprobado originalmente para el tratamiento del cáncer de pulmón no microcítico (CPNM) con reordenamientos genéticos ALK+ o ROS1+. El modelo TxGNN predice que podría ser efectivo para la **Fibromatosis Gingival**, sin embargo, actualmente **no existen ensayos clínicos ni publicaciones científicas** que respalden esta dirección. El alto puntaje del modelo (99.81%) es probablemente resultado de propagación de proximidad en la red de grafos biológica, y no de una conexión mecanística real.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer de pulmón no microcítico (CPNM) con reordenamiento ALK+/ROS1+ (inferido de literatura; sin registro en Colombia) |
| Nueva Indicación Predicha | Fibromatosis Gingival |
| Puntaje de Predicción TxGNN | 99.81% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en este Evidence Pack. Sin embargo, según la información disponible en la literatura científica incluida en este informe, Crizotinib es un inhibidor competitivo de ATP que bloquea las tirosina quinasas receptoras ALK (quinasa de linfoma anaplásico), ROS1 y c-MET. Su eficacia en el cáncer de pulmón no microcítico con reordenamientos EML4-ALK y fusiones ROS1 ha sido ampliamente demostrada y cuenta con aprobación de la FDA.

La fibromatosis gingival es una condición caracterizada por el engrosamiento progresivo del tejido gingival, asociada principalmente a mutaciones en los genes SOS1 y HRAS que activan vías de señalización de crecimiento celular. Los blancos terapéuticos de Crizotinib (ALK, ROS1, c-MET) no tienen una relación mecanística conocida con las vías SOS1/HRAS responsables de la fibromatosis gingival.

El análisis de racionalidad del reposicionamiento concluye que la alta puntuación TxGNN (0.998) es probablemente un **falso positivo por propagación de proximidad en la red de grafos biológica**, y no refleja una conexión biológica real entre el mecanismo de acción del fármaco y la fisiopatología de la fibromatosis gingival. No existe evidencia clínica, preclínica ni mecanística que sustente este reposicionamiento en la actualidad.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para Crizotinib en Fibromatosis Gingival.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para Crizotinib en Fibromatosis Gingival.

---

## Información de Mercado en Colombia

Crizotinib no cuenta con registros sanitarios activos ante el INVIMA. El fármaco no está comercializado en el mercado colombiano a la fecha de corte de datos (2026-06-04).

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida — Inhibidor de tirosina quinasa ALK/ROS1/c-MET (no citotóxico convencional) |
| Riesgo de Mielosupresión | Bajo a moderado (neutropenia reportada; menor incidencia que quimioterapia citotóxica tradicional) |
| Clasificación de Emetogenicidad | Baja a moderada (antineoplásico oral; riesgo menor al de platinos o antraciclinas) |
| Items de Monitoreo | Función hepática (ALT/AST/bilirrubina), hemograma completo, ECG con intervalo QT, radiografía o TC de tórax (monitoreo de neumonitis intersticial) |
| Protección en Manejo | Requiere medidas estándar de protección para antineoplásicos orales; manipulación con guantes; evitar trituración de cápsulas |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La fibromatosis gingival es causada por mutaciones en SOS1/HRAS que no tienen intersección mecanística conocida con los blancos terapéuticos de Crizotinib (ALK/ROS1/MET). La ausencia total de ensayos clínicos y literatura específica, combinada con el nivel de evidencia L5, indica que la predicción TxGNN es muy probablemente un falso positivo por propagación de proximidad en la red de grafos y no debe avanzar a evaluación clínica sin hipótesis mecanística sustentada.

**Para avanzar se necesita:**
- Completar el mecanismo de acción (MOA) de Crizotinib mediante consulta a la API de DrugBank (DB08865)
- Descargar y analizar el prospecto oficial para obtener advertencias, contraindicaciones e interacciones farmacológicas
- Realizar búsqueda bibliográfica exploratoria sobre posible rol de c-MET o ALK en fibroblastos gingivales o en vías de señalización HRAS/SOS1
- Verificar si existe evidencia de reposicionamiento en otras fibromatosis (p. ej., fibromatosis désmoides) donde c-MET ha sido investigado, antes de descartar definitivamente
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

