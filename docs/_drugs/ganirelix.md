---
layout: default
title: Ganirelix
parent: Solo Predicción del Modelo (L5)
nav_order: 309
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-29
description: "Ganirelix: nueva indicación predicha, Hipertricosis (nivel de evidencia L5). Indicación original: Ganirelix"
monitor_inn: "GANIRELIX"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial male-limited precocious puberty", "persistent fetal circulation syndrome", "aromatase excess syndrome", "centra precocious puberty 1", "familial isolated trichomegaly"]
---

# Ganirelix
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

## Ganirelix: De Prevención de Ovulación Prematura (Indicación Aprobada no Detallada) a Hipertricosis
{: .text-alpha }

## Resumen en Una Frase

Ganirelix es un antagonista del receptor de GnRH. En Colombia el registro sanitario solo consigna el nombre del principio activo como indicación; su uso conocido es evitar la ovulación prematura en mujeres sometidas a estimulación ovárica durante tratamientos de fertilidad.
El modelo TxGNN predice que podría ser efectivo para **hipertricosis**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es solo una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Ganirelix (el registro no detalla el texto de la indicación; el uso conocido es prevenir la ovulación prematura en estimulación ovárica) |
| Nueva Indicación Predicha | Hipertricosis |
| Puntaje de Predicción TxGNN | 0.9998 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Autorizado pero no comercializado (registros: 1) |
| Número de Registros Sanitarios | 1 (vigentes: 0) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Ganirelix es un péptido antagonista del receptor de GnRH (GnRH₁, gen GNRHR). Al bloquear este receptor, suprime la liberación de LH y FSH y, por consiguiente, reduce la producción de esteroides sexuales gonadales. Los datos compilados para este reporte no incluyen una descripción detallada del mecanismo de acción registrada en la base de datos, por lo que esta descripción se basa en la información farmacológica disponible.

La relación con la hipertricosis es **especulativa**. La hipertricosis no se explica clásicamente por el eje gonadotrópico (a diferencia del hirsutismo, que depende de andrógenos), por lo que no hay una razón mecanística clara para que suprimir el eje GnRH la modifique. El puntaje muy alto del modelo TxGNN (deep learning) (0.9998) puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica, farmacológica ni clínica.

Como contexto, otras predicciones del modelo para este fármaco incluyen la pubertad precoz central, que es la más coherente mecanísticamente (bloqueo del eje hipotálamo-hipófisis-gonadal). Sin embargo, ganirelix es de acción corta y no tiene formulación de depósito, lo que limita su uso práctico. También aparecen la pubertad precoz familiar limitada al varón y el síndrome de exceso de aromatasa, clasificados como preguntas de investigación. Ninguna cuenta con ensayos ni literatura en los datos compilados.

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
| 20254283 (cancelado) | NOVOLEX 0.25 MG/0.5 ML solución inyectable en jeringa precargada (GEDEON RICHTER PLC) | Solución inyectable | Ganirelix |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 7 registros de interacción. Seis son de nivel moderado y provienen de la base DDInter: gonadorelina, gonadotropina coriónica humana, menotropinas, triptorelina, folitropina y urofolitropina. El séptimo es la entrada farmacológica del propio ganirelix sobre el receptor GnRH₁, sin nivel de interacción asignado. En general se trata de otros fármacos que actúan sobre el eje reproductivo, por lo que la combinación debe valorarse con cuidado.

No se dispone de datos de advertencias ni contraindicaciones del prospecto; consultar el prospecto para esa información. Tampoco se identificaron contraindicaciones enfermedad-fármaco en el grafo de conocimiento.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para hipertricosis es solo del modelo (L5), sin ensayos ni literatura, y carece de un vínculo mecanístico plausible. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA para completar advertencias y contraindicaciones.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una revisión de literatura dirigida y evaluar la plausibilidad biológica antes de cualquier estudio.
- Priorizar, como línea de investigación más coherente, la pubertad precoz central, considerando las limitaciones de la formulación de acción corta.
- Aclarar la situación regulatoria (registro cancelado) y la compatibilidad de vías de administración.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

