---
layout: default
title: Baricitinib
parent: Solo Predicción del Modelo (L5)
nav_order: 78
evidence_level: L5
indication_count: 2
---

# Baricitinib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Baricitinib: De Indicación No Especificada en el Registro a Síndrome de Displasia Rizomélica con Microftalmia Colobomatosa

## Resumen en Una Frase

Baricitinib se comercializa en Colombia como tableta recubierta (Olumiant), pero el registro sanitario solo consigna el nombre del principio activo y no una indicación original.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de displasia rizomélica con microftalmia colobomatosa**,
sin **ningún ensayo clínico** ni **publicación** que respalde esta dirección; es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro solo dice "BARICITINIB") |
| Nueva Indicación Predicha | Síndrome de displasia rizomélica con microftalmia colobomatosa |
| Puntaje de Predicción TxGNN | 99.94% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos del mecanismo de acción no están disponibles en el Evidence Pack. En términos generales, baricitinib se conoce como inhibidor de JAK1/JAK2, pero esto no proviene de un MOA registrado en los datos recibidos.

La enfermedad predicha es un síndrome raro del desarrollo con malformaciones oculares y esqueléticas. No se aportó ningún papel establecido de la vía JAK-STAT en su patogenia, por lo que **no hay un vínculo mecanístico sustentado por los datos**. El puntaje de 0.9994 es solo una salida del modelo y puede reflejar la topología del grafo de conocimiento más que una biología real. No debe leerse como respaldo clínico.

También se predijo otra enfermedad: el **síndrome de braquidactilia-sindactilia** (puntaje 99.94%, también L5, Hold). Tampoco tiene ensayos ni literatura, y su vínculo con la inhibición de JAK1/JAK2 no está respaldado por los datos.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Se muestran los registros principales. Todos corresponden al registro sanitario 20157001 (Eli Lilly and Company), con presentaciones repetidas en los datos.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20157001 | Olumiant 2 mg | Tableta recubierta | Solo consta el nombre del principio activo (baricitinib) |
| 20157001 | Olumiant 4 mg | Tableta recubierta | Solo consta el nombre del principio activo (baricitinib) |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el puntaje del modelo (L5), sin ensayos, literatura ni vínculo mecanístico plausible. Además, faltan datos de seguridad y del mecanismo de acción.

**Para avanzar se necesita:**
- Obtener el mecanismo de acción desde DrugBank y evaluar si la vía JAK-STAT se relaciona con la enfermedad predicha
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones), que es un vacío bloqueante para el tamizaje de seguridad
- Aclarar la indicación original aprobada, ya que el registro solo muestra el nombre del fármaco
- Someter las predicciones a revisión de expertos y buscar evidencia preclínica o de mecanismo antes de cualquier seguimiento
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

