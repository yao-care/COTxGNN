---
layout: default
title: Droxidopa
parent: Solo Predicción del Modelo (L5)
nav_order: 239
evidence_level: L5
indication_count: 1
---

# Droxidopa
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Droxidopa: De Indicación No Especificada en el Registro a Prionopatía Variablemente Sensible a Proteasas

## Resumen en Una Frase

Droxidopa es un precursor sintético de la noradrenalina; en el registro sanitario colombiano figura únicamente con el nombre del principio activo, sin una indicación detallada.
El modelo TxGNN predice que podría ser efectivo para la **prionopatía variablemente sensible a proteasas (VPSPr)**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es solo una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | DROXIDOPA (el registro no detalla la indicación) |
| Nueva Indicación Predicha | Prionopatía variablemente sensible a proteasas |
| Puntaje de Predicción TxGNN | 99.33% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados (no comercializado) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, droxidopa es un aminoácido sintético precursor de la noradrenalina, que se convierte en esta por acción de la enzima descarboxilasa de L-aminoácidos aromáticos. Se usa en la hipotensión ortostática neurogénica.

La VPSPr es una enfermedad priónica esporádica y rara, caracterizada por la acumulación de proteína priónica mal plegada y por neurodegeneración. La acción noradrenérgica de droxidopa no actúa sobre el mal plegamiento, la propagación del prión ni la pérdida neuronal. **Con los datos disponibles no se sustenta un vínculo mecanístico directo.**

A lo sumo, podría considerarse para el manejo sintomático de la disfunción autonómica asociada a enfermedades neurodegenerativas, lo cual no equivale a un efecto modificador de la enfermedad. El puntaje elevado de TxGNN (0.993) proviene solo del grafo de conocimiento y su base no puede verificarse con la información disponible.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20178274 | XIDROPA® 300 (Laboratorios Legrand S.A.) | Cápsula dura | DROXIDOPA | Cancelado |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 32 interacciones en total. Las principales son:
  - **Mayor**: cocaína (tópica y nasal).
  - **Moderada**: simpaticomiméticos y fármacos afines, como epinefrina (incluidas las formas oftálmica y tópica), efedrina (incluida la nasal), fenilefrina (incluida la oftálmica), pseudoefedrina, isometepteno, dietilpropión, fenfluramina, mazindol y fentermina. También figuran agonistas beta-adrenérgicos (formoterol, salbutamol, indacaterol, isoprenalina) y azul de metileno.

  En general, se trata de combinaciones con otros agentes que actúan sobre el sistema adrenérgico, por lo que conviene vigilar la presión arterial y la frecuencia cardíaca.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (L5), sin ensayos ni publicaciones, y no hay un vínculo mecanístico plausible entre la acción noradrenérgica de droxidopa y la fisiopatología priónica. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto del INVIMA (advertencias y contraindicaciones), indispensable para cualquier evaluación de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar estudios preclínicos que evalúen algún efecto de droxidopa sobre el plegamiento o la propagación del prión.
- Aclarar la base de la predicción del modelo (por ejemplo, qué relaciones del grafo de conocimiento la sustentan).
- Considerar, si hay interés clínico, un enfoque de manejo sintomático de la disfunción autonómica, evaluado por separado y no como terapia modificadora de la enfermedad.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

