---
layout: default
title: Teriparatide
parent: Solo Predicción del Modelo (L5)
nav_order: 619
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-12
description: "Teriparatide: nueva indicación predicha, Úlcera duodenal (nivel de evidencia L5). Indicación original: Osteoporosis en pacientes con alto riesgo de fractura"
monitor_inn: "Teriparatide"
predicted_indications: ["duodenal ulcer (disease)", "non-syndromic esophageal malformation", "duodenal obstruction", "duodenogastric reflux", "esophageal disease", "Worth syndrome", "autosomal dominant neovascular inflammatory vitreoretinopathy", "succinyl-CoA:3-ketoacid CoA transferase deficiency", "amenorrhea (disease)"]
---

# Teriparatide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Teriparatida: De Osteoporosis a Úlcera Duodenal
{: .text-alpha }

## Resumen en Una Frase

La teriparatida es un fragmento activo de la hormona paratiroidea (PTH 1-34), utilizado originalmente para tratar la osteoporosis en pacientes con alto riesgo de fractura. El modelo TxGNN predice que podría ser efectiva para **úlcera duodenal**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción; se basa únicamente en el modelo computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Osteoporosis en pacientes con alto riesgo de fractura (el registro sanitario solo indica el nombre del principio activo, "Teriparatide", sin texto de indicación detallado) |
| Nueva Indicación Predicha | Úlcera duodenal |
| Puntaje de Predicción TxGNN | 0.9986 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 4 de 4) |
| Número de Registros Sanitarios | 4 (vigentes: 4) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información farmacológica conocida, la teriparatida es un péptido que actúa sobre los receptores PTH1R y PTH2R. En el hueso y el riñón estimula la formación ósea mediada por osteoblastos, y su eficacia en osteoporosis ha sido comprobada.

**No se identifica una relación mecanística plausible con la úlcera duodenal.** La indicación original (fragilidad ósea) y la nueva (lesión de la mucosa duodenal) pertenecen a sistemas distintos, y los datos disponibles no respaldan ningún papel de la señalización de PTH1R en la cicatrización de la mucosa duodenal.

El puntaje alto de TxGNN (0.9986) proviene del modelo TxGNN (deep learning). Puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica ni clínica. Por ello debe tratarse como una señal computacional sin validación.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

<!-- review:begin co-lic-20261105-teriparatide-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "El único registro sanitario está cancelado, por lo que actualmente no hay un producto de teriparatida vigente con este registro en Colombia." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 4 registros sanitarios (vigentes: 4); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-teriparatide-2 -->

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20177308 | TERROSA® (GEDEON RICHTER PLC) | Solución inyectable | Teriparatide (sin texto de indicación detallado); estado: vigente |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del texto del prospecto): hipotensión, hipercalcemia, nefrocalcinosis, trastornos del metabolismo del fósforo, osteosarcoma óseo, enfermedad ósea de Paget, enfermedad de Paget juvenil, osteomalacia, raquitismo, urolitiasis, osteodistrofia renal, osteítis fibrosa e hiperparatiroidismo.
- **Interacciones farmacológicas:** no se reportan interacciones con otros fármacos. La consulta solo devolvió información de los blancos farmacológicos (receptores PTH1R y PTH2R).

Las advertencias y contraindicaciones del prospecto de INVIMA no están disponibles. Consultar el prospecto para información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para úlcera duodenal tiene evidencia de nivel L5: no hay ensayos, no hay literatura y no existe un vínculo mecanístico plausible.

<!-- review:begin co-lic-20261105-teriparatide-3 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción para úlcera duodenal tiene evidencia de nivel L5: no hay ensayos, no hay literatura y no existe un vínculo mecanístico plausible. Además, el único registro sanitario en Colombia está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 4 registros sanitarios (vigentes: 4); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-teriparatide-3 -->

**Para avanzar se necesita:**
- Una hipótesis mecanística que justifique el papel de PTH1R/PTH2R en la mucosa duodenal, y estudios preclínicos que la respalden.
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones) para completar la evaluación de seguridad.
- Datos detallados del mecanismo de acción (MOA).
- Priorizar otras predicciones del mismo fármaco con mejor sustento. Por ejemplo, la osteoporosis asociada al embarazo y la lactancia tiene literatura observacional (nivel L3) y una relación biológica coherente con el mecanismo de la teriparatida. Esta evidencia debería verificarse en los textos completos.

<!-- review:begin co-lic-20261031-teriparatide-1 -->

> **Corrección de revisión (2026-10-31)**: Texto original: "Confirmar la situación regulatoria (registro cancelado) y la disponibilidad de producto en Colombia. / Priorizar otras predicciones del mismo fármaco con mejor sustento." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-10-31. El medicamento tiene 4 registros sanitarios (vigentes: 4); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261031-teriparatide-1 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-10-31 | Eliminado: "Confirmar la situación regulatoria (registro cancelado) y la disponibilidad de producto en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "El único registro sanitario está cancelado, por lo que actualmente no hay un producto de teriparatida vigente con este registro en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Además, el único registro sanitario en Colombia está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

