---
layout: default
title: Venetoclax
parent: Solo Predicción del Modelo (L5)
nav_order: 656
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Venetoclax: nueva indicación predicha, Linfoma de Hodgkin (nivel de evidencia L4). Indicación original: No especificada en el registro (el texto apr…"
monitor_inn: "VENETOCLAX"
predicted_indications: ["Hodgkins lymphoma", "chronic myelogenous leukemia, BCR-ABL1 positive", "Ewing sarcoma", "follicular lymphoma", "metastatic neoplasm", "malignant spiradenoma"]
---

# Venetoclax
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Venetoclax: De Indicación No Especificada en el Registro a Linfoma de Hodgkin
{: .text-alpha }

## Resumen en Una Frase

Venetoclax es un inhibidor oral de BCL-2. Su registro sanitario en Colombia solo consigna el nombre del principio activo y no detalla la indicación aprobada. El modelo TxGNN predice que podría ser efectivo en **leucemia linfocítica crónica/linfoma linfocítico de células pequeñas (LLC/LLCP) del subtipo de centro pregerminal**, pero solo hay **0 ensayos clínicos** y **1 publicación** indirecta que respalden esta predicción. Además, este subtipo pertenece a una indicación ya establecida de venetoclax, por lo que no es un reposicionamiento genuino.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto aprobado solo repite el nombre "Venetoclax") |
| Nueva Indicación Predicha | Leucemia linfocítica crónica/linfoma linfocítico de células pequeñas del centro pregerminal (LLC/LLCP con IGHV no mutado) |
| Puntaje de Prediccion TxGNN | 0.9951 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada para este informe. Venetoclax se conoce como un inhibidor selectivo de la proteína antiapoptótica BCL-2. Al bloquearla, restablece la muerte celular programada en células malignas que dependen de BCL-2 para sobrevivir.

La LLC/LLCP es una neoplasia de linfocitos B con marcada dependencia de BCL-2, por lo que el encaje mecanístico es fuerte. El subtipo predicho corresponde a la LLC con genes IGHV no mutados, de origen pregerminal y pronóstico desfavorable. Según el análisis de los datos, este subtipo forma parte de una indicación ya establecida de venetoclax (LLC/LLCP). Por eso la predicción es biológicamente plausible, pero más una confirmación que un hallazgo nuevo.

La única publicación vinculada es una revisión sobre la estructura y función del receptor de células B (BCR) tumoral en la LLC. Aporta contexto biológico sobre este subtipo, pero no evalúa venetoclax directamente. Por ello la evidencia es indirecta.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para este subtipo específico.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35158929](https://pubmed.ncbi.nlm.nih.gov/35158929/) | 2022 | Revisión / análisis traslacional | Cancers | Analiza la estructura y función del receptor de células B tumoral en la LLC. Distingue la LLC con IGHV no mutado (origen pregerminal, mal pronóstico) de la mutada (origen postgerminal, buen pronóstico). Es evidencia indirecta sobre biología, no sobre venetoclax. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20139971 (cancelado) | VENCLEXTA® 100 MG TABLETA RECUBIERTA (ABBVIE S.A.S.) | Tableta recubierta | Solo consigna el nombre del principio activo ("Venetoclax"), sin indicación detallada |

Venetoclax está comercializado en Colombia y tiene 1 registro vigente de 1 en total.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de BCL-2, mimético de BH3) |
| Riesgo de Mielosupresión | Medio a alto. La literatura describe citopenias (neutropenia, trombocitopenia) como eventos frecuentes |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial, función renal y hepática, electrolitos, ácido úrico y fósforo (riesgo de síndrome de lisis tumoral) |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas:** la consulta de interacciones se completó y arrojó 100 interacciones. Entre las 20 listadas, las de nivel **mayor** son:
  - Aprepitant
  - Dexametasona
  - Claritromicina
  - Eliglustat
  - Rolapitant
  - Fidaxomicina
  - Cobicistat
  - Deferiprona
  - Samario (153Sm) lexidronam

  Las de nivel **moderado** incluyen:
  - Alvimopán
  - Loperamida
  - Cimetidina
  - Naldemedina
  - Metreleptina
  - Miconazol
  - Rifaximina
  - Clotrimazol
  - Troglitazona
  - Deferasirox

  La de nivel **menor** es naloxegol.
- Venetoclax es sustrato de CYP3A. Los inhibidores de esta enzima, como los azoles (p. ej., posaconazol) y los macrólidos, pueden requerir ajuste de dosis.
- Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
En Colombia, venetoclax está comercializado y tiene 1 registro vigente de 1 en total.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto del INVIMA (advertencias, contraindicaciones e indicaciones aprobadas) para completar la evaluación de seguridad.
- Obtener datos detallados del mecanismo de acción desde DrugBank.
- Aclarar la situación regulatoria: el registro está cancelado y el texto de indicación no detalla el uso aprobado.
- Reorientar el análisis hacia candidatos con evidencia clínica específica, como linfoma folicular (L2) o leucemia mieloide crónica BCR-ABL1 positiva (L2). La leucemia mieloide (L1) ya es un uso clínico establecido.
- Diseñar un plan de monitoreo para síndrome de lisis tumoral, citopenias e interacciones con inhibidores de CYP3A.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

