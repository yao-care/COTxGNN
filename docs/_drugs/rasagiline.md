---
layout: default
title: Rasagiline
parent: Solo Predicción del Modelo (L5)
nav_order: 550
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-29
description: "Rasagiline: nueva indicación predicha, Neurodegeneración asociada a PLA2G6 (nivel de evidencia L5). Indicación original: Rasagilina"
monitor_inn: "Rasagiline"
predicted_indications: ["PLA2G6-associated neurodegeneration", "Rasmussen subacute encephalitis", "myelitis", "paralysis agitans, juvenile, of Hunt", "transaldolase deficiency", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis"]
---

# Rasagiline
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Rasagilina: De Enfermedad de Parkinson a Neurodegeneración Asociada a PLA2G6
{: .text-alpha }

## Resumen en Una Frase

Rasagilina es un inhibidor selectivo e irreversible de la MAO-B, utilizado originalmente en el tratamiento de la enfermedad de Parkinson.
El modelo TxGNN predice que podría ser efectivo para **neurodegeneración asociada a PLA2G6**,
pero actualmente **no hay ensayos clínicos ni publicaciones** en los datos compilados que respalden esta dirección: es solo una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Rasagilina (el registro sanitario no detalla la indicación; el uso conocido del fármaco es la enfermedad de Parkinson) |
| Nueva Indicación Predicha | Neurodegeneración asociada a PLA2G6 |
| Puntaje de Predicción TxGNN | 0.9971 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Autorizado pero no comercializado (registros: 1) |
| Número de Registros Sanitarios | 1 (vigentes: 0) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Rasagilina es un inhibidor selectivo e irreversible de la monoaminooxidasa B (MAO-B). Al bloquear esta enzima aumenta la disponibilidad de dopamina en el estriado, y se le han atribuido efectos neuroprotectores (antiapoptóticos y de estabilización mitocondrial). Estos efectos neuroprotectores son propuestos y no están plenamente demostrados. Los datos compilados no incluyen una descripción detallada del mecanismo de acción; la información sobre MAO-B proviene de los datos farmacológicos del fármaco.

La neurodegeneración asociada a PLA2G6 incluye la distrofia neuroaxonal infantil y la distonía-parkinsonismo relacionada con PLA2G6. Comparte con la enfermedad de Parkinson la patología de alfa-sinucleína y la pérdida de neuronas dopaminérgicas. Por ello, el efecto de rasagilina sobre el tono dopaminérgico ofrece un vínculo plausible, sobre todo para el fenotipo parkinsoniano.

Este vínculo es solo una hipótesis. El puntaje alto del modelo (0.9971) es una predicción computacional sin ensayos clínicos ni literatura que la respalden. No se sabe si el beneficio sintomático en Parkinson se traduce a esta enfermedad genética, generalmente de inicio pediátrico.

### Otras predicciones del modelo (todas de evidencia limitada)

| Enfermedad predicha | Puntaje TxGNN | Nivel de Evidencia | Comentario |
|------|------|------|------|
| Encefalitis subaguda de Rasmussen | 0.9956 | L5 | Enfermedad inflamatoria mediada por linfocitos T; no hay vínculo mecanístico directo |
| Mielitis | 0.9932 | L5 | Posible efecto neuroprotector teórico; sin fundamento directo |
| Parálisis agitante juvenil de Hunt | 0.9925 | L5 | Síndrome parkinsoniano juvenil cercano a la enfermedad de Parkinson; evidencia indirecta, sin estudios en población juvenil |
| Deficiencia de transaldolasa | 0.9919 | L5 | Sin acción conocida sobre la vía de las pentosas fosfato |
| Polimicrogiria perisilviana con hipoplasia cerebelosa y artrogriposis | 0.9901 | L5 | Malformación estructural; sin mecanismo plausible |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20158581 (cancelado) | ZAGIL® | Tableta | Rasagilina |

El fabricante es GENEPHARM S.A. Actualmente no hay registros vigentes en Colombia.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (TxGNN/PrimeKG, no provienen del prospecto):** hipertensión y trastornos hipertensivos, atrofia multisistémica, síndrome de taquicardia postural ortostática, hipotensión ortostática, discinesia inducida por fármacos, epilepsia, trastorno bipolar, trastorno afectivo mayor, enfermedad hepática, enfermedad de la vesícula biliar, melanoma, feocromocitoma y paraganglioma simpático, y cánceres de duodeno, intestino delgado, corazón y glándula suprarrenal. Deben verificarse con el prospecto oficial.
- **Interacciones farmacológicas:** el dato farmacológico disponible señala su diana principal, la MAO-B humana (gen MAOB). No hay interacciones con otros fármacos clasificadas por nivel de gravedad en los datos compilados.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para neurodegeneración asociada a PLA2G6 tiene un puntaje alto, pero no cuenta con ensayos clínicos ni literatura (nivel L5). Además, rasagilina no tiene registros sanitarios vigentes en Colombia y faltan datos de seguridad oficiales.

**Para avanzar se necesita:**
- Revisión de la literatura y de registros de ensayos sobre rasagilina en neurodegeneración asociada a PLA2G6 y parkinsonismos genéticos
- Datos detallados del mecanismo de acción
- Obtención y análisis del prospecto aprobado por INVIMA (advertencias y contraindicaciones)
- Evaluación de la seguridad en población pediátrica, dado el inicio temprano de la enfermedad
- Verificación de la situación regulatoria: no hay registro vigente y habría que solicitar uno nuevo o reactivar el existente
- Estudios preclínicos en modelos de neurodegeneración asociada a PLA2G6 antes de considerar estudios clínicos
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

