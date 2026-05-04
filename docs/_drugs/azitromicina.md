---
layout: default
title: Azitromicina
parent: 僅模型預測 (L5)
nav_order: 53
evidence_level: L5
indication_count: 0
---

# Azitromicina
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

# Azitromicina: Evaluación de Reposicionamiento No Disponible — Datos Insuficientes

---

## Resumen en Una Frase

Azitromicina (INN: AZITROMICINA) es un fármaco con indicaciones conocidas en el ámbito clínico global; sin embargo, el Evidence Pack actual no contiene indicaciones originales registradas ni predicciones de nuevas indicaciones generadas por TxGNN.
Con múltiples brechas de datos críticas identificadas y **0 predicciones disponibles**, no es posible realizar un análisis formal de reposicionamiento en esta versión del informe.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sin datos disponibles en este Evidence Pack |
| Nueva Indicación Predicha | Sin predicciones disponibles |
| Puntaje de Predicción TxGNN | — |
| Nivel de Evidencia | L5 (sin predicciones ni estudios asociados) |
| Estado de Mercado en Colombia | ✗ No Comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué No Hay Predicción Disponible?

El pipeline TxGNN no generó predicciones de nuevas indicaciones para AZITROMICINA en esta ejecución. Se identificaron dos brechas de datos que bloquean o limitan de forma significativa el análisis:

**Brecha DG001 — Prospecto oficial (severidad: Bloqueante)**
No se cuenta con las advertencias y contraindicaciones del prospecto aprobado por la autoridad sanitaria (INVIMA o equivalente). Esta información es requisito para completar la evaluación de seguridad inicial (S1) del pipeline. Sin ella, el candidato no puede avanzar a las etapas de análisis de reposicionamiento.

**Brecha DG002 — Mecanismo de acción (severidad: Alta)**
El MOA no está disponible en las fuentes consultadas. La ausencia de información mecanística impide que el modelo establezca relaciones entre la indicación original y posibles indicaciones nuevas, reduciendo la capacidad de priorización y explicabilidad de cualquier predicción.

Adicionalmente, la consulta a registros sanitarios colombianos no arrojó resultados (0 licencias), lo que elimina la fuente estructural de indicaciones aprobadas que normalmente alimenta el perfil del fármaco.

> **Nota técnica:** El log de consultas indica que la búsqueda en DrugBank fue marcada como `success` con 1 resultado, y la búsqueda de prospecto (`tfda_package_insert`) también fue `success` con 1 resultado. Sin embargo, los datos extraídos no fueron integrados al Evidence Pack en esta versión (`drugbank_id: null`, `original_moa: [Data Gap]`). Se recomienda revisar el paso de integración del pipeline para recuperar esta información antes de la próxima ejecución.

---

## Información de Mercado en Colombia

No se encontraron registros sanitarios para AZITROMICINA bajo ese INN en Colombia. El fármaco figura como **no comercializado** en las fuentes consultadas.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|--------------------|---------------------|-------------------|---------------------|
| — | Sin registros disponibles | — | — |

> Considerar que AZITROMICINA puede estar registrada bajo nombres comerciales (p. ej., Zithromax, Azitrocin, Zitromax) que no fueron incluidos en esta consulta. Se sugiere ampliar la búsqueda por nombre comercial o principio activo alternativo.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La ausencia de predicciones TxGNN y la presencia de brechas bloqueantes (DG001 y DG002) impiden realizar cualquier evaluación de reposicionamiento fundamentada. No existe base suficiente para emitir una recomendación de avance.

**Para avanzar se necesita:**
- **Remediar DG001:** Descargar y parsear el prospecto oficial de INVIMA (o fuente equivalente) para extraer indicaciones aprobadas, advertencias y contraindicaciones
- **Remediar DG002:** Ejecutar la consulta a DrugBank API con el identificador correcto y completar la integración del MOA al Evidence Pack (el log indica que la consulta fue exitosa pero los datos no se propagaron)
- **Verificar nombres comerciales:** Ampliar la búsqueda de registros sanitarios en Colombia usando nombres comerciales conocidos de azitromicina
- **Re-ejecutar el pipeline TxGNN** con el Evidence Pack completo para generar predicciones de nuevas indicaciones y habilitar el análisis de reposicionamiento
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

