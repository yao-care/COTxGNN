---
layout: default
title: Mitoxantrone
parent: Evidencia Alta (L1-L2)
nav_order: 451
evidence_level: L2
indication_count: 8
last_modified_at: 2026-10-14
description: "Mitoxantrone: nueva indicación predicha, Cáncer de cabeza y cuello (head and neck cancer) (nivel de evidencia L2). Indicación original: No especificada en el registro"
monitor_inn: "mitoxantrone"
predicted_indications: ["upper aerodigestive tract neoplasm", "small cell lung carcinoma", "primary pulmonary lymphoma", "well-differentiated fetal adenocarcinoma of the lung", "pulmonary blastoma", "head and neck cancer", "bladder exstrophy-epispadias-cloacal exstrophy complex"]
---

# Mitoxantrone
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

# Mitoxantrona: De Indicación No Especificada a Cáncer de Cabeza y Cuello

## Resumen en Una Frase

Mitoxantrona es un agente antineoplásico (antraquinona) con registro sanitario en Colombia en forma de solución inyectable, aunque el texto de indicación registrado no detalla la enfermedad original.
El modelo TxGNN predice que podría ser efectivo para **cáncer de cabeza y cuello** (la predicción con mayor respaldo clínico entre las candidatas), con **6 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto registrado solo indica "Mitoxantrona") |
| Nueva Indicación Predicha | Cáncer de cabeza y cuello (head and neck cancer) |
| Puntaje de Predicción TxGNN | 99.31% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Proceed with Guardrails |

**Nota sobre la selección de la indicación:** el modelo generó 8 predicciones. Se eligió el cáncer de cabeza y cuello (posición 7 por puntaje) por ser la que cuenta con mayor evidencia clínica real. La predicción de mayor puntaje, neoplasia del tracto aerodigestivo superior (99.78%), solo alcanza nivel L3, sin ensayos registrados. Las demás predicciones son de evidencia limitada o nula: cáncer de pulmón de células pequeñas (L4), linfoma pulmonar primario (L3), leucemia mieloide crónica BCR-ABL1 positiva (L2, pero con evidencia indirecta y limitada a crisis blástica), y tres predicciones L5 sin respaldo (adenocarcinoma fetal de pulmón, blastoma pulmonar y complejo extrofia vesical-epispadias), esta última sin plausibilidad mecanística.

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos consultada. Según la información conocida, mitoxantrona es un inhibidor de la topoisomerasa II e intercalador del ADN con actividad citotóxica contra tumores sólidos y hematológicos, con un mecanismo similar al de las antraciclinas.

La indicación original no puede determinarse a partir del registro colombiano. Aun así, el uso de mitoxantrona como antineoplásico es bien conocido y, en la literatura, la actividad contra tumores de cabeza y cuello ya había sido explorada desde los años 80 en ensayos de fase II (por ejemplo, PMID 6511239 y 1650529) y en carcinoma adenoide quístico (EORTC, PMID 8922205). Los resultados históricos fueron modestos: algunos estudios reportaron respuestas parciales aisladas y otros no hallaron actividad antitumoral significativa.

Hoy el interés se concentra en la formulación liposomal, con un estudio de fase Ib completado y ensayos de fase II y III en carcinoma nasofaríngeo. Esto hace razonable la predicción del modelo, aunque la eficacia aún debe confirmarse en ensayos controlados.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04902027](https://clinicaltrials.gov/study/NCT04902027) | Fase 1b | Completado | 45 | Mitoxantrona liposomal en cáncer de cabeza y cuello recurrente/metastásico; estudio multicéntrico de brazo único sobre seguridad y eficacia |
| [NCT05717764](https://clinicaltrials.gov/study/NCT05717764) | Fase 3 | Aún no recluta | 500 | Mitoxantrona liposomal + capecitabina vs. capecitabina sola en carcinoma nasofaríngeo recurrente/metastásico tras fracaso de platino |
| [NCT06472713](https://clinicaltrials.gov/study/NCT06472713) | Fase 2 | Reclutando | 32 | Mitoxantrona liposomal + bloqueo de PD-1 en carcinoma nasofaríngeo previamente tratado |
| [NCT06892431](https://clinicaltrials.gov/study/NCT06892431) | Fase 2 | Aún no recluta | 150 | JMT101 + mitoxantrona liposomal en carcinoma nasofaríngeo tras al menos dos líneas previas |
| [NCT07070479](https://clinicaltrials.gov/study/NCT07070479) | Fase 2 | Reclutando | 208 | Estudio adaptativo bayesiano con cuatro brazos en carcinoma nasofaríngeo resistente a PD-1; la mitoxantrona liposomal + anti-PD-1 es uno de ellos |
| [NCT07354698](https://clinicaltrials.gov/study/NCT07354698) | Fase 4 | Aún no recluta | 114 | Uso como trazador linfático en cirugía robótica transoral de cáncer de tiroides (uso de imagen, no antitumoral) |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39952083](https://pubmed.ncbi.nlm.nih.gov/39952083/) | 2025 | Estudio clínico fase 1b | Oral Oncology | Evalúa seguridad y eficacia de mitoxantrona liposomal (PLM60) en carcinoma escamoso de cabeza y cuello recurrente/metastásico |
| [8922205](https://pubmed.ncbi.nlm.nih.gov/8922205/) | 1996 | Ensayo fase II | Annals of Oncology | Estudio EORTC de mitoxantrona en carcinoma adenoide quístico de cabeza y cuello |
| [1650529](https://pubmed.ncbi.nlm.nih.gov/1650529/) | 1991 | Ensayo fase II | Am J Clin Oncol | 19 pacientes con carcinoma de cabeza y cuello; dosis ajustadas según nadir leucocitario |
| [11290867](https://pubmed.ncbi.nlm.nih.gov/11290867/) | 2001 | Ensayo fase II | Anti-Cancer Drugs | Ifosfamida + mitoxantrona en carcinoma escamoso recurrente/metastásico de cabeza y cuello |
| [12045460](https://pubmed.ncbi.nlm.nih.gov/12045460/) | 2002 | Ensayo fase II | Anti-Cancer Drugs | Mitoxantrona + cisplatino en tumores de glándulas salivales recurrentes/metastásicos (14 pacientes) |
| [6511243](https://pubmed.ncbi.nlm.nih.gov/6511243/) | 1984 | Ensayo fase II | Invest New Drugs | Southwest Oncology Group: sin actividad antitumoral significativa en carcinoma escamoso avanzado (1 respuesta parcial en 22 pacientes) |
| [4066226](https://pubmed.ncbi.nlm.nih.gov/4066226/) | 1985 | Ensayo fase II | Invest New Drugs | Southeastern Cancer Study Group: 53 pacientes evaluables con carcinoma escamoso avanzado |
| [34659878](https://pubmed.ncbi.nlm.nih.gov/34659878/) | 2021 | Revisión | Am J Cancer Res | Terapias sistémicas para el carcinoma adenoide quístico de glándulas salivales |
| [31324333](https://pubmed.ncbi.nlm.nih.gov/31324333/) | 2019 | Revisión sistemática | Bulletin du Cancer | Tratamientos sistémicos del carcinoma adenoide quístico de cabeza y cuello metastásico o recurrente |
| [1735075](https://pubmed.ncbi.nlm.nih.gov/1735075/) | 1992 | Estudio farmacocinético | Cancer | Farmacocinética y farmacodinamia en 15 pacientes con carcinoma nasofaríngeo avanzado |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20063702 (cancelado) | MITOXANTRONA 20 MG / 10 ML (Blau Farmacéutica Colombia S.A.S.) | Solución inyectable | MITOXANTRONA |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (inhibidor de topoisomerasa II / intercalador del ADN, antraquinona similar a las antraciclinas) |
| Riesgo de Mielosupresión | Alto: la leucopenia y la trombocitopenia son toxicidades principales descritas en los estudios de fase II |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Ítems de Monitoreo | Hemograma con diferencial, función hepática y renal, y fracción de eyección del ventrículo izquierdo (LVEF) por cardiotoxicidad acumulativa |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas por el grafo de conocimiento (no provienen del prospecto):** insuficiencia hepática, enfermedad hepática, enfermedad de la vesícula biliar, insuficiencia cardíaca, trombocitopenia, neutropenia, agranulocitosis, leucopenia, anemia (incluida la macrocítica), epilepsia, enfermedades infecciosas (incluidas las fúngicas y la dermatofitosis).
- **Interacciones farmacológicas:** se identificaron 355 interacciones. Entre las principales:
  - Mayor: dolasetrón.
  - Moderada: claritromicina, eliglustat, rolapitant.
  - Menor: levofloxacino.
  - Otras con nivel no clasificado: metformina, lansoprazol, anfotericina B, hidrocortisona, omeprazol, pantoprazol, morfina y otras.
- **Riesgos señalados en el análisis de la predicción:** cardiotoxicidad acumulativa, mielosupresión y riesgo de leucemia secundaria.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen estudios históricos de fase II con resultados mixtos y, sobre todo, ensayos modernos con formulación liposomal (fase Ib completada, fase II en curso y fase III planificada) en cáncer de cabeza y cuello, en especial carcinoma nasofaríngeo. La evidencia es suficiente para continuar la evaluación, pero la eficacia aún no está confirmada en ensayos controlados, y el único registro local está cancelado.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto del INVIMA (advertencias y contraindicaciones), una brecha bloqueante para el tamizaje de seguridad.
- Complementar los datos del mecanismo de acción desde DrugBank.
- Esperar los resultados de los ensayos de fase II y III con mitoxantrona liposomal; la formulación liposomal no está registrada en Colombia, por lo que habría que evaluar su disponibilidad.
- Definir un plan de monitoreo cardíaco (LVEF), hematológico y de interacciones farmacológicas.
- Evaluar la vía regulatoria dado que no hay registros vigentes en Colombia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

