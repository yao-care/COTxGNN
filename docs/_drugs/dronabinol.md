---
layout: default
title: Dronabinol
parent: Solo Predicción del Modelo (L5)
nav_order: 237
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Dronabinol: nueva indicación predicha, Trastorno de migraña (migraine disorder) (nivel de evidencia L5). Indicación original: No especificada"
monitor_inn: "dronabinol"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "headache disorder", "trigeminal autonomic cephalalgia", "pulmonary hypertension", "hypertrichosis (disease)", "migraine with or without aura, susceptibility to", "kyphoscoliotic heart disease", "Ambras type hypertrichosis universalis congenita", "atrophoderma vermiculata"]
---

# Dronabinol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Dronabinol: De Indicación No Especificada a Trastorno de Migraña
{: .text-alpha }

## Resumen en Una Frase

Dronabinol (delta-9-tetrahidrocannabinol) contó en Colombia con registros sanitarios en cápsula blanda (marca LAXENOL), aunque el texto de indicación registrado solo menciona el nombre del principio activo y no una enfermedad concreta.
El modelo TxGNN predice que podría ser efectivo para **trastorno de migraña**, con **1 ensayo clínico** de Fase 2 y **1 publicación** (una encuesta) que respaldan esta dirección de forma limitada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro solo indica "DRONABINOL") |
| Nueva Indicación Predicha | Trastorno de migraña (migraine disorder) |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L3 (con evidencia débil: un ensayo de Fase 2 sin resultados disponibles y una encuesta) |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 4 (0 vigentes, 4 cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Dronabinol es el delta-9-tetrahidrocannabinol (THC), un agonista de los receptores cannabinoides CB1 y CB2. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en las fuentes compiladas para este informe, pero este perfil farmacológico es ampliamente conocido.

El sistema endocannabinoide modula la señalización nociceptiva en la vía trigeminovascular, la liberación de serotonina y la sensibilización central del dolor, procesos relevantes en la fisiopatología de la migraña. Esto es coherente con el puntaje alto del modelo, aunque se trata de una predicción computacional y no de una prueba clínica.

Como la indicación original no está detallada en el registro colombiano, no es posible comparar directamente la enfermedad original con la nueva. La plausibilidad se apoya en la biología de los cannabinoides en el dolor y la regulación neurovascular.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00123201](https://clinicaltrials.gov/study/NCT00123201) | Fase 2 | Completado | No reportada | Estudio multicéntrico, aleatorizado, doble ciego y controlado con placebo de dronabinol en inhalador de dosis medida (MDI) para el tratamiento agudo de migraña de moderada a grave (2005-09 a 2007-03). No se dispone de resultados; la intervención, la población y los desenlaces requieren verificación. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10575286](https://pubmed.ncbi.nlm.nih.gov/10575286/) | 1999 | Encuesta | Forschende Komplementärmedizin | Encuesta estandarizada sobre el uso médico de productos de cannabis en países de habla alemana; evidencia indirecta y de bajo grado para migraña. |

Para otras indicaciones relacionadas (cefalea en general y cefalea en racimos) hay una revisión narrativa ([28281107](https://pubmed.ncbi.nlm.nih.gov/28281107/), 2017, *Current Pain and Headache Reports*) y un reporte de caso ([19220500](https://pubmed.ncbi.nlm.nih.gov/19220500/), 2009, *Headache*) en que un paciente con cefalea en racimos refractaria abortó sus ataques con cannabis recreativo y luego con dronabinol. Son evidencias de bajo grado que no permiten afirmar eficacia.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 19967436 | LAXENOL 2.5 MG | Cápsula blanda | DRONABINOL | Cancelado |
| 19967437 | LAXENOL 5 MG | Cápsula blanda | DRONABINOL | Cancelado |
| 20233134 | LAXENOL® 5 MG | Cápsula blanda | DRONABINOL | Cancelado |
| 19967647 | LAXENOL 10 MG | Cápsula blanda | DRONABINOL | Cancelado |

Todos los registros pertenecen a PROCAPS S.A. y actualmente ninguno está vigente.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** el grafo de conocimiento del modelo asocia dronabinol con contraindicación en hipertensión, hipotensión, epilepsia, trastornos de ansiedad, trastornos neuróticos, trastorno distímico, trastorno bipolar, trastornos afectivos mayores, esquizofrenia y abuso o dependencia de sustancias.
- **Interacciones farmacológicas:** se identificaron 357 interacciones potenciales. Destacan:
  - **Mayor:** tramadol.
  - **Moderadas (ejemplos):** fentanilo, codeína, dihidrocodeína, alfentanilo, etanol, gabapentina, fluvoxamina, clorfeniramina, butalbital, nifedipino, furosemida, fosfenitoína, acebutolol y aldesleukina. En general predomina el riesgo de depresión del sistema nervioso central y de efectos cardiovasculares aditivos.
- Dronabinol puede causar taquicardia e hipotensión, aspecto de seguridad cardiovascular relevante.

No se dispone de advertencias ni contraindicaciones del prospecto; consultar el prospecto para esa información.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia clínica se limita a un ensayo de Fase 2 sin resultados disponibles y a literatura indirecta de bajo grado. Además, no hay registros vigentes en Colombia y falta la información de seguridad del prospecto, lo que impide avanzar a una evaluación de seguridad.

**Para avanzar se necesita:**
- Obtener el prospecto oficial desde INVIMA (advertencias y contraindicaciones).
- Confirmar los datos de mecanismo de acción en DrugBank.
- Verificar la intervención, la población y los resultados de NCT00123201.
- Revisar la viabilidad regulatoria, dado que todos los registros están cancelados y la vía de administración del ensayo (inhalador) difiere de la cápsula blanda.
- Evaluar el riesgo de las contraindicaciones neuropsiquiátricas y cardiovasculares en pacientes con migraña.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

