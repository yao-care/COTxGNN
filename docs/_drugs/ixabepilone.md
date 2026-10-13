---
layout: default
title: Ixabepilone
parent: Evidencia Alta (L1-L2)
nav_order: 364
evidence_level: L2
indication_count: 10
---

# Ixabepilone
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **10** 
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

# Ixabepilona: De Ixabepilona (indicación aprobada sin detalle) a Sarcoma de Ewing

## Resumen en Una Frase

Ixabepilona es un análogo de la epotilona B, un agente antineoplásico que estabiliza los microtúbulos y que está aprobado en otros países para el cáncer de mama metastásico. El modelo TxGNN predice que podría ser efectivo para el **Sarcoma de Ewing**, con **2 ensayos clínicos** (uno de Fase 1 y uno de Fase 2, ambos completados) y **1 publicación** específica que respaldan esta dirección, aunque ninguno demuestra una señal de eficacia concluyente.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Ixabepilona (el registro sanitario no detalla la indicación; en otros países se usa en cáncer de mama metastásico) |
| Nueva Indicación Predicha | Sarcoma de Ewing |
| Puntaje de Predicción TxGNN | 99.76% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, ixabepilona es un análogo semisintético de la epotilona B que estabiliza los microtúbulos, provoca detención mitótica y apoptosis en células tumorales de rápida división. A diferencia de los taxanos, no es sustrato de la glicoproteína P, por lo que podría conservar actividad en tumores resistentes a taxanos.

El Sarcoma de Ewing es un sarcoma pediátrico y de adultos jóvenes altamente proliferativo, por lo que un agente antimitótico es mecanísticamente plausible. Existen datos clínicos de ixabepilona en poblaciones pediátricas y de adultos jóvenes con tumores sólidos refractarios que incluyen Sarcoma de Ewing.

Sin embargo, los datos disponibles no identifican una señal de eficacia suficientemente fuerte para respaldar su adopción. El ensayo de Fase 2 no informa la tasa de respuesta en los datos recibidos, y el ensayo de Fase 1 no es específico para esta enfermedad.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00331643](https://clinicaltrials.gov/study/NCT00331643) | Fase 2 | Completado | 120 | Ixabepilona en niños y adultos jóvenes con tumores sólidos refractarios, incluido el Sarcoma de Ewing. Es la evidencia clínica más directa; no se indica la tasa de respuesta. |
| [NCT00030108](https://clinicaltrials.gov/study/NCT00030108) | Fase 1 | Completado | 30 | Búsqueda de dosis y farmacocinética en pacientes pediátricos con tumores sólidos y leucemias refractarias. Aporta datos de seguridad, no específicos de Sarcoma de Ewing. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [20068084](https://pubmed.ncbi.nlm.nih.gov/20068084/) | 2010 | Ensayo clínico Fase 2 (un solo brazo) | Clin Cancer Res | Ixabepilona administrada diariamente por 5 días en niños y adultos jóvenes con tumores sólidos refractarios (Children's Oncology Group). La dosis máxima tolerada fue de 8 mg/m²/dosis en niños y la toxicidad limitante fue la neutropenia. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20001658 | IXEMPRA® 45 MG POLVO PARA SOLUCIÓN INYECTABLE (cancelado) | Polvo liofilizado para reconstituir a solución inyectable | Ixabepilona |
| 20001660 | IXEMPRA® 15 MG POLVO SOLUCIÓN INYECTABLE (cancelado) | Polvo liofilizado para reconstituir a solución inyectable | Ixabepilona |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (agente estabilizador de microtúbulos, clase epotilona) |
| Riesgo de Mielosupresión | Alto: la neutropenia es la toxicidad limitante de la dosis en los estudios pediátricos |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial (neutrófilos y plaquetas), función hepática y renal, evaluación de neuropatía periférica |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

- **Contraindicaciones y enfermedades de riesgo (grafo de conocimiento, no texto del prospecto)**: el grafo de conocimiento asocia el fármaco con insuficiencia y enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia, neutropenia, agranulocitosis, anemia, neuropatía periférica, enfermedad cardíaca y cardiovascular, cardiopatía isquémica y enfermedad coronaria, paro cardíaco súbito, trastornos de la conducción cardíaca, diabetes mellitus, cetoacidosis diabética, hiperbilirrubinemia y síndrome de Gilbert.
- **Interacciones Farmacológicas**: se identificaron 276 interacciones. Las de nivel **mayor** incluyen deferiprona y lexidronam de samario (153Sm). Entre las de nivel **moderado** figuran aprepitant, dexametasona, cimetidina, claritromicina, clotrimazol, metronidazol, miconazol, rosuvastatina, simvastatina, tinidazol, troglitazona, cobicistat, deferasirox, palifermina, cloruro de estroncio Sr-89, fostamatinib, lusutrombopag y cloroquina. Muchas son compatibles con la modulación de CYP3A4 y con efectos mielosupresores aditivos.
- Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Existe un ensayo de Fase 2 completado en tumores sólidos pediátricos refractarios que incluye Sarcoma de Ewing (nivel L2), pero no se identificó una señal de eficacia que respalde su adopción. Además, los registros sanitarios en Colombia están cancelados, el perfil de toxicidad es considerable (mielosupresión y neuropatía) y no se dispone del prospecto oficial.

**Para avanzar se necesita:**
- Obtener los resultados de eficacia (tasa de respuesta específica en Sarcoma de Ewing) de los estudios NCT00331643 y 20068084.
- Descargar y analizar el prospecto oficial del INVIMA para completar el tamizaje de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Evaluar la disponibilidad real del fármaco en Colombia, dado que ambos registros están cancelados, y definir una vía regulatoria en caso de interés.
- Comparar con las alternativas estándar en Sarcoma de Ewing refractario.

*Nota: las otras nueve predicciones del modelo (afecciones mamarias benignas o raras) carecen de evidencia específica y se mantienen en Hold; su puntaje alto parece reflejar la cercanía en el grafo con el cáncer de mama, no evidencia propia de cada enfermedad.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

