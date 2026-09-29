---
layout: default
title: Droxidopa
parent: Solo Predicción del Modelo (L5)
nav_order: 168
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

# Droxidopa: De Hipotensión Ortostática Neurogénica a Prionopatía Variablemente Sensible a Proteasas

## Resumen en Una Frase

Droxidopa es un precursor aminoacídico sintético de la noradrenalina, comercializado para la hipotensión ortostática neurogénica sintomática.
El modelo TxGNN predice que podría ser efectivo para la **prionopatía variablemente sensible a proteasas (VPSPr)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es solo una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto aprobado solo dice «DROXIDOPA»); según la información disponible, hipotensión ortostática neurogénica |
| Nueva Indicación Predicha | Prionopatía variablemente sensible a proteasas (VPSPr) |
| Puntaje de Predicción TxGNN | 99.33% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 7 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos disponibles no respaldan un vínculo mecanístico. Droxidopa es un precursor de la noradrenalina: la enzima DOPA descarboxilasa la convierte en noradrenalina, y por eso se usa para la hipotensión ortostática neurogénica. No hay datos curados de mecanismo de acción (MOA) en DrugBank para contrastar la predicción.

La VPSPr es una enfermedad priónica esporádica y rara, causada por la proteína priónica mal plegada. No se conoce ninguna vía que conecte el reemplazo de noradrenalina con el mal plegamiento, la propagación del prion o la neurodegeneración.

El puntaje de 0.993 es únicamente una predicción del modelo. Podría reflejar cercanía en el grafo de conocimiento con términos neurodegenerativos o autonómicos, y no una relación biológica validada. Por ahora la predicción debe tratarse como una hipótesis sin sustento mecanístico.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20178274 | XIDROPA® 300 (LABORATORIOS LEGRAND S.A.) | Cápsula dura | Droxidopa (el registro no detalla la indicación) |

Nota: el sistema reporta 7 registros en total, pero el detalle recibido repite el mismo número de registro (20178274), por lo que se muestra una sola vez.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ensayos clínicos, literatura ni un mecanismo plausible que la respalde (nivel L5). Además, la VPSPr es una enfermedad priónica sin vínculo conocido con la vía noradrenérgica.

**Para avanzar se necesita:**
- Obtener del prospecto de INVIMA las advertencias y contraindicaciones (brecha de seguridad bloqueante)
- Completar los datos de mecanismo de acción desde DrugBank
- Revisar por qué el modelo asocia droxidopa con la VPSPr (vecindad en el grafo) y buscar estudios preclínicos que sustenten una hipótesis biológica
- Aclarar el detalle de los 7 registros sanitarios y la indicación aprobada en el registro colombiano

*Este informe es solo para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

