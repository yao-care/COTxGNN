---
layout: default
title: Celecoxib
parent: Solo Predicción del Modelo (L5)
nav_order: 119
evidence_level: L5
indication_count: 10
---

# Celecoxib
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

# Celecoxib: De Indicación Original No Especificada en el Registro a Displasia Acromesomélica tipo Hunter-Thompson

## Resumen en Una Frase

Celecoxib es un inhibidor selectivo de la COX-2 comercializado en Colombia, pero los registros disponibles no detallan su indicación original.
El modelo TxGNN predice que podría ser efectivo para **displasia acromesomélica tipo Hunter-Thompson**, con **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. La predicción parece un artefacto del grafo de conocimiento y no una señal clínica.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro solo repite el nombre "CELECOXIB") |
| Nueva Indicación Predicha | Displasia acromesomélica tipo Hunter-Thompson |
| Puntaje de Predicción TxGNN | 99.88% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, celecoxib actúa inhibiendo la COX-2 y reduce la inflamación y el dolor mediados por prostaglandinas.

La displasia acromesomélica tipo Hunter-Thompson es una displasia esquelética genética causada por pérdida de función de *CDMP1/GDF5*, lo que altera la señalización de las BMP. Celecoxib no actúa sobre esta vía.

**No se encontró un vínculo mecanístico plausible.** El puntaje alto de TxGNN (0.9988), sin ensayos ni publicaciones, parece un artefacto del grafo de conocimiento. La similitud con la indicación original no pudo evaluarse.

## Consideraciones sobre Otras Predicciones

Entre las 10 predicciones del paquete, solo una tiene evidencia sólida: **espondilopatía inflamatoria** (puesto 9, nivel L1, 2 ensayos de Fase 3 completados: NCT00762463 y NCT00648141). Sin embargo, la espondilitis anquilosante ya es un uso reconocido de celecoxib en muchas jurisdicciones. Por eso se trata de una confirmación de uso existente y no de un reposicionamiento novedoso. Conviene evaluarla por separado.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Se listan los registros únicos. El paquete de datos repite cuatro veces el registro 20193169, y solo hay dos registros distintos entre los datos entregados.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20193169 | SOSEDOL® | Cápsula dura | CELECOXIB (el texto no describe una indicación) |
| 19933716 | CELECOXIB 200 MG CÁPSULA | Cápsula dura | CELECOXIB (el texto no describe una indicación) |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas en la consulta realizada.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni publicaciones, y no existe un vínculo mecanístico plausible entre la inhibición de COX-2 y la vía GDF5/BMP. El puntaje alto del modelo no basta para avanzar.

**Para avanzar se necesita:**
- Un fundamento biológico que conecte la COX-2 con la señalización de BMP/GDF5. Sin él, no se justifica continuar con esta indicación.
- Completar los datos de seguridad (advertencias y contraindicaciones) desde el prospecto de INVIMA.
- Obtener el mecanismo de acción detallado desde DrugBank.
- Definir la indicación original aprobada, porque el registro solo repite el nombre del principio activo.
- Priorizar la revisión de la predicción de espondilopatía inflamatoria, que tiene mayor respaldo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

