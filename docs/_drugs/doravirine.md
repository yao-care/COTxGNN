---
layout: default
title: Doravirine
parent: Solo Predicción del Modelo (L5)
nav_order: 232
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Doravirine: nueva indicación predicha, Síndrome de inmunodeficiencia adquirida felina (nivel de evidencia L5). Indicación original: Lamivudina, tenofovir disoproxilo y doravirina (combinación)"
monitor_inn: "Doravirine"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Doravirine
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

# Doravirina: De VIH-1 a Síndrome de Inmunodeficiencia Adquirida Felina

## Resumen en Una Frase

Doravirina es un inhibidor no nucleosídico de la transcriptasa inversa (NNRTI) del VIH-1, autorizado en Colombia solo o en combinación con lamivudina y tenofovir disoproxilo.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de inmunodeficiencia adquirida felina**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción; se basa únicamente en el modelo computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Lamivudina, tenofovir disoproxilo y doravirina (combinación); doravirina |
| Nueva Indicación Predicha | Síndrome de inmunodeficiencia adquirida felina |
| Puntaje de Predicción TxGNN | 99.93% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Doravirina es un inhibidor no nucleosídico de la transcriptasa inversa del VIH-1. Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción, por lo que este análisis se basa en la clase farmacológica conocida del fármaco.

El virus de la inmunodeficiencia felina (FIV) es un lentivirus emparentado con el VIH, lo que explica en parte la predicción del modelo. Sin embargo, su transcriptasa inversa es diferente y, en general, los NNRTI tienen poca actividad contra el FIV. La plausibilidad biológica es baja a moderada y no está verificada para esta clase de fármacos.

Esta predicción es solo computacional. Sin ensayos ni literatura, no se puede considerar respaldada.

**Otras predicciones del modelo (con la misma limitación de evidencia):**
- **Infección por virus de inmunodeficiencia simia (SIV)**, puntaje 99.93%: el SIV está estrechamente relacionado con el VIH, pero los NNRTI suelen ser específicos para la transcriptasa inversa del VIH-1 y el SIV (en particular SIVmac) es naturalmente resistente a muchos de ellos.
- **Trastorno del neurodesarrollo con marcha atáxica, ausencia del habla y disminución de la sustancia blanca cortical**, puntaje 99.91%: no se identificó un vínculo mecanístico plausible; el puntaje probablemente refleja artefactos del grafo de conocimiento.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Para la indicación principal (inmunodeficiencia felina) no hay literatura relacionada disponible.

Para la segunda predicción (infección por SIV) se recuperó una sola publicación, que **no constituye evidencia directa** para doravirina:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31658118](https://pubmed.ncbi.nlm.nih.gov/31658118/) | 2020 | Revisión | Current Opinion in HIV and AIDS | Analiza el posible papel de islatravir (inhibidor de la translocación de la transcriptasa inversa, otro fármaco) en el tratamiento y la prevención del VIH-1 |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20160000 | DELSTRIGO® tabletas recubiertas (cancelado) | Tableta recubierta | Lamivudina, tenofovir disoproxilo y doravirina |
| 20178856 | PIFELTRO 100 mg tabletas recubiertas (cancelado) | Tableta recubierta | Doravirina |

Ambos registros, de Merck Sharp & Dohme LLC, están cancelados; actualmente no hay registros vigentes.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas:** se identificaron 59 interacciones en total. Las de mayor relevancia:
  - **Mayor:** dexametasona y lumacaftor.
  - **Moderada:** glicerol fenilbutirato, metreleptina, troglitazona, deferasirox, praziquantel y griseofulvina.
  - **Menor:** aprepitant, cimetidina, claritromicina, clotrimazol, miconazol, cobicistat, ticagrelor, ivacaftor, zafirlukast, cloranfenicol, eritromicina y fluconazol, entre otros.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Las tres predicciones tienen nivel de evidencia L5: no hay ensayos clínicos ni literatura directa, y el mecanismo sugiere baja actividad de los NNRTI contra FIV y SIV. Además, los registros sanitarios en Colombia están cancelados.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción de doravirina.
- Estudios preclínicos (in vitro) de actividad de doravirina contra la transcriptasa inversa de FIV y SIV.
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones) para completar la evaluación de seguridad.
- Aclarar la situación regulatoria actual del fármaco en Colombia.
- Valorar si la indicación en medicina veterinaria es relevante para el objetivo del proyecto.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

