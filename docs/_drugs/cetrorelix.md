---
layout: default
title: Cetrorelix
parent: Solo Predicción del Modelo (L5)
nav_order: 148
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Cetrorelix: nueva indicación predicha, Hipertricosis (nivel de evidencia L5). Indicación original: Cetrorelix"
monitor_inn: "cetrorelix"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "persistent fetal circulation syndrome", "familial isolated trichomegaly", "familial male-limited precocious puberty", "aromatase excess syndrome", "centra precocious puberty 1"]
---

# Cetrorelix
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Cetrorelix: De Inhibición del Pico Prematuro de LH a Hipertricosis

## Resumen en Una Frase

Cetrorelix es un antagonista del receptor de GnRH, utilizado para inhibir los picos prematuros de hormona luteinizante (LH) en mujeres sometidas a estimulación ovárica controlada como parte de un tratamiento de fertilidad.
El modelo TxGNN predice que podría ser efectivo para **hipertricosis**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cetrorelix (el registro sanitario solo indica el nombre del principio activo; el uso clínico conocido es la inhibición de picos prematuros de LH en estimulación ovárica controlada) |
| Nueva Indicación Predicha | Hipertricosis |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo cancelado (sin registros vigentes) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según la información farmacológica conocida, cetrorelix es un antagonista del receptor GnRH₁ (gen GNRHR) que suprime la liberación de LH y FSH y, en consecuencia, reduce las hormonas sexuales posteriores.

La supresión androgénica podría influir en el hirsutismo dependiente de andrógenos. Sin embargo, la hipertricosis suele ser independiente de los andrógenos, por lo que el vínculo mecanístico es débil. El puntaje TxGNN muy alto (99.98%) proviene de una predicción basada en grafos, sin respaldo clínico ni bibliográfico.

Otras predicciones del modelo muestran el mismo patrón: varias corresponden a síndromes congénitos o de desarrollo (síndrome de Ambras, anomalías del tallo piloso, tricomegalia familiar, malformación de Dandy-Walker, síndromes con componente dental/periodontal) sin relación biológica clara con el bloqueo de GnRH, y probablemente reflejan cercanía en la red del grafo de conocimiento. Las más afines a la farmacología de cetrorelix son la **pubertad precoz central** (el bloqueo del receptor de GnRH es mecanísticamente coherente, aunque el tratamiento estándar usa agonistas y la formulación de acción corta y el estado cancelado limitan su practicidad) y la **pubertad precoz familiar limitada al varón** (el mecanismo, basado en mutaciones activadoras de LHCGR, sugiere que no habría beneficio). Ambas están clasificadas como "pregunta de investigación".

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19908844 (cancelado) | CETROTIDE® 0.25MG (MERCK S.A.) | Polvo liofilizado para reconstituir a solución inyectable | CETRORELIX |

---

## Consideraciones de Seguridad

**Interacciones Farmacológicas**: la consulta se completó y solo devolvió información farmacológica de blanco (receptor GnRH₁, humano), no interacciones con otros fármacos.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para hipertricosis tiene un puntaje alto en el modelo, pero carece de ensayos clínicos y literatura (nivel L5), y el vínculo mecanístico es débil. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), actualmente un vacío bloqueante para la evaluación de seguridad
- Completar los datos del mecanismo de acción desde DrugBank
- Revisar la literatura preclínica y clínica sobre antagonistas de GnRH en trastornos de pilosidad
- Considerar priorizar la pubertad precoz central como hipótesis más coherente mecanísticamente, evaluando su viabilidad frente a los agonistas estándar
- Evaluar la compatibilidad de la vía de administración y la situación regulatoria en Colombia, dado que el producto está cancelado
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

