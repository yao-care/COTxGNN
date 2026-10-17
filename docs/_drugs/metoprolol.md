---
layout: default
title: Metoprolol
parent: Solo Predicción del Modelo (L5)
nav_order: 439
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Metoprolol: nueva indicación predicha, Enfermedad renal hipertensiva maligna (nivel de evidencia L5). Indicación original: METOPROLOL"
monitor_inn: "metoprolol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "chronic pulmonary heart disease", "trichotillomania"]
---

# Metoprolol
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

# Metoprolol: De Metoprolol (indicación sin especificar) a Enfermedad Renal Hipertensiva Maligna

## Resumen en Una Frase

Metoprolol es un betabloqueante selectivo, registrado en Colombia bajo varios productos cuyo texto de indicación solo indica "METOPROLOL", sin detallar la enfermedad aprobada.
El modelo TxGNN predice que podría ser efectivo para **enfermedad renal hipertensiva maligna**, pero para esta predicción **no hay ensayos clínicos ni publicaciones** que la respalden.
La señal con más soporte entre las 10 predicciones es la **cardiopatía pulmonar crónica** (4 ensayos clínicos y 20 publicaciones), por lo que se incluye como referencia comparativa.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | METOPROLOL (el registro no detalla la indicación aprobada) |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna |
| Puntaje de Predicción TxGNN | 99.91% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 4 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, metoprolol es un bloqueador beta-1 selectivo: reduce la frecuencia cardíaca, el gasto cardíaco y la liberación de renina.

Mecanísticamente, la reducción de renina y del gasto cardíaco podría ayudar al control de la presión arterial en la hipertensión maligna con daño renal. Sin embargo, metoprolol ya es un antihipertensivo de uso general, por lo que esta predicción **no representa una señal de reposicionamiento distinta**, sino una extensión de su uso cardiovascular habitual.

Además, no hay ensayos ni literatura que evalúen metoprolol específicamente en esta enfermedad. El puntaje alto de TxGNN es, por ahora, una predicción sin respaldo empírico.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta indicación.

*Referencia: para la indicación predicha en el puesto 9 (cardiopatía pulmonar crónica) sí existen ensayos, que se resumen a continuación como contexto.*

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT06825728](https://clinicaltrials.gov/study/NCT06825728) | Fase 4 | Aún no recluta | 311 | Metoprolol en insuficiencia cardíaca con fracción de eyección reducida y EPOC; evalúa mortalidad y rehospitalización. |
| [NCT02587351](https://clinicaltrials.gov/study/NCT02587351) | Fase 3 | Terminado | 532 | Betabloqueantes para prevenir exacerbaciones de EPOC; terminado anticipadamente. |
| [NCT00384566](https://clinicaltrials.gov/study/NCT00384566) | Fase 4 | Retirado | 0 | Carvedilol vs metoprolol en evaluación respiratoria; sin participantes ni datos. |
| [NCT05096884](https://clinicaltrials.gov/study/NCT05096884) | Fase 1 temprana | Terminado | 14 | Disnea y taquicardia post-COVID; relevancia solo indirecta. |

---

## Evidencia de Literatura

Para la enfermedad renal hipertensiva maligna no hay literatura relacionada disponible. La única publicación de la predicción vecina (hipertensión renovascular maligna) no respalda la eficacia de metoprolol:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [1988765](https://pubmed.ncbi.nlm.nih.gov/1988765/) | 1991 | Estudio diagnóstico | Medicine | Cromogranina A como marcador diagnóstico de feocromocitoma; no evalúa metoprolol. |

*Referencia de contexto (cardiopatía pulmonar crónica):*

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38587241](https://pubmed.ncbi.nlm.nih.gov/38587241/) | 2024 | ECA | N Engl J Med | Betabloqueantes tras infarto con fracción de eyección preservada. |
| [38762800](https://pubmed.ncbi.nlm.nih.gov/38762800/) | 2024 | ECA | JAMA | Bisoprolol en EPOC con alto riesgo de exacerbación; menciona que metoprolol no redujo exacerbaciones y aumentó las que requirieron hospitalización. |
| [32000982](https://pubmed.ncbi.nlm.nih.gov/32000982/) | 2020 | Cohorte | Am J Cardiol | Metoprolol vs carvedilol en insuficiencia cardíaca, EPOC, diabetes e insuficiencia renal. |
| [26844454](https://pubmed.ncbi.nlm.nih.gov/26844454/) | 2016 | Cohorte | Medicine | Carvedilol, bisoprolol y metoprolol en insuficiencia cardíaca con EPOC (base de datos de Taiwán). |
| [14520486](https://pubmed.ncbi.nlm.nih.gov/14520486/) | 2003 | Estudio clínico | Heart Vessels | Metoprolol puede usarse con seguridad en enfermedad coronaria con EPOC. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19961415 | Metoprolol Tartrato 50 mg tabletas | Tableta | METOPROLOL |
| 20278182 | Metoprolol Tartrato 5 mg/5 mL solución inyectable | Solución inyectable | METOPROLOL |
| 19992946 | Metoprolol tabletas recubiertas 50 mg | Tableta con cubierta entérica con película | METOPROLOL |
| 19927923 | Betaloc ZOK 25 mg | Tableta de liberación prolongada | METOPROLOL |

Los cuatro registros figuran como **cancelados**; no hay registros vigentes.

---

## Consideraciones de Seguridad

- **Contraindicaciones sugeridas por el grafo de conocimiento** (relaciones fármaco-enfermedad del modelo, no texto de prospecto): trastornos de ansiedad y neuróticos, pancreatitis, enfermedad hepática y de la vesícula, lupus eritematoso sistémico, psoriasis, diabetes mellitus y cetoacidosis diabética, gota, hipotensión, hiperparatiroidismo, encefalopatía hepática, anuria, miastenia gravis y feocromocitoma, entre otras.
- **Interacciones farmacológicas**: se identificaron 338 interacciones. Las más relevantes son de nivel moderado, con epinefrina, corticoides (hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona), anticolinérgicos (atropina, hiosciamina, glicopirronio), bupropión, morfina, cimetidina, lorcaserina, inhibidores de SGLT2 (canagliflozina, dapagliflozina), clorpropamida y sales de calcio. Con ácido acetilsalicílico y óxido de magnesio son de nivel menor.
- **Precaución específica**: en hipertensión pulmonar y cardiopatía pulmonar, los betabloqueantes se usan con cautela por el riesgo de broncoespasmo y el efecto sobre la función del ventrículo derecho. El ensayo BLOCK-COPD mostró más exacerbaciones graves con metoprolol en EPOC.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para enfermedad renal hipertensiva maligna tiene un puntaje alto, pero carece de ensayos y literatura (nivel L5), y se solapa con el uso antihipertensivo ya establecido de metoprolol. Además, no hay registros sanitarios vigentes en Colombia.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (DrugBank) y de las advertencias y contraindicaciones del prospecto de INVIMA, que hoy bloquean el tamizaje de seguridad.
- Revisión de literatura dirigida a metoprolol en hipertensión maligna y nefroesclerosis hipertensiva.
- Aclarar la indicación aprobada en los registros y el estado regulatorio (todos cancelados).
- Valorar si la indicación con más soporte (cardiopatía pulmonar crónica, nivel L3, "Research Question") merece priorizarse. Requiere resolver la seguridad de metoprolol en EPOC, dados los resultados de BLOCK-COPD.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

