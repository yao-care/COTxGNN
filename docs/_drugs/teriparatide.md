---
layout: default
title: Teriparatide
parent: Solo Predicción del Modelo (L5)
nav_order: 619
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Teriparatide: nueva indicación predicha, Úlcera duodenal (nivel de evidencia L5). Indicación original: Osteoporosis en pacientes con alto riesgo de fractura"
monitor_inn: "Teriparatide"
predicted_indications: ["duodenal ulcer (disease)", "non-syndromic esophageal malformation", "duodenal obstruction", "duodenogastric reflux", "esophageal disease", "Worth syndrome", "autosomal dominant neovascular inflammatory vitreoretinopathy", "pregnancy associated osteoporosis", "succinyl-CoA:3-ketoacid CoA transferase deficiency", "amenorrhea (disease)"]
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

La teriparatida es un fragmento activo de la hormona paratiroidea (PTH 1-34), utilizado originalmente para tratar la osteoporosis en pacientes con alto riesgo de fractura. El modelo TxGNN predice que podría ser efectiva para **úlcera duodenal**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción; se basa únicamente en el modelo computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Osteoporosis en pacientes con alto riesgo de fractura (el registro sanitario solo indica el nombre del principio activo, "Teriparatide", sin texto de indicación detallado) |
| Nueva Indicación Predicha | Úlcera duodenal |
| Puntaje de Predicción TxGNN | 99.86% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 (0 vigentes, 1 cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información farmacológica conocida, la teriparatida es un péptido que actúa sobre los receptores PTH1R y PTH2R. En el hueso y el riñón estimula la formación ósea mediada por osteoblastos, y su eficacia en osteoporosis ha sido comprobada.

**No se identifica una relación mecanística plausible con la úlcera duodenal.** La indicación original (fragilidad ósea) y la nueva (lesión de la mucosa duodenal) pertenecen a sistemas distintos, y los datos disponibles no respaldan ningún papel de la señalización de PTH1R en la cicatrización de la mucosa duodenal.

El puntaje alto de TxGNN (99.86%) es una predicción basada en grafos de conocimiento. Probablemente refleja la cercanía entre nodos de enfermedades en la red y no un hallazgo biológico o clínico. Por ello debe tratarse como una señal computacional sin validación.

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
| 20177308 | TERROSA® (GEDEON RICHTER PLC) | Solución inyectable | Teriparatide (sin texto de indicación detallado); estado: cancelado |

El único registro sanitario está cancelado, por lo que actualmente no hay un producto de teriparatida vigente con este registro en Colombia.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del texto del prospecto): hipotensión, hipercalcemia, nefrocalcinosis, trastornos del metabolismo del fósforo, osteosarcoma óseo, enfermedad ósea de Paget, enfermedad de Paget juvenil, osteomalacia, raquitismo, urolitiasis, osteodistrofia renal, osteítis fibrosa e hiperparatiroidismo.
- **Interacciones farmacológicas:** no se reportan interacciones con otros fármacos. La consulta solo devolvió información de los blancos farmacológicos (receptores PTH1R y PTH2R).

Las advertencias y contraindicaciones del prospecto de INVIMA no están disponibles. Consultar el prospecto para información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para úlcera duodenal tiene evidencia de nivel L5: no hay ensayos, no hay literatura y no existe un vínculo mecanístico plausible. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Una hipótesis mecanística que justifique el papel de PTH1R/PTH2R en la mucosa duodenal, y estudios preclínicos que la respalden.
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones) para completar la evaluación de seguridad.
- Datos detallados del mecanismo de acción (MOA).
- Confirmar la situación regulatoria (registro cancelado) y la disponibilidad de producto en Colombia.
- Priorizar otras predicciones del mismo fármaco con mejor sustento. Por ejemplo, la osteoporosis asociada al embarazo y la lactancia tiene literatura observacional (nivel L3) y una relación biológica coherente con el mecanismo de la teriparatida. Esta evidencia debería verificarse en los textos completos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

