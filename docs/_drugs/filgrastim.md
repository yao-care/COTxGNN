---
layout: default
title: Filgrastim
parent: 僅模型預測 (L5)
nav_order: 79
evidence_level: L5
indication_count: 10
---

# Filgrastim
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

El skill confirma que estoy en el contexto correcto del pipeline TxGNN. Procedo a generar el informe de evaluación.

---

# Filgrastim: De Neutropenia por Quimioterapia a Trastorno Primario de Liberación de Plaquetas

## Resumen en Una Frase

Filgrastim es un Factor Estimulante de Colonias de Granulocitos (G-CSF) recombinante, ampliamente utilizado a nivel global para la prevención y tratamiento de la neutropenia post-quimioterapia y la movilización de células madre hematopoyéticas para trasplante.
El modelo TxGNN predice que podría ser efectivo para el **Trastorno Primario de Liberación de Plaquetas**, con **14 ensayos clínicos** recuperados y **1 publicación** que ofrecen evidencia periférica en el ámbito hematopoyético.
Sin embargo, ninguno de los ensayos evalúa directamente a Filgrastim como tratamiento primario de este trastorno, por lo que la evidencia se clasifica como nivel L4 (mecanística/indirecta).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Neutropenia post-quimioterapia / Movilización de células madre hematopoyéticas |
| Nueva Indicación Predicha | Trastorno primario de liberación de plaquetas |
| Puntaje de Predicción TxGNN | 99.998% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de Filgrastim en esta base de datos. Sin embargo, por conocimiento farmacológico establecido, Filgrastim es un G-CSF recombinante que actúa uniéndose al receptor CSF3R (CD114), activando vías de señalización JAK2/STAT3, MAPK y PI3K. Esto promueve la proliferación, diferenciación y supervivencia de precursores mieloides en médula ósea, con efecto predominante sobre el linaje granulocítico (neutrófilos).

El trastorno primario de liberación de plaquetas —como las enfermedades asociadas a MYH9 (síndrome de May-Hegglin, síndrome de Sebastian) o el síndrome PARIS— involucra una disfunción de los megacariocitos en su capacidad para fragmentarse correctamente y liberar plaquetas maduras. El vínculo mecanístico propuesto se basa en la expresión baja pero documentada del receptor CSF3R en megacariocitos y sus precursores: Filgrastim podría teóricamente ampliar el reservorio de progenitores megacariocíticos (CMP → MkP), compensando de forma indirecta la deficiencia en la producción plaquetaria. La racionalidad del modelo TxGNN refleja esta conexión de proximidad en el grafo de conocimiento hematopoyético.

No obstante, esta conexión se clasifica como **"indirecta-plausible"**: la actividad primaria de Filgrastim favorece el linaje granulocítico, no el megacariocítico. Los 14 ensayos recuperados corresponden exclusivamente a contextos de trasplante hematopoyético donde Filgrastim actúa como soporte, no como tratamiento causal del trastorno de liberación plaquetaria. La distancia biológica entre ambas indicaciones es considerable y requiere validación preclínica específica antes de cualquier desarrollo clínico.

---

## Evidencia de Ensayos Clínicos

> ⚠️ **Nota de interpretación:** Los 14 ensayos identificados utilizan Filgrastim en contextos de trasplante de células madre hematopoyéticas (HSCT) como agente de soporte, **no** como tratamiento primario del trastorno de liberación de plaquetas. Todos presentan relevancia Grade C (indirecta) para esta indicación predicha.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00281879](https://clinicaltrials.gov/study/NCT00281879) | Fase 2 | Terminado | 200 | HSCT de donante no relacionado para malignidades hematológicas; Filgrastim como apoyo en movilización de células madre. Terminado antes de completarse. |
| [NCT00043979](https://clinicaltrials.gov/study/NCT00043979) | Fase 2 | Completado | 60 | Trasplante alogénico/singénico en sarcomas pediátricos de alto riesgo; Filgrastim para reconstitución hematopoyética post-trasplante. |
| [NCT00354172](https://clinicaltrials.gov/study/NCT00354172) | Fase 2 | Terminado | 16 | Trasplante de sangre de cordón umbilical + células NK para leucemia mieloide; Filgrastim como medicación de soporte. Terminado con muestra pequeña (n=16). |
| [NCT00923364](https://clinicaltrials.gov/study/NCT00923364) | Fase 2 | Completado | 19 | HSCT de intensidad reducida en pacientes con mutaciones GATA2 (que afectan megacariocitos y plaquetas); Filgrastim para soporte hematopoyético previo al trasplante. |
| [NCT02646098](https://clinicaltrials.gov/study/NCT02646098) | Fase 2 | Completado | 64 | Selección CD34+ vs. no-selección en trasplante autólogo para linfoma de células del manto y DLBCL; evaluación de estrategias de recolección de progenitores hematopoyéticos. |
| [NCT05436418](https://clinicaltrials.gov/study/NCT05436418) | Fase 1/2 | Reclutando | 260 | Dosis mínima efectiva de ciclofosfamida post-trasplante para profilaxis de GvHD combinado con sirolimus y MMF; Filgrastim como soporte hematopoyético post-trasplante. |
| [NCT04047628](https://clinicaltrials.gov/study/NCT04047628) | Fase 3 | Reclutando | 156 | HSCT autólogo vs. mejor terapia disponible en esclerosis múltiple recurrente resistente al tratamiento; Filgrastim para movilización de células madre. Seguimiento a 72 meses. |
| [NCT00076752](https://clinicaltrials.gov/study/NCT00076752) | Fase 2 | Completado | 9 | Linfodepleción intensificada + HSCT autólogo en lupus eritematoso sistémico grave; Filgrastim como agente de movilización de células madre. |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Fase 2 | Reclutando | 358 | Plataforma de comparación de combinaciones para profilaxis de GvHD en HSCT con donante no relacionado no compatible; Filgrastim no es el fármaco de investigación principal. |
| [NCT00245037](https://clinicaltrials.gov/study/NCT00245037) | Fase 1/2 | Completado | 147 | HSCT alogénico no mieloablativo con busulfán + fludarabina + irradiación corporal total en malignidades hematológicas; Filgrastim para movilización de células madre periféricas. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [29770133](https://pubmed.ncbi.nlm.nih.gov/29770133/) | 2018 | Estudio observacional prospectivo | Frontiers in Immunology | G-CSF en donantes sanos moviliza preferencialmente subconjuntos de linfocitos para trasplante alogénico. Documenta la selectividad de linaje celular de Filgrastim en un contexto hematopoyético real, pero no aborda directamente la función megacariocítica ni los trastornos de liberación de plaquetas. |

---

## Información de Mercado en Colombia

Filgrastim **no cuenta con registros sanitarios activos en Colombia** (0 licencias en el sistema INVIMA). Aunque el fármaco tiene amplio uso clínico global —con aprobaciones en FDA (Neupogen®), EMA y múltiples agencias regulatorias— su ausencia del mercado colombiano representa una barrera regulatoria que deberá resolverse antes de cualquier desarrollo clínico local orientado a esta nueva indicación.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de TxGNN descansa sobre una conexión mecanística indirecta y biológicamente plausible (actividad G-CSF sobre progenitores megacariocíticos), pero no existe ningún ensayo clínico ni publicación que evalúe directamente a Filgrastim como tratamiento del trastorno primario de liberación de plaquetas. La ausencia de registros sanitarios en Colombia (0 licencias INVIMA), la falta de datos de seguridad locales y el nivel de evidencia L4 hacen prematuro avanzar hacia el desarrollo clínico sin investigación básica y preclínica previa.

**Para avanzar se necesita:**
- Confirmar la expresión y funcionalidad del receptor CSF3R en megacariocitos y progenitores megacariocíticos humanos (resolver Data Gap DG002 — MOA)
- Realizar estudios preclínicos dirigidos en modelos de trastorno primario de liberación de plaquetas (modelos *in vitro* y *in vivo* de enfermedades MYH9 o síndrome PARIS)
- Obtener y revisar el prospecto oficial de Filgrastim para completar advertencias, contraindicaciones e interacciones farmacológicas (resolver Data Gap DG001)
- Estratificar el subtipo específico del trastorno (defecto de liberación vs. defecto de producción megacariocítica) para refinar la hipótesis terapéutica
- Evaluar la viabilidad de obtener registro sanitario INVIMA en Colombia para esta indicación potencial, en caso de que la evidencia preclínica resulte favorable
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

