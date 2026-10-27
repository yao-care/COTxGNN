---
layout: default
title: Loxoprofen
parent: Solo Predicción del Modelo (L5)
nav_order: 415
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Loxoprofen: nueva indicación predicha, Síndrome de microftalmia colobomatosa con displasia rizomélica (nivel de evidencia L5). Indicación original: Loxoprofeno"
monitor_inn: "loxoprofen"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome"]
---

# Loxoprofen
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Loxoprofeno: De Loxoprofeno (AINE) a Síndrome de Microftalmia Colobomatosa con Displasia Rizomélica
{: .text-alpha }

## Resumen en Una Frase

Loxoprofeno es un antiinflamatorio no esteroideo (AINE) registrado en Colombia como tabletas de 60 mg (LOXONIN 60 MG), cuyo registro sanitario se encuentra cancelado.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de microftalmia colobomatosa con displasia rizomélica**, con un puntaje alto pero con **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Loxoprofeno (el registro no detalla una indicación específica) |
| Nueva Indicación Predicha | Síndrome de microftalmia colobomatosa con displasia rizomélica |
| Puntaje de Predicción TxGNN | 99.80% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, loxoprofeno es un profármaco AINE cuyo metabolito activo (trans-alcohol) inhibe la ciclooxigenasa 1 y 2 (COX-1 y COX-2), con efecto analgésico y antiinflamatorio.

La nueva indicación es un síndrome congénito extremadamente raro, con malformaciones oculares y esqueléticas. La inhibición de COX no tiene un papel establecido en su patogenia, por lo que **los datos compilados no respaldan un vínculo mecanístico**. El puntaje de TxGNN (0.998) proviene únicamente de una predicción sobre el grafo de conocimiento, sin respaldo clínico ni bibliográfico.

Además, el fármaco solo tiene un registro cancelado en Colombia, por lo que no existe una vía comercial o regulatoria vigente.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20089378 | LOXONIN 60 MG | Tableta | LOXOPROFEN | Cancelado |

Fabricante: Daiichi Sankyo Brasil Farmacêutica Ltda. Vía de administración: oral.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como consideración contextual, la exposición a AINE durante el embarazo es una preocupación de seguridad en el marco de trastornos del desarrollo. No se encontraron interacciones farmacológicas en la consulta realizada.

## Candidato Alternativo Evaluado

Para completar el análisis, se evaluó también la segunda predicción:

| Item | Contenido |
|------|------|
| Indicación Predicha | Síndrome de braquidactilia-sindactilia |
| Puntaje TxGNN | 99.75% |
| Nivel de Evidencia | L5 |
| Ensayos clínicos / Publicaciones | 0 / 0 |
| Decisión | Hold |

Se trata de malformaciones congénitas de las extremidades, generalmente de origen genético. No se espera que la acción antiinflamatoria o analgésica modifique la condición estructural subyacente.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo computacional, sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico plausible entre la inhibición de COX y un síndrome del desarrollo congénito. Además, el único registro sanitario está cancelado.

**Para avanzar se necesita:**
- Datos del mecanismo de acción confirmados (por ejemplo, desde DrugBank)
- Información de advertencias y contraindicaciones del prospecto de INVIMA
- Evidencia preclínica o de literatura que sustente un vínculo biológico con la enfermedad
- Evaluación de la vía regulatoria, dado que el registro está cancelado
- Evaluación de seguridad específica, dado el riesgo de los AINE en el desarrollo fetal
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

