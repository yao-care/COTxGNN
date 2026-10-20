---
layout: default
title: Ascorbic Acid
parent: Solo Predicción del Modelo (L5)
nav_order: 68
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ascorbic Acid: nueva indicación predicha, Malformación esofágica no sindrómica (nivel de evidencia L5). Indicación original: Ácido ascórbico (vitamina C)"
monitor_inn: "Ascorbic acid"
predicted_indications: ["non-syndromic esophageal malformation", "esophageal disease", "congenital prothrombin deficiency", "injury", "biotin metabolic disease", "florid cemento-osseous dysplasia", "segmental odontomaxillary dysplasia", "perinatal disease", "disease by subcellular system affected", "vitamin deficiency disorder"]
---

# Ascorbic Acid
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

# Ácido ascórbico: De Ácido ascórbico (vitamina C) a Malformación esofágica no sindrómica

## Resumen en Una Frase

El ácido ascórbico (vitamina C) se utilizaba originalmente como suplemento vitamínico, con registros sanitarios en Colombia para tabletas masticables.
El modelo TxGNN predice que podría ser efectivo para **malformación esofágica no sindrómica**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. La predicción se basa únicamente en el modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Ácido ascórbico (vitamina C) |
| Nueva Indicación Predicha | Malformación esofágica no sindrómica |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, el ácido ascórbico es un antioxidante hidrosoluble y cofactor de la síntesis de colágeno. Su eficacia está comprobada en la prevención y el tratamiento de la deficiencia de vitamina C, pero no en malformaciones congénitas.

El análisis de los datos compilados no identificó un fundamento mecanístico para esta predicción. Una malformación estructural congénita del esófago no se corrige plausiblemente con una vitamina antioxidante. El puntaje alto del modelo (99.96%) refleja una asociación calculada a partir de un grafo de conocimiento, no una evidencia clínica ni experimental.

Por ello, esta predicción debe considerarse una señal computacional sin respaldo, y no una hipótesis terapéutica lista para evaluarse.

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
| 20265640 | VITAMINA C 500 MG (PROCAPS S.A.) | Tableta masticable | Ácido ascórbico (vitamina C) — registro cancelado |
| 20024687 | DEVIT-C® (LABQUIFAR LTDA.) | Tableta masticable | Ácido ascórbico (vitamina C) — registro cancelado |

Ninguno de los dos registros está vigente actualmente.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** el grafo de conocimiento asocia el fármaco con contraindicaciones en enfermedad renal, anuria, nefrocalcinosis, hiperoxaluria primaria, hemocromatosis hereditaria, anemia falciforme, diabetes mellitus, cetoacidosis diabética, enfermedad hepática, úlcera péptica, hipertensión, epilepsia, lupus eritematoso sistémico, artritis reumatoide, esclerosis múltiple, sarcoidosis, hipercalcemia, hiperparatiroidismo, trastornos de la coagulación y otras condiciones. Deben verificarse contra la información oficial del producto.
- **Interacciones farmacológicas:** se identificaron 25 interacciones en total; las 20 siguientes son las consultadas.
  - **Moderadas:** anfetamina, dextroanfetamina, lisdexanfetamina, metanfetamina, benzfetamina, hidróxido de aluminio, bortezomib y deferoxamina.
  - **Leves:** paclitaxel, cisplatino, doxorrubicina (incluida la liposomal), pseudoefedrina, efedrina (incluida la nasal), etinilestradiol, flecainida, flufenazina, indinavir y mexiletina.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para malformación esofágica no sindrómica no tiene ensayos clínicos ni literatura, y no existe un mecanismo plausible que la sustente. Además, el fármaco no cuenta actualmente con registros sanitarios vigentes en Colombia.

**Para avanzar se necesita:**
- Una hipótesis mecanística creíble y estudios preclínicos que la respalden, sin los cuales no se justifica avanzar.
- Los datos de mecanismo de acción y las advertencias y contraindicaciones del prospecto, que no están disponibles.
- Un registro sanitario vigente, o un nuevo trámite ante INVIMA, si se quisiera una vía de uso en Colombia.
- Priorizar otras indicaciones predichas para este mismo fármaco, que tienen mayor respaldo que la malformación esofágica:
  - **Trastorno por deficiencia de vitaminas:** nivel L3, con recomendación "Proceed with Guardrails".
  - **Lesión (injury):** nivel L2, con 15 ensayos clínicos, incluidos varios de Fase 2 completados. Se señala riesgo de nefropatía por oxalato con dosis altas por vía intravenosa.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

