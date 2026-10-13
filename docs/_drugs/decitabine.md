---
layout: default
title: Decitabine
parent: Evidencia Moderada (L3-L4)
nav_order: 199
evidence_level: L4
indication_count: 1
---

# Decitabine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **1** 
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

# Decitabina: De Decitabina (indicación registrada sin detalle) a Citopenia Refractaria de la Infancia

## Resumen en Una Frase

Decitabina es un agente hipometilante (inhibidor de la ADN metiltransferasa) conocido por su uso en síndromes mielodisplásicos; en Colombia sus registros sanitarios solo mencionan el nombre del principio activo como indicación, sin describir la enfermedad.
El modelo TxGNN predice que podría ser efectiva para **citopenia refractaria de la infancia**,
con **0 ensayos clínicos** y **2 publicaciones** (un estudio de cohorte y un reporte de caso) que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Los registros solo indican "Decitabina", sin enfermedad especificada |
| Nueva Indicación Predicha | Citopenia refractaria de la infancia |
| Puntaje de Predicción TxGNN | 99.03% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registro vigente) |
| Número de Registros Sanitarios | 3 (todos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción de la decitabina. Según el conocimiento farmacológico general, es un agente hipometilante que inhibe la ADN metiltransferasa y se usa en síndromes mielodisplásicos (SMD). Esta descripción proviene de conocimiento general y no de los datos suministrados.

La citopenia refractaria de la infancia es el subtipo más común de SMD pediátrico. Ambas condiciones comparten una biología de hematopoyesis clonal con metilación aberrante del ADN, lo que ofrece una base plausible para la predicción.

El puntaje alto de TxGNN (0.99) es solo una predicción computacional y no constituye evidencia clínica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35624441](https://pubmed.ncbi.nlm.nih.gov/35624441/) | 2022 | Cohorte (probablemente retrospectivo, inferido del título) | BMC Pediatrics | Experiencia de 10 años en un centro con decitabina combinada con un régimen mínimamente mielosupresor como puente al trasplante alogénico de progenitores hematopoyéticos en SMD pediátrico |
| [42125547](https://pubmed.ncbi.nlm.nih.gov/42125547/) | 2026 | Reporte de caso | Experimental and Therapeutic Medicine | Niño de 8 años con SMD (citopenia refractaria de la infancia) no elegible para trasplante ni inmunosupresión, tratado con decitabina en monoterapia |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19991325 (cancelado) | DACOGEN ® | Polvo liofilizado para reconstituir a solución inyectable | Decitabina |
| 20195412 (cancelado) | AURODECINJET 50 MG | Polvo liofilizado para reconstituir a solución inyectable | Decitabina |
| 20097119 (cancelado) | REDTIBIN 50 MG/VIAL | Polvo liofilizado | Decitabina |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (agente hipometilante, análogo de nucleósido); clasificación basada en conocimiento general |
| Riesgo de Mielosupresión | Alto, según conocimiento general. Las asociaciones del grafo de conocimiento con neutropenia, trombocitopenia y agranulocitosis son coherentes con este riesgo |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial y plaquetas, función hepática y renal |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

- **Condiciones asociadas a contraindicación en el grafo de conocimiento** (no provienen del texto del prospecto): enfermedad renal, piouréter, enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia, diabetes mellitus, cetoacidosis diabética, neutropenia y agranulocitosis.
- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. Las principales de nivel **Mayor** son:
  - Deferiprona
  - Samario (153Sm) lexidronam
  - Adalimumab
  - Baricitinib

  Entre las de nivel **Moderado** figuran palifermina, cloruro de estroncio Sr-89, mercaptopurina, roflumilast, cloranfenicol, zidovudina, aldesleucina, alemtuzumab, ganciclovir, gemcitabina, anakinra, azatioprina y vacunas (toxoide tetánico, ántrax).

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia es de nivel L4: no hay ensayos clínicos, solo un estudio de cohorte y un reporte de caso. Además, en Colombia no existe ningún registro sanitario vigente y faltan los datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), un vacío bloqueante para el tamizaje de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Definir la indicación original aprobada, ya que los registros solo mencionan el nombre del principio activo.
- Evaluar la situación regulatoria: los tres registros están cancelados, por lo que se requeriría un nuevo registro o su reactivación.
- Generar evidencia clínica prospectiva (por ejemplo, ensayos de fase 2) en citopenia refractaria de la infancia.
- Establecer un plan de monitoreo hematológico dado el alto riesgo de mielosupresión y las interacciones de nivel Mayor.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

