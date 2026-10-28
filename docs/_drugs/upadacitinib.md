---
layout: default
title: Upadacitinib
parent: Solo Predicción del Modelo (L5)
nav_order: 650
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Upadacitinib: nueva indicación predicha, Síndrome de microftalmía colobomatosa con displasia rizomélica (nivel de evidencia L5). Indicación original: No especificada en el registro (el texto aprobado…"
monitor_inn: "upadacitinib"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome"]
---

# Upadacitinib
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

## Upadacitinib: De Indicación Original No Especificada a Síndrome de Microftalmía Colobomatosa con Displasia Rizomélica
{: .text-alpha }

## Resumen en Una Frase

Upadacitinib (marca RINVOQ®) es un inhibidor de JAK1 de administración oral; en los registros sanitarios de Colombia la indicación aprobada figura solo con el nombre del principio activo, sin detalle de la enfermedad.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de microftalmía colobomatosa con displasia rizomélica**, con **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.
La predicción se basa únicamente en el puntaje del modelo, sin estudios reales.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto aprobado solo indica "UPADACITINIB") |
| Nueva Indicación Predicha | Síndrome de microftalmía colobomatosa con displasia rizomélica |
| Puntaje de Predicción TxGNN | 0.9961 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 2 de 2) |
| Número de Registros Sanitarios | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, upadacitinib es un inhibidor de JAK1, que bloquea la señalización inflamatoria JAK-STAT.

La nueva indicación predicha es un síndrome congénito raro que afecta el desarrollo ocular y esquelético. Estos trastornos suelen tener origen genético y no depender de la señalización inflamatoria mediada por JAK-STAT, que es el blanco de upadacitinib. No se puede establecer un vínculo mecanístico plausible a partir de los datos disponibles.

El puntaje alto (0.9961) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. Esta predicción debe considerarse con mucha cautela.

**Otra predicción del modelo:** el síndrome de braquidactilia-sindactilia (puntaje 0.9958, nivel L5, Hold). También es una malformación congénita de las extremidades, ligada a vías de desarrollo (por ejemplo HOX o BMP/GDF5) y no a la señalización inflamatoria JAK-STAT. Tampoco cuenta con ensayos clínicos ni literatura.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20178268 | RINVOQ® | Tableta de liberación prolongada | UPADACITINIB | Vigente |
| 20224531 | RINVOQ® 45 MG | Tableta de liberación prolongada | UPADACITINIB | Vigente |

Ambos registros pertenecen a ABBVIE S.A.S. y actualmente no hay registros vigentes.

---

## Consideraciones de Seguridad

**Interacciones Farmacológicas:** se identificaron 359 interacciones. Entre las principales:

- **Gravedad mayor:** hidrocortisona, triamcinolona, dexametasona, beclometasona, betametasona, budesonida, prednisona, prednisolona, claritromicina, cobicistat, deferiprona, iobenguano (I-131).
- **Gravedad moderada:** aprepitant, cimetidina, miconazol, deferasirox.
- **Gravedad menor:** sulfato, acetato y gluconato de zinc.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La única base es un puntaje alto del modelo, sin ensayos clínicos ni literatura, y sin un vínculo mecanístico plausible entre la inhibición de JAK1 y un síndrome congénito del desarrollo. Además, el producto no tiene registros vigentes en Colombia.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (consultar la API de DrugBank)
- Advertencias y contraindicaciones del prospecto de INVIMA
- Evidencia biológica o preclínica que vincule la vía JAK-STAT con la fisiopatología de este síndrome
- Aclarar la indicación original aprobada y la situación regulatoria (registros cancelados)
- Evaluación de compatibilidad de vía de administración y similitud con la indicación original (pendientes)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

