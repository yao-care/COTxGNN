---
layout: default
title: Trastuzumab
parent: 僅模型預測 (L5)
nav_order: 228
evidence_level: L5
indication_count: 10
---

# Trastuzumab
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

# Trastuzumab: De Cáncer de Mama HER2-Positivo a Carcinoma de Mama Subtipo Normal Breast-Like

## Resumen en Una Frase

Trastuzumab es un anticuerpo monoclonal humanizado dirigido contra el receptor HER2 (ErbB2), reconocido mundialmente como terapia estándar para el cáncer de mama y gástrico HER2-positivo.
El modelo TxGNN predice que podría ser efectivo para el **Subtipo Normal Breast-Like del Carcinoma de Mama**,
con **12 ensayos clínicos** y **1 publicación** que actualmente respaldan esta dirección de investigación.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer de mama y gástrico HER2-positivo (indicación global; sin registro activo en Colombia) |
| Nueva Indicación Predicha | Subtipo Normal Breast-Like del Carcinoma de Mama |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | ✗ No Comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Trastuzumab es un anticuerpo monoclonal humanizado de tipo IgG1 que se une con alta afinidad al dominio extracelular IV del receptor HER2. Su mecanismo de acción comprende el bloqueo de la homodimerización y heterodimerización del receptor, la inhibición de la vía de señalización PI3K/Akt, la inducción de citotoxicidad celular dependiente de anticuerpos (ADCC) y la modulación del crecimiento tumoral. Aunque los datos formales de mecanismo de acción del DrugBank no estuvieron disponibles en este análisis, el mecanismo de Trastuzumab está ampliamente documentado en la literatura oncológica internacional. Su eficacia en cáncer de mama HER2-positivo ha transformado el pronóstico de este subtipo durante las últimas tres décadas.

El subtipo Normal Breast-Like (clasificación PAM50) se caracteriza por un perfil de expresión génica que se asemeja al tejido mamario normal y adiposo, con baja actividad proliferativa y marcadores luminales tenues. De manera crítica, este subtipo presenta una tasa de amplificación de HER2 inferior al 5%, lo que representa una desconexión biológica fundamental con el mecanismo de acción de Trastuzumab. Los ensayos clínicos identificados corresponden mayoritariamente a estudios en cáncer de mama HER2-positivo que incluyen análisis de subtipos moleculares, pero no están diseñados específicamente para el subtipo normal breast-like.

La predicción de TxGNN con puntuación alta (99.90%) probablemente refleja la proximidad en el espacio de características del grafo de conocimiento entre el subtipo normal breast-like y otros subtipos de carcinoma mamario donde Trastuzumab tiene eficacia demostrada. La racionalidad mecanística es débil: únicamente en los casos excepcionales en que este subtipo coexiste con amplificación HER2 confirmada (IHC 3+ o FISH+) existiría justificación biológica para considerar Trastuzumab.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04759248](https://clinicaltrials.gov/study/NCT04759248) | Fase 2 | Activo, sin reclutamiento | 55 | Estudio ATREZZO: Atezolizumab + Trastuzumab + Vinorelbina en HER2+ avanzado con ER negativo o PAM50 No-luminal; es el ensayo más directamente relevante para el subtipo normal-like por su selección explícita de enfermedad no-luminal |
| [NCT03168880](https://clinicaltrials.gov/study/NCT03168880) | Fase 3 | Activo, sin reclutamiento | 720 | ECA fase 3 de Paclitaxel ± Carboplatino neoadyuvante en cáncer de mama triple negativo; incluye caracterización de subtipos moleculares y proporciona contexto de fondo para el subtipo basal-like/normal-like |
| [NCT01796197](https://clinicaltrials.gov/study/NCT01796197) | Fase 2 | Completado | 23 | Trastuzumab + Pertuzumab + Paclitaxel preoperatorio en cáncer de mama inflamatorio HER2+; incluye análisis de subtipos moleculares PAM50 que permite inferencia sobre subgrupo normal-like |
| [NCT04329065](https://clinicaltrials.gov/study/NCT04329065) | Fase 2 | Reclutando | 25 | Vacuna WOKVAC + quimioterapia neoadyuvante + terapia anti-HER2; investiga respuesta inmune combinada; no estratifica por subtipo molecular |
| [NCT04750122](https://clinicaltrials.gov/study/NCT04750122) | Fases 1/2 | Reclutando | 46 | Organoides derivados de tumor para guiar tratamiento neoadyuvante HER2+; ~60% de tasa de respuesta completa patológica con doble bloqueo anti-HER2; enfoque metodológico sin especificidad de subtipo |
| [NCT06328387](https://clinicaltrials.gov/study/NCT06328387) | Fases 1/2 | Desconocido | 120 | Hidroxicloroquina + conjugado anticuerpo-fármaco (T-DXd o SG) en cáncer de mama avanzado; explora autophagia como mecanismo de resistencia |
| [NCT05900206](https://clinicaltrials.gov/study/NCT05900206) | Fase 2 | Reclutando | 370 | Estudio ARIADNE: T-DXd vs tratamiento estándar neoadyuvante en HER2+ no metastásico; diseño impulsado por biomarcadores biológicos |
| [NCT01670877](https://clinicaltrials.gov/study/NCT01670877) | Fase 2 | Completado | 56 | Neratinib en HER2 mutado no amplificado; evalúa la pregunta inversa al subtipo de interés; proporciona referencia sobre actividad HER2 sin amplificación |
| [NCT06348134](https://clinicaltrials.gov/study/NCT06348134) | Fase 2 | Reclutando | 74 | Optimización de tratamiento anti-HER2 neoadyuvante y adyuvante en mujeres nigerianas con HER2+; sin estratificación por subtipo molecular |
| [NCT05582499](https://clinicaltrials.gov/study/NCT05582499) | Fase 2 | Reclutando | 716 | FASCINATE-N: Plataforma de investigación prospectiva de terapia neoadyuvante de precisión basada en subtipos clínicos; explora refinamiento de clasificación molecular y nuevos blancos terapéuticos |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [19466513](https://pubmed.ncbi.nlm.nih.gov/19466513/) | 2009 | Morfológico/Observacional | Breast Cancer (Tokyo, Japan) | Caracterización citológica e histológica del subtipo basal-like; describe los 5 subtipos PAM50 del carcinoma mamario (luminal A, luminal B, normal breast-like, sobreexpresión de HER2 y basal-like) y su asociación con diferentes esquemas de quimioterapia y pronóstico clínico |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida — anticuerpo monoclonal anti-HER2 (IgG1 humanizado); no es un agente citotóxico convencional |
| Riesgo de Mielosupresión | Bajo en monoterapia; puede incrementarse significativamente al combinarse con quimioterapia citotóxica (especialmente taxanos y antraciclinas) |
| Clasificación de Emetogenicidad | Mínima a baja |
| Ítems de Monitoreo | Fracción de eyección ventricular izquierda (FEVI) basal y cada 3 meses durante el tratamiento; reacciones a la infusión (fiebre, escalofríos, hipotensión); función pulmonar; hemograma diferencial al combinarse con quimioterapia |
| Protección en Manejo | Como medicamento biológico, no requiere las precauciones de manipulación de citotóxicos convencionales; seguir protocolos institucionales para preparación y administración de anticuerpos monoclonales |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El subtipo Normal Breast-Like del carcinoma de mama presenta una tasa de amplificación HER2 inferior al 5%, lo que debilita de forma fundamental la conexión mecanística con Trastuzumab. La evidencia clínica disponible (nivel L3) proviene de estudios en cáncer de mama HER2-positivo que no estratifican específicamente por este subtipo, y la única publicación identificada es un estudio observacional sobre caracterización morfológica. La alta puntuación de TxGNN refleja probable proximidad en el grafo de conocimiento, no una relación terapéutica establecida.

**Para avanzar se necesita:**
- Estudios traslacionales que caractericen la frecuencia real de HER2 3+ (IHC o FISH+) dentro de tumores clasificados como Normal Breast-Like por PAM50
- Análisis de subgrupos en estudios existentes con clasificación PAM50 que reporten la respuesta a Trastuzumab en pacientes normal breast-like con HER2 amplificado
- Datos formales de MOA y ficha técnica actualizada (DrugBank)
- Definición de criterios de selección de pacientes: la amplificación HER2 confirmada es condición necesaria antes de cualquier uso en este subtipo
- Obtención de registro sanitario ante el INVIMA previo a cualquier uso en Colombia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

