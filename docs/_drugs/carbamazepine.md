---
layout: default
title: Carbamazepine
parent: Evidencia Moderada (L3-L4)
nav_order: 113
evidence_level: L4
indication_count: 10
---

# Carbamazepine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
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

# Carbamazepina: De Epilepsia y Neuralgia del Trigémino a Neoplasia del Nervio Trigémino

## Resumen en Una Frase

La carbamazepina es un anticonvulsivante que se usa para tratar convulsiones y dolor neuropático como la neuralgia del trigémino.
El modelo TxGNN predice que podría ser efectiva para **neoplasia del nervio trigémino**, pero la evidencia es muy débil: **1 ensayo clínico** (sin relación directa con el fármaco) y **20 publicaciones** (casi todas reportes de caso).
El puntaje alto probablemente refleja cercanía con la neuralgia del trigémino y no un efecto antitumoral real.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Convulsiones, neuralgia del trigémino y dolor neuropático (el registro INVIMA solo indica "Carbamazepina", sin describir la indicación) |
| Nueva Indicación Predicha | Neoplasia del nervio trigémino |
| Puntaje de Predicción TxGNN | 99.998% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos. Según la información conocida, la carbamazepina bloquea los canales de sodio dependientes de voltaje y es tratamiento de primera línea para la neuralgia del trigémino. Su eficacia en esa indicación está comprobada.

La relación con la nueva indicación es indirecta. Los tumores del nervio trigémino, o los que lo comprimen, suelen causar dolor facial similar a la neuralgia. En ese contexto, la carbamazepina podría dar alivio sintomático del dolor. No hay evidencia de que actúe contra el tumor.

Por eso la predicción no parece una señal real de reposicionamiento. El puntaje alto probablemente proviene de la proximidad del tumor con la neuralgia del trigémino en el grafo de conocimiento. Varios reportes de caso muestran justamente lo contrario: la carbamazepina no controló el dolor de pacientes con linfoma, y en algunos casos el tumor se detectó después.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT06853119](https://clinicaltrials.gov/study/NCT06853119) | N/A | Aún sin reclutar | 120 | Estudio de resonancia magnética sobre cambios cerebrales en neuralgia del trigémino. No evalúa carbamazepina ni neoplasias. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36824641](https://pubmed.ncbi.nlm.nih.gov/36824641/) | 2022 | Revisión | Acta Clin Croat | Opciones de tratamiento de la neuralgia del trigémino; puede deberse a compresión vascular o a un tumor. |
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Revisión | Expert Rev Neurother | Tratamientos médicos y quirúrgicos de la neuralgia del trigémino. |
| [30741017](https://pubmed.ncbi.nlm.nih.gov/30741017/) | 2023 | Reporte de caso | Br J Neurosurg | Linfoma primario del nervio trigémino con dolor facial; la carbamazepina no mejoró los síntomas. |
| [25142539](https://pubmed.ncbi.nlm.nih.gov/25142539/) | 2014 | Reporte de caso | Rinsho Shinkeigaku | Linfoma con diseminación perineural que se presentó como neuralgia; mejoró al inicio con carbamazepina y luego dejó de responder. |
| [3181365](https://pubmed.ncbi.nlm.nih.gov/3181365/) | 1988 | Preclínico | Exp Neurol | En ratas, la carbamazepina intravenosa inhibió la actividad espontánea de neuromas experimentales (efecto sobre la excitabilidad nerviosa, no antitumoral). |
| [33989821](https://pubmed.ncbi.nlm.nih.gov/33989821/) | 2021 | Reporte de caso | World Neurosurg | Meningioma petroclival que causó neuralgia del trigémino; se trató con resección quirúrgica. |
| [26768887](https://pubmed.ncbi.nlm.nih.gov/26768887/) | 2016 | Reporte de caso | Turk Neurosurg | Adenoma hipofisario que se manifestó solo como neuralgia del trigémino. |
| [25433061](https://pubmed.ncbi.nlm.nih.gov/25433061/) | 2014 | Reporte de caso | No Shinkei Geka | Lipoma del ángulo pontocerebeloso; la carbamazepina no controló el dolor por efectos secundarios. |
| [12590697](https://pubmed.ncbi.nlm.nih.gov/12590697/) | 2003 | Reporte de caso | Neurosurgery | Granuloma sarcoideo del nervio trigémino que simulaba un schwannoma. |
| [27729607](https://pubmed.ncbi.nlm.nih.gov/27729607/) | 2016 | Reporte de caso | No Shinkei Geka | Quiste dermoide en la cavidad de Meckel con parálisis oculomotora y neuralgia del trigémino. |

---

## Información de Mercado en Colombia

Los cinco registros devueltos corresponden al mismo registro sanitario, por lo que se muestra una sola fila. El total informado es de 20 registros.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 226679 | TEGRETOL® 2% SUSPENSIÓN (Novartis Pharma AG) | Suspensión oral | Solo figura "Carbamazepina" (sin texto de indicación) |

También existe una presentación de tableta de liberación prolongada.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

El único registro de interacciones es una anotación farmacológica sobre el receptor FZD8 (vía Wnt), sin nivel de gravedad. No corresponde a una interacción medicamentosa clínica.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Ningún ensayo ni publicación respalda un efecto antitumoral de la carbamazepina en tumores del nervio trigémino. El único beneficio plausible es el alivio sintomático del dolor, que ya es un uso conocido y no constituye reposicionamiento.

**Para avanzar se necesita:**
- Definir si el objetivo es control del dolor asociado al tumor (uso ya establecido) o efecto antitumoral (sin base actual).
- Datos preclínicos de actividad antitumoral, si se quiere sostener esa hipótesis.
- Prospecto de INVIMA con advertencias y contraindicaciones.
- Datos detallados del mecanismo de acción (MOA).
- Considerar otras predicciones de este mismo análisis, como la epilepsia refleja de lectura o de sobresalto, que tienen mayor plausibilidad mecanística aunque tampoco tienen ensayos específicos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

