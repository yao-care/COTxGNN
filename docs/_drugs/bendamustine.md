---
layout: default
title: Bendamustine
parent: Evidencia Alta (L1-L2)
nav_order: 85
evidence_level: L1
indication_count: 10
---

# Bendamustine
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **10** 
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

# Bendamustina: De Indicación Original No Especificada a Linfoma de Células del Manto

## Resumen en Una Frase

La bendamustina es un agente alquilante bifuncional que se usa en oncohematología. En Colombia, el registro sanitario solo consigna el texto «BENDAMUSTINE» y no detalla una indicación original.
El modelo TxGNN predice que podría ser efectiva para **linfoma de células del manto**, con **50 ensayos clínicos** y **20 publicaciones** asociados. Entre ellos hay ensayos de Fase 3 completados y ensayos aleatorizados publicados en revistas de alto impacto.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro solo dice «BENDAMUSTINE») |
| Nueva Indicación Predicha | Linfoma de células del manto (mantle cell lymphoma) |
| Puntaje de Predicción TxGNN | 99.63% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 2 (ambos con el mismo número, 20154170) |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en esta fuente. Según la información conocida, la bendamustina es un agente alquilante bifuncional con rasgos similares a los análogos de purina. Provoca entrecruzamiento del ADN y catástrofe mitótica en las células tumorales.

El registro colombiano no indica para qué enfermedad fue aprobada, así que no se puede comparar directamente con la indicación original. La relación mecanística se apoya en su actividad en neoplasias de células B indolentes y del manto, que ya está establecida en la práctica clínica. El puntaje alto de TxGNN es coherente con esa actividad.

La combinación bendamustina + rituximab (BR) es el eje de varios ensayos de Fase 3 en linfoma de células del manto. En ellos se compara con R-CHOP/R-CVP o con fludarabina + rituximab, o se le añade un inhibidor de BTK (ibrutinib, acalabrutinib). La predicción no es solo teórica: refleja un uso clínico ya documentado.

---

## Evidencia de Ensayos Clínicos

Se muestran los 10 ensayos más relevantes de un total de 50 recuperados. Muchos de los restantes no estudian bendamustina en linfoma de células del manto.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00877006](https://clinicaltrials.gov/study/NCT00877006) | Fase 3 | Completado | 447 | Estudio BRIGHT: BR frente a R-CHOP/R-CVP en primera línea de linfoma no Hodgkin indolente o de células del manto, con la tasa de respuesta completa como objetivo principal |
| [NCT01776840](https://clinicaltrials.gov/study/NCT01776840) | Fase 3 | Completado | 523 | Ibrutinib + BR frente a placebo + BR en mayores de 65 años con linfoma de células del manto recién diagnosticado |
| [NCT02972840](https://clinicaltrials.gov/study/NCT02972840) | Fase 3 | Activo, sin reclutar | 635 | Acalabrutinib + BR frente a placebo + BR en linfoma de células del manto sin tratamiento previo |
| [NCT01456351](https://clinicaltrials.gov/study/NCT01456351) | Fase 3 | Completado | 230 | Estudio de no inferioridad de BR frente a fludarabina + rituximab en linfomas de bajo grado y del manto recurrentes |
| [NCT05868395](https://clinicaltrials.gov/study/NCT05868395) | Fase 2 | Reclutando | 16 | Polatuzumab + bendamustina + rituximab en linfoma de células del manto en recaída o refractario |
| [NCT05245656](https://clinicaltrials.gov/study/NCT05245656) | Fase 2 | Reclutando | 90 | RB alternado con RBAC frente a RB solo en ancianos no candidatos a trasplante con diagnóstico reciente |
| [NCT06136351](https://clinicaltrials.gov/study/NCT06136351) | Fase 2 | Reclutando | 23 | Zanubrutinib + BR en pacientes de edad avanzada, con alteraciones de TP53 o intolerancia a quimioterapia |
| [NCT01737177](https://clinicaltrials.gov/study/NCT01737177) | Fase 2 | Completado | 42 | Bendamustina + lenalidomida + rituximab (R2-B) como segunda línea en primera recaída o refractariedad |
| [NCT00992134](https://clinicaltrials.gov/study/NCT00992134) | Fase 2 | Completado | 41 | Rituximab + bendamustina + citarabina (R-BAC) en pacientes no elegibles para regímenes intensivos o trasplante |
| [NCT01661881](https://clinicaltrials.gov/study/NCT01661881) | Fase 2 | Activo, sin reclutar | 23 | Rituximab/bendamustina seguido de rituximab/citarabina en pacientes sin tratamiento previo elegibles para trasplante |

---

## Evidencia de Literatura

Se muestran las 10 publicaciones más relevantes de 20. Los hallazgos se resumen a partir de los resúmenes disponibles.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [23433739](https://pubmed.ncbi.nlm.nih.gov/23433739/) | 2013 | ECA Fase 3 | Lancet | BR frente a R-CHOP como primera línea en linfomas indolentes y de células del manto (estudio de no inferioridad) |
| [24591201](https://pubmed.ncbi.nlm.nih.gov/24591201/) | 2014 | ECA Fase 3 | Blood | Estudio BRIGHT: BR frente a R-CHOP/R-CVP en linfoma indolente o de células del manto sin tratamiento previo |
| [30811293](https://pubmed.ncbi.nlm.nih.gov/30811293/) | 2019 | ECA (seguimiento) | J Clin Oncol | Resultados a 5 años del estudio BRIGHT, con datos de eficacia y seguridad a largo plazo |
| [35657079](https://pubmed.ncbi.nlm.nih.gov/35657079/) | 2022 | ECA | N Engl J Med | Ibrutinib + BR seguido de mantenimiento con rituximab en pacientes mayores con linfoma de células del manto sin tratamiento previo |
| [40311141](https://pubmed.ncbi.nlm.nih.gov/40311141/) | 2025 | ECA | J Clin Oncol | Acalabrutinib + BR en linfoma de células del manto sin tratamiento previo, con la hipótesis de menor toxicidad que ibrutinib |
| [41052510](https://pubmed.ncbi.nlm.nih.gov/41052510/) | 2025 | ECA Fase 2/3 | Lancet | ENRICH: ibrutinib + rituximab frente a inmunoquimioterapia (R-CHOP o BR) en mayores de 60 años |
| [40975105](https://pubmed.ncbi.nlm.nih.gov/40975105/) | 2025 | Ensayo Fase 2 | Lancet Haematol | FIL_V-RBAC: RBAC seguido de venetoclax en pacientes mayores con linfoma de células del manto de alto riesgo |
| [32126141](https://pubmed.ncbi.nlm.nih.gov/32126141/) | 2020 | Ensayo Fase 2 (análisis agrupado) | Blood Adv | Inducción con rituximab/bendamustina y rituximab/citarabina antes del trasplante autólogo en pacientes elegibles |
| [41380101](https://pubmed.ncbi.nlm.nih.gov/41380101/) | 2026 | Estudio retrospectivo | Blood Adv | 911 pacientes tratados con BR de primera línea; evalúa el beneficio del mantenimiento con rituximab |
| [41132246](https://pubmed.ncbi.nlm.nih.gov/41132246/) | 2025 | Guía clínica | HemaSphere | Guías EHA-EU MCL para el diagnóstico y tratamiento del linfoma de células del manto |

---

## Información de Mercado en Colombia

Los dos registros del Evidence Pack tienen el mismo número, 20154170, y los mismos datos, por lo que se presenta una sola fila.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20154170 | Bendamustina clorhidrato 100 mg polvo liofilizado para inyección (Laboratorio Kemex S.A) | Polvo liofilizado para reconstituir a solución inyectable | BENDAMUSTINE (sin indicación detallada) |

---

## Citotoxicidad

El Evidence Pack no incluye datos de toxicidad. Los valores de la tabla salen de la clase del fármaco (agente alquilante) y deben confirmarse en el prospecto.

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (agente alquilante bifuncional) |
| Riesgo de Mielosupresión | Medio a alto, esperable en alquilantes; confirmar en las advertencias del prospecto |
| Clasificación de Emetogenicidad | Media, según la categoría del fármaco; confirmar en el prospecto |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal, vigilancia de infecciones |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos (preparación con protección del personal) |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay varios ensayos de Fase 3 completados (BRIGHT y el estudio de BR frente a fludarabina + rituximab, entre otros) y ensayos aleatorizados publicados en revistas de alto impacto que sostienen el uso de bendamustina + rituximab en linfoma de células del manto (nivel L1). Aun así, el registro colombiano no especifica una indicación y no hay datos de seguridad locales, por lo que conviene avanzar con salvaguardas.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias, contraindicaciones e interacciones), que hoy falta.
- Confirmar si el registro sanitario 20154170 incluye linfoma de células del manto entre sus indicaciones aprobadas o si el uso sería fuera de indicación.
- Complementar el mecanismo de acción con datos de DrugBank.
- Definir un plan de monitoreo hematológico y de infecciones, y limitar el uso a centros con experiencia en quimioterapia citotóxica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

