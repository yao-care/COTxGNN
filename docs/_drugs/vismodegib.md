---
layout: default
title: Vismodegib
parent: Solo Predicción del Modelo (L5)
nav_order: 408
evidence_level: L5
indication_count: 10
---

# Vismodegib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Vismodegib: De Carcinoma Basocelular Avanzado a Meduloblastoma con Nodularidad Extensa

## Resumen en Una Frase

Vismodegib (Erivedge®) es un inhibidor oral de la vía Hedgehog que actúa sobre Smoothened (SMO). Se comercializa para el carcinoma basocelular avanzado.
El modelo TxGNN predice que podría ser efectivo para **meduloblastoma con nodularidad extensa**,
pero para esta indicación hay **0 ensayos clínicos** y **0 publicaciones** que la respalden, por lo que la predicción es solo computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Carcinoma basocelular avanzado (el registro sanitario solo consigna el texto "VISMODEGIB", sin describir la indicación) |
| Nueva Indicación Predicha | Meduloblastoma con nodularidad extensa |
| Puntaje de Predicción TxGNN | 99.93% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 4 (todos con el mismo número de registro, 20048393) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, vismodegib inhibe la proteína Smoothened (SMO) de la vía Hedgehog. Su eficacia en el carcinoma basocelular, un tumor impulsado por la activación de PTCH1/SMO, está establecida, y mecanísticamente podría ser aplicable a tumores con señalización Hedgehog aberrante.

El meduloblastoma con nodularidad extensa se asocia estrechamente con el subgrupo SHH del meduloblastoma, en el que la señalización Hedgehog anómala impulsa el tumor. Por eso el vínculo es biológicamente plausible.

Aun así, no se aportaron ensayos ni literatura para esta indicación, y un puntaje alto del modelo no es evidencia clínica. Además, el uso pediátrico plantea una preocupación por el cierre prematuro e irreversible de las placas de crecimiento.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta indicación.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20048393 | ERIVEDGE® (F. Hoffmann-La Roche Ltda., Basilea, Suiza) | Cápsula dura | VISMODEGIB (el registro no detalla la indicación) |

Las 4 entradas de licencia del paquete de evidencia son idénticas, por eso se muestran una sola vez.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de la vía Hedgehog/SMO) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto y la normativa institucional de manejo de antineoplásicos orales |

## Consideraciones de Seguridad

- **Riesgo en población pediátrica**: en el meduloblastoma, el uso en niños genera preocupación por el cierre prematuro e irreversible de las placas de crecimiento.
- **Efectos asociados a vismodegib en otras indicaciones** (según el análisis del paquete de evidencia): teratogenicidad, espasmos musculares, alopecia y disgeusia.
- No se identificaron interacciones farmacológicas registradas.

Consultar el prospecto para información de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para meduloblastoma con nodularidad extensa es de nivel L5: solo hay un puntaje del modelo, sin ensayos ni publicaciones. El riesgo en pediatría requiere una evaluación específica antes de avanzar.

**Para avanzar se necesita:**
- Datos de mecanismo de acción (MOA) desde DrugBank
- Prospecto de INVIMA con advertencias y contraindicaciones
- Evidencia preclínica o clínica de vismodegib en meduloblastoma del subgrupo SHH
- Evaluación de seguridad pediátrica, en particular el efecto sobre las placas de crecimiento

**Nota sobre otras indicaciones predichas en el mismo análisis:**
- **Cáncer de piel** (puntaje 99.82%, nivel L2, "Proceed with Guardrails"): 23 ensayos y 20 publicaciones, con fase 1, varias fase 2 y un estudio de seguridad de una sola rama con 1232 pacientes. Se centra en el carcinoma basocelular, donde vismodegib ya está comercializado, y no debe extrapolarse a otros cánceres de piel.
- **Xeroderma pigmentoso** (puntaje 99.91%, nivel L4, "Research Question"): 3 reportes de caso de vismodegib para carcinoma basocelular en pacientes con xeroderma pigmentoso. Estos respaldan la actividad contra el tumor, no el tratamiento de la enfermedad de base.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

