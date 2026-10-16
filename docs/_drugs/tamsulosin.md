---
layout: default
title: Tamsulosin
parent: Solo Predicción del Modelo (L5)
nav_order: 605
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Tamsulosin: nueva indicación predicha, Hipertricosis universal congénita tipo Ambras (nivel de evidencia L5). Indicación original: Tamsulosina y dutasterida"
monitor_inn: "tamsulosin"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "migraine with brainstem aura"]
---

# Tamsulosin
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

# Tamsulosina: De Tamsulosina y Dutasterida (Hiperplasia Prostática) a Hipertricosis Universal Congénita tipo Ambras

## Resumen en Una Frase

Tamsulosina es un antagonista de los receptores adrenérgicos alfa-1, registrado en Colombia en combinación con dutasterida (producto TAMSULON® DUO), cuyo uso habitual es el tratamiento de los síntomas de la hiperplasia prostática benigna.
El modelo TxGNN predice que podría ser efectivo para **hipertricosis universal congénita tipo Ambras**, pero **no existen ensayos clínicos ni publicaciones** que respalden esta dirección: es una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Tamsulosina y dutasterida (según el registro INVIMA; el texto no detalla la enfermedad) |
| Nueva Indicación Predicha | Hipertricosis universal congénita tipo Ambras |
| Puntaje de Predicción TxGNN | 99.996% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según el conocimiento farmacológico general, la tamsulosina bloquea los receptores adrenérgicos alfa-1A/1D del músculo liso de la próstata y el cuello vesical, lo que mejora el flujo urinario. Es un tratamiento sintomático, sin efecto conocido sobre el folículo piloso.

Con los datos compilados, **no se identifica un vínculo mecanístico creíble**. El síndrome de Ambras es un trastorno genético raro (reordenamientos cromosómicos que afectan la regulación de TRPS1) y no hay evidencia de que el bloqueo alfa-1 influya en el crecimiento del cabello o del vello. El puntaje alto de TxGNN refleja probablemente la cercanía en el grafo de conocimiento entre nodos de fenotipos relacionados con el pelo, y no una base farmacológica.

Otras predicciones del modelo (hipertricosis, hipotricosis, alopecia areata difusa, alopecia, malformaciones congénitas y migraña con aura de tronco encefálico) tienen igualmente nivel L5 y ningún mecanismo plausible. Para la migraña, los efectos vasodilatadores y ortostáticos de la tamsulosina podrían incluso empeorar la cefalea o el mareo.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal (Ambras). Para la predicción de alopecia (posición 9) se recuperaron dos artículos, que **no constituyen evidencia de beneficio** y reflejan probablemente el contexto de coprescripción en hiperplasia prostática:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33175100](https://pubmed.ncbi.nlm.nih.gov/33175100/) | 2021 | Cohorte / farmacovigilancia | JAMA Dermatology | Suicidalidad y eventos adversos psicológicos con finasterida (alopecia e HPB); no evalúa tamsulosina |
| [32826647](https://pubmed.ncbi.nlm.nih.gov/32826647/) | 2021 | Estudio transversal / cohorte | Cornea | Cambios morfológicos de las glándulas de Meibomio en hombres con HPB; no evalúa tamsulosina para pérdida de cabello |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20115124 (cancelado) | TAMSULON® DUO | Cápsula dura | Tamsulosina y dutasterida |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** atrofia multisistémica, síndrome de taquicardia postural ortostática, hipotensión ortostática, enfermedad hepática, enfermedad de la vesícula biliar, priapismo y síndrome del iris flácido intraoperatorio.
- **Interacciones farmacológicas:** se identificaron 202 interacciones. Entre las principales:
  - **Mayor:** claritromicina.
  - **Moderadas:** bupropión, aprepitant, morfina, lorcaserina, canagliflozina, cimetidina, dapagliflozina, dronabinol, clotrimazol, dexfenfluramina, eliglustat, empagliflozina, ertugliflozina, fenfluramina, fenilbutirato de glicerol, miconazol, nabilona y opio.

Las advertencias y contraindicaciones del prospecto de INVIMA no están disponibles; consultar el prospecto para esa información.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el puntaje del modelo (nivel L5), sin ensayos, sin literatura de respaldo y sin mecanismo plausible. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (consulta a DrugBank) y un análisis que justifique algún vínculo con la biología del folículo piloso o con TRPS1.
- Advertencias y contraindicaciones del prospecto de INVIMA para completar el tamizaje de seguridad.
- Evidencia preclínica o de series de casos que respalde algún efecto sobre el crecimiento del pelo.
- Evaluar si, dado el estado cancelado del registro, existe una presentación vigente de tamsulosina en monoterapia en Colombia.
- Considerar priorizar otras predicciones o fármacos con mayor plausibilidad biológica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

