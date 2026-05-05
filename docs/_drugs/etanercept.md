---
layout: default
title: Etanercept
parent: 僅模型預測 (L5)
nav_order: 72
evidence_level: L5
indication_count: 6
---

# Etanercept
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

Usando `txgnn-pipeline` para guiar la generación del informe de reposicionamiento. Procedo ahora a redactar el informe completo basado en el Evidence Pack proporcionado.

---

# Etanercept: De Artritis Reumatoide a Vasculitis Reumatoide

## Resumen en Una Frase

Etanercept (Enbrel) es una proteína de fusión del receptor p75 de TNF-α, ampliamente utilizada a nivel internacional para el tratamiento de la artritis reumatoide, artritis psoriásica, espondilitis anquilosante y artritis idiopática juvenil, aunque actualmente no cuenta con registros sanitarios activos en Colombia.
El modelo TxGNN predice que podría ser efectivo para la **Vasculitis Reumatoide**, una de las manifestaciones extraarticulares más graves de la AR,
con **1 ensayo clínico interventivo directo** (Fase 1/2 en vasculitis sistémica ANCA+, completado) y **20 publicaciones** que respaldan esta dirección — aunque la evidencia revela una dualidad crítica: el fármaco puede tanto tratar como paradójicamente inducir vasculitis.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Artritis reumatoide (indicación reconocida internacionalmente; sin registro activo en Colombia) |
| Nueva Indicación Predicha | Vasculitis Reumatoide |
| Puntaje de Predicción TxGNN | 99.71% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Etanercept es una proteína de fusión dimérica compuesta por el dominio extracelular del receptor p75 de TNF-α (TNFR2) ligado a la fracción Fc de IgG1 humana. Actúa como receptor señuelo soluble que captura TNF-α soluble y unido a membrana, impidiendo su interacción con los receptores celulares y bloqueando la cascada inflamatoria mediada por NF-κB. Si bien no se dispone de datos detallados del mecanismo de acción en el presente paquete de evidencia (Data Gap en MOA), la acción anti-TNF-α de etanercept es ampliamente documentada en la literatura y constituye la base de su eficacia en múltiples enfermedades inflamatorias articulares.

La vasculitis reumatoide (VR) es una complicación extraarticular grave de la AR de larga evolución, caracterizada por inflamación necrotizante de los vasos sanguíneos. El TNF-α se expresa de forma marcadamente elevada en las lesiones vasculares, promoviendo la adhesión leucocitaria, la activación del endotelio y el daño orgánico sistémico. Desde una perspectiva mecanística, el bloqueo de TNF-α resulta teóricamente atractivo: al suprimir esta citocina pivotal se podría controlar la inflamación vascular de forma análoga a su efecto sobre la sinovitis en AR.

Sin embargo, existe una paradoja clínica documentada que representa la mayor preocupación de seguridad de esta indicación: múltiples publicaciones —incluyendo estudios de cohorte, series de casos y reportes individuales— registran que los inhibidores de TNF-α, incluyendo etanercept, pueden **inducir paradójicamente vasculitis cutánea y sistémica**. El mecanismo propuesto involucra la sobrexpresión de interferón-α, la formación de autoanticuerpos (ANA, anti-dsDNA) y la deposición de inmunocomplejos en la pared vascular. Esta dualidad terapéutica-adversa exige una evaluación de seguridad prioritaria antes de cualquier avance en esta indicación.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00001901](https://clinicaltrials.gov/study/NCT00001901) | Fase 1/2 | Completado | 60 | Único ensayo interventivo directo: evaluación de etanercept (TNFR:Fc) en granulomatosis de Wegener (vasculitis sistémica ANCA+). Comparado con prednisona + agente citotóxico como estándar. Es la evidencia interventiva más relevante disponible para esta indicación, aunque de grado Fase 1/2. |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Fase 2 | Aún no reclutando | 80 | Manejo perioperatorio de inmunosupresores en pacientes reumatológicos sometidos a artroplastia total de hombro; no específico para vasculitis, relevancia indirecta para manejo de biológicos en contexto quirúrgico. |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completado | 184 | Estudio observacional multicéntrico de tocilizumab en AR con respuesta inadecuada a DMARDs o un biológico; evalúa patrones de práctica clínica en AR, sin enfoque en subgrupo de vasculitis. |
| [NCT01557322](https://clinicaltrials.gov/study/NCT01557322) | N/A | Completado | 1,754 | Características basales y rutas de tratamiento en AR moderada en práctica real (cohorte etanercept vs. terapias no biológicas, BSRBR); sin enfoque específico en vasculitis. |
| [NCT02590562](https://clinicaltrials.gov/study/NCT02590562) | N/A | Completado | 808 | Estudio transversal de patrones de uso de bDMARDs en AR en China; no específico para vasculitis reumatoide. |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Desconocido | 750,000 | Gran estudio observacional sobre incidencia de enfermedades inflamatorias inmunomediadas en pacientes tratados con biológicos; proporciona contexto de riesgo de comorbilidades autoinmunes, relevancia indirecta. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33058033](https://pubmed.ncbi.nlm.nih.gov/33058033/) | 2021 | Revisión Sistemática | Clinical Rheumatology | Revisión PRISMA del uso de fármacos biológicos en vasculitis reumatoide; evalúa el arsenal terapéutico biológico disponible incluyendo agentes anti-TNF, con resultados de morbilidad y mortalidad. |
| [28391344](https://pubmed.ncbi.nlm.nih.gov/28391344/) | 2017 | Revisión | Nephrology, Dialysis, Transplantation | Analiza el rol potencial del bloqueo de TNF-α en vasculitis asociada a ANCA y glomerulonefritis; documenta evidencia de TNF-α en la patofisiología de la enfermedad vascular. |
| [28123776](https://pubmed.ncbi.nlm.nih.gov/28123776/) | 2017 | Estudio de Cohorte | RMD Open | Compara el riesgo de eventos tipo lupus y tipo vasculitis en pacientes con AR tratados con TNFi vs. nbDMARDs (registro BSRBR-RA); datos cuantitativos de riesgo farmacoespecífico. |
| [15468348](https://pubmed.ncbi.nlm.nih.gov/15468348/) | 2004 | Revisión | Journal of Rheumatology | Revisa el riesgo de vasculitis asociado al bloqueo de TNF-α; debate el perfil de seguridad y los mecanismos de vasculitis inducida por anti-TNF. |
| [15853915](https://pubmed.ncbi.nlm.nih.gov/15853915/) | 2005 | Serie de Casos | Scandinavian Journal of Immunology | Caracterización inmunológica de vasculitis cutánea asociada a etanercept e infliximab; propone el mecanismo de autoinmunidad inducida por inhibición de TNF. |
| [12209493](https://pubmed.ncbi.nlm.nih.gov/12209493/) | 2002 | Reporte de Caso | Arthritis and Rheumatism | Nodulosis acelerada y vasculitis tras terapia con etanercept en AR; una de las primeras alertas documentadas sobre el efecto paradójico del anti-TNF. |
| [31632872](https://pubmed.ncbi.nlm.nih.gov/31632872/) | 2019 | Reporte de Caso | Cureus | Nefropatía asociada a etanercept con formación de autoanticuerpos y vasculitis renal; describe el mecanismo de autoinmunidad sistémica inducida por inhibidores de TNF-α. |
| [41327089](https://pubmed.ncbi.nlm.nih.gov/41327089/) | 2025 | Reporte de Caso | BMC Nephrology | Caso de AR con desarrollo secuencial de nefropatía membranosa y vasculitis asociada a ANCA; destaca el papel del uso creciente de biológicos en la aparición de nefropatía. |
| [15801034](https://pubmed.ncbi.nlm.nih.gov/15801034/) | 2005 | Reporte de Caso | Journal of Rheumatology | Nefritis lúpica proliferativa y vasculitis leucocitoclástica durante tratamiento con etanercept; documenta una manifestación paradójica grave con implicaciones de seguridad relevantes. |
| [25544845](https://pubmed.ncbi.nlm.nih.gov/25544845/) | 2014 | Reporte de Caso | Case Reports in Medicine | Vasculitis de grandes vasos en paciente con AR bajo terapia anti-TNF; describe clasificación como vasculitis inducida por agente biológico y debate el manejo clínico. |

---

## Información de Mercado en Colombia

Etanercept actualmente **no cuenta con registros sanitarios activos ante el INVIMA en Colombia**. No se encontraron licencias registradas para ninguna indicación, forma farmacéutica o fabricante.

> No hay registros sanitarios de etanercept disponibles en Colombia a la fecha de corte (2026-05-05).

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

> **Nota clínica relevante derivada de la literatura:** Aunque los datos formales de seguridad (advertencias y contraindicaciones del prospecto) no están disponibles en este paquete de evidencia, múltiples publicaciones indexadas documentan que etanercept puede **inducir paradójicamente vasculitis cutánea y sistémica**, así como nefritis lúpica y vasculitis asociada a ANCA. Este hallazgo es de especial relevancia para la indicación evaluada y debe considerarse prioritario en cualquier evaluación beneficio-riesgo.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia disponible revela una paradoja clínica que impide recomendar el avance: aunque el mecanismo anti-TNF-α es teóricamente aplicable a la vasculitis reumatoide, el único ensayo interventivo directo es de Fase 1/2 (insuficiente para establecer eficacia neta), y múltiples publicaciones —incluyendo estudios de cohorte y series de casos— documentan que etanercept puede **inducir** vasculitis paradójica a través de sobrexpresión de interferón-α y deposición de inmunocomplejos. Adicionalmente, la ausencia total de registros sanitarios en Colombia y la falta de datos de seguridad locales formales impiden pasar la evaluación inicial de seguridad (Etapa S1).

**Para avanzar se necesita:**
- Recuperar y analizar los datos de MOA completos desde DrugBank (remediation DG002) y las advertencias/contraindicaciones del prospecto oficial (remediation DG001)
- Obtener y revisar en detalle los resultados publicados del ensayo NCT00001901 (Fase 1/2 en granulomatosis de Wegener, n=60)
- Realizar una revisión sistemática que diferencie cuantitativamente el uso terapéutico de la vasculitis inducida por etanercept, con datos de incidencia comparativa
- Consultar con especialistas en reumatología para definir el perfil de paciente (VR severa vs. leve, ANCA+ vs. ANCA-) que podría beneficiarse neto del tratamiento
- Antes de cualquier uso, tramitar el registro sanitario ante INVIMA con la indicación correspondiente
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

