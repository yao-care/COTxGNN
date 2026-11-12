---
layout: default
title: Paroxetine
parent: Solo Predicción del Modelo (L5)
nav_order: 501
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
description: "Paroxetine: nueva indicación predicha, Síndrome de Ohdo y variantes (nivel de evidencia L5). Indicación original: PAROXETINA"
monitor_inn: "paroxetine"
predicted_indications: ["Ohdo syndrome and variants"]
---

# Paroxetine
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

## Paroxetina: De Paroxetina (indicación no detallada en el registro) a Síndrome de Ohdo y variantes
{: .text-alpha }

## Resumen en Una Frase

Paroxetina es un inhibidor selectivo de la recaptación de serotonina (ISRS), cuyo registro sanitario en Colombia solo consigna el nombre del principio activo como indicación.
El modelo TxGNN predice que podría ser efectivo para el **Síndrome de Ohdo y variantes**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; la predicción se apoya únicamente en el puntaje del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | PAROXETINA (el registro no especifica una indicación clínica) |
| Nueva Indicación Predicha | Síndrome de Ohdo y variantes |
| Puntaje de Predicción TxGNN | 0.9911 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 5 de 6) |
| Número de Registros Sanitarios | 6 (vigentes: 5) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la paroxetina es un ISRS usado clásicamente en trastornos depresivos y de ansiedad. No obstante, el registro sanitario colombiano no detalla la indicación aprobada.

El síndrome de Ohdo y sus variantes (por ejemplo, el síndrome de Say-Barber-Biesecker-Young-Simpson, asociado a variantes del gen KAT6B) son trastornos congénitos raros que cursan con discapacidad intelectual, blefarofimosis y anomalías del desarrollo. Su base es epigenética y del desarrollo, y no se identifica una vía plausible que conecte la actividad serotoninérgica de un ISRS con esa causa.

El puntaje alto (0.9911) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas (por ejemplo, asociaciones con fenotipos neuroconductuales o del neurodesarrollo), no evidencia biológica ni un vínculo causal o terapéutico. Además, la paroxetina tiene señales de preocupación en el embarazo y el desarrollo temprano (como malformaciones cardíacas congénitas), lo que exige cautela en cualquier contexto de trastornos del desarrollo.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20065995 | NATH 7.5 MG CAPSULAS (vigente) | Cápsula dura | PAROXETINA |
| 19952343 | PAROXETINA 20 MG (vigente) | Tableta cubierta con película | PAROXETINA |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: epilepsia, trastorno bipolar, trastorno afectivo mayor, enfermedad hepática, enfermedad de la vesícula biliar, fractura patológica, trastornos de la coagulación sanguínea, síndrome neuroléptico maligno, síndrome de secreción inadecuada de ADH, síndrome nefrogénico de antidiuresis inapropiada, síndrome serotoninérgico y acatisia inducida por fármacos.
- **Interacciones farmacológicas**: se identificaron 327 interacciones en total. Entre las de nivel **mayor** figuran bupropión, lorcaserina, dietilpropión, dolasetrón, eliglustat, palonosetrón y fentermina. Entre las de nivel moderado se incluyen morfina, ácido acetilsalicílico, clorpropamida, cimetidina, claritromicina, dronabinol, eluxadolina, glimepirida y repaglinida. Aprepitant figura con interacción menor.
- Para advertencias y contraindicaciones del prospecto, consultar el prospecto del producto, ya que no se dispone de esa información.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el puntaje del modelo (nivel L5), sin ensayos clínicos, literatura ni un mecanismo plausible. Además, existen señales de cautela en el desarrollo temprano.

<!-- review:begin co-lic-20261105-paroxetine-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, no hay registros sanitarios vigentes en Colombia y existen señales de cautela en el desarrollo temprano." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 6 registros sanitarios (vigentes: 5); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-paroxetine-1 -->

**Para avanzar se necesita:**
- Obtener el mecanismo de acción desde DrugBank y analizar un posible vínculo mecanístico con la vía de KAT6B/epigenética.
- Descargar y analizar el prospecto en INVIMA para completar advertencias y contraindicaciones (brecha bloqueante para el tamizaje de seguridad).
- Realizar una búsqueda de literatura y ensayos clínicos específica para síndrome de Ohdo y paroxetina.
- Evaluar la viabilidad regulatoria.
- Valorar el riesgo-beneficio en población pediátrica y en contextos de desarrollo, dadas las señales de seguridad en el embarazo.

<!-- review:begin co-lic-20261105-paroxetine-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Evaluar la viabilidad regulatoria, dado que ambos registros están cancelados." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 6 registros sanitarios (vigentes: 5); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-paroxetine-2 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "no hay registros sanitarios vigentes en Colombia y" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "dado que ambos registros están cancelados" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

