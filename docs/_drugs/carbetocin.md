---
layout: default
title: Carbetocin
parent: Solo Predicción del Modelo (L5)
nav_order: 136
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Carbetocin: nueva indicación predicha, Síndrome similar a la isotretinoína (nivel de evidencia L5). Indicación original: Carbetocina"
monitor_inn: "carbetocin"
predicted_indications: ["isotretinoin-like syndrome", "Goodman syndrome"]
---

# Carbetocin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Carbetocina: De Carbetocina (indicación sin detallar en el registro) a Síndrome similar a la isotretinoína

## Resumen en Una Frase

Carbetocina es un análogo de acción prolongada de la oxitocina, utilizado para provocar la contracción uterina y prevenir la hemorragia posparto por atonía uterina.
El modelo TxGNN predice que podría ser efectivo para el **síndrome similar a la isotretinoína**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Carbetocina (el registro sanitario solo indica el nombre del principio activo, sin texto de indicación detallado; el uso clínico conocido es la prevención de hemorragia posparto por atonía uterina) |
| Nueva Indicación Predicha | Síndrome similar a la isotretinoína |
| Puntaje de Predicción TxGNN | 99.15% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo cancelado (sin registros vigentes) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información farmacológica compilada, la carbetocina es un péptido agonista del receptor de oxitocina (OXTR), con efecto uterotónico de acción prolongada. Su uso establecido es la prevención de la hemorragia posparto. También se menciona una formulación intranasal en desarrollo para el síndrome de Prader-Willi, dirigida a reducir el hambre extrema.

El síndrome similar a la isotretinoína (malformaciones por embriopatía por ácido retinoico) es un trastorno del desarrollo sin una vía conocida que involucre al receptor de oxitocina. Los datos compilados **no sustentan ningún vínculo mecanístico** entre ambas condiciones.

El puntaje alto (99.15%) proviene solo del grafo de conocimiento y no está respaldado por evidencia clínica ni bibliográfica. Sin datos de mecanismo de acción original, no es posible verificar el razonamiento mecanístico. La predicción debe considerarse con mucha cautela.

**Otra predicción del modelo:** el síndrome de Goodman (puntaje 99.06%, rango 13383), una malformación congénita craneofacial y de extremidades, tampoco tiene ensayos, literatura ni vínculo con la señalización de oxitocina. También se clasifica como L5 y Hold, y su plausibilidad biológica es baja.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19984250 | DURATOCIN® 100 MCG/ML SOLUCION INYECTABLE (Ferring GmbH) – Cancelado | Solución inyectable | Carbetocina |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas:** solo se identificó una entrada farmacológica (no es una interacción medicamentosa clínica): la carbetocina actúa como ligando del receptor de oxitocina (OXTR), su diana principal. No hay datos de interacciones con otros fármacos.

No se dispone de advertencias ni contraindicaciones del prospecto. Consultar el prospecto para más información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo TxGNN (nivel L5), sin ensayos ni literatura, y sin un vínculo mecanístico plausible entre un agonista del receptor de oxitocina y un síndrome malformativo del desarrollo. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Datos del mecanismo de acción original y análisis de una posible vía biológica hacia la nueva indicación
- Revisión de literatura preclínica que justifique la hipótesis
- Descarga y análisis del prospecto de INVIMA para advertencias y contraindicaciones
- Evaluación de compatibilidad de vía de administración y de la viabilidad de reposicionar un uterotónico en una condición congénita
- Aclarar la situación regulatoria local, dado que no hay registros vigentes
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

