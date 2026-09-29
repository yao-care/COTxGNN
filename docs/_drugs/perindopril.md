---
layout: default
title: Perindopril
parent: Solo Predicción del Modelo (L5)
nav_order: 322
evidence_level: L5
indication_count: 5
---

# Perindopril
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Perindopril: De Perindopril y Amlodipino (combinación registrada) a Enfermedad Renal Hipertensiva Maligna

## Resumen en Una Frase

Perindopril es un inhibidor de la enzima convertidora de angiotensina (IECA). En Colombia está registrado en la combinación con amlodipino (COVERAM®), aunque el texto de indicación del registro no detalla la enfermedad aprobada.
El modelo TxGNN predice que podría ser efectivo para **enfermedad renal hipertensiva maligna**.
Actualmente hay **0 ensayos clínicos** y **1 publicación** recuperada, y esa publicación no estudia perindopril, por lo que la predicción es solo computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Perindopril y amlodipino (el registro no especifica la enfermedad) |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna |
| Puntaje de Predicción TxGNN | 99.77% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según el conocimiento farmacológico general (no según datos suministrados), perindopril es un IECA. Bloquea el sistema renina-angiotensina-aldosterona (SRAA), lo que puede reducir el tono de la arteriola eferente, la presión intraglomerular y el daño vascular mediado por angiotensina II.

La hipertensión maligna con compromiso renal se caracteriza por daño vascular renal agudo y una fuerte activación del SRAA. Por eso el bloqueo con un IECA es mecanísticamente plausible. Esa plausibilidad no equivale a evidencia clínica.

El puntaje TxGNN de 0.998 es una predicción del modelo. No hay ensayos registrados, y el único artículo recuperado trata sobre la función del riñón solitario tras nefrectomía por cáncer renal, sin evaluar perindopril.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36382821](https://pubmed.ncbi.nlm.nih.gov/36382821/) | 2022 | Observacional | Urologiia | Estado funcional del riñón solitario tras nefrectomía por cáncer renal. Trata la pérdida de función renal posquirúrgica; no evalúa perindopril ni hipertensión maligna, por lo que no respalda directamente la indicación. |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20007274 | COVERAM® 10 MG / 5MG COMPRIMIDOS (LES LABORATOIRES SERVIER) | Tableta | Perindopril y amlodipino |

Nota: el paquete de evidencia reporta 20 registros en total, pero los cinco listados corresponden al mismo registro (20007274), por lo que se muestra una sola vez.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se recuperaron advertencias, contraindicaciones ni interacciones farmacológicas en los datos disponibles.

Como nota general, no derivada de los datos: los IECA pueden precipitar deterioro renal agudo en estenosis bilateral de arteria renal o en riñón único estenótico. Esto es relevante para las indicaciones renales y renovasculares predichas.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo TxGNN (nivel L5). No hay ensayos clínicos ni literatura que evalúe perindopril en esta condición. Además, falta la información de seguridad del prospecto de INVIMA, que es un vacío bloqueante para pasar al tamizaje de seguridad.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA para obtener advertencias y contraindicaciones (vacío bloqueante).
- Obtener datos del mecanismo de acción desde DrugBank.
- Realizar una búsqueda de literatura dirigida (perindopril o IECA en hipertensión maligna y nefropatía hipertensiva) para reemplazar el artículo no relacionado.
- Evaluar explícitamente el riesgo renal de los IECA en pacientes con enfermedad renovascular antes de considerar esa indicación relacionada.
- Confirmar la indicación clínica aprobada de los registros colombianos, ya que el texto actual solo indica la combinación.

Las otras cuatro indicaciones predichas (hipertensión renovascular maligna, dos formas de hipertensión pulmonar y síndrome de Braddock) no tienen evidencia y quedan en Hold (nivel L5).

*Este informe es solo para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

