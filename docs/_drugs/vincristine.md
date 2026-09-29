---
layout: default
title: Vincristine
parent: Solo Predicción del Modelo (L5)
nav_order: 407
evidence_level: L5
indication_count: 3
---

# Vincristine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Vincristina: De Indicación Original No Especificada en el Registro a Ganglioneuroblastoma

## Resumen en Una Frase

La vincristina es un alcaloide de la vinca que inhibe los microtúbulos y se usa como antineoplásico. El registro colombiano solo indica "VINCRISTINA", sin describir una indicación original.
El modelo TxGNN predice que podría ser efectiva para **ganglioneuroblastoma**, con **4 ensayos clínicos** y **6 publicaciones** que respaldan esta dirección. La evidencia es en su mayoría indirecta, porque la vincristina forma parte del esquema de quimioterapia base y no es la variable evaluada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | "VINCRISTINA" (el texto del registro no describe la indicación) |
| Nueva Indicación Predicha | Ganglioneuroblastoma |
| Puntaje de Predicción TxGNN | 99.31% |
| Nivel de Evidencia | L2 (con reservas: ensayo de Fase 2 completado, pero no aísla el efecto de la vincristina) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 12 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

DrugBank no aporta datos detallados sobre el mecanismo de acción (MOA), pero los datos de farmacología confirman que la vincristina se une a la **tubulina beta clase I (TUBB)**. Así bloquea el ensamblaje de los microtúbulos y detiene la mitosis en las células que se dividen rápido. Su uso clínico conocido incluye leucemia, enfermedad de Hodgkin, linfomas no Hodgkin, rabdomiosarcoma, neuroblastoma y tumor de Wilms.

El ganglioneuroblastoma pertenece al espectro de los tumores neuroblásticos, y la vincristina es un agente habitual en los esquemas de inducción multiagente del neuroblastoma. Por eso el puntaje alto de TxGNN es coherente con un uso ya establecido. Esto se parece más a una brecha de etiquetado que a un reposicionamiento verdadero.

Hay una limitación importante. Los ensayos de Fase 3 evalúan agentes añadidos (131I-MIBG, inhibidores de ALK, dinutuximab) sobre una base de quimioterapia. No aíslan el efecto propio de la vincristina, por lo que no constituyen evidencia directa (L1). La inscripción es principalmente de neuroblastoma de alto riesgo. Los datos específicos de ganglioneuroblastoma se limitan a reportes de caso y un ensayo prospectivo sobre estrategia quirúrgica.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03786783](https://clinicaltrials.gov/study/NCT03786783) | Fase 2 | Completado | 42 | Dinutuximab y sargramostim añadidos a quimioterapia de inducción en neuroblastoma de alto riesgo recién diagnosticado. La vincristina probablemente está en el esquema base, pero no es la variable evaluada. |
| [NCT03126916](https://clinicaltrials.gov/study/NCT03126916) | Fase 3 | Reclutando | 750 | 131I-MIBG o lorlatinib sobre terapia intensiva en neuroblastoma o ganglioneuroblastoma de alto riesgo. Apoya el contexto clínico, no la eficacia independiente. Aún sin resultados. |
| [NCT06172296](https://clinicaltrials.gov/study/NCT06172296) | Fase 3 | Reclutando | 478 | Dinutuximab añadido a terapia multimodal intensiva en neuroblastoma de alto riesgo. La vincristina probablemente está en el esquema base. Sin resultados. |
| [NCT01798004](https://clinicaltrials.gov/study/NCT01798004) | Fase 1 | Completado | 150 | Consolidación mieloablativa con busulfán/melfalán tras la inducción. La vincristina solo aparece en la inducción previa, por lo que la relevancia es indirecta. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31342649](https://pubmed.ncbi.nlm.nih.gov/31342649/) | 2019 | Ensayo clínico prospectivo | Pediatric Blood & Cancer | Uso de factores de riesgo definidos por imagen para decidir el momento de la cirugía en neuroblastoma de bajo riesgo. Busca reducir complicaciones del tratamiento. |
| [8255850](https://pubmed.ncbi.nlm.nih.gov/8255850/) | 1993 | Reporte de caso | Postgraduate Medical Journal | Ganglioneuroblastoma espinal irresecable con remisión completa histológica con quimioterapia combinada (doxorrubicina, vincristina, ciclofosfamida, etopósido, ifosfamida y cisplatino) sin radioterapia. |
| [15701990](https://pubmed.ncbi.nlm.nih.gov/15701990/) | 2005 | Reporte de caso | Journal of Pediatric Hematology/Oncology | Ganglioneuroblastoma con ictericia obstructiva como presentación inicial, tratado con quimioterapia que incluyó vincristina. |
| [7421294](https://pubmed.ncbi.nlm.nih.gov/7421294/) | 1980 | Reporte de caso (serie de 31 pacientes) | J Thorac Cardiovasc Surg | Ganglioneuroblastoma intratorácico. Sobrevivieron 27 de 31 pacientes, con seguimiento de hasta 25 años, tras resección, radioterapia o quimioterapia. |
| [3071124](https://pubmed.ncbi.nlm.nih.gov/3071124/) | 1988 | Reporte de caso | Hinyokika Kiyo | Ganglioneuroblastoma suprarrenal en un adulto con metástasis ganglionar regional gigante, tratado con enfoque multimodal. |
| [8888754](https://pubmed.ncbi.nlm.nih.gov/8888754/) | 1996 | Reporte de caso | J Pediatr Hematol Oncol | Ganglioneuroblastoma multifocal en estadio 4 con compromiso gástrico en un lactante. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20006838 | Vincristina sulfato 1 mg/1 ml solución inyectable (Venus Remedies Limited) | Solución inyectable | VINCRISTINA |

Nota: el sistema informa 12 registros en total, pero los datos recibidos solo muestran el número 20006838, repetido. También existe una presentación de polvo liofilizado para reconstituir a solución inyectable.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (alcaloide de la vinca, inhibidor de tubulina) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar el prospecto |
| Items de Monitoreo | Hemograma, función hepática y renal, evaluación neurológica (la neurotoxicidad es un riesgo relevante del fármaco) |
| Protección en Manejo | Sí. Debe seguir las regulaciones de manejo de fármacos citotóxicos. |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La vincristina es un componente establecido de los esquemas de quimioterapia del espectro neuroblástico, y hay ensayos de Fase 2/3 sobre esos esquemas. Sin embargo, ningún ensayo aísla su efecto. La evidencia específica de ganglioneuroblastoma son reportes de caso, y no se han verificado las advertencias del prospecto.

**Para avanzar se necesita:**
- Obtener del sitio de INVIMA el prospecto con advertencias y contraindicaciones, y analizarlo. Es un vacío que bloquea el tamizaje de seguridad.
- Obtener el MOA desde DrugBank para completar el análisis mecanístico.
- Confirmar en los protocolos de los ensayos (NCT03126916, NCT06172296) que la vincristina está en el esquema base y con qué dosis.
- Buscar evidencia específica de ganglioneuroblastoma, separada de la de neuroblastoma de alto riesgo.
- Definir un plan de monitoreo de neurotoxicidad y hematológico, con protocolos de administración segura.

**Otras predicciones del mismo fármaco:** "retroperitoneal neoplasm" (puntaje 99.23%) es una categoría anatómica heterogénea con respaldo solo de series retrospectivas y reportes de caso, y conviene acotarla a histologías específicas. "Vertebral anomalies and variable endocrine and T-cell dysfunction" (99.24%) no tiene racional mecanístico ni evidencia, por lo que se recomienda Hold.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

