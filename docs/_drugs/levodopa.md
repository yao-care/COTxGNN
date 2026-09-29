---
layout: default
title: Levodopa
parent: Solo Predicción del Modelo (L5)
nav_order: 257
evidence_level: L5
indication_count: 1
---

# Levodopa
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

# Levodopa: De Levodopa con inhibidor de descarboxilasa e inhibidor de COMT a Encefalitis Subaguda de Rasmussen

## Resumen en Una Frase

Levodopa es un precursor de la dopamina que en Colombia se comercializa en combinación con un inhibidor de descarboxilasa y un inhibidor de COMT (Stalevo). El registro sanitario solo indica la composición y no describe la indicación clínica.
El modelo TxGNN predice que podría ser efectivo para la **Encefalitis Subaguda de Rasmussen**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Levodopa con inhibidor de descarboxilasa e inhibidor de COMT (el registro solo indica la composición, no una indicación clínica) |
| Nueva Indicación Predicha | Encefalitis subaguda de Rasmussen |
| Puntaje de Predicción TxGNN | 99.06% (posición 6917 en el ranking del modelo) |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, levodopa es un precursor de la dopamina y en Colombia se comercializa en combinación con un inhibidor de descarboxilasa y un inhibidor de COMT. Con los datos suministrados no se puede establecer un vínculo mecanístico respaldado por evidencia entre este fármaco y la nueva indicación.

La encefalitis de Rasmussen es una enfermedad neuroinflamatoria rara, crónica, unilateral y mediada por linfocitos T. Se manifiesta con convulsiones focales refractarias (a menudo epilepsia parcial continua), atrofia hemisférica progresiva y deterioro neurológico. Levodopa actúa sobre la vía dopaminérgica y no sobre la patología inmunomediada. Cualquier relación, como un efecto dopaminérgico sobre la neuroinflamación o sobre alteraciones del movimiento asociadas, sería especulativa.

El puntaje alto (99.06%) podría reflejar cercanía en el grafo de conocimiento, por ejemplo genes o fenotipos neurológicos compartidos, y no una relevancia causal. Antes de invertir más recursos hay que revisar manualmente la ruta del grafo que llevó a esta predicción.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Los 5 registros devueltos corresponden al mismo registro sanitario y al mismo producto, por lo que se presentan una sola vez. En total existen 20 registros sanitarios.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19995528 | Stalevo® comprimidos con cubierta pelicular 200/50/200 mg (Sandoz GmbH) | Tableta recubierta (vía oral) | Levodopa, inhibidor de descarboxilasa e inhibidor de COMT (solo composición) |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas en la consulta realizada.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo, sin ensayos clínicos ni literatura, y el mecanismo de acción de levodopa (dopaminérgico) no explica de forma evidente una enfermedad inmunomediada como la encefalitis de Rasmussen. Además, faltan los datos de seguridad del prospecto de INVIMA.

**Para avanzar se necesita:**
- Revisar manualmente la ruta del grafo de TxGNN que conecta levodopa con la encefalitis de Rasmussen.
- Obtener el mecanismo de acción detallado (por ejemplo, desde DrugBank).
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones), y precisar la indicación clínica aprobada.
- Hacer una búsqueda sistemática de ensayos clínicos y literatura, incluidos reportes de caso, sobre levodopa o dopaminérgicos en la encefalitis de Rasmussen.
- Evaluar la similitud con la indicación original y la compatibilidad de vías de administración, hoy pendientes.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

