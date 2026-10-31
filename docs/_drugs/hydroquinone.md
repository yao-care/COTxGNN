---
layout: default
title: Hydroquinone
parent: Solo Predicción del Modelo (L5)
nav_order: 330
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-31
description: "Hydroquinone: nueva indicación predicha, Queratosis seborreica (nivel de evidencia L4). Indicación original: Hidroquinona"
monitor_inn: "hydroquinone"
predicted_indications: ["seborrheic keratosis", "vulvar inverted follicular keratosis", "exanthem (disease)", "lichen disease"]
---

# Hydroquinone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

## Hidroquinona: De Hidroquinona (uso tópico despigmentante) a Queratosis Seborreica
{: .text-alpha }

## Resumen en Una Frase

La hidroquinona es un agente despigmentante tópico, registrado en Colombia en forma de crema al 5% (CREMOQUINONA 5% CREMA).
El modelo TxGNN predice que podría ser efectiva para **queratosis seborreica**,
pero hasta ahora solo hay **0 ensayos clínicos** y **1 publicación** (un estudio observacional prospectivo sobre trastornos pigmentarios faciales) con relación indirecta a esta predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hidroquinona (el registro no detalla una indicación específica) |
| Nueva Indicación Predicha | Queratosis seborreica |
| Puntaje de Predicción TxGNN | 0,9973 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 1) |
| Número de Registros Sanitarios | al menos 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

La hidroquinona es un inhibidor de la tirosinasa que reduce la síntesis de melanina. No se dispone de datos detallados sobre el mecanismo de acción en la base de datos consultada, pero este mecanismo es ampliamente conocido en dermatología para el tratamiento de la hiperpigmentación.

Las lesiones de queratosis seborreica suelen estar hiperpigmentadas, por lo que un agente despigmentante podría aclararlas con fines cosméticos. Sin embargo, esto no trataría la proliferación subyacente de los queratinocitos. El puntaje elevado de TxGNN probablemente refleja características de red compartidas relacionadas con la pigmentación, y no un mecanismo que modifique la enfermedad.

Por lo tanto, la predicción es plausible solo como beneficio sintomático/estético y no como tratamiento de la enfermedad en sí.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para queratosis seborreica.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33046430](https://pubmed.ncbi.nlm.nih.gov/33046430/) | 2021 | Estudio observacional prospectivo | J Plast Reconstr Aesthet Surg | Algoritmo de tratamiento combinado para trastornos pigmentarios faciales en pacientes asiáticos; la mayoría presenta varios trastornos a la vez y no existía un algoritmo definitivo |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 48599 (cancelado) | CREMOQUINONA 5% CREMA | Crema tópica | Hidroquinona |

---

## Consideraciones de Seguridad

- **Posibles contraindicaciones según el grafo de conocimiento (PrimeKG, no provienen del prospecto):** quemadura solar, insuficiencia suprarrenal, enfermedad de Addison, atrofia cutánea, telangiectasia, enfermedad capilar, telangiectasia hemorrágica hereditaria, enfermedad vascular periférica, claudicación vascular intermitente, enfermedad arterial periférica, eccema atópico y dermatitis.
- **Interacciones farmacológicas:** no se encontraron interacciones registradas en la consulta realizada.

Consultar el prospecto para obtener información completa sobre advertencias y contraindicaciones.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia es de nivel L4: no hay ensayos clínicos y la única publicación trata de trastornos pigmentarios en general, no de queratosis seborreica. Además, el único registro sanitario en Colombia está cancelado, y el mecanismo solo respaldaría un efecto cosmético, no una acción sobre la enfermedad.

**Para avanzar se necesita:**
- Estudios clínicos específicos de hidroquinona en queratosis seborreica que midan resultados clínicos y estéticos
- Obtener y revisar el prospecto (advertencias y contraindicaciones), pues faltan datos de seguridad de la etiqueta
- Datos detallados del mecanismo de acción
- Aclarar la situación regulatoria en Colombia (registro cancelado; evaluar un nuevo registro o alternativas vigentes)
- Evaluar la seguridad de uso prolongado y sobre piel con atrofia, dermatitis o telangiectasias, dadas las contraindicaciones señaladas en el grafo de conocimiento
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

