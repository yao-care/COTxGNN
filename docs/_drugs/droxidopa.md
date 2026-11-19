---
layout: default
title: Droxidopa
parent: Solo Predicción del Modelo (L5)
nav_order: 239
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
description: "Droxidopa: nueva indicación predicha, Prionopatía variablemente sensible a proteasas (nivel de evidencia L5). Indicación original: DROXIDOPA"
monitor_inn: "DROXIDOPA"
predicted_indications: ["variably protease-sensitive prionopathy"]
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

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Droxidopa: De Indicación No Especificada en el Registro a Prionopatía Variablemente Sensible a Proteasas
{: .text-alpha }

## Resumen en Una Frase

Droxidopa es un precursor sintético de la noradrenalina; en el registro sanitario colombiano figura únicamente con el nombre del principio activo, sin una indicación detallada.
El modelo TxGNN predice que podría ser efectivo para la **prionopatía variablemente sensible a proteasas (VPSPr)**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es solo una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | DROXIDOPA (el registro no detalla la indicación) |
| Nueva Indicación Predicha | Prionopatía variablemente sensible a proteasas |
| Puntaje de Predicción TxGNN | 0.9933 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Droxidopa (traducción no oficial): «Se desconoce el mecanismo de acción exacto de NORTHERA en el tratamiento de la hipotensión ortostática neurogénica. NORTHERA es un análogo sintético de aminoácido que se metaboliza directamente a norepinefrina por acción de la dopa-descarboxilasa, la cual está ampliamente distribuida por todo el organismo.» Texto original en inglés: "The exact mechanism of action of NORTHERA in the treatment of neurogenic orthostatic hypotension is unknown. NORTHERA is a synthetic amino acid analog that is directly metabolized to norepinephrine by dopa­-decarboxylase, which is extensively distributed throughout the body." ([DailyMed: Northera (droxidopa) prescribing information, Lundbeck Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2179f02c-48d7-48eb-8007-5ae43d8d16bc), versión del 2019-07-01; consultado el 2026-11-19). Según la información conocida, droxidopa es un aminoácido sintético precursor de la noradrenalina, que se convierte en esta por acción de la enzima descarboxilasa de L-aminoácidos aromáticos. Se usa en la hipotensión ortostática neurogénica.

La VPSPr es una enfermedad priónica esporádica y rara, caracterizada por la acumulación de proteína priónica mal plegada y por neurodegeneración. La acción noradrenérgica de droxidopa no actúa sobre el mal plegamiento, la propagación del prión ni la pérdida neuronal. **Con los datos disponibles no se sustenta un vínculo mecanístico directo.**

A lo sumo, podría considerarse para el manejo sintomático de la disfunción autonómica asociada a enfermedades neurodegenerativas, lo cual no equivale a un efecto modificador de la enfermedad. El puntaje elevado de TxGNN (0.9933) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica; su base no puede verificarse con la información disponible.

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
| 20178274 | XIDROPA® 300 (Laboratorios Legrand S.A.) | Cápsula dura | DROXIDOPA | Vigente |

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
La predicción se apoya solo en el modelo (L5), sin ensayos ni publicaciones, y no hay un vínculo mecanístico plausible entre la acción noradrenérgica de droxidopa y la fisiopatología priónica.

<!-- review:begin co-lic-20261105-droxidopa-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción se apoya solo en el modelo (L5), sin ensayos ni publicaciones, y no hay un vínculo mecanístico plausible entre la acción noradrenérgica de droxidopa y la fisiopatología priónica. Además, el único registro sanitario en Colombia está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-droxidopa-1 -->

**Para avanzar se necesita:**
- Obtener y analizar el prospecto del INVIMA (advertencias y contraindicaciones), indispensable para cualquier evaluación de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar estudios preclínicos que evalúen algún efecto de droxidopa sobre el plegamiento o la propagación del prión.
- Aclarar la base de la predicción del modelo TxGNN (aprendizaje profundo), por ejemplo, qué similitudes entre enfermedades relacionadas aprendió el modelo, ya que no constituyen evidencia biológica.
- Considerar, si hay interés clínico, un enfoque de manejo sintomático de la disfunción autonómica, evaluado por separado y no como terapia modificadora de la enfermedad.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Además, el único registro sanitario en Colombia está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Northera (droxidopa) prescribing information, Lundbeck Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2179f02c-48d7-48eb-8007-5ae43d8d16bc) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

