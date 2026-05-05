---
layout: default
title: Axitinib
parent: 僅模型預測 (L5)
nav_order: 53
evidence_level: L5
indication_count: 10
---

# Axitinib
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

# AXITINIB: Evaluación de Reposicionamiento Pendiente – Evidence Pack Incompleto

## Resumen en Una Frase

AXITINIB (DrugBank: DB06626) es un inhibidor selectivo de tirosina quinasa dirigido a VEGFR-1/2/3, aprobado internacionalmente para el carcinoma de células renales avanzado.
El presente Evidence Pack (v4, corte 2026-04-20) **no contiene predicciones TxGNN** ni datos estructurados de indicación original, mecanismo de acción o seguridad.
Sin una indicación predicha, **no es posible completar la evaluación de reposicionamiento** en esta versión del paquete.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en este Evidence Pack |
| Nueva Indicación Predicha | Sin predicción disponible |
| Puntaje de Predicción TxGNN | No disponible |
| Nivel de Evidencia | L5 – Sin estudios reales en este paquete |
| Estado de Mercado en Colombia | No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | **Hold** |

---

## Información de Mercado en Colombia

AXITINIB **no cuenta con registros sanitarios vigentes en Colombia**. La consulta realizada el 2026-03-29 no encontró licencias activas.

> No hay registros sanitarios que listar para este fármaco.

---

## Citotoxicidad

AXITINIB pertenece a la clase de agentes antineoplásicos de terapia dirigida, por lo que aplica la sección de citotoxicidad con base en su perfil farmacológico conocido. Los datos del Evidence Pack para este apartado están pendientes de incorporación desde el prospecto recuperado.

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida – Inhibidor de tirosina quinasa (VEGFR-1/2/3) |
| Riesgo de Mielosupresión | Bajo a moderado (menor que quimioterapia citotóxica convencional) |
| Clasificación de Emetogenicidad | Baja |
| Ítems de Monitoreo | Presión arterial, función tiroidea (TSH), función hepática (ALT/AST), función renal, hemograma |
| Protección en Manejo | Seguir precauciones estándar para agentes antineoplásicos orales |

> **Nota:** Estos datos provienen del perfil farmacológico general de AXITINIB. El prospecto fue recuperado exitosamente (log ID 4) pero aún no ha sido incorporado al campo de seguridad del Evidence Pack.

---

## Consideraciones de Seguridad

> Consultar el prospecto para información de seguridad. El registro del pipeline confirma que se recuperó 1 prospecto (fuente: `tfda_package_insert`, 2026-03-29), pero los datos de advertencias y contraindicaciones no fueron cargados en los campos estructurados de este Evidence Pack.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El Evidence Pack v4 de AXITINIB presenta brechas de datos en múltiples campos críticos: no se generaron predicciones TxGNN (`predicted_indications: []`), los campos de indicación original y mecanismo de acción están vacíos, y los datos de seguridad del prospecto recuperado no fueron incorporados. Sin una indicación predicha, no existe base para el análisis de reposicionamiento.

**Para avanzar se necesita:**
- **Ejecutar el pipeline TxGNN** para generar `predicted_indications` (el fármaco existe en DrugBank – log ID 3 confirmó 1 resultado)
- **Incorporar datos de DrugBank** a los campos `original_moa` y `original_indications`
- **Parsear el prospecto recuperado** (log ID 4: `tfda_package_insert`, éxito) hacia los campos `safety.key_warnings` y `safety.contraindications`
- **Evaluar viabilidad de ingreso al mercado colombiano**: AXITINIB no tiene registro sanitario vigente; se debe determinar si procede solicitud de registro nuevo o importación bajo mecanismo especial
- Actualizar el Evidence Pack a **v5** con los datos completos antes de reclasificar la decisión
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

