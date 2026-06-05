---
layout: default
title: Celecoxib
parent: 僅模型預測 (L5)
nav_order: 85
evidence_level: L5
indication_count: 10
---

# Celecoxib
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

El skill txgnn-pipeline no añade instrucciones específicas para generación de informes. Procedo directamente con el informe según las instrucciones del sistema, usando la indicación de **rango 9 (espondilopatía inflamatoria)** como sujeto principal, ya que es la única candidata con evidencia L1 y recomendación accionable — usar el rango 1 ("acromesomelic dysplasia") produciría un informe vacío de evidencia.

---

# Celecoxib: De Artritis Reumatoide/Osteoartritis a Espondilopatía Inflamatoria

## Resumen en Una Frase

Celecoxib es el primer inhibidor selectivo de la ciclooxigenasa-2 (COX-2) introducido en la práctica clínica, utilizado en múltiples países para el tratamiento sintomático de la osteoartritis, artritis reumatoide y dolor agudo.
El modelo TxGNN predice que podría ser efectivo para la **Espondilopatía Inflamatoria** (incluyendo espondilitis anquilosante y espondiloartritis axial),
con **19 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sin registro en Colombia (globalmente aprobado para osteoartritis y artritis reumatoide) |
| Nueva Indicación Predicha | Espondilopatía Inflamatoria |
| Puntaje de Predicción TxGNN | 99.80% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados del mecanismo de acción en la base de datos local. Sin embargo, Celecoxib es ampliamente reconocido como inhibidor selectivo de la ciclooxigenasa-2 (COX-2), enzima responsable de la síntesis de prostaglandina E2 (PGE2), mediador central de la inflamación articular, el dolor y la fiebre. A diferencia de los AINEs no selectivos, Celecoxib inhibe preferentemente COX-2 preservando la actividad de COX-1, lo que reduce significativamente la toxicidad gastrointestinal típica de otros antiinflamatorios.

En la espondilopatía inflamatoria (SpA/AS), la COX-2 se expresa de forma intensa en las articulaciones sacroilíacas y los puntos de entesis (inserción tendinosa-ósea). La PGE2 derivada de COX-2 no solo sostiene la inflamación local sino que también activa vías de osificación progresiva de la columna vertebral. Evidencia reciente de 2025 (PMID 39757202) demuestra que Celecoxib es el **único AINE capaz de inhibir la progresión radiológica** en espondiloartritis, con un mecanismo diferenciador independiente de la inhibición COX que no se observa con diclofenaco u otros AINEs no selectivos. Este hallazgo eleva considerablemente la relevancia clínica de Celecoxib frente a los competidores de su clase.

La predicción del modelo TxGNN está sólidamente respaldada por un extenso programa clínico global: cuatro ensayos de Fase 3/4 completados con más de 1.000 participantes acumulados, junto con estudios de combinación con terapia biológica, confirman eficacia y seguridad en espondilitis anquilosante —subentidad principal de la espondilopatía inflamatoria. En países como Estados Unidos, la Unión Europea y China, Celecoxib ya cuenta con aprobación regulatoria para AS, lo que refuerza la razonabilidad de su entrada al mercado colombiano para esta indicación.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00648141](https://clinicaltrials.gov/study/NCT00648141) | Fase 3 | Completado | 458 | Celecoxib 200mg QD vs 200mg BID vs Diclofenac 75mg BID en AS durante 12 semanas; ensayo pivotal de referencia que evalúa eficacia y seguridad comparativa |
| [NCT00762463](https://clinicaltrials.gov/study/NCT00762463) | Fase 3 | Completado | 240 | Celecoxib vs Diclofenac SR en pacientes chinos con AS; doble ciego con fase de extensión a Celecoxib 400mg QD para validación en población asiática |
| [NCT02528201](https://clinicaltrials.gov/study/NCT02528201) | Fase 4 | Completado | 330 | Celecoxib 200mg/400mg QD vs Diclofenac TID en AS durante 12 semanas; confirma resultados de ensayo previo en condiciones reales de uso poscomercialización |
| [NCT01934933](https://clinicaltrials.gov/study/NCT01934933) | Fase 4 | Completado | 150 | Etanercept + Celecoxib vs monoterapias en AS activa; aleatorizado 1:1:1, evaluación de valor añadido del AINE mediante MRI (score SPARCC de articulación sacroilíaca) |
| [NCT02758782](https://clinicaltrials.gov/study/NCT02758782) | Fase 4 | Completado | 156 | Ensayo CONSUL: Celecoxib + Golimumab vs Golimumab solo; impacto sobre progresión estructural espinal en axSpA radiográfica a 2 años |
| [NCT02456363](https://clinicaltrials.gov/study/NCT02456363) | Fase 2 | Desconocido | 300 | Registro anti-TNF en AS con NSAIDs como tratamiento de fondo; datos de seguridad y eficacia combinada en mundo real |
| [NCT04115098](https://clinicaltrials.gov/study/NCT04115098) | Fase 2 | Terminado | 42 | Comparación de COX-2 selectivos vs no selectivos en axSpA mediante diseño N-of-1; calidad de vida, actividad de enfermedad y proteómica predictiva |
| [NCT03190603](https://clinicaltrials.gov/study/NCT03190603) | Fase 4 | Completado | 12 | Efecto de NSAIDs sobre lesiones inflamatorias en axSpA por MRI; evaluación del control de inflamación sacroilíaca y prevención de anquilosis |
| [NCT01572675](https://clinicaltrials.gov/study/NCT01572675) | N/A | Completado | 547 | Estudio poscomercialización de Celecoxib (Celebrex®) y Etoricoxib (Arcoxia®) en práctica clínica habitual en Francia; patrones de uso en mundo real |
| [NCT03473665](https://clinicaltrials.gov/study/NCT03473665) | Fase 4 | Terminado | 9 | Ensayo piloto aleatorizado doble ciego de 4 AINEs distintos en axSpA; comparación del cambio en puntuación de dolor a semanas 4 y 6 |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39757202](https://pubmed.ncbi.nlm.nih.gov/39757202/) | 2025 | Rev. Sistemática | BMB Reports | Celecoxib es el único AINE que inhibe la progresión ósea en espondiloartritis; efecto diferenciador demostrado como independiente de la inhibición COX |
| [40911151](https://pubmed.ncbi.nlm.nih.gov/40911151/) | 2025 | Revisión Paraguas | Drugs | Síntesis de evidencia de metaanálisis y revisiones sistemáticas sobre seguridad de Celecoxib en condiciones musculoesqueléticas crónicas |
| [40028763](https://pubmed.ncbi.nlm.nih.gov/40028763/) | 2025 | Cohorte Comparativa | Scand J Rheumatol | Riesgo cardiovascular y sangrado GI comparable entre Celecoxib y nsNSAIDs en pacientes con AS; estudio de cohorte nacional retrospectivo |
| [38228361](https://pubmed.ncbi.nlm.nih.gov/38228361/) | 2024 | ECA | Ann Rheum Dis | Resultados del ensayo CONSUL: Celecoxib + anti-TNF vs anti-TNF solo sobre progresión radiológica espinal en axSpA radiográfica a 2 años |
| [36800138](https://pubmed.ncbi.nlm.nih.gov/36800138/) | 2023 | ECA | Clin Rheumatol | Celecoxib en axSpA modifica marcadores de metabolismo óseo y angiogénesis en articulación sacroilíaca; correlación con eficacia clínica |
| [28626213](https://pubmed.ncbi.nlm.nih.gov/28626213/) | 2017 | ECA | Med Sci Monit | Celecoxib vs Imrecoxib en axSpA a semana 4 y 12; correlación de scores radiológicos con niveles séricos de DKK-1 (marcador inhibidor de osificación) |
| [16960941](https://pubmed.ncbi.nlm.nih.gov/16960941/) | 2006 | ECA | J Rheumatol | Celecoxib es eficaz y bien tolerado en el tratamiento de signos y síntomas de espondilitis anquilosante; primer ensayo clínico dedicado |
| [22141388](https://pubmed.ncbi.nlm.nih.gov/22141388/) | 2011 | Revisión | Drugs | Celecoxib en OA, RA y AS: revisión comprehensiva de eficacia sintomática, perfil gastrointestinal y cardiovascular tras una década de uso |
| [27603385](https://pubmed.ncbi.nlm.nih.gov/27603385/) | 2016 | Caso-Control | Medicine | Celecoxib y sulfasalazina asociados negativamente con enfermedad coronaria en pacientes con AS; análisis de base de datos nacional de salud de Taiwán (n=4.829) |
| [17983259](https://pubmed.ncbi.nlm.nih.gov/17983259/) | 2007 | Revisión | Drugs | Celecoxib aprobado en múltiples países para OA, RA, JRA, AS y dolor agudo; revisión de una década de uso clínico y perfil de seguridad |

---

## Información de Mercado en Colombia

Celecoxib **no cuenta con registros sanitarios activos en Colombia** según los datos disponibles. No existe ningún producto comercializado con este principio activo en el mercado local a la fecha de corte (2026-05-06). Para comercializar Celecoxib en Colombia bajo cualquier indicación, se requiere iniciar un proceso formal de registro sanitario ante el INVIMA.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Cuatro ensayos clínicos de Fase 3/4 completados (incluyendo dos de Fase 3 con un total de 698 participantes) y evidencia de revisiones sistemáticas recientes (2025) confirman la eficacia y seguridad de Celecoxib en espondilopatía inflamatoria/espondilitis anquilosante. La predicción TxGNN tiene un sólido respaldo empírico; el principal obstáculo no es la evidencia clínica sino la **ausencia total de registro sanitario en Colombia**, que debe resolverse antes de cualquier avance comercial.

**Para avanzar se necesita:**
- Obtener datos completos del mecanismo de acción (consultar DrugBank API, resolver Data Gap DG002)
- Descargar y analizar el prospecto oficial para documentar advertencias de caja negra, contraindicaciones e interacciones farmacológicas (resolver Data Gap DG001)
- Iniciar proceso de registro sanitario ante INVIMA Colombia con la indicación prioritaria: espondilitis anquilosante / espondilopatía inflamatoria
- Revisar posicionamiento competitivo frente a AINEs no selectivos ya disponibles en el mercado colombiano (naproxeno, diclofenaco, ibuprofeno)
- Establecer plan de farmacovigilancia local para monitoreo de eventos cardiovasculares y gastrointestinales en la población colombiana
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

