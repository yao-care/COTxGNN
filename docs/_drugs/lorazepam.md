---
layout: default
title: Lorazepam
parent: 僅模型預測 (L5)
nav_order: 162
evidence_level: L5
indication_count: 10
---

# Lorazepam
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

# Lorazepam: De Ansiedad y Crisis Epilépticas a Insomnio

## Resumen en Una Frase

Lorazepam es una benzodiazepina de referencia utilizada clásicamente para el manejo de la ansiedad, la sedación procedimental, las crisis epilépticas y la abstinencia alcohólica, actuando como modulador positivo alostérico del receptor GABA-A.
El modelo TxGNN predice que podría ser efectivo para **Insomnio**, con un puntaje de predicción del **99.80%**,
respaldado por **4 ensayos clínicos relevantes** y **18 publicaciones científicas** que actualmente sustentan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Ansiedad, sedación y crisis epilépticas (no especificada formalmente en este paquete de evidencia) |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99.80% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos formales sobre el mecanismo de acción en este paquete de evidencia. Sin embargo, según la información conocida, Lorazepam es una benzodiazepina de potencia media-alta que actúa aumentando la frecuencia de apertura del canal de cloro mediado por el receptor GABA-A, produciendo efectos sedantes, ansiolíticos, anticonvulsivantes y de relajación muscular. Esta acción farmacológica está ampliamente caracterizada en la literatura científica.

La conexión entre la actividad GABAérgica de Lorazepam y el insomnio es directa: el insomnio se asocia con hiperactivación de los circuitos de excitación cortical, y el potenciamiento de la transmisión inhibitoria GABA-A reduce esta hiperexcitabilidad, facilitando el inicio y el mantenimiento del sueño. De hecho, las benzodiazepinas de acción corta e intermedia han sido históricamente empleadas como agentes hipnóticos a corto plazo y figuran en guías de práctica clínica internacionales como tratamiento farmacológico de segunda línea para el insomnio agudo y transitorio.

La principal consideración para esta predicción no es la plausibilidad de la eficacia —demostrada en ensayos clínicos directos con Fase 3 completada— sino el perfil de seguridad a largo plazo: la tolerancia farmacológica aparece típicamente a las 2–4 semanas y el riesgo de dependencia física limita el uso a ciclos cortos. Cualquier protocolo de uso en insomnio deberá incluir guardarraíles explícitos de duración y un plan estructurado de discontinuación.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03331042](https://clinicaltrials.gov/study/NCT03331042) | Fase 3 | Completado | 85 | Doble ciego, 4 períodos cruzados: SM-1 (difenhidramina 50 mg + zolpidem 5 mg liberación retardada + **lorazepam 0.5 mg liberación retardada**) vs dos comparadores activos vs placebo en modelo de insomnio transitorio por adelanto de fase 5 h; evalúa eficacia, seguridad y tolerabilidad |
| [NCT02671760](https://clinicaltrials.gov/study/NCT02671760) | Fase 2 | Completado | 39 | Estudio farmacodinámico de SM-1 (incluye **lorazepam de liberación retardada**) vs comparador vs placebo en adultos con insomnio ocasional; medición de tiempo total de sueño en centro de sueño de Nueva York |
| [NCT04396327](https://clinicaltrials.gov/study/NCT04396327) | Fase 2 | Sin iniciar | 14 | Cruzado 2 vías: SM-1 (incluye **lorazepam 0.5 mg**) vs combinación difenhidramina + lorazepam en modelo de insomnio transitorio por adelanto de fase 3 h; evalúa efectos farmacodinámicos sobre sueño y seguridad |
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | N/A | Desconocido | 1400 | Cohorte prospectiva en centro académico de Taiwán: patrones de uso de hipnóticos (incluyendo benzodiazepinas) en adultos mayores; evalúa eficacia, seguridad, farmacocinética y resultados clínicos a largo plazo |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10220122](https://pubmed.ncbi.nlm.nih.gov/10220122/) | 1999 | ECA | Int Clin Psychopharmacol | **Lorazepam directamente en insomnio primario**: 0.5 mg TID (tratamiento en 24 h) superior a 1.5 mg nocturno en latencia MSLT y síntomas diurnos; respalda enfoque de tratamiento continuo |
| [3280615](https://pubmed.ncbi.nlm.nih.gov/3280615/) | 1988 | ECA | J Clin Pharmacol | Estudio cruzado doble ciego, 8 insomníacos crónicos, 3 semanas: **lorazepam 2 mg superó a flurazepam 30 mg** en la mayoría de parámetros polisomnográficos del sueño |
| [35087274](https://pubmed.ncbi.nlm.nih.gov/35087274/) | 2022 | Revisión | J Multidiscip Healthc | Revisión de eficacia, seguridad e interacciones farmacológicas del tratamiento del insomnio en COVID-19; incluye benzodiazepinas (lorazepam) entre las opciones terapéuticas con análisis de DDI |
| [30625122](https://pubmed.ncbi.nlm.nih.gov/30625122/) | 2018 | Revisión | Medical Letter | Guía comparativa de fármacos aprobados para insomnio crónico; incluye lorazepam en la tabla de hipnóticos orales disponibles |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | Meta-análisis | Acta Pharmaceutica (Zagreb) | Meta-análisis de tranquilizantes (incluyendo benzodiazepinas) en adultos mayores con enfermedades crónicas; determina dosis óptima y perfil de efectos adversos aceptable |
| [19514972](https://pubmed.ncbi.nlm.nih.gov/19514972/) | 2009 | Estudio Preclínico | Drug Delivery | Microemulsiones intranasales de **lorazepam** para insomnio; inducción de sueño comparable o superior a diazepam y alprazolam en modelo de ratas; sugiere viabilidad de nueva formulación |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Revisión | Expert Opin Drug Metab Toxicol | Farmacocinética comparada de ansiolíticos incluyendo lorazepam; caracteriza propiedades de absorción y eliminación relevantes para la dosificación hipnótica |
| [15341891](https://pubmed.ncbi.nlm.nih.gov/15341891/) | 2004 | Epidemiológico | Sleep Medicine | Análisis de patrones de prescripción de hipnóticos en gran HMO; describe uso real de benzodiazepinas (incluido lorazepam) en la población con diagnóstico de insomnio |
| [15040803](https://pubmed.ncbi.nlm.nih.gov/15040803/) | 2004 | Cohorte | Health Qual Life Outcomes | Evaluación de calidad del sueño y uso de sedantes (incluyendo benzodiazepinas) en pacientes hospitalizados adultos; identifica factores asociados a prescripción de hipnóticos |
| [25453732](https://pubmed.ncbi.nlm.nih.gov/25453732/) | 2014 | Cohorte | Clin Therapeutics | Uso de benzodiazepinas e hipnóticos en adultos mayores gravemente enfermos; contextualiza riesgos de uso inapropiado en insomnio según criterios Choosing Wisely 2014 |

---

## Información de Mercado en Colombia

Lorazepam **no cuenta con registros sanitarios activos en Colombia**. No se encontraron licencias vigentes en la base de datos de INVIMA para este principio activo. Cualquier uso requeriría gestión de importación bajo régimen especial o solicitud de nuevo registro sanitario.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La eficacia de Lorazepam como agente hipnótico cuenta con respaldo directo de ensayos clínicos de Fase 3 completados (NCT03331042) y ECAs clásicos (PMID 10220122, 3280615), y el mecanismo GABA-A es directamente aplicable al insomnio. Sin embargo, la ausencia total de registro sanitario en Colombia y el perfil de dependencia inherente a las benzodiazepinas requieren condiciones estrictas de implementación antes de cualquier avance clínico.

**Para avanzar se necesita:**
- Obtener registro sanitario en INVIMA o evaluar uso bajo régimen especial de importación
- Completar datos de MOA y advertencias oficiales (actualmente con Data Gap en fuente regulatoria)
- Establecer protocolo clínico con duración máxima de tratamiento (≤4 semanas) y plan estructurado de discontinuación gradual
- Definir criterios de exclusión para poblaciones de alto riesgo (adultos mayores, pacientes con antecedentes de abuso de sustancias, insuficiencia respiratoria)
- Evaluar posicionamiento frente a alternativas ya aprobadas en Colombia (antagonistas de orexina, z-drugs) como terapias de primera línea para insomnio crónico
- Implementar sistema de farmacovigilancia activa para detección temprana de dependencia en la indicación de insomnio
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

