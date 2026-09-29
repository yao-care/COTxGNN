---
layout: default
title: Selpercatinib
parent: Solo Predicción del Modelo (L5)
nav_order: 357
evidence_level: L5
indication_count: 3
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

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Selpercatinib: De Cáncer con Alteraciones en RET a Hipertensión Pulmonar

## Resumen en Una Frase

Selpercatinib es un inhibidor selectivo de la quinasa RET. Según la literatura revisada, se usa en cáncer de pulmón de células no pequeñas con fusión de RET y en carcinoma medular de tiroides. El modelo TxGNN predice que podría ser efectivo para **hipertensión pulmonar**, pero por ahora no hay **ningún ensayo clínico** ni **publicación** que estudie directamente esta indicación. La predicción se basa solo en el modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro. El texto de indicación del registro solo repite el nombre del fármaco. El uso oncológico se deduce de la literatura. |
| Nueva Indicación Predicha | Hipertensión pulmonar |
| Puntaje de Predicción TxGNN | 99.18% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, selpercatinib es un inhibidor selectivo de la quinasa RET. Su actividad se ha descrito en tumores con alteraciones de RET, como el cáncer de pulmón con fusión de RET y el carcinoma medular de tiroides. Mecanísticamente, su aplicación a la hipertensión pulmonar es **especulativa**.

El papel de la señalización de RET en la remodelación vascular pulmonar no está establecido en los datos disponibles. El puntaje del modelo es alto (0.992), pero no hay respaldo biológico ni clínico que lo acompañe. Además, la hipertensión sistémica es un evento adverso conocido de selpercatinib, por lo que cualquier uso en una enfermedad vascular pulmonar requeriría una revisión cuidadosa de la seguridad cardiovascular.

El modelo también predijo otras dos indicaciones: **migraña** (99.17%) y **migraña con aura de tronco encefálico** (99.05%). Ninguna tiene ensayos ni literatura. La conexión con migraña es solo una hipótesis: RET es receptor de ligandos de la familia GDNF y se expresa en algunas neuronas sensoriales, lo que sugiere un posible vínculo con las vías del dolor trigeminal. Esto tampoco está respaldado por evidencia.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Ninguna de las publicaciones encontradas estudia hipertensión pulmonar. Solo describen el uso y el perfil de seguridad de selpercatinib en oncología.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [34178121](https://pubmed.ncbi.nlm.nih.gov/34178121/) | 2021 | Análisis retrospectivo | Ther Adv Med Oncol | Análisis retrospectivo (SIREN) de pacientes con cáncer de pulmón de células no pequeñas con fusión de RET tratados con selpercatinib mediante un programa de acceso. Evalúa su eficacia en la práctica real. |
| [39372206](https://pubmed.ncbi.nlm.nih.gov/39372206/) | 2024 | Estudio de farmacovigilancia | Front Pharmacol | Compara los eventos adversos de pralsetinib y selpercatinib con datos reales del sistema FAERS de la FDA. |
| [41918669](https://pubmed.ncbi.nlm.nih.gov/41918669/) | 2026 | Reporte de caso | Cureus | Carcinoma medular de tiroides metastásico en NEM 2B con mutación RET M918T. Describe los retos del manejo a largo plazo y la terapia dirigida. |

---

## Información de Mercado en Colombia

Los 20 registros corresponden al mismo producto (los cinco primeros son idénticos), por lo que se muestra una sola vez.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20232108 | RETSEVMO ® 80 MG (ELI LILLY AND COMPANY) | Cápsula dura | El registro solo indica "SELPERCATINIB", sin texto de indicación |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor selectivo de la quinasa RET) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Presión arterial (la hipertensión es un evento adverso conocido). Para otros parámetros, consultar el prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Advertencia principal**: la hipertensión sistémica es un evento adverso conocido de selpercatinib. Es especialmente relevante si se considera su uso en una enfermedad vascular pulmonar.

Para las demás advertencias, contraindicaciones e interacciones farmacológicas, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (L5). No hay ensayos clínicos ni literatura que estudien selpercatinib en hipertensión pulmonar. El vínculo mecanístico es especulativo y el perfil de seguridad, en particular la hipertensión, plantea una preocupación adicional.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA, con sus advertencias y contraindicaciones.
- Completar los datos del mecanismo de acción (MOA) desde DrugBank.
- Realizar estudios preclínicos que respalden un papel de RET en la remodelación vascular pulmonar.
- Hacer una revisión formal de la seguridad cardiovascular, dado el riesgo de hipertensión.
- Aclarar la indicación aprobada en Colombia, porque el registro solo repite el nombre del fármaco.

*Este informe es solo de referencia para la investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

