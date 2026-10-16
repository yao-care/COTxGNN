---
layout: default
title: Dabigatran Etexilate
parent: Solo Predicción del Modelo (L5)
nav_order: 189
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Dabigatran Etexilate: nueva indicación predicha, Colangitis esclerosante (nivel de evidencia L5). Indicación original: Dabigatrán etexilato"
---

# Dabigatran Etexilate
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Dabigatrán etexilato: De Anticoagulante Oral a Colangitis Esclerosante

## Resumen en Una Frase

Dabigatrán etexilato es un anticoagulante oral inhibidor directo de la trombina, registrado en Colombia en cápsulas duras. El modelo TxGNN predice que podría ser efectivo para **colangitis esclerosante**, pero actualmente hay **0 ensayos clínicos** y **1 publicación** (que no evalúa eficacia en esta enfermedad), por lo que la predicción no tiene respaldo clínico.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dabigatrán etexilato (el registro sanitario no detalla una indicación clínica específica) |
| Nueva Indicación Predicha | Colangitis esclerosante |
| Puntaje de Predicción TxGNN | 99.82% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 3 (los 3 cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, dabigatrán es un inhibidor directo de la trombina, y su eficacia como anticoagulante está establecida en sus usos aprobados.

Mecanísticamente existe un vínculo plausible pero hipotético: la trombina y la señalización de PAR-1 contribuyen a la inflamación y la fibrosis hepática, por lo que inhibir la trombina podría influir en la fibrosis colestásica propia de la colangitis esclerosante. Sin embargo, no hay estudios que lo confirmen.

La única publicación recuperada (PMID 36906733) trata sobre interacciones farmacológicas de cilofexor, un agonista de FXR, y no sobre dabigatrán ni sobre su eficacia en colangitis esclerosante. El puntaje de 99.82% es solo una predicción computacional y no constituye evidencia clínica.

Otras predicciones del modelo (hiperlipidemias, hipoalfalipoproteinemia, trastorno de liberación plaquetaria) tienen aún menos sustento mecanístico. En particular, para el trastorno de liberación plaquetaria, un anticoagulante podría agravar el riesgo de sangrado.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para colangitis esclerosante.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36906733](https://pubmed.ncbi.nlm.nih.gov/36906733/) | 2023 | Farmacología (evaluación de interacciones) | Clinical Pharmacokinetics | Evalúa el potencial de interacciones mediadas por citocromo P450 y transportadores de cilofexor, agonista de FXR en desarrollo para esteatohepatitis y colangitis esclerosante primaria. No estudia dabigatrán ni su eficacia. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20188200 (cancelado) | DAGITRAN® 150 MG CAPSULAS DURAS | Cápsula dura | Dabigatrán etexilato |
| 20195074 (cancelado) | DABIFIB® 150 MG CÁPSULA DURA | Cápsula dura | Dabigatrán etexilato |
| 20218080 (cancelado) | NORMOLET® 110 MG CÁPSULA DURA | Cápsula dura | Dabigatrán etexilato |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: enfermedad de la coagulación sanguínea, anemia, anemia macrocítica y hemorragia intracerebral.
- **Riesgo de sangrado**: al ser un anticoagulante, existe preocupación de que empeore trastornos hemorrágicos, en especial en la predicción de trastorno de liberación plaquetaria.

No se encontraron interacciones farmacológicas en la consulta realizada. Consultar el prospecto para el resto de la información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para colangitis esclerosante se basa solo en el modelo (nivel L5): no hay ensayos clínicos ni literatura que evalúe dabigatrán en esta enfermedad. Además, el producto no tiene registros vigentes en Colombia.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank
- Advertencias y contraindicaciones del prospecto de INVIMA
- Estudios preclínicos que evalúen la inhibición de trombina/PAR-1 en modelos de fibrosis colestásica
- Revisión sistemática de literatura específica sobre dabigatrán en enfermedades hepatobiliares
- Evaluación de la viabilidad regulatoria, dado que no hay registros vigentes en Colombia
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

