---
noindex: true
sitemap: false
layout: default
title: Atorvastatina
parent: Solo Predicción del Modelo (L5)
nav_order: 74
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Atorvastatina
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **0** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Atorvastatina: Evaluación de Reposicionamiento — Datos Insuficientes para Predicción
{: .text-alpha }

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
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 18) |
| Número de Registros Sanitarios | al menos 20 |
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
El pack carece de los insumos mínimos para una evaluación de reposicionamiento: no hay predicciones TxGNN, no hay datos de seguridad procesados. No se puede emitir ninguna recomendación clínica o comercial con la información actual.

<!-- review:begin co-lic-20261105-atorvastatina-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "El pack carece de los insumos mínimos para una evaluación de reposicionamiento: no hay predicciones TxGNN, no hay datos de seguridad procesados y el registro regulatorio colombiano muestra 0 licencias." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-atorvastatina-1 -->

**Para avanzar se necesita:**

1. **Corregir el término de búsqueda TxGNN**: Reejecutar el pipeline usando el INN inglés `atorvastatin` o el DrugBank ID `DB01076` para obtener predicciones de nuevas indicaciones.
2. **Completar datos DrugBank**: Poblar los campos `original_moa`, `key_warnings` y `contraindications` con el resultado ya obtenido de DrugBank (`result_count: 1` en query log).
3. **Ampliar búsqueda INVIMA**: Repetir la consulta con variantes como `ATORVASTATINA CALCICA`, `LIPITOR` y código ATC `C10AA05` para recuperar los registros sanitarios colombianos existentes.
4. **Regenerar Evidence Pack v5**: Con los insumos corregidos, el pipeline debería producir `predicted_indications` con candidatos TxGNN y un pack completo apto para evaluación.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "y el registro regulatorio colombiano muestra 0 licencias" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

