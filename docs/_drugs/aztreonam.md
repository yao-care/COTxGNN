---
layout: default
title: Aztreonam
parent: 僅模型預測 (L5)
nav_order: 58
evidence_level: L5
indication_count: 10
---

# Aztreonam
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

# Aztreonam: Evaluación de Reposicionamiento — Sin Indicaciones Predichas Disponibles

## Resumen en Una Frase

Aztreonam es un antibiótico monobactámico utilizado para el tratamiento de infecciones causadas por bacterias gramnegativas aerobias, incluyendo *Pseudomonas aeruginosa*.
El modelo TxGNN **no generó indicaciones predichas** para este fármaco en el ciclo de análisis actual, debido a bloqueos de datos identificados en el pipeline.
La evaluación no puede avanzar hasta resolver los gaps críticos de información.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infecciones por bacterias gramnegativas aerobias (uso clínico conocido; sin registro en Colombia) |
| Nueva Indicación Predicha | Sin datos — TxGNN no generó predicciones en este ciclo |
| Puntaje de Predicción TxGNN | No disponible |
| Nivel de Evidencia | L5 (sin estudios reales disponibles para reposicionamiento) |
| Estado de Mercado en Colombia | ✗ No comercializado (0 registros INVIMA) |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | **Hold** |

---

## Por qué No Se Generaron Predicciones

Aztreonam es el único antibiótico de la clase monobactámico aprobado para uso clínico. A diferencia de las penicilinas y cefalosporinas, posee un anillo β-lactámico monocíclico que le confiere actividad selectiva contra bacterias gramnegativas aerobias —incluyendo *Pseudomonas aeruginosa*, *Escherichia coli*, *Klebsiella pneumoniae* y *Haemophilus influenzae*— con mínima actividad contra grampositivos y anaerobios.

Sin embargo, el análisis actual enfrenta **dos bloqueos de datos que impidieron la ejecución del pipeline TxGNN**:

1. **[Bloqueante — DG001]** No se dispone de los datos de advertencias, contraindicaciones ni perfil de seguridad del prospecto oficial. Esto impide completar la evaluación de seguridad preliminar (fase S1), requisito obligatorio antes de generar candidatos de reposicionamiento.
2. **[Alta prioridad — DG002]** El mecanismo de acción formal no está cargado en el Evidence Pack. Sin este dato, el modelo no puede evaluar la relevancia mecanística entre la indicación original y posibles nuevas indicaciones.

Adicionalmente, Aztreonam **no cuenta con ningún registro sanitario activo en Colombia (INVIMA)**, lo que añade una barrera regulatoria de entrada independiente del resultado del modelo.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El pipeline TxGNN no pudo generar indicaciones predichas debido a bloqueos de datos en seguridad y mecanismo de acción. Sin predicciones que evaluar, sin registros en Colombia y con gaps bloqueantes sin resolver, no existe base para avanzar en este momento.

**Para avanzar se necesita:**
- **[DG001 — Bloqueante]** Descargar y parsear el prospecto oficial de INVIMA/TFDA para obtener advertencias, contraindicaciones y perfil de seguridad completo
- **[DG002 — Alta prioridad]** Consultar la API de DrugBank (ID: DB00355) para cargar los datos de mecanismo de acción (MOA) en el Evidence Pack
- Volver a ejecutar el pipeline TxGNN con el Evidence Pack completo para generar indicaciones predichas válidas
- Evaluar la viabilidad de obtener registro sanitario en Colombia si el reposicionamiento resulta prometedor tras el análisis completo
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

