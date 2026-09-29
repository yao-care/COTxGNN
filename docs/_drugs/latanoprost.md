---
layout: default
title: Latanoprost
parent: Solo Predicción del Modelo (L5)
nav_order: 243
evidence_level: L5
indication_count: 10
---

# Latanoprost
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

# Latanoprost: De Glaucoma e Hipertensión Ocular a Glaucoma Hereditario Primario

## Resumen en Una Frase

Latanoprost es un análogo de la prostaglandina F2-alfa que se usa en gotas oftálmicas, y según su uso conocido se emplea contra el glaucoma y la hipertensión ocular.
El modelo TxGNN predice que podría ser efectivo para **glaucoma hereditario primario**,
con **1 ensayo clínico** (Fase 2, completado) y **0 publicaciones** que respaldan esta dirección.
Esta predicción se parece más a una extensión de población (formas hereditarias o pediátricas) que a un reposicionamiento propiamente dicho.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Glaucoma e hipertensión ocular (uso conocido). El texto del registro INVIMA solo dice "LATANOPROST", sin indicación explícita |
| Nueva Indicación Predicha | Glaucoma hereditario primario |
| Puntaje de Predicción TxGNN | 99.88% |
| Nivel de Evidencia | L2 (provisional) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información conocida, latanoprost es agonista del receptor FP de prostaglandinas. Reduce la presión intraocular al aumentar el drenaje del humor acuoso por la vía uveoescleral, y esa presión elevada es el principal factor de riesgo modificable del glaucoma.

La indicación original (glaucoma e hipertensión ocular) y la nueva (glaucoma hereditario primario) comparten el mismo problema de fondo, que es la presión intraocular alta. Lo que cambia es la causa, en este caso genética. Por eso el puntaje tan alto del modelo es coherente con el mecanismo.

Un punto de cautela es que la respuesta en formas hereditarias o pediátricas, refractarias a cirugía, es menos predecible que en el glaucoma del adulto. El único ensayo disponible usa además una terapia combinada, así que no aísla el efecto del latanoprost.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01527682](https://clinicaltrials.gov/study/NCT01527682) | Fase 2 | Completado | 37 | Evalúa el efecto hipotensor ocular de latanoprost (análogo de prostaglandina) y dorzolamida (inhibidor de anhidrasa carbónica) en glaucoma pediátrico primario refractario a cirugía, además de su seguridad. El protocolo se modificó de 96 a 68 ojos. Relevancia: B |

El diseño combina dos fármacos y la muestra es pequeña. Además, el título del ensayo está truncado, por lo que no se puede confirmar la población exacta (hereditaria o congénita) ni el comparador.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Se registraron 20 licencias en total. Las cinco entradas de muestra corresponden al mismo registro, por lo que se presenta una sola fila.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19947216 | LATANOX® (PROCAPS S.A.) | Solución oftálmica | LATANOPROST (el registro solo indica el principio activo, sin texto de indicación) |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

No se encontraron interacciones farmacológicas en la consulta realizada.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
El mecanismo es directo y el fármaco ya está comercializado en Colombia en forma oftálmica. Existe además un ensayo de Fase 2 completado en glaucoma pediátrico. Sin embargo, la evidencia es limitada (un solo ensayo con terapia combinada, sin literatura) y falta la información de seguridad del prospecto, por lo que se recomienda avanzar solo con salvaguardas.

**Para avanzar se necesita:**
- Descargar y revisar el prospecto de INVIMA (advertencias y contraindicaciones), que es un requisito para la evaluación de seguridad
- Consultar el registro completo del ensayo NCT01527682 para confirmar la población, el comparador y la contribución específica del latanoprost
- Obtener datos de mecanismo de acción desde DrugBank
- Corregir el campo de indicaciones originales, que está vacío, ya que la predicción es en la práctica una extensión de población
- Revisar la literatura sobre uso de latanoprost en glaucoma pediátrico y hereditario

**Nota sobre otras predicciones:** las otras nueve predicciones del modelo (por ejemplo, calcifilaxis visceral, síndromes del desierto torácico, hipotricosis) tienen nivel L5 y decisión Hold. Solo la hipotricosis del cuero cabelludo tiene un fundamento biológico plausible, por el efecto conocido de las prostaglandinas sobre el crecimiento del pelo, pero no hay evidencia clínica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

