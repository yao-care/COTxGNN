---
layout: default
title: Bupropion
parent: Evidencia Alta (L1-L2)
nav_order: 122
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-28
description: "Bupropion: nueva indicación predicha, Trastorno por déficit de atención e hiperactividad (TDAH) (nivel de evidencia L5). Indicación original: BUPROPION"
monitor_inn: "bupropion"
predicted_indications: ["attention deficit-hyperactivity disorder", "attention deficit hyperactivity disorder, inattentive type", "faciodigitogenital syndrome", "specific developmental disorder", "chondromyxoid fibroma", "proximal 16p11.2 microdeletion syndrome", "hypervitaminosis", "benign paroxysmal torticollis of infancy", "trigeminal nerve neoplasm", "obsolete hypertelorism (disease)"]
---

# Bupropion
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **10** 
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

## Bupropión: De Indicación Registrada (Bupropión) a Trastorno por Déficit de Atención e Hiperactividad (TDAH)
{: .text-alpha }

## Resumen en Una Frase

Bupropión es un fármaco antidepresivo de liberación prolongada que contó con registros sanitarios en Colombia (WELLBUTRIN® XL y BUPRION®), actualmente todos cancelados.
El modelo TxGNN predice que podría ser efectivo para el **trastorno por déficit de atención e hiperactividad (TDAH)**,
con **6 ensayos clínicos** (uno de ellos de Fase 3 completado) y **20 publicaciones** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | BUPROPION (el registro sanitario no detalla una indicación específica) |
| Nueva Indicación Predicha | Trastorno por déficit de atención e hiperactividad (TDAH) |
| Puntaje de Predicción TxGNN | 0.9999 |
| Nivel de Evidencia | L2 (ver nota abajo) |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 3) |
| Número de Registros Sanitarios | 3 (todos cancelados) |
| Decisión Recomendada | Proceed with Guardrails |

**Nota sobre el nivel de evidencia:** Según las reglas, L1 exige al menos 2 ECA de Fase 3 completados. Solo un ensayo de Fase 3 (NCT00048360) está completado, y el ensayo de Fase 2/3 (NCT00061087) también está completado. Esto corresponde a L2 de forma estricta. El análisis automático de los datos asignó L1; aquí se aplica la regla de forma conservadora, y además hay que confirmar si bupropión fue el agente evaluado en ambos ensayos.

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la literatura revisada, bupropión inhibe la recaptación de noradrenalina y dopamina, sin actividad serotoninérgica relevante, y se usa como antidepresivo y para la cesación tabáquica.

Los tratamientos establecidos para el TDAH actúan sobre las mismas vías catecolaminérgicas (dopamina y noradrenalina). Esto ofrece un mecanismo plausible para mejorar la atención y el control de impulsos. Las revisiones sobre farmacoterapia del TDAH incluyen a bupropión entre los fármacos usados como alternativa a los estimulantes, y existe una revisión Cochrane específica sobre bupropión en adultos con TDAH.

La alta puntuación de TxGNN (0.9999) es coherente con este solapamiento mecanístico. La relación con la indicación original (depresión y otros usos del mismo fármaco) es de vecindad neuropsiquiátrica: ambas condiciones involucran disfunción catecolaminérgica.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00048360](https://clinicaltrials.gov/study/NCT00048360) | Fase 3 | Completado | 162 | Ensayo aleatorizado, doble ciego, controlado con placebo, de 8 semanas, con bupropión de liberación prolongada 300-450 mg/día en adultos con TDAH (verificar comparador exacto) |
| [NCT00061087](https://clinicaltrials.gov/study/NCT00061087) | Fase 2/3 | Completado | 115 | Tratamiento del TDAH adulto en pacientes en mantenimiento con metadona (confirmar que bupropión fue el agente evaluado) |
| [NCT00936299](https://clinicaltrials.gov/study/NCT00936299) | Fase 4 | Completado | 105 | Bupropión para TDAH en adolescentes con trastorno por uso de sustancias |
| [NCT01270555](https://clinicaltrials.gov/study/NCT01270555) | No aplica | Completado | 32 | Estudio abierto de bupropión SR en adultos con TDAH y trastornos por uso de sustancias recientes o actuales |
| [NCT00000268](https://clinicaltrials.gov/study/NCT00000268) | No aplica | Completado | 32 | Abuso de cocaína y trastorno por déficit de atención; enfoque principal en el abuso de cocaína |
| [NCT04553263](https://clinicaltrials.gov/study/NCT04553263) | Fase 1 temprana | Retirado | 0 | Prevención de recaídas en trastorno por uso de estimulantes; sin datos utilizables sobre TDAH |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [30097390](https://pubmed.ncbi.nlm.nih.gov/30097390/) | 2018 | Revisión sistemática / metaanálisis en red | The Lancet Psychiatry | Eficacia y tolerabilidad comparada de medicamentos para TDAH en niños, adolescentes y adultos |
| [33085721](https://pubmed.ncbi.nlm.nih.gov/33085721/) | 2020 | Revisión sistemática / metaanálisis en red | PLoS One | Efectos relativos de tratamientos farmacológicos para TDAH en adultos |
| [28965364](https://pubmed.ncbi.nlm.nih.gov/28965364/) | 2017 | Revisión sistemática (Cochrane) | Cochrane Database Syst Rev | Bupropión para TDAH en adultos, como alternativa cuando los estimulantes no se toleran o no responden |
| [40203844](https://pubmed.ncbi.nlm.nih.gov/40203844/) | 2025 | Revisión sistemática / metaanálisis en red | The Lancet Psychiatry | Seguridad cardiovascular comparada de los medicamentos para TDAH |
| [27738872](https://pubmed.ncbi.nlm.nih.gov/27738872/) | 2017 | Metaanálisis en red | Molecular Neurobiology | Eficacia y seguridad de tratamientos para TDAH en niños y adolescentes |
| [37405312](https://pubmed.ncbi.nlm.nih.gov/37405312/) | 2023 | Revisión | Health Psychology Research | Efectos farmacocinéticos y farmacodinámicos de bupropión en depresión, TDAH y cesación tabáquica |
| [38915262](https://pubmed.ncbi.nlm.nih.gov/38915262/) | 2024 | Revisión | Expert Review of Neurotherapeutics | Medicamentos no estimulantes para adultos con TDAH |
| [39172673](https://pubmed.ncbi.nlm.nih.gov/39172673/) | 2024 | Revisión | American Family Physician | Diagnóstico y manejo del TDAH en adultos |
| [26601963](https://pubmed.ncbi.nlm.nih.gov/26601963/) | 2016 | Revisión | Current Pharmaceutical Design | Efectos y efectos adversos de la psicofarmacología del TDAH; incluye bupropión entre los fármacos usados |
| [32845025](https://pubmed.ncbi.nlm.nih.gov/32845025/) | 2021 | Revisión sistemática / metaanálisis | J Child Psychol Psychiatry | Tratamiento farmacológico de síntomas de TDAH en niños y jóvenes con trastorno del espectro autista |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19967275 | WELLBUTRIN® XL 150 MG | Tableta de liberación prolongada | BUPROPION (vigente) |
| 19967276 | WELLBUTRIN® XL 300 MG | Tableta de liberación prolongada | BUPROPION (vigente) |
| 20058938 | BUPRION® 150 MG | Tableta de liberación prolongada | BUPROPION (vigente) |

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento (no provienen del prospecto):** epilepsia, hipertensión, insuficiencia y enfermedad hepática (incluida cirrosis), enfermedad renal, trastorno bipolar maníaco, trastornos psicóticos (esquizoafectivo, esquizofreniforme), anorexia y bulimia nerviosa, trastornos de ansiedad, abuso de sustancias y dependencia de opiáceos, infarto de miocardio, enfermedad de la vesícula biliar, hemoglobinopatías y neoplasias del sistema nervioso central.
- **Interacciones farmacológicas:** se identificaron 665 interacciones. Entre las de nivel **mayor** figuran fentanilo, lidocaína, codeína, dihidrocodeína, tramadol, alfentanilo, metilfenidato, hidrocortisona, aldesleucina y amantadina. Entre las de nivel moderado: nifedipino, hidroclorotiazida, cetirizina, alprazolam, alfuzosina, acebutolol, clorfeniramina, alpelisib, abametapir (tópico) y etanol. Se señala además inhibición de CYP2D6.
- **Puntos de vigilancia:** riesgo de convulsiones, efectos sobre la presión arterial y la frecuencia cardíaca, y monitoreo del uso de sustancias en pacientes con comorbilidad.

El prospecto no estuvo disponible en los datos compilados; consultar el prospecto para las advertencias oficiales.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un ensayo de Fase 3 completado, otro de Fase 2/3 y uno de Fase 4, junto con una revisión Cochrane y metaanálisis que sitúan a bupropión como alternativa no estimulante en TDAH. Sin embargo, el perfil de seguridad (convulsiones, efectos cardiovasculares, alta carga de interacciones) y la ausencia de registros vigentes en Colombia exigen cautela.

**Para avanzar se necesita:**
- Confirmar que bupropión fue el agente evaluado y el comparador en NCT00048360 y NCT00061087, y revisar sus resultados publicados.
- Obtener el prospecto de INVIMA para completar advertencias y contraindicaciones oficiales.
- Obtener datos del mecanismo de acción desde DrugBank.
- Definir la situación regulatoria: los tres registros están cancelados, por lo que se requeriría un nuevo registro o su reactivación.
- Diseñar un plan de seguimiento de seguridad: riesgo de convulsiones, presión arterial y frecuencia cardíaca, interacciones (especialmente CYP2D6 y opioides) y poblaciones con comorbilidad por uso de sustancias.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

