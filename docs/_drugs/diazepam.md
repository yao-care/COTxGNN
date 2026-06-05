---
layout: default
title: Diazepam
parent: 僅模型預測 (L5)
nav_order: 99
evidence_level: L5
indication_count: 10
---

# Diazepam
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

# Diazepam: De Trastorno de Ansiedad a Insomnio

## Resumen en Una Frase

Diazepam (Valium) es una benzodiacepina históricamente utilizada para el tratamiento de trastornos de ansiedad, espasmos musculares y convulsiones.
El modelo TxGNN predice que podría ser efectivo para **Insomnio**,
con **24 ensayos clínicos** y **18 publicaciones** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trastorno de ansiedad (benzodiacepina de amplio espectro; uso histórico consolidado) |
| Nueva Indicación Predicha | Insomnio (insomnia disease) |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## Por qué es Razonable esta Predicción?

Diazepam actúa como modulador alostérico positivo (PAM) del receptor GABA-A, prolongando el tiempo de apertura del canal de cloruro (Cl⁻) y potenciando la inhibición neuronal tónica y fásica. Este mecanismo produce efectos sedantes e hipnóticos directamente relacionados con la fisiopatología del insomnio: la hiperactivación cortical y la insuficiencia GABAérgica son dos de los principales mecanismos patológicos identificados en el insomnio crónico. La literatura reciente (PMID 39581171, 2024) confirma explícitamente que diazepam, como PAM prototípico del GABA-A, exhibe efectos terapéuticos reconocidos en epilepsia, ansiedad e insomnio.

La relación entre ansiedad e insomnio es intrínseca desde el punto de vista clínico y neurobiológico: ambas condiciones comparten el sustrato de la hiperactivación del sistema nervioso central mediada por déficits en la señalización inhibitoria. Las benzodiacepinas han sido el tratamiento de primera línea histórico para el insomnio de corta duración, con diazepam siendo uno de los compuestos de referencia en ensayos comparativos controlados con doble ciego desde la década de 1980 (PMID 6113175). Además, diazepam se usa sistemáticamente como control positivo en modelos preclínicos de insomnio (PCPA, tirotoxicosis, CUMS), lo que confirma su efecto sedante-hipnótico bien establecido.

Cabe destacar que la predicción TxGNN con puntaje 99.99% no representa un reposicionamiento en sentido estricto, sino la formalización de una indicación históricamente reconocida pero desplazada por alternativas más seguras (Z-drogas, antagonistas de orexina) en las guías clínicas modernas. La robustez de la señal refleja la conectividad mecanística directa entre diazepam y los circuitos del sueño en el grafo de conocimiento farmacológico.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04050176](https://clinicaltrials.gov/study/NCT04050176) | Fase 3 | Activo (sin reclutamiento) | 260 | Protocolo de reducción gradual ciega de hipnóticos (benzodiacepinas y Z-drogas) combinado con TCC-I para mejorar tasas de discontinuación; confirma uso extendido de BZD en insomnio |
| [NCT02831894](https://clinicaltrials.gov/study/NCT02831894) | Fase 2 | Completado | 74 | Velocidad de reducción y rasgos personales en discontinuación de sedantes hipnóticos (benzodiacepinas); >65% de pacientes con prescripción hipnótica la usan por más de un año |
| [NCT03687086](https://clinicaltrials.gov/study/NCT03687086) | N/A | Completado | 188 | Nuevo mecanismo para ayudar a adultos mayores a discontinuar hipnóticos; evalúa estrategias más allá de la reducción gradual y la TCC-I |
| [NCT04751851](https://clinicaltrials.gov/study/NCT04751851) | N/A | Completado | 128 | Terapia de Aceptación y Compromiso (ACT) en telepsicología vs. apoyo psicológico para reducción de benzodiacepinas en insomnio con dependencia hipnótica |
| [NCT03461042](https://clinicaltrials.gov/study/NCT03461042) | Fase 4 | Completado | 17 | Combinación de ramelteon (agonista melatoninérgico) con reducción gradual de hipnóticos BZD/no-BZD en insomnio crónico |
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | N/A | Desconocido | 1400 | Cohorte prospectiva taiwanesa sobre patrones de uso de hipnóticos en adultos mayores; evalúa eficacia, seguridad y características farmacocinéticas incluyendo benzodiacepinas |
| [NCT02530580](https://clinicaltrials.gov/study/NCT02530580) | Fase 1 | Completado | 12 | Estudio cruzado de AZD7325 (nuevo modulador GABA selectivo) vs. diazepam como referencia activa; proporciona datos PK de diazepam en contexto GABA-A/insomnio |
| [NCT02281175](https://clinicaltrials.gov/study/NCT02281175) | N/A | Completado | 114 | Intervención psicosocial PASSE-65+ para reducción gradual de benzodiacepinas en adultos mayores con insomnio, ansiedad y depresión |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [6113175](https://pubmed.ncbi.nlm.nih.gov/6113175/) | 1981 | ECA | J Int Med Res | ECA doble ciego (n=100): lormetazepam 1 mg vs. diazepam 5 mg en trastornos del sueño como síntoma concomitante; lormetazepam superior en latencia de inicio y duración del sueño ininterrumpido; ambos clínicamente eficaces |
| [39581171](https://pubmed.ncbi.nlm.nih.gov/39581171/) | 2024 | Revisión | Bioorganic Chemistry | Revisión sistemática de moduladores GABA-A: diazepam confirmado como PAM prototípico con aplicaciones terapéuticas en epilepsia, ansiedad e insomnio; analiza efectos secundarios de sedación, problemas de memoria y adicción |
| [40570297](https://pubmed.ncbi.nlm.nih.gov/40570297/) | 2025 | Cohorte | Sleep | Uso crónico de BZD/BZRA en adultos mayores con insomnio crónico altera macroarquitectura del sueño NREM, oscilaciones lentas y husos del sueño; relevante para evaluación de riesgo-beneficio a largo plazo |
| [35228700](https://pubmed.ncbi.nlm.nih.gov/35228700/) | 2022 | Preclínico | Nature Neuroscience | Diazepam a largo plazo deteriora la plasticidad estructural de espinas dendríticas (via microglía/TSPO), causando deterioro cognitivo en ratones; alerta de seguridad crítica para uso crónico |
| [40583063](https://pubmed.ncbi.nlm.nih.gov/40583063/) | 2025 | Clínico-molecular | Cell Mol Biol Lett | Uso prolongado de benzodiacepinas (diazepam) y Z-drogas se asocia a mayor riesgo de cáncer de mama vía receptores GABA-A; señal de seguridad a largo plazo para poblaciones específicas |
| [37776625](https://pubmed.ncbi.nlm.nih.gov/37776625/) | 2023 | Preclínico | J Pharm Biomed Anal | Diazepam utilizado como control positivo estándar en modelo de insomnio inducido por PCPA en ratas; evalúa modulación metabólica y de vías biológicas relacionadas con el sueño |
| [34983880](https://pubmed.ncbi.nlm.nih.gov/34983880/) | 2021 | Preclínico | Exp Neurobiology | Validación de modelo de insomnio asociado a tirotoxicosis (estimulación simpática); diazepam confirma su eficacia como referencia hipnótica positiva |
| [40350874](https://pubmed.ncbi.nlm.nih.gov/40350874/) | 2025 | Preclínico | China J Chin Materia Medica | Diazepam (2 mg/kg) como grupo control positivo en modelo CUMS de depresión-insomnio en ratones; respalda su efecto hipnótico como estándar de referencia preclínico |

---

## Información de Mercado en Colombia

Diazepam **no cuenta con registros sanitarios activos en Colombia** según los datos disponibles. El medicamento presenta estado **No comercializado** con **0 registros sanitarios** en la base de datos consultada (corte: 2026-06-04). No se dispone de tabla de registros sanitarios al no existir licencias activas.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Las benzodiacepinas, incluyendo diazepam, cuentan con una base clínica bien documentada para el insomnio de corta duración desde la década de 1980 (ECA, PMID 6113175) y múltiples ensayos de Fase 2-3 vigentes que confirman su uso real en práctica clínica. El puntaje TxGNN de 99.99% refleja la robusta conectividad mecanística GABA-A → circuitos del sueño. Sin embargo, las guías clínicas modernas desplazan a las benzodiacepinas como primera línea en insomnio crónico por sus riesgos de dependencia, deterioro cognitivo y señales de seguridad oncológica emergentes, lo que exige guardrails estrictos para cualquier expansión de indicación.

**Para avanzar se necesita:**
- Obtener datos formales de mecanismo de acción (MOA desde DrugBank API) para completar el análisis mecanístico
- Descargar y analizar el prospecto oficial (INVIMA/TFDA) para extraer advertencias, contraindicaciones e interacciones farmacológicas
- Gestionar registro sanitario ante INVIMA si se considera comercialización en Colombia (actualmente sin registro)
- Diseñar plan de monitoreo de seguridad específico: evaluación del riesgo de dependencia, deterioro cognitivo en adultos mayores y señales de seguridad oncológica (cáncer de mama, PMID 40583063)
- Definir claramente el subpoblación objetivo y duración máxima de tratamiento (insomnio agudo vs. crónico) en el contexto regulatorio colombiano
- Revisar compatibilidad con guías clínicas colombianas de manejo del insomnio, donde las benzodiacepinas han sido desplazadas por alternativas con mejor perfil de seguridad
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

