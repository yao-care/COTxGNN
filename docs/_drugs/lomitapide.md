---
layout: default
title: Lomitapide
parent: Solo Predicción del Modelo (L5)
nav_order: 407
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Lomitapide: nueva indicación predicha, Macrotrombocitopenia con insuficiencia de la válvula mitral (nivel de evidencia L5). Indicación original: El registro sanitario solo indica el nombre del princi…"
monitor_inn: "lomitapide"
predicted_indications: ["marcothrombocytopenia with mitral valve insufficiency", "hereditary thrombocytopenia with normal platelets", "dense granule disease", "transient neonatal thrombocytopenia", "thrombocytopenia", "primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "hyperlipoproteinemia", "platelet storage pool deficiency"]
---

# Lomitapide
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

# Lomitapida: De Hipercolesterolemia Familiar Homocigota a Macrotrombocitopenia con Insuficiencia de la Válvula Mitral

## Resumen en Una Frase

Lomitapida es un inhibidor de la proteína microsomal de transferencia de triglicéridos (MTP), utilizado para tratar la hipercolesterolemia familiar homocigota.
El modelo TxGNN predice que podría ser efectiva para **macrotrombocitopenia con insuficiencia de la válvula mitral**, con un puntaje muy alto (99.92%).
Sin embargo, **no hay ensayos clínicos ni publicaciones** que respalden esta predicción, que se basa únicamente en el modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | El registro sanitario solo indica el nombre del principio activo («Lomitapida»). El uso conocido del fármaco es la hipercolesterolemia familiar homocigota. |
| Nueva Indicación Predicha | Macrotrombocitopenia con insuficiencia de la válvula mitral |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 8 (0 vigentes, 8 cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Lomitapida inhibe la MTP, una proteína que ensambla y secreta las lipoproteínas con apoB (VLDL en el hígado y quilomicrones en el intestino). Con ello reduce el colesterol LDL. Este es el mecanismo de su uso en la hipercolesterolemia familiar homocigota.

**Los datos compilados no permiten identificar un vínculo mecanístico plausible** entre la inhibición de la MTP y la producción de plaquetas o la patología de la válvula mitral. El puntaje tan alto probablemente refleja la cercanía entre trastornos plaquetarios en el grafo de conocimiento del modelo, más que una relación biológica real.

La relación entre la indicación original (metabolismo de lipoproteínas) y la nueva (trastorno plaquetario con compromiso valvular) es débil. Por ahora esta predicción debe considerarse una hipótesis sin respaldo.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta indicación.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

---

## Información de Mercado en Colombia

Los 8 registros sanitarios de lomitapida en Colombia están **cancelados**. No hay ninguno vigente. Se listan los 5 principales:

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20250301 | TROMBACTAN® 10 MG CAPSULAS DURAS | Cápsula dura | Lomitapida (sin detalle de indicación) |
| 20245910 | TROMBACTAN® 5 MG CAPSULAS | Cápsula dura | Lomitapida (sin detalle de indicación) |
| 20246008 | TROMBACTAN® 20 MG CAPSULAS | Cápsula dura | Lomitapida (sin detalle de indicación) |
| 20097720 | JUXTAPID® CÁPSULAS POR 5 MG | Cápsula dura | Lomitapida (sin detalle de indicación) |
| 20071948 | JUXTAPID® CÁPSULAS POR 20 MG | Cápsula dura | Lomitapida (sin detalle de indicación) |

Los otros tres registros, también cancelados, corresponden a OLESTAPIDE® de Laboratorios Elmor (5, 10 y 20 mg).

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 206 interacciones, una carga muy alta. Entre las 20 revisadas, las de nivel **mayor** incluyen:
  - Acarbosa
  - Doxiciclina, minociclina y tetraciclina
  - Pioglitazona
  - Bupropión
  - Aprepitant
  - Ácido quenodesoxicólico
  - Claritromicina
  - Naltrexona
  - Oxandrolona y oximetolona

  También hay interacciones de nivel moderado, por ejemplo con ranitidina, cimetidina, loperamida, budesonida, saxagliptina, linagliptina y eliglustat.
- **Perfil de seguridad general del fármaco** (según el análisis de las predicciones): preocupaciones por hepatotoxicidad (elevación de transaminasas, esteatosis hepática), efectos gastrointestinales y teratogenicidad.

Consultar el prospecto para las advertencias y contraindicaciones oficiales, que no están disponibles en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para macrotrombocitopenia con insuficiencia mitral es solo del modelo (L5), sin ensayos ni literatura y sin mecanismo plausible. Además, todos los registros colombianos están cancelados y el perfil de seguridad es exigente.

**Observación sobre otras predicciones:**
Entre las 10 indicaciones predichas, solo la hiperlipoproteinemia (puesto 9, puntaje 99.74%) tiene evidencia sólida: nivel L1, con 7 ensayos clínicos (incluidos varios de Fase 3 completados en hipercolesterolemia familiar homocigota, también en población pediátrica) y 20 publicaciones. Esto corresponde en la práctica a la indicación original, no a un reposicionamiento real. Las demás indicaciones predichas son trastornos plaquetarios (trombocitopenia, enfermedad de Glanzmann, déficit de gránulos densos, entre otros), todas L5 y con recomendación Hold.

**Para avanzar se necesita:**
- Un fundamento biológico que vincule la inhibición de la MTP con la producción o función plaquetaria, o con la patología valvular mitral.
- Estudios preclínicos o series de casos que sustenten la hipótesis.
- Las advertencias y contraindicaciones del prospecto del INVIMA.
- Verificar el estado regulatorio actual en Colombia, dado que todos los registros están cancelados.
- Si el interés real es la hiperlipoproteinemia, evaluarla como indicación separada, con medidas de control (monitoreo hepático, dieta baja en grasa, precauciones de teratogenicidad y manejo de interacciones con inhibidores de CYP3A4).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

