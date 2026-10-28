---
layout: default
title: Amantadine
parent: Solo Predicción del Modelo (L5)
nav_order: 44
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-28
description: "Amantadine: nueva indicación predicha, Encefalitis subaguda de Rasmussen (nivel de evidencia L5). Indicación original: AMANTADINA"
monitor_inn: "amantadine"
predicted_indications: ["Rasmussen subacute encephalitis", "transaldolase deficiency", "myelitis", "PLA2G6-associated neurodegeneration"]
---

# Amantadine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

## Amantadina: De Amantadina (indicación registrada sin detallar) a Rasmussen subacute encephalitis (encefalitis subaguda de Rasmussen)
{: .text-alpha }

## Resumen en Una Frase

La amantadina es un principio activo registrado en Colombia bajo el nombre ZINTERGIA® 100 mg cápsulas; el texto de indicación del registro solo menciona "AMANTADINA", sin detallar el uso aprobado.
El modelo TxGNN predice que podría ser efectiva para **encefalitis subaguda de Rasmussen**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción específica: se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | AMANTADINA (el registro no detalla la indicación) |
| Nueva Indicación Predicha | Encefalitis subaguda de Rasmussen |
| Puntaje de Predicción TxGNN | 0.9948 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 1) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según el conocimiento general, la amantadina es un antagonista del receptor NMDA con acción dopaminérgica, y podría modular la excitotoxicidad mediada por glutamato.

La encefalitis de Rasmussen es un síndrome epiléptico neuroinflamatorio. Una hipótesis plausible es que la modulación glutamatérgica podría ser relevante, pero es **especulativa** y no está confirmada por los datos disponibles. Tampoco se ha establecido la similitud con la indicación original.

Conviene interpretar con cautela el puntaje alto (0.9948): refleja una predicción del modelo, no evidencia clínica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la encefalitis subaguda de Rasmussen.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 19931778 | ZINTERGIA® 100 MG CAPSULAS (NOVAMED S.A.S.) | Cápsula dura | AMANTADINA | Vigente |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: el grafo de conocimiento TxGNN (PrimeKG) asocia la amantadina con enfermedades en las que podría estar contraindicada, entre ellas: epilepsia, enfermedad renal, insuficiencia cardíaca congestiva, trastornos psicóticos y otros trastornos mentales (esquizoafectivo, esquizofreniforme), glaucoma de ángulo cerrado, hipotensión ortostática, síndrome de taquicardia postural ortostática, atrofia multisistémica, abuso/dependencia de sustancias, melanoma, dermatitis/eccema atópico y piouréter. Es especialmente relevante la **epilepsia**, dado que la indicación predicha (encefalitis de Rasmussen) cursa con crisis epilépticas.
- **Interacciones farmacológicas**: se identificaron 93 interacciones en total. Entre las principales:
  - **Mayor**: bupropión.
  - **Moderadas**: anticolinérgicos (atropina, escopolamina, hioscina/hiosciamina, glicopirronio, diciclomina, clidinio, mepenzolato, metescopolamina, propantelina, trospio), metoclopramida, polietilenglicol con electrolitos, picosulfato sódico y sulfato de sodio.
  - **Nivel desconocido**: calcitriol, pantoprazol, glimepirida, doxiciclina, metformina.

No se dispone de advertencias ni contraindicaciones del prospecto de INVIMA; se recomienda consultarlo.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, el único registro sanitario está cancelado y el grafo de conocimiento señala la epilepsia como posible contraindicación.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA (advertencias y contraindicaciones) y completar los datos del mecanismo de acción en DrugBank.
- Revisión bibliográfica específica sobre amantadina y encefalitis de Rasmussen, así como estudios preclínicos que respalden el vínculo con la modulación glutamatérgica.
- Evaluar el riesgo de la amantadina en pacientes con epilepsia.
- Confirmar la situación regulatoria, dado que no hay registros vigentes en Colombia.

---

### Nota sobre otras predicciones evaluadas

Las demás predicciones del modelo tienen también puntajes altos pero evidencia limitada:

| Enfermedad predicha | Puntaje TxGNN | Nivel | Recomendación | Observación |
|------|------|------|------|------|
| Deficiencia de transaldolasa | 0.9927 | L5 | Hold | Sin evidencia ni vínculo mecanístico identificable |
| Mielitis | 0.9924 | L4 | Pregunta de investigación | 8 publicaciones, todas sobre síndrome post-polio y fatiga (evidencia indirecta). Incluye un ECA doble ciego de 1995 sobre fatiga (PMID 7611638); las revisiones y guías no respaldan un beneficio claro |
| Neurodegeneración asociada a PLA2G6 | 0.9923 | L4 | Pregunta de investigación | Una sola publicación (PMID 31366412), sobre otra enfermedad (PKAN); evidencia indirecta y solo sintomática |
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

