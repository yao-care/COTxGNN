---
layout: default
title: Modafinil
parent: Evidencia Moderada (L3-L4)
nav_order: 452
evidence_level: L4
indication_count: 1
last_modified_at: 2026-10-14
description: "Modafinil: nueva indicación predicha, Insomnio (nivel de evidencia L4). Indicación original: No especificada en el registro (el texto de indicación solo dice \"MOD…"
monitor_inn: "MODAFINIL"
predicted_indications: ["insomnia (disease)"]
---

# Modafinil
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **1** 
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

## Modafinilo: De Indicación No Especificada en el Registro a Insomnio
{: .text-alpha }

## Resumen en Una Frase

Modafinilo es un fármaco promotor de la vigilia que tuvo registros sanitarios en Colombia (VIGIA®), actualmente cancelados; el texto de indicación del registro solo repite el nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para **insomnio**, pero solo hay **2 ensayos clínicos** de relevancia limitada y literatura mayormente indirecta (sueño y somnolencia en otras enfermedades).
La predicción es mecanísticamente poco plausible, porque el fármaco promueve la vigilia en lugar del sueño.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto de indicación solo dice "MODAFINIL") |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 0.9985 |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 2) |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información general conocida, modafinilo es un agente promotor de la vigilia, farmacológicamente distinto de otros estimulantes, aprobado en otros países para la somnolencia excesiva diurna asociada a narcolepsia, apnea obstructiva del sueño y trastorno del sueño por trabajo en turnos. Se entiende que actúa mediante inhibición del transportador de dopamina y modulación de circuitos que favorecen la vigilia.

La relación entre su uso conocido y el insomnio es débil. Ambos pertenecen al ámbito de los trastornos del sueño y la vigilia, lo que probablemente explica el puntaje alto del modelo (proximidad en la red de conocimiento con narcolepsia, somnolencia y trastorno por turnos). Sin embargo, un fármaco que promueve la vigilia es mecanísticamente opuesto al tratamiento del insomnio.

Por ello, la predicción probablemente refleja una clasificación errónea de una indicación relacionada con el ciclo sueño-vigilia, más que un vínculo terapéutico real. Los dos ensayos de Fase 4 evalúan el funcionamiento diurno y las alteraciones sueño/vigilia, no la eficacia contra el insomnio.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00124384](https://clinicaltrials.gov/study/NCT00124384) | Fase 4 | Completado | 40 | Efectos del modafinilo, solo o con terapia cognitivo-conductual para el insomnio (TCC-I), sobre el funcionamiento diurno y la gravedad del insomnio en insomnio primario. Sin resultados disponibles; relevancia moderada (B). |
| [NCT00626210](https://clinicaltrials.gov/study/NCT00626210) | Fase 4 | Terminado | 2 | Alteraciones del sueño/vigilia en adultos mayores. Terminado con solo 2 participantes, sin evidencia interpretable; relevancia baja (C). |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [24312590](https://pubmed.ncbi.nlm.nih.gov/24312590/) | 2013 | Revisión sistemática/Metaanálisis | PloS one | Eficacia y seguridad del modafinilo en fatiga y somnolencia diurna asociadas a trastornos neurológicos; resultados previos inconsistentes. |
| [27010071](https://pubmed.ncbi.nlm.nih.gov/27010071/) | 2016 | Revisión sistemática/Metaanálisis | Parkinsonism & Related Disorders | Intervenciones farmacológicas para somnolencia diurna y trastornos del sueño en Parkinson; pocos ensayos disponibles. |
| [18729534](https://pubmed.ncbi.nlm.nih.gov/18729534/) | 2008 | Revisión | Drugs | Revisión basada en evidencia de usos aprobados y en investigación del modafinilo como agente promotor de la vigilia. |
| [22021174](https://pubmed.ncbi.nlm.nih.gov/22021174/) | 2011 | Revisión | Movement Disorders | Actualización de la Sociedad de Trastornos del Movimiento sobre tratamientos de síntomas no motores del Parkinson. |
| [39535843](https://pubmed.ncbi.nlm.nih.gov/39535843/) | 2024 | Revisión | Expert Opinion on Pharmacotherapy | Manejo farmacológico y no farmacológico de alteraciones del sueño en Parkinson. |
| [17060310](https://pubmed.ncbi.nlm.nih.gov/17060310/) | 2006 | Serie de casos | Am J Hosp Palliat Care | El modafinilo redujo la fatiga en la enfermedad de Charcot-Marie-Tooth tipo 1A. |
| [17181377](https://pubmed.ncbi.nlm.nih.gov/17181377/) | 2006 | Revisión | Drugs | Carga y manejo del trastorno del sueño por trabajo en turnos. |
| [18805301](https://pubmed.ncbi.nlm.nih.gov/18805301/) | 2008 | Revisión | Revue Neurologique | Narcolepsia con cataplejía: características clínicas y manejo. |

Ninguna de estas publicaciones evalúa directamente el modafinilo como tratamiento del insomnio.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19968570 | VIGIA® 100 MG (PROCAPS S.A.) | Cápsula blanda | MODAFINIL (sin detalle de indicación; estado: vigente) |
| 19968571 | VIGIA® 200 MG (PROCAPS S.A.) | Cápsula blanda | MODAFINIL (sin detalle de indicación; estado: vigente) |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** hipertensión, insuficiencia hepática, trastornos de ansiedad, trastornos psicóticos y otros trastornos mentales (esquizoafectivo, esquizofreniforme, distímico, neurótico), abuso/dependencia de sustancias, enfermedad coronaria (síndrome coronario agudo, infarto de miocardio, isquemia miocárdica), prolapso de la válvula mitral, síndrome de taquicardia postural ortostática y hemoglobinopatías.
- **Interacciones farmacológicas:** se identificaron 100 interacciones; entre las mostradas, las de nivel **moderado** incluyen rabeprazol, omeprazol, esomeprazol, dexametasona, eliglustat, linagliptina y cisaprida. Las de nivel **menor** incluyen hidrocortisona, pioglitazona, aprepitant, triamcinolona, betametasona, cimetidina, claritromicina, saxagliptina, dronabinol, clotrimazol, granisetrón, miconazol y naldemedina.

Las advertencias y contraindicaciones del prospecto del INVIMA no están disponibles; consultar el prospecto para confirmarlas.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia es de nivel L4: no hay ensayos de Fase 3, los dos ensayos de Fase 4 no evalúan la eficacia en insomnio (uno terminó con 2 participantes) y el mecanismo promotor de la vigilia es opuesto al efecto buscado. Además, no hay registros vigentes en Colombia y el perfil de seguridad no está documentado con el prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto del INVIMA (advertencias y contraindicaciones) para completar la evaluación de seguridad.
- Confirmar el mecanismo de acción con DrugBank y evaluar si existe algún vínculo mecanístico real con el insomnio.
- Reconsiderar si la indicación relevante es, en realidad, somnolencia diurna o un trastorno del sueño-vigilia (por ejemplo, narcolepsia o trabajo por turnos) y no insomnio.
- Aclarar la indicación original del registro y el motivo de la cancelación de los registros.
- Revisar con prioridad el riesgo cardiovascular y psiquiátrico del paciente antes de considerar este uso.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

