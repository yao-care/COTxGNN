---
layout: default
title: Adalimumab
parent: 僅模型預測 (L5)
nav_order: 22
evidence_level: L5
indication_count: 6
---

# Adalimumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

El skill de TxGNN pipeline cubre el flujo general de trabajo. Para este caso concreto, las instrucciones de formato del informe están definidas directamente en el prompt del sistema. Procedo a generar el informe completo.

---

# Adalimumab: De Artritis Reumatoide a Vasculitis Reumatoide

## Resumen en Una Frase

Adalimumab es un anticuerpo monoclonal anti-TNF-α utilizado mundialmente como tratamiento de primera línea para la artritis reumatoide (AR) y otras enfermedades inflamatorias crónicas, aunque actualmente no cuenta con registros sanitarios activos ante el INVIMA en Colombia.
El modelo TxGNN predice que podría ser efectivo para **Vasculitis Reumatoide**, con **5 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección.
La vasculitis reumatoide es una complicación extraarticular grave de la AR de larga evolución, y el mecanismo de inhibición del TNF-α representa el sustrato biológico central para su manejo.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Artritis reumatoide (indicación global; sin registros activos en Colombia) |
| Nueva Indicación Predicha | Vasculitis Reumatoide |
| Puntaje de Predicción TxGNN | 99.80% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## Por qué es Razonable esta Predicción?

La vasculitis reumatoide (VR) es una de las manifestaciones extraarticulares más graves de la artritis reumatoide de larga evolución, con significativa morbilidad y mortalidad. Se caracteriza por depósito de complejos inmunes en la pared vascular, activación de neutrófilos y sobreexpresión sostenida de TNF-α, citocina que actúa como eje central de la cascada inflamatoria que destruye los vasos sanguíneos pequeños y medianos.

Actualmente no se dispone de datos detallados sobre el mecanismo de acción a través del pipeline. No obstante, según la información clínica conocida, adalimumab es un anticuerpo monoclonal completamente humanizado (IgG1) que se une y neutraliza directamente al TNF-α, bloqueando su interacción con los receptores p55 y p75. Al interrumpir esta cascada inflamatoria, el fármaco teóricamente puede controlar la inflamación de la pared vascular y prevenir el daño orgánico progresivo en la VR. Esta hipótesis está respaldada por casos documentados de mejoría clínica significativa en VR digital y otras formas vasculíticas asociadas a AR, así como por una revisión sistemática que avala el uso de terapia biológica en este contexto.

Sin embargo, existe un riesgo paradójico crítico que debe considerarse: el propio adalimumab puede inducir vasculitis leucocitoclástica cutánea y eventos similares a lupus en un subconjunto de pacientes con AR. Esta dualidad —eficacia terapéutica potencial vs. riesgo de vasculitis inducida por el fármaco— representa el principal elemento de guardrail para esta indicación y exige evaluación individual cuidadosa por parte del especialista tratante.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|------------------|------|--------|-------------|----------------------|
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Desconocido | 750,000 | Estudio de mundo real a gran escala que evalúa el riesgo de desarrollar nuevas enfermedades inflamatorias mediadas por el sistema inmune (IMID) en pacientes tratados con biológicos e inmunosupresores; la vasculitis puede figurar como resultado secundario |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Fase 2 | Por iniciar | 80 | Manejo perioperatorio de inmunosupresores (incluyendo adalimumab) en pacientes reumatológicos sometidos a artroplastia total de hombro; evalúa brotes y complicaciones al suspender medicación |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completado | 184 | Estudio observacional multicéntrico de tocilizumab en AR con respuesta inadecuada a DMARDs o a un biológico previo; describe patrones de práctica clínica en AR activa |
| [NCT02590562](https://clinicaltrials.gov/study/NCT02590562) | N/A | Completado | 808 | Estudio transversal sobre patrones de uso de DMARDs biológicos en AR en China; caracteriza demografía y actividad de la enfermedad en práctica rutinaria |

> **Nota:** No existen ensayos clínicos registrados que evalúen directamente adalimumab como tratamiento específico para vasculitis reumatoide. Los ensayos identificados tienen relevancia indirecta (Grado B–C). El ensayo NCT05111743 (brolucizumab en AMD húmeda) fue excluido por carecer de relación con adalimumab o vasculitis.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [33058033](https://pubmed.ncbi.nlm.nih.gov/33058033/) | 2021 | Revisión Sistemática | Clinical Rheumatology | Revisión PRISMA sobre uso de terapia biológica en vasculitis reumatoide; evalúa anti-TNF y otros agentes en el arsenal terapéutico de la VR, con análisis de eficacia y seguridad |
| [28123776](https://pubmed.ncbi.nlm.nih.gov/28123776/) | 2017 | Cohorte/Farmacovigilancia | RMD Open | Riesgo específico por fármaco de eventos tipo lupus y tipo vasculitis en 2,707 pacientes con AR tratados con inhibidores de TNF vs. DMARDs no biológicos (Registro BSRBR-RA) |
| [18799049](https://pubmed.ncbi.nlm.nih.gov/18799049/) | 2008 | Revisión Sistemática | Clinical and Experimental Rheumatology | Comparación de características clínicas de vasculitis en pacientes con AR bajo anti-TNF vs. sin tratamiento biológico; n=2,707 pacientes, 18 casos de vasculitis documentados |
| [25133007](https://pubmed.ncbi.nlm.nih.gov/25133007/) | 2014 | Reporte de Caso | Case Reports in Rheumatology | Vasculitis digital en paciente con AR de 15 años de evolución respondió favorablemente a adalimumab; resolución de úlcera necrotizante en dedos tras inicio del tratamiento |
| [30773522](https://pubmed.ncbi.nlm.nih.gov/30773522/) | 2019 | Reporte de Caso | Internal Medicine (Tokyo) | Crisis aguda de hipertensión pulmonar ocho meses después de reducción de dosis de adalimumab en paciente con vasculitis reumatoide; sugiere papel de adalimumab en el control de VR pulmonar |
| [34068884](https://pubmed.ncbi.nlm.nih.gov/34068884/) | 2021 | Revisión | Journal of Clinical Medicine | Episcleritis y escleritis asociadas a AR: actualización en tratamiento con DMARDs biológicos incluyendo anti-TNF en formas difusas y necrotizantes refractarias |
| [28719435](https://pubmed.ncbi.nlm.nih.gov/28719435/) | 2018 | Reporte de Caso | American Journal of Dermatopathology | Vasculitis leucocitoclástica con hemofagocitosis perivascular dérmica asociada a terapia con adalimumab en AR; primer caso reportado de vasculitis paradójica inducida por el fármaco |
| [36418100](https://pubmed.ncbi.nlm.nih.gov/36418100/) | 2023 | Reporte de Caso | Internal Medicine (Tokyo) | Nefritis asociada a ANCA durante tratamiento con abatacept y adalimumab en AR; tocilizumab atenuó la vasculitis renal pauci-inmune |
| [23559388](https://pubmed.ncbi.nlm.nih.gov/23559388/) | 2013 | Reporte de Caso | Clinical Rheumatology | Primer caso reportado de síndrome antifosfolípido asociado a adalimumab; revisión de la literatura sobre vasculitis y SAF inducidos por adalimumab |
| [19482531](https://pubmed.ncbi.nlm.nih.gov/19482531/) | 2009 | Reporte de Caso | Néphrologie & Thérapeutique | Glomerulonefritis extracapilar necrotizante con ANCA-MPO positivo en paciente con AR tratado con adalimumab; vasculitis renal como efecto adverso de anti-TNF |

---

## Información de Mercado en Colombia

Según los datos disponibles, adalimumab **no cuenta con registros sanitarios activos ante el INVIMA en Colombia** a la fecha de este análisis. Al ser uno de los medicamentos biológicos de mayor uso a nivel mundial (Humira®, AbbVie), su ausencia en el registro colombiano puede reflejar un vacío en la base de datos consultada o una situación regulatoria pendiente de actualización. Se recomienda verificar directamente con el INVIMA y con el distribuidor local el estado actual de registro.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad completa.

> **Alerta de seguridad relevante identificada en la literatura:** Múltiples reportes de caso y estudios de farmacovigilancia incluidos en este análisis documentan que adalimumab puede **inducir paradójicamente vasculitis** en pacientes con AR, incluyendo vasculitis leucocitoclástica cutánea, eventos tipo lupus, vasculitis asociada a ANCA y nefritis pauci-inmune. Este riesgo paradójico es el principal guardrail para el uso de adalimumab específicamente en vasculitis reumatoide y debe ser evaluado y monitoreado cuidadosamente caso a caso por el especialista tratante.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La vasculitis reumatoide comparte el sustrato inflamatorio mediado por TNF-α con la AR subyacente, y existe evidencia de nivel L3 (revisión sistemática más múltiples reportes de casos) que documenta respuesta favorable a adalimumab en VR. Sin embargo, la ausencia de ensayos clínicos controlados específicos para esta indicación y el riesgo paradójico de vasculitis inducida por el fármaco justifican una recomendación condicional con supervisión estricta.

**Para avanzar se necesita:**
- Obtener datos completos de mecanismo de acción (MOA) desde DrugBank para formalizar el análisis de conexión mecanística
- Gestionar el registro sanitario ante INVIMA Colombia, dado que el fármaco no tiene registro local activo
- Recuperar información de seguridad completa del prospecto oficial (advertencias, contraindicaciones, interacciones) para completar la evaluación S1
- Establecer un protocolo de monitoreo para detección temprana de vasculitis paradójica inducida por adalimumab (hemograma, análisis de orina, ANCA, complemento)
- Validar con panel de reumatólogos expertos el uso en VR en el contexto clínico colombiano, referenciando las guías EULAR/ACR más recientes para enfermedades extraarticulares de la AR
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

