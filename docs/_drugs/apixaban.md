---
layout: default
title: Apixaban
parent: 僅模型預測 (L5)
nav_order: 37
evidence_level: L5
indication_count: 1
---

# Apixaban
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

# APIXABAN: Evaluación Incompleta — Sin Predicciones TxGNN Disponibles

## Resumen en Una Frase

APIXABAN (DB06605) es un fármaco identificado como candidato para evaluación de reposicionamiento de fármacos.
Sin embargo, el Evidence Pack actual **no contiene indicaciones predichas por TxGNN**, no registra aprobaciones en Colombia y presenta brechas críticas de datos que impiden una evaluación completa.
No es posible generar un análisis de reposicionamiento en el estado actual del expediente.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sin datos disponibles |
| Nueva Indicación Predicha | Sin predicciones TxGNN disponibles |
| Puntaje de Predicción TxGNN | N/D |
| Nivel de Evidencia | L5 — Sin estudios reales asociados |
| Estado de Mercado en Colombia | No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | **Hold** |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El Evidence Pack de APIXABAN está incompleto en sus tres dimensiones clave: no se generaron predicciones TxGNN de nuevas indicaciones, no hay registros sanitarios activos en Colombia, y los datos de mecanismo de acción y seguridad no están disponibles. Sin indicaciones predichas, no existe base para un análisis de reposicionamiento.

**Para avanzar se necesita:**
- Ejecutar el pipeline TxGNN para generar predicciones de nuevas indicaciones (`predicted_indications`)
- Obtener datos de mecanismo de acción (MOA) desde DrugBank API — brecha **DG002 (Alta severidad)**
- Resolver las advertencias y contraindicaciones desde el prospecto oficial — brecha **DG001 (Bloqueante)**
- Verificar el estado regulatorio actualizado en INVIMA Colombia
- Consultar fuentes de interacciones farmacológicas (DDI actualmente sin resultados)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

