---
layout: default
title: Dutasteride
parent: Solo Predicción del Modelo (L5)
nav_order: 243
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-31
description: "Dutasteride: nueva indicación predicha, Hipertricosis universal congénita tipo Ambras (nivel de evidencia L5). Indicación original: Dutasterida"
monitor_inn: "DUTASTERIDE"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "migraine with brainstem aura", "familial isolated trichomegaly"]
---

# Dutasteride
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

## Dutasterida: De Dutasterida (indicación registrada sin detalle) a Hipertricosis Universal Congénita tipo Ambras
{: .text-alpha }

## Resumen en Una Frase

Dutasterida es un inhibidor de la 5-alfa-reductasa, registrado en Colombia como dutasterida sola y en combinación con tamsulosina; el texto de indicación del registro no detalla la enfermedad tratada.
El modelo TxGNN predice que podría ser efectivo para **hipertricosis universal congénita tipo Ambras**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dutasterida (el registro sanitario no detalla la enfermedad) |
| Nueva Indicación Predicha | Hipertricosis universal congénita tipo Ambras |
| Puntaje de Predicción TxGNN | 1.0000 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 3) |
| Número de Registros Sanitarios | al menos 3 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la dutasterida inhibe la 5-alfa-reductasa tipo 1 y tipo 2, con lo que reduce la dihidrotestosterona (DHT). Su eficacia está establecida en afecciones dependientes de andrógenos, como la hiperplasia prostática benigna y la alopecia androgenética.

El síndrome de Ambras es un trastorno congénito del crecimiento del cabello con base genética (reordenamientos cromosómicos que afectan la regulación de TRPS1). No se sabe que la hipertricosis de esta condición dependa de andrógenos, por lo que el vínculo mecanístico es **especulativo**.

La puntuación del modelo TxGNN (aprendizaje profundo) es muy alta, pero es solo una predicción, sin ensayos ni literatura que la respalden. Las demás predicciones del modelo (hipertricosis, anomalías del tallo piloso, hipotricosis, etc.) tienen el mismo problema: la puntuación proviene del modelo TxGNN y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas (fenotipos de pelo y ectodermo), no evidencia biológica ni una razón farmacológica. En la hipertricosis, además, la dirección del efecto es ambigua, porque los inhibidores de la 5-alfa-reductasa se usan sobre todo para reducir efectos androgénicos en el cabello.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal (Ambras).

Como referencia, la octava predicción (alopecia areata difusa) tiene una única publicación, que corresponde a otra enfermedad y aporta solo contexto indirecto:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [41714473](https://pubmed.ncbi.nlm.nih.gov/41714473/) | 2026 | Revisión | American Journal of Clinical Dermatology | Revisión narrativa sobre fisiopatología, evaluación clínica y tratamientos de la alopecia androgenética en mujeres; no evalúa la alopecia areata |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20128081 | DUTASVITAE® 0.5 MG CÁPSULAS BLANDAS | Cápsula blanda | DUTASTERIDA (vigente) |
| 20158830 | DUTASTERIDA 0.5MG CÁPSULA BLANDA | Cápsula blanda | DUTASTERIDA (vigente) |
| 20188809 | DUTAZ DUO® | Cápsula dura | TAMSULOSINA Y DUTASTERIDA (vigente) |

Los tres registros están cancelados; no hay registros vigentes.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: atrofia multisistémica, síndrome de taquicardia postural ortostática, hipotensión ortostática, enfermedad hepática, enfermedad de la vesícula biliar, priapismo y síndrome del iris flácido intraoperatorio. Varias de estas parecen asociarse sobre todo al componente tamsulosina de la combinación.
- **Interacciones farmacológicas**: se identificaron 100 interacciones. Las de nivel moderado son aprepitant, cimetidina, claritromicina, clotrimazol y miconazol. Otras (calcitriol, pantoprazol, glimepirida, mesalazina, doxiciclina, morfina, metformina, omeprazol, rosiglitazona, lansoprazol, lactulosa, triamcinolona, prednisona, simvastatina, hidrocortisona) tienen nivel no clasificado.
- **Embarazo**: según el análisis de la predicción, la dutasterida está contraindicada en el embarazo por su efecto sobre el desarrollo genital del feto masculino.

Consultar el prospecto para el resto de la información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos ni literatura, con un vínculo mecanístico débil y sin registros sanitarios vigentes en Colombia.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (consultar DrugBank) y análisis de si existe un vínculo real entre la DHT y la hipertricosis de Ambras
- Revisión bibliográfica dirigida y evidencia preclínica que respalde la hipótesis
- Prospecto de INVIMA con advertencias y contraindicaciones para completar el análisis de seguridad
- Evaluar la situación regulatoria: el medicamento está comercializado y cuenta con 3 licencias vigentes
- Priorizar otras predicciones con mayor plausibilidad, como la hipotricosis simple del cuero cabelludo, que tiene cercanía fenotípica con la alopecia androgenética
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

