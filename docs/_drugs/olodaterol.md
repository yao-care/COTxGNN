---
layout: default
title: Olodaterol
parent: 僅模型預測 (L5)
nav_order: 184
evidence_level: L5
indication_count: 2
---

# Olodaterol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Olodaterol: De Enfermedad Pulmonar Obstructiva Crónica a Bronquitis

## Resumen en Una Frase

Olodaterol es un broncodilatador de acción ultralarga (LABA) indicado para el tratamiento de mantenimiento de la Enfermedad Pulmonar Obstructiva Crónica (EPOC) en múltiples países, aunque actualmente no está comercializado en Colombia.
El modelo TxGNN predice que podría ser efectivo para **Bronquitis**, con **3 ensayos clínicos** y **2 publicaciones** que actualmente respaldan esta dirección, principalmente de forma indirecta a través de estudios en poblaciones con EPOC que incluyen bronquitis crónica como fenotipo principal.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad Pulmonar Obstructiva Crónica (EPOC) — broncodilatador de mantenimiento |
| Nueva Indicación Predicha | Bronquitis |
| Puntaje de Predicción TxGNN | 99.84% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Olodaterol es un agonista β₂-adrenérgico de alta selectividad y larga duración (LABA). Su mecanismo de acción se basa en la activación de receptores β₂ en el músculo liso bronquial, lo que incrementa el AMPc intracelular mediante la activación de la adenilato ciclasa. El AMPc elevado activa la PKA, que inhibe la fosforilación de la cadena ligera de miosina, produciendo relajación del músculo liso de la vía aérea y broncodilatación sostenida durante 24 horas con una sola dosis diaria. Adicionalmente, la activación de receptores β₂ puede suprimir la desgranulación de mastocitos y reducir la liberación de mediadores proinflamatorios.

La bronquitis crónica es uno de los dos fenotipos clásicos de la EPOC, caracterizada por hipersecreción de moco, inflamación de la vía aérea y obstrucción al flujo aéreo. El componente obstructivo y broncoespástico de la bronquitis puede ser directamente aliviado por un agonista β₂ de larga duración como olodaterol. La superposición fisiopatológica entre bronquitis crónica y EPOC es tal que la mayoría de los estudios clínicos de olodaterol incluyen pacientes con bronquitis crónica dentro de la población con EPOC estudiada.

Desde el punto de vista clínico, el estudio de vigilancia poscomercialización NCT02850978 incluyó explícitamente pacientes japoneses con EPOC en sus fenotipos de bronquitis crónica y enfisema. Esto respalda la plausibilidad de la predicción del modelo TxGNN, aunque la evidencia para bronquitis como indicación primaria e independiente de la EPOC sigue siendo indirecta, sin ensayos controlados con bronquitis como criterio de inclusión principal.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02850978](https://clinicaltrials.gov/study/NCT02850978) | N/A (PMS) | Completado | 1.335 | Vigilancia poscomercialización de tiotropio+olodaterol en pacientes japoneses con EPOC (bronquitis crónica y enfisema); evaluó seguridad y efectividad a largo plazo en entorno del mundo real, con datos de tolerabilidad directamente aplicables al fenotipo bronquítico |
| [NCT05127304](https://clinicaltrials.gov/study/NCT05127304) | N/A | Completado | 11.316 | Estudio de vida real comparando TIO/OLO vs FF/UMEC/VI en EPOC; evalúa utilización de recursos de salud y resultados clínicos incluyendo el fenotipo de bronquitis crónica como parte del espectro de la EPOC |
| [NCT03333018](https://clinicaltrials.gov/study/NCT03333018) | N/A | Completado | 22.155 | Estudio de utilización de medicamentos para EPOC en Europa; cubre población con bronquitis crónica y evalúa patrones de uso de broncodilatadores (el fármaco principal es aclidinium; datos de olodaterol no extraíbles de forma independiente) |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [27354040](https://pubmed.ncbi.nlm.nih.gov/27354040/) | 2016 | Revisión Narrativa | Am J Health-Syst Pharm | Revisión exhaustiva de la farmacología, farmacocinética, eficacia y seguridad de olodaterol como LABA de una vez al día para EPOC; proporciona base mecanística aplicable a bronquitis crónica |
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Guía Clínica | Basic Clin Pharmacol Toxicol | Guía finlandesa nacional de EPOC estable: diagnóstico y farmacoterapia; posiciona los broncodilatadores de larga duración como piedra angular del tratamiento en un espectro que incluye bronquitis crónica |

---

## Información de Mercado en Colombia

Olodaterol no cuenta con registros sanitarios activos ante INVIMA en Colombia. El medicamento no está comercializado en el país, por lo que cualquier estrategia de acceso requeriría iniciar un proceso de registro sanitario o importación bajo modalidades especiales.

---

## Consideraciones de Seguridad

> Consultar el prospecto oficial para información completa de seguridad. Los datos de advertencias, contraindicaciones e interacciones farmacológicas de olodaterol no estuvieron disponibles en este Evidence Pack y representan una brecha de datos de severidad bloqueante para la evaluación de seguridad inicial (ver Data Gap DG001).

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
El mecanismo de acción de olodaterol es farmacológicamente coherente con el manejo del componente obstructivo de la bronquitis crónica, que coexiste habitualmente con la EPOC en la práctica clínica. Sin embargo, la evidencia directa para bronquitis como indicación primaria es limitada e indirecta, sin ensayos controlados que aborden bronquitis como criterio de inclusión principal. Adicionalmente, el fármaco carece de registro sanitario en Colombia, lo que constituye una barrera regulatoria significativa.

**Para avanzar se necesita:**
- Obtener el prospecto oficial (INVIMA, EMA o FDA) para completar la evaluación de advertencias y contraindicaciones (Data Gap DG001 — bloqueante)
- Confirmar el mecanismo de acción detallado mediante consulta a DrugBank API (Data Gap DG002 — alta severidad)
- Identificar y evaluar ensayos clínicos que aborden bronquitis como indicación primaria, diferenciada del espectro EPOC
- Definir la subpoblación objetivo: bronquitis crónica en el contexto de EPOC vs. bronquitis aguda aislada
- Evaluar la viabilidad de registro sanitario ante INVIMA o explorar vías de acceso bajo uso compasivo o importación especial
- Completar el análisis de interacciones farmacológicas (DDI — no encontrado en esta versión del pack)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

