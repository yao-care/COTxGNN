---
layout: default
title: Lovastatin
parent: Evidencia Moderada (L3-L4)
nav_order: 414
evidence_level: L3
indication_count: 6
last_modified_at: 2026-10-14
description: "Lovastatin: nueva indicación predicha, Hipercolesterolemia familiar homocigota (nivel de evidencia L3). Indicación original: LOVASTATINA"
monitor_inn: "Lovastatin"
predicted_indications: ["homozygous familial hypercholesterolemia", "hyperlipoproteinemia", "hypercholesterolemia due to cholesterol 7alpha-hydroxylase deficiency", "cholesterol-ester transfer protein deficiency", "hyperlipidemia due to hepatic triglyceride lipase deficiency"]
---

# Lovastatin
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **6** 
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

## Lovastatina: De Indicación Original (LOVASTATINA) a Hipercolesterolemia Familiar Homocigota
{: .text-alpha }

## Resumen en Una Frase

Lovastatina es una estatina (inhibidor de la HMG-CoA reductasa) registrada en Colombia como tableta oral de 20 mg, utilizada tradicionalmente para reducir el colesterol.
El modelo TxGNN predice que podría ser efectiva para **hipercolesterolemia familiar homocigota**,
pero el único ensayo clínico asociado evalúa otro fármaco (alirocumab) y la evidencia directa sobre lovastatina se limita a **reportes de casos y pequeños estudios clínicos históricos**, con resultados mixtos.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | LOVASTATINA (el registro sanitario no detalla la indicación) |
| Nueva Indicación Predicha | Hipercolesterolemia familiar homocigota |
| Puntaje de Predicción TxGNN | 99.89% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Lovastatina inhibe la enzima HMG-CoA reductasa, que limita la velocidad de la síntesis de colesterol en el hígado. Al reducir esa síntesis, aumenta la expresión de receptores de LDL y disminuye el colesterol LDL. Los datos compilados no incluyen una descripción detallada del mecanismo de acción, pero la farmacología registrada confirma como blancos la HMG-CoA reductasa (HMGCR) y el receptor X de pregnano (NR1I2).

La indicación original (reducción de lípidos) y la nueva indicación comparten el mismo eje fisiopatológico: el colesterol LDL elevado. Sin embargo, en la forma homocigota la ausencia o el defecto grave de receptores de LDL limita el beneficio de las estatinas, porque su efecto depende de la actividad residual del receptor.

La literatura histórica refleja esta limitación: hubo respuesta en un niño con actividad residual del receptor tras un trasplante hepático (PMID 3534334, 1986) y ausencia de efecto en niños con receptor negativo (PMID 3397806, 1988). Por eso la plausibilidad mecanística es parcial y depende del estado del receptor.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Fase 3 | Completado | 18 | Estudio abierto de alirocumab en niños y adolescentes (8-17 años) con HoFH. No evalúa lovastatina; sirve solo como contexto de la enfermedad. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [3397806](https://pubmed.ncbi.nlm.nih.gov/3397806/) | 1988 | Estudio clínico | J Pediatr | En tres niños con HoFH sin receptores, lovastatina (2 mg/kg/día) no redujo el LDL-C ni modificó su recambio. |
| [3534334](https://pubmed.ncbi.nlm.nih.gov/3534334/) | 1986 | Reporte de caso | JAMA | Niña con HoFH tras trasplante hepático: con lovastatina se normalizaron los niveles de colesterol. |
| [1785747](https://pubmed.ncbi.nlm.nih.gov/1785747/) | 1991 | Estudio clínico | An Esp Pediatr | Dos pacientes con HoFH tratados con lovastatina combinada con probucol y colestiramina; análisis de receptores de LDL y respuesta lipídica. |
| [2252289](https://pubmed.ncbi.nlm.nih.gov/2252289/) | 1990 | Reporte de caso | An Esp Pediatr | Paciente con HoFH y receptor defectuoso tratado con colestiramina y lovastatina combinadas. |
| [2209665](https://pubmed.ncbi.nlm.nih.gov/2209665/) | 1990 | Reporte de caso | Eur J Pediatr | Niña de 7 años con HoFH tratada con aféresis de LDL (HELP), con y sin lovastatina; regresión de xantomas. |
| [2042836](https://pubmed.ncbi.nlm.nih.gov/2042836/) | 1991 | Revisión | Ann N Y Acad Sci | Revisión del tratamiento farmacológico y quirúrgico de la dislipidemia pediátrica, incluida lovastatina. |
| [12063772](https://pubmed.ncbi.nlm.nih.gov/12063772/) | 2001 | Revisión | Nutr Metab Cardiovasc Dis | Revisión sobre el uso de estatinas en niños con hipercolesterolemia familiar. |
| [2912429](https://pubmed.ncbi.nlm.nih.gov/2912429/) | 1989 | Estudio piloto | Arteriosclerosis | Experiencia con intercambio plasmático y aféresis de LDL en HoFH; se evalúa la combinación con lovastatina. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 38340 (cancelado) | LOVASTATINA 20 MG TABLETAS (Tecnoquímicas S.A., Planta Yumbo) | Tableta | LOVASTATINA |
| 1981959 (cancelado) | LOVASTATINA 20 MG TABLETAS (Novamed S.A.S.) | Tableta | LOVASTATINA |

---

## Consideraciones de Seguridad

- **Contraindicaciones potenciales (según el grafo de conocimiento, no según el prospecto):** enfermedad hepática, enfermedad de la vesícula biliar, miopatía y enfermedades musculares, rabdomiólisis, trombocitopenia, diabetes mellitus y cetoacidosis diabética, hiperglucemia, úlcera péptica, gota, trastornos hipotensivos, enfermedades de la coagulación, síndrome coronario agudo, enfermedad coronaria, infarto de miocardio, hemoglobinopatías y abuso de sustancias, entre otras.
- **Interacciones farmacológicas:** se registraron 2 interacciones de tipo farmacológico, con el receptor X de pregnano (NR1I2) y con la HMG-CoA reductasa (HMGCR). Además, el análisis del caso recomienda vigilar las interacciones mediadas por CYP3A4, la miopatía y la hepatotoxicidad.

No se dispone del texto de advertencias y contraindicaciones del prospecto; se debe consultar el prospecto para completar la información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Aunque el puntaje de TxGNN es alto (99.89%), el único ensayo registrado evalúa alirocumab y no lovastatina, y la evidencia directa sobre lovastatina en HoFH consiste en casos aislados y estudios pequeños con resultados contradictorios según el estado del receptor de LDL. Además, no hay registros sanitarios vigentes en Colombia.

**Para avanzar se necesita:**
- Confirmar la disponibilidad regulatoria, ya que ambos registros están cancelados.
- Obtener el prospecto con advertencias y contraindicaciones oficiales.
- Complementar los datos del mecanismo de acción.
- Estratificar a los pacientes por estado del receptor de LDL (residual frente a negativo), con revisión de seguridad específica para población pediátrica.
- Comparar con alternativas con evidencia más sólida en HoFH (por ejemplo, alirocumab y otras estatinas).

**Nota complementaria:** en los datos compilados, dos indicaciones relacionadas, **hiperlipoproteinemia** (L1, ensayo de Fase 2/3 con lovastatina NCT00116870) e **hipercolesterolemia familiar** (L1, incluye estudios en adolescentes con forma heterocigota), tienen evidencia más sólida y recomendación de "Proceed with Guardrails". Corresponden, sin embargo, al uso lipídico clásico de la lovastatina más que a un reposicionamiento propiamente dicho.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

