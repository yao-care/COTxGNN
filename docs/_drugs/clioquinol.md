---
layout: default
title: Clioquinol
parent: Evidencia Moderada (L3-L4)
nav_order: 166
evidence_level: L4
indication_count: 7
last_modified_at: 2026-10-14
description: "Clioquinol: nueva indicación predicha, Candidiasis cutánea (nivel de evidencia L4). Indicación original: Betametasona y antibióticos"
monitor_inn: "CLIOQUINOL"
predicted_indications: ["ectothrix infectious disease", "Majocchi granuloma", "endothrix infectious disease"]
---

# Clioquinol
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **7** 
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

## Clioquinol: De Betametasona y Antibióticos a Candidiasis Cutánea
{: .text-alpha }

## Resumen en Una Frase

Clioquinol es un compuesto de la familia de las 8-hidroxiquinolinas halogenadas, registrado en Colombia únicamente en cremas tópicas asociadas a betametasona y antibióticos.
El modelo TxGNN predice que podría ser efectivo para **candidiasis cutánea**, pero actualmente solo cuenta con **0 ensayos clínicos** y **1 publicación** de relevancia indirecta que respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Betametasona y antibióticos |
| Nueva Indicación Predicha | Candidiasis cutánea |
| Puntaje de Predicción TxGNN | 99.84% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 3 (todos cancelados) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen información detallada sobre el mecanismo de acción. Según la información conocida, clioquinol es una 8-hidroxiquinolina halogenada con actividad antifúngica y antibacteriana, que se cree actúa quelando iones metálicos (cobre, zinc, hierro) esenciales para las enzimas y el crecimiento de los hongos.

En Colombia el clioquinol se comercializó en cremas tópicas combinadas con betametasona y antibióticos, es decir, ya se usaba sobre la piel como componente antimicrobiano. Una infección cutánea por *Candida* es un escenario cercano a ese uso, lo que hace plausible la predicción del modelo desde el punto de vista mecanístico.

Sin embargo, la plausibilidad es solo indirecta. La única publicación recuperada para esta indicación trata de la prevención de infección ocupacional por *Candida albicans* (con jabones), no de clioquinol en pacientes. El puntaje alto de TxGNN es una predicción del modelo y no está respaldado por datos clínicos directos.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [2978600](https://pubmed.ncbi.nlm.nih.gov/2978600/) | 1988 | Sin clasificar (probable estudio de prevención/salud ocupacional) | Przeglad dermatologiczny | Estudio in vitro de aditivos para jabones de tocador frente a cepas de *Candida albicans* aisladas de pacientes; relevancia indirecta para clioquinol |

Para otras indicaciones predichas, se identificó un estudio preclínico: [33772895](https://pubmed.ncbi.nlm.nih.gov/33772895/) (2021, *Mycoses*), que evaluó clioquinol combinado con ciclopirox y terbinafina en modelos alternativos de dermatofitosis (actividad antifúngica y potencial irritante). Respalda de forma indirecta la actividad antifúngica, sin datos de eficacia en humanos.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19972065 | BETAGEN CREMA TÓPICA | Crema tópica | Betametasona y antibióticos |
| 19972066 | DERMA - 3 CREMA | Crema tópica | Betametasona y antibióticos |
| 19994745 | DERMOCUAD CREMA | Crema tópica | Betametasona y antibióticos |

Los tres registros están cancelados; actualmente no hay registros vigentes.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** insuficiencia adrenocortical, enfermedad de Addison, atrofia cutánea, telangiectasia, enfermedad capilar, telangiectasia hemorrágica hereditaria, enfermedad vascular periférica, claudicación vascular intermitente y enfermedad arterial periférica. Varias de ellas probablemente se relacionan con el corticoide presente en las combinaciones (betametasona) más que con el clioquinol por sí solo, por lo que deben interpretarse con cautela.
- **Interacciones farmacológicas:** no se encontraron interacciones registradas en la consulta realizada.

Consultar el prospecto para información de seguridad adicional (advertencias y contraindicaciones oficiales).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para candidiasis cutánea tiene un puntaje alto, pero no hay ensayos clínicos y la única publicación es de relevancia indirecta (nivel L4). Además, no hay registros vigentes en Colombia y falta la información de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto en INVIMA (advertencias y contraindicaciones) para poder realizar el tamizaje de seguridad.
- Consultar los datos del mecanismo de acción en DrugBank.
- Buscar evidencia directa de clioquinol en candidiasis cutánea (estudios in vitro con *Candida* y ensayos clínicos).
- Aclarar la situación regulatoria: los registros están cancelados, por lo que se requeriría un nuevo registro o una nueva formulación.
- Evaluar la seguridad histórica del clioquinol, en particular con uso prolongado o extenso, y la compatibilidad de la vía tópica con la indicación.
- Las demás indicaciones predichas (infecciones dermatofíticas del pelo, granuloma de Majocchi, tinea profunda) tienen solo soporte del modelo (L5) y suelen requerir tratamiento sistémico, por lo que son menos prioritarias; la micosis superficial (L4) es la alternativa con algo de apoyo preclínico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

