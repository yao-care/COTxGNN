---
layout: default
title: Carfilzomib
parent: Solo Predicción del Modelo (L5)
nav_order: 138
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-31
monitor_inn: "CARFILZOMIB"
predicted_indications: ["CMM7", "pediatric leptomeningeal melanoma", "epithelioid cell uveal melanoma", "vulvar melanoma (disease)", "melanoma"]
description: "Carfilzomib: nueva indicación predicha, CMM7 (nivel de evidencia L5). Indicación original: CARFILZOMIB"
---

# Carfilzomib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Carfilzomib: CMM7
{: .text-alpha }

## Resumen en Una Frase

Carfilzomib es un inhibidor del proteasoma que cuenta con registros sanitarios en Colombia, aunque el texto de indicación registrado solo repite el nombre del fármaco, por lo que no se dispone de una indicación original descrita.
El modelo TxGNN predice que podría ser efectivo para **CMM7** (un subtipo o locus de susceptibilidad de melanoma maligno cutáneo), con un puntaje de 0.9937.
Actualmente hay **0 ensayos clínicos** y **0 publicaciones** directamente asociados a esta predicción, por lo que se trata de una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | CARFILZOMIB |
| Nueva Indicación Predicha | CMM7 |
| Puntaje de Predicción TxGNN | 0.9937 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 4) |
| Número de Registros Sanitarios | al menos 4 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, carfilzomib es un inhibidor irreversible de la actividad tipo quimotripsina del proteasoma 20S, usado en oncología (principalmente mieloma múltiple). Al bloquear el proteasoma se acumulan proteínas mal plegadas y reguladoras, lo que genera estrés del retículo endoplásmico y apoptosis.

CMM7 parece corresponder a un subtipo o locus de susceptibilidad de melanoma maligno cutáneo. Un vínculo plausible es que la inhibición del proteasoma cause estrés proteotóxico y muerte celular en las células de melanoma. Sin embargo, esta relación se infiere del contexto general del melanoma y no está respaldada por datos directos sobre CMM7.

Es importante señalar que la similitud entre la indicación original y la nueva no pudo evaluarse con los datos disponibles.

Otras predicciones de alto puntaje para este fármaco también corresponden a melanomas, con diferentes limitaciones:
- **Melanoma leptomeníngeo pediátrico** (0.9930): se espera una mala penetración de carfilzomib a través de la barrera hematoencefálica, además de preocupaciones adicionales de seguridad en población pediátrica.
- **Melanoma uveal de células epitelioides** (0.9923): es biológicamente distinto del melanoma cutáneo (dependiente de GNAQ/GNA11), por lo que los datos cutáneos no son extrapolables directamente.
- **Melanoma vulvar** (0.9919): el melanoma mucoso difiere genéticamente del cutáneo y la extrapolación no está validada.
- **Melanoma** en general (0.9903, nivel L4): existe respaldo preclínico (ver abajo).

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Para CMM7 no hay literatura disponible. Como referencia contextual, para la indicación más amplia de **melanoma** se identificaron los siguientes estudios, todos preclínicos o computacionales:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33671902](https://pubmed.ncbi.nlm.nih.gov/33671902/) | 2021 | Estudio preclínico in vitro | Biology | Carfilzomib combinado con bortezomib aumenta la muerte celular apoptótica en células de melanoma B16-F1, con activación de caspasas 3, 8, 9 y 12 |
| [36134605](https://pubmed.ncbi.nlm.nih.gov/36134605/) | 2023 | Estudio computacional | J Biomol Struct Dyn | Acoplamiento molecular y simulaciones para reposicionar fármacos contra dianas de cinasas en varios cánceres, incluido el melanoma |
| [31540997](https://pubmed.ncbi.nlm.nih.gov/31540997/) | 2019 | Estudio mecanístico preclínico | Mol Cancer Res | El gen AIRAP-L (ZFAND2A) regula la supervivencia celular en melanoma humano, con participación de la ligasa E3 cIAP2 |
| [27016342](https://pubmed.ncbi.nlm.nih.gov/27016342/) | 2016 | Estudio mecanístico preclínico | Matrix Biol | Bortezomib y carfilzomib activan NF-κB e inducen la expresión de heparanasa, asociada a un fenotipo tumoral más agresivo |

Los tres últimos estudios ofrecen solo apoyo indirecto o contextual. El último, de hecho, sugiere un posible efecto no deseado de los inhibidores del proteasoma.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20087826 | KYPROLIS® (Amgen Inc.) | Polvo liofilizado | Carfilzomib (vigente) |
| 20260831 | DETAMZIB® 60 MG (Sandoz GmbH) | Polvo liofilizado | Carfilzomib (vigente) |
| 20252729 | GLENCARFIL® (Glenmark Pharmaceuticals Colombia S.A.S.) | Polvo liofilizado para reconstituir a solución inyectable | Carfilzomib (vigente) |
| 20228189 | ALCAF ELEA® 60 MG (Laboratorio Elea Colombia S.A.S.) | Polvo liofilizado para reconstituir a solución inyectable | Carfilzomib (vigente) |

Los cuatro registros se encuentran cancelados; actualmente no hay registros vigentes.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor del proteasoma) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto (en la práctica clínica se describen trombocitopenia y neutropenia) |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal, electrolitos |
| Protección en Manejo | Seguir las regulaciones de manejo de fármacos citotóxicos/antineoplásicos |

---

## Consideraciones de Seguridad

**Interacciones Farmacológicas:** se identificaron 100 interacciones en total (fuente: DDInter). Entre las de nivel **Mayor** destacan:
- Esteroides anabolizantes: oxandrolona, oximetolona, estanozolol
- Deferiprona
- Samario (153Sm) lexidronam
- Factores de coagulación y hemostáticos: factor antihemofílico recombinante, ácido aminocaproico, factor de von Willebrand, factor VIIa recombinante, factor X humano, inhibidor de C1-esterasa humano, conestat alfa
- Avatrombopag

Entre las de nivel **Moderado** se incluyen metronidazol, tinidazol, naltrexona, rosuvastatina, simvastatina, palifermina y cloruro de estroncio Sr-89.

No se dispone de advertencias ni contraindicaciones del prospecto en los datos compilados; consultar el prospecto para esa información.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de CMM7 se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura directa. Además, los registros sanitarios en Colombia están cancelados y faltan datos de seguridad y mecanismo.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto (advertencias y contraindicaciones), un faltante que bloquea el tamizaje de seguridad
- Completar los datos del mecanismo de acción (por ejemplo, desde DrugBank)
- Aclarar qué es CMM7 y su relación con el melanoma cutáneo
- Generar evidencia preclínica específica (líneas celulares, modelos in vivo) y valorar la indicación más amplia de melanoma (L4) como pregunta de investigación
- Aclarar la situación regulatoria y la disponibilidad del producto en Colombia, dado que está comercializado y cuenta con 4 registros vigentes
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

