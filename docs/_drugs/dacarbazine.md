---
layout: default
title: Dacarbazine
parent: Solo Predicción del Modelo (L5)
nav_order: 146
evidence_level: L5
indication_count: 1
---

# Dacarbazine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Dacarbazina: De Indicación Original No Especificada en el Registro a Neoplasia del Tracto Aerodigestivo Superior

## Resumen en Una Frase

Dacarbazina es un agente alquilante antineoplásico comercializado en Colombia en polvo liofilizado inyectable. Los registros sanitarios disponibles solo consignan el nombre del principio activo y no detallan la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **neoplasia del tracto aerodigestivo superior**, pero solo hay **1 ensayo clínico** indirecto (con temozolomida, terminado) y **20 publicaciones** de relevancia limitada. Ninguna evalúa dacarbazina directamente en esta indicación.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro INVIMA solo consigna «DACARBAZINA») |
| Nueva Indicación Predicha | Neoplasia del tracto aerodigestivo superior |
| Puntaje de Predicción TxGNN | 99.26% |
| Nivel de Evidencia | L4 (solo respaldo indirecto a nivel de clase; sin estudios directos con dacarbazina) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro. Según la farmacología general, dacarbazina es un agente alquilante que metila el ADN. Se activa en el hígado (mediante CYP) a MTIC, el mismo metabolito activo que la temozolomida forma de manera espontánea. Este es el vínculo mecanístico que sustenta la predicción. Esta explicación es una inferencia y no proviene del registro proporcionado.

Ese vínculo lleva a un ensayo de Fase 2 con temozolomida en cánceres aerodigestivos avanzados (cabeza y cuello, esófago, pulmón, colorrectal) seleccionados por metilación del promotor de MGMT. Si dacarbazina actuara en este contexto, su actividad probablemente dependería del estado de MGMT.

Hay razones para ser cautelosos. El carcinoma escamoso de cabeza y cuello, la histología dominante en esta indicación, no se reconoce como un tumor sensible a alquilantes. Los pocos subtipos con respuesta en la literatura son tumores raros de tipo neuroendocrino o paraganglioma. El puntaje de 99.26% es una predicción computacional y no tiene respaldo de datos clínicos directos con dacarbazina.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00423150](https://clinicaltrials.gov/study/NCT00423150) | Fase 2 | Terminado | 86 | Temozolomida (no dacarbazina) en cánceres aerodigestivos avanzados, colorrectal, pulmón no microcítico, cabeza y cuello y esófago, seleccionados por metilación del promotor de MGMT. Apoyo indirecto a nivel de clase. No hay resultados de eficacia en el registro. |

## Evidencia de Literatura

De las 20 publicaciones recuperadas, se listan las más relevantes. Todas tienen relevancia aún pendiente de revisión.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [23443801](https://pubmed.ncbi.nlm.nih.gov/23443801/) | 2013 | Fase 2 (temozolomida) | Mol Cancer Ther | Estudio NCT00423150: evalúa si la metilación de MGMT predice la respuesta a temozolomida en cáncer aerodigestivo y colorrectal avanzado. El resumen disponible no incluye resultados. |
| [7826911](https://pubmed.ncbi.nlm.nih.gov/7826911/) | 1994 | Estudio clínico | Ann Oncol | Dacarbazina con 5-fluorouracilo en carcinoma medular de tiroides avanzado, un tumor neuroendocrino. Es la única publicación con dacarbazina como agente de estudio, pero no es la indicación predicha. |
| [8346929](https://pubmed.ncbi.nlm.nih.gov/8346929/) | 1993 | Revisión | Gan To Kagaku Ryoho | Quimioterapia del angiosarcoma de cabeza y cuello, incluido el esquema CYVADIC (que contiene DTIC, es decir dacarbazina). Pronóstico descrito como muy malo. |
| [17987262](https://pubmed.ncbi.nlm.nih.gov/17987262/) | 2008 | Fase 2 (temozolomida) | J Neurooncol | Vinorelbina con temozolomida intensiva en metástasis cerebrales recurrentes. Apoyo indirecto. |
| [34654328](https://pubmed.ncbi.nlm.nih.gov/34654328/) | 2024 | Cohorte (un centro) | Ear Nose Throat J | Seis pacientes con paraganglioma maligno de cabeza y cuello: características clínicas, genéticas y opciones de tratamiento. |
| [25772801](https://pubmed.ncbi.nlm.nih.gov/25772801/) | 2015 | Revisión | J Clin Neurosci | Temozolomida en tumores hipofisarios agresivos, con resultados prometedores. Apoyo indirecto a nivel de clase. |
| [20627492](https://pubmed.ncbi.nlm.nih.gov/20627492/) | 2010 | Revisión | Clin Oncol | Carcinoma medular de tiroides: aspectos generales y tratamiento. |
| [34705104](https://pubmed.ncbi.nlm.nih.gov/34705104/) | 2022 | Revisión | J Cancer Res Clin Oncol | Carga global de cánceres relacionados con el virus de Epstein-Barr. Contexto epidemiológico, sin datos de dacarbazina. |
| [11163509](https://pubmed.ncbi.nlm.nih.gov/11163509/) | 2001 | Serie de casos | Int J Radiat Oncol Biol Phys | Radioterapia del estesioneuroblastoma, tumor intranasal raro. |
| [3153227](https://pubmed.ncbi.nlm.nih.gov/3153227/) | 1986 | Reporte de caso | Pediatr Hematol Oncol | Neuroblastoma olfatorio en un niño de 2 años, tratado con radiación y quimioterapia combinada. |

## Información de Mercado en Colombia

Se reportan 20 registros sanitarios en total. Los datos entregados contienen solo 3 registros distintos, todos de polvo liofilizado para reconstituir a solución inyectable. El texto de indicación aprobada de cada uno solo consigna «Dacarbazina».

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20211561 | NEGORIX® 200 MG (Korea United Pharm. Inc.) | Polvo liofilizado para reconstituir a solución inyectable | No especificada (solo consigna «Dacarbazina») |
| 20080268 | CARBAVEN 200 (Seven Pharma Colombia S.A.S.) | Polvo liofilizado para reconstituir a solución inyectable | No especificada (solo consigna «Dacarbazina») |
| 19961319 | DACARBAZINA 200 MG (Blau Farmacéutica Colombia S.A.S.) | Polvo liofilizado para reconstituir a solución inyectable | No especificada (solo consigna «Dacarbazina») |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (agente alquilante que metila el ADN) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar el prospecto. En general, en citotóxicos se vigilan hemograma y función hepática y renal. |
| Protección en Manejo | Aplicar las normas de manejo de fármacos citotóxicos (práctica general) |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El puntaje TxGNN es alto (99.26%), pero no hay ningún estudio directo de dacarbazina en esta indicación. El único ensayo relacionado usa temozolomida, fue terminado y no reporta resultados de eficacia. Además, la histología dominante (carcinoma escamoso de cabeza y cuello) no es sensible a alquilantes.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA para completar advertencias y contraindicaciones, un vacío bloqueante para el tamizaje de seguridad.
- Obtener el mecanismo de acción y las indicaciones originales desde DrugBank.
- Revisar los resultados completos de NCT00423150 (PMID 23443801) para evaluar si el efecto de clase es replicable con dacarbazina.
- Buscar evidencia directa de dacarbazina en subtipos histológicos específicos (neuroendocrinos, paragangliomas) y considerar el estado de MGMT como criterio de selección.
- Aclarar la indicación aprobada en cada registro sanitario, que hoy solo consigna el nombre del principio activo.

*Los resultados son solo de referencia para investigación y no constituyen consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de cualquier aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

