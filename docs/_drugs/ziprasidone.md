---
layout: default
title: Ziprasidone
parent: Solo Predicción del Modelo (L5)
nav_order: 669
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ziprasidone: nueva indicación predicha, Tricotilomanía (nivel de evidencia L5). Indicación original: No especificada en el registro (el texto solo dice \"ZIPRASIDONA\")"
monitor_inn: "ziprasidone"
predicted_indications: ["trichotillomania", "hydranencephaly (disease)", "major affective disorder", "congenital disorder of glycosylation with defective fucosylation", "myopia X-linked", "retinal dystrophy with or without extraocular anomalies", "Tourette syndrome", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "myopia 26, X-linked, female-limited", "syndromic myopia"]
---

# Ziprasidone
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

# Ziprasidona: De Antipsicótico (indicación no detallada en el registro) a Tricotilomanía

## Resumen en Una Frase

Ziprasidona es un antipsicótico atípico. En Colombia se registró como GEODON® cápsulas 80 mg, pero el texto del registro sanitario solo repite el nombre del fármaco y no detalla la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **tricotilomanía**, pero hasta ahora hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Se trata de una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto solo dice "ZIPRASIDONA") |
| Nueva Indicación Predicha | Tricotilomanía |
| Puntaje de Predicción TxGNN | 99.83% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registro cancelado |
| Número de Registros Sanitarios | 1 (0 vigentes, 1 cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción de ziprasidona. Por su farmacología conocida, es un antipsicótico atípico que antagoniza los receptores de serotonina 5-HT2A y de dopamina D2.

La tricotilomanía es un trastorno de conductas repetitivas y compulsivas de arrancarse el cabello. Se relaciona con circuitos dopaminérgicos y serotoninérgicos que regulan los hábitos y los impulsos. Por eso, un fármaco que modula ambos sistemas podría influir en estas conductas.

Esta relación es solo una hipótesis. No hay ensayos ni literatura que la confirmen, y la conexión con la indicación original no ha sido evaluada formalmente. Con la información actual, la predicción no es más que una señal del modelo.

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
| 19922147 | GEODON® CAPSULAS 80 MG (Aspen Colombiana S.A.S.) | Cápsula dura | ZIPRASIDONA (sin indicación detallada) |

Este registro tiene estado **cancelado**. Actualmente no hay registros vigentes de ziprasidona en los datos consultados.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** el grafo de conocimiento asocia ziprasidona con contraindicaciones en varios grupos de enfermedades:
  - **Cardiovasculares:** síndrome de QT largo (incluido el familiar), torsades de pointes, infarto de miocardio, paro cardíaco súbito, enfermedades de la conducción cardíaca, hipotensión ortostática y síndrome de taquicardia postural ortostática.
  - **Metabólicas:** diabetes mellitus, cetoacidosis diabética, hiperglucemia, hiperlipidemia, obesidad y deficiencia de potasio.
  - **Hematológicas:** neutropenia y agranulocitosis.
  - **Neurológicas:** epilepsia, enfermedades de los ganglios basales, distonía focal de la mano, blefaroespasmo y atrofia multisistémica.
  - **Otras:** insuficiencia hepática, enfermedad renal y carcinoma de mama femenino.
- **Interacciones farmacológicas:** se identificaron 305 interacciones. Entre las de nivel **mayor** figuran hidrocortisona, anfotericina B (y su complejo lipídico), bupropión y morfina. Hay además numerosas interacciones moderadas, entre ellas antidiabéticos (metformina, pioglitazona, acarbosa, alogliptina, albiglutida), anticolinérgicos (atropina, hiosciamina, glicopirronio) y epinefrina.
- **Cardiaca en pediatría:** la revisión sistemática de seguridad cardíaca de antipsicóticos en población pediátrica (PMID 39549076) destaca la preocupación por la prolongación del QT. Esto es relevante, porque la tricotilomanía suele iniciar en la infancia o la adolescencia.

Consultar el prospecto para la información de seguridad detallada.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto (99.83%), pero no hay ensayos clínicos ni literatura que la respalden (nivel L5). Además, el único registro sanitario en Colombia está cancelado y existen alertas de seguridad cardiometabólica relevantes.

**Para avanzar se necesita:**
- Revisión sistemática de la literatura sobre antipsicóticos atípicos en tricotilomanía y trastornos de conductas repetitivas, y su comparación con las opciones terapéuticas establecidas.
- Datos detallados del mecanismo de acción y del prospecto (advertencias y contraindicaciones oficiales).
- Evaluación del riesgo cardíaco (QT) y metabólico para la población objetivo, que incluye niños y adolescentes.
- Aclarar la situación regulatoria en Colombia, ya que el único registro está cancelado.

**Nota:** dentro de las predicciones de ziprasidona hay candidatos con respaldo clínico bastante mayor que la tricotilomanía. Son el **trastorno afectivo mayor** (nivel L2, con varios ensayos de Fase 2, incluido uno controlado con placebo en 120 pacientes con depresión mayor) y el **síndrome de Tourette** (nivel L3, con un estudio piloto pediátrico y revisiones). Si el objetivo es priorizar recursos, conviene evaluarlos antes que la tricotilomanía.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

