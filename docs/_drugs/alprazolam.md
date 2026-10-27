---
layout: default
title: Alprazolam
parent: Evidencia Moderada (L3-L4)
nav_order: 40
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-14
description: "Alprazolam: nueva indicación predicha, Insomnio (nivel de evidencia L4). Indicación original: No detallada"
monitor_inn: "ALPRAZOLAM"
predicted_indications: ["insomnia (disease)", "benign paroxysmal torticollis of infancy", "agoraphobia"]
---

# Alprazolam
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **3** 
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

## Alprazolam: De Indicación No Detallada en el Registro INVIMA a Insomnio
{: .text-alpha }

## Resumen en Una Frase

Alprazolam es una benzodiacepina cuyos registros sanitarios en Colombia solo consignan el nombre del principio activo, sin detallar la indicación aprobada. El modelo TxGNN predice que podría ser efectivo para **insomnio**, pero hoy no hay **ningún ensayo clínico** registrado y la literatura recuperada (**18 publicaciones**) es en su mayoría indirecta.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No detallada (el registro INVIMA solo indica "Alprazolam") |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99.81% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 4 (todos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada para este informe. Según el conocimiento farmacológico general, el alprazolam es una benzodiacepina que potencia la señalización inhibitoria del receptor GABA-A, lo que produce efectos ansiolíticos, sedantes e hipnóticos.

Ese efecto sedante-hipnótico hace plausible su uso en el insomnio, que es un efecto de clase de las benzodiacepinas. Además, el insomnio suele acompañar a los trastornos de ansiedad, el ámbito donde el alprazolam es más conocido.

Sin embargo, la literatura recuperada es mayormente indirecta. Incluye revisiones sobre trastorno de pánico, farmacocinética, patrones de uso de benzodiacepinas y estudios de comorbilidad o desprescripción (por ejemplo, con zolpidem). No se recuperó ningún ensayo controlado de alprazolam específicamente para insomnio. A ello se suman los riesgos conocidos de dependencia, tolerancia, caídas y sedación diurna, sobre todo en adultos mayores y en personas con cirrosis.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39183410](https://pubmed.ncbi.nlm.nih.gov/39183410/) | 2024 | Estudio observacional retrospectivo | Medicine | En 116 pacientes con cardiopatía coronaria e insomnio, el grupo control recibió alprazolam y el grupo experimental, moxibustión y acupuntura auricular. Se evaluó función cardíaca y neurotransmisores. |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | Metaanálisis | Acta Pharmaceutica | Evalúa tranquilizantes en adultos mayores con enfermedades crónicas no transmisibles (dosis, resultados y efectos adversos). |
| [7484706](https://pubmed.ncbi.nlm.nih.gov/7484706/) | 1995 | Revisión | American Family Physician | Revisión del trastorno de pánico, con alta morbilidad y mayor riesgo de suicidio. Evidencia indirecta para insomnio. |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Revisión | Expert Opin Drug Metab Toxicol | Farmacocinética de los ansiolíticos. |
| [37984023](https://pubmed.ncbi.nlm.nih.gov/37984023/) | 2024 | Modelado / análisis económico | Value in Health Regional Issues | Tendencias y carga económica del uso de benzodiacepinas. El uso prolongado se asocia con pérdida de memoria, dependencia, caídas y accidentes de tráfico. |
| [15341891](https://pubmed.ncbi.nlm.nih.gov/15341891/) | 2004 | Estudio de prescripción | Sleep Medicine | Patrones de prescripción de hipnóticos en una población de atención gestionada. |
| [35493764](https://pubmed.ncbi.nlm.nih.gov/35493764/) | 2022 | Cohorte | JHEP Reports | La desprescripción de zolpidem (no alprazolam) reduce caídas y fracturas en cirrosis. |
| [37801512](https://pubmed.ncbi.nlm.nih.gov/37801512/) | 2023 | Preclínico (ratones) | Aging | La administración repetida de alprazolam causa disfunción mitocondrial y afecta la consolidación de la memoria dependiente del hipocampo. |
| [38363887](https://pubmed.ncbi.nlm.nih.gov/38363887/) | 2024 | Transversal | Medicine | Insomnio en sobrevivientes de COVID-19. No evalúa alprazolam directamente. |
| [25532388](https://pubmed.ncbi.nlm.nih.gov/25532388/) | 2014 | Análisis de datos del mundo real | Zhongguo Zhong Yao Za Zhi | Enfermedades concurrentes y uso de medicamentos en pacientes con insomnio. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 41269 | XANAX ® 1.0 MG TABLETAS | Tableta | Alprazolam |
| 227600 | ALPRAZOLAM 0.5 MG TABLETAS | Tableta | Alprazolam |
| 13874 | XANAX 0.25 MG TABLETAS | Tableta | Alprazolam |
| 19928029 | XANAX ® 0.5 MG TABLETAS | Tableta | Alprazolam |

Los cuatro registros figuran como cancelados, por lo que actualmente no hay registros vigentes.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad de TxGNN/PrimeKG, no texto del prospecto): trastorno de ansiedad, trastorno neurótico, trastorno distímico, enfermedad renal, piouréter, enfermedad hepática, enfermedad de la vesícula biliar, glaucoma de ángulo abierto, glaucoma de ángulo cerrado, trastornos de obesidad, obesidad monogénica, síndrome de apnea obstructiva del sueño, síndrome de apnea del sueño, síndrome de hipoventilación central congénita, síndrome de Haddad, trastornos relacionados con sustancias y abuso/dependencia de sustancias.
- **Interacciones farmacológicas**: se identificaron 100 interacciones. Entre las 20 listadas:
  - **Mayores**: morfina y morfina liposomal (riesgo de depresión del sistema nervioso central y respiratoria).
  - **Moderadas**: aprepitant, bupropión, cimetidina, claritromicina, clotrimazol, dronabinol, eliglustat, fenilbutirato de glicerol, metoclopramida y miconazol.
  - **Menores**: antiácidos (hidróxido de aluminio, carbonato de calcio, magaldrato, sales de magnesio) y corticoides (betametasona, dexametasona).
- **Riesgos de la literatura**: dependencia, tolerancia, deterioro de la memoria, caídas y sedación diurna. Preocupan especialmente los adultos mayores y los pacientes con cirrosis.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El puntaje del modelo es muy alto, pero no hay ensayos clínicos y la evidencia disponible para insomnio es solo indirecta. Además, todos los registros sanitarios en Colombia están cancelados y existen riesgos relevantes de dependencia y sedación.

**Para avanzar se necesita:**
- Evidencia directa: ensayos controlados de alprazolam frente a placebo u otros hipnóticos en insomnio.
- Datos del mecanismo de acción y de las advertencias y contraindicaciones oficiales del prospecto.
- Aclarar la indicación aprobada en los registros INVIMA y la razón de las cancelaciones.
- Un plan de seguridad para poblaciones vulnerables (adultos mayores, cirrosis, apnea del sueño) y para interacciones con depresores del sistema nervioso central.

Nota: el modelo también predijo **agorafobia** (puntaje 99.56%, nivel L1, "Proceed with Guardrails"), respaldada por múltiples estudios controlados en trastorno de pánico con agorafobia. Se trata, en la práctica, de un uso ya establecido del alprazolam y no de un reposicionamiento nuevo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

