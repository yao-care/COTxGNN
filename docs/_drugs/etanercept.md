---
layout: default
title: Etanercept
parent: Solo Predicción del Modelo (L5)
nav_order: 186
evidence_level: L5
indication_count: 6
---

# Etanercept
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Etanercept: De Artritis Reumatoide a Vasculitis Reumatoide

## Resumen en Una Frase

Etanercept es una proteína de fusión que bloquea el TNF-alfa. Se usa en enfermedades inflamatorias como la artritis reumatoide, la artritis idiopática juvenil, la artritis psoriásica, la espondilitis anquilosante y la psoriasis (según la literatura; el registro sanitario colombiano solo consigna el nombre del principio activo).
El modelo TxGNN predice que podría ser efectivo para **vasculitis reumatoide**, con un puntaje alto (99.71%).
Sin embargo, esta dirección está respaldada solo indirectamente: **6 ensayos clínicos** (ninguno evalúa directamente la vasculitis reumatoide) y **20 publicaciones**, muchas de las cuales describen vasculitis *asociada* al uso de etanercept.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto registrado solo dice «Etanercept»); por la literatura: artritis reumatoide y otras enfermedades inflamatorias |
| Nueva Indicación Predicha | Vasculitis reumatoide |
| Puntaje de Predicción TxGNN | 99.71% |
| Nivel de Evidencia | L3 (existe una revisión sistemática, pero es indirecta y de nivel de casos; el paquete de evidencia la calificó de forma más conservadora como L4) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la literatura, etanercept es una proteína de fusión formada por dos cadenas del receptor p75 del TNF unidas a la porción Fc de la IgG1. Se une al TNF-alfa y bloquea su actividad biológica, y su eficacia está demostrada en artritis reumatoide y otras enfermedades inflamatorias.

La vasculitis reumatoide es una de las manifestaciones extraarticulares más graves de la artritis reumatoide. Como el TNF-alfa impulsa la inflamación en la artritis reumatoide, bloquearlo es plausible en su complicación vascular. Una revisión sistemática de 2021 ya evaluó el uso de fármacos biológicos en esta enfermedad.

Aun así, la evidencia directa es débil y contradictoria:

- El único ensayo de Fase 2 con etanercept en vasculitis es en granulomatosis de Wegener, una vasculitis distinta.
- La literatura describe repetidamente vasculitis, incluida la cutánea y la asociada a ANCA, que aparece **durante** el tratamiento con etanercept.
- El puntaje alto del modelo no está respaldado por datos clínicos, y las señales de seguridad apuntan en sentido opuesto.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00001901](https://clinicaltrials.gov/study/NCT00001901) | Fase 2 | Completado | 60 | Etanercept en granulomatosis de Wegener (vasculitis sistémica relacionada, no reumatoide); evidencia indirecta |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Fase 2 | Aún sin reclutar | 80 | Manejo perioperatorio de inmunosupresores en pacientes reumatológicos con artroplastia de hombro; no evalúa eficacia en vasculitis |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completado | 184 | Estudio no intervencionista de tocilizumab en artritis reumatoide; sin desenlace de vasculitis |
| [NCT01557322](https://clinicaltrials.gov/study/NCT01557322) | N/A | Completado | 1754 | Estudio de práctica real en artritis reumatoide moderada (etanercept vs. tratamientos no biológicos); sin desenlace de vasculitis |
| [NCT02590562](https://clinicaltrials.gov/study/NCT02590562) | N/A | Completado | 808 | Estudio transversal de patrones de uso de biológicos en artritis reumatoide en China; no evalúa eficacia |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Desconocido | 750000 | Registro del riesgo de nuevas enfermedades inmunomediadas tras usar biológicos; evalúa riesgo, no eficacia |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33058033](https://pubmed.ncbi.nlm.nih.gov/33058033/) | 2021 | Revisión sistemática | Clinical Rheumatology | Revisa el uso de fármacos biológicos en la vasculitis reumatoide, una manifestación grave que requiere corticoides o inmunosupresores |
| [28391344](https://pubmed.ncbi.nlm.nih.gov/28391344/) | 2017 | Revisión | Nephrology Dialysis Transplantation | Analiza si bloquear el TNF-alfa sirve en vasculitis asociada a ANCA y glomerulonefritis |
| [15468348](https://pubmed.ncbi.nlm.nih.gov/15468348/) | 2004 | Revisión | Journal of Rheumatology | Bloqueo del TNF-alfa y riesgo de vasculitis |
| [28123776](https://pubmed.ncbi.nlm.nih.gov/28123776/) | 2017 | Cohorte | RMD Open | Compara el riesgo de eventos tipo lupus y tipo vasculitis en pacientes con artritis reumatoide tratados con anti-TNF frente a FARME no biológicos (registro BSRBR-RA) |
| [15853915](https://pubmed.ncbi.nlm.nih.gov/15853915/) | 2005 | Serie de casos | Scandinavian Journal of Immunology | Inmunología de la vasculitis cutánea asociada a etanercept e infliximab; la autoinmunidad, incluida la vasculitis, es rara pero posible |
| [12209493](https://pubmed.ncbi.nlm.nih.gov/12209493/) | 2002 | Reporte de caso | Arthritis and Rheumatism | Nodulosis acelerada y vasculitis tras etanercept en artritis reumatoide |
| [11792895](https://pubmed.ncbi.nlm.nih.gov/11792895/) | 2002 | No clasificado | Rheumatology (Oxford) | Vasculitis cutánea asociada a etanercept e infliximab |
| [15801034](https://pubmed.ncbi.nlm.nih.gov/15801034/) | 2005 | No clasificado | Journal of Rheumatology | Nefritis lúpica proliferativa y vasculitis leucocitoclástica durante el tratamiento con etanercept |
| [25544845](https://pubmed.ncbi.nlm.nih.gov/25544845/) | 2014 | No clasificado | Case Reports in Medicine | Vasculitis de grandes vasos en un paciente con artritis reumatoide bajo tratamiento anti-TNF |
| [41327089](https://pubmed.ncbi.nlm.nih.gov/41327089/) | 2025 | Reporte de caso | BMC Nephrology | Paciente con artritis reumatoide que desarrolló sucesivamente nefropatía membranosa y vasculitis asociada a ANCA |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20211583 | ALTEBREL® 50MG/ML (RTM Healthcare Private Limited) | Solución inyectable | Solo consta el nombre del principio activo («Etanercept») |
| 19978839 | ENBREL® 25 MG solución para inyección (Pfizer S.A.S.) | Solución inyectable | Solo consta el nombre del principio activo («Etanercept») |

Los datos muestran 20 registros en total; en el listado recibido solo aparecen 2 números de registro distintos, repetidos varias veces.

---

## Consideraciones de Seguridad

No hay datos de interacciones farmacológicas en el paquete de evidencia (consulta sin resultados). Consultar el prospecto para informacion de seguridad.

Señal de seguridad de la literatura: varios reportes y series de casos describen vasculitis (cutánea, de grandes vasos o asociada a ANCA), lupus inducido y nefropatía durante el tratamiento con etanercept. Esto debe pesar en contra de cualquier uso en vasculitis reumatoide.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El puntaje del modelo es muy alto (99.71%), pero ningún ensayo prueba etanercept en vasculitis reumatoide. El único estudio de Fase 2 es en otra vasculitis, y la literatura señala con frecuencia que etanercept puede provocar vasculitis. Por ahora es una pregunta de investigación, no una candidata para avanzar.

**Para avanzar se necesita:**
- Evidencia directa de etanercept en vasculitis reumatoide (series de casos comparativas o un estudio prospectivo).
- Revisar los datos de la revisión sistemática de 2021 para ver qué biológicos y con qué resultados, y separar la vasculitis reumatoide de la vasculitis paradójica inducida por anti-TNF.
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones).
- Obtener el mecanismo de acción desde DrugBank.
- Nota: en este mismo paquete, las predicciones de espondilopatía inflamatoria y de artritis reumatoide juvenil poliarticular tienen evidencia mucho más sólida (nivel L1), pero corresponden a usos ya establecidos, no a reposicionamiento nuevo.

*Este resultado es solo para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

