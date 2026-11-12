---
layout: default
title: Ravulizumab
parent: Solo Predicción del Modelo (L5)
nav_order: 552
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
description: "Ravulizumab: nueva indicación predicha, Neutropenia congénita grave autosómica recesiva por deficiencia de G6PC3 (nivel de evidencia L5). Indicación original: No disponible"
monitor_inn: "RAVULIZUMAB"
predicted_indications: ["autosomal recessive severe congenital neutropenia due to G6PC3 deficiency", "cyclic hematopoiesis", "primary hyperoxaluria", "severe congenital neutropenia", "autosomal recessive severe congenital neutropenia due to CXCR2 deficiency", "primary immunodeficiency syndrome due to p14 deficiency", "pseudo-von Willebrand disease", "X-linked severe congenital neutropenia", "primary release disorder of platelets", "megaloblastic anemia (disease)"]
---

# Ravulizumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Ravulizumab: De Indicación Original No Especificada a Neutropenia congénita grave autosómica recesiva por deficiencia de G6PC3
{: .text-alpha }

## Resumen en Una Frase

Ravulizumab es un inhibidor del complemento C5 comercializado en Colombia como Ultomiris®. En el registro sanitario disponible no consta un texto de indicación aprobada, solo el nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para **neutropenia congénita grave autosómica recesiva por deficiencia de G6PC3**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata solo de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (el registro solo indica "Ravulizumab") |
| Nueva Indicación Predicha | Neutropenia congénita grave autosómica recesiva por deficiencia de G6PC3 |
| Puntaje de Predicción TxGNN | 0.9996 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, ravulizumab es un anticuerpo monoclonal que inhibe el componente C5 del complemento, bloqueando la vía terminal del complemento.

La neutropenia congénita por deficiencia de G6PC3 es un trastorno del metabolismo y la supervivencia de los neutrófilos. No se ha establecido un mecanismo mediado por el complemento en esta enfermedad, por lo que no es posible verificar un vínculo mecanístico entre la inhibición de C5 y la nueva indicación.

La alta puntuación (0.9996) refleja únicamente una predicción basada en la red de conocimiento. Sin ensayos, literatura ni datos del mecanismo original, la razonabilidad biológica de esta predicción no está respaldada. Cabe señalar que el modelo generó otras nueve predicciones con puntajes similares (entre 0.9980 y 0.9994), en su mayoría trastornos hematológicos raros (por ejemplo, neutropenia cíclica, neutropenia congénita grave, hiperoxaluria primaria), todas también sin evidencia clínica.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20224196 | ULTOMIRIS® | Solución concentrada para infusión | Ravulizumab |

---

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento TxGNN, no texto del prospecto)**: infección meningocócica.
- **Interacciones Farmacológicas**: se identificaron 4 interacciones de nivel menor con inmunoglobulina G humana (intravenosa, subcutánea, intramuscular, e intravenosa/subcutánea).
- **Consideración adicional**: el bloqueo del complemento terminal aumenta el riesgo de infecciones, y esto podría ser más relevante en poblaciones con inmunodeficiencia o neutropenia.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo computacional (nivel L5), sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico plausible entre la inhibición de C5 y la neutropenia por deficiencia de G6PC3. Además, faltan datos de seguridad del prospecto.

<!-- review:begin co-lic-20261105-ravulizumab-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, el único registro sanitario en Colombia está cancelado y faltan datos de seguridad del prospecto." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-ravulizumab-1 -->

**Para avanzar se necesita:**
- Datos del mecanismo de acción desde DrugBank y análisis del vínculo mecanístico con la nueva indicación
- Obtener y analizar el prospecto del INVIMA (advertencias y contraindicaciones), requisito para el tamizaje de seguridad
- Revisión sistemática de literatura y ensayos que evalúen el papel del complemento en la neutropenia congénita
- Evaluación del riesgo de infecciones (especialmente meningocócicas) en una población neutropénica o inmunodeficiente
- Estudios preclínicos que respalden la hipótesis antes de considerar cualquier estudio clínico

<!-- review:begin co-lic-20261105-ravulizumab-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Aclarar la indicación aprobada original y la situación regulatoria del registro cancelado / Revisión sistemática de literatura y ensayos que evalúen el papel del complemento en la neutropenia congénita" Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-ravulizumab-2 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "el único registro sanitario en Colombia está cancelado y" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Aclarar la indicación aprobada original y la situación regulatoria del registro cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

