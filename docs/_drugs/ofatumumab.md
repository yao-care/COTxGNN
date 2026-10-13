---
layout: default
title: Ofatumumab
parent: Evidencia Alta (L1-L2)
nav_order: 478
evidence_level: L2
indication_count: 8
---

# Ofatumumab
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **8** 
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

# Ofatumumab: De la indicación registrada (ofatumumab) a Linfoma Folicular

## Resumen en Una Frase

Ofatumumab es un anticuerpo monoclonal anti-CD20 registrado en Colombia como KESIMPTA (solución inyectable), cuyo registro sanitario figura actualmente como cancelado.
El modelo TxGNN predice que podría ser efectivo para **linfoma folicular**, con **11 ensayos clínicos** y **20 publicaciones** que respaldan esta dirección (principalmente estudios de Fase 2).
Esta es la nueva indicación con mejor equilibrio entre evidencia y novedad; la leucemia linfocítica crónica (LLC/LLP) tiene más evidencia, pero corresponde al uso oncológico ya establecido del fármaco.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Ofatumumab (el registro sanitario no detalla una indicación específica) |
| Nueva Indicación Predicha | Linfoma folicular |
| Puntaje de Predicción TxGNN | 99,70 % |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 1 (0 vigentes, 1 cancelado) |
| Decisión Recomendada | Proceed with Guardrails |

**Nota sobre la selección de la indicación principal:** las dos primeras predicciones del modelo (subtipos moleculares de LLC/LLP) tienen puntajes ligeramente superiores, pero carecen de ensayos y literatura propios (nivel L5, Hold). El linfoma folicular es la primera predicción con evidencia clínica sustancial, y por eso se desarrolla en este informe.

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos consultada. Según la información conocida, ofatumumab es un anticuerpo monoclonal humano dirigido contra CD20, una proteína de superficie de los linfocitos B. Se une a un epítopo distinto y cercano a la membrana, y destruye las células B mediante citotoxicidad dependiente del complemento (CDC) y citotoxicidad celular dependiente de anticuerpos (ADCC).

Las células del linfoma folicular expresan CD20, por lo que el objetivo farmacológico está presente. Los ensayos de Fase 2 (en monoterapia y en combinación con quimioterapia o bortezomib) y un estudio multicéntrico en enfermedad refractaria a rituximab respaldan su actividad clínica.

Conviene matizar: el linfoma folicular pertenece a la misma familia de neoplasias de células B que la LLC, la indicación hematológica mejor establecida de ofatumumab. Por ello se trata de un reposicionamiento de baja novedad dentro de la misma clase y enfermedad. Además, el estado de mercado (solo registro cancelado) limita el desarrollo práctico en Colombia.

---

## Evidencia de Ensayos Clínicos

Se muestran los 10 ensayos más relevantes para linfoma folicular (de 11 registrados):

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01077518](https://clinicaltrials.gov/study/NCT01077518) | Fase 3 | Terminado | 346 | Ofatumumab + bendamustina vs. bendamustina sola en linfoma indolente de células B no respondedor a rituximab |
| [NCT01286272](https://clinicaltrials.gov/study/NCT01286272) | Fase 2 | Completado | 135 | Aleatorizado: ofatumumab + bendamustina con o sin bortezomib en linfoma folicular sin tratamiento previo |
| [NCT00394836](https://clinicaltrials.gov/study/NCT00394836) | Fase 2 | Completado | 116 | Brazo único multicéntrico en linfoma folicular refractario a rituximab |
| [NCT02710643](https://clinicaltrials.gov/study/NCT02710643) | Fase 2 | Completado | 110 | Estudio MIRO: radioterapia local con o sin ofatumumab en linfoma folicular estadio I/II |
| [NCT00823719](https://clinicaltrials.gov/study/NCT00823719) | Fase 2 | Completado | 61 | Ofatumumab con ICE o DHAP en linfoma agresivo en recaída/refractario antes del trasplante autólogo |
| [NCT00494780](https://clinicaltrials.gov/study/NCT00494780) | Fase 2 | Completado | 59 | Aleatorizado de dos dosis de ofatumumab + CHOP en linfoma folicular sin tratamiento previo |
| [NCT01190449](https://clinicaltrials.gov/study/NCT01190449) | Fase 2 | Completado | 51 | Ofatumumab en linfoma folicular no Hodgkin sin tratamiento previo |
| [NCT01239394](https://clinicaltrials.gov/study/NCT01239394) | Fase 2 | Completado | 43 | Tratamiento inicial del linfoma indolente de células B (población más amplia que el linfoma folicular) |
| [NCT01119794](https://clinicaltrials.gov/study/NCT01119794) | Fase 2 | Terminado | 10 | Ofatumumab + bortezomib en linfoma de bajo grado en recaída; muestra demasiado pequeña |
| [NCT00742144](https://clinicaltrials.gov/study/NCT00742144) | Fase 1 | Completado | 6 | Seguridad y tolerabilidad en pacientes japoneses con linfoma folicular o LLC |

Otros dos ensayos (NCT01397591, terminado con 3 pacientes, y NCT01263418, retirado sin inscripción) no aportan evidencia.

---

## Evidencia de Literatura

Se muestran las 10 publicaciones más relevantes (de 20), priorizando ensayos clínicos sobre revisiones:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31174236](https://pubmed.ncbi.nlm.nih.gov/31174236/) | 2019 | ECA (Fase 2) | Cancer | CALGB 50904: ofatumumab + bendamustina con o sin bortezomib en linfoma folicular de alto riesgo sin tratamiento previo |
| [22409295](https://pubmed.ncbi.nlm.nih.gov/22409295/) | 2012 | Fase 2 (aleatorizado, dos dosis) | Br J Haematol | Ofatumumab + CHOP (O-CHOP) como tratamiento de primera línea en 59 pacientes con linfoma folicular |
| [22389254](https://pubmed.ncbi.nlm.nih.gov/22389254/) | 2012 | Estudio multicéntrico de brazo único | Blood | Monoterapia con ofatumumab en 116 pacientes con linfoma folicular refractario a rituximab; tasa de respuesta global de 10-13 % |
| [30723894](https://pubmed.ncbi.nlm.nih.gov/30723894/) | 2019 | Fase 2 | Br J Haematol | CALGB 50901: ofatumumab en monoterapia en linfoma folicular sin tratamiento previo |
| [38937025](https://pubmed.ncbi.nlm.nih.gov/38937025/) | 2024 | Fase 2 | Lancet Haematol | FIL MIRO: radioterapia local e inmunoterapia guiada por enfermedad residual medible en linfoma folicular temprano |
| [18390837](https://pubmed.ncbi.nlm.nih.gov/18390837/) | 2008 | Fase 1/2 | Blood | Primer uso clínico de ofatumumab en linfoma folicular en recaída/refractario |
| [24443277](https://pubmed.ncbi.nlm.nih.gov/24443277/) | 2014 | Farmacocinética poblacional | J Clin Pharmacol | Farmacocinética de ofatumumab en LLC, linfoma folicular y artritis reumatoide (477 pacientes) |
| [26043777](https://pubmed.ncbi.nlm.nih.gov/26043777/) | 2015 | Revisión | Expert Opin Biol Ther | Actividad de ofatumumab en linfomas no Hodgkin de células B CD20+ |
| [29934061](https://pubmed.ncbi.nlm.nih.gov/29934061/) | 2018 | Revisión basada en evidencia | Clin Lymphoma Myeloma Leuk | Regímenes con anticuerpos anti-CD20 en LLC, LDCBG y linfoma folicular en recaída/refractarios |
| [35663281](https://pubmed.ncbi.nlm.nih.gov/35663281/) | 2022 | Revisión | Leuk Res Rep | Inmunoterapia en linfomas no Hodgkin indolentes |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20190663 (cancelado) | KESIMPTA | Solución inyectable | OFATUMUMAB |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Inmunoterapia (anticuerpo monoclonal anti-CD20) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal, recuento de linfocitos B y niveles de inmunoglobulinas |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas:** se identificaron 80 interacciones potenciales. Entre las de gravedad **mayor** figuran: deferiprona, samario (153Sm) lexidronam, adalimumab, baricitinib, certolizumab pegol, cladribina y clozapina. Entre las de gravedad **moderada**: estroncio-89, roflumilast, cloranfenicol, zidovudina, alemtuzumab, anakinra, azatioprina, canakinumab, alefacept, y varias vacunas (toxoide tetánico, ántrax, cólera vivo). La mayoría se relaciona con inmunosupresión aditiva o riesgo de mielosupresión, y las vacunas vivas o inactivadas pueden tener una respuesta reducida.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen múltiples ensayos de Fase 2 completados (incluidos ECA publicados) y un estudio multicéntrico que respaldan la actividad de ofatumumab en linfoma folicular, con nivel de evidencia L2. No hay un ECA de Fase 3 con resultados específicos para esta indicación, y el único registro colombiano está cancelado, lo que limita la viabilidad práctica.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), un vacío de datos que bloquea el tamizaje de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Revisar los resultados del ensayo de Fase 3 NCT01077518 (ofatumumab + bendamustina, terminado) y los estudios de brazo único para estimar el beneficio real.
- Aclarar la situación regulatoria: reactivar o tramitar un nuevo registro sanitario en Colombia, ya que el único registro está cancelado (y KESIMPTA corresponde a una presentación subcutánea orientada a esclerosis múltiple, no a oncología).
- Definir un plan de manejo de interacciones (inmunosupresores, vacunas) y de monitoreo de seguridad en poblaciones específicas.

**Otras predicciones del modelo (para referencia):**
- **LLC/LLP (nivel L1, Proceed with Guardrails):** evidencia sólida con ensayos de Fase 3 (DUO, RESONATE), pero ofatumumab fue comparador y corresponde a su uso oncológico establecido, no a un reposicionamiento novedoso.
- **Subtipos de LLC/LLP, linfoma espiradenoma maligno, histiocitosis de células de Langerhans (nivel L5, Hold):** solo predicción computacional, sin ensayos ni literatura.
- **Leucemia linfocítica, susceptibilidad (L4, Hold):** término de susceptibilidad genética que corresponde a la biología de la LLC; sin ensayos propios.
- **Neoplasia metastásica (L3, pregunta de investigación):** solo un piloto de Fase 2 (n=10) en melanoma; término inespecífico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

