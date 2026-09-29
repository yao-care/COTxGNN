---
layout: default
title: Filgrastim
parent: Solo Predicción del Modelo (L5)
nav_order: 199
evidence_level: L5
indication_count: 10
---

# Filgrastim
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

# Filgrastim: De Indicación No Especificada en el Registro a Trastorno Primario de Liberación Plaquetaria

## Resumen en Una Frase

Filgrastim (G-CSF) es un factor estimulante de colonias de granulocitos. El registro sanitario colombiano solo repite el nombre del fármaco como texto de indicación, por lo que la indicación original no queda documentada en los datos disponibles.
El modelo TxGNN predice que podría ser efectivo para el **trastorno primario de liberación plaquetaria**, con una puntuación muy alta.
Sin embargo, los **13 ensayos clínicos** y la **1 publicación** asociados no estudian esa enfermedad, así que la predicción carece de respaldo real.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto aprobado solo dice "FILGRASTIM") |
| Nueva Indicación Predicha | Trastorno primario de liberación plaquetaria (primary release disorder of platelets) |
| Puntaje de Predicción TxGNN | 99.998% |
| Nivel de Evidencia | L5 (el paquete de datos asigna L4, pero ningún estudio aborda esta indicación) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Por lo que se conoce de la clase, filgrastim actúa sobre la línea de neutrófilos y moviliza células CD34+ de la médula ósea.

Un defecto de liberación plaquetaria es un trastorno funcional de las plaquetas. No hay evidencia de que el G-CSF lo corrija. La revisión mecanística concluye que **no existe un vínculo directo**.

El puntaje TxGNN (99.998%) proviene solo del grafo de conocimiento y no de estudios reales. Los ensayos asociados son protocolos de trasplante de progenitores hematopoyéticos, donde el G-CSF es un agente de apoyo o movilización, no el objeto de estudio. La predicción debe tratarse como una hipótesis sin sustento clínico ni mecanístico.

## Evidencia de Ensayos Clínicos

Se listan 10 de los 13 ensayos vinculados. Todos fueron calificados con relevancia baja (grado C) porque ninguno evalúa un trastorno plaquetario.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00281879](https://clinicaltrials.gov/study/NCT00281879) | Fase 2 | Terminado | 200 | Trasplante de células madre de donante no emparentado en neoplasias hematológicas |
| [NCT00043979](https://clinicaltrials.gov/study/NCT00043979) | Fase 2 | Completado | 60 | Trasplante alogénico/singénico en sarcomas pediátricos de alto riesgo |
| [NCT00354172](https://clinicaltrials.gov/study/NCT00354172) | Fase 2 | Terminado | 16 | Trasplante de sangre de cordón en leucemia mieloide con células NK |
| [NCT00923364](https://clinicaltrials.gov/study/NCT00923364) | Fase 2 | Completado | 19 | Trasplante de intensidad reducida en pacientes con mutaciones GATA2 |
| [NCT02646098](https://clinicaltrials.gov/study/NCT02646098) | Fase 2 | Completado | 64 | Trasplante autólogo con selección CD34+ en linfoma del manto y linfoma B difuso de células grandes |
| [NCT05436418](https://clinicaltrials.gov/study/NCT05436418) | Fase 1/2 | Reclutando | 260 | Dosis mínima eficaz de ciclofosfamida postrasplante para prevenir enfermedad injerto contra huésped |
| [NCT05170828](https://clinicaltrials.gov/study/NCT05170828) | Fase 1 | Retirado | 0 | Trasplante con médula ósea criopreservada de donante no compatible; sin participantes, no aporta evidencia |
| [NCT00076752](https://clinicaltrials.gov/study/NCT00076752) | Fase 2 | Completado | 9 | Linfodepleción y trasplante autólogo en lupus eritematoso sistémico grave |
| [NCT04540120](https://clinicaltrials.gov/study/NCT04540120) | Fase 2 | Terminado | 49 | Dapansutrile oral (no filgrastim) en COVID-19 moderado con síndrome de liberación de citocinas |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Fase 2 | Reclutando | 358 | Plataforma de profilaxis de enfermedad injerto contra huésped con ciclofosfamida postrasplante |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [29770133](https://pubmed.ncbi.nlm.nih.gov/29770133/) | 2018 | Estudio clínico (donantes sanos) | Frontiers in Immunology | La movilización de células madre con G-CSF en donantes sanos moviliza de forma preferente subpoblaciones de linfocitos. No trata trastornos plaquetarios. |

## Información de Mercado en Colombia

El registro tiene 20 entradas de licencia. Las cinco revisadas corresponden al mismo registro sanitario, por lo que se muestra una sola vez.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20002046 | Filgrastim 300 mcg/ml solución inyectable (MEGALABS COLOMBIA S.A.S) | Solución inyectable | Texto registrado: "FILGRASTIM" (sin descripción de indicación) |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Ningún ensayo ni publicación evalúa filgrastim en trastornos de la función plaquetaria, y no hay un mecanismo plausible que respalde la predicción. El puntaje alto de TxGNN no es suficiente por sí solo. Las otras nueve indicaciones predichas para este fármaco tampoco tienen respaldo: dos tienen evidencia tangencial (síndrome de Scott y trastorno hemorrágico plaquetario) y siete son solo predicción.

**Para avanzar se necesita:**
- Obtener del INVIMA el prospecto con advertencias, contraindicaciones e indicaciones aprobadas, porque el registro solo repite el nombre del fármaco.
- Consultar DrugBank para completar el mecanismo de acción.
- Buscar evidencia preclínica o clínica que vincule al G-CSF con la función plaquetaria antes de reconsiderar la candidatura.
- Revisar si alguna de las otras indicaciones predichas tiene mejor sustento.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

