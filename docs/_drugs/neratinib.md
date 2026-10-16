---
layout: default
title: Neratinib
parent: Evidencia Alta (L1-L2)
nav_order: 466
evidence_level: L2
indication_count: 4
last_modified_at: 2026-10-14
description: "Neratinib: nueva indicación predicha, Cáncer de mama positivo para receptor de progesterona (nivel de evidencia L2). Indicación original: No especificada en el registro"
monitor_inn: "neratinib"
predicted_indications: ["normal breast-like subtype of breast carcinoma", "progesterone-receptor positive breast cancer", "progesterone-receptor negative breast cancer", "breast tumor luminal A or B"]
---

# Neratinib
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **4** 
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

# Neratinib: De Indicación Registrada (sin texto descriptivo) a Cáncer de Mama Positivo para Receptor de Progesterona

## Resumen en Una Frase

Neratinib es un inhibidor irreversible de tirosina quinasas de la familia HER (EGFR/HER1, HER2 y HER4), comercializado como NERLYNX® y utilizado en cáncer de mama HER2 positivo.
El modelo TxGNN predice que podría ser efectivo para **cáncer de mama positivo para receptor de progesterona**,
con **2 ensayos clínicos** (ambos de Fase 2: uno en reclutamiento y otro retirado sin participantes) y **12 publicaciones** que respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el registro sanitario solo indica "NERATINIB") |
| Nueva Indicación Predicha | Cáncer de mama positivo para receptor de progesterona |
| Puntaje de Predicción TxGNN | 99.68% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registro vigente) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Neratinib inhibe de forma irreversible las vías de señalización HER2/EGFR/HER4. Actualmente no se dispone de datos detallados del mecanismo de acción en la base de datos consultada, pero la literatura describe claramente su perfil como inhibidor pan-HER.

En el cáncer de mama HR+/HER2+, existe comunicación bidireccional entre las vías de HER2 y del receptor de estrógeno, lo que genera resistencia a la terapia endocrina. Por ello, combinar el bloqueo de HER2 con terapia endocrina tiene sentido mecanístico. El análisis de extensión del ensayo ExteNET (Fase 3, PMID 26874901) mostró el mayor beneficio en el subgrupo HR+.

Es importante señalar que esta predicción coincide en gran parte con la indicación ya establecida del fármaco (terapia adyuvante extendida en cáncer de mama temprano HER2+), por lo que no constituye un reposicionamiento genuinamente nuevo. Las señales más novedosas están en la enfermedad HR+/HER2-negativa con mutación de HER2 (SUMMIT, PMID 37597578) y en la enfermedad HER2-low combinada con inhibidores de CDK4/6 (solo datos preclínicos).

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04886531](https://clinicaltrials.gov/study/NCT04886531) | Fase 2 | En reclutamiento | 30 | Neratinib + inhibidor de aromatasa + trastuzumab durante 24 semanas antes de la cirugía en cáncer de mama ER+/HER2+; sin resultados aún |
| [NCT04901299](https://clinicaltrials.gov/study/NCT04901299) | Fase 2 | Retirado | 0 | Fulvestrant + neratinib en cáncer de mama metastásico HR+/HER2-negativo previamente tratado; no se inscribieron participantes |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [26874901](https://pubmed.ncbi.nlm.nih.gov/26874901/) | 2016 | ECA (Fase 3) | The Lancet Oncology | ExteNET: 12 meses de neratinib tras terapia adyuvante con trastuzumab en cáncer de mama temprano HER2+ |
| [27406346](https://pubmed.ncbi.nlm.nih.gov/27406346/) | 2016 | ECA (Fase 2 adaptativo) | N Engl J Med | I-SPY 2: aleatorización adaptativa de neratinib en cáncer de mama temprano de alto riesgo |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Guía | J Clin Oncol | Actualización de la guía ASCO sobre terapia sistémica en cáncer de mama avanzado HER2+ |
| [29784737](https://pubmed.ncbi.nlm.nih.gov/29784737/) | 2018 | Guía | J Natl Compr Canc Netw | Actualización de guías NCCN en cáncer de mama (inhibidores de CDK4/6 y terapia extendida) |
| [33726508](https://pubmed.ncbi.nlm.nih.gov/33726508/) | 2021 | Revisión | Future Oncol | Tendencias actuales en el tratamiento del cáncer de mama HR+/HER2+ |
| [32139271](https://pubmed.ncbi.nlm.nih.gov/32139271/) | 2020 | Revisión | Clin Breast Cancer | Mesa redonda de expertos sobre el cáncer de mama HER2+ y los inhibidores de tirosina quinasa |
| [39153126](https://pubmed.ncbi.nlm.nih.gov/39153126/) | 2024 | Cohorte | Breast Cancer Res Treat | Patrones de uso y tolerancia de neratinib adyuvante en HR+/HER2+; la diarrea provoca frecuentes suspensiones |
| [32782013](https://pubmed.ncbi.nlm.nih.gov/32782013/) | 2020 | Cohorte (análisis in silico) | Breast Cancer Res | Las mutaciones ERBB2 dirigibles se asocian con peor pronóstico en carcinoma lobulillar ER+ no amplificado |
| [41886605](https://pubmed.ncbi.nlm.nih.gov/41886605/) | 2026 | Preclínico | Cancer Research | BRD8/EP400 como módulo de cromatina que media la respuesta anti-HER2 en HR+/HER2+ |
| [35251981](https://pubmed.ncbi.nlm.nih.gov/35251981/) | 2022 | Reporte de caso | Front Oncol | Piotinib y vinorelbina metronómica en cáncer de mama HER2+ con enfermedad leptomeníngea |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20200349 (cancelado) | NERLYNX® 40MG TABLETAS RECUBIERTAS | Tableta recubierta | NERATINIB (sin texto de indicación detallado) |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasa pan-HER) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Función hepática (según las salvaguardas del análisis) y hemograma; vigilancia de diarrea |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Tolerabilidad**: La diarrea es el principal problema de tolerabilidad y exige profilaxis (PMID 39153126). Se recomienda monitorear la función hepática.
- **Interacciones Farmacológicas**: Se identificaron 181 interacciones en total. Entre las de nivel **Mayor** destacan:
  - Antiácidos y reductores de ácido gástrico: famotidina, ranitidina, cimetidina, y los inhibidores de la bomba de protones omeprazol, esomeprazol, lansoprazol, dexlansoprazol y rabeprazol
  - Claritromicina
  - Aprepitant
  - Dexametasona
  - Clotrimazol
  
  Entre las de nivel **Moderado**: loperamida, óxido de magnesio, hidróxido de aluminio, carbonato de calcio, empagliflozina y naldemedina. Naloxegol y fidaxomicina son de nivel **Menor**.
  
  Cabe destacar que loperamida (usada para la profilaxis de diarrea) y los reductores de ácido figuran entre las interacciones, por lo que requieren revisión cuidadosa.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe evidencia de Fase 3 (ExteNET) y Fase 2 que respalda neratinib en el contexto HER2+, con mayor beneficio en el subgrupo HR+. Sin embargo, esa evidencia corresponde en gran parte a la indicación ya establecida, y los dos ensayos de Fase 2 mapeados a esta indicación son indirectos: uno sin resultados y otro retirado sin participantes. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Confirmar el estado de HER2 o la presencia de mutación de HER2 antes de cualquier uso
- Plan de profilaxis de diarrea y monitoreo de función hepática
- Revisión de las interacciones farmacológicas mayores (especialmente reductores de ácido gástrico y claritromicina)
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones no disponibles) y definir la situación regulatoria, dado que el registro está cancelado
- Datos detallados del mecanismo de acción
- Resultados del ensayo NCT04886531 y evidencia específica en enfermedad PR-positiva
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

