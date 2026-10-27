---
layout: default
title: Topiramate
parent: Solo Predicción del Modelo (L5)
nav_order: 631
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Topiramate: nueva indicación predicha, Neoplasia del nervio trigémino (nivel de evidencia L5). Indicación original: Topiramato"
monitor_inn: "Topiramate"
predicted_indications: ["trigeminal nerve neoplasm"]
---

# Topiramate
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Topiramato: De Indicación Registrada (Topiramato) a Neoplasia del Nervio Trigémino
{: .text-alpha }

## Resumen en Una Frase

Topiramato es un fármaco antiepiléptico de amplio espectro; su único registro sanitario en Colombia (TOPAMAC® 100 mg tabletas) figura solo con el nombre del principio activo, sin una indicación detallada.
El modelo TxGNN predice que podría ser efectivo para **neoplasia del nervio trigémino** (puntaje 99.70%), pero para esta predicción **no se encontraron ensayos clínicos ni publicaciones**; se trata únicamente de una predicción del modelo.
Entre las demás predicciones, las que tienen más respaldo son subtipos de epilepsia (por ejemplo, convulsiones inducidas por el pensamiento), que se comentan más abajo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Topiramato (el registro no detalla la indicación; el fármaco se usa en epilepsia) |
| Nueva Indicación Predicha | Neoplasia del nervio trigémino |
| Puntaje de Predicción TxGNN | 99.70% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información farmacológica conocida, topiramato bloquea los canales de sodio dependientes de voltaje, potencia la actividad GABA-A, antagoniza receptores glutamatérgicos AMPA/kainato e inhibe la anhidrasa carbónica. Los datos compilados confirman su interacción con las isoformas CA1, CA4, CA7 y CA12.

Estos mecanismos explican su eficacia antiepiléptica, pero **no corresponden a un mecanismo antineoplásico establecido**. Cualquier vínculo con una neoplasia del nervio trigémino sería, como mucho, sintomático (por ejemplo, alivio de dolor de tipo neuralgia del trigémino) y no dirigido contra el tumor. El puntaje alto de TxGNN (0.997) proviene solo de la estructura del grafo de conocimiento y no está respaldado por evidencia real.

### Otras predicciones evaluadas

Los datos incluyen otras indicaciones predichas, casi todas epilepsias reflejas, donde el vínculo mecanístico sí es plausible:

| Indicación predicha | Puntaje TxGNN | Nivel | Observación |
|------|------|------|------|
| Epilepsia visual | 99.28% | L3 | Revisiones y guías de epilepsia general; evidencia indirecta |
| Convulsiones inducidas por el pensamiento | 99.21% | L1* | Revisiones Cochrane de topiramato como terapia adicional en epilepsia focal resistente; *no específicas del subtipo* |
| Convulsiones audiogénicas | 99.21% | L4 | Solo estudios en animales (ratones DBA/2, ratas GAERS) |
| Convulsiones por micción | 99.21% | L4 | Literatura general de epilepsia, nada específico |
| Convulsiones al comer | 99.21% | L4 | Literatura sobre trastornos alimentarios; coincidencia de palabras clave |
| Epilepsia por sobresalto | 99.21% | L5 | Solo predicción |
| Convulsiones inducidas por orgasmo | 99.21% | L5 | Solo predicción |
| Convulsiones al leer | 99.09% | L4 | Evidencia indirecta |

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para neoplasia del nervio trigémino (ni para ninguna de las otras indicaciones predichas).

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para neoplasia del nervio trigémino.

A modo de referencia, la indicación predicha con mayor respaldo bibliográfico (convulsiones inducidas por el pensamiento) cuenta con las siguientes publicaciones relevantes, todas sobre epilepsia en general y no específicas del subtipo:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31642054](https://pubmed.ncbi.nlm.nih.gov/31642054/) | 2019 | Revisión sistemática (Cochrane) | Cochrane Database Syst Rev | Topiramato como terapia adicional en epilepsia focal resistente a fármacos |
| [24570033](https://pubmed.ncbi.nlm.nih.gov/24570033/) | 2014 | Revisión sistemática (Cochrane) | Cochrane Database Syst Rev | Topiramato adicional en epilepsia parcial resistente |
| [18646072](https://pubmed.ncbi.nlm.nih.gov/18646072/) | 2008 | Revisión sistemática (Cochrane) | Cochrane Database Syst Rev | Topiramato adicional en epilepsia parcial resistente |
| [12137625](https://pubmed.ncbi.nlm.nih.gov/12137625/) | 2002 | Revisión sistemática (Cochrane) | Cochrane Database Syst Rev | Topiramato adicional en epilepsia parcial resistente |
| [10796787](https://pubmed.ncbi.nlm.nih.gov/10796787/) | 2000 | Revisión sistemática (Cochrane) | Cochrane Database Syst Rev | Resumen de la evidencia inicial de topiramato adicional |
| [39854828](https://pubmed.ncbi.nlm.nih.gov/39854828/) | 2025 | Revisión/Consenso | Epilepsy Behav | Medicamentos antiepilépticos en síndrome de Lennox-Gastaut; topiramato está aprobado por la FDA |
| [9706735](https://pubmed.ncbi.nlm.nih.gov/9706735/) | 1998 | Revisión | Can J Neurol Sci | Seguridad y tolerabilidad de topiramato en siete estudios doble ciego |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 213766 (cancelado) | TOPAMAC® 100 MG TABLETAS | Tableta | TOPIRAMATO |

El único registro encontrado (Janssen Cilag S.A.) está cancelado, por lo que no hay registro vigente en los datos compilados. Conviene verificar si existen otros productos de topiramato (por ejemplo, genéricos) con registro vigente.

---

## Consideraciones de Seguridad

- **Interacciones farmacológicas / farmacología de dianas:** topiramato interactúa con las anhidrasas carbónicas 1, 4, 7 y 12 (4 interacciones registradas, sin nivel de severidad asignado).
- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** trastorno de ansiedad, trastorno neurótico, trastorno distímico, enfermedad renal, piouréter, enfermedad hepática, enfermedad de la vesícula biliar, enfermedad diarreica, hipertensión ocular, nefrolitiasis (incluida la susceptibilidad asociada a SLC26A1), nefropatía aguda por uratos, trastorno acidótico, acidosis metabólica, trastorno amnésico y amnesia retrógrada.
- **Señales de la literatura:** se describen exacerbación psicótica, episodio maníaco, complicaciones durante el embarazo y reacciones adversas en niños.

Para advertencias y contraindicaciones oficiales, consultar el prospecto aprobado, ya que no se dispone de esa información en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold** (para neoplasia del nervio trigémino)

**Justificación:**
- La predicción es solo del modelo (L5): no hay ensayos ni literatura, y topiramato no tiene un mecanismo antineoplásico conocido. Además, el único registro sanitario en Colombia está cancelado.
- Si se desea avanzar con topiramato, las indicaciones con mejor soporte son subtipos de epilepsia (convulsiones inducidas por el pensamiento, epilepsia visual); sin embargo, la evidencia es indirecta y proviene de la epilepsia en general, un uso que ya es conocido del fármaco, por lo que aportan poco valor de reposicionamiento. Se consideran preguntas de investigación.

**Para avanzar se necesita:**
- Datos del mecanismo de acción desde DrugBank y análisis del vínculo mecanístico.
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones), que constituye una brecha bloqueante para el tamizaje de seguridad.
- Verificar el estado de otros registros de topiramato en Colombia.
- Para neoplasia del nervio trigémino: revisión de literatura dirigida y evidencia preclínica antes de cualquier consideración clínica.
- Para los subtipos de epilepsia refleja: series de casos o estudios específicos de cada subtipo.
- Evaluar las contraindicaciones del grafo de conocimiento (enfermedad renal, litiasis, acidosis metabólica, enfermedad hepática) frente a la población objetivo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

