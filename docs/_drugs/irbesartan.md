---
layout: default
title: Irbesartan
parent: Solo Predicción del Modelo (L5)
nav_order: 355
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Irbesartan: nueva indicación predicha, Enfermedad renal hipertensiva maligna (nivel de evidencia L5). Indicación original: IRBESARTAN"
monitor_inn: "IRBESARTAN"
predicted_indications: ["malignant hypertensive renal disease"]
---

# Irbesartan
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Irbesartán: De Irbesartán (indicación sin detallar) a Hipertensión Renal Maligna

## Resumen en Una Frase

Irbesartán es un antagonista del receptor de angiotensina II tipo 1 (AT1), registrado en Colombia bajo el nombre de su principio activo, sin que el registro detalle la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **enfermedad renal hipertensiva maligna**, con un puntaje muy alto, pero **sin ensayos clínicos ni publicaciones** que respalden específicamente esta indicación.
La predicción se apoya solo en el modelo computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | IRBESARTAN (el registro sanitario no detalla una indicación específica) |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna |
| Puntaje de Predicción TxGNN | 99.31% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, irbesartán es un antagonista selectivo del receptor AT1 de angiotensina II, con efectos antihipertensivos y renoprotectores establecidos.

El bloqueo del sistema renina-angiotensina es biológicamente plausible en el daño renal de origen hipertensivo, y esto explica la cercanía entre el uso original del fármaco y la nueva indicación, reflejada en el puntaje alto del modelo (0.993).

Sin embargo, la hipertensión maligna es una emergencia aguda que normalmente se maneja con fármacos parenterales de acción rápida, por lo que un ARA-II oral en monoterapia difícilmente sería el tratamiento principal. Esta predicción debe considerarse hipótesis computacional, no evidencia clínica.

**Otras indicaciones predichas (para contexto):**

| Indicación | Puntaje TxGNN | Nivel | Recomendación |
|---|---|---|---|
| Hipertensión renovascular maligna | 99.31% | L5 | Hold |
| Hipertensión pulmonar por enfermedad pulmonar y/o hipoxia | 99.25% | L4 | Pregunta de investigación |
| Hipertensión pulmonar de mecanismo multifactorial poco claro | 99.25% | L5 | Hold |

La hipertensión pulmonar asociada a hipoxia es la que cuenta con más literatura mecanística (ver más abajo), aunque exclusivamente preclínica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para la indicación principal (enfermedad renal hipertensiva maligna), ni para las demás indicaciones predichas.

---

## Evidencia de Literatura

Para la indicación principal no hay literatura disponible. La siguiente tabla corresponde a la literatura de la indicación de rango 3 (hipertensión pulmonar por enfermedad pulmonar/hipoxia), la única con publicaciones. Se omiten los trabajos ajenos al irbesartán (extractos herbales, reporte de caso de roxadustat).

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35288835](https://pubmed.ncbi.nlm.nih.gov/35288835/) | 2022 | Revisión | Inflammopharmacology | Efectos pleiotrópicos de los antagonistas AT1 en hipoxia por isquemia cardíaca |
| [30356256](https://pubmed.ncbi.nlm.nih.gov/30356256/) | 2018 | Preclínico (in vitro) | PLoS One | Irbesartán protege a cardiomiocitos bajo estrés hipóxico |
| [34626328](https://pubmed.ncbi.nlm.nih.gov/34626328/) | 2022 | Preclínico (animal) | Sleep & Breathing | Irbesartán atenúa la apoptosis cardíaca inducida por apnea del sueño |
| [17142340](https://pubmed.ncbi.nlm.nih.gov/17142340/) | 2007 | Preclínico (animal) | Am J Physiol Heart Circ Physiol | Irbesartán inhibe la angiogénesis coronaria estimulada por hipoxia intermitente en ratas neonatas |
| [34147903](https://pubmed.ncbi.nlm.nih.gov/34147903/) | 2021 | Preclínico (animal) | Biomed Pharmacother | Irbesartán mejora el mal de montaña crónico en ratas mediante el metabolismo del colesterol |
| [34286497](https://pubmed.ncbi.nlm.nih.gov/34286497/) | 2021 | Sin clasificar | Eur Rev Med Pharmacol Sci | Irbesartán mejora el estrés oxidativo en ratas con hipertensión pulmonar de altura, mediante la flora intestinal |
| [15526904](https://pubmed.ncbi.nlm.nih.gov/15526904/) | 2004 | Preclínico (animal) | Renal Failure | Irbesartán reduce la nefrotoxicidad por ciclosporina |
| [30525078](https://pubmed.ncbi.nlm.nih.gov/30525078/) | 2018 | Preclínico (animal) | Regenerative Therapy | El pretratamiento con un ARA-II anuló los beneficios de láminas de células madre tras infarto de miocardio |

Ningún estudio evalúa directamente la presión arterial pulmonar en pacientes.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20048718 (cancelado) | CORIONAL® 300 MG TABLETAS RECUBIERTAS | Tableta recubierta | IRBESARTAN |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (TxGNN/PrimeKG, no provienen del prospecto):** pancreatitis, angioedema (incluido el hereditario, el adquirido y el inducido por bloqueadores del sistema renina-angiotensina-aldosterona), lupus eritematoso sistémico, miopatía y enfermedades musculares, rabdomiólisis, diabetes mellitus y cetoacidosis diabética, hipotensión, hiperparatiroidismo, encefalopatía hepática, anuria, gota, hipercalcemia, nefrocalcinosis, obstrucción de la arteria renal y deficiencia de potasio, entre otras.
- **Interacciones farmacológicas:** se identificaron 100 interacciones. Las de nivel **mayor** más relevantes son con **citrato de potasio** y **bicarbonato de potasio** (riesgo de hiperpotasemia). Entre las de nivel moderado figuran corticoides (hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona), inhibidores de SGLT2 (canagliflozina, dapagliflozina, empagliflozina), insulinas, ácido acetilsalicílico, morfina y bupropión.
- **Precaución específica:** en la hipertensión renovascular, los ARA-II pueden provocar deterioro agudo de la función renal en estenosis bilateral de arteria renal o en riñón único. Esto debe resolverse antes de cualquier consideración de reposicionamiento.

No se dispone de advertencias del prospecto; consultar el prospecto para el resto de la información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto, pero es solo computacional (L5), sin ensayos clínicos ni literatura específica. Además, el fármaco no tiene registro vigente en Colombia y la hipertensión maligna se maneja habitualmente con terapia parenteral.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank
- Prospecto de INVIMA con advertencias y contraindicaciones, para la revisión de seguridad
- Revisión sistemática de literatura clínica sobre ARA-II en hipertensión maligna y nefroesclerosis hipertensiva
- Evaluación del estado regulatorio (registro cancelado) y de la compatibilidad de vía de administración
- Si se desea priorizar una línea de investigación alternativa, explorar la hipertensión pulmonar asociada a hipoxia, que cuenta con evidencia preclínica (nivel L4), con estudios clínicos de seguridad y eficacia previos a cualquier decisión
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

