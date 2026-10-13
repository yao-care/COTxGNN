---
layout: default
title: Itopride
parent: Solo Predicción del Modelo (L5)
nav_order: 360
evidence_level: L5
indication_count: 4
---

# Itopride
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Itopride: De Itoprida (procinético) a Enfermedad de Crohn del Intestino Delgado

## Resumen en Una Frase

Itopride es un procinético gastrointestinal registrado en Colombia bajo el nombre comercial PRIDOT®, cuyo registro sanitario figura únicamente como cancelado.
El modelo TxGNN predice que podría ser efectivo para **enfermedad de Crohn del intestino delgado**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; es una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Itoprida (el registro no detalla una indicación clínica específica) |
| Nueva Indicación Predicha | Enfermedad de Crohn del intestino delgado |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin producto vigente) |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción registrado. Según el conocimiento farmacológico general, itopride es un antagonista del receptor de dopamina D2 y un inhibidor de la acetilcolinesterasa, que estimula la motilidad del tracto digestivo superior.

No se ha establecido un vínculo mecanístico plausible entre este mecanismo y la inflamación transmural de origen inmunológico de la enfermedad de Crohn. El puntaje alto del modelo (99.90%) proviene de asociaciones en un grafo de conocimiento y no está respaldado por ningún ensayo ni publicación. Además, un procinético podría estar contraindicado en estenosis u obstrucción, complicaciones frecuentes en el Crohn del intestino delgado.

### Otras predicciones del modelo

Todas las predicciones restantes también tienen nivel de evidencia L5, sin ensayos ni literatura, y recomendación Hold:

| Posición | Enfermedad | Puntaje TxGNN | Comentario |
|------|------|------|------|
| 2 | Insuficiencia venosa | 99.23% | Sin conexión farmacológica clara; probablemente producto de asociaciones indirectas del grafo. |
| 3 | Aclorhidria | 99.16% | Vínculo débil: itopride podría aliviar síntomas dispépticos, pero no trata la pérdida de secreción ácida. |
| 4 | Hernia de hiato | 99.02% | La más plausible biológicamente (posible mejoría del vaciamiento gástrico y del tono del esfínter esofágico inferior), aunque el beneficio sería solo sintomático. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20199458 (cancelado) | PRIDOT® | Tableta recubierta | Itoprida |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no cuenta con ensayos clínicos ni literatura (nivel L5) y carece de un vínculo mecanístico plausible con la enfermedad de Crohn. Además, el único registro sanitario en Colombia está cancelado, y el uso de un procinético podría ser riesgoso en presencia de estenosis u obstrucción.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto del INVIMA (advertencias y contraindicaciones), indispensable para cualquier evaluación de seguridad
- Complementar los datos del mecanismo de acción desde DrugBank
- Realizar una revisión sistemática de la literatura y de registros de ensayos para cada indicación predicha
- Priorizar, si se continúa el análisis, la hernia de hiato como indicación biológicamente más plausible
- Evaluar la viabilidad regulatoria, dado que no existe un producto vigente en el mercado colombiano
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

