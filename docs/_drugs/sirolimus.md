---
layout: default
title: Sirolimus
parent: Evidencia Moderada (L3-L4)
nav_order: 588
evidence_level: L3
indication_count: 6
last_modified_at: 2026-11-04
monitor_inn: "sirolimus"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "uterine corpus perivascular epithelioid cell tumor", "benign PEComa", "lung PEComa", "vulva sarcoma"]
description: "Sirolimus: nueva indicación predicha, Liposarcoma (nivel de evidencia L3). Indicación original: SIROLIMUS"
---

# Sirolimus
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **6** 
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

Sirolimus es un inhibidor de la vía mTOR (mTORC1), utilizado originalmente como inmunosupresor en el contexto del trasplante.
El modelo TxGNN predice que podría ser efectivo para **liposarcoma (liposarcoma)**, con **1 ensayo clínico** de Fase 2 y **7 publicaciones** asociadas, aunque sin evidencia aleatorizada: el nivel de evidencia es **L3**.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | SIROLIMUS |
| Nueva Indicación Predicha | Liposarcoma |
| Puntaje de Predicción TxGNN | 0.9989 |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 1) |
| Número de Registros Sanitarios | al menos 1 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Sirolimus inhibe mTORC1, una vía de señalización (PI3K/AKT/mTOR) que se encuentra con frecuencia activada en sarcomas de tejidos blandos, incluido el liposarcoma. En los subtipos bien diferenciado y desdiferenciado también se observa co-amplificación de CDK4/MDM2. Los modelos en ratón sugieren que la inhibición de mTOR puede frenar el crecimiento tumoral.

Actualmente no se dispone de datos detallados del mecanismo de acción en las fuentes compiladas; la descripción anterior proviene del análisis mecanístico asociado a la predicción.

Existe un ensayo de Fase 2 de un solo brazo que combina sirolimus con ciclofosfamida en liposarcoma mixoide y condrosarcoma. No hay ensayos aleatorizados, y la literatura es sobre todo de revisión o de datos indirectos en pacientes trasplantados. Por ello el respaldo es real, pero limitado.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Fase 2 | Completado | 70 | Sirolimus + ciclofosfamida en liposarcoma mixoide y condrosarcoma metastásico o irresecable; brazo único, multicéntrico. Los resultados de eficacia no se pueden confirmar con los datos disponibles |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | ECA | J Am Soc Nephrol | En trasplante renal, sirolimus tras retirada temprana de ciclosporina redujo el riesgo de cáncer (evidencia indirecta) |
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Revisión | Cancers | Avances terapéuticos y moleculares en sarcomas de tejidos blandos |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Revisión | Curr Opin Oncol | Tratamientos dirigidos recientes en sarcomas avanzados |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Revisión | Bull Cancer | Tratamientos dirigidos en tumores raros del tejido conectivo y sarcomas |
| [26093731](https://pubmed.ncbi.nlm.nih.gov/26093731/) | 2015 | Revisión | Transplant Proc | Cribado de cáncer en receptores de trasplante renal con inmunosupresión prolongada |
| [42753013](https://pubmed.ncbi.nlm.nih.gov/42753013/) | 2026 | Cohorte | Fam Cancer | Espectro clínico y fenotípico del síndrome de hamartoma tumoral PTEN |
| [32711543](https://pubmed.ncbi.nlm.nih.gov/32711543/) | 2020 | Reporte de caso | Diagn Pathol | Anomalía vascular fibroadiposa y vía mTOR; sirolimus como inhibidor de mTOR |

## Información de Mercado en Colombia

Estado de mercado: comercializado. Hay al menos 1 registro sanitario vigente y la lista puede ser parcial.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19914809 | RAPAMUNE 1.0 MG GRAGEAS (PFIZER S.A.S.) | Tableta cubierta (gragea) | SIROLIMUS |

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: se identificaron 645 interacciones en total. Entre las de nivel mayor figuran anfotericina B (incluida la formulación de complejo lipídico), mesalazina, balsalazida y claritromicina. Entre las de nivel moderado figuran antidiabéticos (acarbosa, metformina, pioglitazona, alogliptina, canagliflozina, clorpropamida, albiglutida), corticoides (hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona), aprepitant y cimetidina.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un ensayo de Fase 2 completado de sirolimus combinado en liposarcoma mixoide, con un fundamento mecanístico plausible (vía mTOR). Sin embargo, es de un solo brazo, sin aleatorización, por lo que el nivel de evidencia es L3 y se requiere cautela.

**Para avanzar se necesita:**
- Resultados publicados de eficacia y seguridad del ensayo NCT02821507, por subtipo de liposarcoma
- Evidencia comparativa o aleatorizada en liposarcoma
- Datos de advertencias y contraindicaciones del prospecto
- Plan de monitoreo de seguridad (infecciones, función renal y hepática, glucosa y lípidos) y revisión de interacciones relevantes
- Datos del mecanismo de acción confirmados en fuentes de referencia

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

