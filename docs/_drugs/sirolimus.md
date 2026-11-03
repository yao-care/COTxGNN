---
layout: default
title: Sirolimus
parent: Evidencia Alta (L1-L2)
nav_order: 588
evidence_level: L2
indication_count: 6
last_modified_at: 2026-11-03
monitor_inn: "sirolimus"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "uterine corpus perivascular epithelioid cell tumor", "benign PEComa", "lung PEComa", "vulva sarcoma"]
description: "Sirolimus: nueva indicación predicha, Liposarcoma (nivel de evidencia L2). Indicación original: SIROLIMUS"
---

# Sirolimus
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **6** 
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

Sirolimus es un inhibidor de la vía mTOR (mTORC1) que se comercializa en Colombia en forma de tableta cubierta (gragea).
El modelo TxGNN predice que podría ser efectivo para **liposarcoma (liposarcoma)**,
con **1 ensayo clínico** y **7 publicaciones** relacionadas con esta dirección, aunque la mayoría son revisiones o datos indirectos.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | SIROLIMUS |
| Nueva Indicación Predicha | Liposarcoma |
| Puntaje de Predicción TxGNN | 0.9989 |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 1) |
| Número de Registros Sanitarios | al menos 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Sirolimus inhibe mTORC1, una vía de señalización que con frecuencia está activada en los sarcomas de tejidos blandos, incluido el liposarcoma (señalización PI3K/AKT/mTOR, con coamplificación de CDK4/MDM2 en los subtipos bien diferenciado y desdiferenciado). Los datos de mecanismo de acción detallados de la base de datos farmacológica no están disponibles, por lo que este razonamiento se apoya en el conocimiento general de la clase.

Los modelos en ratón sugieren que la inhibición de mTOR puede frenar el crecimiento tumoral en sarcomas, lo que da una base biológica para evaluar el fármaco en esta enfermedad.

Existe un ensayo de Fase 2 de un solo brazo con una combinación que incluye sirolimus, pero no hay evidencia aleatorizada. La literatura disponible consiste sobre todo en revisiones y datos indirectos de pacientes trasplantados, por lo que la predicción debe considerarse una hipótesis de investigación.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Fase 2 | Completado | 70 | Sirolimus combinado con ciclofosfamida en liposarcoma mixoide y condrosarcoma metastásico o irresecable; estudio de un solo brazo, multicéntrico. Los resultados de eficacia no se pueden confirmar con los datos disponibles. |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | ECA | J Am Soc Nephrol | En trasplante renal, sirolimus tras retirada temprana de ciclosporina redujo el riesgo de cáncer (dato indirecto). |
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Revisión | Cancers | Avances en terapias novedosas y caracterización molecular de sarcomas de tejidos blandos. |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Revisión | Curr Opin Oncol | Tratamientos dirigidos recientes para sarcomas avanzados. |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Revisión | Bull Cancer | Tratamientos dirigidos en tumores raros del tejido conectivo y sarcomas. |
| [26093731](https://pubmed.ncbi.nlm.nih.gov/26093731/) | 2015 | Revisión | Transplant Proc | Tamizaje de cáncer en receptores de trasplante renal con inmunosupresión prolongada. |
| [42753013](https://pubmed.ncbi.nlm.nih.gov/42753013/) | 2026 | Cohorte | Fam Cancer | Espectro clínico del síndrome de hamartoma PTEN (dato indirecto). |
| [32711543](https://pubmed.ncbi.nlm.nih.gov/32711543/) | 2020 | Reporte de caso | Diagn Pathol | Tres casos de anomalía vascular fibroadiposa con énfasis en la vía mTOR (dato indirecto). |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19914809 | RAPAMUNE 1.0 MG GRAGEAS (PFIZER S.A.S.) | Tableta cubierta (gragea) | SIROLIMUS |

La lista de registros puede ser parcial.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 645 interacciones en total. Entre las de nivel mayor figuran anfotericina B (incluida la forma de complejo lipídico), mesalazina, balsalazida y claritromicina. Entre las de nivel moderado figuran antidiabéticos (acarbosa, metformina, pioglitazona, alogliptina, canagliflozina, clorpropamida, albiglutida), corticoides (hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona), aprepitant y cimetidina.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Hay un ensayo de Fase 2 de un solo brazo con una combinación, pero sin resultados de eficacia confirmados, sin evidencia aleatorizada y con literatura mayormente indirecta. Por ello la predicción se mantiene como pregunta de investigación.

**Para avanzar se necesita:**
- Resultados publicados del ensayo NCT02821507 y confirmación de la población específica de liposarcoma
- Evidencia comparativa o aleatorizada en liposarcoma
- Datos detallados del mecanismo de acción
- Información de advertencias y contraindicaciones del prospecto del INVIMA
- Plan de monitoreo de seguridad, dadas las numerosas interacciones farmacológicas

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

