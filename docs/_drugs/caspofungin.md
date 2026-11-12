---
layout: default
title: Caspofungin
parent: Solo Predicción del Modelo (L5)
nav_order: 140
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
description: "Caspofungin: nueva indicación predicha, Anomalía de la secreción de gastrina (nivel de evidencia L5). Indicación original: Caspofungina"
monitor_inn: "caspofungin"
predicted_indications: ["gastrin secretion abnormality"]
---

# Caspofungin
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

## Caspofungina: De Indicación Original (caspofungina, según registro INVIMA) a Anomalía de la Secreción de Gastrina
{: .text-alpha }

## Resumen en Una Frase

Caspofungina es un antifúngico de la clase de las equinocandinas; en el registro sanitario colombiano figura únicamente con el texto "CASPOFUNGIN" como indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **anomalía de la secreción de gastrina**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Caspofungina (el registro no detalla la indicación clínica) |
| Nueva Indicación Predicha | Anomalía de la secreción de gastrina |
| Puntaje de Predicción TxGNN | 0.9944 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 14 de 18) |
| Número de Registros Sanitarios | 18 (vigentes: 14) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según el conocimiento general, caspofungina es una equinocandina que inhibe la enzima beta-(1,3)-D-glucano sintasa, necesaria para la pared celular de los hongos. Por eso se utiliza en infecciones fúngicas.

La secreción de gastrina depende de las células G, del pH gástrico y de señales vagales y peptídicas. Ninguno de estos elementos es una diana conocida de caspofungina. Por lo tanto, no se identifica un vínculo mecanístico establecido entre la indicación original y la nueva indicación.

El puntaje alto de TxGNN (0.9944) proviene solo de una predicción del modelo TxGNN (aprendizaje profundo), sin una justificación a nivel de vías biológicas. Cualquier relación sería especulativa (por ejemplo, un efecto indirecto por colonización fúngica gastrointestinal o un efecto fuera de diana), y los datos disponibles no la respaldan.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20095165 | KAFUM 50 MG/VIAL | Polvo liofilizado para reconstituir a solución inyectable | CASPOFUNGIN |

## Consideraciones de Seguridad

- **Enfermedades asociadas a contraindicación en el grafo de conocimiento** (relaciones fármaco-enfermedad del grafo PrimeKG, no texto del prospecto): enfermedad hepática, enfermedad de la vesícula biliar y deficiencia de potasio.
- **Interacciones farmacológicas**: se identificaron 81 interacciones potenciales. Las principales:
  - **Mayor**: dexametasona.
  - **Moderada**: naltrexona.
  - **Nivel no clasificado**: entre otras, calcitriol, pantoprazol, doxiciclina, morfina, omeprazol, lansoprazol, vancomicina, sucralfato, lactulosa, prednisona, simvastatina, nistatina, epinefrina, anfotericina B, hidrocortisona, manitol, cloruro de potasio y prednisolona.

Para advertencias y contraindicaciones del prospecto, consultar el prospecto del producto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (L5), sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico plausible entre la inhibición de la glucano sintasa fúngica y la secreción de gastrina.

<!-- review:begin co-lic-20261105-caspofungin-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción se basa únicamente en el modelo (L5), sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico plausible entre la inhibición de la glucano sintasa fúngica y la secreción de gastrina. Además, el único registro sanitario en Colombia está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 18 registros sanitarios (vigentes: 14); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-caspofungin-1 -->

**Para avanzar se necesita:**
- Datos del mecanismo de acción desde DrugBank y análisis de posibles vías que conecten caspofungina con la regulación de la gastrina.
- Revisión sistemática de literatura y de registros de ensayos para identificar cualquier evidencia preclínica o clínica.
- Obtención y análisis del prospecto de INVIMA (advertencias y contraindicaciones), pendiente para el tamizaje de seguridad.
- Evaluación de la compatibilidad de la vía de administración (caspofungina es inyectable) con la nueva indicación.
- Aclarar la situación regulatoria en Colombia.

<!-- review:begin co-lic-20261105-caspofungin-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Aclarar la situación regulatoria en Colombia, dado que no hay registros vigentes." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 18 registros sanitarios (vigentes: 14); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-caspofungin-2 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Además, el único registro sanitario en Colombia está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "dado que no hay registros vigentes" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

