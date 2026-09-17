---
layout: default
title: Apixaban
parent: Solo Predicción del Modelo (L5)
nav_order: 41
evidence_level: L5
indication_count: 1
---

# Apixaban
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# APIXABAN: Evaluación Incompleta — Sin Predicciones TxGNN Disponibles

## Resumen en Una Frase

APIXABAN (DB06605) es un fármaco identificado como candidato para evaluación de reposicionamiento de fármacos.
Sin embargo, el Evidence Pack actual **no contiene indicaciones predichas por TxGNN**, no registra aprobaciones en Colombia y presenta brechas críticas de datos que impiden una evaluación completa.
No es posible generar un análisis de reposicionamiento en el estado actual del expediente.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sin datos disponibles |
| Nueva Indicación Predicha | Sin predicciones TxGNN disponibles |
| Puntaje de Predicción TxGNN | N/D |
| Nivel de Evidencia | L5 — Sin estudios reales asociados |
| Estado de Mercado en Colombia | No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | **Hold** |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El Evidence Pack de APIXABAN está incompleto en sus tres dimensiones clave: no se generaron predicciones TxGNN de nuevas indicaciones, no hay registros sanitarios activos en Colombia, y los datos de mecanismo de acción y seguridad no están disponibles. Sin indicaciones predichas, no existe base para un análisis de reposicionamiento.

**Para avanzar se necesita:**
- Ejecutar el pipeline TxGNN para generar predicciones de nuevas indicaciones (`predicted_indications`)
- Obtener datos de mecanismo de acción (MOA) desde DrugBank API — brecha **DG002 (Alta severidad)**
- Resolver las advertencias y contraindicaciones desde el prospecto oficial — brecha **DG001 (Bloqueante)**
- Verificar el estado regulatorio actualizado en INVIMA Colombia
- Consultar fuentes de interacciones farmacológicas (DDI actualmente sin resultados)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

