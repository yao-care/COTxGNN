---
layout: default
title: Axitinib
parent: Solo Predicción del Modelo (L5)
nav_order: 68
evidence_level: L5
indication_count: 10
---

# Axitinib
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

# Axitinib: De Carcinoma de Células Renales Avanzado a Carcinoma Renal con Translocaciones Xp11.2/Fusiones del Gen TFE3

## Resumen en Una Frase

Axitinib es un inhibidor oral de los receptores VEGFR1-3, utilizado en el tratamiento del carcinoma de células renales (CCR) avanzado.
El modelo TxGNN predice que podría ser efectivo para el **carcinoma renal asociado a translocaciones Xp11.2/fusiones del gen TFE3**,
con **1 ensayo clínico** (fase 2, sin resultados publicados) y **ninguna publicación** que respalden actualmente esta dirección específica.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Carcinoma de células renales avanzado (el texto del registro INVIMA solo dice "AXITINIB" y no detalla la indicación; esta se toma de la evidencia clínica del paquete) |
| Nueva Indicación Predicha | Carcinoma de células renales asociado a translocaciones Xp11.2/fusiones del gen TFE3 |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L5 (criterio estricto: el único ensayo no está completado y no tiene resultados; el Evidence Pack sugiere L2) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados de DrugBank sobre el mecanismo de acción. Según la información del paquete de evidencia, axitinib es un inhibidor selectivo de VEGFR1-3 (con actividad más débil sobre PDGFR y KIT) que bloquea la angiogénesis tumoral. Su eficacia en el CCR de células claras está respaldada por ensayos de fase 3: AXIS en segunda línea, y KEYNOTE-426 y JAVELIN Renal 101 en primera línea combinado con inmunoterapia.

El CCR con fusión TFE3 es un tumor muy vascularizado. Por eso el bloqueo antiangiogénico es mecanísticamente plausible, y los inhibidores de VEGFR habrían mostrado actividad en series retrospectivas. Esas series no forman parte de los datos recibidos, así que no se pueden verificar aquí.

Esta variante es biológicamente distinta del CCR de células claras, que es el que domina los ensayos pivotales. Por eso la extrapolación es indirecta y hoy se apoya en la cercanía en el grafo de conocimiento y en un ensayo pequeño en curso.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03595124](https://clinicaltrials.gov/study/NCT03595124) | Fase 2 | Activo, sin reclutamiento | 15 | Ensayo aleatorizado de axitinib + nivolumab frente a nivolumab solo en CCR con translocación TFE, irresecable o metastásico, en todos los grupos de edad. Sin resultados disponibles; la muestra es muy pequeña y la finalización está prevista para nov. 2026. |

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación específica.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20210813 | GLENMARK AXZYB® 5 MG TABLETAS RECUBIERTAS | Tableta recubierta | Solo figura el principio activo: AXITINIB |
| 20056375 | INLYTA® 1 MG TABLETA RECUBIERTA | Tableta recubierta | Solo figura el principio activo: AXITINIB |

Nota: el paquete reporta 20 registros en total, pero solo se incluyeron 5 entradas, de las cuales 4 son duplicados del registro 20210813.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasa de VEGFR1-3) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Presión arterial (hipertensión), función hepática, y signos de sangrado o trombosis (según las salvaguardas del paquete de evidencia) |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para esta variante específica solo existe un ensayo de fase 2 pequeño (n=15), aún sin resultados, y ninguna publicación. La predicción es mecanísticamente plausible, pero todavía no hay evidencia clínica que la confirme.

**Para avanzar se necesita:**
- Resultados del ensayo NCT03595124, cuya finalización está prevista para noviembre de 2026.
- Datos de eficacia específicos para CCR con fusión TFE3, por ejemplo las series retrospectivas mencionadas en el análisis mecanístico.
- Datos del mecanismo de acción desde DrugBank.
- Advertencias y contraindicaciones del prospecto INVIMA, requeridas para el tamizaje de seguridad.
- Vigilar hipertensión, función hepática, riesgo de sangrado o trombosis e interacciones con CYP3A4 si se avanza.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

