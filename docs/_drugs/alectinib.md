---
layout: default
title: Alectinib
parent: 僅模型預測 (L5)
nav_order: 22
evidence_level: L5
indication_count: 10
---

# Alectinib
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

# ALECTINIB: De Cáncer de Pulmón ALK-Positivo a Indicación Pendiente de Predicción

## Resumen en Una Frase

ALECTINIB es un inhibidor selectivo de ALK (quinasa de linfoma anaplásico) y RET, aprobado internacionalmente para el tratamiento del cáncer de pulmón de células no pequeñas (CPNM) ALK-positivo.
El Evidence Pack actual **no contiene indicaciones predichas por TxGNN** para este fármaco, lo que impide completar el análisis de reposicionamiento.
Sin predicciones disponibles y con múltiples brechas de datos críticas, no es posible emitir una recomendación fundamentada en esta etapa.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer de pulmón de células no pequeñas (CPNM) ALK-positivo |
| Nueva Indicación Predicha | Sin datos disponibles |
| Puntaje de Predicción TxGNN | Sin datos disponibles |
| Nivel de Evidencia | L5 — sin predicción del modelo ejecutada |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | **Hold** |

---

## ¿Por qué es Razonable esta Predicción?

No se dispone de predicciones TxGNN en este Evidence Pack (`predicted_indications: []`). Sin una indicación candidata, no es posible evaluar la relación mecanística entre la indicación original y una nueva diana terapéutica.

ALECTINIB actúa como inhibidor selectivo de ALK y RET, bloqueando la proliferación celular en tumores que dependen de la señalización de estas quinasas. Su eficacia en CPNM ALK-positivo está bien documentada a nivel internacional, y mecanísticamente podría ser relevante para otras neoplasias impulsadas por fusiones o mutaciones de ALK/RET. Sin embargo, **el mecanismo de acción detallado también está marcado como brecha de datos (DG002)**, lo que impide profundizar en el análisis de transposición mecanística.

La ejecución del pipeline TxGNN para este fármaco es el paso previo indispensable antes de continuar con cualquier evaluación de reposicionamiento.

---

## Información de Mercado en Colombia

ALECTINIB **no cuenta con registros sanitarios activos ante el INVIMA**. No se registró ninguna licencia en la consulta realizada el 2026-03-29. Esto implica que, en caso de identificarse una indicación viable, el proceso regulatorio partiría desde cero.

---

## Citotoxicidad

ALECTINIB es un fármaco antineoplásico de tipo terapia dirigida (inhibidor de tirosina quinasa ALK/RET), por lo que aplica esta sección.

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida — inhibidor de tirosina quinasa (ALK/RET) |
| Riesgo de Mielosupresión | Bajo a moderado — anemia y neutropenia reportadas, generalmente grado 1-2 |
| Clasificación de Emetogenicidad | Baja (administración oral) |
| Items de Monitoreo | Hemograma completo, función hepática (ALT/AST/bilirrubina), función pulmonar (neumonitis intersticial), frecuencia cardíaca (bradicardia), creatinina |
| Protección en Manejo | Aplican precauciones estándar para agentes antineoplásicos orales; consultar prospecto del fabricante para manejo de derrames y almacenamiento |

---

## Consideraciones de Seguridad

Los datos de advertencias clave y contraindicaciones no están disponibles en este Evidence Pack (brecha DG001: prospecto del fabricante no analizado). No se identificaron interacciones farmacológicas en la consulta DDI del 2026-03-29.

Consultar el prospecto oficial del fabricante para información de seguridad completa antes de cualquier evaluación clínica.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El Evidence Pack para ALECTINIB presenta brechas que bloquean la evaluación: ausencia total de predicciones TxGNN, mecanismo de acción no disponible, datos de seguridad sin resolver y ningún registro sanitario en Colombia. No existe base suficiente para avanzar en el proceso de reposicionamiento en este momento.

**Para avanzar se necesita:**
- Ejecutar el modelo TxGNN con los datos de ALECTINIB y obtener predicciones de nuevas indicaciones
- Obtener datos del mecanismo de acción (MOA) desde DrugBank API — resolver DG002
- Descargar y parsear el prospecto del fabricante (Roche/Alecensa) para datos de seguridad — resolver DG001
- Verificar con el INVIMA si existe algún trámite de registro en curso o si aplica la figura de importación especial para uso compasivo
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

