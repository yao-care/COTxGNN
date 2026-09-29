---
layout: default
title: Raltegravir
parent: Evidencia Moderada (L3-L4)
nav_order: 337
evidence_level: L4
indication_count: 3
---

# Raltegravir
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **3** 
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

# Raltegravir: De Infección por VIH-1 a Infección por Virus de Inmunodeficiencia de los Simios (SIV)

## Resumen en Una Frase

Raltegravir es un inhibidor de la integrasa del VIH-1 comercializado en Colombia como Isentress®.
El modelo TxGNN predice que podría ser efectivo para la **infección por virus de inmunodeficiencia de los simios (SIV)**,
pero la evidencia es solo preclínica: **1 ensayo clínico** (retirado, sin participantes) y **19 publicaciones**, casi todas en macacos o in vitro. El SIV es el modelo animal estándar del VIH, no una enfermedad humana, por lo que esto no constituye una nueva indicación terapéutica.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto solo dice "RALTEGRAVIR"); farmacológicamente, infección por VIH-1 |
| Nueva Indicación Predicha | Infección por virus de inmunodeficiencia de los simios (SIV) |
| Puntaje de Predicción TxGNN | 99.78% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 4 (2 números de registro distintos) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información conocida, raltegravir es un inhibidor de la transferencia de cadena de la integrasa retroviral (INSTI). Su eficacia en el VIH-1 está comprobada, y mecanísticamente podría ser aplicable al SIV.

La integrasa del SIV está lo bastante conservada como para que el fármaco actúe sobre ella. Los estudios en macacos rhesus y en cultivos celulares lo confirman: el SIVmac251 responde a esquemas con raltegravir y el SIVmac239 es sensible a los INSTI, con mutaciones de resistencia similares a las del VIH.

Esa evidencia respalda el uso de raltegravir en el modelo animal del VIH-1, es decir, la indicación ya aprobada. No abre una indicación nueva en humanos.

Las otras dos predicciones del modelo son más débiles:
- **Sida felino**: la integrasa del FIV es homóloga a la del VIH-1, pero no hay datos en felinos. Los dos ensayos de Fase 3 son en VIH-1 humano, con raltegravir como comparador.
- **Trastorno del neurodesarrollo con marcha atáxica, ausencia del habla y reducción de la sustancia blanca cortical**: no se identificó ningún vínculo mecanístico, y el puntaje alto probablemente es un artefacto del grafo de conocimiento.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00863668](https://clinicaltrials.gov/study/NCT00863668) | N/A | Retirado | 0 | Cinética de decaimiento del VIH con raltegravir en humanos, no en SIV. Al ser retirado y no tener participantes, no aporta datos. |

## Evidencia de Literatura

No hay ensayos clínicos aleatorizados ni revisiones sistemáticas. Todos los estudios son preclínicos (macacos o in vitro).

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [20233398](https://pubmed.ncbi.nlm.nih.gov/20233398/) | 2010 | Preclínico (primates no humanos) | Retrovirology | Esquema de dos análogos nucleósidos/nucleótidos más raltegravir en macacos infectados con SIVmac251; base para un tratamiento del SIDA simio. |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Preclínico (primates no humanos) | PLoS Pathogens | Terapia antirretroviral muy intensificada que logra supresión viral prolongada y restricción del reservorio en un modelo de SIDA simio. |
| [29643246](https://pubmed.ncbi.nlm.nih.gov/29643246/) | 2018 | Preclínico (primates no humanos) | Journal of Virology | Dinámica de círculos 2-LTR del SIV en macacos tratados con un inhibidor de integrasa, con y sin células CD8+. |
| [29466356](https://pubmed.ncbi.nlm.nih.gov/29466356/) | 2018 | Preclínico (primates no humanos) | PLoS One | Aparición de mutaciones de resistencia en macacos con SIV bajo terapia no supresora (tenofovir/emtricitabina más raltegravir). |
| [31597776](https://pubmed.ncbi.nlm.nih.gov/31597776/) | 2019 | Preclínico (primates no humanos) | Journal of Virology | Integridad de los genomas virales persistentes en macacos con SIV tras iniciar terapia antirretroviral en el primer año. |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | Preclínico (primates no humanos) | mBio | Los lentivirus persisten en el cerebro a pesar de la terapia antirretroviral efectiva. |
| [24622515](https://pubmed.ncbi.nlm.nih.gov/24622515/) | 2014 | Preclínico (primates no humanos) | Science Translational Medicine | Protección posexposición de macacos frente a SHIV vaginal con inhibidores de integrasa tópicos. |
| [24920794](https://pubmed.ncbi.nlm.nih.gov/24920794/) | 2014 | In vitro | Journal of Virology | Efecto de mutaciones de resistencia de la integrasa del VIH-1, introducidas en SIVmac239, sobre la sensibilidad a los INSTI. |
| [26378179](https://pubmed.ncbi.nlm.nih.gov/26378179/) | 2015 | In vitro | Journal of Virology | Perfiles de resistencia a INSTI en SIVmac239; se seleccionan mutaciones similares a las del VIH. |
| [32166319](https://pubmed.ncbi.nlm.nih.gov/32166319/) | 2020 | In vitro / mecanístico | Clinical Infectious Diseases | Dolutegravir y raltegravir tienen efectos proadipogénicos y profibróticos e inducen resistencia a la insulina en tejido adiposo humano/simio. Es un hallazgo de seguridad, no de eficacia contra el SIV. |

## Información de Mercado en Colombia

Los 4 registros del paquete de evidencia corresponden a 2 números de registro distintos (cada uno aparece duplicado). Se listan sin repetir.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20082552 | ISENTRESS® Gránulos para suspensión oral 100 mg | Gránulos | El registro solo indica "RALTEGRAVIR" |
| 20060995 | ISENTRESS® Tabletas masticables 25 mg | Tableta masticable | El registro solo indica "RALTEGRAVIR" |

Ambos productos son fabricados por Merck Sharp & Dohme LLC.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El SIV es un modelo animal del VIH-1, y toda la evidencia (19 publicaciones preclínicas y un ensayo retirado sin participantes) respalda el uso ya aprobado, no una nueva indicación. Con nivel de evidencia L4, no hay base para avanzar en una etapa de reposicionamiento.

**Para avanzar se necesita:**
- Definir si esta predicción tiene relevancia clínica humana. Si no la tiene, descartarla como candidata de reposicionamiento.
- Descargar y analizar el prospecto de INVIMA para completar advertencias y contraindicaciones, un bloqueo para el tamizaje de seguridad.
- Consultar la API de DrugBank para completar el mecanismo de acción.
- Aclarar la indicación aprobada de los registros sanitarios, cuyo texto solo repite el nombre del fármaco.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

