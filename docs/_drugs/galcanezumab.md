---
layout: default
title: Galcanezumab
parent: Solo Predicción del Modelo (L5)
nav_order: 308
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-12
monitor_inn: "GALCANEZUMAB"
predicted_indications: ["heparin cofactor 2 deficiency", "antithrombin deficiency type 2", "factor 5 excess with spontaneous thrombosis"]
description: "Galcanezumab: nueva indicación predicha, Deficiencia del cofactor 2 de la heparina (heparin cofactor 2 deficiency) (nivel de evidencia L5). Indicación original: GALCANEZUMAB"
---

# Galcanezumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Galcanezumab: Deficiencia del cofactor 2 de la heparina (heparin cofactor 2 deficiency)
{: .text-alpha }

## Resumen en Una Frase

Galcanezumab es un anticuerpo monoclonal que neutraliza el péptido relacionado con el gen de la calcitonina (CGRP). Se usa para la prevención de la migraña y la cefalea en racimos, aunque el registro sanitario colombiano solo menciona el nombre del principio activo y no detalla la indicación.
El modelo TxGNN predice que podría ser efectivo para **deficiencia del cofactor 2 de la heparina**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | GALCANEZUMAB |
| Nueva Indicación Predicha | Deficiencia del cofactor 2 de la heparina (heparin cofactor 2 deficiency) |
| Puntaje de Predicción TxGNN | 0.9950 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, galcanezumab neutraliza el CGRP, un neuropéptido que participa en la señalización del dolor trigeminovascular y en la vasodilatación.

La deficiencia del cofactor 2 de la heparina es un trastorno de los inhibidores de la coagulación, en el que se reduce la inhibición de la trombina (gen SERPIND1). No se conoce que la señalización del CGRP regule la actividad de este cofactor ni la inhibición de la trombina.

**No se identificó un vínculo mecanístico creíble.** El puntaje alto de TxGNN (0.9950) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica; tampoco está respaldado por ensayos clínicos ni literatura. Las otras dos predicciones de mayor rango tienen la misma limitación:

- **Deficiencia de antitrombina tipo 2** (0.9941): es un defecto funcional de SERPINC1, y el CGRP no influye en la función de la antitrombina ni en la cascada de coagulación.
- **Exceso de factor V con trombosis espontánea** (0.9941): es una anomalía de la vía de coagulación sin relación conocida con el CGRP. Además, los anticuerpos contra la vía del CGRP tienen precauciones cardiovasculares y vasculares (por ejemplo, hipertensión y eventos de tipo Raynaud notificados tras la comercialización), por lo que una población propensa a trombosis requeriría mayor escrutinio de seguridad.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20155001 | EMGALITY (Eli Lilly and Company) | Solución inyectable | Galcanezumab (sin indicación detallada) |

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo computacional (nivel L5): no hay ensayos clínicos ni literatura, y la revisión no encontró un vínculo mecanístico creíble.

<!-- review:begin co-lic-20261105-galcanezumab-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción es solo computacional (nivel L5): no hay ensayos clínicos ni literatura, y la revisión no encontró un vínculo mecanístico creíble. Además, el único registro sanitario en Colombia está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-galcanezumab-2 -->

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank para evaluar mejor un posible vínculo biológico
- El prospecto de INVIMA con advertencias y contraindicaciones, para poder realizar la evaluación de seguridad
- Evidencia preclínica o clínica que conecte la inhibición del CGRP con la regulación de la coagulación
- Evaluación de seguridad cardiovascular y vascular específica para poblaciones con tendencia trombótica

<!-- review:begin co-lic-20261031-galcanezumab-1 -->

> **Corrección de revisión (2026-10-31)**: Texto original: "Aclarar la situación regulatoria (registro cancelado) y la compatibilidad de la vía de administración / Evaluación de seguridad cardiovascular y vascular específica para poblaciones con tendencia trombótica" Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-10-31. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261031-galcanezumab-1 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-10-31 | Eliminado: "Aclarar la situación regulatoria (registro cancelado) y la compatibilidad de la vía de administración" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Además, el único registro sanitario en Colombia está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

