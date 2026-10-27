---
layout: default
title: Melphalan
parent: Evidencia Alta (L1-L2)
nav_order: 426
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-14
description: "Melphalan: nueva indicación predicha, Tumor de células germinales gonadal (nivel de evidencia L2). Indicación original: Melphalan"
monitor_inn: "melphalan"
predicted_indications: ["female breast carcinoma", "rectum mucinous adenocarcinoma", "colon mucinous adenocarcinoma", "gallbladder mucinous adenocarcinoma", "cervical mucinous adenocarcinoma", "endometrial mucinous adenocarcinoma"]
---

# Melphalan
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **10** 
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

## Melfalán: De Indicación Registrada (Melphalan) a Tumor de Células Germinales Gonadal
{: .text-alpha }

## Resumen en Una Frase

Melfalán es un agente alquilante antineoplásico que en Colombia contó con registros sanitarios de la sustancia "melphalan" (hoy todos cancelados). El modelo TxGNN predice que podría ser efectivo para **tumor de células germinales gonadal**, con **7 ensayos clínicos** y **1 publicación** de relevancia muy limitada. Los ensayos evalúan regímenes de quimioterapia combinada a dosis altas, por lo que el aporte propio del melfalán no puede aislarse.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Melphalan (el registro sanitario no detalla la indicación en texto) |
| Nueva Indicación Predicha | Tumor de células germinales gonadal |
| Puntaje de Predicción TxGNN | 99.77% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 7 (todos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, el melfalán es un agente alquilante bifuncional que entrecruza el ADN e impide la división de las células tumorales.

Los tumores de células germinales son muy sensibles a la quimioterapia. Los regímenes de dosis altas con agentes alquilantes y rescate con células madre autólogas son una estrategia establecida de rescate en enfermedad recidivante. Esto es coherente con el puntaje tan alto del modelo.

Una limitación importante: la evidencia proviene de regímenes combinados a dosis altas (por ejemplo, con gemcitabina, docetaxel y carboplatino), por lo que no se puede atribuir el beneficio al melfalán por sí solo.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00936936](https://clinicaltrials.gov/study/NCT00936936) | Fase 2 | Completado | 64 | Dos ciclos de quimioterapia a dosis altas (gemcitabina, docetaxel, melfalán, carboplatino; luego ifosfamida, carboplatino, etopósido) en tumores germinales recidivantes de mal pronóstico |
| [NCT00060255](https://clinicaltrials.gov/study/NCT00060255) | Fase 2 | Completado | 451 | Trasplante autólogo con ocho regímenes de dosis altas en neoplasias hematológicas y tumores sólidos seleccionados; los tumores germinales son solo un subgrupo |
| [NCT00003425](https://clinicaltrials.gov/study/NCT00003425) | Fase 1/2 | Completado | 25 | Escalada de dosis de melfalán con rescate de células madre y amifostina en tumores sólidos |
| [NCT00638898](https://clinicaltrials.gov/study/NCT00638898) | Fase 1 | Completado | 25 | Busulfán, melfalán y topotecán con trasplante autólogo en tumores avanzados o recurrentes |
| [NCT00536601](https://clinicaltrials.gov/study/NCT00536601) | No aplica | Completado | 174 | Dosis altas con o sin irradiación corporal total antes del trasplante autólogo; población amplia |
| [NCT00002750](https://clinicaltrials.gov/study/NCT00002750) | Fase 1 | Completado | 6 | Melfalán intratecal en meningitis neoplásica recurrente; vía y contexto distintos |
| [NCT00003926](https://clinicaltrials.gov/study/NCT00003926) | Fase 1 | Terminado | 13 | Amifostina como quimioprotector con trasplante; enfoque en cuidados de soporte |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [14151951](https://pubmed.ncbi.nlm.nih.gov/14151951/) | 1964 | Otro (función hipofisaria) | Acta - Unio Internationalis Contra Cancrum | Estudio antiguo sobre la influencia de fármacos hormonales y alquilantes en la función estimulante folicular de la hipófisis; sin resumen disponible y de relevancia clínica limitada |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20167599 | Melfalán 50 mg | Polvo liofilizado para reconstituir a solución inyectable | MELPHALAN | Cancelado |
| 20269433 | Melfalán para inyección 50 mg/vial | Polvo liofilizado | MELPHALAN | Cancelado |
| 218558 | Alkeran® inyectable | Polvo liofilizado para reconstituir a solución inyectable | MELPHALAN | Cancelado |
| 46265 | Alkeran® 2 mg tabletas | Tableta cubierta con película | MELPHALAN | Cancelado |
| 20161853 | Nozomi® 50 mg | Polvo liofilizado para reconstituir a solución inyectable | MELPHALAN | Cancelado |

Se muestran 5 de los 7 registros; los otros dos (Myelkilan® y Melfaseven®) también están cancelados.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (agente alquilante, mostaza nitrogenada) |
| Riesgo de Mielosupresión | Alto. Los datos del grafo de conocimiento asocian el fármaco con contraindicaciones en neutropenia, leucopenia, trombocitopenia y anemia, y los regímenes de dosis altas requieren rescate con células madre |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal; vigilancia de función pulmonar |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

- **Condiciones con relación de contraindicación en el grafo de conocimiento** (no provienen del texto del prospecto): enfermedad renal, trombocitopenia, anemia (incluida la macrocítica y la hemolítica), leucopenia, agranulocitosis, neutropenia (incluidas varias formas congénitas), enfermedad pulmonar intersticial, fibrosis pulmonar, lesión hepática inducida por fármacos y vasculitis.
- **Interacciones farmacológicas**: se identificaron 234 interacciones. Entre las principales:
  - Moderadas: anfotericina B (y sus formulaciones lipídicas, de sulfato de colesterilo y liposomal).
  - Leves: cimetidina, levofloxacino, sulfato de zinc y gluconato de zinc.
  - Nivel desconocido (ejemplos): omeprazol, pantoprazol, prednisona, metformina, morfina y vancomicina.
- Una revisión de 1984 señala que los agentes alquilantes como el melfalán tienen una de las tasas más altas de segundas neoplasias, sobre todo leucemias agudas.

Las advertencias y contraindicaciones del prospecto no están disponibles; consultar el prospecto para la información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Aunque el puntaje de TxGNN es muy alto y existe un ensayo de Fase 2 completado en tumores germinales recidivantes, se trata de un régimen combinado en el que no se puede aislar el efecto del melfalán. Además, hoy no hay ningún registro sanitario vigente en Colombia y faltan los datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Resultados publicados del ensayo NCT00936936 y análisis de la contribución específica del melfalán.
- Información del prospecto (advertencias y contraindicaciones) y datos del mecanismo de acción.
- Aclarar la situación regulatoria: tramitar un nuevo registro o importación bajo un régimen especial, dado que todos los registros están cancelados.
- Comparación con los esquemas actuales de rescate en tumores germinales (por ejemplo, regímenes de dosis altas con carboplatino y etopósido).
- Un plan de monitoreo hematológico, renal y pulmonar para poblaciones de riesgo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

