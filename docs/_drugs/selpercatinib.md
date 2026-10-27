---
layout: default
title: Selpercatinib
parent: Solo Predicción del Modelo (L5)
nav_order: 582
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Selpercatinib: nueva indicación predicha, Hipertensión pulmonar (nivel de evidencia L5). Indicación original: No especificada"
monitor_inn: "SELPERCATINIB"
predicted_indications: ["pulmonary hypertension", "migraine disorder", "migraine with brainstem aura"]
---

# Selpercatinib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Selpercatinib: De Indicación Original (no especificada en el registro) a Hipertensión Pulmonar
{: .text-alpha }

## Resumen en Una Frase

Selpercatinib es un inhibidor selectivo de la cinasa RET, comercializado en Colombia como Retsevmo® (Eli Lilly); el texto del registro sanitario solo repite el nombre del principio activo, sin precisar la indicación.
El modelo TxGNN predice que podría ser efectivo para **hipertensión pulmonar**, pero **no hay ensayos clínicos ni publicaciones que respalden directamente esta indicación**: las tres publicaciones recuperadas tratan sobre cánceres con alteración de RET y perfiles de eventos adversos.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro solo indica "SELPERCATINIB") |
| Nueva Indicación Predicha | Hipertensión pulmonar |
| Puntaje de Predicción TxGNN | 99.18% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 (0 vigentes, 2 cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Selpercatinib es un inhibidor selectivo de la cinasa RET. Este dato proviene del conocimiento general del fármaco, ya que los datos compilados para este informe no incluyen el mecanismo de acción detallado. Se usa en tumores con alteraciones de RET, como el cáncer de pulmón de células no pequeñas con fusión de RET y el carcinoma medular de tiroides, como reflejan las publicaciones recuperadas.

La relación entre la indicación original (oncología con alteración de RET) y la hipertensión pulmonar **no es evidente**. El puntaje alto de TxGNN (0.99) proviene de una predicción basada en grafos de conocimiento y no de evidencia experimental o clínica. En los datos compilados no se establece un mecanismo plausible mediado por RET en el remodelado vascular pulmonar.

Conviene aclarar que los reportes de eventos adversos de inhibidores de RET pueden mencionar efectos cardiovasculares o hipertensivos, pero se refieren a hipertensión sistémica y constituyen una señal de seguridad, no evidencia terapéutica para hipertensión pulmonar.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Ninguna de las publicaciones evalúa selpercatinib en hipertensión pulmonar; se listan como contexto del fármaco.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [34178121](https://pubmed.ncbi.nlm.nih.gov/34178121/) | 2021 | Análisis retrospectivo | Therapeutic Advances in Medical Oncology | Experiencia en vida real de selpercatinib en CPNM con fusión de RET tratado mediante un programa de acceso (SIREN) |
| [39372206](https://pubmed.ncbi.nlm.nih.gov/39372206/) | 2024 | Estudio de farmacovigilancia | Frontiers in Pharmacology | Compara los eventos adversos de pralsetinib y selpercatinib con datos reales del sistema FAERS |
| [41918669](https://pubmed.ncbi.nlm.nih.gov/41918669/) | 2026 | Reporte de caso | Cureus | Carcinoma medular de tiroides metastásico en MEN 2B con mutación RET M918T; retos del manejo a largo plazo y terapia dirigida |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20232108 | RETSEVMO® 80 MG (cancelado) | Cápsula dura | SELPERCATINIB |
| 20232107 | RETSEVMO® 40 MG (cancelado) | Cápsula dura | SELPERCATINIB |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor selectivo de la cinasa RET) |
| Riesgo de Mielosupresión | Sin datos específicos en la información compilada |
| Clasificación de Emetogenicidad | Sin datos específicos en la información compilada |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones potenciales. Entre las de nivel **mayor** figuran:
  - Antiácidos y reductores de acidez gástrica: famotidina, ranitidina, cimetidina, omeprazol, rabeprazol, dexlansoprazol y óxido de magnesio.
  - Aprepitant.
  - Claritromicina.
  - Dexametasona.

  Entre las de nivel **moderado** figuran hidrocortisona, triamcinolona, betametasona, budesonida, pioglitazona, loperamida, bisacodilo, saxagliptina y polietilenglicol con electrolitos.
- **Perfil de seguridad general**: según el análisis de las predicciones, el perfil conocido de selpercatinib incluye hipertensión, prolongación del QT y hepatotoxicidad, lo que exige cautela en cualquier uso fuera de oncología.

Consultar el prospecto para advertencias y contraindicaciones, ya que no se dispone de ellas en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura que evalúen selpercatinib en hipertensión pulmonar. Además, no hay un mecanismo plausible documentado, el perfil de seguridad es relevante y los registros sanitarios en Colombia están cancelados.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto del INVIMA (advertencias y contraindicaciones), requisito previo para cualquier evaluación de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Establecer una hipótesis mecanística sobre la vía RET en la vasculatura pulmonar, con estudios preclínicos que la respalden.
- Aclarar la disponibilidad del fármaco en Colombia, dado que los registros están cancelados.
- Evaluar la relación beneficio-riesgo, en particular los efectos cardiovasculares, antes de considerar un uso no oncológico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

