---
layout: default
title: Treprostinil
parent: Solo Predicción del Modelo (L5)
nav_order: 395
evidence_level: L5
indication_count: 10
---

# Treprostinil
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

# Treprostinil: De Hipertensión Arterial Pulmonar a Malformación Arteriovenosa Pulmonar

## Resumen en Una Frase

Treprostinil es un análogo de la prostaciclina que en el registro sanitario colombiano figura solo con el nombre del principio activo. Por su uso conocido, se emplea en la hipertensión arterial pulmonar (dato a confirmar con el prospecto, porque el registro no trae la indicación).
El modelo TxGNN predice que podría ser efectivo para **malformación arteriovenosa pulmonar**, pero hoy hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (solo aparece "TREPROSTINILO"). Uso conocido: hipertensión arterial pulmonar, por verificar con el prospecto |
| Nueva Indicación Predicha | Malformación arteriovenosa pulmonar |
| Puntaje de Predicción TxGNN | 99.70% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base consultada. Según la información conocida, treprostinil es un análogo de la prostaciclina que actúa sobre el receptor IP y produce vasodilatación pulmonar. Su eficacia en enfermedad vascular pulmonar está establecida en otros contextos.

En este caso la relación con la nueva indicación es débil y la dirección del efecto es incierta. La malformación arteriovenosa pulmonar consiste en conexiones anormales entre arterias y venas, con paso de sangre sin oxigenar (cortocircuito). En ese escenario, una vasodilatación adicional podría aumentar el cortocircuito y empeorar la hipoxemia. Es decir, el efecto podría ser perjudicial.

El puntaje alto de TxGNN (99.70%) refleja una asociación en el grafo de conocimiento, no evidencia clínica. Sin ensayos ni literatura, esta predicción debe considerarse solo una hipótesis.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20154250 | TYVASO® 0.6 MG/ML AMPOLLA (Ferrer Internacional S.A.) | Solución para inhalación | TREPROSTINILO |

Los cinco registros devueltos corresponden al mismo número sanitario (20154250), por lo que se muestra una sola vez. Además de la solución para inhalación, se reporta una presentación de solución inyectable.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ensayos clínicos ni publicaciones (L5). Además, el mecanismo del fármaco (vasodilatación) podría empeorar el cortocircuito propio de esta enfermedad, por lo que no hay base para avanzar.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (indicación aprobada, advertencias y contraindicaciones), hoy sin datos.
- Completar los datos del mecanismo de acción desde DrugBank.
- Generar evidencia preclínica o fisiológica que demuestre que treprostinil no agrava el cortocircuito en este tipo de malformación.
- Priorizar otras indicaciones predichas para el mismo fármaco, que tienen respaldo mucho mayor:
  - Hipertensión arterial pulmonar asociada a enfermedad del tejido conectivo (L2, Proceed with Guardrails).
  - Hipertensión arterial pulmonar asociada a cardiopatía congénita (L3, Proceed with Guardrails).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

