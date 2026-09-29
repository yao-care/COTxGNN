---
layout: default
title: Vitamin A
parent: Solo Predicción del Modelo (L5)
nav_order: 409
evidence_level: L5
indication_count: 10
---

# Vitamin A
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

# Vitamin A: De Retinol (Vit A) a Deficiencia Congénita de Protrombina

## Resumen en Una Frase

La vitamina A (retinol) está registrada en Colombia como cápsulas de retinol y se usa como suplemento vitamínico.
El modelo TxGNN predice que podría ser efectiva para **deficiencia congénita de protrombina**, pero **ninguno de los 5 ensayos clínicos** recuperados evalúa vitamina A y **no hay publicaciones** que respalden esta dirección.
La predicción se basa casi exclusivamente en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Retinol (Vit A) |
| Nueva Indicación Predicha | Deficiencia congénita de protrombina |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la vitamina A (retinol) es un nutriente esencial de uso establecido en Colombia como suplemento en cápsulas. No hay datos que sustenten una acción sobre la coagulación.

La síntesis de protrombina depende de la vitamina K, no de la vitamina A. La deficiencia congénita de protrombina es un trastorno genético de la coagulación, y no se identificó ningún vínculo mecanístico creíble entre la vitamina A y esta enfermedad.

El puntaje alto de TxGNN (99.97%) no está respaldado por evidencia clínica ni bibliográfica. Probablemente refleja asociaciones generales del modelo dentro de la red de conocimiento, y no un efecto específico de la vitamina A.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03534752](https://clinicaltrials.gov/study/NCT03534752) | N/A | Completado | 220 | Estudio retrospectivo de adultos con errores innatos del metabolismo en Suiza francófona; sin intervención con vitamina A |
| [NCT02392767](https://clinicaltrials.gov/study/NCT02392767) | N/A | Completado | 25 | Suplemento combinado (L-arginina, Pycnogenol, vitamina K2, vitaminas B y ácido fólico) en hipertensión; no evalúa vitamina A |
| [NCT04384341](https://clinicaltrials.gov/study/NCT04384341) | N/A | Completado | 448 | Pérdida ósea en hemofilia; otro trastorno de coagulación, sin intervención con vitamina A |
| [NCT00168077](https://clinicaltrials.gov/study/NCT00168077) | Fase 3 | Completado | 40 | Concentrado de complejo de protrombina (Beriplex P/N) en deficiencia adquirida de factores por anticoagulación oral; no evalúa vitamina A ni la enfermedad congénita |
| [NCT00562783](https://clinicaltrials.gov/study/NCT00562783) | Fase 2 | Completado | 90 | Vitalliver en cirrosis descompensada; no se puede confirmar que el agente sea vitamina A ni que aplique a un trastorno de coagulación |

Ninguno de estos ensayos puede considerarse evidencia directa.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19960905 | VITAMINA A CAPSULAS (C.I. Farmacápsulas S.A.S.) | Cápsula dura | Retinol (Vit A) |

Se registran 20 entradas en total. Los 5 registros principales devueltos corresponden al mismo número sanitario y al mismo producto, por eso se muestran una sola vez.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción solo cuenta con el puntaje del modelo (nivel L5). No hay ensayos que evalúen vitamina A, no hay literatura, y la biología de la protrombina depende de la vitamina K, por lo que no existe un vínculo mecanístico creíble.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (consulta a DrugBank), actualmente ausentes.
- Advertencias y contraindicaciones del prospecto de INVIMA, actualmente no disponibles y pendientes para cualquier tamizaje de seguridad.
- Evidencia preclínica o clínica directa de vitamina A en trastornos de la coagulación. Sin ella, no se recomienda continuar con esta indicación.

**Nota:** en este mismo Evidence Pack, la indicación predicha en 7.º lugar, *enfermedad perinatal*, tiene evidencia de nivel L1 (Fase 3 y revisiones Cochrane) y decisión *Proceed with Guardrails*. Corresponde a un uso nutricional ya establecido, en poblaciones específicas como recién nacidos de muy bajo peso, y no a un reposicionamiento nuevo. Conviene evaluarla en un informe aparte.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

