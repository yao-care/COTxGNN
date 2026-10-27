---
layout: default
title: Pitavastatin
parent: Evidencia Moderada (L3-L4)
nav_order: 519
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Pitavastatin: nueva indicación predicha, Hipercolesterolemia familiar homocigota (nivel de evidencia L4). Indicación original: No especificada en el registro (el texto aprobado solo dice \"PITAVAST…"
monitor_inn: "pitavastatin"
predicted_indications: ["hyperlipoproteinemia", "cholesterol-ester transfer protein deficiency", "HIV infectious disease", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "hyperlipidemia due to hepatic triglyceride lipase deficiency", "feline acquired immunodeficiency syndrome"]
---

# Pitavastatin
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
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

## Pitavastatina: De Indicación Registrada (Pitavastatina) a Hipercolesterolemia Familiar Homocigota
{: .text-alpha }

## Resumen en Una Frase

Pitavastatina es una estatina (inhibidor de la HMG-CoA reductasa) registrada en Colombia con el nombre comercial ALTACOR®, cuyo texto de indicación en el registro sanitario solo indica "PITAVASTATINA", sin detallar la enfermedad.
El modelo TxGNN predice que podría ser efectiva para **hipercolesterolemia familiar homocigota** (puntaje 99.99 %), pero la evidencia directa es muy limitada: **0 ensayos clínicos** y **2 publicaciones** indirectas (un ensayo en dislipidemia por VIH y un reporte de casos de una enfermedad distinta).

> **Nota importante:** el primer resultado del modelo tiene la evidencia más débil entre las indicaciones relevantes. Las predicciones con mayor respaldo son **hiperlipoproteinemia** (L1), **hipercolesterolemia familiar** (L2) e **infección por VIH** (L1, como prevención cardiovascular). Se resumen en la sección de conclusión.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto aprobado solo dice "PITAVASTATINA"); clase: hipolipemiante |
| Nueva Indicación Predicha | Hipercolesterolemia familiar homocigota |
| Puntaje de Predicción TxGNN | 99.996 % |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo cancelado (ningún registro vigente) |
| Número de Registros Sanitarios | 3 (los 3 cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, pitavastatina inhibe la HMG-CoA reductasa, reduce la síntesis hepática de colesterol y aumenta la expresión de receptores hepáticos de LDL, lo que disminuye el colesterol LDL.

La hipercolesterolemia familiar homocigota se caracteriza por una función residual del receptor de LDL nula o mínima. Por ello, la eficacia de una estatina, cuyo efecto depende justamente de ese receptor, se espera **limitada**. La relación mecanística existe (ambas son enfermedades del colesterol), pero es débil en esta forma grave de la enfermedad.

La evidencia es indirecta: un ensayo en pacientes con VIH y dislipidemia (no HoFH) y un reporte de casos de hipercolesterolemia autosómica recesiva, una condición distinta aunque clínicamente similar.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta indicación.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [28416195](https://pubmed.ncbi.nlm.nih.gov/28416195/) | 2017 | ECA (Fase 4, INTREPID) | The Lancet HIV | Pitavastatina vs. pravastatina en adultos con VIH-1 y dislipidemia; evalúa seguridad y eficacia. Población distinta a HoFH |
| [39532566](https://pubmed.ncbi.nlm.nih.gov/39532566/) | 2025 | Reporte de casos | Journal of Clinical Lipidology | Respuesta rápida de reducción lipídica en dos casos de hipercolesterolemia autosómica recesiva (variantes en LDLRAP1) |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20250238 | ALTACOR® 2 MG TABLETA RECUBIERTA | Tableta recubierta | PITAVASTATINA | Cancelado |
| 20250244 | ALTACOR® 4 MG TABLETAS RECUBIERTAS | Tableta recubierta | PITAVASTATINA | Cancelado |
| 20250209 | ALTACOR® 1 MG TABLETAS RECUBIERTAS | Tableta recubierta | PITAVASTATINA | Cancelado |

Los tres registros pertenecen a ALTADIS FARMACÉUTICA S.A.S. y están cancelados; no hay registros vigentes en los datos compilados.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad, no texto de prospecto): enfermedad hepática, enfermedad de la vesícula biliar, hipotiroidismo (incluido mixedema e hipotiroidismo congénito), miopatía y enfermedades musculares, parálisis periódica familiar, trastornos hipotensivos, rabdomiólisis, fascitis nodular, insuficiencia renal y lesiones.
- **Interacciones farmacológicas:** se registraron 86 interacciones. Entre las principales:
  - **Mayor:** eritromicina.
  - **Moderadas:** rosuvastatina, simvastatina, cobicistat, eltrombopag, metronidazol, tinidazol, secnidazol, benznidazol, naltrexona, eluxadolina, etanol, cloroquina, hidroxicloroquina, disulfiram, zafirlukast, cloranfenicol y dapsona.
  - **Menores:** warfarina y dicumarol.
- El texto del prospecto del INVIMA con advertencias y contraindicaciones no estaba disponible; consultar el prospecto para información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para HoFH solo hay evidencia indirecta (L4), sin ensayos clínicos, y el mecanismo de la estatina depende del receptor de LDL, que en esta enfermedad está casi ausente. Además, no hay registros sanitarios vigentes en Colombia.

**Otras predicciones del modelo (para contexto):**

| Indicación Predicha | Nivel | Recomendación | Comentario |
|------|------|------|------|
| Hiperlipoproteinemia | L1 | Proceed with Guardrails | Ensayos Fase 3/4 controlados en dislipidemia (p. ej., NCT01386853, NCT01256476); es prácticamente el uso original del fármaco, por lo que no es un reposicionamiento real |
| Hipercolesterolemia familiar | L2 | Proceed with Guardrails | Estudios pediátricos y de adultos con reducción de LDL-C; el único ensayo listado (NCT01890967) evalúa otro fármaco |
| Hipercolesterolemia autosómica dominante | L2 | Proceed with Guardrails | Se solapa con la forma heterocigota; mismo respaldo pediátrico |
| Infección por VIH | L1 | Proceed with Guardrails | Debe plantearse como prevención cardiovascular en personas con VIH (ensayo REPRIEVE, NEJM 2023, [PMID 37486775](https://pubmed.ncbi.nlm.nih.gov/37486775/)); no trata la infección |
| Deficiencia de CETP, deficiencia de colesterol 7α-hidroxilasa, trastorno del neurodesarrollo con ataxia, deficiencia de lipasa hepática, SIDA felino | L5 | Hold | Solo puntaje del modelo, sin evidencia |

**Para avanzar se necesita:**
- Verificar si existen otros productos de pitavastatina con registro vigente en Colombia, ya que los tres de ALTACOR® están cancelados.
- Obtener el prospecto del INVIMA (advertencias y contraindicaciones) y los datos del mecanismo de acción desde DrugBank.
- Para HoFH: evidencia clínica directa en pacientes homocigotos, o reorientar el análisis hacia las indicaciones con mayor respaldo (hipercolesterolemia familiar heterocigota y prevención cardiovascular en VIH).
- Plan de monitoreo de interacciones (especialmente con eritromicina y antirretrovirales), de riesgo de miopatía/rabdomiólisis y de función hepática y renal.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

