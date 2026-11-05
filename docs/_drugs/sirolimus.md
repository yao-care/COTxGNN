---
layout: default
title: Sirolimus
parent: Solo Predicción del Modelo (L5)
nav_order: 588
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-06
monitor_inn: "sirolimus"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "uterine corpus perivascular epithelioid cell tumor", "benign PEComa", "lung PEComa", "vulva sarcoma"]
description: "Sirolimus: nueva indicación predicha, Liposarcoma (nivel de evidencia L5). Indicación original: SIROLIMUS"
---

# Sirolimus
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Sirolimus: Liposarcoma
{: .text-alpha }

## Resumen en Una Frase

Sirolimus es un inhibidor de la vía mTOR (mTORC1), utilizado como inmunosupresor.
El modelo TxGNN predice que podría ser efectivo para **liposarcoma (liposarcoma)**, pero por ahora solo hay **1 ensayo clínico** de Fase 2 sin resultados publicados y ninguna publicación que estudie directamente sirolimus en esta enfermedad, por lo que la evidencia es de nivel **L5**.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | SIROLIMUS |
| Nueva Indicación Predicha | Liposarcoma |
| Puntaje de Predicción TxGNN | 0.9989 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Sirolimus inhibe mTORC1, una vía que con frecuencia está activada en los sarcomas de tejidos blandos, incluido el liposarcoma (señalización PI3K/AKT/mTOR, con coamplificación de CDK4/MDM2 en los subtipos bien diferenciado y desdiferenciado). Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción del fármaco, por lo que este razonamiento se basa en el conocimiento general de la farmacología de sirolimus.

La lógica es que, si la vía mTOR impulsa el crecimiento del tumor, bloquearla podría frenarlo. Modelos en ratón han mostrado que la inhibición de mTOR puede prevenir el crecimiento tumoral en sarcomas. Sin embargo, esto es una hipótesis mecanística: no hay evidencia aleatorizada ni resultados publicados que confirmen eficacia en liposarcoma.

Además, la literatura disponible son sobre todo revisiones generales de sarcomas y datos indirectos de pacientes trasplantados, donde sirolimus se asocia con menor riesgo de cáncer. Esto no equivale a demostrar un efecto terapéutico en liposarcoma.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Fase 2 | Completado | 70 | Ensayo de un solo brazo, multicéntrico, de sirolimus más ciclofosfamida en liposarcoma mixoide y condrosarcoma metastásico o irresecable. No se dispone de resultados publicados ni registrados. |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Revisión | Cancers | Panorama de nuevas terapias en sarcomas de tejidos blandos; no estudia directamente sirolimus en liposarcoma |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Revisión | Current Opinion in Oncology | Fundamento y resultados de ensayos con agentes dirigidos en sarcomas avanzados |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Revisión | Bulletin du Cancer | Tratamientos dirigidos en tumores raros del tejido conectivo y sarcomas |
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | ECA | J Am Soc Nephrol | En trasplante renal, sirolimus tras retirada temprana de ciclosporina redujo el riesgo de cáncer; no es un estudio en liposarcoma |
| [26093731](https://pubmed.ncbi.nlm.nih.gov/26093731/) | 2015 | Revisión | Transplantation Proceedings | Tamizaje de cáncer en receptores de trasplante renal con inmunosupresión prolongada |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19914809 | RAPAMUNE 1.0 MG GRAGEAS (PFIZER S.A.S.) | Tableta cubierta (gragea) | SIROLIMUS |

La lista de registros puede ser parcial.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 645 interacciones. Entre las de nivel mayor figuran anfotericina B (y su complejo lipídico), mesalazina, balsalazida y claritromicina. Entre las de nivel moderado figuran antidiabéticos (acarbosa, metformina, pioglitazona, alogliptina, canagliflozina, dapagliflozina, clorpropamida, albiglutida), corticoides (hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona), aprepitant y cimetidina.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Solo existe un ensayo de Fase 2 de un solo brazo sin resultados publicados, y ningún estudio publicado evalúa sirolimus en liposarcoma; por ello la evidencia es de nivel L5 y se basa principalmente en la predicción del modelo y en la plausibilidad mecanística.

**Para avanzar se necesita:**
- Obtener los resultados del ensayo NCT02821507 (eficacia y seguridad por subtipo de liposarcoma)
- Datos detallados del mecanismo de acción y de la actividad de la vía mTOR en liposarcoma
- Información de seguridad del prospecto (advertencias y contraindicaciones)
- Evidencia aleatorizada o prospectiva específica en liposarcoma antes de reconsiderar la decisión

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

