---
layout: default
title: Levofloxacin
parent: Solo Predicción del Modelo (L5)
nav_order: 400
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Levofloxacin: nueva indicación predicha, Queratoconjuntivitis epitelial punteada (nivel de evidencia L5). Indicación original: Levofloxacino"
monitor_inn: "Levofloxacin"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder"]
---

# Levofloxacin
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

# Levofloxacino: De Infecciones Bacterianas (Registro INVIMA) a Queratoconjuntivitis Epitelial Punteada

## Resumen en Una Frase

Levofloxacino es una fluoroquinolona antibacteriana cuyos registros sanitarios en Colombia figuran con el nombre del principio activo, sin un texto de indicación detallado.
El modelo TxGNN predice que podría ser efectivo para **queratoconjuntivitis epitelial punteada**, pero no hay ensayos clínicos y solo existe **1 publicación** (un informe de brote por microsporidios, sin respaldo clínico para levofloxacino). La predicción se apoya únicamente en el modelo computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Levofloxacino (el registro INVIMA solo menciona el nombre del principio activo, sin indicación detallada) |
| Nueva Indicación Predicha | Queratoconjuntivitis epitelial punteada |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 4 (todos cancelados) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, levofloxacino es una fluoroquinolona de amplio espectro que inhibe la ADN girasa y la topoisomerasa IV bacterianas, y se utiliza en infecciones bacterianas, incluidas infecciones oculares.

La predicción probablemente refleja la cercanía en la red de conocimiento con indicaciones de infección ocular. Sin embargo, el único artículo recuperado trata de un brote de queratoconjuntivitis microsporidial asociado a agua contaminada en piscinas en Taiwán. Los microsporidios no son bacterias y no son susceptibles a la inhibición de la girasa bacteriana, por lo que no existe sustento mecanístico ni clínico que respalde a levofloxacino en esta condición.

Por lo tanto, el puntaje alto del modelo debe interpretarse con cautela: es una señal computacional, no una evidencia de eficacia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [30055152](https://pubmed.ncbi.nlm.nih.gov/30055152/) | 2018 | Informe de brote | American Journal of Ophthalmology | Brote de queratoconjuntivitis microsporidial asociado a contaminación del agua en piscinas en Taiwán; no aporta evidencia sobre levofloxacino |

## Información de Mercado en Colombia

Todos los registros sanitarios están cancelados.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20134443 | LANDAX | Solución oftálmica | Levofloxacino |
| 20087579 | LEQUIBAC® | Tableta cubierta con película | Levofloxacina |
| 20094747 | PRINF® 750 MG TABLETAS RECUBIERTAS | Tableta recubierta | Levofloxacina |
| 20077633 | AVOSAL® | Tableta recubierta | Levofloxacina |

## Consideraciones de Seguridad

No se dispone de texto de advertencias ni contraindicaciones del prospecto. A continuación se presentan datos del grafo de conocimiento (no provienen del prospecto).

- **Contraindicaciones o condiciones de riesgo según el grafo de conocimiento**: síndrome de QT largo (incluido el familiar), torsades de pointes, epilepsia, enfermedad hepática y lesión hepática inducida por fármacos, enfermedad de la vesícula biliar, trombocitopenia, leucopenia, pancitopenia, anemia, deficiencia de potasio, tendinitis y otras afecciones de tendones, diabetes mellitus y cetoacidosis diabética, neuropatía periférica, rabdomiólisis, colitis por *Clostridium difficile*, insuficiencia renal, miastenia gravis y enfermedades de la unión neuromuscular, isquemia miocárdica y enfermedad coronaria.
- **Interacciones farmacológicas**: se identificaron 100 interacciones. Entre las de nivel **mayor** figuran **tramadol** e **hidrocortisona**. Entre las de nivel moderado se encuentran abiraterona, acarbosa, famotidina, formoterol, ketorolaco, adenosina, ibuprofeno, etinilestradiol, albiglutida, salbutamol, alfuzosina, alogliptina, metformina, pioglitazona y amifampridina. Entre las de nivel menor: paclitaxel, aldesleukina y altretamina.

Consultar el prospecto para confirmar la información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para queratoconjuntivitis epitelial punteada solo cuenta con respaldo computacional (L5): no hay ensayos clínicos, y la única publicación trata de una infección por microsporidios, frente a los cuales las fluoroquinolonas no tienen actividad esperada. Además, los 4 registros sanitarios en Colombia están cancelados.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y del prospecto (advertencias y contraindicaciones), actualmente no disponibles.
- Evidencia clínica o preclínica que demuestre actividad de levofloxacino en esta condición; de lo contrario, la señal debe tratarse como un artefacto del modelo.
- Confirmar la situación regulatoria en Colombia (registros cancelados, incluida la presentación oftálmica).

**Otras predicciones del modelo con evidencia (para referencia):**
- **Gammapatía monoclonal** (puntaje 99.81%): existe un ECA de Fase 3 (TEAMM, PMID 31668592) sobre profilaxis con levofloxacino, pero en mieloma múltiple sintomático. No es extrapolable a la gammapatía monoclonal premaligna, por lo que se considera una pregunta de investigación.
- **Peste septicémica** (puntaje 99.80%): levofloxacino está aprobado por la FDA para peste bajo la Regla de Eficacia Animal, con evidencia principalmente en modelos animales. Es un uso antibacteriano real, no un reposicionamiento novedoso.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

