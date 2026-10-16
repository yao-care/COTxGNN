---
layout: default
title: Bismuth Subsalicylate
parent: Solo Predicción del Modelo (L5)
nav_order: 109
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Bismuth Subsalicylate: nueva indicación predicha, Paratifoidea (fiebre paratifoidea) (nivel de evidencia L5). Indicación original: Subcitrato de bismuto / Subsalicilato de bismuto"
---

# Bismuth Subsalicylate
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Subsalicilato de Bismuto: De Trastornos Gastrointestinales a Paratifoidea

## Resumen en Una Frase

El subsalicilato de bismuto está registrado en Colombia como producto de bismuto de uso oral (suspensión y tableta masticable), y se emplea clásicamente en trastornos digestivos.
El modelo TxGNN predice que podría ser efectivo para **paratifoidea (fiebre paratifoidea)**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta indicación específica; se trata solo de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Subcitrato de bismuto / Subsalicilato de bismuto (según el texto del registro INVIMA) |
| Nueva Indicación Predicha | Paratifoidea (fiebre paratifoidea) |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registro vigente) |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, el subsalicilato de bismuto es una sal de bismuto poco soluble en agua, usada para trastornos gastrointestinales, con actividad antisecretora y antibacteriana frente a patógenos entéricos. Mecanísticamente, esto podría relacionarse con infecciones entéricas por *Salmonella*.

La paratifoidea es una infección sistémica por *Salmonella*. Un agente de acción local en el intestino difícilmente sería suficiente, ya que el tratamiento requiere antibióticos sistémicos. El alto puntaje del modelo no está respaldado por evidencia en los datos compilados y debe interpretarse con cautela.

### Otras predicciones del modelo (para contexto)

| Posición | Enfermedad | Puntaje TxGNN | Nivel de Evidencia | Recomendación |
|------|------|------|------|------|
| 2 | Esclerodermia difusa | 99.96% | L5 | Hold |
| 3 | Salmonelosis | 99.95% | L4 | Pregunta de investigación |
| 4 | Fiebre tifoidea | 99.92% | L5 | Hold |
| 5 | Conjuntivitis | 99.92% | L5 | Hold |
| 6 | Fiebre recurrente | 99.85% | L5 | Hold |
| 7 | Conjuntivitis contagiosa aguda | 99.84% | L5 | Hold |
| 8 | Gingivitis | 99.75% | L4 | Pregunta de investigación |
| 9 | Queratoconjuntivitis epitelial punteada | 99.74% | L5 | Hold |
| 10 | Otitis externa | 99.68% | L5 | Hold |

Las predicciones con algo de respaldo indirecto son la **salmonelosis** (estudio in vitro que muestra que el subsalicilato de bismuto se une a bacterias y las mata) y la **gingivitis** (estudios preclínicos con nanopartículas y membranas dentales). La esclerodermia difusa carece de un fundamento mecanístico claro y probablemente sea un artefacto del grafo.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para paratifoidea.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para paratifoidea.

Como referencia, la literatura disponible para la predicción cercana de **salmonelosis** es la siguiente:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [2694949](https://pubmed.ncbi.nlm.nih.gov/2694949/) | 1989 | Estudio in vitro | Antimicrob Agents Chemother | El subsalicilato de bismuto se une a bacterias de diversas especies y las mata; reducción de 4 log10 de *E. coli* en 4 horas |
| [3893119](https://pubmed.ncbi.nlm.nih.gov/3893119/) | 1985 | Revisión | Am J Med | Como agente antisecretor, reduce el número de deposiciones en cerca de 50% en diarrea aguda |
| [2655632](https://pubmed.ncbi.nlm.nih.gov/2655632/) | 1989 | Revisión | Annu Rev Public Health | Control de enfermedades diarreicas (evidencia indirecta) |
| [1760758](https://pubmed.ncbi.nlm.nih.gov/1760758/) | 1991 | Revisión veterinaria | Vet Clin North Am Food Anim Pract | Manejo de diarrea en terneros neonatos; menciona antisecretores como el subsalicilato de bismuto |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1991423 (cancelado) | BISBACTER® SUSPENSION | Suspensión oral | Bismuto subcitrato |
| 20248335 (cancelado) | BISMUCAR® TABLETAS | Tableta masticable | Subsalicilato de bismuto |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: el grafo de conocimiento asocia el fármaco con las siguientes enfermedades como contraindicación: insuficiencia hepática, enfermedad hepática, enfermedad renal, epilepsia, enfermedad de la vesícula biliar, diabetes mellitus, cetoacidosis diabética, neutropenia, agranulocitosis, gota, enfermedad del sistema nervioso periférico, neuropatía periférica, abuso/dependencia de sustancias, trastornos de la coagulación, colitis por *Clostridium difficile*, enterocolitis necrosante perinatal, enfermedad cerebral, meningitis no infecciosa y piouréter.
- **Interacciones Farmacológicas**: se identificaron 64 interacciones; las 20 mostradas son de nivel moderado. Las principales corresponden a:
  - **Tetraciclinas**: doxiciclina, tetraciclina, minociclina.
  - **Antidiabéticos e insulinas**: clorpropamida, glimepirida, glipizida, gliburida, tolazamida, repaglinida, nateglinida, y varias insulinas (aspart, degludec, detemir, glargina, glulisina, humana isófana, regular e inhalada).
  - **Otros**: morfina y fenfluramina.
- El componente salicilato implica exposición sistémica a salicilatos, relevante en pacientes con diabetes, alteración de la coagulación, enfermedad renal o hepática.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de paratifoidea se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura. Además, es una infección sistémica que requiere antibióticos, por lo que un agente de acción local es poco plausible. Actualmente tampoco hay registro sanitario vigente en Colombia.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) del subsalicilato de bismuto.
- Información del prospecto (advertencias y contraindicaciones) obtenida de INVIMA, para completar el análisis de seguridad.
- Evidencia clínica o preclínica específica en paratifoidea; si se busca una dirección con más sustento, priorizar **salmonelosis** (como terapia sintomática o adyuvante) o **gingivitis**, ambas en fase de pregunta de investigación (L4).
- Aclarar la situación regulatoria en Colombia (registros cancelados) y la viabilidad de una nueva comercialización.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

