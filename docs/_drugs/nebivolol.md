---
layout: default
title: Nebivolol
parent: Solo Predicción del Modelo (L5)
nav_order: 464
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Nebivolol: nueva indicación predicha, Enfermedad renal hipertensiva maligna (nivel de evidencia L5). Indicación original: NEBIVOLOL"
monitor_inn: "nebivolol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
---

# Nebivolol
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

## Nebivolol: De Nebivolol (indicación sin detallar) a Enfermedad Renal Hipertensiva Maligna
{: .text-alpha }

## Resumen en Una Frase

Nebivolol es un betabloqueante selectivo beta-1 con efecto vasodilatador mediado por óxido nítrico, registrado en Colombia como tableta oral (NABILA® 10 mg), aunque el registro sanitario consta como cancelado y no detalla la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **enfermedad renal hipertensiva maligna**, pero sin **ningún ensayo clínico** ni **publicaciones** directamente relacionadas con esta indicación.
La predicción se apoya únicamente en el modelo computacional (nivel de evidencia L5).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | NEBIVOLOL (el registro sanitario no detalla la indicación aprobada) |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna |
| Puntaje de Predicción TxGNN | 99.42% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, nebivolol es un betabloqueante selectivo beta-1 que además activa la óxido nítrico sintasa endotelial (eNOS), lo que produce vasodilatación. Esto da un fundamento plausible para un efecto hipotensor y, de forma teórica, renoprotector.

La relación con la indicación original es indirecta: el registro local solo menciona el nombre del principio activo, sin texto de indicación. Por su clase farmacológica, el uso esperado es en enfermedades cardiovasculares como la hipertensión, por lo que una enfermedad hipertensiva con compromiso renal es cercana en lo conceptual.

Sin embargo, la hipertensión maligna con afectación renal es una emergencia que normalmente se maneja con fármacos intravenosos, por lo que nebivolol oral no tiene un papel establecido. El puntaje alto del modelo (99.42%) no cuenta con validación clínica.

Otras predicciones del modelo (con el mismo nivel de evidencia bajo) fueron: hipertensión renovascular maligna (99.42%), hipertensión pulmonar por enfermedad pulmonar o hipoxia (99.39%, nivel L4 por literatura preclínica indirecta), hipertensión pulmonar de mecanismo multifactorial poco claro (99.39%) y síndrome de Braddock (99.14%, sin vínculo mecanístico identificable).

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20009035 | NABILA® 10 MG COMPRIMIDOS | Tableta | NEBIVOLOL | Cancelado |

El fabricante es MONTE VERDE S.A. No hay registros vigentes en el país.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** insuficiencia hepática, enfermedad hepática, enfermedad de la vesícula biliar, diabetes mellitus, cetoacidosis diabética, enfermedad vascular periférica, claudicación intermitente, enfermedad arterial periférica, hipoglucemia, bloqueo auriculoventricular, enfermedad bronquial, síndrome del seno enfermo (incluida su forma familiar).
- **Interacciones farmacológicas:** se identificaron 174 interacciones. Entre las listadas, la mayoría son de nivel moderado: epinefrina, hidrocortisona, hiosciamina, bupropión, triamcinolona, morfina, atropina, dexametasona, lorcaserina, betametasona, fosfato de calcio, budesonida, glicopirronio, acetato de calcio, canagliflozina, clorpropamida, dapagliflozina y diciclomina. Son de nivel menor el ácido acetilsalicílico y el óxido de magnesio.
- Los betabloqueantes requieren cautela en enfermedad pulmonar o hipoxia y en hipertensión pulmonar arterial, por el posible deterioro de la función del ventrículo derecho.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción solo se sustenta en el modelo TxGNN, sin ensayos clínicos ni literatura directa. Además, la hipertensión maligna con compromiso renal se trata con agentes intravenosos, y el único registro sanitario local está cancelado.

**Para avanzar se necesita:**
- Datos del mecanismo de acción confirmados (por ejemplo, desde DrugBank).
- Prospecto del INVIMA con advertencias y contraindicaciones, que hoy no están disponibles y bloquean el análisis de seguridad.
- Estudios clínicos o literatura específicos de nebivolol en enfermedad renal hipertensiva maligna.
- Evaluación de compatibilidad de vía de administración (oral frente a la vía intravenosa que requiere la emergencia hipertensiva).
- Aclarar la situación regulatoria en Colombia, dado que no hay registros vigentes.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

