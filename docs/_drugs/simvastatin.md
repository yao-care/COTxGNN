---
layout: default
title: Simvastatin
parent: Solo Predicción del Modelo (L5)
nav_order: 587
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
description: "Simvastatin: nueva indicación predicha, Infarto del tronco encefálico (nivel de evidencia L1). Indicación original: Simvastatina combinaciones paquetes"
monitor_inn: "simvastatin"
predicted_indications: ["brain stem infarction", "cholesterol-ester transfer protein deficiency", "HIV infectious disease", "ABri amyloidosis", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Simvastatin
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

## Simvastatina: De Combinaciones de Simvastatina a Infarto del tronco encefálico
{: .text-alpha }

## Resumen en Una Frase

La simvastatina es una estatina (inhibidor de la HMG-CoA reductasa) registrada en Colombia dentro de una combinación con ezetimiba, y su indicación original figura como "simvastatina combinaciones paquetes".
El modelo TxGNN predice que podría ser efectiva para **hipercolesterolemia familiar**,
con **8 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección. Cabe señalar que se trata más de un uso ya establecido que de un reposicionamiento propiamente dicho.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Simvastatina combinaciones paquetes |
| Nueva Indicación Predicha | Hipercolesterolemia familiar |
| Puntaje de Predicción TxGNN | 0.9941 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 1) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción registrado. Según la información farmacológica conocida, la simvastatina inhibe la HMG-CoA reductasa, reduce la síntesis hepática de colesterol y aumenta los receptores de LDL, lo que incrementa la depuración del colesterol LDL (LDL-C).

La indicación original (una combinación de simvastatina con ezetimiba para reducir lípidos) y la hipercolesterolemia familiar comparten la misma vía fisiopatológica: el exceso de LDL-C. En la hipercolesterolemia familiar heterocigota, la elevación residual de LDL-C suele requerir terapia combinada (por ejemplo, ezetimiba o inhibidores de PCSK9), lo que coincide con el producto registrado en Colombia.

Por tanto, la predicción es mecanísticamente coherente, pero corresponde a un uso terapéutico establecido y no a un hallazgo novedoso.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Fase 3 | Completado | 720 | ENHANCE: ezetimiba + simvastatina en dosis alta vs. simvastatina sola sobre la progresión de la aterosclerosis carotídea en hipercolesterolemia familiar heterocigota |
| [NCT00129402](https://clinicaltrials.gov/study/NCT00129402) | Fase 3 | Completado | 248 | Eficacia y seguridad de ezetimiba con simvastatina en adolescentes (10-17 años) con hipercolesterolemia familiar heterocigota |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Fase 3 | Completado | 442 | Efectos renales de rosuvastatina y simvastatina en dislipidemia tipo IIa y IIb, incluida hipercolesterolemia familiar heterocigota |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Fase 3 | Completado | 50 | Eficacia y seguridad de ezetimiba añadida a atorvastatina o simvastatina en hipercolesterolemia familiar homocigota |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Fase 3 | Completado | 44 | Extensión abierta de seguridad a largo plazo (hasta 24 meses) de ezetimiba con atorvastatina o simvastatina en hipercolesterolemia familiar homocigota |
| [NCT01709500](https://clinicaltrials.gov/study/NCT01709500) | Fase 3 | Completado | 249 | Alirocumab vs. placebo en hipercolesterolemia familiar heterocigota no controlada con terapia hipolipemiante (relación indirecta con simvastatina) |
| [NCT03510884](https://clinicaltrials.gov/study/NCT03510884) | Fase 3 | Completado | 153 | Alirocumab vs. placebo en niños y adolescentes con hipercolesterolemia familiar heterocigota (simvastatina, a lo sumo, como tratamiento de base) |
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Fase 3 | Completado | 18 | Alirocumab abierto en niños y adolescentes con hipercolesterolemia familiar homocigota (simvastatina, a lo sumo, como tratamiento de base) |
| [NCT01890967](https://clinicaltrials.gov/study/NCT01890967) | Fase 2 | Completado | 527 | Estudio de búsqueda de dosis de LY3015014 (anticuerpo anti-PCSK9) en hipercolesterolemia primaria con estatinas de base |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [18376000](https://pubmed.ncbi.nlm.nih.gov/18376000/) | 2008 | Ensayo clínico (ENHANCE) | N Engl J Med | Simvastatina con o sin ezetimiba en hipercolesterolemia familiar; evalúa el efecto sobre la progresión de la aterosclerosis |
| [28685504](https://pubmed.ncbi.nlm.nih.gov/28685504/) | 2017 | Revisión sistemática (Cochrane) | Cochrane Database Syst Rev | Estatinas en niños con hipercolesterolemia familiar |
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Revisión sistemática (Cochrane) | Cochrane Database Syst Rev | Actualización de la revisión sobre estatinas en niños con hipercolesterolemia familiar |
| [12908847](https://pubmed.ncbi.nlm.nih.gov/12908847/) | 2003 | Revisión | Drug Safety | Beneficios y riesgos de la simvastatina en hipercolesterolemia familiar |
| [15794711](https://pubmed.ncbi.nlm.nih.gov/15794711/) | 2005 | Revisión | Expert Opin Drug Saf | Evaluación de beneficios y riesgos de la simvastatina en hipercolesterolemia familiar |
| [41824590](https://pubmed.ncbi.nlm.nih.gov/41824590/) | 2026 | Guía clínica | J Am Coll Cardiol | Guía ACC/AHA 2026 para el manejo de la dislipidemia, que reemplaza la guía de 2018 |
| [41824552](https://pubmed.ncbi.nlm.nih.gov/41824552/) | 2026 | Guía clínica | Circulation | Publicación paralela de la guía ACC/AHA 2026 sobre dislipidemia |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guía clínica | Endocr Pract | Guías AACE/ACE para el manejo de la dislipidemia y la prevención cardiovascular |
| [14727947](https://pubmed.ncbi.nlm.nih.gov/14727947/) | 2003 | Revisión | Am J Cardiovasc Drugs | Ezetimiba inhibe la absorción intestinal de colesterol y reduce el LDL-C al combinarse con estatinas |
| [35629051](https://pubmed.ncbi.nlm.nih.gov/35629051/) | 2022 | Estudio transversal | J Clin Med | Efecto de simvastatina 10 mg sobre parámetros de inmunidad celular en 26 niños con hipercolesterolemia familiar |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19989089 (cancelado) | Ezetimibe 10 + Simvastatina 20 tabletas cubiertas | Tableta recubierta | Simvastatina combinaciones paquetes |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** el grafo de conocimiento del modelo asocia la simvastatina con enfermedades como pancreatitis, enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia, hiperglucemia, úlcera péptica, miopatía, enfermedad muscular, rabdomiólisis, diabetes mellitus, cetoacidosis diabética, gota, trastornos de la coagulación, síndrome coronario agudo, enfermedad coronaria e infarto de miocardio, entre otras. Estas relaciones requieren verificación con el prospecto oficial.
- **Interacciones farmacológicas:** se registraron 696 interacciones. Entre las de nivel **mayor** figuran amiodarona, amlodipino y fenofibrato. Hay además múltiples interacciones de nivel moderado (por ejemplo, zidovudina, paclitaxel, nifedipino, omeprazol, aprepitant y etanol).
- **Riesgo de miopatía:** dependiente de la dosis (especialmente con 80 mg). En personas con VIH, los inhibidores de proteasa potenciados y el cobicistat elevan de forma marcada la exposición a simvastatina, con riesgo de miopatía y rabdomiólisis.
- **Uso pediátrico:** requiere consideraciones específicas.

No se dispone de advertencias ni contraindicaciones del prospecto de INVIMA; consultar el prospecto para esa información.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Varios ensayos de Fase 3 completados (ENHANCE, con 720 participantes, y el estudio en adolescentes, con 248) evalúan directamente simvastatina en hipercolesterolemia familiar, lo que corresponde a un nivel de evidencia L1. Sin embargo, es un uso ya establecido, el único registro sanitario en Colombia está cancelado y existe una carga alta de interacciones y riesgo de miopatía.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), una brecha que bloquea el tamizaje de seguridad.
- Confirmar el mecanismo de acción en DrugBank.
- Verificar la situación regulatoria: el único registro está cancelado, por lo que habría que confirmar la disponibilidad de productos vigentes con simvastatina en Colombia.
- Definir un plan de monitoreo de seguridad (función hepática, CK/miopatía, revisión de interacciones, uso pediátrico).
- Aclarar que el resto de las predicciones (por ejemplo, infarto de tronco encefálico, VIH, amiloidosis ABri) carecen de respaldo clínico directo y deben mantenerse en espera. En VIH, la simvastatina suele evitarse con regímenes potenciados por la interacción farmacológica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

