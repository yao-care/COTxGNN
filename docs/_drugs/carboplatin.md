---
layout: default
title: Carboplatin
parent: Evidencia Alta (L1-L2)
nav_order: 137
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-14
description: "Carboplatin: nueva indicación predicha, Carcinoma de mama femenino (nivel de evidencia L2). Indicación original: Carboplatino"
---

# Carboplatin
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **10** 
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

# Carboplatino: De Indicación Original (Carboplatino) a Carcinoma de Mama Femenino

## Resumen en Una Frase

Carboplatino es un agente antineoplásico a base de platino, registrado en Colombia con la indicación genérica "carboplatino" (el texto del registro no detalla la enfermedad).
El modelo TxGNN predice que podría ser efectivo para **carcinoma de mama femenino**, con **41 ensayos clínicos** y **20 publicaciones** compilados para esta indicación, incluidos varios ensayos aleatorizados de Fase 2 y 3.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Carboplatino (el registro sanitario no especifica la enfermedad) |
| Nueva Indicación Predicha | Carcinoma de mama femenino |
| Puntaje de Predicción TxGNN | 99.86% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registro vigente) |
| Número de Registros Sanitarios | 4 (todos cancelados) |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, carboplatino es un agente de platino que entrecruza el ADN y provoca daño que lleva a la muerte de las células tumorales.

Los tumores con deficiencia de recombinación homóloga (mutaciones BRCA1/2 o cáncer de mama triple negativo) son especialmente sensibles al daño del ADN inducido por platino. Esto explica por qué agregar carboplatino a los esquemas estándar aumenta la tasa de respuesta patológica completa en estudios neoadyuvantes como GeparSixto y CALGB 40603.

Dado que el fármaco ya se usa clínicamente en cáncer de mama, esta predicción se entiende mejor como una ampliación u optimización de un uso existente que como un reposicionamiento totalmente novedoso.

---

## Evidencia de Ensayos Clínicos

Se muestran los ensayos más relevantes (de 41 compilados):

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00321633](https://clinicaltrials.gov/study/NCT00321633) | Fase 2 | Completado | 148 | Carboplatino vs docetaxel en cáncer de mama metastásico con mutación genética (BRCA); aleatorizado |
| [NCT00616967](https://clinicaltrials.gov/study/NCT00616967) | Fase 2 | Activo, no recluta | 68 | Carboplatino + nab-paclitaxel con o sin vorinostat, preoperatorio en cáncer de mama HER2 negativo |
| [NCT00021255](https://clinicaltrials.gov/study/NCT00021255) | Fase 3 | Completado | 3222 | AC-T vs AC-TH vs TCH (docetaxel, carboplatino, trastuzumab) adyuvante en HER2 positivo |
| [NCT00047255](https://clinicaltrials.gov/study/NCT00047255) | Fase 3 | Completado | 263 | Docetaxel + trastuzumab con o sin carboplatino en cáncer de mama avanzado HER2 positivo |
| [NCT02125344](https://clinicaltrials.gov/study/NCT02125344) | Fase 3 | Completado | 961 | GeparOcto: dos estrategias neoadyuvantes intensificadas, una con carboplatino, en cáncer de mama temprano de alto riesgo |
| [NCT00025688](https://clinicaltrials.gov/study/NCT00025688) | Fase 3 | Desconocido | N/D | Paclitaxel semanal con o sin carboplatino en mayores de 65 años con cáncer metastásico |
| [NCT01208480](https://clinicaltrials.gov/study/NCT01208480) | Fase 2 | Completado | 45 | Bevacizumab, docetaxel y carboplatino neoadyuvantes en cáncer de mama triple negativo |
| [NCT00003612](https://clinicaltrials.gov/study/NCT00003612) | Fase 2 | Completado | 92 | Paclitaxel, carboplatino y trastuzumab de primera línea en cáncer metastásico HER2 positivo |
| [NCT06291064](https://clinicaltrials.gov/study/NCT06291064) | Fase 2 | Reclutando | 85 | Respuesta y biomarcadores en cáncer de mama triple negativo con quimioterapia estándar que incluye docetaxel + carboplatino (Nigeria) |
| [NCT05020860](https://clinicaltrials.gov/study/NCT05020860) | Fase 2 | Reclutando | 185 | Correlación entre respuesta clínica y patológica con terapia sistémica neoadyuvante en cáncer de mama temprano |

---

## Evidencia de Literatura

Se muestran las publicaciones más relevantes (de 20 compiladas), priorizando ensayos aleatorizados:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [24794243](https://pubmed.ncbi.nlm.nih.gov/24794243/) | 2014 | ECA (Fase 2) | The Lancet Oncology | GeparSixto: carboplatino neoadyuvante en cáncer de mama triple negativo y HER2 positivo |
| [29501363](https://pubmed.ncbi.nlm.nih.gov/29501363/) | 2018 | ECA (Fase 3) | The Lancet Oncology | BrighTNess: veliparib más carboplatino o carboplatino solo añadido a quimioterapia neoadyuvante estándar en triple negativo |
| [35044810](https://pubmed.ncbi.nlm.nih.gov/35044810/) | 2022 | ECA (Fase 2) | J Clin Oncol | CALGB 40603: resultados a largo plazo con o sin carboplatino y bevacizumab en triple negativo |
| [33208340](https://pubmed.ncbi.nlm.nih.gov/33208340/) | 2021 | ECA (Fase 2) | Clin Cancer Res | NeoSTOP: esquemas neoadyuvantes con carboplatino, con y sin antraciclina, en triple negativo |
| [41436191](https://pubmed.ncbi.nlm.nih.gov/41436191/) | 2025 | ECA (Fase 3) | BMJ | CITRINE: quimioterapia adyuvante intensificada con carboplatino vs estándar en triple negativo de alto riesgo |
| [41115255](https://pubmed.ncbi.nlm.nih.gov/41115255/) | 2026 | ECA (Fase 3) | J Clin Oncol | Adición de carboplatino a quimioterapia neoadyuvante secuencial taxano-antraciclina en triple negativo |
| [29175149](https://pubmed.ncbi.nlm.nih.gov/29175149/) | 2018 | ECA (Fase 3) | The Lancet Oncology | KRISTINE: trastuzumab, pertuzumab y quimioterapia vs T-DM1 más pertuzumab en HER2 positivo |
| [39631485](https://pubmed.ncbi.nlm.nih.gov/39631485/) | 2024 | Revisión | Pharmacological Research | Inhibidores dirigidos y citotóxicos usados en cáncer de mama |
| [16720915](https://pubmed.ncbi.nlm.nih.gov/16720915/) | 2006 | Revisión | Medical Oncology | Evidencia de sinergia, eficacia y seguridad de paclitaxel-carboplatino en cáncer de mama avanzado |
| [38705336](https://pubmed.ncbi.nlm.nih.gov/38705336/) | 2024 | Preclínico | Int J Biol Macromol | Nanopartículas para coadministrar carboplatino y doxorrubicina en células de cáncer de mama |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19974848 | Carboplatino 450 mg inyectable 450mg/45ml | Solución inyectable | Carboplatino (cancelado) |
| 19941539 | Oncocarb 150 mg/15 ml | Solución inyectable | Carboplatino (cancelado) |
| 19982073 | Carboplatino 450mg/45ml solución inyectable | Solución inyectable | Carboplatino (cancelado) |
| 20215154 | Carbohet® 10 mg/ml solución concentrada para infusión | Solución concentrada para infusión | Carboplatino (cancelado) |

Los cuatro registros figuran como cancelados; no hay registro vigente.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (clase platino, agente alquilante tipo entrecruzador de ADN) |
| Riesgo de Mielosupresión | Alto (las contraindicaciones del grafo de conocimiento señalan trombocitopenia, neutropenia, leucopenia, anemia y agranulocitosis) |
| Clasificación de Emetogenicidad | Media a alta, según la categoría del fármaco |
| Items de Monitoreo | Hemograma con diferencial y plaquetas, función renal y hepática, electrolitos, audiometría y evaluación neurológica |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos (preparación en cabina, EPP) |

---

## Consideraciones de Seguridad

- **Contraindicaciones relacionadas (grafo de conocimiento, no texto del prospecto)**: enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia, neutropenia, agranulocitosis, leucopenia, anemia (incluida la macrocítica), trastornos de la coagulación sanguínea, neuropatía periférica y enfermedades del sistema nervioso periférico, trastornos de la audición, pérdida funcional de la visión y piouréter.
- **Interacciones Farmacológicas**: se identificaron 488 interacciones. Entre las de nivel moderado destacan los aminoglucósidos (kanamicina, neomicina, estreptomicina) y la vancomicina, con posible suma de toxicidad renal y auditiva; los inhibidores de la bomba de protones (omeprazol, esomeprazol, lansoprazol, dexlansoprazol, pantoprazol, rabeprazol); metronidazol y tinidazol; y las estatinas (rosuvastatina, simvastatina). Levofloxacino figura como interacción menor.

Consultar el prospecto para advertencias y contraindicaciones oficiales, ya que no se dispone del texto del prospecto de INVIMA.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen múltiples ensayos aleatorizados de Fase 2 y Fase 3 con carboplatino en cáncer de mama, especialmente en subtipos triple negativo y HER2 positivo. Sin embargo, el carboplatino ya forma parte de la práctica clínica en esta enfermedad, y en Colombia no hay registro sanitario vigente.

**Para avanzar se necesita:**
- Revisar los resultados de supervivencia del ensayo de Fase 3 CITRINE (PMID 41436191) y de PMID 41115255 para confirmar la elevación a nivel L1.
- Obtener el prospecto de INVIMA (advertencias y contraindicaciones) y los datos del mecanismo de acción desde DrugBank.
- Definir la situación regulatoria: ningún registro vigente en Colombia, por lo que habría que reactivar o solicitar un nuevo registro.
- Establecer un plan de monitoreo hematológico, renal, auditivo y neurológico, y revisar las interacciones con aminoglucósidos y otros nefrotóxicos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

