---
layout: default
title: Articaina
parent: 僅模型預測 (L5)
nav_order: 41
evidence_level: L5
indication_count: 0
---

# Articaina
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Articaína: Evaluación Detenida — Datos Insuficientes para Predicción de Reposicionamiento

## Resumen en Una Frase

Articaína (Articaine) es un anestésico local de tipo amida conocido principalmente por su uso en procedimientos odontológicos, aunque el Evidence Pack recibido no registra indicaciones originales formalizadas.
El modelo TxGNN **no generó predicciones de nuevas indicaciones** para este compuesto en la ejecución actual,
por lo que no existe evidencia de ensayos clínicos ni literatura asociada a una indicación candidata concreta.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | No registrada en el Evidence Pack |
| Nueva Indicación Predicha | Sin predicción disponible (TxGNN no generó candidatos) |
| Puntaje de Predicción TxGNN | No disponible |
| Nivel de Evidencia | L5 — Solo predicción del modelo, sin estudios reales (y en este caso, sin predicción) |
| Estado de Mercado en Colombia | ✗ No comercializado (0 registros sanitarios) |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | **Hold** |

---

## Información de Mercado en Colombia

Articaína no cuenta con ningún registro sanitario activo en Colombia según los datos consultados el 29 de marzo de 2026. El medicamento figura como **no comercializado** en el mercado colombiano bajo este INN.

> No hay registros sanitarios disponibles para mostrar.

---

## Consideraciones de Seguridad

La consulta de interacciones farmacológicas (DDI) no arrojó resultados. La información de advertencias y contraindicaciones no fue recuperada en esta ejecución del pipeline.

> Consultar el prospecto oficial para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El pipeline TxGNN no generó ninguna indicación candidata para Articaína en esta ejecución, y el Evidence Pack presenta brechas críticas en los datos de mecanismo de acción, indicaciones originales y seguridad. Sin una predicción de indicación, no es posible construir un argumento de reposicionamiento ni identificar evidencia de respaldo.

**Para avanzar se necesita:**

- **Resolver DG002 (Alta prioridad):** Recuperar el mecanismo de acción completo desde DrugBank (el query_log confirma que DrugBank devolvió 1 resultado — verificar por qué `original_moa` quedó vacío).
- **Resolver DG001 (Bloqueante):** Descargar y parsear el prospecto oficial (tfda_package_insert devolvió 1 resultado en el log — revisar por qué las advertencias y contraindicaciones no se extrajeron).
- **Re-ejecutar TxGNN:** Con los datos de MOA y categorías DrugBank completos, el modelo podría generar candidatos de indicación. La ausencia de predicciones puede estar relacionada con la falta de nodos de entrada en el knowledge graph.
- **Verificar INN normalizado:** Confirmar que el identificador "ARTICAINA" (con mayúsculas, sin tilde) esté correctamente mapeado en el vocabulario del pipeline; la variante correcta en inglés es "articaine" y en español "articaína".
- **Registros sanitarios en Colombia:** Evaluar si el producto se comercializa bajo combinaciones fijas (p. ej., articaína + epinefrina) que podrían no estar indexadas bajo el INN genérico solo.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

