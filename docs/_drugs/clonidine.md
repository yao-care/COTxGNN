---
layout: default
title: Clonidine
parent: Solo Predicción del Modelo (L5)
nav_order: 173
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Clonidine: nueva indicación predicha, Síndrome de Tourette (nivel de evidencia L5). Indicación original: CLONIDINA"
monitor_inn: "clonidine"
predicted_indications: ["faciodigitogenital syndrome", "specific developmental disorder", "chondromyxoid fibroma", "trichotillomania", "Tourette syndrome", "obesity disorder", "hypervitaminosis", "proximal 16p11.2 microdeletion syndrome", "migraine disorder", "manic bipolar affective disorder"]
---

# Clonidine
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

# Clonidina: De Indicación Registrada (Clonidina) a Síndrome de Tourette

## Resumen en Una Frase

Clonidina es un agonista alfa-2 adrenérgico, registrado en Colombia en tabletas de uso oral (el texto de indicación del registro solo menciona "CLONIDINA", sin especificar la enfermedad).
El modelo TxGNN predice que podría ser efectivo para **Síndrome de Tourette**, con **2 ensayos clínicos** (ambos de Fase 4) y **18 publicaciones** que respaldan esta dirección, incluyendo una guía clínica europea y un metaanálisis en red.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | CLONIDINA (el registro sanitario no detalla la indicación clínica) |
| Nueva Indicación Predicha | Síndrome de Tourette |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L1 (según la clasificación de los datos compilados; ver nota en la conclusión) |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Proceed with Guardrails |

**Nota sobre la selección:** el candidato con mayor puntaje TxGNN (síndrome faciodigitogenital, 99.999%) carece de ensayos, literatura y fundamento mecanístico. Se presenta Tourette porque es la indicación con la evidencia más sólida entre las predichas.

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, clonidina es un agonista de receptores alfa-2 adrenérgicos que reduce la salida noradrenérgica central. Su uso como antihipertensivo está bien establecido, y mecanísticamente podría ser aplicable al síndrome de Tourette.

La relación entre ambas indicaciones es indirecta: el efecto simpaticolítico central de clonidina modula los circuitos cortico-estriato-tálamo-corticales implicados en los tics. Es una opción recomendada por las guías europeas para tics, en particular cuando existe TDAH comórbido. Reportes clínicos desde 1979 describen mejoría en niños que no respondían a haloperidol.

Cabe señalar que la indicación original registrada no está especificada en el texto del registro sanitario, por lo que la comparación con la indicación original se basa en el uso farmacológico conocido y no en el texto regulatorio.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00152750](https://clinicaltrials.gov/study/NCT00152750) | Fase 4 | Desconocido | 32 | Evalúa si tratar el sueño nocturno con clonidina mejora la agresividad diurna en niños con Tourette y TDAH comórbido |
| [NCT00370838](https://clinicaltrials.gov/study/NCT00370838) | Fase 4 | Completado | 12 | Comparación cruzada doble ciego de levetiracetam frente a clonidina para suprimir tics en niños con Tourette; muestra muy pequeña |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36528030](https://pubmed.ncbi.nlm.nih.gov/36528030/) | 2023 | Metaanálisis en red | Lancet Child & Adolescent Health | Compara eficacia, tolerabilidad y aceptabilidad de intervenciones farmacológicas en niños, adolescentes y jóvenes con Tourette |
| [34757514](https://pubmed.ncbi.nlm.nih.gov/34757514/) | 2022 | Guía clínica | Eur Child Adolesc Psychiatry | Guías europeas (v2.0), parte III, sobre tratamiento farmacológico del Tourette y otros trastornos de tics |
| [38695046](https://pubmed.ncbi.nlm.nih.gov/38695046/) | 2024 | Estudio clínico | Psychiatry Investigation | Eficacia y seguridad del parche de clonidina en Tourette con TDAH comórbido |
| [34286606](https://pubmed.ncbi.nlm.nih.gov/34286606/) | 2021 | Revisión sistemática | J Psychopharmacol | Evalúa la calidad de la evidencia del tratamiento farmacológico del Tourette en niños y adultos |
| [27132945](https://pubmed.ncbi.nlm.nih.gov/27132945/) | 2016 | Revisión sistemática | J Child Psychol Psychiatry | Revisión de tratamientos del Tourette en niños y jóvenes |
| [23473832](https://pubmed.ncbi.nlm.nih.gov/23473832/) | 2013 | Revisión | Eur J Paediatr Neurol | Opciones farmacológicas para Tourette con TDAH comórbido |
| [89558](https://pubmed.ncbi.nlm.nih.gov/89558/) | 1979 | Estudio clínico | Lancet | Dosis bajas de clonidina mejoraron la condición en algunos niños sin respuesta a haloperidol |
| [6109915](https://pubmed.ncbi.nlm.nih.gov/6109915/) | 1981 | Estudio clínico | Lancet | Reporte sobre clonidina en síndrome de Tourette |
| [11393328](https://pubmed.ncbi.nlm.nih.gov/11393328/) | 2001 | Revisión | Paediatric Drugs | Los agentes de primera línea para la supresión de tics incluyen clonidina |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20015994 | CLONIDIN® TABLETA | Tableta | CLONIDINA (cancelado) |
| 19995299 | CLONIDINA TABLETAS POR 0.150 MG. | Tableta | CLONIDINA (cancelado) |

Ambos registros figuran como cancelados; actualmente no hay registros vigentes de clonidina como monofármaco en Colombia.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no son texto de prospecto):** el grafo de conocimiento TxGNN asocia clonidina con condiciones como hipotensión, infarto de miocardio, enfermedad de conducción cardíaca, paro cardíaco súbito, insuficiencia hepática, insuficiencia respiratoria, pancreatitis, diabetes tipo 1 y 2, cetoacidosis diabética, lupus eritematoso sistémico, gota y trastornos de ansiedad, entre otras. Esta lista debe verificarse contra el prospecto oficial.
- **Interacciones farmacológicas:** se identificaron 234 interacciones, de las cuales las principales mostradas son de nivel moderado: corticoides (hidrocortisona, triamcinolona, dexametasona, betametasona, budesonida), bupropión, morfina, dronabinol, antidiabéticos (inhibidores de SGLT2 como canagliflozina, dapagliflozina, empagliflozina y ertugliflozina; sulfonilureas como clorpropamida, acetohexamida, glimepirida, glipizida y gliburida) e insulinas.
- **Guardrails sugeridos en los datos compilados:** monitorear presión arterial y frecuencia cardíaca, evitar la suspensión abrupta (riesgo de hipertensión de rebote) y vigilar la sedación.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La evidencia para Tourette proviene de guías clínicas, un metaanálisis en red y revisiones sistemáticas, además de décadas de uso clínico. Los dos ensayos de Fase 4 son pequeños (n=32 y n=12), por lo que el nivel L1 se apoya en fuentes de síntesis y no en ensayos de Fase 3 propios; conviene interpretarlo con cautela. Además, no hay registros vigentes en Colombia y falta información de seguridad del prospecto.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA para advertencias y contraindicaciones (brecha de datos bloqueante para el tamizaje de seguridad).
- Obtener datos del mecanismo de acción desde DrugBank.
- Aclarar la indicación original registrada, ya que el texto del registro solo dice "CLONIDINA".
- Definir la situación regulatoria: no existen registros vigentes, por lo que se requeriría una nueva solicitud o reactivación.
- Confirmar la compatibilidad de vía de administración y formulación (tableta oral frente al parche utilizado en el estudio de 2024).
- Plan de monitoreo cardiovascular (presión arterial, frecuencia cardíaca) y de sedación, y estrategia de retirada gradual.

---

### Otras indicaciones predichas (referencia breve)

| Indicación | Puntaje TxGNN | Nivel | Recomendación |
|---|---|---|---|
| Trastorno bipolar maníaco | 99.76% | L3 | Pregunta de investigación (un ensayo terminado con 5 participantes; revisión sistemática 2023 y estudio aleatorizado 2022) |
| Trastorno de migraña | 99.81% | L3 | Pregunta de investigación (evidencia histórica inconsistente) |
| Obesidad | 99.91% | L3 | Pregunta de investigación (estudios fisiológicos, no de pérdida de peso) |
| Tricotilomanía | 99.99% | L5 | Hold (solo un estudio en ratones) |
| Trastorno específico del desarrollo | 100.00% | L4 | Hold (literatura indirecta) |
| Síndrome faciodigitogenital, fibroma condromixoide, hipervitaminosis, microdeleción 16p11.2 | 99.86%–100.00% | L5 | Hold (sin evidencia) |
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

