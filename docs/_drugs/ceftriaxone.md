---
layout: default
title: Ceftriaxone
parent: Solo Predicción del Modelo (L5)
nav_order: 144
evidence_level: L5
indication_count: 7
monitor_inn: "Ceftriaxone"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "infectious otitis media", "blood group incompatibility", "suppurative otitis media", "chronic otitis media"]
last_modified_at: 2026-10-28
description: "Ceftriaxone: nueva indicación predicha, hiperamilasemia (hyperamylasemia) (nivel de evidencia L5). Indicación original: CEFTRIAXONA"
---

# Ceftriaxone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

## Ceftriaxona: antibiótico betalactámico (cefalosporina) → hiperamilasemia (hyperamylasemia)
{: .text-alpha }

## Resumen en Una Frase

Ceftriaxona es un antibiótico inyectable que cuenta con registro sanitario local.
El modelo TxGNN predice que podría ser útil para **hiperamilasemia (hyperamylasemia)**, pero **no hay ensayos clínicos** y solo hay **3 publicaciones** de baja relevancia directa (un reporte de caso, un estudio de cohorte sobre enzimas pancreáticas en hemorragia intracraneal y un estudio de profilaxis tras papilo-esfinterotomía endoscópica), por lo que la evidencia es muy débil.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | CEFTRIAXONA |
| Nueva Indicación Predicha | hiperamilasemia (hyperamylasemia) |
| Puntaje de Predicción TxGNN | 0,9939 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 1) |
| Número de Registros Sanitarios | al menos 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este informe. Por conocimiento general, la ceftriaxona es una cefalosporina que inhibe la síntesis de la pared celular bacteriana, por lo que actúa contra infecciones bacterianas.

La hiperamilasemia es un hallazgo de laboratorio (elevación de la amilasa en sangre) y no una infección, por lo que no existe un vínculo mecanístico directo con un antibiótico. El único nexo indirecto es que la ceftriaxona se usa de forma profiláctica tras procedimientos endoscópicos biliares (papilo-esfinterotomía), que pueden causar una hiperamilasemia transitoria. El puntaje alto del modelo probablemente es un artefacto de la red de relaciones y no refleja una razón terapéutica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10458061](https://pubmed.ncbi.nlm.nih.gov/10458061/) | 1999 | Estudio clínico | Bratislavske lekarske listy | Ceftriaxona 1 g profiláctica en 30 pacientes tras papilo-esfinterotomía endoscópica, comparada con 30 sin antibiótico; las bacterias biliares fueron sensibles a ceftriaxona |
| [7522351](https://pubmed.ncbi.nlm.nih.gov/7522351/) | 1994 | Cohorte | Southern Medical Journal | En 38 pacientes con hemorragia intracraneal se observó elevación de lipasa y amilasa sin pancreatitis; no evalúa ceftriaxona |
| [36263834](https://pubmed.ncbi.nlm.nih.gov/36263834/) | 2023 | Reporte de caso | Revista Española de Enfermedades Digestivas | Síndrome de Weil con hemorragia digestiva alta; no demuestra eficacia de ceftriaxona en hiperamilasemia |

Ninguna de estas publicaciones estudia directamente la ceftriaxona como tratamiento de la hiperamilasemia.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20163214 | CEFTRINOX® 1000 MG | Polvo estéril para reconstituir a solución inyectable | No registrada en los datos locales |

La lista de registros puede ser parcial.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (100 interacciones identificadas; se muestran las principales):
  - **Mayores:** cloruro de calcio, glucoheptonato de calcio, gluconato de calcio.
  - **Moderadas:** kanamicina, neomicina, estreptomicina, ácido picosulfúrico.
  - Otras con nivel no clasificado: calcitriol, epinefrina, anfotericina B, manitol, ácido acetilsalicílico, amoxicilina, entre otras.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe mecanismo plausible ni estudios que evalúen directamente la ceftriaxona para la hiperamilasemia; la predicción descansa solo en el puntaje del modelo, y la hiperamilasemia es un hallazgo de laboratorio, no una enfermedad tratable con un antibiótico.

**Para avanzar se necesita:**
- Evidencia clínica o preclínica que estudie directamente la relación entre ceftriaxona y la hiperamilasemia
- Datos del mecanismo de acción y del prospecto (advertencias y contraindicaciones)
- Aclarar si la hiperamilasemia es un objetivo terapéutico razonable o solo un efecto asociado a procedimientos
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

