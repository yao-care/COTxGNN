---
layout: default
title: Mirtazapine
parent: Solo Predicción del Modelo (L5)
nav_order: 449
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Mirtazapine: nueva indicación predicha, Síndrome de Ohdo y variantes (nivel de evidencia L5). Indicación original: Mirtazapina"
monitor_inn: "Mirtazapine"
predicted_indications: ["Ohdo syndrome and variants", "blepharophimosis - intellectual disability syndrome, Ohdo type", "benign paroxysmal torticollis of infancy"]
---

# Mirtazapine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Mirtazapina: De Mirtazapina (indicación registrada) a Síndrome de Ohdo y variantes
{: .text-alpha }

## Resumen en Una Frase

Mirtazapina es un antidepresivo cuyos registros sanitarios en Colombia figuran bajo el nombre del principio activo, sin un texto de indicación detallado; en la literatura farmacológica se usa para el trastorno depresivo mayor.
El modelo TxGNN predice que podría ser efectivo para el **Síndrome de Ohdo y variantes**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.
Se trata de una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Mirtazapina (el texto de indicación registrado en INVIMA solo menciona el nombre del principio activo) |
| Nueva Indicación Predicha | Síndrome de Ohdo y variantes |
| Puntaje de Predicción TxGNN | 0.9942 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 4) |
| Número de Registros Sanitarios | 4 (0 vigentes, 4 cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según el conocimiento farmacológico general y los datos de afinidad por receptores, la mirtazapina es un antidepresivo noradrenérgico y serotoninérgico específico: tiene mayor afinidad por los adrenoceptores α2 (α2A, α2B, α2C) y por los receptores serotoninérgicos 5-HT2A y 5-HT2C, donde actúa como antagonista.

El síndrome de Ohdo y sus variantes son trastornos raros del neurodesarrollo, asociados comúnmente con mutaciones en KAT6B y desregulación de la cromatina o de mecanismos epigenéticos. **No se identifica una vía plausible** que conecte el perfil receptorial de la mirtazapina con la etiología genética de la enfermedad. El puntaje alto de TxGNN (0.9942) proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica ni clínica independiente.

Cualquier uso sintomático (por ejemplo, para el sueño, el apetito o el estado de ánimo) sería especulativo y no está respaldado por los datos disponibles.

**Otras predicciones del modelo (todas con nivel L5 y recomendación Hold):**

| Posición | Enfermedad | Puntaje TxGNN | Comentario |
|------|------|------|------|
| 2 | Síndrome de blefarofimosis con discapacidad intelectual, tipo Ohdo | 0.9911 | Se solapa con la predicción principal (espectro KAT6B); el puntaje proviene del modelo TxGNN (deep learning) y puede reflejar similitudes aprendidas entre enfermedades relacionadas, no evidencia biológica |
| 3 | Tortícolis paroxística benigna de la infancia | 0.9911 | Una conexión especulativa sería la modulación serotoninérgica (antagonismo 5-HT2 usado en profilaxis de migraña), pero no hay estudios y la condición se resuelve sola; faltan datos de seguridad en lactantes y los antidepresivos llevan advertencias pediátricas |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20165068 | AUROZAPINE OD 30 MG TABLETAS ORODISPERSABLES | Tableta orodispersable | MIRTAZAPINA | Vigente |
| 19928993 | MIRTAPAX ® | Tableta recubierta | MIRTAZAPINA | Vigente |
| 20165061 | AUROZAPINE OD 15 MG TABLETAS ORODISPERSABLES | Tableta orodispersable | MIRTAZAPINA | Vigente |
| 20090945 | EPILFARMO 30 MG | Tableta recubierta | MIRTAZAPINA | Vigente |

Los cuatro registros son de monofármaco y están cancelados; actualmente no hay productos vigentes en Colombia.

---

## Consideraciones de Seguridad

- **Contraindicaciones y condiciones de riesgo según el grafo de conocimiento (no provienen del prospecto):** el grafo de conocimiento asocia la mirtazapina con las siguientes condiciones:
  - Neurológicas y psiquiátricas: epilepsia, trastorno bipolar maníaco, síndrome serotoninérgico, acatisia inducida por fármacos, atrofia multisistémica.
  - Cardiovasculares: hipotensión ortostática, trastornos hipotensivos, síndrome de taquicardia postural ortostática, accidente cerebrovascular y trastornos cerebrovasculares, infarto cerebral, infarto de miocardio, trombosis coronaria.
  - Hematológicas: neutropenia, agranulocitosis, hemoglobinopatías.
  - Hepáticas, biliares y renales: enfermedad hepática, enfermedad de la vesícula biliar, función renal alterada.
  - Metabólicas: hipertrigliceridemia, obesidad (incluida la monogénica).
- **Perfil farmacológico (receptores diana):** receptores 5-HT2A, 5-HT2C, y adrenoceptores α2A, α2B y α2C. Esta información describe el perfil de unión a receptores y no constituye una lista de interacciones fármaco-fármaco clínicas.
- **Población pediátrica:** los antidepresivos llevan advertencias pediátricas y no hay datos de seguridad en lactantes, relevante para la tercera predicción.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es puramente computacional (nivel L5), sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico plausible entre el perfil receptorial de la mirtazapina y la causa genética del síndrome de Ohdo. Además, no hay registros sanitarios vigentes en Colombia.

**Para avanzar se necesita:**
- Datos oficiales del mecanismo de acción (consulta a DrugBank)
- Advertencias y contraindicaciones del prospecto de INVIMA
- Evidencia preclínica o mecanística que conecte la acción de la mirtazapina con la vía KAT6B/epigenética
- Revisión de literatura dirigida sobre síndrome de Ohdo y antidepresivos
- Clarificar la situación regulatoria (registros cancelados) si se considerara avanzar
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

