---
layout: default
title: Cabozantinib
parent: 僅模型預測 (L5)
nav_order: 77
evidence_level: L5
indication_count: 10
---

# Cabozantinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

A continuación presento el informe de evaluación generado a partir del Evidence Pack proporcionado:

---

# Cabozantinib: De Carcinoma de Células Renales a Liposarcoma

## Resumen en Una Frase

Cabozantinib es un inhibidor de tirosina quinasa multiobjetivo (VEGFR2 / MET / AXL) aprobado globalmente para el tratamiento del carcinoma de células renales avanzado, aunque actualmente no cuenta con registro sanitario en Colombia. El modelo TxGNN predice que podría ser efectivo para **Liposarcoma**, con **1 ensayo clínico** y **1 publicación** que respaldan actualmente esta dirección. La evidencia disponible es preliminar: el liposarcoma aparece incluido como subgrupo dentro de un ensayo más amplio de sarcoma de tejidos blandos, con resultados específicos de subgrupo aún pendientes de publicación.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Carcinoma de Células Renales (aprobado por FDA; sin registro en Colombia) |
| Nueva Indicación Predicha | Liposarcoma |
| Puntaje de Predicción TxGNN | 99.83% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Cabozantinib inhibe simultáneamente tres vías de señalización cinasa clave: VEGFR2 (suprime la angiogénesis tumoral bloqueando el suministro vascular al tumor), MET (interrumpe los mecanismos de resistencia a los inhibidores de VEGF y la invasión tumoral mediada por HGF) y AXL (revierte el microambiente inmunosupresor, potenciando la sinergia con inhibidores de PD-1/PD-L1). Esta triple mecanística ha sido ampliamente validada en carcinoma renal a través de múltiples ensayos de Fase 3 de gran escala (METEOR, CABOSUN y CheckMate 9ER).

En el liposarcoma —particularmente en la variante desdiferenciada— se ha documentado sobreexpresión de MET, dependencia angiogénica mediada por VEGFR y alta expresión de AXL. Estos tres receptores representan los blancos terapéuticos directos de Cabozantinib, lo que aporta una base mecanística biológicamente plausible para explorar esta indicación. Un estudio de Fase 1 ya ha evaluado la seguridad de Cabozantinib neoadyuvante en sarcomas de extremidades, ofreciendo un primer dato de viabilidad clínica en esta familia tumoral.

No obstante, actualmente no se dispone de datos de eficacia específicos para liposarcoma ni de un análisis de subgrupo publicado. El único ensayo clínico disponible (NCT05836571, Fase 2) incluye liposarcoma dentro de una cohorte más amplia de sarcoma de tejidos blandos avanzado. Hasta que se conozcan los resultados del subgrupo, la evidencia permanece en nivel L3 y la hipótesis de reposicionamiento requiere confirmación clínica adicional.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|------------------|------|--------|-------------|----------------------|
| [NCT05836571](https://clinicaltrials.gov/study/NCT05836571) | Fase 2 | Activo, sin nuevas inscripciones | 66 | ECA aleatorizado que compara Cabozantinib + Ipilimumab + Nivolumab frente a inmunoterapia sola (Ipilimumab + Nivolumab) en sarcoma de tejidos blandos avanzado. El liposarcoma está incluido como subgrupo dentro de la cohorte general de STS; los resultados específicos de este subgrupo están pendientes de publicación (finalización estimada mayo 2026). |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [41770651](https://pubmed.ncbi.nlm.nih.gov/41770651/) | 2026 | Ensayo Fase 1 | American Journal of Clinical Oncology | Evaluación de seguridad de Cabozantinib neoadyuvante combinado con radioterapia en sarcomas de extremidades. El estudio abordó la preocupación por riesgo de fístula o perforación con esta combinación, y reportó actividad de Cabozantinib en múltiples subtipos de STS incluyendo liposarcoma como parte de la población tratada. |

---

## Información de Mercado en Colombia

Cabozantinib no cuenta con ningún registro sanitario aprobado por el INVIMA. No se identificaron licencias activas ni antecedentes de comercialización en el país.

---

## Citotoxicidad

| Item | Contenido |
|------|-----------|
| Clasificación de Citotoxicidad | Terapia dirigida — Inhibidor de tirosina quinasa multidiana (VEGFR2 / MET / AXL) |
| Riesgo de Mielosupresión | Moderado (neutropenia y trombocitopenia reportadas en ensayos de RCC; monitoreo hematológico periódico recomendado) |
| Clasificación de Emetogenicidad | Baja a moderada (formulación oral) |
| Ítems de Monitoreo | Hemograma completo con diferencial, función hepática (ALT / AST / bilirrubina), función renal (creatinina / TFGe), presión arterial, TSH (riesgo de hipotiroidismo), electrolitos séricos |
| Protección en Manejo | Formulación oral; seguir protocolos estándar de manejo seguro de medicamentos citotóxicos orales |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia actual para Cabozantinib en liposarcoma se limita a un ensayo de Fase 2 en curso que incluye este subtipo como subgrupo dentro de una cohorte más amplia de sarcoma de tejidos blandos (sin resultados de subgrupo disponibles) y un estudio de Fase 1 de seguridad neoadyuvante. El nivel de evidencia L3 es insuficiente para respaldar una decisión regulatoria o comercial, especialmente considerando que Cabozantinib no tiene registro INVIMA en Colombia (0 licencias activas).

**Para avanzar se necesita:**
- Resultados del análisis de subgrupo de liposarcoma del ensayo NCT05836571 (finalización estimada mayo 2026)
- Datos de eficacia específicos para liposarcoma: tasa de respuesta objetiva (ORR), supervivencia libre de progresión (SLP) y supervivencia global (SG)
- Información completa del mecanismo de acción (MOA) de Cabozantinib en el contexto de sarcomas y liposarcoma (actualmente en brecha de datos)
- Inicio del proceso de registro sanitario ante el INVIMA como prerrequisito para cualquier uso en Colombia
- Estratificación por subtipos histológicos de liposarcoma (bien diferenciado / desdiferenciado / mixoide / pleomórfico) dado el potencial diferencial de respuesta a la inhibición de MET / VEGFR / AXL
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

