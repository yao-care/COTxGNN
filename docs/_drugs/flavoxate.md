---
layout: default
title: Flavoxate
parent: Solo Predicción del Modelo (L5)
nav_order: 287
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
description: "Flavoxate: nueva indicación predicha, Trastorno por déficit de atención e hiperactividad, tipo inatento (nivel de evidencia L5). Indicación original: Flavoxato"
monitor_inn: "flavoxate"
predicted_indications: ["attention deficit hyperactivity disorder, inattentive type", "irritable bowel syndrome", "specific developmental disorder", "attention deficit-hyperactivity disorder", "cauda equina syndrome", "obsolete neurogenic bladder (disease)", "gastroduodenitis", "peptic ulcer disease"]
---

# Flavoxate
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

# Flavoxato: De Indicación Urológica (Flavoxato) a Trastorno por Déficit de Atención e Hiperactividad, Tipo Inatento

## Resumen en Una Frase

Flavoxato es un relajante del músculo liso urinario, autorizado en Colombia como BLADURIL® 200 MG (tableta recubierta), cuyo registro sanitario figura como cancelado.
El modelo TxGNN predice que podría ser efectivo para el **trastorno por déficit de atención e hiperactividad, tipo inatento**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción. Se trata de una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Flavoxato (el registro no detalla una indicación clínica específica) |
| Nueva Indicación Predicha | Trastorno por déficit de atención e hiperactividad, tipo inatento |
| Puntaje de Predicción TxGNN | 99.75% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción original del fármaco. Según la información farmacológica conocida, el flavoxato es un relajante del músculo liso urinario con propiedades antimuscarínicas, inhibidoras de la fosfodiesterasa y antagonistas del calcio.

Para el TDAH de tipo inatento **no se identifica un vínculo mecanístico respaldado**. La fisiopatología del TDAH se asocia principalmente con la desregulación dopaminérgica y noradrenérgica, vías que no son blanco establecido del flavoxato. Además, la carga anticolinérgica suele relacionarse con deterioro cognitivo y no con beneficio. El puntaje alto de TxGNN es solo una predicción computacional.

### Otras predicciones del modelo (todas con nivel L5 y decisión Hold)

| Posición | Indicación predicha | Puntaje TxGNN | Plausibilidad mecanística |
|------|------|------|------|
| 2 | Síndrome del intestino irritable | 99.74% | Plausible pero no verificada: la actividad antimuscarínica y relajante del músculo liso se parece a la de antiespasmódicos aprobados (hioscina, diciclomina). Es la candidata más razonable para formular una pregunta de investigación. |
| 3 | Trastorno específico del desarrollo | 99.56% | Sin conexión identificable; probablemente por similitud de red con términos de TDAH. |
| 4 | TDAH (general) | 99.39% | Sin vínculo respaldado; concepto superpuesto con el TDAH inatento, no es evidencia independiente. |
| 5 | Síndrome de cauda equina | 99.27% | Indirecta: solo manejo sintomático de la vejiga, sin modificar la enfermedad. |
| 6 | Vejiga neurogénica (término obsoleto) | 99.13% | Coherente y cercana al uso urológico original, pero el término está obsoleto y no hay evidencia. |
| 7 | Gastroduodenitis | 99.12% | Débil. |
| 8 | Enfermedad ulcerosa péptica | 99.10% | Débil; los antimuscarínicos fueron reemplazados por inhibidores de la bomba de protones y erradicación de H. pylori. |

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20026026 | BLADURIL® 200 MG | Tableta recubierta | Flavoxato | Cancelado |

Fabricante: Recordati Ireland Limited. Vía de administración: oral.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** glaucoma de ángulo cerrado, estenosis pilórica, íleo paralítico, obstrucción intestinal, miopatía visceral familiar, enfermedad ulcerosa péptica activa y obstrucción de las vías urinarias.
- **Interacciones farmacológicas:** se identificaron 74 interacciones en total. Las de nivel **mayor** son con **citrato de potasio** y **cloruro de potasio**. Las de nivel **moderado** incluyen otros antimuscarínicos o anticolinérgicos (hiosciamina, atropina, glicopirronio, clidinio, diciclomina, trospio, mepenzolato, metescopolamina, propantelina, escopolamina), fármacos que afectan la motilidad gastrointestinal u opioides (loperamida, morfina, eluxadolina, metoclopramida, pramlintida, prucaloprida) y cannabinoides (dronabinol, nabilona).

Las advertencias y contraindicaciones del prospecto del INVIMA no están disponibles; consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (nivel L5), sin ensayos ni literatura, y no existe un vínculo mecanístico respaldado con el TDAH. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Obtener el mecanismo de acción desde DrugBank.
- Descargar y analizar el prospecto del INVIMA para completar el tamizaje de seguridad.
- Si se desea continuar, priorizar el síndrome del intestino irritable (o la vejiga neurogénica, más cercana a la indicación original) como hipótesis de investigación, con revisión sistemática de la literatura.
- Evaluar la viabilidad regulatoria dado que el registro está cancelado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

