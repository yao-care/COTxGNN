---
layout: default
title: Candesartan Cilexetil
parent: Solo Predicción del Modelo (L5)
nav_order: 131
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Candesartan Cilexetil: nueva indicación predicha, Hipertensión renovascular maligna (nivel de evidencia L5). Indicación original: Candesartán"
monitor_inn: "CANDESARTAN CILEXETIL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism"]
---

# Candesartan Cilexetil
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Candesartán cilexetilo: De Hipertensión (candesartán) a Hipertensión Renovascular Maligna

## Resumen en Una Frase

Candesartán cilexetilo es un antagonista del receptor de angiotensina II (tipo 1), registrado en Colombia bajo la indicación genérica "candesartán" (el texto de la licencia no detalla la enfermedad).
El modelo TxGNN predice que podría ser efectivo para **hipertensión renovascular maligna**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden directamente esta indicación, por lo que la predicción se basa solo en el modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Candesartán (el registro no especifica la enfermedad) |
| Nueva Indicación Predicha | Hipertensión renovascular maligna |
| Puntaje de Predicción TxGNN | 99.68% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, candesartán cilexetilo es un profármaco que se convierte en candesartán, un bloqueador del receptor de angiotensina II tipo 1 (ARA-II). Mecanísticamente, podría ser aplicable a la hipertensión renovascular.

La hipertensión renovascular depende en gran medida de la activación del sistema renina-angiotensina, por lo que bloquear el receptor AT1 es biológicamente plausible. Además, el fármaco ya se usa en hipertensión en general, por lo que esta predicción se entiende mejor como un subtipo de una indicación existente que como un reposicionamiento genuino.

Hay una advertencia importante: en la forma maligna, el bloqueo del sistema renina-angiotensina conlleva riesgo de deterioro agudo de la función renal, especialmente con estenosis bilateral de arteria renal. El puntaje alto (0.997) es solo una predicción computacional.

**Otras indicaciones predichas (todas de nivel L5, decisión Hold):**

| Indicación predicha | Puntaje TxGNN | Comentario |
|------|------|------|
| Enfermedad renal hipertensiva maligna | 99.68% | Plausible por el papel de la angiotensina II en el daño vascular y glomerular; sin ensayos ni literatura. Debe evaluarse el riesgo de hiperpotasemia y lesión renal aguda. |
| Hipertensión pulmonar por enfermedad pulmonar y/o hipoxia | 99.67% | Plausible mecanísticamente, pero los vasodilatadores sistémicos pueden empeorar la relación ventilación-perfusión en hipoxia. |
| Hipertensión pulmonar de mecanismo multifactorial poco claro | 99.67% | Vínculo mecanístico débil por la categoría heterogénea. |
| Síndrome de Braddock | 99.56% | Enfermedad muy rara; sin conexión mecanística evidente. El puntaje probablemente refleja cercanía en la red de conocimiento. |

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal (hipertensión renovascular maligna).

Para la tercera indicación predicha (hipertensión pulmonar por enfermedad pulmonar/hipoxia) se recuperaron dos trabajos, ambos preclínicos e indirectos:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31396238](https://pubmed.ncbi.nlm.nih.gov/31396238/) | 2019 | Preclínico (modelo animal) | Frontiers in Immunology | Candesartán cilexetilo, por su efecto antiinflamatorio, mejoró los resultados neurológicos en un modelo murino de hipoxia neonatal. No aborda hipertensión pulmonar. |
| [21423692](https://pubmed.ncbi.nlm.nih.gov/21423692/) | 2011 | Preclínico (otra intervención) | Evid Based Complement Alternat Med | Estudio de una fórmula herbal (Hachimijiogan) en riñón remanente de rata, comparada con un ARA-II; sin vínculo directo con hipertensión pulmonar. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19995395 (cancelado) | CANDEPREX® 16 MG TABLETAS | Tableta | Candesartán |

---

## Consideraciones de Seguridad

- **Contraindicaciones o condiciones de precaución según el grafo de conocimiento (no provienen del prospecto):** pancreatitis, enfermedad hepática, enfermedad de la vesícula biliar, lupus eritematoso sistémico (incluido el pediátrico), deficiencia de potasio, diabetes mellitus, cetoacidosis diabética, hiperuricemia, trastornos hipotensivos, hiperparatiroidismo, osteítis fibrosa, coma hepático, encefalopatía hepática, ictericia neonatal, anuria, gota, hipercalcemia, nefrocalcinosis, trastornos del metabolismo del fósforo, obstrucción de la arteria renal y deterioro de la función renal.
- Para las indicaciones renales y vasculares predichas, es especialmente relevante la obstrucción de la arteria renal y el deterioro de la función renal, junto con el riesgo de hiperpotasemia y lesión renal aguda.

Para advertencias, contraindicaciones oficiales e interacciones farmacológicas, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Toda la predicción se apoya únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura directa. Además, el único registro sanitario en Colombia está cancelado y existe un riesgo renal relevante en la forma maligna de la enfermedad.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto del INVIMA (advertencias y contraindicaciones oficiales), requisito previo para cualquier evaluación de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Aclarar la indicación aprobada original, ya que el registro solo dice "candesartán".
- Revisar la literatura clínica sobre ARA-II en hipertensión renovascular maligna y su seguridad renal (estenosis bilateral, hiperpotasemia, lesión renal aguda).
- Confirmar la situación comercial actual, dado que el registro está cancelado y no hay presentaciones vigentes.
- Evaluar si la indicación constituye reposicionamiento real o un subtipo de la hipertensión ya cubierta.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

