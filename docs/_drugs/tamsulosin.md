---
layout: default
title: Tamsulosin
parent: Solo Predicción del Modelo (L5)
nav_order: 605
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
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

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Tamsulosina: De Tamsulosina y Dutasterida (Hiperplasia Prostática) a Hipertricosis Universal Congénita tipo Ambras
{: .text-alpha }

## Resumen en Una Frase

Tamsulosina es un antagonista de los receptores adrenérgicos alfa-1, registrado en Colombia en combinación con dutasterida (producto TAMSULON® DUO), cuyo uso habitual es el tratamiento de los síntomas de la hiperplasia prostática benigna.
El modelo TxGNN predice que podría ser efectivo para **hipertricosis universal congénita tipo Ambras**, pero **no existen ensayos clínicos ni publicaciones** que respalden esta dirección: es una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Tamsulosina y dutasterida (según el registro INVIMA; el texto no detalla la enfermedad) |
| Nueva Indicación Predicha | Hipertricosis universal congénita tipo Ambras |
| Puntaje de Predicción TxGNN | 1.0000 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 14 de 17) |
| Número de Registros Sanitarios | 17 (vigentes: 14) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según el conocimiento farmacológico general, la tamsulosina bloquea los receptores adrenérgicos alfa-1A/1D del músculo liso de la próstata y el cuello vesical, lo que mejora el flujo urinario. Es un tratamiento sintomático, sin efecto conocido sobre el folículo piloso.

Con los datos compilados, **no se identifica un vínculo mecanístico creíble**. El síndrome de Ambras es un trastorno genético raro (reordenamientos cromosómicos que afectan la regulación de TRPS1) y no hay evidencia de que el bloqueo alfa-1 influya en el crecimiento del cabello o del vello. El puntaje alto proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas con el pelo, no evidencia biológica ni una base farmacológica.

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
| 20115124 | TAMSULON® DUO | Cápsula dura | Tamsulosina y dutasterida |

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
La predicción se basa únicamente en el puntaje del modelo (nivel L5), sin ensayos, sin literatura de respaldo y sin mecanismo plausible.

<!-- review:begin co-lic-20261105-tamsulosin-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción se basa únicamente en el puntaje del modelo (nivel L5), sin ensayos, sin literatura de respaldo y sin mecanismo plausible. Además, el único registro sanitario en Colombia está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 17 registros sanitarios (vigentes: 14); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-tamsulosin-1 -->

**Para avanzar se necesita:**
- Datos del mecanismo de acción (consulta a DrugBank) y un análisis que justifique algún vínculo con la biología del folículo piloso o con TRPS1.
- Advertencias y contraindicaciones del prospecto de INVIMA para completar el tamizaje de seguridad.
- Evidencia preclínica o de series de casos que respalde algún efecto sobre el crecimiento del pelo.
- Considerar priorizar otras predicciones o fármacos con mayor plausibilidad biológica.

<!-- review:begin co-lic-20261105-tamsulosin-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Evaluar si, dado el estado cancelado del registro, existe una presentación vigente de tamsulosina en monoterapia en Colombia. / Considerar priorizar otras predicciones o fármacos con mayor plausibilidad biológica." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 17 registros sanitarios (vigentes: 14); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-tamsulosin-2 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Además, el único registro sanitario en Colombia está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Evaluar si, dado el estado cancelado del registro, existe una presentación vigente de tamsulosina en monoterapia en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

