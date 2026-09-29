---
layout: default
title: Guselkumab
parent: Solo Predicción del Modelo (L5)
nav_order: 215
evidence_level: L5
indication_count: 10
---

# Guselkumab
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

# Guselkumab: De Psoriasis en Placas a Osteoporosis Inducida por Fármacos

## Resumen en Una Frase

Guselkumab es un anticuerpo monoclonal anti-IL-23 (subunidad p19) que se comercializa como TREMFYA®. Su uso establecido es la psoriasis, aunque el registro sanitario colombiano solo lista el nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para **osteoporosis inducida por fármacos**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección. Es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el campo solo dice «GUSELKUMAB»); uso establecido: psoriasis |
| Nueva Indicación Predicha | Osteoporosis inducida por fármacos |
| Puntaje de Predicción TxGNN | 99.84% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 12 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos de DrugBank no traen el mecanismo de acción. Aun así, guselkumab es conocido como un anticuerpo monoclonal que bloquea la subunidad p19 de la interleucina-23 (IL-23). Esta citocina mantiene la diferenciación de los linfocitos Th17 en la inflamación inmunomediada, como la de la piel en la psoriasis.

La relación con la osteoporosis inducida por fármacos es débil. La IL-23 tiene un papel especulativo en la remodelación ósea, pero eso no está establecido para esta condición. No se identificó ningún vínculo clínico. El único respaldo es el puntaje alto de predicción del grafo de conocimiento (0.998), que no basta por sí solo para sustentar la hipótesis.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20123370 | TREMFYA® (JANSSEN CILAG S.A.) | Solución inyectable | GUSELKUMAB (el registro no detalla la indicación) |

El sistema tiene 12 registros en total. Los cinco primeros son entradas idénticas del mismo registro sanitario, por lo que se muestra una sola fila.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de osteoporosis inducida por fármacos no tiene ensayos, literatura ni mecanismo plausible documentado (nivel L5). Otras predicciones del mismo modelo, como psoriasis y colitis ulcerosa (ambas L1), corresponden a indicaciones ya conocidas del fármaco. Son confirmaciones, no reposicionamiento nuevo.

**Para avanzar se necesita:**
- Estudios preclínicos que muestren un papel de la IL-23 en el hueso, específicamente en la osteoporosis inducida por fármacos
- Revisión sistemática de la literatura sobre IL-23 y metabolismo óseo
- Datos de mecanismo de acción desde DrugBank
- Advertencias y contraindicaciones del prospecto de INVIMA, que hoy están pendientes
- Confirmar la indicación aprobada en Colombia, ya que el registro solo lista el nombre del principio activo
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

