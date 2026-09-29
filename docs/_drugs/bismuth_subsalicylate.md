---
layout: default
title: Bismuth Subsalicylate
parent: Solo Predicción del Modelo (L5)
nav_order: 92
evidence_level: L5
indication_count: 10
---

# Bismuth Subsalicylate
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

# Subsalicilato de Bismuto: De Indicación No Especificada en el Registro a Fiebre Paratifoidea

## Resumen en Una Frase

El subsalicilato de bismuto es un compuesto de bismuto usado ampliamente en trastornos gastrointestinales. En los datos suministrados, su registro sanitario en Colombia solo menciona "bismuto subcitrato" y no una indicación clara.
El modelo TxGNN predice que podría ser efectivo para la **fiebre paratifoidea**, pero hoy hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta indicación. Es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada. El texto del registro sanitario dice solo "Bismuto subcitrato", que es un principio activo y no una indicación |
| Nueva Indicación Predicha | Fiebre paratifoidea (paratyphoid fever) |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de este fármaco en el material suministrado. Lo que sí se sabe es que el subsalicilato de bismuto es una sal poco soluble en agua, de uso común en trastornos gastrointestinales. Un estudio in vitro (PMID 2694949) mostró que se une a bacterias de especies diversas y luego las elimina. Esto sugiere una posible extrapolación a infecciones por *Salmonella*.

La fiebre paratifoidea es una fiebre entérica, es decir, una infección sistémica que pasa a la sangre. El subsalicilato de bismuto actúa sobre todo de forma local en el intestino y tiene poca actividad fuera de la luz intestinal. Por eso el vínculo mecanístico es débil: la actividad antibacteriana local no garantiza eficacia en una infección sistémica.

Además, el puntaje alto de TxGNN no está respaldado por ningún ensayo ni publicación en los datos recibidos. Debe leerse como una hipótesis para explorar, no como evidencia de eficacia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Otras Indicaciones Predichas por TxGNN

Ninguna de estas predicciones cuenta con ensayos clínicos registrados. Solo dos tienen literatura de apoyo, indirecta y de nivel preclínico o histórico.

| Rango | Indicación | Puntaje | Nivel | Recomendación | Evidencia disponible |
|------|------|------|------|------|------|
| 2 | Esclerodermia difusa | 99.96% | L5 | Hold | Ninguna; no se identifica un vínculo mecanístico plausible |
| 3 | Salmonelosis | 99.95% | L4 | Pregunta de investigación | 6 publicaciones indirectas: un estudio in vitro de unión y muerte bacteriana ([2694949](https://pubmed.ncbi.nlm.nih.gov/2694949/), 1989), revisiones sobre diarrea del viajero y diarrea aguda, y un estudio veterinario en terneros. Ninguna es evidencia clínica humana específica para *Salmonella* |
| 4 | Fiebre tifoidea | 99.92% | L5 | Hold | Ninguna; misma limitación sistémica que la paratifoidea |
| 5 | Conjuntivitis | 99.92% | L5 | Hold | Ninguna; sin datos de formulación oftálmica |
| 6 | Fiebre recurrente | 99.85% | L5 | Hold | Ninguna |
| 7 | Conjuntivitis contagiosa aguda | 99.84% | L5 | Hold | Ninguna |
| 8 | Gingivitis | 99.75% | L4 | Pregunta de investigación | 4 publicaciones: 2 estudios preclínicos ([28837052](https://pubmed.ncbi.nlm.nih.gov/28837052/), 2017; [34038883](https://pubmed.ncbi.nlm.nih.gov/34038883/), 2021) y 2 informes clínicos históricos de 1946 sobre angina de Vincent, uno de ellos duplicado |
| 9 | Queratoconjuntivitis epitelial punteada | 99.74% | L5 | Hold | Ninguna |
| 10 | Otitis externa | 99.68% | L5 | Hold | Ninguna; sin datos de formulación ótica |

## Información de Mercado en Colombia

Los 5 registros detallados en los datos corresponden al mismo número de registro sanitario (1991423), así que se muestran una sola vez. El total reportado es de 20 registros. Además de la suspensión oral, existe una forma de tableta masticable.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1991423 | BISBACTER® SUSPENSION (Laboratorio Franco Colombiano - Lafrancol S.A.S.) | Suspensión oral | Bismuto subcitrato (el texto no describe una indicación clínica) |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para fiebre paratifoidea es de nivel L5: solo puntaje del modelo, sin ensayos ni publicaciones. Además, el mecanismo local en el intestino es poco compatible con una infección sistémica. Las señales más defendibles del conjunto, salmonelosis y gingivitis (nivel L4), son indirectas y preclínicas.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA y sus advertencias y contraindicaciones, requisito previo a cualquier evaluación de seguridad.
- Completar los datos del mecanismo de acción (por ejemplo, consultando la API de DrugBank).
- Aclarar la indicación original, porque el registro sanitario menciona "bismuto subcitrato" y no subsalicilato.
- Reunir estudios clínicos de *Salmonella* en humanos, o priorizar salmonelosis intestinal (L4) sobre la fiebre entérica sistémica.
- Verificar la compatibilidad de vía de administración y formulación, hoy pendiente para todas las indicaciones.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

