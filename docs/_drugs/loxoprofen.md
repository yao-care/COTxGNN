---
layout: default
title: Loxoprofen
parent: Solo Predicción del Modelo (L5)
nav_order: 415
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-12
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

Loxoprofeno es un antiinflamatorio no esteroideo (AINE) registrado en Colombia como tabletas de 60 mg (LOXONIN 60 MG).
El modelo TxGNN predice que podría ser efectivo para el **síndrome de microftalmia colobomatosa con displasia rizomélica**, con un puntaje alto pero con **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

<!-- review:begin co-lic-20261105-loxoprofen-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Loxoprofeno es un antiinflamatorio no esteroideo (AINE) registrado en Colombia como tabletas de 60 mg (LOXONIN 60 MG), cuyo registro sanitario se encuentra cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-loxoprofen-2 -->

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Loxoprofeno (el registro no detalla una indicación específica) |
| Nueva Indicación Predicha | Síndrome de microftalmia colobomatosa con displasia rizomélica |
| Puntaje de Predicción TxGNN | 0.9980 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, loxoprofeno es un profármaco AINE cuyo metabolito activo (trans-alcohol) inhibe la ciclooxigenasa 1 y 2 (COX-1 y COX-2), con efecto analgésico y antiinflamatorio.

La nueva indicación es un síndrome congénito extremadamente raro, con malformaciones oculares y esqueléticas. La inhibición de COX no tiene un papel establecido en su patogenia, por lo que **los datos compilados no respaldan un vínculo mecanístico**. El puntaje de TxGNN (0.998) proviene únicamente de una predicción del modelo TxGNN (aprendizaje profundo), sin respaldo clínico ni bibliográfico.

<!-- review:begin co-lic-20261031-loxoprofen-1 -->

> **Corrección de revisión (2026-10-31)**: Texto original: "Además, el fármaco solo tiene un registro cancelado en Colombia, por lo que no existe una vía comercial o regulatoria vigente." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-10-31. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261031-loxoprofen-1 -->

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20089378 | LOXONIN 60 MG | Tableta | LOXOPROFEN | Vigente |

Fabricante: Daiichi Sankyo Brasil Farmacêutica Ltda. Vía de administración: oral.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como consideración contextual, la exposición a AINE durante el embarazo es una preocupación de seguridad en el marco de trastornos del desarrollo. No se encontraron interacciones farmacológicas en la consulta realizada.

## Candidato Alternativo Evaluado

Para completar el análisis, se evaluó también la segunda predicción:

| Item | Contenido |
|------|------|
| Indicación Predicha | Síndrome de braquidactilia-sindactilia |
| Puntaje TxGNN | 0.9975 |
| Nivel de Evidencia | L5 |
| Ensayos clínicos / Publicaciones | 0 / 0 |
| Decisión | Hold |

Se trata de malformaciones congénitas de las extremidades, generalmente de origen genético. No se espera que la acción antiinflamatoria o analgésica modifique la condición estructural subyacente.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo computacional, sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico plausible entre la inhibición de COX y un síndrome del desarrollo congénito.

<!-- review:begin co-lic-20261105-loxoprofen-3 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción se basa únicamente en el modelo computacional, sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico plausible entre la inhibición de COX y un síndrome del desarrollo congénito. Además, el único registro sanitario está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-loxoprofen-3 -->

**Para avanzar se necesita:**
- Datos del mecanismo de acción confirmados (por ejemplo, desde DrugBank)
- Información de advertencias y contraindicaciones del prospecto de INVIMA
- Evidencia preclínica o de literatura que sustente un vínculo biológico con la enfermedad
- Evaluación de la vía regulatoria
- Evaluación de seguridad específica, dado el riesgo de los AINE en el desarrollo fetal

<!-- review:begin co-lic-20261105-loxoprofen-4 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Evaluación de la vía regulatoria, dado que el registro está cancelado" Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-loxoprofen-4 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-10-31 | Eliminado: "Además, el fármaco solo tiene un registro cancelado en Colombia, por lo que no existe una vía comercial o regulatoria vigente" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "cuyo registro sanitario se encuentra cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Además, el único registro sanitario está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "dado que el registro está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

