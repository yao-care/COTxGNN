---
layout: default
title: Quetiapine
parent: Evidencia Moderada (L3-L4)
nav_order: 544
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Quetiapine: nueva indicación predicha, Tricotilomanía (nivel de evidencia L4). Indicación original: QUETIAPINA"
monitor_inn: "Quetiapine"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "congenital disorder of glycosylation with defective fucosylation", "hydranencephaly (disease)", "distal 17p13.3 microdeletion syndrome", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "myopia X-linked", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "trichotillomania", "syndromic myopia", "myopia 26, X-linked, female-limited"]
---

# Quetiapine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
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

# Quetiapina: De Indicación Original (QUETIAPINA, sin descripción detallada) a Tricotilomanía

## Resumen en Una Frase

Quetiapina es un antipsicótico atípico; en el único registro sanitario colombiano disponible, la indicación aprobada figura solo como "QUETIAPINA", sin mayor detalle. El modelo TxGNN predice que podría ser efectivo para **tricotilomanía**, con **0 ensayos clínicos** y **6 publicaciones** (reportes de caso y revisiones, según sus títulos) que respaldan de forma indirecta esta dirección.

Nota: la primera predicción por puntaje (enfermedad 1 de la lista) es "distrofia retiniana con o sin anomalías extraoculares" (99.57%), pero no tiene ninguna evidencia clínica ni bibliográfica. Este informe se centra en tricotilomanía (puesto 8, puntaje 99.38%), el único candidato con literatura disponible.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | QUETIAPINA (el registro no detalla la indicación; el uso conocido es esquizofrenia y trastorno bipolar) |
| Nueva Indicación Predicha | Tricotilomanía |
| Puntaje de Predicción TxGNN | 99.38% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold (con la tricotilomanía como pregunta de investigación) |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información farmacológica compilada, quetiapina actúa como antagonista de varios receptores: dopaminérgico D2, serotoninérgicos (5-HT1A, 5-HT1D, 5-HT1E, 5-HT1F, 5-HT2A), histaminérgico H1, y también interactúa con el transportador de noradrenalina (NET). Su uso clínico conocido incluye esquizofrenia, trastorno bipolar y depresión mayor.

La tricotilomanía es un trastorno de conducta repetitiva centrada en el cuerpo (arrancarse el cabello), dentro del espectro obsesivo-compulsivo. Los antipsicóticos atípicos con antagonismo 5-HT2A y D2 se emplean como tratamiento de aumento en condiciones de este espectro, lo que da un vínculo mecanístico plausible, aunque no demostrado.

Cabe señalar que la literatura también incluye un reporte en el que quetiapina agravó síntomas obsesivo-compulsivos en un paciente con TOC y tricotilomanía, lo que introduce una señal contradictoria. Por ello, la predicción debe tomarse como generadora de hipótesis y no como base para una recomendación terapéutica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Los tipos de estudio se infirieron únicamente a partir de los títulos; no se revisaron textos completos.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [12405081](https://pubmed.ncbi.nlm.nih.gov/12405081/) | 2002 | Revisión / reporte de caso | Psychiatry | Resumen de la tricotilomanía y reporte de una mujer de 33 años con respuesta clínica favorable a quetiapina |
| [19142421](https://pubmed.ncbi.nlm.nih.gov/19142421/) | 2008 | Reporte de caso / serie | Rev Bras Psiquiatr | "Quetiapina para el tratamiento de la tricotilomanía" (sin resumen disponible) |
| [11212595](https://pubmed.ncbi.nlm.nih.gov/11212595/) | 2001 | Reporte de caso y revisión | J Psychiatry Neurosci | Quetiapina exacerbó síntomas obsesivo-compulsivos en un paciente con TOC y tricotilomanía; revisión de síntomas obsesivo-compulsivos inducidos por antipsicóticos atípicos |
| [38797877](https://pubmed.ncbi.nlm.nih.gov/38797877/) | 2025 | Revisión / comentario | Int J Dermatol | Panorama del tratamiento farmacológico de la tricotilomanía y la falta de guías; no específico de quetiapina |
| [20833945](https://pubmed.ncbi.nlm.nih.gov/20833945/) | 2010 | Reporte de caso y revisión | Psychosomatics | Tratamiento del síndrome de Rapunzel recurrente y tricotilomanía; indirecto |
| [27840761](https://pubmed.ncbi.nlm.nih.gov/27840761/) | 2016 | Reporte de caso | Case Rep Psychiatry | Tricotilomanía como manifestación de demencia; indirecto, no específico de quetiapina |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20115222 (cancelado) | QUEPINA 100 MG TABLETAS RECUBIERTAS | Tableta recubierta | QUETIAPINA |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: el grafo de conocimiento TxGNN asocia quetiapina con contraindicación en las siguientes condiciones:
  - Cardiovasculares: hipertensión, hipotensión ortostática, síndrome de taquicardia postural ortostática, atrofia multisistémica, síndrome de QT largo (incluido el familiar), torsades de pointes e infarto de miocardio.
  - Neurológicas: epilepsia, enfermedad de los ganglios basales, distonía focal de la mano y blefaroespasmo.
  - Metabólicas y endocrinas: diabetes mellitus, cetoacidosis diabética, hiperglucemia, hipotiroidismo (incluidos el mixedema y el congénito), deficiencia de potasio, hiperlipidemia (incluida la familiar), hipertrigliceridemia, obesidad (incluida la monogénica).
  - Hematológicas: neutropenia y agranulocitosis.
  - Otras: enfermedad hepática, enfermedad de la vesícula biliar y carcinoma de mama femenino.
- **Perfil farmacológico**: la actividad sobre receptores H1, D2 y 5-HT2A es coherente con los riesgos conocidos de sedación y efectos metabólicos, que deben sopesarse frente a una condición no mortal como la tricotilomanía.

No se dispone de advertencias ni contraindicaciones del prospecto de INVIMA; consultar el prospecto para información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia disponible para tricotilomanía se limita a reportes de caso y revisiones (nivel L4), sin ensayos clínicos registrados, y con una señal contradictoria de exacerbación obsesivo-compulsiva. El único registro sanitario colombiano está cancelado y faltan datos de seguridad del prospecto, por lo que no es posible avanzar a un cribado de seguridad. Las demás predicciones de mayor puntaje (por ejemplo, distrofia retiniana, trastornos congénitos de la glicosilación, hidranencefalia) solo tienen predicción computacional (L5) y ningún vínculo mecanístico plausible.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), que es un vacío bloqueante.
- Completar los datos del mecanismo de acción desde DrugBank.
- Revisar los textos completos de los reportes de caso y las revisiones para confirmar su diseño real.
- Verificar la situación comercial actual de quetiapina en Colombia, ya que el único registro está cancelado.
- Evaluar, si se continúa, un estudio piloto o una revisión sistemática comparativa frente a tratamientos establecidos para tricotilomanía, con un plan de monitoreo metabólico, cardiovascular y hematológico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

