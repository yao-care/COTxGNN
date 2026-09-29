---
layout: default
title: Silodosin
parent: Solo Predicción del Modelo (L5)
nav_order: 360
evidence_level: L5
indication_count: 6
---

# Silodosin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Silodosina: De Hiperplasia Prostática Benigna a Hipertricosis Universal Congénita tipo Ambras

## Resumen en Una Frase

Silodosina es un antagonista selectivo de los receptores alfa-1A adrenérgicos, utilizado originalmente para mejorar el flujo urinario en la hiperplasia prostática benigna (HPB).
El modelo TxGNN predice que podría ser efectivo para la **hipertricosis universal congénita tipo Ambras**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hiperplasia prostática benigna (según la farmacología del fármaco; el texto del registro INVIMA solo dice "SILODOSINA") |
| Nueva Indicación Predicha | Hipertricosis universal congénita tipo Ambras |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Silodosina bloquea de forma selectiva el receptor adrenérgico alfa-1A (gen *ADRA1A*). Los datos farmacológicos también registran interacción con los receptores alfa-1B y alfa-1D. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la ficha del fármaco. Su eficacia en HPB está comprobada y es su uso principal.

Con la información actual, **la predicción no tiene un respaldo mecanístico claro**. El síndrome de Ambras es un trastorno congénito asociado a reordenamientos genómicos en 8q22, que afectan la regulación de *TRPS1*. No se conoce ninguna vía que conecte el bloqueo alfa-1A con ese mecanismo.

El puntaje alto (0.9999) proviene solo de la estructura del grafo de conocimiento. Otras predicciones cercanas del modelo (hipertricosis general, anomalías del tallo piloso, tricomegalia familiar, síndromes malformativos) tampoco tienen evidencia clínica. En la hipertricosis general, además, no está claro si el efecto sería tratarla o inducirla.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20070804 | SILOTRIF® 4 MG CAPSULAS (MSN Laboratories Private Limited) | Cápsula dura | SILODOSINA (el texto registrado no detalla la indicación) |

Nota: el registro mostró cinco entradas idénticas para este mismo número, por lo que se presenta una sola fila. El total informado es de 20 registros.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es de nivel L5 (solo modelo), sin ensayos, sin literatura y sin vínculo mecanístico plausible entre el bloqueo alfa-1A y un trastorno genético congénito del desarrollo. No se recomienda avanzar con los datos actuales.

**Para avanzar se necesita:**
- Una hipótesis mecanística documentada que conecte la señalización alfa-1 con la biología de *TRPS1* o del folículo piloso.
- Estudios preclínicos o de mecanismo que apoyen la predicción.
- El prospecto de INVIMA (advertencias y contraindicaciones) para completar el análisis de seguridad.
- La indicación aprobada en Colombia con texto explícito y los datos de mecanismo de acción desde DrugBank.
- Definir la dirección del efecto (tratar frente a inducir crecimiento de vello), en caso de que se revisen las predicciones de hipertricosis.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

