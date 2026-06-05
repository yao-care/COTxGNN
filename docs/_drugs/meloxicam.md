---
layout: default
title: Meloxicam
parent: 僅模型預測 (L5)
nav_order: 167
evidence_level: L5
indication_count: 10
---

# Meloxicam
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

# Meloxicam: De Osteoartritis y Artritis Reumatoide a Acromesomelic Dysplasia, Hunter-Thompson Type

## Resumen en Una Frase

Meloxicam es un antiinflamatorio no esteroideo (AINE) con selectividad preferencial por COX-2, utilizado ampliamente para el manejo del dolor e inflamación en condiciones como osteoartritis, artritis reumatoide y artritis idiopática juvenil.
El modelo TxGNN predice que podría ser efectivo para **Acromesomelic Dysplasia, Hunter-Thompson Type** (displasia acromesomélica tipo Hunter-Thompson),
sin embargo, **no existen ensayos clínicos ni publicaciones** que respalden actualmente esta dirección, situando la evidencia exclusivamente en la predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | No disponible en el registro colombiano (sin licencias activas) |
| Nueva Indicación Predicha | Acromesomelic dysplasia, Hunter-Thompson type |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en este Evidence Pack. Según la información conocida, Meloxicam es un AINE con inhibición preferencial de COX-2 que actúa suprimiendo la síntesis de prostaglandinas mediante la inhibición de las ciclooxigenasas 1 y 2. Este mecanismo produce efectos antiinflamatorios, analgésicos y antipiréticos, siendo utilizado clásicamente para osteoartritis, artritis reumatoide y artritis idiopática juvenil.

La displasia acromesomélica tipo Hunter-Thompson es una condición genética causada por mutaciones en el gen **GDF5/CDMP-1**, que genera anomalías estructurales en el desarrollo de los segmentos medios de las extremidades (cúbito, radio, tibia, peroné). Se trata de un defecto del desarrollo óseo de origen genético, no de una enfermedad inflamatoria primaria.

Según el análisis de racionalidad incluido en este Evidence Pack, la conexión mecanística es extremadamente débil: la inhibición de prostaglandinas por Meloxicam podría teóricamente aliviar inflamación secundaria, pero no tiene ningún efecto modificador sobre la causa genética subyacente. El puntaje elevado de TxGNN probablemente refleja un efecto de agrupamiento de nodos de enfermedades esqueléticas dentro del grafo de conocimiento, más que una relación biológica directa y verificable. La predicción carece de credibilidad biológica suficiente para justificar investigación clínica en esta indicación específica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de TxGNN para displasia acromesomélica tipo Hunter-Thompson no cuenta con respaldo clínico ni preclínico: no existen ensayos clínicos ni publicaciones que apoyen este uso, y el análisis mecanístico evidencia una conexión biológica extremadamente débil entre la inhibición de prostaglandinas (mecanismo de Meloxicam) y la patogénesis genético-estructural de esta displasia.

**Para avanzar se necesita:**
- Completar el perfil de seguridad del fármaco: obtener advertencias, contraindicaciones e interacciones desde el prospecto oficial
- Confirmar el mecanismo de acción detallado (MOA) mediante consulta a DrugBank API
- Obtener registro sanitario o reconocimiento de comercialización en Colombia para viabilidad regulatoria
- Considerar priorizar indicaciones con mayor plausibilidad biológica identificadas en el mismo pack:
  - **Espondiloartropatía** (Rank 6, L4): respaldo indirecto de clase (AINE como primera línea en SpA según guías ASAS/EULAR)
  - **Artritis idiopática juvenil RF+ poliarticular** (Rank 8, L4): FDA ha aprobado Meloxicam en JIA pediátrica; existe literatura de seguridad disponible (PMID 25057265)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

