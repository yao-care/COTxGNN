---
layout: default
title: Azatioprina
parent: 僅模型預測 (L5)
nav_order: 55
evidence_level: L5
indication_count: 0
---

# Azatioprina
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

# Azatioprina: Evaluación de Reposicionamiento — Datos Insuficientes para Generar Predicción

## Resumen en Una Frase

Azatioprina (AZATIOPRINA) es un fármaco con registro de consulta en DrugBank, pero el Evidence Pack actual no contiene indicaciones originales confirmadas, mecanismo de acción ni predicciones TxGNN activas.
El modelo TxGNN **no generó indicaciones predichas** para este compuesto en la corrida actual, por lo que no es posible evaluar una nueva indicación objetivo.
Se requiere completar los datos faltantes antes de continuar con el proceso de evaluación de reposicionamiento.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | No disponible en este Evidence Pack |
| Nueva Indicación Predicha | Sin predicciones generadas |
| Puntaje de Predicción TxGNN | No aplica |
| Nivel de Evidencia | L5 — Sin estudios reales, sin predicción activa |
| Estado de Mercado en Colombia | ✗ No comercializado (0 registros INVIMA) |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | **Hold** |

---

## Por qué No es Posible Evaluar esta Predicción

El Evidence Pack recibido presenta dos brechas de datos críticas que bloquean el análisis de reposicionamiento:

**1. Mecanismo de acción no disponible (DG002 — Severidad Alta):** No se cuenta con datos de MOA provenientes de DrugBank para explicar la relación mecanística entre la indicación original y cualquier indicación nueva candidata. Esto impide el análisis de plausibilidad biológica que sustenta la evaluación TxGNN.

**2. Array de indicaciones predichas vacío:** El campo `predicted_indications` del Evidence Pack está vacío (`[]`). Esto puede deberse a que el pipeline TxGNN no procesó este fármaco, a que el INN "AZATIOPRINA" no fue reconocido correctamente como entidad en el grafo de conocimiento, o a que el fármaco fue excluido por umbrales de score. Sin una indicación predicha, no es posible construir ninguna sección de evidencia clínica, literatura ni razonabilidad.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El Evidence Pack está incompleto en sus componentes fundamentales — no hay indicación original estructurada, no hay MOA, no hay predicciones TxGNN y el fármaco no tiene registros INVIMA en Colombia. No existe base suficiente para emitir una recomendación de reposicionamiento.

**Para avanzar se necesita:**
- **[DG001 — Bloqueante]** Obtener y parsear la ficha técnica/prospecto del fármaco desde INVIMA o fuente equivalente colombiana para extraer indicaciones aprobadas, advertencias y contraindicaciones
- **[DG002 — Alta prioridad]** Consultar DrugBank API con el INN normalizado (`azathioprine` en inglés) para recuperar DrugBank ID, MOA, categorías farmacológicas y datos de toxicidad
- **Re-ejecutar el pipeline TxGNN** con el identificador DrugBank correcto y verificar que el nodo del fármaco esté presente en el grafo de conocimiento
- **Verificar el INN de entrada:** "AZATIOPRINA" es la denominación en español; el pipeline puede requerir el INN en inglés (`azathioprine`) o el DrugBank ID (`DB00993`) para la búsqueda correcta
- **Evaluar registro en Colombia:** Si el fármaco no está comercializado bajo este nombre, investigar si existen equivalentes o presentaciones importadas con registro INVIMA
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

