---
layout: default
title: Vitamin A
parent: Solo Predicción del Modelo (L5)
nav_order: 663
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Vitamin A: nueva indicación predicha, Deficiencia congénita de protrombina (nivel de evidencia L5). Indicación original: Retinol (vitamina A)"
monitor_inn: "Vitamin A"
predicted_indications: ["congenital prothrombin deficiency", "biotin metabolic disease", "non-syndromic esophageal malformation", "injury", "cell proliferation disorder", "florid cemento-osseous dysplasia", "perinatal disease", "segmental odontomaxillary dysplasia", "disease by subcellular system affected", "radiation or chemically induced disorder"]
---

# Vitamin A
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

## Vitamina A: De Suplemento de Retinol a Enfermedad Perinatal
{: .text-alpha }

## Resumen en Una Frase

La vitamina A (retinol) está registrada en Colombia como suplemento en cápsulas de retinol (vitamina A).
El modelo TxGNN predice que podría ser efectivo para **enfermedad congénita por deficiencia de protrombina** (primera posición del ranking), pero sin ningún ensayo clínico ni publicación que lo respalde; la indicación con mayor soporte entre las candidatas es **enfermedad perinatal**, con **1 ensayo clínico** y **múltiples revisiones sistemáticas Cochrane** centradas en bebés prematuros de muy bajo peso.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Retinol (vitamina A) |
| Nueva Indicación Predicha | Deficiencia congénita de protrombina (rank 1 del modelo) |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L5 (para la indicación principal); la candidata con más soporte, enfermedad perinatal, alcanza L1 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, la vitamina A es un micronutriente liposoluble cuyos metabolitos (retinoides) actúan sobre receptores nucleares RAR/RXR y regulan la diferenciación, la proliferación y la apoptosis celular, además de la visión, la inmunidad y la integridad del epitelio.

Para la indicación principal predicha, la deficiencia congénita de protrombina, la predicción **no parece tener sustento biológico**. Se trata de un trastorno genético de la coagulación cuya vía plausible es la síntesis de factores dependientes de la vitamina K, no de la vitamina A. El puntaje alto probablemente refleja cercanía en la red de conocimiento del modelo (por ser ambas vitaminas liposolubles) y no una relación terapéutica real.

Entre las demás candidatas, la más coherente es **enfermedad perinatal**. La vitamina A es necesaria para el desarrollo y la reparación del epitelio pulmonar, y los recién nacidos prematuros nacen con reservas bajas, lo que se asocia con displasia broncopulmonar. Otras candidatas (lesión, trastorno de proliferación celular, trastorno inducido por radiación o químicos) tienen una justificación general e indirecta, y varias (malformación esofágica, displasia cemento-ósea, displasia odontomaxilar segmentaria) no tienen evidencia alguna.

## Evidencia de Ensayos Clínicos

Para la indicación principal (deficiencia congénita de protrombina) no hay ensayos clínicos registrados. Los ensayos disponibles corresponden a otras candidatas:

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01203488](https://clinicaltrials.gov/study/NCT01203488) | Fase 1/2 | Completado | 807 | Vitamina A en dosis altas en recién nacidos de peso extremadamente bajo (401-1000 g), para evaluar supervivencia sin displasia broncopulmonar y riesgo de sepsis (candidata: lesión) |
| [NCT02102711](https://clinicaltrials.gov/study/NCT02102711) | N/A | Completado | 62 | Vitamina A oral en neonatos <1500 g para prevenir displasia broncopulmonar y retinopatía del prematuro (candidata: lesión) |
| [NCT01115478](https://clinicaltrials.gov/study/NCT01115478) | N/A | Completado | 2500 | Suplementación con zinc y/o vitamina A para reducir malaria placentaria y resultados adversos del embarazo (candidata: enfermedad perinatal; relevancia limitada) |
| [NCT04000789](https://clinicaltrials.gov/study/NCT04000789) | N/A | Desconocido | 96 | Gotas oftálmicas de vitamina A + vitamina E + hialuronato en retinopatía diabética (candidata: trastorno de proliferación celular; relevancia baja) |

## Evidencia de Literatura

Para la indicación principal no hay literatura disponible. Las publicaciones más relevantes de las demás candidatas son:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [27552058](https://pubmed.ncbi.nlm.nih.gov/27552058/) | 2016 | Revisión sistemática (Cochrane) | Cochrane Database Syst Rev | Suplementación de vitamina A para prevenir mortalidad y morbilidad en recién nacidos de muy bajo peso |
| [21975731](https://pubmed.ncbi.nlm.nih.gov/21975731/) | 2011 | Revisión sistemática (Cochrane) | Cochrane Database Syst Rev | Versión previa de la misma revisión; vitamina A y enfermedad pulmonar crónica del prematuro |
| [17943744](https://pubmed.ncbi.nlm.nih.gov/17943744/) | 2007 | Revisión sistemática (Cochrane) | Cochrane Database Syst Rev | Actualización previa sobre morbilidad a corto y largo plazo en prematuros |
| [34105132](https://pubmed.ncbi.nlm.nih.gov/34105132/) | 2021 | Metaanálisis | J Spec Oper Med | Revisa la asociación entre vitamina A y riesgo de fractura ósea (señal de seguridad) |
| [31697447](https://pubmed.ncbi.nlm.nih.gov/31697447/) | 2019 | Revisión | Nutr Clin Pract | Papel de la vitamina A y los retinoides en la cicatrización de heridas |
| [34181622](https://pubmed.ncbi.nlm.nih.gov/34181622/) | 2021 | Revisión sistemática | Plast Reconstr Surg | Intervenciones nutricionales en el cuidado de heridas; poca evidencia para vitaminas y minerales |
| [40901583](https://pubmed.ncbi.nlm.nih.gov/40901583/) | 2025 | Revisión | World J Hepatol | Toxicidad de la vitamina A y patología hepática |
| [29173522](https://pubmed.ncbi.nlm.nih.gov/29173522/) | 2017 | Revisión | Gastroenterol Clin North Am | Vitaminas y minerales en enfermedad inflamatoria intestinal; la vitamina A dio resultados decepcionantes |
| [24419474](https://pubmed.ncbi.nlm.nih.gov/24419474/) | 2014 | Revisión | Hautarzt | Retinoides en dermatofarmacología y regulación de la proliferación celular |
| [39233460](https://pubmed.ncbi.nlm.nih.gov/39233460/) | 2024 | Revisión | Skin Res Technol | Cosmecéuticos en fotoenvejecimiento |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19960905 | VITAMINA A CAPSULAS (C.I. Farmacápsulas S.A.S.) | Cápsula dura | Retinol (vitamina A) — estado: cancelado |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento del modelo** (relaciones fármaco-enfermedad, no texto de prospecto): enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, úlcera péptica, sarcoidosis, hipercalcemia, nefrocalcinosis, nefrolitiasis, hiperoxaluria primaria, anemia falciforme, anemia hemolítica, hemocromatosis hereditaria, hemosiderosis, enfermedad de Wilson, enfermedad inflamatoria intestinal, colitis ulcerosa, gastroenteritis, hipervitaminosis y arteriosclerosis obliterante, entre otras.
- **Interacciones farmacológicas** (68 registradas): las de nivel **mayor** incluyen retinoides (isotretinoína, acitretina, tretinoína) y tetraciclinas (doxiciclina, tetraciclina, minociclina, omadaciclina, demeclociclina, eravaciclina, oxitetraciclina, sarecyclina). De nivel **moderado**: bexaroteno, colestiramina, colesevelam, colestipol, sevelámero y selpercatinib. De nivel **menor**: orlistat.
- **Señales de la literatura**: la vitamina A en exceso es teratogénica y se asocia con toxicidad hepática y mayor riesgo de fracturas óseas, lo que es especialmente relevante en candidatas del desarrollo (malformaciones) y en el embarazo.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación con mayor puntaje del modelo (deficiencia congénita de protrombina) carece de evidencia y de plausibilidad biológica. La candidata con más respaldo (enfermedad perinatal, en la práctica displasia broncopulmonar en prematuros) tiene revisiones Cochrane, pero el beneficio es modesto, la etiqueta es muy amplia, el único registro sanitario en Colombia está cancelado y faltan datos de seguridad de prospecto.

**Para avanzar se necesita:**
- Obtener las advertencias y contraindicaciones del prospecto en INVIMA (brecha bloqueante para el tamizaje de seguridad).
- Obtener datos del mecanismo de acción desde DrugBank.
- Verificar los ensayos clínicos aleatorizados primarios detrás de las revisiones Cochrane, porque el nivel L1 de enfermedad perinatal se basa en esas revisiones y no en ensayos incluidos en los datos.
- Delimitar la indicación perinatal a una condición concreta (por ejemplo, displasia broncopulmonar en prematuros de muy bajo peso) y evaluar la vía de administración (intramuscular) y su viabilidad.
- Evaluar la situación regulatoria, dado que no hay registros vigentes en Colombia, y el perfil de seguridad en poblaciones vulnerables (embarazo, enfermedad hepática y renal).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

