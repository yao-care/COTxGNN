---
layout: default
title: Hydroxyurea
parent: Solo Predicción del Modelo (L5)
nav_order: 331
evidence_level: L5
indication_count: 6
monitor_inn: "hydroxyurea"
predicted_indications: ["female breast carcinoma", "sickle cell-hemoglobin E disease syndrome", "cervical adenosarcoma", "colon mucinous adenocarcinoma", "rectum mucinous adenocarcinoma", "gallbladder mucinous adenocarcinoma"]
last_modified_at: 2026-11-03
description: "Hydroxyurea: nueva indicación predicha, Carcinoma de mama femenino (female breast carcinoma) (nivel de evidencia L5). Indicación original: HIDROXICARBAMIDA"
---

# Hydroxyurea
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

## Hydroxyurea: Carcinoma de mama femenino (female breast carcinoma)
{: .text-alpha }

## Resumen en Una Frase

Hidroxiurea es un antineoplásico que inhibe la enzima ribonucleótido reductasa y que cuenta con registros sanitarios vigentes en Colombia.
El modelo TxGNN predice que podría ser efectivo para **carcinoma de mama femenino (female breast carcinoma)**, pero no hay ensayos clínicos registrados y la literatura disponible es principalmente preclínica, por lo que la evidencia es muy limitada.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | HIDROXICARBAMIDA |
| Nueva Indicación Predicha | Carcinoma de mama femenino (female breast carcinoma) |
| Puntaje de Predicción TxGNN | 0.9997 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 2 de 2) |
| Número de Registros Sanitarios | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción detallado. Por conocimiento general, la hidroxiurea inhibe la ribonucleótido reductasa, lo que reduce las reservas de desoxirribonucleótidos (dNTP) y genera estrés de replicación del ADN.

Este mecanismo es biológicamente plausible en tumores que dependen de la tolerancia al estrés de replicación, por ejemplo mediante la vía ATR/RPA2. Varios estudios preclínicos describen que las células de cáncer de mama pueden ser sensibilizadas a la hidroxiurea, y que conjugados lipídicos de hidroxiurea se han diseñado in silico para mejorar su captación.

Sin embargo, no existen datos de eficacia clínica específicos en cáncer de mama. El puntaje alto del modelo es solo una predicción y no constituye evidencia clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Ninguna publicación es un ensayo clínico que estudie directamente la hidroxiurea en cáncer de mama; por ello el nivel de evidencia se limita a L5.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38211596](https://pubmed.ncbi.nlm.nih.gov/38211596/) | 2024 | In silico / preclínico | Drug Research | Diseño in silico de conjugados lípido-hidroxiurea dirigidos a la vía PI3K/AKT/mTOR en cáncer de mama |
| [28837865](https://pubmed.ncbi.nlm.nih.gov/28837865/) | 2017 | Preclínico | DNA Repair | El ácido valproico sensibiliza células de cáncer de mama a la hidroxiurea al inhibir la reparación del ADN mediada por RPA2 |
| [32795962](https://pubmed.ncbi.nlm.nih.gov/32795962/) | 2020 | Preclínico | DNA Repair | Un análogo del ácido valproico podría sensibilizar el carcinoma de mama a la hidroxiurea influyendo en la reparación del ADN |
| [1957839](https://pubmed.ncbi.nlm.nih.gov/1957839/) | 1991 | Fase 1 | Am J Clin Oncol | Esquema con 5-FU, leucovorina y luego hidroxiurea en 20 pacientes con carcinomas avanzados (colorrectal, páncreas, estómago y mama) |
| [1733549](https://pubmed.ncbi.nlm.nih.gov/1733549/) | 1992 | Fase 1/2 | Cancer Chemother Pharmacol | Combinación de 5-FU, leucovorina, hidroxiurea y cisplatino con radioterapia en tumores sólidos avanzados |
| [30159181](https://pubmed.ncbi.nlm.nih.gov/30159181/) | 2018 | Reporte de caso | Case Rep Hematol | Paciente con cáncer de mama y trombocitemia esencial: desafíos terapéuticos |
| [27504932](https://pubmed.ncbi.nlm.nih.gov/27504932/) | 2017 | Preclínico | J Cell Physiol | Quimiorresistencia de células de pulmón y mama bajo privación prolongada de suero |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 42034 | HYDREA CAPSULAS 500 MG | Cápsula dura | HIDROXICARBAMIDA |
| 20257687 | HIDROXIUREA 500 MG CAPSULA DURA | Cápsula dura | HIDROXICARBAMIDA |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (antimetabolito, inhibidor de la ribonucleótido reductasa) |
| Riesgo de Mielosupresión | Alto (leucopenia, trombocitopenia y anemia son efectos esperados) |
| Clasificación de Emetogenicidad | Baja |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal |
| Protección en Manejo | Seguir las regulaciones de manejo de fármacos citotóxicos |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se registran 309 interacciones. Entre las consultadas figuran levofloxacino (menor) y otros fármacos como doxiciclina, anfotericina B, hidrocortisona, ácido acetilsalicílico, metformina, prednisona y simvastatina, cuyo nivel de gravedad no está clasificado. Se recomienda revisar cada combinación.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos registrados ni estudios clínicos específicos en cáncer de mama; la literatura es mayormente preclínica o de combinaciones antiguas en tumores sólidos mixtos. El puntaje alto de TxGNN no sustituye la evidencia clínica.

**Para avanzar se necesita:**
- Evidencia clínica directa de hidroxiurea en carcinoma de mama (ensayos de fase 2 o superior)
- Datos detallados del mecanismo de acción
- Advertencias y contraindicaciones del prospecto
- Evaluación de la relación riesgo-beneficio frente a los tratamientos estándar de cáncer de mama, dada la mielosupresión esperada

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

