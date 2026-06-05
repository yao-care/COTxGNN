---
layout: default
title: Sunitinib
parent: 僅模型預測 (L5)
nav_order: 217
evidence_level: L5
indication_count: 10
---

# Sunitinib
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

# Sunitinib: De Carcinoma de Células Renales a Liposarcoma

## Resumen en Una Frase

Sunitinib es un inhibidor multiobjetivo de tirosina quinasa globalmente reconocido como tratamiento de primera línea para el carcinoma de células renales (ccRCC) y tumores del estroma gastrointestinal (GIST), aunque no cuenta con registro sanitario en Colombia.
El modelo TxGNN predice que podría ser efectivo para **Liposarcoma**,
con **3 ensayos clínicos** y **9 publicaciones** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Carcinoma de células renales / GIST (indicación global reconocida; sin registro en Colombia) |
| Nueva Indicación Predicha | Liposarcoma |
| Puntaje de Predicción TxGNN | 99.87% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Sin embargo, según la información conocida, sunitinib pertenece a la clase de inhibidores de tirosina quinasa con receptores múltiples (RTK inhibidor), bloqueando entre otros VEGFR1/2/3, PDGFRα/β, KIT y FLT3. Su eficacia en carcinoma de células renales y GIST ha sido ampliamente comprobada a nivel global, y mecanísticamente es aplicable al liposarcoma a través de vías compartidas.

El liposarcoma desdiferenciado presenta con frecuencia amplificación de PDGFRA y sobreexpresión de VEGF; al inhibir PDGFRα/β y VEGFR, sunitinib puede bloquear simultáneamente las señales de proliferación tumoral y angiogénesis. El subtipo mixoide con fusión FUS-DDIT3 también cuenta con reportes de activación de la vía PDGFR relacionada, lo que refuerza la base mecanística de la predicción del modelo TxGNN.

Los sarcomas de tejidos blandos y el RCC comparten dependencia de la señalización VEGF/PDGFR, explicando por qué sunitinib ha sido explorado en ambas entidades. Los ensayos clínicos directos en sarcomas de tejidos blandos —incluyendo liposarcoma— demuestran actividad antitumoral, aunque las tasas de respuesta son modestas comparadas con las observadas en RCC.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00400569](https://clinicaltrials.gov/study/NCT00400569) | Fase 2 | Completado | 48 | Sunitinib vía oral una vez al día en sarcoma de tejidos blandos metastásico e irresecable; incluye explícitamente liposarcoma, leiomiosarcoma, fibrosarcoma y MFH; evalúa dosis y actividad antitumoral |
| [NCT00474994](https://clinicaltrials.gov/study/NCT00474994) | Fase 2 | Completado | 53 | Sunitinib en dosificación continua en sarcomas no-GIST metastásicos, localmente avanzados o recurrentes; diseño específico para sarcomas con enfoque en respuesta y tolerabilidad |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Fase 2 | Completado | 131 | Regorafenib (inhibidor RTK de la misma clase) en múltiples subtipos de sarcoma; sustentado en actividad previa de sunitinib en GIST y sarcomas de tejidos blandos; evidencia indirecta de clase terapéutica |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [21154746](https://pubmed.ncbi.nlm.nih.gov/21154746/) | 2011 | Ensayo Fase 2 | Int J Cancer | Sunitinib en tres subtipos prevalentes de STS (leiomiosarcoma, **liposarcoma**, MFH); evalúa seguridad y eficacia en pacientes en recaída o refractarios con alteraciones moleculares accionables similares a GIST |
| [23482782](https://pubmed.ncbi.nlm.nih.gov/23482782/) | 2013 | Reporte de Caso | Anticancer Res | Beneficio clínico duradero de sunitinib en **liposarcoma metastásico** con múltiples líneas previas; documentación directa de actividad en este subtipo específico |
| [38254762](https://pubmed.ncbi.nlm.nih.gov/38254762/) | 2024 | Revisión Traslacional | Cancers | Alteraciones genéticas, epigenéticas y transcriptómicas en liposarcoma para selección de terapia dirigida; contextualiza opciones actuales e identifica dianas como PDGFRA relevantes para sunitinib |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Revisión | Ann Oncol | Tratamiento de STS impulsado por histología; menciona actividad de sunitinib en el espectro de terapias dirigidas para subtipos específicos incluyendo liposarcoma y sarcomas con perfil PDGFR |
| [24555529](https://pubmed.ncbi.nlm.nih.gov/24555529/) | 2014 | Revisión | Expert Rev Anticancer Ther | Terapias emergentes para STS en adultos; describe el papel de sunitinib y otros TKIs en segunda línea o enfermedad metastásica irresecable con evidencia de actividad parcial |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Revisión | Magyar Onkologia | Tratamiento médico de STS basado en subtipo histológico; revisa evidencia de inhibidores de tirosina quinasa incluyendo sunitinib en liposarcoma y otros subtipos con dianas moleculares |
| [28423517](https://pubmed.ncbi.nlm.nih.gov/28423517/) | 2017 | Estudio Molecular | Oncotarget | Secuenciación de nueva generación en condrosarcoma mixoide extraesquelético; identifica factores predictivos de beneficio a sunitinib incluyendo activación de vías PDGFR/VEGFR |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | Protocolo de Ensayo | BMC Cancer | Protocolo del ensayo REGOSARC (regorafenib en STS avanzado); fundamenta el uso de inhibidores de RTK en sarcomas citando actividad previa documentada de sunitinib en esta indicación |
| [38717131](https://pubmed.ncbi.nlm.nih.gov/38717131/) | 2024 | Cohorte | Am J Surg Pathol | Sarcoma miofibroblástico inflamatorio mixoide con alteraciones moleculares accionables; amplía el espectro de sarcomas con potencial de terapia dirigida y contexto biológico relevante |

---

## Información de Mercado en Colombia

Sunitinib no cuenta con ningún registro sanitario vigente ante el INVIMA. No existen productos comercializados en Colombia bajo esta denominación común internacional.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida — Inhibidor multiobjetivo de tirosina quinasa (RTK inhibidor; clase oral antineoplásico) |
| Riesgo de Mielosupresión | Moderado — neutropenia y trombocitopenia son efectos adversos frecuentes documentados en ensayos clínicos de sarcoma y RCC |
| Clasificación de Emetogenicidad | Baja a moderada (oral; menor potencial emetogénico que citotóxicos convencionales) |
| Items de Monitoreo | Hemograma completo con diferencial, ALT/AST (función hepática), creatinina (función renal), TSH (función tiroidea), ECG (intervalo QTc), presión arterial en cada ciclo |
| Protección en Manejo | Cumplir regulaciones de manejo de antineoplásicos orales; precauciones de seguridad para medicamentos citotóxicos según protocolo institucional |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Dos ensayos clínicos de Fase 2 completados evalúan directamente sunitinib en sarcomas de tejidos blandos (incluyendo liposarcoma), respaldados por un reporte de caso con beneficio clínico duradero en liposarcoma metastásico y múltiples revisiones sistemáticas que sustentan la actividad de inhibidores RTK en esta entidad. La base mecanística mediante inhibición de PDGFRα/β en tumores con amplificación PDGFRA es biológicamente coherente, aunque la evidencia no alcanza nivel de Fase 3 ni cuenta con aprobación regulatoria específica.

**Para avanzar se necesita:**
- Obtener datos completos de MOA y perfil de seguridad (advertencias, contraindicaciones) desde el prospecto oficial y DrugBank
- Iniciar proceso de evaluación de registro sanitario ante el INVIMA para viabilidad de acceso en Colombia
- Identificar subtipos histológicos de liposarcoma con mayor probabilidad de respuesta (desdiferenciado con amplificación PDGFRA vs. mixoide vs. bien diferenciado)
- Diseñar protocolo de monitoreo cardiovascular (QTc, hipertensión, fracción de eyección) dado el perfil de toxicidad cardíaca conocido de sunitinib
- Evaluar secuenciación terapéutica y criterios de selección de pacientes para uso compasivo o ensayo clínico en Colombia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

