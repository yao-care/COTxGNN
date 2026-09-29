---
layout: default
title: Rosuvastatin
parent: Solo Predicción del Modelo (L5)
nav_order: 350
evidence_level: L5
indication_count: 10
---

# Rosuvastatin
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

# Rosuvastatina: De Dislipidemia a Deficiencia de la Proteína de Transferencia de Ésteres de Colesterol (CETP)

## Resumen en Una Frase

La rosuvastatina es una estatina, utilizada para tratar la hiperlipidemia primaria, la dislipidemia mixta y la hipertrigliceridemia.
El modelo TxGNN predice que podría ser efectiva para la **deficiencia de la proteína de transferencia de ésteres de colesterol**, pero **no hay ensayos clínicos** y solo hay **2 publicaciones**, ambas reportes de casos de otros trastornos lipídicos (no estudios con rosuvastatina).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro sanitario (el texto registrado solo dice «Rosuvastatina»). Según la ficha farmacológica: hiperlipidemia primaria, dislipidemia mixta e hipertrigliceridemia |
| Nueva Indicación Predicha | Deficiencia de la proteína de transferencia de ésteres de colesterol |
| Puntaje de Predicción TxGNN | 99,54 % |
| Nivel de Evidencia | L5 (el Evidence Pack asigna L4, pero los artículos recuperados no estudian la rosuvastatina ni esta enfermedad) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

La rosuvastatina inhibe la enzima HMG-CoA reductasa (HMGCR), el paso limitante de la síntesis hepática de colesterol. Esto reduce el colesterol intrahepático, aumenta los receptores de LDL y disminuye el LDL-C. Los datos detallados de mecanismo de acción del Evidence Pack no están disponibles; este dato proviene de la ficha farmacológica (blanco: HMGCR).

El puntaje alto (99,54 %) probablemente refleja la cercanía dentro del grafo de conocimiento entre enfermedades del metabolismo lipídico, no una relación mecanística demostrada. La deficiencia de CETP eleva el HDL-C y no presenta un blanco terapéutico claro que responda a las estatinas.

Los dos artículos recuperados tratan de otras enfermedades (deficiencia completa de Apo AI y deficiencia de lipasa hepática) y no evalúan la rosuvastatina. No hay datos clínicos ni mecanísticos que respalden un beneficio en esta indicación.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [21122686](https://pubmed.ncbi.nlm.nih.gov/21122686/) | 2010 | Reporte de caso/Revisión | Journal of Clinical Lipidology | Deficiencia completa de Apo AI en una familia mandea iraquí, por una nueva mutación sin sentido en APOA1. Los dos homocigotos tuvieron presentaciones clínicas muy distintas. No evalúa la rosuvastatina |
| [22798447](https://pubmed.ncbi.nlm.nih.gov/22798447/) | 2010 | Reporte de caso | BMJ Case Reports | Deficiencia de lipasa hepática en un varón de origen árabe de Oriente Medio. Reporta la actividad y masa de CETP en este paciente. No evalúa la rosuvastatina |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20147254 | ROSUVITAE® 20 MG TABLETAS RECUBIERTAS | Tableta recubierta | Rosuvastatina (el texto registrado no detalla la indicación) |

Nota: el Evidence Pack reporta 20 registros en total, pero las cinco filas de muestra corresponden al mismo registro (20147254), por lo que se muestra una sola vez. También se registra la forma cápsula blanda.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni estudios de rosuvastatina en deficiencia de CETP, y la relación mecanística es débil, ya que esta enfermedad eleva el HDL-C y no ofrece un blanco claro para las estatinas. El puntaje del modelo no compensa la ausencia de evidencia real.

**Para avanzar se necesita:**
- Una revisión sistemática de la literatura sobre estatinas en deficiencia de CETP y en trastornos genéticos del HDL
- Datos de mecanismo o estudios preclínicos que muestren un efecto de la inhibición de HMGCR en esta enfermedad
- Advertencias y contraindicaciones del prospecto de INVIMA, aún no disponibles y necesarias para el tamizaje de seguridad
- Confirmar la indicación original registrada en Colombia, porque el campo de indicaciones originales está vacío
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

