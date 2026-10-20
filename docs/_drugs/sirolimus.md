---
layout: default
title: Sirolimus
parent: Solo Predicción del Modelo (L5)
nav_order: 588
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Sirolimus: nueva indicación predicha, Liposarcoma (nivel de evidencia L5). Indicación original: No especificada en el registro (el texto aprobado solo indica \"SIROLI…"
monitor_inn: "sirolimus"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "uterine corpus perivascular epithelioid cell tumor", "benign PEComa", "lymphangiomyoma", "lung PEComa", "vulva sarcoma"]
---

# Sirolimus
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

# Sirolimus: De Sirolimus (indicación original no detallada) a Liposarcoma

## Resumen en Una Frase

Sirolimus (comercializado en Colombia como RAPAMUNE 1.0 MG GRAGEAS) es un inhibidor de mTOR cuyo registro sanitario en INVIMA solo consigna el nombre del principio activo como indicación, sin detallar el uso aprobado.
El modelo TxGNN predice que podría ser efectivo para **liposarcoma**, con **1 ensayo clínico** (Fase 2, de un solo brazo) y **7 publicaciones** que respaldan esta dirección, la mayoría revisiones e indicios indirectos.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto aprobado solo indica "SIROLIMUS") |
| Nueva Indicación Predicha | Liposarcoma |
| Puntaje de Predicción TxGNN | 99.89% |
| Nivel de Evidencia | L2 (1 ensayo de Fase 2 completado, sin aleatorización) |
| Estado de Mercado en Colombia | Solo cancelado (sin registros vigentes) |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, sirolimus inhibe mTORC1, una vía de señalización (PI3K/AKT/mTOR) que se activa con frecuencia en los sarcomas de tejidos blandos, incluido el liposarcoma.

En el liposarcoma, esta vía coexiste con la coamplificación de CDK4/MDM2 en los subtipos bien diferenciado y desdiferenciado. Los modelos en ratón han mostrado que la inhibición de mTOR puede frenar el crecimiento tumoral, lo que da una base biológica a la predicción.

Sin embargo, la relación entre la indicación original (sin detallar) y el liposarcoma no está caracterizada en los datos, y no existe evidencia aleatorizada. La plausibilidad es mecanística, no clínicamente demostrada.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Fase 2 | Completado | 70 | Ensayo de un solo brazo, multicéntrico, de sirolimus combinado con ciclofosfamida en liposarcoma mixoide y condrosarcoma metastásicos o irresecables. No se dispone de los resultados de eficacia ni se puede confirmar qué proporción de pacientes tenía liposarcoma. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | ECA | J Am Soc Nephrol | En trasplante renal, retirar ciclosporina y mantener sirolimus redujo el riesgo de cáncer (evidencia indirecta, no específica de liposarcoma) |
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Revisión | Cancers | Panorama de terapias novedosas en sarcomas de tejidos blandos |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Revisión | Curr Opin Oncol | Fundamento y resultados de ensayos con agentes dirigidos en sarcomas avanzados |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Revisión | Bull Cancer | Tratamientos dirigidos de tumores raros del tejido conectivo y sarcomas |
| [26093731](https://pubmed.ncbi.nlm.nih.gov/26093731/) | 2015 | Revisión | Transplant Proc | Tamizaje de cáncer en receptores de trasplante renal con inmunosupresión prolongada |
| [42753013](https://pubmed.ncbi.nlm.nih.gov/42753013/) | 2026 | Cohorte | Fam Cancer | Espectro clínico del síndrome de tumor hamartomatoso PTEN (relación indirecta con la vía mTOR) |
| [32711543](https://pubmed.ncbi.nlm.nih.gov/32711543/) | 2020 | Reporte de caso | Diagn Pathol | Tres casos de anomalía vascular fibroadiposa con énfasis en la vía mTOR |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19914809 (cancelado) | RAPAMUNE 1.0 MG GRAGEAS (PFIZER S.A.S.) | Tableta cubierta (gragea) | SIROLIMUS |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de mTOR); no es un citotóxico convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar el prospecto; en general se recomienda hemograma, función hepática y renal, y perfil lipídico y glucémico |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no proviene del prospecto)**: el grafo de conocimiento asocia sirolimus con enfermedades como hipertensión, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, hiperglucemia, diabetes mellitus, cetoacidosis diabética, hipertrigliceridemia e hiperlipidemia, enfermedad cerebrovascular y accidente cerebrovascular, hiperbilirrubinemia (incluido el síndrome de Gilbert), enfermedad pulmonar intersticial, infecciones (neumocistosis, citomegalovirus), cáncer (incluidos los tumores cerebrales), derrame pericárdico y leucoencefalopatía multifocal progresiva. Estas relaciones deben verificarse contra el texto oficial del prospecto.
- **Interacciones Farmacológicas**: se registraron 645 interacciones. Entre las de nivel **mayor** figuran anfotericina B (y su complejo lipídico), mesalazina, balsalazida y claritromicina. Entre las de nivel **moderado** figuran antidiabéticos (acarbosa, metformina, pioglitazona, alogliptina, albiglutida, canagliflozina, clorpropamida, dapagliflozina), corticoides (hidrocortisona, triamcinolona, dexametasona, betametasona, budesonida), aprepitant y cimetidina.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Solo existe un ensayo de Fase 2 de un solo brazo con una combinación (sirolimus + ciclofosfamida), sin resultados disponibles ni evidencia aleatorizada, y la literatura es mayormente de revisión o indirecta. Además, el único registro sanitario en Colombia está cancelado y faltan datos de seguridad del prospecto, por lo que no es posible avanzar con garantías.

**Para avanzar se necesita:**
- Obtener los resultados publicados de NCT02821507 y confirmar la proporción de pacientes con liposarcoma
- Descargar y analizar el prospecto en INVIMA para completar advertencias y contraindicaciones
- Obtener datos del mecanismo de acción desde DrugBank
- Aclarar la disponibilidad regulatoria en Colombia, dado que el registro está cancelado
- Buscar evidencia aleatorizada o ensayos específicos por subtipo de liposarcoma

---

### Nota sobre otras indicaciones predichas

Los datos compilados incluyen otras predicciones con mayor respaldo que liposarcoma. La más destacada es la **linfangioleiomiomatosis (LAM)**, con nivel de evidencia L1: cuenta con el ensayo aleatorizado de Fase 3 MILES ([NCT00414648](https://clinicaltrials.gov/study/NCT00414648), 89 pacientes, completado) y un ensayo de Fase 3 en enfermedad temprana ([NCT03150914](https://clinicaltrials.gov/study/NCT03150914), en curso). La recomendación para esa indicación es *Proceed with Guardrails*. Se sugiere evaluarla en un informe independiente, con atención a la monitorización de eventos adversos por inmunosupresión, las interacciones farmacológicas y la necesidad de tratamiento prolongado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

