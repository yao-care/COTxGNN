---
layout: default
title: Etofenamate
parent: Solo Predicción del Modelo (L5)
nav_order: 188
evidence_level: L5
indication_count: 10
---

# Etofenamate
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

# Etofenamato: De Antiinflamatorio (indicación original no especificada) a Espondiloartropatía (susceptibilidad)

## Resumen en Una Frase

Etofenamato es un antiinflamatorio no esteroideo (AINE) del grupo de los fenamatos. En Colombia se comercializa como solución inyectable, pero los registros disponibles no detallan su indicación original.
El modelo TxGNN predice que podría ser efectivo para **espondiloartropatía (susceptibilidad genética)**, con **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción.
La segunda predicción, **espondilitis anquilosante**, cuenta con un único estudio farmacocinético indirecto.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | ETOFENAMATO (el registro solo repite el nombre del principio activo y no describe una indicación) |
| Nueva Indicación Predicha | Espondiloartropatía, susceptibilidad a (etiqueta de predisposición genética) |
| Puntaje de Predicción TxGNN | 99.9996% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información recibida. Etofenamato es un AINE de la clase de los fenamatos, que actúa por inhibición de la ciclooxigenasa (COX). Los AINE son tratamiento sintomático de primera línea en las espondiloartritis, por lo que existe un vínculo biológico plausible.

Sin embargo, la primera predicción es una etiqueta de **predisposición genética**, no un estado clínico tratable. Un AINE podría aliviar los síntomas inflamatorios de una espondiloartritis, pero ningún dato respalda este término específico. El puntaje alto del modelo no equivale a evidencia clínica.

La predicción más coherente con el mecanismo es la de **espondilitis anquilosante** (rango 2, puntaje 99.9984%). Aun así, su respaldo se limita a evidencia indirecta, como se detalla más abajo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la primera predicción.

**Evidencia indirecta para la segunda predicción (espondilitis anquilosante):**

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [11455681](https://pubmed.ncbi.nlm.nih.gov/11455681/) | 2001 | Estudio farmacocinético | Arzneimittel-Forschung | Tras 5 días de iontoforesis con gel de etofenamato (100 mg/día) en 11 pacientes con dolor lumbar y 13 con sinovitis de rodilla, se midió el fármaco en suero y líquido sinovial. Demuestra penetración tisular, pero no eficacia ni seguridad en espondilitis anquilosante. |

## Información de Mercado en Colombia

Los 5 registros listados en los datos corresponden al mismo número de registro sanitario (20069025), repetido. El total declarado es de 20.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20069025 | ETOFENAMATO 1G/2ML (Laboratorios MK S.A.S) | Solución inyectable | ETOFENAMATO (sin texto de indicación descriptivo) |

**Nota de vía de administración:** la única forma farmacéutica registrada es inyectable. La evidencia farmacocinética disponible corresponde a un gel tópico aplicado por iontoforesis. La compatibilidad de vía para las indicaciones predichas está pendiente de evaluar.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal es solo del modelo (nivel L5): es una etiqueta genética sin estado clínico tratable, sin ensayos ni literatura. La predicción de espondilitis anquilosante es más plausible (L4), pero su único respaldo es un estudio de penetración tisular con otra vía de administración.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), ya que sin él no es posible el tamizaje de seguridad.
- Consultar el mecanismo de acción en DrugBank para sustentar el análisis mecanístico.
- Aclarar la indicación original real del producto inyectable registrado.
- Reorientar la evaluación hacia espondilitis anquilosante y buscar estudios de eficacia y seguridad de etofenamato en esa condición.
- Evaluar la compatibilidad de vía de administración (inyectable frente a tópica).

*Este informe es solo de referencia para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

