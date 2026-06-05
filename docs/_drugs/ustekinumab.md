---
layout: default
title: Ustekinumab
parent: 僅模型預測 (L5)
nav_order: 233
evidence_level: L5
indication_count: 10
---

# Ustekinumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Ustekinumab: De Psoriasis y Enfermedad de Crohn a Dermatitis

## Resumen en Una Frase

Ustekinumab (Stelara®) es un anticuerpo monoclonal humano anti-IL-12/IL-23, aprobado internacionalmente para el tratamiento de psoriasis en placas moderada-grave, artritis psoriásica, enfermedad de Crohn y colitis ulcerosa.
El modelo TxGNN predice que podría ser efectivo para **Dermatitis** (especialmente dermatitis atópica),
con **7 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Psoriasis en placas moderada-grave, artritis psoriásica, enfermedad de Crohn, colitis ulcerosa (aprobaciones internacionales; sin registro en Colombia) |
| Nueva Indicación Predicha | Dermatitis (Dermatitis Atópica) |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## Por qué es Razonable esta Predicción?

Ustekinumab es un anticuerpo monoclonal IgG1 humano que bloquea la subunidad p40 compartida por las interleucinas IL-12 e IL-23, dos citocinas clave en la regulación de la respuesta inmune Th1 y Th17. Sus indicaciones aprobadas internacionalmente —psoriasis, artritis psoriásica, enfermedad de Crohn y colitis ulcerosa— comparten como denominador común la hiperactivación de estas vías inflamatorias, lo que confirma un perfil farmacológico orientado a la modulación de la inmunidad adaptativa mediada por linfocitos T.

La dermatitis atópica (DA) se clasifica clásicamente como una enfermedad de predominio Th2, pero estudios de transcriptómica cutánea han demostrado que la forma crónica y la presentación en pacientes adultos y de origen asiático también exhiben activación significativa de los ejes Th1 y Th17. El bloqueo de p40 por ustekinumab puede modular este componente inflamatorio mixto, ofreciendo una base mecanística plausible para su uso en DA. Esta hipótesis ha sido directamente investigada en ensayos clínicos Fase 2, doble ciego, controlados con placebo en pacientes con DA moderada-grave, tanto en población occidental como japonesa.

La similitud inmunológica entre la psoriasis —indicación plenamente aprobada— y determinadas formas de DA refuerza la coherencia de la predicción del modelo TxGNN: ambas enfermedades comparten disfunción de la barrera cutánea, infiltración de células T activadas y señalización anómala de citocinas. Los datos robustos de seguridad acumulados en psoriasis y artritis psoriásica sirven además como plataforma de referencia para estimar el perfil de riesgo en esta extensión de indicación.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01806662](https://clinicaltrials.gov/study/NCT01806662) | Fase 2 | Completado | 32 | Estudio piloto aleatorizado de ustekinumab en adultos con DA crónica con respuesta subóptima a terapia previa; evaluó eficacia directa en el target de indicación |
| [NCT01945086](https://clinicaltrials.gov/study/NCT01945086) | Fase 2 | Completado | 79 | Estudio multicéntrico, aleatorizado, doble ciego, controlado con placebo en pacientes japoneses adultos con DA grave; comparó 2 dosis de ustekinumab vs. placebo |
| [NCT07041112](https://clinicaltrials.gov/study/NCT07041112) | N/A | Completado | 1000 | Estudio observacional retrospectivo farmacogenético sobre supervivencia a 10 años de terapias biológicas en psoriasis moderada-grave; evalúa influencia de variantes genéticas y factores cardiometabólicos en durabilidad del tratamiento |
| [NCT05535738](https://clinicaltrials.gov/study/NCT05535738) | Fase 2/3 | En curso | 45 | Estudio de inflamación cutánea mediante modelo de dermatitis por contacto con ampollas de succión; evalúa múltiples biológicos incluyendo ustekinumab para caracterizar mecanismos de acción en piel |
| [NCT07352566](https://clinicaltrials.gov/study/NCT07352566) | Fase 4 | No iniciado | 10 | Estudio de microdispositivo cutáneo in situ para probar medicamentos aprobados por FDA directamente sobre DA y psoriasis; muestra muy reducida, relevancia limitada |
| [NCT01356758](https://clinicaltrials.gov/study/NCT01356758) | N/A | Completado | 126 | Evaluación de riesgo cardiovascular en pacientes con psoriasis grave bajo agentes biológicos; provee contexto de seguridad sistémica a largo plazo para la clase farmacológica |
| [NCT02074982](https://clinicaltrials.gov/study/NCT02074982) | Fase 3 | Completado | 676 | Estudio CLEAR: secukinumab (anti-IL-17A) vs. ustekinumab en psoriasis en placas moderada-grave; ustekinumab actuó como comparador activo, confirmando su eficacia establecida en enfermedades inflamatorias cutáneas |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [27304428](https://pubmed.ncbi.nlm.nih.gov/27304428/) | 2017 | ECA | Experimental Dermatology | Fase 2 RDBPC en 33 pacientes con DA moderada-grave; evaluó eficacia y seguridad de ustekinumab vs. placebo; evidencia directa sobre el target de indicación |
| [28338223](https://pubmed.ncbi.nlm.nih.gov/28338223/) | 2017 | ECA | British Journal of Dermatology | ECA Fase 2 en pacientes japoneses con DA grave; evaluó ustekinumab anti-IL-12/23 como potencial tratamiento, con datos de eficacia y seguridad |
| [33074565](https://pubmed.ncbi.nlm.nih.gov/33074565/) | 2021 | Revisión Sistemática + Metaanálisis | Allergy | Evaluación crítica de evidencia para tratamientos sistémicos (incluyendo ustekinumab) en DA moderada-grave; base para guías clínicas EAACI |
| [29164954](https://pubmed.ncbi.nlm.nih.gov/29164954/) | 2018 | Revisión Sistemática | Journal of Dermatological Treatment | Revisión sistemática de eficacia y seguridad de ustekinumab específicamente en el tratamiento de DA; síntesis de evidencia disponible |
| [33849369](https://pubmed.ncbi.nlm.nih.gov/33849369/) | 2022 | Cohorte de Vida Real | Journal of Dermatological Treatment | Análisis de evidencia del mundo real sobre efectividad de ustekinumab en pacientes con DA; complementa datos de ensayos controlados |
| [27745907](https://pubmed.ncbi.nlm.nih.gov/27745907/) | 2017 | Estudio Mecanístico | Journal of the American Academy of Dermatology | Ustekinumab en DA grave: demuestra regulación a la baja de expresión Th2/Th22; sustento molecular para la hipótesis mecanística |
| [36208443](https://pubmed.ncbi.nlm.nih.gov/36208443/) | 2022 | Revisión Narrativa | Dermatologic Therapy | Síntesis de usos fuera de etiqueta de ustekinumab incluyendo DA; revisión de ensayos clínicos y estudios observacionales disponibles |
| [39987634](https://pubmed.ncbi.nlm.nih.gov/39987634/) | 2025 | Análisis de Seguridad en Vida Real | International Immunopharmacology | Evaluación de eventos adversos de ustekinumab en psoriasis y artritis psoriásica mediante base de datos FDA FAERS; perfil de seguridad actualizado |
| [39201826](https://pubmed.ncbi.nlm.nih.gov/39201826/) | 2024 | Revisión | Children (Basel) | Revisión narrativa de biológicos y terapias dirigidas para DA pediátrica, psoriasis, alopecia areata e hidradenitis supurativa en EE.UU. |
| [38847375](https://pubmed.ncbi.nlm.nih.gov/38847375/) | 2024 | Revisión Sistemática | Journal of Cutaneous Medicine and Surgery | Respuesta a terapia biológica en participantes con piel de color con psoriasis y DA moderada-grave; datos de generalización étnica relevantes para Colombia |

---

## Información de Mercado en Colombia

Ustekinumab no cuenta con registros sanitarios activos ante el INVIMA. No se dispone de licencias locales que listar. El acceso en Colombia requeriría importación por excepción o gestión de uso bajo protocolo específico.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Dos ensayos clínicos de Fase 2 completados (NCT01806662 y NCT01945086) han evaluado directamente ustekinumab en DA moderada-grave, respaldados por revisiones sistemáticas y datos de vida real que confirman actividad clínica; sin embargo, los resultados han sido mixtos y el fármaco carece de aprobación regulatoria para esta indicación, lo que exige diseño cuidadoso, monitoreo activo de seguridad y una estrategia de acceso local bien definida.

**Para avanzar se necesita:**
- Datos completos de mecanismo de acción (MOA) obtenidos desde DrugBank API (DG002 pendiente)
- Advertencias, contraindicaciones e interacciones del prospecto oficial de TFDA/FDA (DG001 pendiente — clasificado como **Blocking**)
- Estrategia de acceso regulatorio en Colombia: ustekinumab no está registrado localmente; evaluar vía de importación por excepción o uso compasivo ante INVIMA
- Identificación del subgrupo respondedor óptimo: pacientes con DA crónica, fenotipo Th1/Th17 elevado o de origen asiático, donde el beneficio mecanístico es mayor
- Seguimiento del estudio en curso NCT05535738 (Fase 2/3) para datos mecanísticos adicionales en piel inflamada
- Comparación con alternativas disponibles (dupilumab, tralokinumab) en términos de eficacia, seguridad y acceso para contextualizar la viabilidad de reposicionamiento en el mercado colombiano
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

