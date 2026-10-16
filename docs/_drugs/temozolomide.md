---
layout: default
title: Temozolomide
parent: Evidencia Alta (L1-L2)
nav_order: 610
evidence_level: L1
indication_count: 2
last_modified_at: 2026-10-14
description: "Temozolomide: nueva indicación predicha, Tumor astrocítico del adulto (adult astrocytic tumour) (nivel de evidencia L1). Indicación original: Temozolomida"
monitor_inn: "Temozolomide"
predicted_indications: ["adult astrocytic tumour", "cauda equina neoplasm"]
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

# Temozolomida: De Indicación Registrada (Temozolomida) a Tumor Astrocítico del Adulto

## Resumen en Una Frase

Temozolomida es un agente alquilante oral, registrado en Colombia bajo cuatro licencias sanitarias que hoy están todas canceladas. El modelo TxGNN predice que podría ser efectivo para **tumor astrocítico del adulto**, con **2 ensayos clínicos** y **20 publicaciones** que respaldan esta dirección. Esta indicación es en la práctica un uso ya establecido (estándar de tratamiento en glioma) y no un reposicionamiento propiamente dicho.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Temozolomida (el texto del registro sanitario no detalla la indicación clínica) |
| Nueva Indicación Predicha | Tumor astrocítico del adulto (adult astrocytic tumour) |
| Puntaje de Predicción TxGNN | 99.36% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 4 (0 vigentes, 4 cancelados) |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción del fármaco. Según la farmacología establecida, temozolomida es un agente alquilante oral que metila el ADN (posiciones O6-guanina, N7-guanina y N3-adenina). Las lesiones O6-metilguanina provocan citotoxicidad mediada por el sistema de reparación de errores de apareamiento (mismatch repair) en células tumorales con baja actividad de MGMT, es decir, con el promotor de MGMT metilado.

Este mecanismo es directamente relevante para los tumores astrocíticos, incluidos el glioblastoma y el astrocitoma anaplásico. La literatura recuperada confirma que la radioterapia con temozolomida concomitante y adyuvante es el tratamiento estándar del glioblastoma recién diagnosticado.

El puntaje de TxGNN (0.994) es coherente con la evidencia clínica. Como el texto del registro INVIMA solo dice "TEMOZOLOMIDA", no se puede contrastar formalmente la indicación original con la nueva.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00052455](https://clinicaltrials.gov/study/NCT00052455) | Fase 3 | Completado | 500 | Ensayo aleatorizado que compara temozolomida con PCV (procarbazina, lomustina y vincristina) en astrocitoma recurrente WHO grado III y IV. Evidencia directa. |
| [NCT00960492](https://clinicaltrials.gov/study/NCT00960492) | Fase 1 | Completado | 26 | Búsqueda de dosis de XL184 (cabozantinib) con temozolomida y radioterapia en glioblastoma de primera línea. Aporta poco a la eficacia de temozolomida. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [15758009](https://pubmed.ncbi.nlm.nih.gov/15758009/) | 2005 | ECA | N Engl J Med | Radioterapia con temozolomida concomitante y adyuvante frente a radioterapia sola en glioblastoma. |
| [19269895](https://pubmed.ncbi.nlm.nih.gov/19269895/) | 2009 | ECA | Lancet Oncol | Análisis a 5 años del ensayo EORTC-NCIC de fase 3 sobre supervivencia con temozolomida más radioterapia. |
| [22578793](https://pubmed.ncbi.nlm.nih.gov/22578793/) | 2012 | ECA | Lancet Oncol | NOA-08: temozolomida sola frente a radioterapia sola en astrocitoma maligno de ancianos (fase 3). |
| [30782343](https://pubmed.ncbi.nlm.nih.gov/30782343/) | 2019 | ECA | Lancet | CeTeG/NOA-09: lomustina-temozolomida frente a temozolomida estándar en glioblastoma con MGMT metilado (fase 3). |
| [26670971](https://pubmed.ncbi.nlm.nih.gov/26670971/) | 2015 | ECA | JAMA | Campos de tratamiento tumoral (TTFields) con temozolomida de mantenimiento frente a temozolomida sola. |
| [29260225](https://pubmed.ncbi.nlm.nih.gov/29260225/) | 2017 | ECA | JAMA | Efecto de TTFields con temozolomida de mantenimiento sobre la supervivencia en glioblastoma. |
| [24552317](https://pubmed.ncbi.nlm.nih.gov/24552317/) | 2014 | ECA | N Engl J Med | Bevacizumab añadido al tratamiento estándar con temozolomida en glioblastoma recién diagnosticado. |
| [39480453](https://pubmed.ncbi.nlm.nih.gov/39480453/) | 2024 | ECA | JAMA Oncol | Veliparib añadido a temozolomida en glioblastoma con MGMT metilado. |
| [34898238](https://pubmed.ncbi.nlm.nih.gov/34898238/) | 2022 | Guía clínica | J Clin Oncol | Guía ASCO-SNO sobre el tratamiento de tumores astrocíticos y oligodendrogliales difusos en adultos. |
| [27668386](https://pubmed.ncbi.nlm.nih.gov/27668386/) | 2016 | Revisión | Clin J Oncol Nurs | Panorama de la enfermedad y el tratamiento del glioblastoma. |

---

## Información de Mercado en Colombia

Las cuatro licencias están canceladas; actualmente no hay presentaciones vigentes.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20001038 | TEMODAL® Cápsulas 140 mg (Merck Sharp & Dohme) | Cápsula dura | TEMOZOLOMIDA (cancelado) |
| 19907390 | TEMODAL® Cápsulas 20 mg (Merck Sharp & Dohme) | Cápsula dura | TEMOZOLOMIDA (cancelado) |
| 20087083 | TEMITOMA 20 mg (Sun Pharmaceutical) | Cápsula dura | TEMOZOLOMIDA (cancelado) |
| 20196779 | MOZOLA® 20 mg (Eurofarma Colombia) | Cápsula dura | TEMOZOLOMIDA (cancelado) |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (agente alquilante) |
| Riesgo de Mielosupresión | Alto. Las asociaciones fármaco-enfermedad del grafo de conocimiento incluyen trombocitopenia, neutropenia, pancitopenia, agranulocitosis, anemia y anemia aplásica. |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Ítems de Monitoreo | Hemograma completo con diferencial (plaquetas y neutrófilos), función hepática y función renal |
| Protección en Manejo | Seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** insuficiencia hepática, trombocitopenia, neutropenia, agranulocitosis, anemia (incluida la macrocítica), neumocistosis, pancitopenia, linfopenia, síndrome mielodisplásico y anemia aplásica idiopática o aplásica.
- **Interacciones farmacológicas:** se identificaron 100 interacciones potenciales. La única de nivel moderado es **naltrexona**; **levofloxacino** es de nivel menor. El resto aparece con nivel no clasificado (por ejemplo calcitriol, pantoprazol, doxiciclina, clotrimazol, morfina, metformina, omeprazol, lansoprazol, prednisona, anfotericina B e hidrocortisona).

No se dispone de las advertencias y contraindicaciones del prospecto de INVIMA; consultar el prospecto para confirmarlas.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay varios ECA de fase 3 completados, entre ellos NCT00052455 y los estudios EORTC-NCIC y NOA-08, que respaldan el uso de temozolomida en tumores astrocíticos, por lo que el nivel de evidencia es L1. Sin embargo, esta indicación ya es un estándar de tratamiento, y los cuatro registros colombianos están cancelados.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA con advertencias y contraindicaciones oficiales, ya que su ausencia bloquea el tamizaje de seguridad.
- Confirmar el mecanismo de acción en DrugBank.
- Aclarar la situación regulatoria: por qué se cancelaron los registros y si existe otra vía de acceso al medicamento en Colombia.
- Definir un plan de monitoreo hematológico, dado el alto riesgo de mielosupresión.
- Revisar las interacciones de nivel moderado y las no clasificadas antes de su uso.

---

### Nota sobre la segunda predicción (neoplasia de la cola de caballo)

El modelo también predice **neoplasia de cauda equina** (puntaje 99.30%), pero con nivel de evidencia **L4**, sin ensayos clínicos y con un solo reporte de caso relevante (PMID 29270703, ependimoma mixopapilar espinal recurrente con respuesta a temozolomida). Las otras dos publicaciones recuperadas tratan de enfermedades distintas. Se clasifica como pregunta de investigación y no como candidata para avanzar.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

