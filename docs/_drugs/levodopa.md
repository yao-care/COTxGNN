---
layout: default
title: Levodopa
parent: Solo Predicción del Modelo (L5)
nav_order: 399
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
description: "Levodopa: nueva indicación predicha, Encefalitis subaguda de Rasmussen (nivel de evidencia L5). Indicación original: Levodopa con inhibidor de decarboxilasa e inhibidor de COMT"
monitor_inn: "LEVODOPA"
predicted_indications: ["Rasmussen subacute encephalitis"]
---

# Levodopa
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Levodopa: De Enfermedad de Parkinson (terapia con inhibidores de decarboxilasa y COMT) a Encefalitis Subaguda de Rasmussen
{: .text-alpha }

## Resumen en Una Frase

Levodopa es un precursor de dopamina que, según el registro sanitario colombiano, se utilizaba en combinación con un inhibidor de la decarboxilasa y un inhibidor de la COMT (producto Stalevo®).
El modelo TxGNN predice que podría ser efectivo para la **Encefalitis Subaguda de Rasmussen**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata solo de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Levodopa con inhibidor de decarboxilasa e inhibidor de COMT |
| Nueva Indicación Predicha | Encefalitis subaguda de Rasmussen |
| Puntaje de Predicción TxGNN | 0.9906 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 13 de 13) |
| Número de Registros Sanitarios | 13 (vigentes: 13) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este informe. Según la información conocida, la levodopa es un precursor de la dopamina: se convierte en dopamina por acción de la descarboxilasa de L-aminoácidos aromáticos y se utiliza junto con un inhibidor de la decarboxilasa (y a veces un inhibidor de la COMT) para reponer la dopamina estriatal en la enfermedad de Parkinson.

La encefalitis de Rasmussen es un trastorno cerebral inflamatorio raro, crónico y generalmente unilateral, con convulsiones focales refractarias, atrofia progresiva del hemisferio afectado y deterioro neurológico. Se cree que está impulsada por citotoxicidad mediada por linfocitos T y activación microglial.

**Con los datos disponibles no se identifica un vínculo mecanístico directo.** La reposición dopaminérgica no actúa sobre los mecanismos inmunomediados de esta enfermedad. El puntaje alto (0.9906) probablemente refleja asociaciones de red entre enfermedades neurológicas y no una justificación biológica validada.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 19995528 | STALEVO® comprimidos con cubierta pelicular 200/50/200 mg (Sandoz GmbH) | Tableta recubierta | Levodopa inhibidor de decarboxilasa e inhibidor COMT | Vigente |

---

## Consideraciones de Seguridad

No se dispone de advertencias ni contraindicaciones del prospecto. Con base en las fuentes disponibles:

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: el grafo de conocimiento asocia la levodopa con enfermedades en las que su uso podría estar contraindicado o requerir cautela, entre ellas:
  - **Neurológicas y psiquiátricas**: atrofia multisistémica, discinesia inducida por fármacos, epilepsia, trastornos psicóticos, esquizoafectivos y esquizofreniformes, trastornos de ansiedad, neuróticos y distímicos, trastorno mental.
  - **Cardiovasculares**: hipotensión ortostática, síndrome de taquicardia postural ortostática, infarto de miocardio, trombosis coronaria, paro cardíaco súbito, enfermedad de la conducción cardíaca.
  - **Oculares**: glaucoma de ángulo abierto y de ángulo cerrado.
  - **Digestivas**: úlcera gástrica, enfermedad ulcerosa péptica, enfermedad de la vesícula biliar, enfermedad diarreica.
  - **Metabólicas, renales y hepáticas**: diabetes mellitus, cetoacidosis diabética, enfermedad renal, enfermedad hepática, piouréter.
  - **Otras**: melanoma, hemoglobinopatía.
- **Interacciones farmacológicas** (se registraron 100; se muestran las principales):
  - **Moderadas**: epinefrina, efedrina, bupropión, metronidazol, piridoxina, metoclopramida, hierro, y anticolinérgicos como atropina, hiosciamina, metescopolamina, glicopirronio, clidinio, diciclomina y mepenzolato.
  - **Menores**: antiácidos como hidróxido de aluminio, carbonato de calcio, magaldrato y sales de magnesio (carbonato, hidróxido y óxido).

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y el mecanismo de la levodopa (reposición dopaminérgica) no se relaciona con la fisiopatología inmunomediada de la encefalitis de Rasmussen. Además, faltan datos de seguridad del prospecto.

<!-- review:begin co-lic-20261105-levodopa-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, el único registro sanitario colombiano está cancelado y faltan datos de seguridad del prospecto." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 13 registros sanitarios (vigentes: 13); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-levodopa-1 -->

**Para avanzar se necesita:**
- Datos del mecanismo de acción de la levodopa desde DrugBank y análisis de un posible vínculo con la neuroinflamación.
- Revisión de la literatura preclínica y clínica sobre dopaminérgicos en encefalitis de Rasmussen o epilepsias inflamatorias.
- Obtener y analizar el prospecto en INVIMA (advertencias y contraindicaciones), dado que la epilepsia figura entre las contraindicaciones del grafo de conocimiento.
- Evaluar la disponibilidad comercial en Colombia.
- Confirmar la compatibilidad de vías de administración con la nueva indicación.

<!-- review:begin co-lic-20261105-levodopa-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Evaluar la disponibilidad comercial en Colombia, ya que no hay registros vigentes." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 13 registros sanitarios (vigentes: 13); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-levodopa-2 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "el único registro sanitario colombiano está cancelado y" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "ya que no hay registros vigentes" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

