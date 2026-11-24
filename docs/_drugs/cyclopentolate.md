---
layout: default
title: Cyclopentolate
parent: Solo Predicción del Modelo (L5)
nav_order: 184
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
description: "Cyclopentolate: nueva indicación predicha, Síndrome de la cola de caballo (nivel de evidencia L5). Indicación original: Ciclopentolato"
monitor_inn: "cyclopentolate"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "irritable bowel syndrome"]
---

# Cyclopentolate
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Ciclopentolato: De Uso Oftálmico (Midriasis y Cicloplejía) a Síndrome de la Cola de Caballo
{: .text-alpha }

## Resumen en Una Frase

El ciclopentolato es un agente antimuscarínico de uso oftálmico, registrado en Colombia en solución oftálmica al 1%.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de la cola de caballo**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; la predicción es solo computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Ciclopentolato (el registro sanitario solo indica el nombre del principio activo, sin texto de indicación detallado) |
| Nueva Indicación Predicha | Síndrome de la cola de caballo |
| Puntaje de Predicción TxGNN | 0.9954 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 2 de 2) |
| Número de Registros Sanitarios | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Clinical Pharmacology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Cyclopentolate (traducción no oficial): «Este preparado anticolinérgico bloquea las respuestas del músculo esfínter del iris y del músculo acomodativo del cuerpo ciliar a la estimulación colinérgica, lo que produce dilatación pupilar (midriasis) y parálisis de la acomodación (cicloplejía). Actúa rápidamente, pero su duración es menor que la de la atropina.» Texto original en inglés: "This anticholinergic preparation blocks the responses of the sphincter muscle of the iris and the accommodative muscle of the ciliary body to cholinergic stimulation, producing pupillary dilation (mydriasis) and paralysis of accommodation (cycloplegia). It acts rapidly, but has a shorter duration than atropine." ([DailyMed: Cyclogyl (cyclopentolate hydrochloride) prescribing information, Alcon Laboratories, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1d008c76-7210-4ace-90fa-7cd22762e12e), versión del 2024-06-25; consultado el 2026-11-19). Según la información conocida, el ciclopentolato es un fármaco antimuscarínico (anticolinérgico) de uso tópico oftálmico, empleado para producir midriasis y cicloplejía. Mecanísticamente, el bloqueo de los receptores muscarínicos podría reducir la hiperactividad del detrusor, lo que se vincularía con la disfunción vesical asociada al síndrome de la cola de caballo.

Este vínculo es **especulativo**. El fármaco está formulado para uso oftálmico, su exposición sistémica es mínima y no hay evidencia clínica ni bibliográfica. Además, el síndrome de la cola de caballo es principalmente una urgencia quirúrgica (descompresión); un papel farmacológico sería, como máximo, sintomático.

**Otras predicciones del modelo (todas con evidencia L5 y decisión Hold):**

- **Vejiga neurogénica** (término marcado como obsoleto en la ontología; puntaje 0.9940): los antimuscarínicos son una clase establecida para la hiperactividad neurogénica del detrusor (p. ej., oxibutinina, tolterodina), por lo que la lógica de clase es plausible. Sin embargo, no hay evidencia de uso oral o intravesical del ciclopentolato, y el término de la enfermedad debería actualizarse a uno vigente.
- **Síndrome de intestino irritable** (puntaje 0.9927): antimuscarínicos como diciclomina o hiosciamina se usan para el dolor y los cólicos abdominales. No hay evidencia directa para el ciclopentolato, y los antimuscarínicos ya aprobados cubren este nicho, por lo que el valor añadido es bajo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 19954096 | CYCLOGYL 1%® SOLUCION OFTALMICA ESTERIL | SOLUCION OFTALMICA | CICLOPENTOLATO | Vigente |
| 37468 | CICLOPENTOLATO CLORHIDRATO 1% | SOLUCION OFTALMICA | CICLOPENTOLATO | Vigente |

Se muestran los 2 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Enfermedades con contraindicación según el grafo de conocimiento (no proviene del prospecto):** hipertensión, diabetes mellitus y cetoacidosis diabética, hiperplasia prostática benigna, enfermedad cardíaca y cardiovascular (incluida enfermedad coronaria, paro cardíaco súbito y trastornos de la conducción), glaucoma de ángulo cerrado, hipertiroidismo (enfermedad de Graves, tirotoxicosis), arteriosclerosis y aterosclerosis, lesión o enfermedad cerebral y síndrome de Down.

Para las advertencias, contraindicaciones oficiales e interacciones farmacológicas, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo TxGNN (nivel L5), sin ensayos ni literatura. Además, el producto es de uso oftálmico, con exposición sistémica mínima, y está comercializado en Colombia, con 2 registros sanitarios vigentes de 2.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (consulta a DrugBank)
- Prospecto de INVIMA con advertencias y contraindicaciones, necesario para el tamizaje de seguridad
- Revisión bibliográfica y de ensayos sobre antimuscarínicos en las indicaciones predichas
- Evaluación de viabilidad de una vía de administración sistémica o intravesical (hoy solo existe la vía oftálmica)
- Conciliar el término obsoleto de vejiga neurogénica con la terminología vigente
- Valorar el beneficio frente a antimuscarínicos ya aprobados para estas indicaciones

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Cyclogyl (cyclopentolate hydrochloride) prescribing information, Alcon Laboratories, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1d008c76-7210-4ace-90fa-7cd22762e12e) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

