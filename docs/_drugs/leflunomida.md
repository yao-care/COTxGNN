---
layout: default
title: Leflunomida
parent: 僅模型預測 (L5)
nav_order: 69
evidence_level: L5
indication_count: 0
---

# Leflunomida
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

# Leflunomida: Evaluación de Reposicionamiento — Sin Predicciones Disponibles

## Resumen en Una Frase

Leflunomida (Leflunomide) es un fármaco inmunosupresor de la clase DMARD (*Disease-Modifying Antirheumatic Drug*), ampliamente reconocido para el tratamiento de la artritis reumatoide y la artritis psoriásica.
Sin embargo, el presente Evidence Pack **no contiene indicaciones predichas por TxGNN**, y los datos regulatorios confirman que el fármaco **no está comercializado en Colombia**.
Debido a la ausencia de predicciones y a múltiples brechas de datos críticas, no es posible completar la evaluación de reposicionamiento en esta versión.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Artritis reumatoide / Artritis psoriásica (conocimiento general; sin datos INVIMA disponibles) |
| Nueva Indicación Predicha | — Sin predicción disponible en este Evidence Pack — |
| Puntaje de Predicción TxGNN | N/D |
| Nivel de Evidencia | L5 (sin estudios; predicción del modelo no ejecutada) |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | **Hold** |

---

## ¿Por Qué Es Razonable Esta Predicción?

Esta sección no puede completarse en la versión actual del Evidence Pack porque el campo `predicted_indications` está vacío.

Según el conocimiento farmacológico general, Leflunomida actúa principalmente como inhibidor de la enzima dihidroorotato deshidrogenasa (DHODH), bloqueando la síntesis de novo de pirimidinas en linfocitos activados. Este mecanismo produce un efecto inmunosupresor y antiproliferativo que, en principio, podría explorarse en condiciones autoinmunes más allá de la artritis reumatoide (p.ej., lupus eritematoso sistémico, enfermedad de Crohn, nefropatía lúpica) o incluso en algunos contextos oncológicos e infecciones virales.

Sin embargo, **sin la ejecución del modelo TxGNN sobre el grafo de conocimiento**, no es posible establecer con rigor qué indicaciones candidatas presenta este fármaco ni cuál es el nivel de priorización. Los datos de MOA (DG002) y la información regulatoria (DG001) deben resolverse antes de avanzar.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados en este Evidence Pack.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible en este Evidence Pack.

---

## Información de Mercado en Colombia

Leflunomida **no cuenta con registros sanitarios INVIMA activos** según los datos consultados (2026-03-29). No hay licencias registradas para este principio activo en Colombia.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

> **Nota:** Las brechas de datos DG001 y DG002 impiden la evaluación de advertencias clave, contraindicaciones e interacciones farmacológicas. Ambas brechas deben ser resueltas antes de cualquier análisis de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El Evidence Pack de Leflunomida carece de predicciones TxGNN, datos de seguridad y registros regulatorios en Colombia, lo que hace imposible emitir una recomendación de reposicionamiento fundamentada en este momento.

**Para avanzar se necesita:**

- **[DG001 — Bloqueante]** Obtener la ficha técnica / prospecto aprobado (fuente: INVIMA o equivalente) para extraer advertencias, contraindicaciones y posología aprobada.
- **[DG002 — Alto]** Consultar la API de DrugBank para confirmar mecanismo de acción (DHODH inhibitor), categorías farmacológicas y perfil de toxicidad.
- **Ejecutar el pipeline TxGNN** sobre el grafo de conocimiento con Leflunomida como nodo semilla para generar `predicted_indications` ranqueadas.
- **Verificar estado INVIMA** directamente en el portal oficial para confirmar si existe algún registro sanitario vigente o en trámite.
- Una vez resueltas las brechas, regenerar el Evidence Pack (versión v5+) y reejecutar la evaluación completa.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

