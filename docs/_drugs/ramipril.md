---
layout: default
title: Ramipril
parent: Solo Predicción del Modelo (L5)
nav_order: 546
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ramipril: nueva indicación predicha, Hipertensión pulmonar de mecanismo multifactorial no aclarado (nivel de evidencia L5). Indicación original: No especificada en el registro (el texto aprobado solo…"
monitor_inn: "RAMIPRIL"
predicted_indications: ["pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant hypertensive renal disease", "brain stem infarction", "Prinzmetal angina", "intracerebral hemorrhage", "ABri amyloidosis"]
---

# Ramipril
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

# Ramipril: De Indicación No Especificada a Hipertensión Pulmonar de Mecanismo Multifactorial No Aclarado

## Resumen en Una Frase

Ramipril es un inhibidor de la enzima convertidora de angiotensina (IECA) que cuenta con un registro sanitario en Colombia, actualmente cancelado; en ese registro la indicación aprobada figura solo como "RAMIPRIL", sin una enfermedad específica.
El modelo TxGNN predice que podría ser efectivo para **hipertensión pulmonar de mecanismo multifactorial no aclarado**.
Para esta predicción no hay ensayos clínicos ni publicaciones; la evidencia disponible se limita a **1 estudio preclínico en ratas** que se refiere a una forma cercana (hipertensión pulmonar por hipoxia).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto aprobado solo dice "RAMIPRIL") |
| Nueva Indicación Predicha | Hipertensión pulmonar de mecanismo multifactorial no aclarado |
| Puntaje de Predicción TxGNN | 99.93% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, ramipril pertenece a la clase de los IECA, que reducen la formación de angiotensina II, un potente vasoconstrictor. Su uso en hipertensión y protección cardiovascular está ampliamente establecido, aunque el registro colombiano no detalla la indicación aprobada.

El vínculo mecanístico planteado es que el bloqueo del sistema renina-angiotensina-aldosterona (SRAA) podría disminuir la vasoconstricción y el remodelado vascular impulsados por angiotensina II, también a nivel pulmonar. Esto es una hipótesis plausible, pero **los IECA no son una terapia establecida para la hipertensión arterial pulmonar**.

La predicción de TxGNN tiene un puntaje alto, pero no está respaldada por ensayos clínicos ni por literatura directa en esta indicación. Por ello debe considerarse una hipótesis para investigar, no una recomendación terapéutica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta indicación.

---

## Evidencia de Literatura

Para la indicación principal (rango 1) no se recuperó literatura. La única evidencia indirecta proviene de una indicación cercana (rango 2, hipertensión pulmonar por enfermedad pulmonar o hipoxia):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [9200213](https://pubmed.ncbi.nlm.nih.gov/9200213/) | 1996 | Preclínico (animal) | Physiological Research | En ratas expuestas 3 semanas a hipoxia crónica, ramipril (10 mg/kg/día) redujo la presión de perfusión basal y atenuó los efectos de la hipoxia sobre los vasos pulmonares. |

Los demás artículos recuperados para la indicación cercana tratan sobre contextos miocárdicos, renales u otros no relacionados, y no constituyen evidencia directa.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20160917 (cancelado) | IPCA RAMCOR 5 | Cápsula dura | RAMIPRIL |

Fabricante: IPCA Laboratories Limited. No hay registros vigentes.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** el grafo de conocimiento TxGNN (PrimeKG) asocia ramipril con las siguientes condiciones:
  - Enfermedad renal y obstrucción de la arteria renal
  - Enfermedad hepática y de la vesícula biliar
  - Lupus eritematoso sistémico (incluido el pediátrico)
  - Neutropenia y agranulocitosis
  - Angioedema hereditario (incluido el asociado a deficiencia de C1 inhibidor)
  - Trastornos hipotensivos
  - Enfermedades del tejido conectivo, esclerodermia (localizada y sistémica) y esclerosis sistémica
  - Enfermedades óseas y del cartílago
- **Interacciones Farmacológicas:** se identificaron 100 interacciones. Las de nivel **mayor** que aparecen entre las principales son:
  - Citrato de potasio
  - Bicarbonato de potasio

  Ambas implican riesgo de hiperpotasemia. Entre las de nivel **moderado** figuran corticoides (hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida), antidiabéticos (metformina, glimepirida, clorpropamida, alogliptina, canagliflozina, dapagliflozina, empagliflozina), ácido acetilsalicílico, morfina, bupropión, dronabinol, ácido picosulfúrico y polietilenglicol con electrolitos.
- **Consideración específica por indicación:** en la hipertensión renovascular, los IECA conllevan riesgo de lesión renal aguda en caso de estenosis bilateral de la arteria renal.

Consultar el prospecto para información de seguridad adicional, ya que no se dispone de advertencias del prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto en TxGNN, pero no cuenta con ensayos clínicos ni literatura directa en humanos, y el único dato de apoyo es un estudio en ratas sobre hipertensión pulmonar hipóxica. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Obtener el mecanismo de acción detallado desde DrugBank.
- Obtener del INVIMA el prospecto con advertencias y contraindicaciones, y aclarar la indicación aprobada del registro.
- Realizar una revisión sistemática de la literatura sobre IECA en hipertensión pulmonar en humanos.
- Evaluar estudios preclínicos adicionales y, solo si son favorables, considerar un ensayo exploratorio de fase 2.
- Aclarar la situación comercial de ramipril en Colombia, dado que el registro está cancelado.
- Definir un plan de seguridad que contemple función renal, potasio y presión arterial.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

