---
layout: default
title: Glucagon
parent: 僅模型預測 (L5)
nav_order: 86
evidence_level: L5
indication_count: 1
---

# Glucagon
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

El skill TxGNN Pipeline confirma el contexto del proyecto. Procedo a generar el informe de evaluación de reposicionamiento a partir del Evidence Pack.

---

# Glucagon: De Hipoglucemia Severa a Síndrome de Intestino Irritable

## Resumen en Una Frase

Glucagon es una hormona peptídica endógena disponible como medicamento inyectable, utilizado clásicamente para el tratamiento de la hipoglucemia severa y como agente de relajación del músculo liso en procedimientos radiológicos gastrointestinales. El modelo TxGNN predice que podría ser efectivo para el **Síndrome de Intestino Irritable (SII)**, con **11 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección, principalmente a través de la clase de agonistas del receptor GLP-1 (GLP-1RA), que comparte origen genético con Glucagon.

## Resumen Rápido

| Ítem | Contenido |
|------|------|
| Indicación Original | Hipoglucemia severa / Agente de relajación gastrointestinal en radiología diagnóstica |
| Nueva Indicación Predicha | Síndrome de Intestino Irritable (IBS) |
| Puntaje de Predicción TxGNN | 99.24% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Glucagon y GLP-1 (Glucagon-like peptide-1) son ambos derivados del mismo precursor genético, el proglucagon (gen *GCG*), y comparten homología estructural significativa. Glucagon actúa sobre el receptor GCGR, elevando el AMPc en el músculo liso intestinal, lo que produce un efecto antiespasmódico ya documentado y utilizado clínicamente en procedimientos de radiología del tubo digestivo. GLP-1, por su parte, actúa sobre el receptor GLP1R, con efectos bien establecidos sobre la motilidad intestinal, la hipersensibilidad visceral y el eje cerebro-intestino, que son mecanismos centrales en la fisiopatología del SII.

La evidencia clínica disponible para el SII se concentra en análogos del GLP-1, como ROSE-010 y liraglutida, y no en Glucagon directamente. Sin embargo, el oxintomódulo —otro derivado del proglucagon— actúa simultáneamente sobre GCGR y GLP1R, lo que sugiere que existe un puente funcional entre ambas vías de señalización. Esto refuerza la hipótesis de que Glucagon podría compartir parte del beneficio observado con los GLP-1RA en el SII, especialmente en lo que respecta a la modulación de la motilidad y la reducción del dolor visceral.

No obstante, la diferencia de receptor (GCGR vs. GLP1R) implica perfiles farmacológicos distintos. Actualmente no se dispone de datos detallados sobre el mecanismo de acción específico de Glucagon en el SII, y la equivalencia funcional con los GLP-1RA no puede asumirse sin validación experimental directa. La plausibilidad es alta, pero la evidencia clínica específica para Glucagon como agente terapéutico en el SII es prácticamente inexistente.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01056107](https://clinicaltrials.gov/study/NCT01056107) | Fase 1/2 | Completado | 52 | ROSE-010 (análogo GLP-1) retrasa el vaciamiento gástrico de sólidos y mejora la acomodación gástrica en mujeres con IBS-C; demostró reducción clínicamente significativa del dolor abdominal (véase PMID 35234561) |
| [NCT02731664](https://clinicaltrials.gov/study/NCT02731664) | Fase 1 | Completado | 12 | GLP-1 nativo inhibe la motilidad prandial antro-duodeno-yeyunal in vivo; proporciona base mecanística directa para péptidos derivados del proglucagon como moduladores de la motilidad intestinal superior |
| [NCT04763564](https://clinicaltrials.gov/study/NCT04763564) | Fase 2 | Terminado | 8 | Liraglutida (GLP-1RA) en pacientes con anastomosis íleo-anal y alta frecuencia intestinal; terminado prematuramente por baja inscripción, sin resultados concluyentes |
| [NCT06408610](https://clinicaltrials.gov/study/NCT06408610) | N/A | Completado | 66 | GLP-1 medido como endpoint en pacientes con IBS obesos y prediabéticos; compara entrenamiento continuo moderado vs. intervalos de alta intensidad sobre disbiosis intestinal y niveles de GLP-1 |
| [NCT05249023](https://clinicaltrials.gov/study/NCT05249023) | N/A | Completado | 37 | Butirato y salud del colon en IBS; vinculado con hipótesis de pérdida de butirato y posible modulación indirecta de secreción de GLP-1 |
| [NCT03256266](https://clinicaltrials.gov/study/NCT03256266) | N/A | Activo (sin reclutamiento) | 375 | Organoides de intestino delgado humano; evalúa respuesta a agentes terapéuticos — plataforma de investigación básica relevante para mecanismos de péptidos intestinales |
| [NCT00802971](https://clinicaltrials.gov/study/NCT00802971) | N/A | Completado | 12 | Hipoglucemia reactiva idiopática y suplementación con FOS; relevante para la biología del Glucagon en contextos de fluctuación glucémica postprandial |
| [NCT06333717](https://clinicaltrials.gov/study/NCT06333717) | N/A | Completado | 33 | Pan de centeno integral y eje microbiota-intestino-cerebro; mide liberación de péptidos intestinales incluyendo GLP-1 como endpoint secundario |
| [NCT04230655](https://clinicaltrials.gov/study/NCT04230655) | N/A | Desconocido | 110 | Dieta baja en calorías vs. balón intragástrico en obesidad; evaluación de hormonas intestinales incluyendo GLP-1 durante intervención de pérdida de peso |
| [NCT06113146](https://clinicaltrials.gov/study/NCT06113146) | N/A | Completado | 41 | Velocidad de ingesta de alimentos ultraprocesados y respuestas metabólicas; GLP-1 medido como endpoint secundario en respuesta a patrones alimentarios |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [40134805](https://pubmed.ncbi.nlm.nih.gov/40134805/) | 2025 | Revisión Sistemática y Metaanálisis | Frontiers in Endocrinology | Los GLP-1RA mejoran síntomas del SII; GLP-1 y ROSE-010 inhiben el complejo motor migratorio y reducen la motilidad GI; revisión más completa y reciente disponible sobre esta clase en IBS |
| [35234561](https://pubmed.ncbi.nlm.nih.gov/35234561/) | 2022 | Reporte de Ensayo Clínico Fase 1/2 | Scandinavian J Gastroenterology | ROSE-010 reduce significativamente el dolor durante exacerbaciones agudas de SII; análisis cruzado identifica subpoblaciones más respondedoras (IBS-C con dolor intenso) |
| [22517769](https://pubmed.ncbi.nlm.nih.gov/22517769/) | 2012 | Ensayo Clínico (doble ciego, controlado con placebo) | Am J Physiology GI Liver Physiology | ROSE-010 a 30, 100 y 300 μg sc retrasa vaciamiento gástrico de sólidos y modifica múltiples funciones motoras GI en IBS-C; evaluación de seguridad, farmacocinética y farmacodinamia |
| [28215540](https://pubmed.ncbi.nlm.nih.gov/28215540/) | 2017 | Estudio Clínico Observacional | Clinics and Research in Hepatology and Gastroenterology | Niveles séricos reducidos de GLP-1 correlacionan con mayor intensidad de dolor abdominal en IBS-C; expresión del receptor GLP-1 detectada en colon |
| [38997662](https://pubmed.ncbi.nlm.nih.gov/38997662/) | 2024 | Revisión Sistemática | J Headache and Pain | GLP-1 actúa en vías neuronales del dolor central y periférico; revisión sistemática con implicaciones para el componente de hipersensibilidad visceral en el SII |
| [30444291](https://pubmed.ncbi.nlm.nih.gov/30444291/) | 2019 | Revisión Mecanística | Experimental Physiology | Las células L intestinales secretan GLP-1 en respuesta a microbiota, ácidos biliares y SCFA; describe el papel de GLP-1 en estrés, activación inmune y sensibilización neuronal, cambios clave en la fisiopatología del SII |
| [40697433](https://pubmed.ncbi.nlm.nih.gov/40697433/) | 2025 | Estudio Real-World | Annals of Gastroenterology | En práctica clínica real, los GLP-1RA se prescriben en pacientes con SII; tasas de discontinuación significativas relacionadas con efectos adversos GI, dato relevante para la seguridad de la clase |
| [31602785](https://pubmed.ncbi.nlm.nih.gov/31602785/) | 2020 | Estudio Preclínico | Neurogastroenterology and Motility | Exendin-4 (GLP-1RA) mejora disfunción GI en modelo de rata Wistar Kyoto con SII; mecanismo vía activación de neuronas mioentéricas |
| [23338623](https://pubmed.ncbi.nlm.nih.gov/23338623/) | 2013 | Estudio Preclínico | Int J Molecular Medicine | En modelos de rata IBS-C e IBS-D, GLP-1 modula motilidad intestinal e hipersensibilidad visceral; base preclínica para el mecanismo de la vía GLP-1R en ambos subtipos de SII |
| [25427821](https://pubmed.ncbi.nlm.nih.gov/25427821/) | 2015 | Experimental/Preclínico | Advances in Experimental Medicine and Biology | GLP-1 en aerosol propuesto como agente terapéutico para diabetes e IBS; respalda la aplicabilidad de péptidos derivados del proglucagon en el SII como indicación emergente |

## Información de Mercado en Colombia

Glucagon no cuenta con registros sanitarios vigentes en Colombia (INVIMA). No se encontraron licencias activas en la base de datos consultada. El fármaco no está comercializado localmente en ninguna forma farmacéutica.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia disponible respalda sólidamente el uso de **análogos de GLP-1** (ROSE-010, liraglutida) en el SII, con base mecanística bien fundamentada en la biología compartida del proglucagon. Sin embargo, la evidencia **clínica específica para Glucagon nativo** actuando vía GCGR en el SII es prácticamente inexistente: ningún ensayo clínico evalúa directamente Glucagon como tratamiento del SII, y la diferencia de receptor (GCGR vs. GLP1R) impide asumir equivalencia terapéutica sin validación.

**Para avanzar se necesita:**
- Estudio preclínico que evalúe específicamente Glucagon (GCGR) en modelos de SII, diferenciando su efecto del de los GLP-1RA
- Obtención del prospecto oficial (INVIMA / FDA) para completar el perfil de seguridad, advertencias y contraindicaciones
- Clarificación del mecanismo de acción (MOA) vía consulta a DrugBank API (vacío de datos activo: DG002)
- Evaluación de compatibilidad de la vía de administración: Glucagon inyectable tiene limitaciones importantes para uso crónico en una indicación funcional como el SII
- Considerar si oxintomódulo (dual GCGR/GLP1R) sería un candidato de reposicionamiento más directo como puente traslacional entre Glucagon y los GLP-1RA
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

