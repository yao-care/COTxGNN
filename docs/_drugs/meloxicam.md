---
layout: default
title: Meloxicam
parent: Solo Predicción del Modelo (L5)
nav_order: 273
evidence_level: L5
indication_count: 10
---

# Meloxicam
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

# Meloxicam: De AINE (indicación original no registrada) a Displasia Acromesomélica tipo Hunter-Thompson

## Resumen en Una Frase

Meloxicam es un antiinflamatorio no esteroideo (AINE) inhibidor de la COX-2. Los registros sanitarios colombianos del Evidence Pack no describen su indicación original.
El modelo TxGNN predice que podría ser efectivo para la **displasia acromesomélica tipo Hunter-Thompson**, con **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Además, el análisis mecanístico no encuentra un vínculo plausible.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible. El texto de indicación registrado solo dice "MELOXICAM" |
| Nueva Indicación Predicha | Displasia acromesomélica tipo Hunter-Thompson |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Meloxicam pertenece a la clase de los AINE y actúa inhibiendo la COX-2, con lo que reduce la síntesis de prostaglandinas y la inflamación y el dolor asociados.

La displasia acromesomélica tipo Hunter-Thompson es una displasia esquelética genética causada por pérdida de función de *CDMP1/GDF5*. El defecto está en el crecimiento óseo, y la inhibición de la COX-2 no actúa sobre esa vía. El análisis no identifica un vínculo plausible entre ambos.

El puntaje TxGNN es muy alto (99.92%), pero probablemente refleja cercanía en el grafo de conocimiento y no una relación farmacológica real. Por eso esta predicción debe tratarse como un artefacto del modelo mientras no se demuestre lo contrario.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Se reportan 20 registros en total. En la muestra de 5 filas, los registros aparecen repetidos, por lo que se listan solo los 2 registros distintos.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19986264 | MEPROGAL 15MG TABLETA | Tableta | MELOXICAM (sin descripción de indicación) |
| 227880 | ARTRICLOX 15 MG TABLETAS | Tableta | MELOXICAM (sin descripción de indicación) |

La vía de administración disponible es oral.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas en la consulta realizada.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos ni literatura que respalden la predicción, y el análisis mecanístico indica que la COX-2 no participa en la patogenia de la enfermedad. Con evidencia L5 (solo predicción del modelo), no se justifica avanzar.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA para obtener advertencias y contraindicaciones.
- Obtener los datos de mecanismo de acción desde DrugBank.
- Confirmar la indicación original aprobada de meloxicam, ya que el registro local solo muestra el nombre del principio activo.
- Revisar las otras predicciones del listado con mayor plausibilidad biológica:
  - Espondiloartropatía, susceptibilidad a (puesto 6). Los AINE son terapia de primera línea, pero no hay ensayos ni literatura en el paquete.
  - Artritis idiopática juvenil poliarticular con factor reumatoide positivo (puesto 8). Solo hay un estudio de seguridad de clase con celecoxib y AINE no selectivos, no específico de meloxicam. Podría ser un uso ya establecido y no un reposicionamiento, lo que debe verificarse contra el etiquetado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

