---
layout: default
title: Galantamine
parent: Solo Predicción del Modelo (L5)
nav_order: 307
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Galantamine: nueva indicación predicha, Trastornos del movimiento psicogénicos (nivel de evidencia L5). Indicación original: No especificada en el registro sanitario (el texto solo indica \"Galan…"
monitor_inn: "galantamine"
predicted_indications: ["psychogenic movement disorders", "chronic tic disorder", "primary orthostatic tremor", "benign shuddering attacks", "extrapyramidal and movement disease", "tremor-nystagmus-duodenal ulcer syndrome", "lingual-facial-buccal dyskinesia", "benign paroxysmal tonic upgaze of childhood with ataxia", "acute intermittent porphyria"]
---

# Galantamine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Galantamina: De Indicación No Especificada en el Registro a Trastornos del Movimiento Psicogénicos
{: .text-alpha }

## Resumen en Una Frase

Galantamina es un inhibidor reversible de la acetilcolinesterasa y modulador alostérico positivo de los receptores nicotínicos. Sus registros sanitarios colombianos (Reminyl®) no detallan la indicación aprobada, solo indican el nombre del principio activo.
El modelo TxGNN predice que podría ser efectiva para **trastornos del movimiento psicogénicos**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción específica.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro sanitario (el texto solo indica "Galantamina") |
| Nueva Indicación Predicha | Trastornos del movimiento psicogénicos |
| Puntaje de Predicción TxGNN | 0.9990 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 2 de 2) |
| Número de Registros Sanitarios | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Galantamina inhibe de forma reversible la acetilcolinesterasa y modula de forma alostérica los receptores nicotínicos de acetilcolina. Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción, por lo que este resumen se basa en el conocimiento farmacológico general del fármaco.

Para los trastornos del movimiento psicogénicos **no se identificó un vínculo mecanístico directo**. Estos trastornos son de naturaleza funcional y no tienen una patología colinérgica establecida. El puntaje elevado (0.999) es solo una predicción computacional, sin ensayos ni literatura de respaldo. Por ello, la predicción debe tratarse con cautela.

**Otras predicciones del modelo.** Otras indicaciones tienen puntajes muy similares (rango 0.9971–0.9989). Dos de ellas cuentan con algo de literatura:

- **Discinesia lingual-facial-bucal** (99.88%): 22 publicaciones, incluido un ensayo aleatorizado cruzado de galantamina en discinesia tardía (PMID 17388711), además de revisiones Cochrane sobre medicación colinérgica en discinesia tardía. Estas revisiones tratan los fármacos colinérgicos como clase, no a la galantamina en particular. Es la candidata con evidencia más relevante, clasificada como "pregunta de investigación".
- **Enfermedad extrapiramidal y del movimiento** (99.88%): 4 publicaciones, incluida una revisión sistemática de 2025 que describe trastornos del movimiento como **efecto adverso** de los inhibidores de la colinesterasa. La dirección del efecto es incierta.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para trastornos del movimiento psicogénicos.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para trastornos del movimiento psicogénicos.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 19954847 | Reminyl® ER cápsulas de 16 mg | Cápsula de liberación prolongada | Galantamina | Vigente |
| 19932247 | Reminyl® solución oral de 4 mg/ml | Solución oral | Galantamina | Vigente |

Ambos registros pertenecen a Janssen Cilag S.A. y no hay registros vigentes.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** síndrome de QT largo familiar, insuficiencia hepática, enfermedad hepática, enfermedad renal, epilepsia, EPOC (incluida la de inicio temprano grave), asma (intrínseca y alérgica), piouréter, enfermedad de la vesícula biliar, úlcera péptica, úlcera duodenal, obstrucción del cuello vesical y bloqueo auriculoventricular.
- **Interacciones farmacológicas:** se identificaron 173 interacciones. Entre las principales:
  - **Mayor:** bupropión.
  - **Moderadas:** famotidina, ranitidina, cimetidina, atropina, claritromicina, dicicloverina, dolasetrón, eliglustat, loperamida, hiosciamina, lorcaserina, metronidazol, glicopirronio, clidinio, ácido picosulfúrico, polietilenglicol con electrolitos, palonosetrón, trospio y sulfato de sodio.

No se dispone de advertencias ni contraindicaciones del prospecto de INVIMA; consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para trastornos del movimiento psicogénicos se basa únicamente en el modelo (L5), sin ensayos, literatura ni vínculo mecanístico plausible. Además, ambos registros sanitarios en Colombia están cancelados y no se dispone de información de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), un vacío de información que bloquea la evaluación de seguridad.
- Obtener datos del mecanismo de acción desde DrugBank.
- Aclarar la indicación original aprobada, ya que el registro solo menciona el nombre del principio activo.
- Considerar priorizar otras predicciones con evidencia indirecta, como la discinesia lingual-facial-bucal, mediante una revisión sistemática específica de galantamina, que incluya el ensayo cruzado PMID 17388711.
- Evaluar la situación regulatoria actual, dado que los registros están cancelados.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

