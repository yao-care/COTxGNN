---
layout: default
title: Terbutaline
parent: Evidencia Alta (L1-L2)
nav_order: 616
evidence_level: L1
indication_count: 3
last_modified_at: 2026-10-14
description: "Terbutaline: nueva indicación predicha, Enfermedad pulmonar obstructiva (nivel de evidencia L1). Indicación original: Terbutalina"
---

# Terbutaline
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **3** 
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

# Terbutalina: De Broncodilatador para Asma/EPOC a Enfermedad Pulmonar Obstructiva

## Resumen en Una Frase

Terbutalina es un agonista beta-2 adrenérgico de acción corta, registrado en Colombia bajo la denominación "Terbutalina" (sola o en combinaciones).
El modelo TxGNN predice que podría ser efectivo para **enfermedad pulmonar obstructiva**, con **14 ensayos clínicos** y **20 publicaciones** relacionados con esta dirección. Cabe aclarar que esta predicción coincide en gran medida con el uso ya establecido del fármaco (broncodilatación), por lo que es más una confirmación que un reposicionamiento novedoso.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Terbutalina |
| Nueva Indicación Predicha | Enfermedad pulmonar obstructiva |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 4 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción del fármaco. Según la farmacología conocida, la terbutalina es un agonista selectivo de los receptores beta-2 adrenérgicos (también con afinidad por beta-1). Su activación eleva el AMPc en el músculo liso bronquial y produce relajación, lo que alivia la broncoconstricción.

La indicación original (terbutalina en solución para nebulización, jarabes y combinaciones con guayacolato) corresponde a enfermedades respiratorias con obstrucción reversible de la vía aérea. La enfermedad pulmonar obstructiva (asma, EPOC, bronquitis, enfisema) comparte precisamente ese sustrato fisiopatológico, por lo que la puntuación tan alta del modelo es coherente con la farmacología establecida.

Es importante reconocer que esta predicción confirma un uso ya conocido y no representa un hallazgo nuevo. Las otras dos predicciones del modelo son mucho más débiles: *malformación respiratoria* (nivel L4, evidencia mayormente de asma y bronquitis, con varios estudios fuera de tema) y *síndrome de Rienhoff* (nivel L5, sin ensayos ni literatura, solo predicción computacional). Ambas quedan en **Hold**.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02224157](https://clinicaltrials.gov/study/NCT02224157) | Fase 3 | Completado | 4215 | Symbicort a demanda vs. Pulmicort dos veces al día + terbutalina a demanda en asma; terbutalina como comparador de rescate |
| [NCT02149199](https://clinicaltrials.gov/study/NCT02149199) | Fase 3 | Completado | 3850 | Symbicort a demanda vs. terbutalina a demanda vs. Pulmicort + terbutalina en asma leve |
| [NCT06626620](https://clinicaltrials.gov/study/NCT06626620) | Fase 3 | Completado | 120 | Sulfato de magnesio IV vs. terbutalina en niños con exacerbación aguda de asma |
| [NCT00839800](https://clinicaltrials.gov/study/NCT00839800) | Fase 3 | Completado | 2091 | Symbicort SMART vs. Symbicort + terbutalina 0,4 mg a demanda en asma |
| [NCT00259766](https://clinicaltrials.gov/study/NCT00259766) | Fase 3 | Completado | 1970 | Costos y control del asma en práctica real; Bricanyl (terbutalina) como rescate |
| [NCT00252863](https://clinicaltrials.gov/study/NCT00252863) | Fase 3 | Completado | 1600 | Terapia Symbicort de mantenimiento y rescate vs. tratamiento convencional en asma persistente |
| [NCT00849095](https://clinicaltrials.gov/study/NCT00849095) | Fase 3 | Completado | 860 | Budesonida/formoterol a demanda vs. regular + terbutalina a demanda en asma persistente leve-moderada |
| [NCT00421122](https://clinicaltrials.gov/study/NCT00421122) | Fase 3 | Completado | 315 | Symbicort + Bricasol (terbutalina) vs. Pulmicort + Bricasol en EPOC en pacientes chinos |
| [NCT02322788](https://clinicaltrials.gov/study/NCT02322788) | Fase 3 | Completado | 95 | Estudio farmacodinámico cruzado de Bricanyl Turbuhaler M3 vs. M2 frente a broncoconstricción por metacolina en asma |
| [NCT01096017](https://clinicaltrials.gov/study/NCT01096017) | Fase 3 | Completado | 24 | Eficacia relativa de terbutalina Turbuhaler 0,4 mg vs. salbutamol pMDI en adultos japoneses con asma |

Nota: el ensayo NCT04973345 (fase 2/3, exposición-respuesta de terbutalina en asma) fue retirado sin participantes, por lo que no aporta evidencia. En la mayoría de los ensayos la terbutalina actúa como comparador o medicación de rescate, no como intervención principal.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [29768149](https://pubmed.ncbi.nlm.nih.gov/29768149/) | 2018 | ECA | N Engl J Med | Budesonida-formoterol a demanda como alternativa a los tratamientos convencionales en asma leve |
| [3073804](https://pubmed.ncbi.nlm.nih.gov/3073804/) | 1988 | ECA | Br J Dis Chest | Terbutalina oral aumentó la fuerza de contracción diafragmática en EPOC (cruzado, doble ciego) |
| [6988343](https://pubmed.ncbi.nlm.nih.gov/6988343/) | 1980 | ECA | Int J Clin Pharmacol Ther Toxicol | Comparación oral de clenbuterol y terbutalina en enfermedad pulmonar obstructiva crónica |
| [6107217](https://pubmed.ncbi.nlm.nih.gov/6107217/) | 1980 | ECA | Chest | Interacción entre betabloqueadores y terbutalina oral en enfermedad pulmonar obstructiva con cardiopatía o hipertensión |
| [36227333](https://pubmed.ncbi.nlm.nih.gov/36227333/) | 2023 | Revisión sistemática | Naunyn-Schmiedeberg's Arch Pharmacol | Farmacocinética clínica de la terbutalina según vía, edad, tabaquismo y otros factores |
| [23348973](https://pubmed.ncbi.nlm.nih.gov/23348973/) | 2013 | Revisión | Am J Respir Crit Care Med | Terapia con agonistas beta-2 en enfermedad pulmonar; terbutalina como agonista inhalado de acción corta |
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Guía | Basic Clin Pharmacol Toxicol | Guía finlandesa para el diagnóstico y tratamiento farmacológico de la EPOC estable |
| [30156361](https://pubmed.ncbi.nlm.nih.gov/30156361/) | 2019 | ECA | Acad Emerg Med | Terbutalina nebulizada con ipratropio vs. terbutalina sola en exacerbación aguda de EPOC con ventilación no invasiva |
| [10384064](https://pubmed.ncbi.nlm.nih.gov/10384064/) | 1999 | ECA cruzado | Lung | Efecto de una dosis de terbutalina (Turbuhaler) sobre función pulmonar y capacidad de ejercicio en EPOC |
| [1615190](https://pubmed.ncbi.nlm.nih.gov/1615190/) | 1992 | ECA cruzado | Respir Med | Terbutalina inhalada y su efecto sobre FEV1, FVC, disnea y distancia de marcha en enfermedad pulmonar obstructiva |

---

## Información de Mercado en Colombia

Los cuatro registros sanitarios están cancelados; actualmente no hay registros vigentes.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 38998 | TERBUROP® Solución para Nebulización | Solución para nebulización | Terbutalina |
| 20009248 | NASMINE N.F. Jarabe | Jarabe | Terbutalina combinaciones |
| 218166 | TERBUROP® Jarabe | Jarabe | Terbutalina |
| 218164 | TERBUROP Guayacolato Jarabe | Jarabe | Terbutalina combinaciones |

---

## Consideraciones de Seguridad

- **Contraindicaciones o precauciones según el grafo de conocimiento** (relaciones fármaco-enfermedad del modelo, no texto de prospecto): hipertensión, epilepsia, hiperglucemia, deficiencia de potasio, diabetes mellitus, cetoacidosis diabética, paro cardíaco súbito, enfermedad de la conducción cardíaca, insuficiencia respiratoria, hipertiroidismo (enfermedad de Graves, tirotoxicosis), edema pulmonar, isquemia miocárdica, enfermedad coronaria y desprendimiento prematuro de placenta.
- **Interacciones y dianas farmacológicas**: la terbutalina actúa sobre los receptores beta-1 (ADRB1) y beta-2 (ADRB2) adrenérgicos. Esto es consistente con la observación en la literatura de una interacción con betabloqueadores (PMID 6107217). No se dispone de interacciones con otros fármacos con nivel de gravedad asignado.

Las advertencias y contraindicaciones del prospecto de INVIMA no están disponibles en los datos compilados; consultar el prospecto para la información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen múltiples ensayos de fase 3 completados y de gran tamaño en asma y EPOC, lo que corresponde a un nivel de evidencia L1. Sin embargo, la terbutalina es en la mayoría un comparador o medicación de rescate, la predicción reproduce un uso ya establecido y, en Colombia, todos los registros están cancelados. Por ello se recomienda avanzar con salvaguardas.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), pendiente y de carácter bloqueante para el tamizaje de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Aclarar la situación regulatoria: ningún registro vigente en Colombia; evaluar si se requeriría un nuevo registro o una reactivación.
- Revisar con atención los riesgos cardiovasculares, metabólicos (glucosa, potasio) y de hipertiroidismo señalados en el grafo de conocimiento.
- Verificar, en los ensayos donde la terbutalina es comparador, su papel específico y los resultados frente al desenlace principal.
- Las predicciones de *malformación respiratoria* y *síndrome de Rienhoff* deben mantenerse en **Hold**, a la espera de evidencia específica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

