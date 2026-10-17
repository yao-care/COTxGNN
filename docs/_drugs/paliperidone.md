---
layout: default
title: Paliperidone
parent: Solo Predicción del Modelo (L5)
nav_order: 494
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Paliperidone: nueva indicación predicha, Distrofia retiniana con o sin anomalías extraoculares (nivel de evidencia L5). Indicación original: Paliperidona"
monitor_inn: "Paliperidone"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "myopia X-linked", "syndromic myopia", "hydranencephaly (disease)", "congenital disorder of glycosylation with defective fucosylation", "myopia 26, X-linked, female-limited", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "atypical glycine encephalopathy"]
---

# Paliperidone
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

# Paliperidona: De Antipsicótico Oral de Liberación Prolongada a Distrofia Retiniana con o sin Anomalías Extraoculares

## Resumen en Una Frase

Paliperidona es un antipsicótico (metabolito activo de la risperidona, 9-hidroxirisperidona) que en Colombia se registró como tableta oral de liberación prolongada (Invega®).
El modelo TxGNN predice que podría ser efectivo para **distrofia retiniana con o sin anomalías extraoculares**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción: es solo una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Paliperidona (el registro sanitario solo indica el nombre del principio activo, sin detallar la indicación) |
| Nueva Indicación Predicha | Distrofia retiniana con o sin anomalías extraoculares |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción. Según el conocimiento farmacológico general, la paliperidona antagoniza los receptores dopaminérgicos D2 y serotoninérgicos 5-HT2A, lo que explica su uso como antipsicótico.

**No se ha identificado un vínculo mecanístico plausible** entre ese mecanismo y la causa de la distrofia retiniana, que es de origen genético. No existen estudios clínicos ni literatura que respalden la relación. El puntaje alto del modelo (99.92%) proviene únicamente de patrones del grafo de conocimiento y no equivale a evidencia de eficacia. Tampoco hay una similitud establecida entre la indicación original (psiquiátrica) y esta nueva indicación (oftalmológica/genética).

**Nota:** entre las predicciones evaluadas, la única con algo de evidencia asociada es *esquizofrenia resistente al tratamiento* (puntaje 99.80%, nivel L4, recomendación "pregunta de investigación"). Allí el ajuste mecanístico es fuerte, pero los ensayos son de Fase 4 y no confirman a la paliperidona como intervención específica. La literatura recuperada son revisiones generales, y el estándar de tratamiento en esa población es la clozapina. Es un candidato más razonable para análisis posterior que la predicción principal.

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
| 19983120 (cancelado) | INVEGA® Tabletas de Liberación Prolongada 6 mg (Janssen Cilag S.A.) | Tableta de liberación prolongada | Paliperidona |

---

## Consideraciones de Seguridad

No se dispone de advertencias ni contraindicaciones del prospecto en los datos compilados. Se debe consultar el prospecto para esa información.

- **Condiciones de precaución según el grafo de conocimiento (no provienen del prospecto):** se identificaron relaciones de contraindicación con, entre otras:
  - **Cardiovasculares:** síndrome de QT largo (incluido el familiar), torsades de pointes, hipotensión ortostática, trastornos hipotensivos, infarto de miocardio, síndrome de taquicardia postural ortostática.
  - **Neurológicas:** epilepsia, enfermedades de los ganglios basales, atrofia multisistémica, distonía focal de la mano, blefaroespasmo.
  - **Metabólicas:** hiperglucemia, diabetes mellitus, cetoacidosis diabética, hiperlipidemia, obesidad, deficiencia de potasio.
  - **Hematológicas:** neutropenia, agranulocitosis, hemoglobinopatías.
  - **Otras:** enfermedad de Crohn y enfermedad inflamatoria intestinal, insuficiencia renal, carcinoma de mama en mujeres.
- **Interacciones farmacológicas:** se registraron 100 interacciones. Las de gravedad **mayor** incluyen **bupropión** y **morfina**. Entre las de gravedad **moderada** están:
  - Antidiabéticos: acarbosa, metformina, pioglitazona, alogliptina, albiglutida, canagliflozina, clorpropamida.
  - Anticolinérgicos: atropina, hiosciamina, glicopirronio.
  - Otros: famotidina, epinefrina, hidrocortisona, anfotericina B, loperamida, lorcaserina, bisacodilo.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo, sin ensayos clínicos ni literatura (nivel L5). No existe un vínculo mecanístico plausible entre el antagonismo D2/5-HT2A y una distrofia retiniana genética. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción y un análisis de la plausibilidad biológica con la fisiopatología retiniana.
- Estudios preclínicos o de mecanismo que justifiquen la hipótesis.
- Obtener y analizar el prospecto (advertencias y contraindicaciones) y confirmar la situación regulatoria vigente del producto en Colombia.
- Valorar priorizar la indicación *esquizofrenia resistente al tratamiento*, que tiene mayor respaldo mecanístico, antes de invertir recursos en esta predicción.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

