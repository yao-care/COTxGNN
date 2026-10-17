---
layout: default
title: Losartan
parent: Solo Predicción del Modelo (L5)
nav_order: 412
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
description: "Losartan: nueva indicación predicha, Enfermedad renal hipertensiva maligna (nivel de evidencia L5). Indicación original: Losartán"
monitor_inn: "LOSARTAN"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Prinzmetal angina", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "brain small vessel disease 1 with or without ocular anomalies"]
---

# Losartan
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

# Losartán: De Hipertensión (registro sanitario cancelado) a Enfermedad Renal Hipertensiva Maligna

## Resumen en Una Frase

Losartán es un antagonista del receptor AT1 de la angiotensina II, registrado en Colombia como losartán solo y combinado con diuréticos, y usado de forma establecida contra la hipertensión.
El modelo TxGNN predice que podría ser efectivo para **enfermedad renal hipertensiva maligna**, pero actualmente no hay ensayos clínicos y solo **1 publicación** (un estudio en modelo animal) respalda esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Losartán (el registro sanitario solo indica "Losartán"; no detalla la enfermedad) |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna |
| Puntaje de Predicción TxGNN | 99.73% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, losartán es un bloqueador del receptor AT1 de la angiotensina II. Su eficacia en hipertensión y su efecto protector sobre el riñón están bien establecidos, y mecanísticamente podría ser aplicable a la enfermedad renal hipertensiva maligna.

La única publicación disponible (PMID 30809002) describe, en un modelo de rata, que la angiotensina II y la vía NF-κB participan en la nefroesclerosis hipertensiva maligna. Esto es coherente con bloquear el receptor AT1, pero el respaldo es solo preclínico.

La novedad del reposicionamiento es baja, porque losartán ya se usa en hipertensión. Además, no se ha verificado que la indicación aprobada cubra este fenotipo grave.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [30809002](https://pubmed.ncbi.nlm.nih.gov/30809002/) | 2019 | Estudio en modelo animal | Hypertension Research | En ratas, la angiotensina II y el sistema NF-κB participan en la nefroesclerosis hipertensiva maligna; la uninefrectomía con sobrecarga de sal agravó la hipertensión y el daño renal |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20189581 (cancelado) | SANTANIL® tableta recubierta 50 mg | Tableta recubierta | Losartán |
| 20263318 (cancelado) | LOSAN HCT® tableta recubierta | Tableta recubierta | Losartán y diuréticos |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no según el prospecto)**: pancreatitis, enfermedad hepática, enfermedad de la vesícula biliar, lupus eritematoso sistémico (incluido el pediátrico), deficiencia de potasio, diabetes mellitus, cetoacidosis diabética, hiperuricemia, trastornos hipotensivos, hiperparatiroidismo, osteítis fibrosa, coma hepático, encefalopatía hepática, ictericia neonatal, anuria, gota, hipercalcemia, nefrocalcinosis, trastornos del metabolismo del fósforo, obstrucción de la arteria renal y función renal deteriorada.
- **Interacciones farmacológicas**: se encontraron 100 interacciones. Las de nivel **mayor** incluyen citrato de potasio y bicarbonato de potasio (riesgo de hiperpotasemia). Las de nivel **moderado** incluyen corticoides (hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida), inhibidores de SGLT2 (canagliflozina, dapagliflozina, empagliflozina), insulinas, ácido acetilsalicílico, morfina, bupropión, aprepitant y dronabinol.
- **Consideración específica**: para la hipertensión renovascular, la estenosis bilateral de la arteria renal es un riesgo reconocido de los ARA-II (lesión renal aguda), por lo que se requeriría monitoreo cuidadoso.

Para las advertencias del prospecto, consultar el prospecto del producto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto, pero solo la respalda un estudio en animales (L5), sin ensayos clínicos. Además, los dos registros sanitarios en Colombia están cancelados, y no hay datos de mecanismo ni de seguridad según el prospecto.

**Para avanzar se necesita:**
- Datos clínicos en humanos (ensayos o estudios observacionales) de losartán en enfermedad renal hipertensiva maligna
- Datos detallados del mecanismo de acción (MOA)
- Advertencias y contraindicaciones del prospecto de INVIMA
- Confirmar la situación regulatoria, dado que no hay registros vigentes en Colombia
- Plan de monitoreo de función renal y potasio, sobre todo si hay estenosis de arteria renal
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

