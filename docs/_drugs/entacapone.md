---
layout: default
title: Entacapone
parent: Solo Predicción del Modelo (L5)
nav_order: 253
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Entacapone: nueva indicación predicha, Neurodegeneración asociada a PLA2G6 (nivel de evidencia L5). Indicación original: Levodopa e inhibidor de decarboxilasa"
---

# Entacapone
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

# Entacapona: De Terapia Adyuvante con Levodopa a Neurodegeneración Asociada a PLA2G6

## Resumen en Una Frase

Entacapona es un inhibidor de la COMT que se usa junto con levodopa/inhibidor de la descarboxilasa; en Colombia su único registro sanitario se asocia a esa indicación original.
El modelo TxGNN predice que podría ser efectivo para la **neurodegeneración asociada a PLA2G6**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Levodopa e inhibidor de decarboxilasa |
| Nueva Indicación Predicha | Neurodegeneración asociada a PLA2G6 |
| Puntaje de Predicción TxGNN | 99.76% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo cancelado (sin registros vigentes) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción detallado. Según lo conocido, la entacapona es un inhibidor periférico de la catecol-O-metiltransferasa (COMT) que prolonga la acción de la levodopa. Su utilidad está establecida como tratamiento adyuvante en la enfermedad de Parkinson.

La neurodegeneración asociada a PLA2G6 incluye la distrofia neuroaxonal infantil y la distonía-parkinsonismo relacionada con PLA2G6. Un vínculo es concebible solo para el fenotipo parkinsoniano, como tratamiento sintomático. No modificaría la enfermedad de fondo, que implica el metabolismo de fosfolípidos y la acumulación de hierro.

La predicción se basa únicamente en el modelo y no cuenta con respaldo clínico ni bibliográfico. Debe interpretarse como una hipótesis para explorar, no como una indicación validada.

### Otras predicciones del modelo

| Posición | Enfermedad | Puntaje TxGNN | Nivel | Comentario |
|---|---|---|---|---|
| 2 | Encefalitis subaguda de Rasmussen | 99.73% | L5 | Sin relevancia mecanística establecida |
| 3 | Mielitis | 99.63% | L5 | Sin mecanismo antiinflamatorio conocido |
| 4 | Parálisis agitante juvenil de Hunt | 99.60% | L5 | Plausible biológicamente (déficit dopaminérgico), sin estudios |
| 7 | Demencia con cuerpos de Lewy | 99.25% | L4 | Apoyo indirecto solo preclínico |
| 10 | Síndrome de parálisis supranuclear progresiva-corticobasal | 99.04% | L5 | Respuesta pobre a levodopa; rationale limitado |

Las demás predicciones (deficiencia de transaldolasa, miopatía mitocondrial infantil letal, deficiencia de fructosa-1,6-bisfosfatasa, polimicrogiria perisilviana) no muestran un vínculo mecanístico plausible y carecen de evidencia.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para neurodegeneración asociada a PLA2G6.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20147960 | LEVOCAPONE 50/12.5/200 tableta recubierta | Tableta recubierta | Levodopa e inhibidor de decarboxilasa | Cancelado |

El único registro está cancelado, por lo que actualmente no hay presentaciones vigentes en el mercado colombiano.

---

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no el prospecto):** el grafo de conocimiento TxGNN (PrimeKG) asocia la entacapona con contraindicaciones en múltiples condiciones, entre ellas:
  - Neurológicas y autonómicas: atrofia multisistémica, hipotensión ortostática, síndrome de taquicardia postural ortostática, discinesia inducida por fármacos, epilepsia.
  - Psiquiátricas: trastornos psicóticos, esquizoafectivo, ansiedad, trastorno neurótico, distimia.
  - Cardiovasculares: infarto de miocardio, trombosis coronaria, paro cardíaco súbito, enfermedad de conducción cardíaca.
  - Hepáticas, renales y digestivas: enfermedad hepática, renal, de la vesícula biliar, úlcera gástrica y péptica, enfermedad diarreica.
  - Otras: glaucoma de ángulo abierto y cerrado, diabetes mellitus, cetoacidosis diabética, melanoma, hemoglobinopatías.
- **Interacciones Farmacológicas:** se identificaron 82 interacciones. Entre las de nivel **moderado** se encuentran epinefrina (incluidas las formas oftálmica y tópica), morfina (incluida la liposomal), dronabinol, opio, nabilona, metoclopramida y hierro. Otras, de nivel no clasificado, incluyen pantoprazol, omeprazol, lansoprazol, doxiciclina, metformina, atropina, lactulosa, prednisona, simvastatina y cloruro de potasio.
- **Consideraciones específicas:** en la parálisis agitante juvenil, las complicaciones motoras a largo plazo en pacientes jóvenes son una preocupación. En enfermedades mitocondriales, la posible hepatotoxicidad sería relevante.

Para advertencias y contraindicaciones del prospecto, consultar el prospecto del producto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal tiene un puntaje alto en TxGNN, pero no cuenta con ensayos clínicos ni literatura (nivel L5). Además, el vínculo mecanístico se limita a un posible efecto sintomático en el fenotipo parkinsoniano. No hay registros vigentes en Colombia.

**Para avanzar se necesita:**
- Obtener los datos del mecanismo de acción (por ejemplo, desde DrugBank).
- Descargar y analizar el prospecto de INVIMA para completar el tamizaje de seguridad.
- Revisar la literatura sobre respuesta a levodopa en la distonía-parkinsonismo por PLA2G6.
- Evaluar, como línea con mayor sustento biológico, la demencia con cuerpos de Lewy (L4) y el parkinsonismo juvenil, antes que las demás predicciones.
- Si se avanza, diseñar estudios preclínicos o series de casos con un plan de monitoreo de seguridad (cardiovascular, hepático y psiquiátrico).
- Confirmar la situación regulatoria: la ausencia de registros vigentes condiciona cualquier ruta de acceso local.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

