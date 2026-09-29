---
layout: default
title: Agomelatine
parent: Solo Predicción del Modelo (L5)
nav_order: 30
evidence_level: L5
indication_count: 10
---

# Agomelatine
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

# Agomelatina: De Trastorno Depresivo Mayor a Tortícolis Paroxística Benigna de la Infancia

## Resumen en Una Frase

Agomelatina es un antidepresivo (comercializado como Valdoxan®) que se usa para el trastorno depresivo mayor.
El modelo TxGNN predice que podría ser efectivo para la **tortícolis paroxística benigna de la infancia**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trastorno depresivo mayor (según los datos de farmacología; el registro sanitario solo indica "AGOMELATINA") |
| Nueva Indicación Predicha | Tortícolis paroxística benigna de la infancia |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro de origen. Según el conocimiento farmacológico general, agomelatina es agonista de los receptores de melatonina MT1 y MT2 y antagonista del receptor de serotonina 5-HT2C. Su eficacia en la depresión mayor está establecida y es su uso autorizado.

La tortícolis paroxística benigna de la infancia es un trastorno pediátrico episódico, similar a una canalopatía, que a menudo se asocia con variantes del gen CACNA1A. No se identificó ninguna vía plausible que conecte la farmacología de agomelatina (ritmos circadianos, modulación serotoninérgica y dopaminérgica frontocortical) con esta enfermedad.

El puntaje alto (99.96%) proviene solo de la proximidad en el grafo de conocimiento, no de evidencia clínica ni mecanística. Por eso esta predicción debe leerse como una señal computacional sin sustento farmacológico visible.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Hay 20 registros sanitarios en total. Los 5 primeros devueltos son entradas idénticas del mismo registro, por lo que se muestra una sola fila.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20014920 | VALDOXAN® 25 MG (Les Laboratoires Servier) | Comprimido | AGOMELATINA (el registro no detalla la indicación) |

## Consideraciones de Seguridad

- **Interacciones farmacológicas:** la consulta se completó, pero los 5 resultados son dianas farmacológicas de agomelatina, no interacciones con otros fármacos. Son los receptores 5-HT2A (HTR2A), 5-HT2B (HTR2B), 5-HT2C (HTR2C), MT1 (MTNR1A) y MT2 (MTNR1B). No hay niveles de severidad de interacciones.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ensayos clínicos ni literatura, y no se identificó un vínculo mecanístico plausible con una enfermedad episódica de tipo canalopatía en niños. El puntaje alto del modelo por sí solo no basta para avanzar.

**Para avanzar se necesita:**
- Datos del mecanismo de acción desde DrugBank
- Prospecto de INVIMA con advertencias y contraindicaciones, para el tamizaje de seguridad
- Si se busca una línea de investigación con mayor respaldo, priorizar otras predicciones del mismo fármaco: melancolía, depresión neurótica y trastorno distímico (L4, "Research Question"). Las dos primeras coinciden con el uso ya autorizado, por lo que no serían un reposicionamiento propiamente dicho, y la evidencia disponible es en su mayoría de clase o de revisión, sin ensayos específicos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

