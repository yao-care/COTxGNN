---
layout: default
title: Lanadelumab
parent: 僅模型預測 (L5)
nav_order: 102
evidence_level: L5
indication_count: 10
---

# Lanadelumab
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

# LANADELUMAB: Evaluación No Disponible — Datos Insuficientes para Predicción

## Resumen en Una Frase

LANADELUMAB (DB14597) es un fármaco registrado en DrugBank, pero el Evidence Pack actual no contiene indicaciones originales ni predicciones TxGNN de nuevas indicaciones.
Sin datos de indicación original, mecanismo de acción ni indicaciones predichas, **no es posible completar una evaluación de reposicionamiento en esta versión**.
Se requiere complementar los datos antes de proceder al análisis.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Sin datos disponibles |
| Nueva Indicación Predicha | Sin predicciones TxGNN disponibles |
| Puntaje de Predicción TxGNN | — |
| Nivel de Evidencia | L5 (sin estudios reales; predicción no generada) |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | **Hold** |

---

## Por qué No es Posible Completar la Predicción

El Evidence Pack presenta dos brechas de datos críticas que bloquean el análisis:

**Brecha DG001 (Bloqueante):** No se dispone de la ficha técnica / prospecto de INVIMA con advertencias y contraindicaciones. Sin esta información no es posible realizar la evaluación de seguridad inicial (S1), requisito previo al análisis de reposicionamiento.

**Brecha DG002 (Alta):** El mecanismo de acción (MOA) de LANADELUMAB está marcado como `[Data Gap]`. Esto impide realizar el análisis de relación mecanística entre la indicación original y cualquier candidata nueva, lo que es esencial para justificar una predicción de reposicionamiento.

Adicionalmente, el campo `predicted_indications` está vacío, lo que indica que el pipeline TxGNN no generó candidatos para este fármaco en la versión actual del Evidence Pack (`v4`, corte de datos `2026-04-20`). Esto puede deberse a que el fármaco no está representado en el Knowledge Graph utilizado para la inferencia, o a que los umbrales de score no se alcanzaron.

---

## Información de Mercado en Colombia

No existen registros sanitarios de LANADELUMAB en Colombia al momento del corte de datos.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El Evidence Pack no contiene indicaciones predichas ni datos de mecanismo de acción, lo que hace imposible generar un análisis de reposicionamiento fundamentado. La decisión es **Hold** hasta completar las brechas identificadas.

**Para avanzar se necesita:**
- **[DG001 — Bloqueante]** Descargar e interpretar el prospecto autorizado (fuente INVIMA o equivalente regulatorio) para extraer advertencias, contraindicaciones e indicaciones aprobadas
- **[DG002 — Alta]** Consultar DrugBank API (`DB14597`) para obtener el mecanismo de acción (MOA), categorías farmacológicas y targets moleculares
- **Re-ejecutar el pipeline TxGNN** con el Knowledge Graph actualizado para obtener predicciones de nuevas indicaciones
- Verificar si LANADELUMAB está representado como nodo en el KG de la versión actual; de lo contrario, agregar entidad y re-entrenar o usar inferencia transductiva
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

