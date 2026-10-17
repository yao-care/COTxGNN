---
layout: default
title: Etofenamate
parent: Solo Predicción del Modelo (L5)
nav_order: 268
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Etofenamate: nueva indicación predicha, Espondilitis anquilosante (predicción de mayor puntaje: «susceptibili… (nivel de evidencia L5). Indicación original: ETOFENAMATO"
monitor_inn: "Etofenamate"
predicted_indications: ["ankylosing spondylitis", "rheumatoid vasculitis", "hypermobility of coccyx", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "pseudoachondroplasia", "myosclerosis", "polyarticular juvenile rheumatoid arthritis", "Kummell disease"]
---

# Etofenamate
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Etofenamato: De Etofenamato (indicación no detallada en el registro) a Espondilitis Anquilosante

## Resumen en Una Frase

Etofenamato es un antiinflamatorio no esteroideo (AINE) del grupo de los fenamatos, con un registro sanitario en Colombia (hoy cancelado) en solución inyectable; el texto de indicación del registro solo repite el nombre del producto.
El modelo TxGNN predice que podría ser efectivo para **espondilitis anquilosante**, con **0 ensayos clínicos** y **1 publicación** (un estudio farmacocinético) que respaldan indirectamente esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | ETOFENAMATO (el registro no detalla una indicación clínica específica) |
| Nueva Indicación Predicha | Espondilitis anquilosante (predicción de mayor puntaje: «susceptibilidad genética a espondiloartropatía», un término genético y no una condición tratable) |
| Puntaje de Predicción TxGNN | 99.998% (espondilitis anquilosante); 99.9996% (susceptibilidad a espondiloartropatía) |
| Nivel de Evidencia | L4 (espondilitis anquilosante); L5 para la mayoría de las demás predicciones |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

**Nota sobre la indicación principal:** la predicción con mayor puntaje es «susceptibilidad genética a espondiloartropatía», un término genético que no corresponde a una condición tratable. Por ello el informe se centra en la espondilitis anquilosante, la primera predicción clínicamente relevante y la única con alguna literatura asociada.

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, el etofenamato es un AINE tópico del grupo de los fenamatos que inhibe la ciclooxigenasa (COX). Esto reduce la inflamación y el dolor mediados por prostaglandinas.

Los AINE son tratamiento sintomático de primera línea en la espondiloartritis y la espondilitis anquilosante. Por eso la relación entre un antiinflamatorio y esta enfermedad es mecanísticamente plausible.

Sin embargo, la evidencia es indirecta. La única publicación vinculada demuestra que el etofenamato llega al suero y al líquido sinovial tras iontoforesis, lo que indica penetración tisular, pero no demuestra eficacia en espondilitis anquilosante. Además, la administración tópica a articulaciones axiales profundas podría ser una limitación.

Las demás predicciones carecen de respaldo: varias son enfermedades genéticas esqueléticas (displasia acromesomélica tipo Hunter-Thompson, síndrome de braquiolmia-amelogénesis imperfecta, pseudoacondroplasia) donde un AINE no actúa sobre la patología de fondo, probablemente por artefactos del grafo del modelo. En la vasculitis reumatoide, que se trata con inmunosupresores, un AINE tópico difícilmente sería adecuado.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [11455681](https://pubmed.ncbi.nlm.nih.gov/11455681/) | 2001 | Estudio farmacocinético | Arzneimittel-Forschung | Tras 5 días de iontoforesis con gel de etofenamato (100 mg diarios) en 11 pacientes con lumbalgia y 13 con sinovitis de rodilla, se midieron concentraciones del fármaco en suero y líquido sinovial, con lo que se confirma su penetración. No evalúa eficacia en espondilitis anquilosante. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20069025 (cancelado) | ETOFENAMATO 1G/2ML (Laboratorios MK S.A.S) | Solución inyectable | ETOFENAMATO |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas en los datos compilados para este informe.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Las predicciones se basan casi por completo en el modelo: no hay ensayos clínicos y la única publicación es un estudio farmacocinético sin datos de eficacia. Además, el único registro sanitario en Colombia está cancelado y no se dispone de información de seguridad. Para espondilitis anquilosante el planteamiento puede mantenerse como pregunta de investigación.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), indispensable antes de cualquier evaluación de seguridad.
- Obtener datos del mecanismo de acción desde DrugBank.
- Estudios de eficacia del etofenamato en espondilitis anquilosante o dolor axial, y evaluación de si la vía tópica alcanza articulaciones profundas.
- Aclarar la situación regulatoria (registro cancelado) y la disponibilidad de una formulación adecuada en Colombia.
- Descartar las predicciones sin plausibilidad biológica (enfermedades genéticas esqueléticas, vasculitis reumatoide) de cualquier priorización.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

