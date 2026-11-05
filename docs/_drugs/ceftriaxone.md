---
layout: default
title: Ceftriaxone
parent: Solo Predicción del Modelo (L5)
nav_order: 144
evidence_level: L5
indication_count: 5
monitor_inn: "Ceftriaxone"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "chronic otitis media"]
last_modified_at: 2026-11-06
description: "Ceftriaxone: nueva indicación predicha, hiperamilasemia (hyperamylasemia) (nivel de evidencia L5). Indicación original: CEFTRIAXONA"
---

# Ceftriaxone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Ceftriaxone: hiperamilasemia (hyperamylasemia)
{: .text-alpha }

## Resumen en Una Frase

Ceftriaxona es un antibiótico betalactámico que inhibe la síntesis de la pared celular bacteriana.
El modelo TxGNN predice que podría ser útil para **hiperamilasemia (hyperamylasemia)**, pero no hay ensayos clínicos y solo se dispone de **3 publicaciones** con relación indirecta, por lo que la predicción se apoya sobre todo en el puntaje del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | CEFTRIAXONA |
| Nueva Indicación Predicha | hiperamilasemia (hyperamylasemia) |
| Puntaje de Predicción TxGNN | 0.9939 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 7 de 9) |
| Número de Registros Sanitarios | 9 (vigentes: 7) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Por su clase, la ceftriaxona actúa sobre la pared celular de las bacterias y se usa contra infecciones bacterianas.

La hiperamilasemia es un hallazgo de laboratorio (elevación de la amilasa en sangre) y no una enfermedad infecciosa que un antibiótico trate directamente. No se identifica un mecanismo directo plausible entre la ceftriaxona y esta condición.

El único vínculo es indirecto: la ceftriaxona se ha usado de forma profiláctica tras procedimientos endoscópicos de la vía biliar (papilosfinterotomía), que pueden causar elevaciones transitorias de amilasa. El puntaje alto probablemente es un artefacto de la red del modelo y no refleja un beneficio terapéutico demostrado.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10458061](https://pubmed.ncbi.nlm.nih.gov/10458061/) | 1999 | Estudio clínico | Bratislavske lekarske listy | 30 pacientes tras papilosfinterotomía endoscópica recibieron 1 g de ceftriaxona preventiva frente a 30 sin antibiótico; las bacterias biliares (Pseudomonas aeruginosa, E. coli) fueron sensibles a ceftriaxona. |
| [7522351](https://pubmed.ncbi.nlm.nih.gov/7522351/) | 1994 | Cohorte | Southern Medical Journal | En 38 pacientes con hemorragia intracraneal, muchos presentaron lipasa y amilasa elevadas sin pancreatitis; no evalúa ceftriaxona. |
| [36263834](https://pubmed.ncbi.nlm.nih.gov/36263834/) | 2023 | Reporte de caso | Revista Española de Enfermedades Digestivas | Síndrome de Weil con hemorragia digestiva alta; no demuestra eficacia de ceftriaxona en hiperamilasemia. |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20163214 | CEFTRINOX® 1000 MG | Polvo estéril para reconstituir a solución inyectable | No registrada en los datos locales |

La información de registros puede ser parcial.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (100 interacciones registradas; principales):
  - Gravedad mayor: cloruro de calcio, gluheptonato de calcio y gluconato de calcio.
  - Gravedad moderada: kanamicina, neomicina, estreptomicina y ácido picosulfúrico.
  - Otras con gravedad no clasificada: calcitriol, epinefrina, anfotericina B, manitol, ácido acetilsalicílico, amoxicilina, entre otras.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos ni estudios que evalúen directamente la ceftriaxona en hiperamilasemia, y no hay un mecanismo plausible; la predicción se sostiene solo en el puntaje del modelo (nivel L5).

**Para avanzar se necesita:**
- Datos del mecanismo de acción y de advertencias y contraindicaciones del prospecto.
- Estudios que evalúen directamente la hiperamilasemia como objetivo terapéutico, si se desea reconsiderar la hipótesis.
- Revisión de la seguridad de la ceftriaxona en pacientes con enfermedad hepática o biliar y de las interacciones con soluciones que contienen calcio.

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

