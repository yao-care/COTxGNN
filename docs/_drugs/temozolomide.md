---
layout: default
title: Temozolomide
parent: Evidencia Alta (L1-L2)
nav_order: 375
evidence_level: L1
indication_count: 2
---

# Temozolomide
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **2** 
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

# Temozolomida: De Indicación Original No Registrada a Tumor Astrocítico del Adulto

## Resumen en Una Frase

Temozolomida es un agente alquilante oral que se usa contra tumores cerebrales. La base de datos no registra una indicación original, y el registro sanitario colombiano solo repite el nombre del fármaco.
El modelo TxGNN predice que podría ser efectivo para **tumor astrocítico del adulto**, incluido el glioblastoma.
Lo respaldan **2 ensayos clínicos** y **20 publicaciones**, entre ellas varios ensayos aleatorizados de Fase 3. Esta predicción parece un vacío de la base de datos más que un reposicionamiento genuino.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro sanitario solo dice "TEMOZOLOMIDA") |
| Nueva Indicación Predicha | Tumor astrocítico del adulto |
| Puntaje de Predicción TxGNN | 99.36% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Temozolomida es un agente alquilante oral que daña el ADN al generar lesiones de O6-metilguanina, y atraviesa la barrera hematoencefálica. Por eso es útil en tumores del sistema nervioso central. Su actividad en tumores astrocíticos, incluido el glioblastoma (astrocitoma grado 4 de la OMS), depende en gran medida del estado de metilación del promotor de MGMT.

Existe evidencia directa de Fase 3 en dos escenarios:
- Astrocitoma recurrente, donde temozolomida se comparó con PCV.
- Glioblastoma recién diagnosticado, donde el esquema de Stupp combina temozolomida con radioterapia.

La base de datos no lista indicaciones originales ni datos detallados del mecanismo de acción. Por eso la "nueva" indicación parece ser una indicación ya establecida que faltaba en el registro, y no un reposicionamiento real.

Hay una limitación importante: la mayor parte de la literatura se centra en glioblastoma y no en astrocitoma de menor grado. Los resultados no se pueden extrapolar sin estratificar por grado tumoral y por estado de MGMT.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00052455](https://clinicaltrials.gov/study/NCT00052455) | Fase 3 | Completado | 500 | Ensayo aleatorizado que compara temozolomida con PCV (procarbazina, lomustina y vincristina) en tumores astrocíticos recurrentes de grado III y IV de la OMS. Evidencia directa y de alta calidad. |
| [NCT00960492](https://clinicaltrials.gov/study/NCT00960492) | Fase 1 | Completado | 26 | Búsqueda de dosis y farmacocinética de XL184 (cabozantinib) con temozolomida y radioterapia en glioblastoma de primera línea. Aporta datos de seguridad de la combinación, pero no evalúa la eficacia de temozolomida sola. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [15758009](https://pubmed.ncbi.nlm.nih.gov/15758009/) | 2005 | ECA | N Engl J Med | Radioterapia sola frente a radioterapia con temozolomida concomitante y adyuvante en glioblastoma; es la base del tratamiento estándar actual. |
| [19269895](https://pubmed.ncbi.nlm.nih.gov/19269895/) | 2009 | ECA (seguimiento a largo plazo) | Lancet Oncol | Análisis a 5 años del ensayo EORTC-NCIC en glioblastoma con temozolomida más radioterapia. |
| [30782343](https://pubmed.ncbi.nlm.nih.gov/30782343/) | 2019 | ECA Fase 3 | Lancet | Lomustina más temozolomida frente a temozolomida estándar en glioblastoma con promotor de MGMT metilado (CeTeG/NOA-09). |
| [22578793](https://pubmed.ncbi.nlm.nih.gov/22578793/) | 2012 | ECA Fase 3 | Lancet Oncol | Temozolomida sola frente a radioterapia sola en adultos mayores con astrocitoma maligno (NOA-08). |
| [26670971](https://pubmed.ncbi.nlm.nih.gov/26670971/) | 2015 | ECA | JAMA | Campos de tratamiento tumoral (TTFields) más temozolomida frente a temozolomida sola como mantenimiento en glioblastoma. |
| [24552317](https://pubmed.ncbi.nlm.nih.gov/24552317/) | 2014 | ECA | N Engl J Med | Bevacizumab añadido al esquema con temozolomida y radioterapia en glioblastoma recién diagnosticado. |
| [35849035](https://pubmed.ncbi.nlm.nih.gov/35849035/) | 2023 | ECA Fase 3 | Neuro-oncology | Depatuxizumab mafodotina en glioblastoma con EGFR amplificado, con temozolomida como base del tratamiento. |
| [40779733](https://pubmed.ncbi.nlm.nih.gov/40779733/) | 2025 | ECA Fase 2/3 | J Clin Oncol | Bloqueo dual de puntos de control inmunitario en glioblastoma con MGMT no metilado (NRG BN007); temozolomida es el brazo comparador. |
| [10561351](https://pubmed.ncbi.nlm.nih.gov/10561351/) | 1999 | Ensayo Fase 2 | J Clin Oncol | Eficacia y seguridad de temozolomida en astrocitoma anaplásico u oligoastrocitoma anaplásico en primera recaída. |
| [36809318](https://pubmed.ncbi.nlm.nih.gov/36809318/) | 2023 | Revisión | JAMA | Revisión sobre glioblastoma y otras neoplasias cerebrales primarias malignas en adultos. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20001038 | TEMODAL® CÁPSULAS 140 MG (Merck Sharp & Dohme LLC) | Cápsula dura | Solo figura "TEMOZOLOMIDA"; el texto de la indicación no está detallado |

Los cinco registros revisados corresponden al mismo número sanitario, por lo que se muestra una sola fila. El total informado en Colombia es de 20 registros.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (agente alquilante que daña el ADN) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar el prospecto; en general se vigilan hemograma y función hepática y renal |
| Protección en Manejo | Seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay evidencia sólida: un ensayo de Fase 3 completado (n=500) y varios ensayos aleatorizados publicados, entre ellos el de Stupp en glioblastoma. Pero la indicación aprobada localmente no está detallada y falta información de seguridad, así que conviene avanzar con controles.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto del INVIMA (advertencias y contraindicaciones), ya que sin él no se puede completar la revisión de seguridad.
- Confirmar las indicaciones autorizadas frente a la etiqueta regulatoria.
- Completar los datos del mecanismo de acción desde DrugBank.
- Estratificar el análisis por estado de MGMT y por grado tumoral, dado que la literatura se centra en glioblastoma y no en astrocitoma de menor grado.

Como nota aparte, la segunda predicción del modelo, **neoplasia de cauda equina** (puntaje 99.30%), queda en **Hold** con nivel L4. Su único respaldo relevante es un reporte de caso en ependimoma mixopapilar espinal recurrente.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

