---
layout: default
title: Rivastigmine
parent: Evidencia Moderada (L3-L4)
nav_order: 349
evidence_level: L4
indication_count: 1
---

# Rivastigmine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **1** 
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

# Rivastigmina: De Enfermedad de Alzheimer a Glaucoma

## Resumen en Una Frase

La rivastigmina es un inhibidor de la acetilcolinesterasa y la butirilcolinesterasa, usado originalmente para tratar la enfermedad de Alzheimer.
El modelo TxGNN predice que podría ser efectiva para **glaucoma**.
Actualmente esta dirección solo tiene respaldo preclínico: **0 ensayos clínicos** y **3 publicaciones**, con un único estudio experimental en conejos.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad de Alzheimer (según datos de farmacología; el registro de INVIMA solo indica "RIVASTIGMINA", sin texto de indicación) |
| Nueva Indicación Predicha | Glaucoma |
| Puntaje de Predicción TxGNN | 99.27% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 6 (2 números de registro distintos) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información farmacológica disponible, la rivastigmina es un inhibidor carbamato de la acetilcolinesterasa (AChE) y de la butirilcolinesterasa (BChE). Su eficacia en la enfermedad de Alzheimer es conocida, y mecanísticamente podría ser aplicable al glaucoma.

Al inhibir estas enzimas, aumenta la acetilcolina disponible. En el ojo, esto puede incrementar el tono del músculo ciliar y favorecer el drenaje por la malla trabecular, lo que reduce la presión intraocular (PIO). Es la misma lógica de los agentes colinérgicos usados en glaucoma, como la pilocarpina y la fisostigmina.

El vínculo es biológicamente plausible, pero el único respaldo directo es un estudio preclínico en conejos con rivastigmina tópica. No hay datos oculares en humanos. Tampoco se han evaluado los efectos colinérgicos sistémicos ni la tolerabilidad ocular de una formulación tópica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10673128](https://pubmed.ncbi.nlm.nih.gov/10673128/) | 2000 | Estudio preclínico en animales (conejo) | J Ocul Pharmacol Ther | La rivastigmina tópica, un inhibidor selectivo de la AChE, redujo la presión intraocular en conejos normotensos |
| [39130374](https://pubmed.ncbi.nlm.nih.gov/39130374/) | 2024 | Revisión / genética de sistemas y análisis molecular (diseño no verificado) | Front Mol Biosci | Analiza los agentes colinérgicos para reducir la PIO. Los agonistas M3 aprobados tienen efectos adversos colinérgicos sistémicos que limitan su uso |
| [27967267](https://pubmed.ncbi.nlm.nih.gov/27967267/) | 2017 | Revisión (literatura de patentes) | Expert Opin Ther Pat | Señala que la inhibición leve de la AChE tiene relevancia terapéutica en Alzheimer, miastenia gravis y glaucoma. Es una referencia general, no específica de rivastigmina |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20242182 | DURIVAST® 9.5MG/24H (BIOTOSCANA FARMA S.A.) | Transdérmicos | RIVASTIGMINA (el registro no detalla la indicación) |
| 20242522 | DURIVAST® 4.6MG/24H (BIOTOSCANA FARMA S.A.) | Sistema transdérmico de liberación prolongada (parche) | RIVASTIGMINA (el registro no detalla la indicación) |

Los datos recibidos repiten varias veces estos dos registros. Ambos productos son parches transdérmicos; no hay formulación oftálmica comercializada.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: no hay interacciones fármaco-fármaco listadas. La consulta solo devolvió las dianas farmacológicas de la rivastigmina: acetilcolinesterasa (ACHE) y butirilcolinesterasa (BCHE).
- Las advertencias y contraindicaciones del prospecto de INVIMA no están disponibles. Consultar el prospecto para esta información.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es mecanísticamente plausible y tiene un puntaje alto en TxGNN. Sin embargo, la evidencia es L4: un solo estudio preclínico en conejos, sin ensayos clínicos ni datos en humanos. Además, las advertencias del prospecto de INVIMA siguen sin revisar, y eso impide avanzar al tamizaje de seguridad.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones).
- Completar el mecanismo de acción desde DrugBank.
- Evaluar la compatibilidad de vía: los productos locales son parches transdérmicos y el glaucoma requeriría una formulación oftálmica.
- Datos de tolerabilidad ocular y de seguridad sistémica (efectos colinérgicos) de una formulación tópica.
- Estudios en humanos sobre la reducción de la PIO, comenzando por fases tempranas.
- Confirmar la relevancia de las publicaciones, que siguen pendientes de revisión.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

