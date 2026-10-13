---
layout: default
title: Sertraline
parent: Evidencia Moderada (L3-L4)
nav_order: 585
evidence_level: L4
indication_count: 8
---

# Sertraline
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **8** 
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

# Sertralina: De Sertralina (indicación según registro INVIMA) a Trastorno Esquizotípico de la Personalidad

## Resumen en Una Frase

Sertralina es un inhibidor selectivo de la recaptación de serotonina (ISRS), registrado en Colombia bajo el texto de indicación "SERTRALINA". El modelo TxGNN predice que podría ser efectivo para el **trastorno esquizotípico de la personalidad**, pero solo existe **1 ensayo clínico** (8 participantes, sin fase definida) y **1 publicación** no relacionada que respaldan esta dirección, por lo que la evidencia es muy débil.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | SERTRALINA (el registro no detalla la indicación) |
| Nueva Indicación Predicha | Trastorno esquizotípico de la personalidad |
| Puntaje de Predicción TxGNN | 99.93% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 (0 vigentes, 1 cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la sertralina es un ISRS que bloquea el transportador de serotonina (SERT, gen SLC6A4). Se usa en depresión mayor, trastorno de estrés postraumático, trastorno obsesivo-compulsivo, trastorno de pánico, trastorno disfórico premenstrual y fobia social.

La relación con el trastorno esquizotípico es indirecta. La modulación serotoninérgica podría influir en síntomas positivos y negativos atenuados, y en rasgos afectivos u obsesivos asociados. Sin embargo, el único ensayo disponible fue muy pequeño y la publicación recuperada trata sobre otra condición (TOC y anorexia nerviosa). El puntaje alto del modelo no está respaldado por datos clínicos.

Cabe señalar que, entre las indicaciones predichas, la **agorafobia** (puntaje 99.54%) tiene una evidencia mucho más sólida (nivel L1, con ensayos aleatorizados y metaanálisis en trastorno de pánico con o sin agorafobia). Se trata más de una confirmación de un uso ya establecido que de un reposicionamiento novedoso.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00169988](https://clinicaltrials.gov/study/NCT00169988) | No definida | Completado | 8 | Sertralina sola frente a sertralina más risperidona en síntomas positivos y negativos atenuados en adolescentes (población de pródromo del espectro esquizofrénico). Muestra muy pequeña; no permite concluir eficacia. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37082034](https://pubmed.ncbi.nlm.nih.gov/37082034/) | 2021 | Reporte de caso | Postepy Psychiatrii Neurologii | Comorbilidad de TOC y anorexia nerviosa en una niña de 14 años; no es relevante para el trastorno esquizotípico. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20224090 (cancelado) | IRRADIAX® 50MG | Tableta recubierta | SERTRALINA |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: epilepsia, trastorno bipolar, trastorno afectivo mayor, enfermedad hepática, enfermedad de la vesícula biliar, trastornos de la coagulación sanguínea, síndrome neuroléptico maligno, síndrome de secreción inapropiada de ADH, síndrome nefrogénico de antidiuresis inapropiada y síndrome serotoninérgico.
- **Interacciones farmacológicas**: solo se registró la interacción farmacológica con el transportador SERT (su objetivo terapéutico); no hay datos de interacciones con otros fármacos. Con ISRS se debe evitar la combinación con otros agentes serotoninérgicos por el riesgo de síndrome serotoninérgico.

Consultar el prospecto para el resto de la información de seguridad (advertencias y contraindicaciones oficiales).

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para el trastorno esquizotípico se apoya solo en el puntaje del modelo, con un único ensayo muy pequeño (n=8) y sin literatura relevante. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Ensayos controlados específicos en trastorno esquizotípico de la personalidad con tamaño de muestra adecuado.
- Datos detallados del mecanismo de acción (consulta a DrugBank).
- Descarga y análisis del prospecto de INVIMA para advertencias y contraindicaciones.
- Aclarar la situación regulatoria local (registro cancelado) y valorar si otros registros de sertralina vigentes permitirían el acceso.
- Considerar priorizar la agorafobia/trastorno de pánico, que tiene evidencia nivel L1 y podría avanzar como "Proceed with Guardrails" tras confirmar el uso en el contexto local.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

