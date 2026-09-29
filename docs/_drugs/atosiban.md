---
layout: default
title: Atosiban
parent: Solo Predicción del Modelo (L5)
nav_order: 64
evidence_level: L5
indication_count: 10
---

# Atosiban
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

# Atosiban: De Tocolisis en Parto Prematuro a Glaucoma Hereditario Primario

## Resumen en Una Frase

Atosiban es un antagonista de los receptores de oxitocina y vasopresina V1A, usado en el contexto de la tocolisis (frenar el trabajo de parto prematuro).
El modelo TxGNN predice que podría ser efectivo para **glaucoma hereditario primario**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | El registro sanitario solo consigna «ATOSIBAN» como texto de indicación. El uso tocolítico proviene del contexto de los estudios recuperados. |
| Nueva Indicación Predicha | Glaucoma hereditario primario |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 8 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Atosiban antagoniza los receptores de oxitocina y de vasopresina V1A. Los datos de mecanismo de acción de DrugBank no están disponibles en este paquete, así que la descripción anterior se basa solo en la información contextual de las predicciones.

No se ha establecido un vínculo mecanístico entre este mecanismo y el glaucoma hereditario primario. El puntaje del modelo es alto (99.92%), pero es solo una predicción, sin ensayos ni literatura que la sustenten. La similitud con la indicación original tampoco ha sido evaluada.

Por ahora no puede afirmarse que la predicción sea razonable desde el punto de vista biológico. Requiere una revisión mecanística previa, por ejemplo si existe señalización de oxitocina o vasopresina relevante en la regulación de la presión intraocular.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Hay 8 registros sanitarios en total. Los datos disponibles corresponden a estos productos únicos (varias filas del origen estaban duplicadas):

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20131614 | EVERPREM® Solución para infusión 6.75 mg/0.9 mL | Solución para infusión | ATOSIBAN |
| 20131612 | EVERPREM® Concentrado para solución para infusión 37.5 mg/5 mL | Solución concentrada para infusión | ATOSIBAN |

Ambos productos son de EVER Valinject GmbH y se administran por infusión.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para glaucoma hereditario primario es de nivel L5: no tiene ensayos clínicos, literatura ni vínculo mecanístico establecido. Con solo el puntaje del modelo no hay base para avanzar.

Entre las 10 principales predicciones, la única con algo de literatura indirecta es «enfermedad vascular» (L4). Esa evidencia es preclínica y sugiere que antagonizar oxitocina podría ser neutral o perjudicial, no beneficioso.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank para analizar el vínculo con el glaucoma.
- Revisión de literatura específica sobre oxitocina o vasopresina y presión intraocular o neuroprotección retiniana.
- Evaluación de compatibilidad de vía de administración: atosiban está registrado solo en infusión, y el glaucoma requeriría probablemente una vía ocular o local.
- Advertencias y contraindicaciones del prospecto de INVIMA para el tamizaje de seguridad.
- Estudios preclínicos que respalden la hipótesis antes de considerar ensayos clínicos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

