---
layout: default
title: Vortioxetine
parent: Solo Predicción del Modelo (L5)
nav_order: 665
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Vortioxetine: nueva indicación predicha, Trastorno neurótico (neurotic disorder) (nivel de evidencia L5). Indicación original: VORTIOXETINA"
monitor_inn: "vortioxetine"
predicted_indications: ["benign paroxysmal torticollis of infancy"]
---

# Vortioxetine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Vortioxetina: De Vortioxetina (Antidepresivo) a Neurosis Depresiva / Trastorno Neurótico

## Resumen en Una Frase

Vortioxetina es un antidepresivo multimodal, registrado en Colombia bajo la denominación "VORTIOXETINA" y utilizado en el trastorno depresivo mayor.
El modelo TxGNN predice que podría ser efectivo para **trastorno neurótico** (primera predicción, puntaje 99.24%), pero la evidencia directa es mínima: **0 ensayos clínicos** y **1 publicación** vinculados a esa predicción.
Las predicciones siguientes (neurosis depresiva, melancolía, distimia) son en realidad reetiquetados o subpoblaciones de la depresión ya aprobada, no reposicionamientos genuinos.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | VORTIOXETINA (el registro no detalla una indicación específica) |
| Nueva Indicación Predicha | Trastorno neurótico (neurotic disorder) |
| Puntaje de Predicción TxGNN | 99.24% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la literatura revisada, vortioxetina es un antidepresivo con actividad multimodal: inhibe el transportador de serotonina (SERT) y modula los receptores 5-HT1A (agonista), 5-HT1B (agonista parcial), 5-HT1D, 5-HT3 y 5-HT7 (antagonistas). Esto aumenta la neurotransmisión serotoninérgica, noradrenérgica, dopaminérgica, colinérgica, histaminérgica y glutamatérgica.

"Trastorno neurótico" es una categoría diagnóstica antigua y amplia que se solapa con los trastornos depresivos y de ansiedad. El puntaje alto del modelo probablemente refleja ese solapamiento con la indicación aprobada (depresión mayor), y no existe evidencia mecanística directa para esta etiqueta específica.

Lo mismo ocurre con las otras predicciones de la lista:
- **Neurosis depresiva** (99.09%): término histórico que corresponde en gran parte a la distimia y la depresión mayor no melancólica. Es un reetiquetado de una indicación existente.
- **Melancolía** (99.09%): subtipo grave de depresión mayor. Los ensayos disponibles se realizaron en poblaciones con depresión mayor general, no en cohortes melancólicas.
- **Tortícolis paroxística benigna de la infancia** (99.07%): sin vínculo mecanístico identificable; parece un artefacto del grafo, y el uso de antidepresivos en lactantes plantearía serias preocupaciones de seguridad.
- **Trastorno distímico** (99.02%): condición depresiva crónica y leve, adyacente a la depresión mayor, con solo evidencia indirecta.

---

## Evidencia de Ensayos Clínicos

Para la predicción principal (trastorno neurótico) actualmente no hay ensayos clínicos relacionados registrados.

A modo de referencia, se muestran los ensayos vinculados a la predicción de **melancolía**, todos realizados en depresión mayor (no específicos del subtipo melancólico):

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01163266](https://clinicaltrials.gov/study/NCT01163266) | Fase 3 | Completado | 462 | Placebo-controlado, doble ciego; dosis fijas de 10 y 20 mg en depresión mayor aguda |
| [NCT01153009](https://clinicaltrials.gov/study/NCT01153009) | Fase 3 | Completado | 614 | Placebo-controlado con duloxetina como referencia; dosis de 15 y 20 mg |
| [NCT00735709](https://clinicaltrials.gov/study/NCT00735709) | Fase 3 | Completado | 560 | Placebo-controlado; 3 dosis fijas en depresión mayor aguda |
| [NCT01255787](https://clinicaltrials.gov/study/NCT01255787) | Fase 2/3 | Completado | 600 | Estudio de rango de dosis, placebo-controlado |
| [NCT01152996](https://clinicaltrials.gov/study/NCT01152996) | Fase 3 | Completado | 1075 | Extensión abierta a largo plazo; seguridad y tolerabilidad (15 y 20 mg) |
| [NCT00707980](https://clinicaltrials.gov/study/NCT00707980) | Fase 3 | Completado | 836 | Extensión abierta a largo plazo; seguridad y tolerabilidad (también vinculado a distimia) |

---

## Evidencia de Literatura

**Trastorno neurótico** (1 publicación):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31006795](https://pubmed.ncbi.nlm.nih.gov/31006795/) | 2019 | Revisión / reporte de caso | Zhurnal nevrologii i psikhiatrii | Caso de depresión neurótica; ventajas de combinar antidepresivos con psicoterapia cognitivo-conductual (no es específico de vortioxetina) |

**Neurosis depresiva y melancolía** (literatura sobre depresión mayor, selección):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [29477251](https://pubmed.ncbi.nlm.nih.gov/29477251/) | 2018 | Metaanálisis en red | Lancet | Eficacia y aceptabilidad comparativas de 21 antidepresivos en depresión mayor aguda |
| [38957929](https://pubmed.ncbi.nlm.nih.gov/38957929/) | 2024 | Metaanálisis dosis-respuesta de ECA | Psychiatry Clin Neurosci | Relación dosis-respuesta de vortioxetina en depresión del adulto |
| [36253442](https://pubmed.ncbi.nlm.nih.gov/36253442/) | 2023 | Metaanálisis en red | Mol Psychiatry | Antidepresivos en la fase de mantenimiento de la depresión mayor |
| [25016186](https://pubmed.ncbi.nlm.nih.gov/25016186/) | 2015 | Revisión | Pharmacol Ther | Datos preclínicos y clínicos de vortioxetina; perfil multimodal |
| [29189941](https://pubmed.ncbi.nlm.nih.gov/29189941/) | 2018 | Revisión | Clin Pharmacokinet | Farmacocinética lineal, vida media ~66 h, biodisponibilidad 75% e interacciones |
| [37424409](https://pubmed.ncbi.nlm.nih.gov/37424409/) | 2023 | Revisión | Clin Psychopharmacol Neurosci | Anhedonia como síntoma central de la depresión y factor de riesgo suicida |
| [34029378](https://pubmed.ncbi.nlm.nih.gov/34029378/) | 2021 | Metaanálisis en red | Cochrane | Antidepresivos de nueva generación en niños y adolescentes |
| [37032427](https://pubmed.ncbi.nlm.nih.gov/37032427/) | 2023 | Guía farmacogenética | Clin Pharmacol Ther | Guía CPIC sobre genotipos (CYP2D6, CYP2C19, etc.) y antidepresivos |

Estas publicaciones respaldan la eficacia de vortioxetina en depresión mayor, no en las etiquetas predichas.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20215225 | ACSODIX® 10MG COMPRIMIDOS RECUBIERTOS (TABLETAS RECUBIERTAS) | Tableta recubierta (vía oral) | VORTIOXETINA | Cancelado |

El único registro (titular: MEGALABS COLOMBIA S.A.S) está cancelado; actualmente no hay registros vigentes.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 151 interacciones en total. Las de nivel **Mayor** incluyen:
  - Bupropión
  - Lorcaserina
  - Dietilpropión
  - Fentermina
  - Dolasetrón
  - Palonosetrón

  Entre las de nivel **Moderado** figuran morfina, ácido acetilsalicílico, dexametasona, clorpropamida, glimepirida, eliglustat, picosulfato, polietilenglicol con electrolitos, sulfato de sodio e insulinas (aspart, degludec, detemir, glargina, glulisina).
- **Perfil de efectos adversos (literatura)**: la literatura revisada describe efectos adversos gastrointestinales, hiperhidrosis y disfunción sexual como efectos frecuentes de los antidepresivos de segunda generación.
- **Poblaciones especiales**: el uso en lactantes (relevante para la predicción de tortícolis paroxística) plantearía serias preocupaciones de seguridad.

Consultar el prospecto para advertencias y contraindicaciones, que no están disponibles en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal (trastorno neurótico) tiene nivel de evidencia L5: solo una publicación indirecta, sin ensayos clínicos, y se trata de una categoría diagnóstica obsoleta que se solapa con la depresión ya aprobada. Las predicciones con mayor respaldo (neurosis depresiva y melancolía, nivel L1 por la evidencia en depresión mayor) corresponden a reetiquetados o subpoblaciones de la indicación existente, no a un reposicionamiento genuino. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Aclarar si se busca realmente reposicionamiento o solo mapear etiquetas históricas a la indicación vigente (depresión mayor y distimia).
- Estudios específicos de subtipo (melancolía) o de distimia con vortioxetina, ya que los ensayos actuales son en depresión mayor general.
- Datos del mecanismo de acción verificados en DrugBank.
- Descargar y analizar el prospecto en INVIMA para obtener advertencias y contraindicaciones.
- Aclarar el motivo de la cancelación del registro 20215225 y evaluar si existe otro registro vigente o una vía de nuevo registro.
- Descartar la predicción de tortícolis paroxística benigna de la infancia por falta de plausibilidad y por riesgo de seguridad.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

