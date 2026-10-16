---
layout: default
title: Atorvastatin
parent: Evidencia Alta (L1-L2)
nav_order: 73
evidence_level: L1
indication_count: 6
last_modified_at: 2026-10-14
description: "Atorvastatin: nueva indicación predicha, Hipercolesterolemia familiar (nivel de evidencia L1). Indicación original: Atorvastatin"
monitor_inn: "Atorvastatin"
predicted_indications: ["familial hypercholesterolemia", "HIV infectious disease", "brain stem infarction", "cholesterol-ester transfer protein deficiency", "hypercholesterolemia due to cholesterol 7alpha-hydroxylase deficiency", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Atorvastatin
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **6** 
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

# Atorvastatina: De Indicación Original (hipercolesterolemia) a Hipercolesterolemia Familiar

## Resumen en Una Frase

Atorvastatina es una estatina (inhibidor de la HMG-CoA reductasa) utilizada para reducir el colesterol. Su indicación original registrada en Colombia consta solo como "atorvastatin".
El modelo TxGNN predice que podría ser efectiva para **hipercolesterolemia familiar**, con **14 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección. Cabe señalar que esta predicción corresponde más a un uso ya establecido que a un reposicionamiento propiamente dicho.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Atorvastatin (el texto del registro no detalla la indicación) |
| Nueva Indicación Predicha | Hipercolesterolemia familiar |
| Puntaje de Predicción TxGNN | 99.42% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Atorvastatina inhibe la enzima HMG-CoA reductasa, que es el paso clave de la síntesis de colesterol en el hígado. Al reducir esa síntesis, aumentan los receptores hepáticos de LDL y se incrementa la eliminación del colesterol LDL (LDL-C) de la sangre. (Los datos compilados para este informe no incluyen el mecanismo de acción detallado, pero el blanco HMGCR figura en los datos farmacológicos.)

La indicación original y la nueva están estrechamente relacionadas: ambas implican niveles elevados de colesterol. La hipercolesterolemia familiar es una forma hereditaria de colesterol muy alto, y las estatinas son tratamiento de primera línea en la forma heterocigota. Por eso este caso es en la práctica un uso establecido y no un reposicionamiento clásico.

Hay limitaciones: el efecto completo requiere cierta función residual del receptor de LDL, y muchos pacientes necesitan terapia adicional (ezetimiba, inhibidores de PCSK9, ácido bempedoico).

---

## Evidencia de Ensayos Clínicos

Se muestran los 10 ensayos más relevantes (de 14 identificados).

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00134485](https://clinicaltrials.gov/study/NCT00134485) | Fase 3 | Completado | 400 | Torcetrapib/atorvastatina vs. atorvastatina sola en hipercolesterolemia familiar heterocigota; el proyecto de torcetrapib se terminó por hallazgos de seguridad |
| [NCT00827606](https://clinicaltrials.gov/study/NCT00827606) | Fase 3 | Completado | 272 | Estudio abierto de 3 años de atorvastatina en niños y adolescentes con hipercolesterolemia familiar heterocigota: crecimiento, desarrollo y reducción del colesterol |
| [NCT00134511](https://clinicaltrials.gov/study/NCT00134511) | Fase 3 | Completado | 30 | Torcetrapib/atorvastatina en hipercolesterolemia familiar homocigota (abierto, sin control) |
| [NCT00136981](https://clinicaltrials.gov/study/NCT00136981) | Fase 3 | Completado | 800 | Ecografía carotídea a 24 meses: torcetrapib/atorvastatina vs. atorvastatina sola en hipercolesterolemia familiar heterocigota |
| [NCT01709500](https://clinicaltrials.gov/study/NCT01709500) | Fase 3 | Completado | 249 | Alirocumab vs. placebo en hipercolesterolemia familiar heterocigota no controlada con su terapia hipolipemiante |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Fase 3 | Completado | 50 | Ezetimiba 10 mg añadida a atorvastatina o simvastatina en hipercolesterolemia familiar homocigota |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Fase 3 | Completado | 44 | Extensión abierta de seguridad a largo plazo de ezetimiba con atorvastatina o simvastatina |
| [NCT03510884](https://clinicaltrials.gov/study/NCT03510884) | Fase 3 | Completado | 153 | Alirocumab vs. placebo en niños y adolescentes con hipercolesterolemia familiar heterocigota, con tratamiento de base con estatinas |
| [NCT00739999](https://clinicaltrials.gov/study/NCT00739999) | Fase 1 | Completado | 39 | Farmacocinética, farmacodinamia y seguridad de atorvastatina en niños y adolescentes con hipercolesterolemia familiar heterocigota |
| [NCT01279590](https://clinicaltrials.gov/study/NCT01279590) | Fase 2 | Completado | 282 | PPD10558 vs. atorvastatina sobre la incidencia de mialgia asociada a estatinas en pacientes intolerantes |

---

## Evidencia de Literatura

Se muestran las publicaciones más relevantes, priorizando ensayos y revisiones sistemáticas.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [25760954](https://pubmed.ncbi.nlm.nih.gov/25760954/) | 2015 | Revisión (Cochrane) | Cochrane Database Syst Rev | Magnitud del efecto dosis-respuesta de atorvastatina sobre los lípidos sanguíneos |
| [27678432](https://pubmed.ncbi.nlm.nih.gov/27678432/) | 2016 | Estudio clínico | J Clin Lipidol | Estudio de 3 años de atorvastatina en niños y adolescentes con hipercolesterolemia familiar heterocigota |
| [11383320](https://pubmed.ncbi.nlm.nih.gov/11383320/) | 2001 | Estudio comparativo | Nutr Metab Cardiovasc Dis | Atorvastatina vs. simvastatina para alcanzar la meta de LDL-C en hipercolesterolemia familiar heterocigota |
| [9301631](https://pubmed.ncbi.nlm.nih.gov/9301631/) | 1997 | Estudio abierto | Arterioscler Thromb Vasc Biol | Eficacia y seguridad de atorvastatina 80 mg en hipercolesterolemia familiar comprobada |
| [12883464](https://pubmed.ncbi.nlm.nih.gov/12883464/) | 2003 | Estudio clínico | Med Sci Monit | Atorvastatina reduce la microalbuminuria en hipercolesterolemia familiar |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guía | Endocr Pract | Guías AACE/ACE para el manejo de dislipidemia y prevención cardiovascular |
| [28623954](https://pubmed.ncbi.nlm.nih.gov/28623954/) | 2017 | ECA (diseño) | Lipids Health Dis | Diseño del estudio ODYSSEY NIPPON de alirocumab en hipercolesterolemia no controlada |
| [9793596](https://pubmed.ncbi.nlm.nih.gov/9793596/) | 1998 | Revisión | Ann Pharmacother | Eficacia y seguridad de atorvastatina en dislipidemias |
| [15199433](https://pubmed.ncbi.nlm.nih.gov/15199433/) | 2004 | Revisión | Semin Vasc Med | Aspectos diagnósticos y terapéuticos de la hipercolesterolemia familiar en niños |
| [40254247](https://pubmed.ncbi.nlm.nih.gov/40254247/) | 2025 | Preclínico | Toxicology | Miotoxicidad de estatinas lipofílicas e hidrofílicas en células musculares derivadas de pacientes con hipercolesterolemia familiar |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19950621 (cancelado) | Atorvastatina 20 mg comprimidos con cubierta pelicular (Sandoz GmbH) | Tableta cubierta con película | ATORVASTATIN |
| 20150389 (cancelado) | Isulor® 20 mg tabletas recubiertas (Mediseg Laboratories S.A.S.) | Tableta recubierta | ATORVASTATIN |

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas por el grafo de conocimiento del modelo** (no provienen del prospecto): insuficiencia hepática, enfermedad hepática, enfermedad renal, enfermedad de la vesícula biliar, hipotiroidismo (incluido mixedema e hipotiroidismo congénito), miopatía y enfermedades musculares, rabdomiólisis, parálisis periódica familiar, trastornos hipotensivos y abuso o dependencia de sustancias.
- **Interacciones farmacológicas**: los datos registran únicamente la interacción con su blanco farmacológico, la HMG-CoA reductasa (HMGCR). Para el uso en pacientes con VIH, la literatura advierte interacciones relevantes con inhibidores de proteasa y cobicistat (vía CYP3A4).

Consultar el prospecto para las advertencias y contraindicaciones oficiales.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen varios ensayos de Fase 3 completados en hipercolesterolemia familiar, incluidos estudios con atorvastatina en población pediátrica y estudios controlados con atorvastatina como comparador o base. Sin embargo, en muchos de ellos la atorvastatina es terapia de fondo, y no hay registros sanitarios vigentes en Colombia.

**Para avanzar se necesita:**
- Verificar la situación regulatoria: ambos registros están cancelados, por lo que habría que evaluar una nueva solicitud o reactivación ante INVIMA.
- Obtener y revisar el prospecto de INVIMA para advertencias y contraindicaciones oficiales.
- Documentar el mecanismo de acción en fuentes como DrugBank.
- Definir un plan de monitoreo hepático y muscular, y de interacciones (especialmente CYP3A4).
- Confirmar si esta indicación se considera uso establecido y no reposicionamiento.

---

### Otras Indicaciones Predichas (referencia)

| Indicación | Puntaje TxGNN | Nivel de Evidencia | Recomendación |
|------|------|------|------|
| Infección por VIH | 99.31% | L2 | Research Question |
| Infarto del tronco encefálico | 99.31% | L4 | Hold |
| Deficiencia de proteína de transferencia de ésteres de colesterol | 99.25% | L4 | Hold |
| Hipercolesterolemia por deficiencia de colesterol 7α-hidroxilasa | 99.20% | L5 | Hold |
| Trastorno del neurodesarrollo con marcha atáxica, ausencia del habla y reducción de sustancia blanca cortical | 99.13% | L5 | Hold |
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

