---
layout: default
title: Pazopanib
parent: Evidencia Moderada (L3-L4)
nav_order: 502
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-14
description: "Pazopanib: nueva indicación predicha, Carcinoma de células renales no clasificado (nivel de evidencia L3). Indicación original: PAZOPANIB"
monitor_inn: "pazopanib"
predicted_indications: ["fibroblastic neoplasm"]
---

# Pazopanib
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **10** 
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

# Pazopanib: De Pazopanib (indicación sin detallar en el registro) a Carcinoma de Células Renales No Clasificado

## Resumen en Una Frase

Pazopanib es un inhibidor de tirosina quinasa multidiana (VEGFR, PDGFR, c-KIT) cuyo registro sanitario colombiano solo menciona el nombre del principio activo, sin detallar la indicación; en la práctica clínica se usa en carcinoma renal avanzado y en sarcomas de tejidos blandos.
El modelo TxGNN predice que podría ser efectivo para el **carcinoma de células renales no clasificado**, con **0 ensayos clínicos** y **6 publicaciones** que actualmente respaldan esta dirección.

> Nota: la predicción de mayor rango (carcinoma renal asociado a translocaciones Xp11.2/TFE3) no tiene evidencia recuperada. Se presenta como foco principal la tercera predicción, que es la primera con evidencia publicada. Además, **liposarcoma** es la predicción con mayor respaldo clínico (6 ensayos y 20 publicaciones) y se resume en la sección final.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | PAZOPANIB (el registro no detalla la indicación) |
| Nueva Indicación Predicha | Carcinoma de células renales no clasificado |
| Puntaje de Predicción TxGNN | 99.63% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 3 (todos cancelados) |
| Decisión Recomendada | Hold (la evidencia es retrospectiva; la categoría de la predicción es "pregunta de investigación") |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según el conocimiento general, pazopanib inhibe VEGFR-1/2/3, PDGFR y c-KIT, bloqueando la angiogénesis tumoral. Su eficacia está establecida en carcinoma renal de células claras avanzado.

El carcinoma renal no clasificado pertenece al grupo de carcinomas renales de células no claras. Estos tumores comparten, en parte, una biología dependiente de la angiogénesis con el subtipo de células claras, por lo que la inhibición de la vía VEGF/PDGF es mecanísticamente plausible.

Las series retrospectivas multicéntricas y un estudio de brazo único sugieren actividad en células no claras. Sin embargo, no hay evidencia aleatorizada en los datos disponibles, y la fase y los resultados del estudio de brazo único no se verificaron.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta indicación.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [28546525](https://pubmed.ncbi.nlm.nih.gov/28546525/) | 2018 | Estudio de brazo único, abierto, multicéntrico (reportado como fase II) | Cancer Res Treat | Evalúa eficacia y seguridad de pazopanib en carcinoma renal metastásico de células no claras |
| [28108284](https://pubmed.ncbi.nlm.nih.gov/28108284/) | 2017 | Cohorte retrospectiva multicéntrica | Clin Genitourin Cancer | Estudio italiano PANORAMA: eficacia y toxicidad de pazopanib de primera línea en células no claras |
| [27568124](https://pubmed.ncbi.nlm.nih.gov/27568124/) | 2017 | Cohorte retrospectiva | Clin Genitourin Cancer | Resultados de pacientes con carcinoma renal metastásico de células no claras tratados con pazopanib |
| [31921344](https://pubmed.ncbi.nlm.nih.gov/31921344/) | 2019 | Evidencia del mundo real | Ecancermedicalscience | Compara sunitinib y pazopanib de primera línea en células no claras y sarcomatoide |
| [41558869](https://pubmed.ncbi.nlm.nih.gov/41558869/) | 2026 | Cohorte retrospectiva | Eur Urol Oncol | Resultados de terapias de primera línea contemporáneas y tradicionales en células no claras (consorcio IMDC) |
| [30268423](https://pubmed.ncbi.nlm.nih.gov/30268423/) | 2019 | Cohorte | Clin Genitourin Cancer | Carcinoma de origen primario desconocido con características de carcinoma renal metastásico tratado con terapia dirigida |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20248619 | REDPANIB® 400 MG (cancelado) | Tableta recubierta | PAZOPANIB |
| 20248583 | REDPANIB® 200 MG (cancelado) | Tableta recubierta | PAZOPANIB |
| 20024562 | VOTRIENT® 200 MG (cancelado) | Tableta recubierta | PAZOPANIB |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasa multidiana), no citotóxico convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar el prospecto; en general se vigilan hemograma, función hepática y renal, presión arterial, función tiroidea y electrocardiograma (QT) |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no proviene del prospecto)**: hipertensión, síndrome de QT largo y torsades de pointes, insuficiencia hepática y lesión hepática inducida por fármacos, hipotiroidismo, infarto de miocardio, hiperbilirrubinemia (incluido síndrome de Gilbert), úlcera péptica activa, hemorragia intracerebral, pancreatitis, proteinuria, enfermedad diarreica, entre otras.
- **Interacciones farmacológicas**: se identificaron 519 interacciones. Entre las de nivel **mayor** destacan los antiácidos y supresores de ácido (famotidina, ranitidina, cimetidina, omeprazol, esomeprazol, rabeprazol, dexlansoprazol), claritromicina y dolasetrón. Entre las de nivel moderado: pioglitazona, loperamida, aprepitant, dexametasona, budesonida, saxagliptina, eliglustat, bisacodilo, óxido de magnesio y polietilenglicol.

Para advertencias y contraindicaciones del prospecto, consultar el prospecto, ya que no se dispone de ese texto.

---

## Otras Predicciones con Evidencia Relevante

| Indicación | Puntaje | Nivel | Evidencia | Recomendación |
|------|------|------|------|------|
| Liposarcoma | 99.59% | L2 | 6 ensayos (p. ej., [NCT01506596](https://clinicaltrials.gov/study/NCT01506596) fase 2 completado, n=42; [NCT01692496](https://clinicaltrials.gov/study/NCT01692496) fase 2 completado, n=52) y 20 publicaciones | Proceed with Guardrails |
| Neoplasia fibroblástica | 99.35% | L2 | 2 ensayos (p. ej., [NCT02066285](https://clinicaltrials.gov/study/NCT02066285) fase 2, n=96) y 20 publicaciones | Pregunta de investigación |
| Dermatofibrosarcoma protuberans | 99.29% | L2 | 4 ensayos (p. ej., [NCT01059656](https://clinicaltrials.gov/study/NCT01059656) fase 2, terminado, n=23) y 14 publicaciones, incluido el estudio fase II [32956651](https://pubmed.ncbi.nlm.nih.gov/32956651/) | Pregunta de investigación |

Las demás predicciones (carcinoma renal con translocaciones Xp11.2/TFE3, carcinoma renal asociado a neuroblastoma, carcinoma renal infantil, liposarcoma mixoide ovárico, fibrosarcoma cardíaco y fibrosarcoma renal) no tienen ensayos ni literatura y se mantienen en nivel L5 (solo predicción del modelo).

En liposarcoma, el beneficio parece modesto y dependiente del subtipo: los subtipos adipocíticos se excluyeron del ensayo pivotal PALETTE por falta de señal de beneficio.

---

## Conclusión y Próximos Pasos

**Decisión: Hold** (para carcinoma renal no clasificado)

**Justificación:**
La evidencia disponible es retrospectiva y de brazo único (nivel L3), sin ensayos clínicos registrados ni datos aleatorizados. Además, todos los registros sanitarios en Colombia están cancelados y no hay datos de seguridad del prospecto. Entre las predicciones, liposarcoma (L2, "Proceed with Guardrails") es la que tiene respaldo clínico más sólido, con uso limitado a pacientes seleccionados y estratificación por subtipo.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA para obtener advertencias y contraindicaciones (brecha de datos bloqueante para el cribado de seguridad).
- Obtener el mecanismo de acción desde DrugBank.
- Verificar la fase y los resultados del estudio de brazo único (PMID 28546525) y revisar los estudios retrospectivos en detalle.
- Aclarar la situación regulatoria: no hay registros vigentes en Colombia, por lo que habría que gestionar un nuevo registro o una vía alternativa.
- Evaluar la seguridad cardiovascular, hepática y las interacciones con inhibidores de la bomba de protones y antagonistas H2.
- Para liposarcoma: definir subtipos elegibles y un plan de monitoreo antes de cualquier avance.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

