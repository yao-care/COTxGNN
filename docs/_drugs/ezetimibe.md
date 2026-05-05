---
layout: default
title: Ezetimibe
parent: 僅模型預測 (L5)
nav_order: 77
evidence_level: L5
indication_count: 4
---

# Ezetimibe
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Ezetimibe: De Hipercolesterolemia a Hiperlipoproteinemia

## Resumen en Una Frase

Ezetimibe es un inhibidor selectivo de la absorción intestinal de colesterol, utilizado internacionalmente para el tratamiento de la hipercolesterolemia primaria y las hiperlipidemias mixtas, aunque actualmente no cuenta con registro sanitario en Colombia.
El modelo TxGNN predice que podría ser efectivo para **Hiperlipoproteinemia**,
con **50 ensayos clínicos** y **19 publicaciones** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sin registro aprobado en Colombia (uso internacional establecido: hipercolesterolemia) |
| Nueva Indicación Predicha | Hiperlipoproteinemia |
| Puntaje de Predicción TxGNN | 99.63% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción a partir de las fuentes consultadas en este Evidence Pack. Sin embargo, según la literatura científica disponible, Ezetimibe actúa mediante la inhibición selectiva de la proteína NPC1L1 (Niemann-Pick C1-Like 1) en el borde en cepillo del intestino delgado, bloqueando la reabsorción de colesterol dietético y biliar. Esta acción reduce el transporte de colesterol exógeno hacia la circulación portal, disminuyendo los niveles de LDL-C aproximadamente un 15–20% en monoterapia, o un 15–25% adicional cuando se combina con estatinas.

La hiperlipoproteinemia engloba un espectro de trastornos del metabolismo lipídico caracterizados por niveles elevados de lipoproteínas en plasma, incluyendo LDL-colesterol y/o triglicéridos. Dado que el mecanismo central de Ezetimibe actúa directamente sobre la patología de fondo de estas condiciones —la absorción excesiva de colesterol externo—, la predicción del modelo TxGNN es mecanísticamente coherente y esperada. La eficacia en hiperlipidemia mixta ha sido demostrada en múltiples ensayos clínicos de Fase 3, particularmente en combinación con fenofibrato o estatinas.

La fortaleza de la predicción (99.63%) refleja la solidez de la evidencia disponible: Ezetimibe ha sido evaluado en ensayos pivotales de Fase 3 directamente en poblaciones con hiperlipoproteinemia, y actúa como comparador de referencia estándar en estudios de nuevas terapias hipolipemiantes (inhibidores de PCSK9, obicetrapib, inclisiran), consolidando su posición como tratamiento de base en este espectro de enfermedad. La ausencia de registro en Colombia representa la principal brecha, no la falta de evidencia clínica.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01763827](https://clinicaltrials.gov/study/NCT01763827) | Fase 3 | Completado | 615 | Evolocumab vs placebo y ezetimibe en adultos con riesgo Framingham ≤10%; ezetimibe como comparador activo de referencia para cambio porcentual en LDL-C |
| [NCT01043380](https://clinicaltrials.gov/study/NCT01043380) | Fase 4 | Completado | 245 | PRECISE-IVUS: Inhibidor de absorción de colesterol (ezetimibe) vs inhibidor de síntesis (estatina) en regresión de placa coronaria medida por ultrasonido intravascular |
| [NCT00093899](https://clinicaltrials.gov/study/NCT00093899) | Fase 3 | Completado | 611 | Eficacia y seguridad de Ezetimibe/Simvastatina más fenofibrato en hiperlipidemia mixta (colesterol elevado + triglicéridos elevados) |
| [NCT06005597](https://clinicaltrials.gov/study/NCT06005597) | Fase 3 | Completado | 407 | Combinación fija de obicetrapib 10 mg + ezetimibe 10 mg en HeFH y/o ASCVD; confirma ezetimibe como componente de base del tratamiento |
| [NCT00092560](https://clinicaltrials.gov/study/NCT00092560) | Fase 3 | Completado | 587 | Eficacia y seguridad de la coadministración de fenofibrato y ezetimibe en hiperlipidemia mixta |
| [NCT00092573](https://clinicaltrials.gov/study/NCT00092573) | Fase 3 | Completado | 576 | Evaluación adicional de la coadministración de fenofibrato y ezetimibe en hiperlipidemia mixta |
| [NCT05611528](https://clinicaltrials.gov/study/NCT05611528) | Fase 3 | Completado | 10 | Evinacumab en HoFH en contexto de vida real en Canadá; ezetimibe figura como terapia de fondo estándar |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Fase 3 | Completado | 50 | Eficacia y seguridad de ezetimibe (SCH58235) 10 mg combinado con atorvastatina o simvastatina en hipercolesterolemia familiar homocigota |
| [NCT03434613](https://clinicaltrials.gov/study/NCT03434613) | Fase 4 | Completado | 64 | Rosuvastatina 5 mg en monoterapia vs rosuvastatina 5 mg/ezetimibe 10 mg en pacientes con hiperlipidemia y enfermedad hepática grasa no alcohólica |
| [NCT04433533](https://clinicaltrials.gov/study/NCT04433533) | Fase 4 | Desconocido | 200 | Rosuvastatina/ezetimibe vs rosuvastatina en monoterapia en pacientes coreanos con disfunción diastólica del ventrículo izquierdo e hiperlipidemia |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [40347969](https://pubmed.ncbi.nlm.nih.gov/40347969/) | 2025 | ECA Fase 3 | Lancet | Ensayo TANDEM: Combinación fija de obicetrapib y ezetimibe reduce significativamente el LDL-C en pacientes con HeFH y ASCVD; demuestra el valor complementario de ezetimibe |
| [41206969](https://pubmed.ncbi.nlm.nih.gov/41206969/) | 2026 | ECA | JAMA | Inhibidor oral de PCSK9 (enlicitide) en HeFH; ezetimibe como comparador de referencia de segunda línea en pacientes que no alcanzan metas con terapia disponible |
| [40682836](https://pubmed.ncbi.nlm.nih.gov/40682836/) | 2025 | Revisión | Mol Med Reports | Revisión de fármacos actuales para hiperlipidemia; ezetimibe descrito como inhibidor de NPC1L1 con eficacia establecida para reducir LDL-C y prevenir ASCVD |
| [37762244](https://pubmed.ncbi.nlm.nih.gov/37762244/) | 2023 | Revisión | Int J Mol Sci | Hiperlipidemia posprandial: fisiopatología, aterogénesis y tratamientos; papel de la absorción intestinal de lípidos como diana terapéutica |
| [35593194](https://pubmed.ncbi.nlm.nih.gov/35593194/) | 2022 | Revisión | J Cardiovasc Pharmacol Ther | Revisión comprehensiva de inhibidores de PCSK9; ezetimibe posicionado como tratamiento estándar de base en pacientes intolerantes a estatinas o con LDL-C no controlado |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Revisión | JACC | Nuevas terapias emergentes para reducción de LDL-C y ApoB; ezetimibe forma parte de la base terapéutica establecida junto con estatinas e inhibidores de PCSK9 |
| [34480646](https://pubmed.ncbi.nlm.nih.gov/34480646/) | 2021 | Revisión | Curr Cardiol Rep | Hipercolesterolemia familiar: carga global y enfoques; ezetimibe citado como pilar del tratamiento en combinación con estatinas |
| [23956253](https://pubmed.ncbi.nlm.nih.gov/23956253/) | 2013 | Consenso | Eur Heart J | Declaración de consenso de la Sociedad Europea de Aterosclerosis: FH subdiagnosticada y subtratada; ezetimibe recomendado como tratamiento de segunda línea |
| [18376001](https://pubmed.ncbi.nlm.nih.gov/18376001/) | 2008 | Editorial | N Engl J Med | Reducción del colesterol y ezetimibe: análisis de eficacia clínica y debate sobre relevancia de los resultados del ensayo ENHANCE |
| [19654419](https://pubmed.ncbi.nlm.nih.gov/19654419/) | 2009 | Revisión | Drug Ther Bull | Actualización sobre ezetimibe: eficacia demostrada como monoterapia y en combinación con estatinas para reducción de LDL-C y colesterol total |

---

## Información de Mercado en Colombia

Según los datos disponibles en este Evidence Pack, **Ezetimibe no cuenta con registros sanitarios INVIMA activos en Colombia** (0 licencias registradas). No existen productos aprobados para listar.

Este hallazgo es relevante desde la perspectiva de reposicionamiento: a pesar de la ausencia de registro local, el fármaco cuenta con amplio reconocimiento internacional y es componente estándar en guías clínicas globales para el manejo de hiperlipoproteinemia. La obtención del registro sanitario ante INVIMA es el principal paso regulatorio requerido.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Múltiples ensayos clínicos de Fase 3 completados respaldan la eficacia de Ezetimibe en hiperlipoproteinemia, y el fármaco actúa como comparador estándar de referencia en los principales estudios internacionales de nuevas terapias hipolipemiantes. La predicción TxGNN (99.63%) y el nivel de evidencia L1 reflejan una base clínica robusta; la principal restricción no es la evidencia clínica sino la ausencia de registro sanitario en Colombia.

**Para avanzar se necesita:**
- Iniciar proceso de registro ante INVIMA con el expediente de aprobaciones internacionales disponibles (FDA, EMA, entre otras)
- Obtener y analizar el prospecto oficial (o equivalente internacional) para extraer advertencias clave, contraindicaciones e interacciones farmacológicas relevantes
- Completar los datos de mecanismo de acción (MOA) desde DrugBank para el análisis mecanístico formal
- Evaluar el perfil de interacciones farmacológicas (DDI) en el contexto clínico colombiano, especialmente con estatinas, fibratos, ciclosporina y anticoagulantes
- Identificar el acceso a fabricantes o distribuidores autorizados para la comercialización local
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

