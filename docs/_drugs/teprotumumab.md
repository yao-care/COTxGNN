---
layout: default
title: Teprotumumab
parent: Solo Predicción del Modelo (L5)
nav_order: 378
evidence_level: L5
indication_count: 10
---

# Teprotumumab
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

# Teprotumumab: De Oftalmopatía Tiroidea a Monosomía X

## Resumen en Una Frase

Teprotumumab es un anticuerpo monoclonal que bloquea el receptor IGF-1R. Según conocimiento general (el registro colombiano solo consigna el nombre del principio activo), se usa en la oftalmopatía tiroidea.
El modelo TxGNN predice que podría ser efectivo para **monosomía X (síndrome de Turner)**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción.
Además, el mecanismo del fármaco iría en sentido contrario al tratamiento habitual de esa enfermedad.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto de indicación solo dice "TEPROTUMUMAB"); oftalmopatía tiroidea según conocimiento general |
| Nueva Indicación Predicha | Monosomía X |
| Puntaje de Predicción TxGNN | 99.79% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 2 entradas (ambas con el mismo número de registro, 20234945) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Hoy no se dispone de datos detallados del mecanismo de acción en el Evidence Pack. Lo que sí se sabe es que teprotumumab bloquea el receptor IGF-1R (receptor del factor de crecimiento similar a la insulina tipo 1).

En este caso la predicción **no resulta convincente desde lo mecanístico**. En la monosomía X (síndrome de Turner), la baja estatura se maneja reforzando la señal de la hormona de crecimiento y del IGF-1. Bloquear IGF-1R iría en la dirección opuesta y sería, en principio, contraproducente.

El alto puntaje (0.998) probablemente refleja la cercanía entre nodos en el grafo de conocimiento y no una relación biológica demostrada. Las otras nueve predicciones del top 10 también son solo de modelo (L5) y sin estudios. Seis de ellas pertenecen al mismo grupo de trastornos del cromosoma X (síndrome de Turner por anomalías estructurales, monosomía X en mosaico, disgenesia gonadal mixta, entre otras) y están correlacionadas entre sí. Las demás (várices esofágicas, enfermedad varicosa, trastorno mitocondrial) tampoco tienen un vínculo plausible con la inhibición de IGF-1R.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20234945 | TEPEZZA® 500MG (Amgen Biotecnológica S.A.S.) | Polvo liofilizado para reconstituir a solución inyectable | Solo figura el nombre del principio activo (TEPROTUMUMAB) |

Las dos entradas del registro son idénticas, por eso se muestran una sola vez.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5), sin ensayos ni literatura. Además, el bloqueo de IGF-1R es mecanísticamente contrario al manejo del síndrome de Turner, así que no se justifica avanzar.

**Para avanzar se necesita:**
- Una justificación biológica que explique por qué inhibir IGF-1R podría beneficiar a la monosomía X, o evidencia preclínica que la respalde
- Descargar y revisar el prospecto de INVIMA (advertencias y contraindicaciones), hoy sin datos
- Confirmar la indicación aprobada en Colombia, ya que el registro solo lista el nombre del principio activo
- Datos del mecanismo de acción desde DrugBank
- Reevaluar solo si aparecen ensayos clínicos o publicaciones relevantes
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

