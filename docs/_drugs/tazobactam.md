---
layout: default
title: Tazobactam
parent: 僅模型預測 (L5)
nav_order: 220
evidence_level: L5
indication_count: 2
---

# Tazobactam
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

# Tazobactam: De Inhibidor de Beta-Lactamasas a Neumonía

## Resumen en Una Frase

Tazobactam es un inhibidor de beta-lactamasas de la clase sulfona, utilizado como componente de combinaciones antibióticas (piperacilina/tazobactam, ceftolozano/tazobactam) para el tratamiento de infecciones bacterianas graves por gérmenes resistentes, sin registros sanitarios como monofármaco en Colombia.
El modelo TxGNN predice que podría ser efectivo para **Neumonía** (incluyendo neumonía nosocomial y asociada a ventilador por patógenos MDR),
con **más de 10 ensayos clínicos directamente relevantes** —incluyendo múltiples de Fase 3 completados— y **20 publicaciones en PubMed** que respaldan sólidamente esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Inhibidor de beta-lactamasas en combinaciones para infecciones bacterianas complicadas (intraabdominal, respiratoria, urinaria) |
| Nueva Indicación Predicha | Neumonía (Nosocomial / Asociada a Ventilador) |
| Puntaje de Predicción TxGNN | 99.46% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | ✗ No comercializado (como monofármaco) |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Tazobactam es un inhibidor de beta-lactamasas tipo sulfona que bloquea las enzimas Ambler clase A (incluyendo ESBL y KPC) y parcialmente clase C, producidas por bacterias resistentes que normalmente inactivarían al antibiótico beta-lactámico acompañante. Al combinarse con piperacilina o ceftolozano, tazobactam restaura la actividad bactericida contra patógenos productores de enzimas, especialmente *Pseudomonas aeruginosa* multirresistente (MDR) y Enterobacterales productores de ESBL, las cuales son causas frecuentes de fracaso terapéutico en infecciones graves.

La neumonía nosocomial (HAP) y la neumonía asociada a ventilador (VAP) son causadas con alta frecuencia precisamente por estos patógenos en entornos de UCI. Las combinaciones que contienen tazobactam logran concentraciones pulmonares adecuadas y alcanzan el objetivo farmacodinámico crítico (%T>MIC) necesario para la eficacia clínica. El mecanismo es directamente aplicable a esta indicación: la inhibición de beta-lactamasas desbloquea la actividad del beta-lactámico compañero contra los agentes causales más problemáticos de HAP/VAP en unidades de cuidados intensivos.

El ensayo pivotal ASPECT-NP (Phase 3 RCT, n=726, *Lancet Infectious Diseases* 2019) demostró de forma inequívoca la no inferioridad de ceftolozano/tazobactam frente a meropenem en neumonía nosocomial ventilada por Gram-negativos. Adicionalmente, múltiples ensayos de Fase 3 (RESTORE-IMI 2, estudio IMI/REL chino, levofloxacino vs. PIP/TAZO) han utilizado piperacilina/tazobactam como comparador activo de referencia en HABP/VABP, validando implícitamente su eficacia como estándar de tratamiento en esta indicación.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02070757](https://clinicaltrials.gov/study/NCT02070757) | Fase 3 | Completado | 726 | ASPECT-NP: ceftolozano/tazobactam vs. meropenem en neumonía nosocomial ventilada (VABP/HABP); objetivo primario de mortalidad a 28 días demostró no inferioridad |
| [NCT02493764](https://clinicaltrials.gov/study/NCT02493764) | Fase 3 | Completado | 537 | RESTORE-IMI 2: imipenem/cilastatina/relebactam vs. piperacilina/tazobactam en HABP/VABP; PIP/TAZO como comparador activo estándar en mortalidad total |
| [NCT03583333](https://clinicaltrials.gov/study/NCT03583333) | Fase 3 | Completado | 274 | IMI/REL vs. piperacilina/tazobactam en HABP/VABP; ensayo doble ciego multinacional, PIP/TAZO como referencia activa |
| [NCT00253955](https://clinicaltrials.gov/study/NCT00253955) | Fase 3 | Completado | 460 | Levofloxacino 750 mg/día vs. piperacilina/tazobactam en HAP leve-moderada (UCI y sala general); no inferioridad en curación clínica al final del tratamiento |
| [NCT01796717](https://clinicaltrials.gov/study/NCT01796717) | Fase 2/3 | Desconocido | 50 | Optimización de PIP/TAZO (4,5 g c/6 h): infusión prolongada vs. intermitente para neumonía nosocomial por patógenos con MIC elevado; evaluación de respuesta clínica y PK/PD |
| [NCT03581370](https://clinicaltrials.gov/study/NCT03581370) | Fase 3 | Reclutando | 80 | Ceftolozano/tazobactam: infusión 4 horas vs. 1 hora (2 g c/8 h) en VAP por *Pseudomonas aeruginosa*; comparación de exposición farmacocinética en equilibrio |
| [NCT06977347](https://clinicaltrials.gov/study/NCT06977347) | N/A | No iniciado | 100 | Monoterapia PIP/TAZO vs. combinación con fluoroquinolona en neumonía grave adquirida en comunidad (Corea del Sur); evidencia prospectiva para uso antipseudomonal empírico |
| [NCT04257812](https://clinicaltrials.gov/study/NCT04257812) | N/A | Desconocido | 20 | Monitoreo terapéutico de niveles plasmáticos (TDM) de ceftolozano/tazobactam en pacientes críticos; análisis del impacto clínico de los regímenes de dosis utilizados |
| [NCT00438269](https://clinicaltrials.gov/study/NCT00438269) | Fase 2 | Completado | 80 | Terapia antimicrobiana apropiada en UCI (piloto RCT); evaluación de estrategia de antibióticos de amplio espectro —incluyendo PIP/TAZO— con ajuste guiado por cultivos |
| [NCT04223752](https://clinicaltrials.gov/study/NCT04223752) | Fase 1 | Completado | 41 | Seguridad, tolerabilidad y farmacocinética de ceftolozano/tazobactam en pacientes pediátricos con neumonía nosocomial; primer estudio PK/PD pediátrico de esta combinación |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31563344](https://pubmed.ncbi.nlm.nih.gov/31563344/) | 2019 | ECA Fase 3 | Lancet Infect Dis | ASPECT-NP: ceftolozano/tazobactam no inferior a meropenem en neumonía nosocomial por Gram-negativos; eficacia y seguridad comparables en mortalidad a 28 días |
| [32785589](https://pubmed.ncbi.nlm.nih.gov/32785589/) | 2021 | ECA Fase 3 | Clin Infect Dis | RESTORE-IMI 2: imipenem/cilastatina/relebactam no inferior a PIP/TAZO en HABP/VABP; confirma a piperacilina/tazobactam como estándar comparador activo robusto |
| [39674398](https://pubmed.ncbi.nlm.nih.gov/39674398/) | 2025 | ECA Fase 3 | Int J Infect Dis | IMI/REL vs. piperacilina/tazobactam en HABP/VABP (pacientes críticamente enfermos en China); evaluación de no inferioridad en mortalidad y respuesta microbiológica |
| [38971203](https://pubmed.ncbi.nlm.nih.gov/38971203/) | 2024 | Revisión Sistemática | Int J Antimicrob Agents | PK/PD de nuevos beta-lactámicos y combinaciones beta-lactámico/inhibidor para neumonía por GNB resistentes a carbapenems; guía para optimización de dosis |
| [38823453](https://pubmed.ncbi.nlm.nih.gov/38823453/) | 2024 | Revisión Sistemática + Metaanálisis | Clin Microbiol Infect | Metaanálisis en red de regímenes antibióticos empíricos para HAP no asociada a ventilador; PIP/TAZO figura como opción estándar de referencia en los algoritmos comparativos |
| [38902935](https://pubmed.ncbi.nlm.nih.gov/38902935/) | 2025 | Cohorte Retrospectiva | Clin Infect Dis | Tasas de resistencia emergente bajo tratamiento: ceftazidima/avibactam vs. ceftolozano/tazobactam en bacteremia/neumonía por MDR-*P. aeruginosa*; C/T mostró menor tasa de resistencia adquirida (10% vs. 40%, p=0,002) |
| [39701120](https://pubmed.ncbi.nlm.nih.gov/39701120/) | 2025 | Estudio de Efectividad Comparativa | Lancet Infect Dis | CACTUS: ceftolozano/tazobactam vs. ceftazidima/avibactam para infecciones invasivas por MDR-*P. aeruginosa* en EE.UU. (estudio multicéntrico real-world, mayor hasta la fecha) |
| [35488823](https://pubmed.ncbi.nlm.nih.gov/35488823/) | 2022 | Revisión Narrativa | Rev Esp Quimioter | Ceftolozano/tazobactam en neumonía nosocomial: espectro antimicrobiano, características PK/PD, evidencia clínica disponible y criterios de selección de pacientes |
| [32662691](https://pubmed.ncbi.nlm.nih.gov/32662691/) | 2020 | Revisión Narrativa | Expert Rev Anti-infect Ther | Ceftolozano/tazobactam para HAP: revisión de eficacia en infecciones por bacilos Gram-negativos no fermentadores (especialmente *P. aeruginosa* MDR) en UCI |
| [38688353](https://pubmed.ncbi.nlm.nih.gov/38688353/) | 2024 | Consenso de Expertos | Int J Antimicrob Agents | Guía práctica SIMIT/SPILF para infecciones por GNB multirresistentes: posicionamiento de piperacilina/tazobactam y ceftolozano/tazobactam en el arsenal terapéutico actual |

---

## Información de Mercado en Colombia

Tazobactam **no cuenta con registros sanitarios vigentes como monofármaco en Colombia** (estado INVIMA: no comercializado, 0 registros). La molécula está disponible en el país exclusivamente a través de combinaciones de dosis fija con antibióticos beta-lactámicos (piperacilina/tazobactam, ceftolozano/tazobactam), cuyos registros sanitarios corresponden a los productos combinados y no al tazobactam como principio activo independiente.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La evidencia de Fase 3 es robusta y directa: el ensayo ASPECT-NP demostró la no inferioridad de ceftolozano/tazobactam frente a meropenem en neumonía nosocomial ventilada, y múltiples ensayos Fase 3 completados han utilizado piperacilina/tazobactam como comparador activo estándar en HABP/VABP, validando su eficacia con nivel L1. La puntuación TxGNN de 99,46% y el contexto mecanístico (inhibición de beta-lactamasas en patógenos causantes de HAP/VAP) son plenamente coherentes con esta evidencia.

**Para avanzar se necesita:**
- Obtener el mecanismo de acción (MOA) detallado de tazobactam desde DrugBank (actualmente [Data Gap])
- Consultar advertencias, contraindicaciones e interacciones del prospecto INVIMA o equivalente colombiano (datos de seguridad ausentes en el Evidence Pack actual)
- Definir qué combinación específica es el candidato de reposicionamiento relevante para Colombia: piperacilina/tazobactam (acceso amplio, genérico disponible) vs. ceftolozano/tazobactam (indicación HAP/VAP por MDR-*P. aeruginosa*, mayor costo)
- Evaluar el perfil de resistencia local de *P. aeruginosa* y Enterobacterales en UCI colombianas para validar la pertinencia del uso de combinaciones con tazobactam frente al patrón epidemiológico local
- Diseñar un plan de farmacovigilancia activa dado el riesgo de selección de resistencias en entornos de alta presión antibiótica
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

