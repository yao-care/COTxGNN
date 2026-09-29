---
layout: default
title: Lorazepam
parent: Solo Predicción del Modelo (L5)
nav_order: 263
evidence_level: L5
indication_count: 10
---

# Lorazepam
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

# Lorazepam: De Benzodiacepina Ansiolítica a Neoplasia del Nervio Trigémino

## Resumen en Una Frase

Lorazepam es una benzodiacepina que actúa sobre el receptor GABA-A. El registro sanitario colombiano no detalla su indicación original, y su uso clásico es sintomático (ansiedad, convulsiones).
El modelo TxGNN predice que podría ser efectivo para **neoplasia del nervio trigémino**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción. Es solo una señal del grafo de conocimiento.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto de indicación dice solo «LORAZEPAM») |
| Nueva Indicación Predicha | Neoplasia del nervio trigémino |
| Puntaje de Predicción TxGNN | 99.87% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Lorazepam es un modulador alostérico positivo del receptor GABA-A. Aumenta la conductancia de cloruro y produce efectos sedantes, ansiolíticos y anticonvulsivantes. El campo de mecanismo de acción (MOA) del Evidence Pack no está disponible, así que esta descripción proviene del análisis de racionalidad de la prediccion.

No se identificó un mecanismo antitumoral plausible que conecte lorazepam con un tumor del nervio trigémino. El puntaje alto (0.9987) refleja únicamente una asociación en el grafo. No hay estudios que la respalden. Cualquier uso en esta condición sería, como máximo, sintomático (ansiedad, convulsiones) y no modificaría la enfermedad.

La similitud entre la indicación original y la nueva no está evaluada.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19902389 | ATIVAN 2 MG TABLETAS (PFIZER S.A.S.) | Tableta | LORAZEPAM (sin indicación detallada) |

El Evidence Pack informa 20 registros en total, pero los 5 listados corresponden al mismo registro (19902389) repetido. Por eso se muestra una sola fila.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para neoplasia del nervio trigémino es L5: no hay ensayos, no hay literatura y no existe un mecanismo antitumoral plausible. No se justifica avanzar.

**Para avanzar se necesita:**
- Evidencia preclínica o clínica que vincule la modulación GABA-A con este tumor. Hoy no existe.
- Prospecto de INVIMA con advertencias y contraindicaciones, que es una brecha bloqueante para el tamizaje de seguridad.
- Datos de MOA verificados desde DrugBank.
- Considerar otras predicciones del mismo modelo con mejor respaldo. **Insomnio** (puntaje 99.80%) tiene nivel L2 y recomendación *Proceed with Guardrails*, con dos estudios clínicos comparativos (lorazepam vs. flurazepam, 1988; lorazepam TID, 1999). Las salvaguardas serían uso corto, riesgo de tolerancia y dependencia, sedación al día siguiente y caídas en adultos mayores. Varias predicciones de convulsiones reflejas (lectura, sobresalto, micción) están en L4 como preguntas de investigación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

