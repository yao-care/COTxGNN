---
layout: default
title: Abatacept
parent: 僅模型預測 (L5)
nav_order: 12
evidence_level: L5
indication_count: 10
---

# Abatacept
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

# ABATACEPT: Evaluación Preliminar — Sin Indicaciones Predichas Disponibles

## Resumen en Una Frase

Abatacept (DrugBank: DB01281) es una proteína de fusión CTLA-4-Ig conocida internacionalmente como modulador selectivo de la coestimulación de células T, utilizada principalmente en artritis reumatoide y otras enfermedades autoinmunes. Sin embargo, el Evidence Pack actual **no contiene indicaciones predichas por TxGNN**, y el fármaco **no se encuentra comercializado en Colombia** (sin registros sanitarios INVIMA). Se requiere completar múltiples brechas de datos antes de avanzar en la evaluación de reposicionamiento.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | No disponible en el Evidence Pack (sin registros sanitarios ni indicaciones listadas) |
| Nueva Indicación Predicha | — Sin predicciones TxGNN disponibles — |
| Puntaje de Predicción TxGNN | N/A |
| Nivel de Evidencia | L5 (solo datos de identificación, sin predicciones ni estudios) |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | **Hold** |

---

## ¿Por qué se Encuentra en Hold esta Evaluación?

Abatacept es un agente biológico ampliamente conocido a nivel mundial. Es una proteína de fusión compuesta por el dominio extracelular de CTLA-4 humano unido al fragmento Fc de IgG1, que actúa modulando selectivamente la coestimulación de células T al unirse a CD80/CD86 en las células presentadoras de antígeno, bloqueando la interacción con CD28. Esta acción lo hace eficaz en enfermedades autoinmunes como la artritis reumatoide, la artritis idiopática juvenil y la artritis psoriásica.

No obstante, el Evidence Pack actual presenta **brechas de datos críticas** que impiden una evaluación completa de reposicionamiento:

1. **Sin predicciones TxGNN**: El array `predicted_indications` está vacío, lo que significa que el modelo no ha generado (o no se han incluido) candidatos de nuevas indicaciones para este fármaco.
2. **Sin datos regulatorios en Colombia**: Abatacept no cuenta con registros sanitarios INVIMA, lo que implica que no está comercializado en el país y cualquier uso requeriría importación o trámite regulatorio especial.
3. **Sin datos de mecanismo de acción (MOA) en el pack**: Aunque el MOA de abatacept es bien documentado en la literatura internacional, el Evidence Pack no incluye esta información, limitando el análisis de plausibilidad mecánica automatizado.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados en el Evidence Pack, dado que no se generaron indicaciones predichas por TxGNN.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible en el Evidence Pack, dado que no se generaron indicaciones predichas por TxGNN.

---

## Información de Mercado en Colombia

Abatacept **no se encuentra comercializado en Colombia**. No se identificaron registros sanitarios INVIMA activos.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------------------|---------------------|---------------------|---------------------|
| — | — | — | — |

> **Nota:** A nivel internacional, abatacept se comercializa bajo la marca **Orencia®** (Bristol-Myers Squibb) en forma de solución inyectable para infusión intravenosa y solución para inyección subcutánea.

---

## Consideraciones de Seguridad

No se dispone de datos de seguridad en el Evidence Pack actual (advertencias, contraindicaciones e interacciones farmacológicas no disponibles).

> Consultar el prospecto internacional del producto (Orencia® / Abatacept) para información completa de seguridad. Entre las precauciones conocidas internacionalmente se incluyen: riesgo de infecciones graves, reactivación de hepatitis B, y precaución en pacientes con EPOC.

---

## Brechas de Datos Identificadas

| ID | Categoría | Item Faltante | Severidad | Impacto | Fuente de Remediación |
|----|-----------|---------------|-----------|---------|----------------------|
| DG001 | Drug_Level | Advertencias y contraindicaciones del prospecto | **Bloqueante** | No se puede iniciar la evaluación de seguridad (S1) | Descargar y analizar prospecto PDF del ente regulatorio |
| DG002 | Drug_Level | Mecanismo de acción (MOA) | Alta | Afecta el análisis de relación mecánica con nuevas indicaciones | Consultar API de DrugBank |

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El Evidence Pack de abatacept carece de los elementos fundamentales para una evaluación de reposicionamiento: no hay indicaciones predichas por TxGNN, no hay datos de MOA integrados, y el fármaco no está comercializado en Colombia. Sin predicciones del modelo, no es posible evaluar la plausibilidad de nuevas indicaciones.

**Para avanzar se necesita:**
- **Ejecutar la predicción TxGNN** para generar candidatos de nuevas indicaciones para abatacept
- **Resolver DG001 (Bloqueante)**: Obtener y analizar el prospecto oficial para extraer advertencias y contraindicaciones
- **Resolver DG002**: Integrar los datos de mecanismo de acción desde DrugBank API
- **Evaluar el contexto regulatorio colombiano**: Determinar si existe algún programa de acceso o trámite INVIMA en curso para abatacept
- **Recopilar evidencia**: Una vez generadas las predicciones, buscar ensayos clínicos y literatura de respaldo en ClinicalTrials.gov y PubMed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

