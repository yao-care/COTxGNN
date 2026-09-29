---
layout: default
title: Teriparatide
parent: Solo Predicción del Modelo (L5)
nav_order: 381
evidence_level: L5
indication_count: 10
---

# Teriparatide
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

# Teriparatida: De Osteoporosis a Úlcera Duodenal

## Resumen en Una Frase

Teriparatida es el fragmento activo (1-34) de la hormona paratiroidea humana. Se usa para tratar la osteoporosis en pacientes con alto riesgo de fractura. El modelo TxGNN predice que podría ser efectivo para la **úlcera duodenal**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción, que por ahora es solo una señal del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Osteoporosis en pacientes con alto riesgo de fractura (el registro de INVIMA solo indica «TERIPARATIDE», sin texto de indicación) |
| Nueva Indicación Predicha | Úlcera duodenal |
| Puntaje de Predicción TxGNN | 99.86% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Por la información farmacológica registrada, teriparatida actúa sobre los receptores de la hormona paratiroidea PTH1R y PTH2R. Es un agente anabólico óseo que estimula la actividad de los osteoblastos, y su eficacia en osteoporosis está bien establecida.

Para la úlcera duodenal no se identificó un mecanismo plausible. Se trata de una lesión de la mucosa gastrointestinal, ligada al ácido, a *H. pylori* o a los antiinflamatorios, y no tiene relación conocida con la señalización de la PTH ni con la formación de hueso. El puntaje alto (99.86%) probablemente refleja conexiones indirectas en el grafo de conocimiento, no un vínculo biológico demostrado.

Por eso esta predicción debe leerse como una hipótesis sin respaldo. No hay razón mecanística ni datos clínicos que justifiquen avanzar.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20177308 | TERROSA® (GEDEON RICHTER PLC) | Solución inyectable | Solo figura «TERIPARATIDE», sin texto de indicación |

El total reportado es de 20 registros. Los cinco detalles entregados corresponden al mismo número de registro (20177308), por lo que se muestra una sola fila. La única forma farmacéutica registrada es la solución inyectable.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para úlcera duodenal es de nivel L5, sin ensayos ni literatura, y no existe un mecanismo biológico plausible que la sustente. No hay base para avanzar.

**Para avanzar se necesita:**
- Un vínculo mecanístico documentado entre la señalización PTH1R/PTH2R y la fisiopatología de la úlcera duodenal, o estudios preclínicos que lo sugieran.
- Los datos de seguridad del prospecto de INVIMA (advertencias y contraindicaciones), que faltan y bloquean el análisis de seguridad.
- Los datos del mecanismo de acción desde DrugBank.

**Otras predicciones del mismo fármaco.** La predicción con mayor respaldo no es la principal de esta lista. Es la **osteoporosis asociada al embarazo y la lactancia**, con nivel L3 (recomendación: Proceed with Guardrails). Cuenta con 2 ensayos clínicos indirectos, una revisión sistemática con metaanálisis y un estudio de cohorte retrospectivo sobre el uso de teriparatida, pero ningún ECA. El mecanismo encaja directamente con este fármaco. Se recomienda evaluarla en un informe aparte. Además, la pérdida ósea en la amenorrea hipotalámica funcional (L4) puede tratarse como pregunta de investigación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

