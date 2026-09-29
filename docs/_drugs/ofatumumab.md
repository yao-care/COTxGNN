---
layout: default
title: Ofatumumab
parent: Solo Predicción del Modelo (L5)
nav_order: 301
evidence_level: L5
indication_count: 8
---

# Ofatumumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

# Ofatumumab: De Indicación Original No Especificada a Leucemia Linfocítica Crónica/Linfoma Linfocítico de Células Pequeñas con Hipermutación Somática de IGHV

## Resumen en Una Frase

Ofatumumab es un anticuerpo monoclonal anti-CD20 comercializado en Colombia como KESIMPTA (solución inyectable). Los datos disponibles no indican para qué enfermedad se aprobó originalmente.
El modelo TxGNN predice que podría ser efectivo para la **leucemia linfocítica crónica/linfoma linfocítico de células pequeñas con hipermutación somática de IGHV**, pero para esta indicación exacta hay **0 ensayos clínicos** y **0 publicaciones** que la respalden.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro solo dice «OFATUMUMAB») |
| Nueva Indicación Predicha | Leucemia linfocítica crónica/linfoma linfocítico de células pequeñas con hipermutación somática del gen de la región variable de la cadena pesada de inmunoglobulina (IGHV) |
| Puntaje de Predicción TxGNN | 99.77% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 2 (ambos con el mismo número de registro, 20190663) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos detallados de mecanismo de acción en el campo original de DrugBank. La justificación del análisis indica que ofatumumab se une a un epítopo de CD20 cercano a la membrana de los linfocitos B y los destruye por citotoxicidad dependiente del complemento (CDC) y por citotoxicidad celular dependiente de anticuerpos (ADCC).

La LLC/LLP con mutación de IGHV es un subtipo molecular de la leucemia linfocítica crónica, una neoplasia de linfocitos B que expresan CD20. Por eso, dirigirse a CD20 es biológicamente plausible.

Esta plausibilidad viene del mecanismo y de la enfermedad madre (LLC/LLP). Para este subtipo específico no hay ninguna evidencia clínica ni bibliográfica; solo existe el puntaje del modelo.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta indicación específica.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación específica.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20190663 | KESIMPTA (Novartis Pharma AG) | Solución inyectable | OFATUMUMAB (el registro no detalla la indicación) |

El registro aparece duplicado en los datos (2 entradas idénticas). Por eso se muestra una sola fila.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para este subtipo (IGHV mutado) solo existe el puntaje de predicción, sin ensayos ni publicaciones (nivel L5). Además, no hay datos de seguridad ni de indicación aprobada en Colombia.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones), un vacío de datos bloqueante.
- Confirmar la indicación aprobada de KESIMPTA. La presentación registrada es una solución inyectable; según conocimiento general (no consta en el Evidence Pack), esa marca corresponde a la formulación subcutánea usada en esclerosis múltiple, no a la formulación intravenosa usada en LLC. Hay que verificar la compatibilidad de vía de administración, que sigue pendiente.
- Obtener el mecanismo de acción desde DrugBank.
- Evaluar la indicación más general de la misma familia, **LLC/LLP** (puntaje 99.55%, nivel L1), que sí tiene ensayos de Fase 3 (por ejemplo NCT00824265, NCT01039376 y NCT01313689) y un metaanálisis. Ese nodo ya está marcado como «Proceed with Guardrails», con la advertencia de que puede ser un uso ya aprobado y no un reposicionamiento. Además, ofatumumab ha sido desplazado en gran parte por los inhibidores de BTK y BCL2.
- El **linfoma folicular** (nivel L2) tiene un ensayo aleatorizado de Fase 2 (CALGB 50904) y estudios de Fase 2. La ventaja incremental frente a rituximab u obinutuzumab no está demostrada.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

