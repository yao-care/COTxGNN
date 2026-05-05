---
layout: default
title: Atorvastatina
parent: 僅模型預測 (L5)
nav_order: 48
evidence_level: L5
indication_count: 0
---

# Atorvastatina
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

# Atorvastatina: Evaluación de Reposicionamiento — Datos Insuficientes para Predicción

## Resumen en Una Frase

Atorvastatina es un fármaco de la clase de las estatinas, ampliamente conocido por su uso en el tratamiento de la hipercolesterolemia y la prevención cardiovascular.
Sin embargo, el presente Evidence Pack **no contiene predicciones TxGNN** ni indicaciones nuevas procesadas, posiblemente debido a que la consulta utilizó el nombre en español ("ATORVASTATINA") en lugar del INN estándar inglés ("atorvastatin").
Con **0 ensayos clínicos**, **0 publicaciones** y **0 registros sanitarios colombianos** encontrados, no es posible generar un informe de reposicionamiento completo en este momento.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en el pack actual |
| Nueva Indicación Predicha | Sin predicciones TxGNN generadas |
| Puntaje de Predicción TxGNN | — |
| Nivel de Evidencia | L5 (sin estudios cargados en el pack) |
| Estado de Mercado en Colombia | No encontrado en consulta INVIMA (0 registros) |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | **Hold** |

---

## Por qué los Datos son Insuficientes

El pipeline de generación del Evidence Pack encontró **dos brechas bloqueantes**:

1. **Sin predicciones TxGNN** (`predicted_indications: []`): El modelo no generó candidatos de reposicionamiento para este fármaco. Esto puede ocurrir si el término de búsqueda utilizado ("ATORVASTATINA") no coincide con el identificador interno del grafo de conocimiento, que generalmente usa el INN en inglés ("**atorvastatin**") o el DrugBank ID correspondiente.

2. **Sin datos de MOA ni seguridad**: Aunque el log indica que DrugBank y el prospecto TFDA fueron consultados exitosamente (`result_count: 1`), los campos `original_moa`, `key_warnings` y `contraindications` no fueron poblados en el pack. Esto impide el análisis de mecanismo y la evaluación de seguridad.

La consulta a INVIMA/TFDA devolvió **0 resultados** para "ATORVASTATINA", lo que es inusual dado que la atorvastatina es uno de los fármacos más prescritos a nivel mundial. Es probable que los registros colombianos estén indexados bajo variantes ortográficas o nombres de marca (p.ej., "ATORVASTATINA CALCICA", "LIPITOR").

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El pack carece de los insumos mínimos para una evaluación de reposicionamiento: no hay predicciones TxGNN, no hay datos de seguridad procesados y el registro regulatorio colombiano muestra 0 licencias. No se puede emitir ninguna recomendación clínica o comercial con la información actual.

**Para avanzar se necesita:**

1. **Corregir el término de búsqueda TxGNN**: Reejecutar el pipeline usando el INN inglés `atorvastatin` o el DrugBank ID `DB01076` para obtener predicciones de nuevas indicaciones.
2. **Completar datos DrugBank**: Poblar los campos `original_moa`, `key_warnings` y `contraindications` con el resultado ya obtenido de DrugBank (`result_count: 1` en query log).
3. **Ampliar búsqueda INVIMA**: Repetir la consulta con variantes como `ATORVASTATINA CALCICA`, `LIPITOR` y código ATC `C10AA05` para recuperar los registros sanitarios colombianos existentes.
4. **Regenerar Evidence Pack v5**: Con los insumos corregidos, el pipeline debería producir `predicted_indications` con candidatos TxGNN y un pack completo apto para evaluación.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

