---
layout: default
title: Levodopa
parent: Solo Predicción del Modelo (L5)
nav_order: 399
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
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

# Levodopa: De Enfermedad de Parkinson (terapia con inhibidores de decarboxilasa y COMT) a Encefalitis Subaguda de Rasmussen

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
| Puntaje de Predicción TxGNN | 99.06% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este informe. Según la información conocida, la levodopa es un precursor de la dopamina: se convierte en dopamina por acción de la descarboxilasa de L-aminoácidos aromáticos y se utiliza junto con un inhibidor de la decarboxilasa (y a veces un inhibidor de la COMT) para reponer la dopamina estriatal en la enfermedad de Parkinson.

La encefalitis de Rasmussen es un trastorno cerebral inflamatorio raro, crónico y generalmente unilateral, con convulsiones focales refractarias, atrofia progresiva del hemisferio afectado y deterioro neurológico. Se cree que está impulsada por citotoxicidad mediada por linfocitos T y activación microglial.

**Con los datos disponibles no se identifica un vínculo mecanístico directo.** La reposición dopaminérgica no actúa sobre los mecanismos inmunomediados de esta enfermedad. El puntaje alto (0.99) probablemente refleja asociaciones de red entre enfermedades neurológicas y no una justificación biológica validada.

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
| 19995528 | STALEVO® comprimidos con cubierta pelicular 200/50/200 mg (Sandoz GmbH) | Tableta recubierta | Levodopa inhibidor de decarboxilasa e inhibidor COMT | Cancelado |

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
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y el mecanismo de la levodopa (reposición dopaminérgica) no se relaciona con la fisiopatología inmunomediada de la encefalitis de Rasmussen. Además, el único registro sanitario colombiano está cancelado y faltan datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de la levodopa desde DrugBank y análisis de un posible vínculo con la neuroinflamación.
- Revisión de la literatura preclínica y clínica sobre dopaminérgicos en encefalitis de Rasmussen o epilepsias inflamatorias.
- Obtener y analizar el prospecto en INVIMA (advertencias y contraindicaciones), dado que la epilepsia figura entre las contraindicaciones del grafo de conocimiento.
- Evaluar la disponibilidad comercial en Colombia, ya que no hay registros vigentes.
- Confirmar la compatibilidad de vías de administración con la nueva indicación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

