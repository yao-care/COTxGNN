---
layout: default
title: Elvitegravir
parent: 僅模型預測 (L5)
nav_order: 108
evidence_level: L5
indication_count: 3
---

# Elvitegravir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Elvitegravir: De Infección por VIH-1 a Infección por Virus de Inmunodeficiencia en Simios

## Resumen en Una Frase

Elvitegravir es un inhibidor de la transferencia de cadena de la integrasa del VIH (INSTI), originalmente desarrollado como componente de regímenes antirretrovirales combinados para el tratamiento de la infección por VIH-1 en adultos. El modelo TxGNN predice que podría ser efectivo para la **Infección por Virus de Inmunodeficiencia en Simios (SIV)**, con **0 ensayos clínicos** y **7 publicaciones** científicas que respaldan esta dirección exclusivamente desde el ámbito preclínico.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección por VIH-1 (inhibidor de integrasa) |
| Nueva Indicación Predicha | Infección por Virus de Inmunodeficiencia en Simios (SIV) |
| Puntaje de Predicción TxGNN | 99.89% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el presente Evidence Pack. Según la información conocida en la literatura, elvitegravir bloquea la integración del ADN viral en el genoma de la célula huésped al inhibir específicamente el paso de transferencia de cadena catalizado por la integrasa del VIH, actuando sobre la tríada DDE del sitio activo enzimático. Su eficacia en infección por VIH-1 ha sido ampliamente comprobada en ensayos clínicos de Fase 3.

El virus de inmunodeficiencia en simios (SIV) y el VIH-1 pertenecen ambos a la familia de los lentivirus de primates y comparten una arquitectura funcional y estructural del sitio activo de la integrasa (tríada DDE) altamente conservada a nivel evolutivo. Esta homología molecular sustenta la hipótesis de que elvitegravir podría inhibir la replicación de SIV de manera mecanísticamente análoga a VIH-1. Los estudios recuperados confirman que EVG presenta actividad in vitro directa contra cepas SIVmac, y se ha caracterizado sistemáticamente su perfil de mutaciones de resistencia en este virus, evidenciando paralelismos con los patrones observados en VIH-1.

Sin embargo, es importante destacar que SIV es una enfermedad exclusiva de primates no humanos (PNH), sin aplicación clínica directa en humanos. La predicción del TxGNN refleja la proximidad biológica entre ambos virus en el grafo de conocimiento, más que una oportunidad terapéutica clínica inmediata. Toda la evidencia disponible pertenece al nivel preclínico (modelos in vitro y en macacos), y no existen ensayos clínicos en seres humanos para esta indicación.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [38134382](https://pubmed.ncbi.nlm.nih.gov/38134382/) | 2024 | Estudio animal NHP | The Journal of Infectious Diseases | Insertos vaginales TAF/EVG protegieron contra exposición vaginal repetida a SHIV en macacas con una eficacia del 93–100% en modelos de PEP hasta 4h post-exposición |
| [39559349](https://pubmed.ncbi.nlm.nih.gov/39559349/) | 2024 | Desarrollo de modelo animal | Frontiers in Immunology | Modelo de ratón humanizado dual para SIV y VIH; EVG empleado como componente del régimen antirretroviral de referencia para evaluar eficacia antiviral |
| [28923862](https://pubmed.ncbi.nlm.nih.gov/28923862/) | 2017 | Comparación antiviral in vitro | Antimicrobial Agents and Chemotherapy | Comparación de bictegravir y cabotegravir frente a EVG contra SIVmac239 con resistencias a INSTIs; EVG como referencia de clase |
| [26378179](https://pubmed.ncbi.nlm.nih.gov/26378179/) | 2015 | Perfil de resistencia in vitro | Journal of Virology | SIVmac239 es susceptible a INSTIs incluyendo EVG; las mutaciones de resistencia bajo presión farmacológica presentan fenotipos similares a los observados en VIH-1 |
| [25583721](https://pubmed.ncbi.nlm.nih.gov/25583721/) | 2015 | Modelo animal / in vitro | Antimicrobial Agents and Chemotherapy | Virus SIV/VIH recombinante tropismo T como modelo de PNH para estudiar resistencia a INSTIs incluyendo EVG y transmisión de variantes resistentes |
| [24920794](https://pubmed.ncbi.nlm.nih.gov/24920794/) | 2014 | Biología molecular / in vitro | Journal of Virology | Mutaciones de resistencia a RAL, EVG y DTG introducidas en el gen IN de SIVmac239; caracterización de susceptibilidad y vías de resistencia cruzada |
| [17977962](https://pubmed.ncbi.nlm.nih.gov/17977962/) | 2008 | Caracterización antiviral in vitro | Journal of Virology | Descripción original del perfil antiviral amplio de EVG (JTK-303/GS-9137) contra VIH-1 incluyendo subtipos y cepas multirresistentes; inhibición de transferencia de cadena de integrasa |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción del TxGNN refleja una relación biológica genuina y bien documentada entre elvitegravir y SIV (homología del sitio activo de la integrasa entre lentivirus), respaldada por 7 publicaciones preclínicas. Sin embargo, SIV es una enfermedad de primates no humanos sin aplicación clínica directa en seres humanos, no existen ensayos clínicos registrados para esta indicación, y elvitegravir no cuenta con registros sanitarios en Colombia, lo que hace inviable una evaluación de reposicionamiento con proyección comercial a corto plazo.

**Para avanzar se necesita:**
- Obtener datos completos de mecanismo de acción (MOA) desde DrugBank API para sustentar el análisis de relación mecanística
- Clarificar si la indicación objetivo tiene relevancia traslacional para humanos, por ejemplo, en el contexto de desarrollo de formulaciones preventivas de VIH (PrEP/PEP) donde los modelos SIV/SHIV en macacos son el estándar de validación preclínica
- Obtener información de seguridad, advertencias y contraindicaciones desde el prospecto oficial (ficha técnica / INVIMA)
- Evaluar si existen ensayos clínicos en humanos con formulaciones que contengan elvitegravir para prevención del VIH que pudieran constituir un pivot traslacional desde los datos de SIV
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

