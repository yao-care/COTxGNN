---
layout: default
title: Carbamazepine
parent: Evidencia Moderada (L3-L4)
nav_order: 135
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-29
description: "Carbamazepine: nueva indicación predicha, Neoplasia del nervio trigémino (nivel de evidencia L4). Indicación original: Carbamazepina"
monitor_inn: "Carbamazepine"
predicted_indications: ["trigeminal nerve neoplasm", "beta-ketothiolase deficiency", "Rett syndrome, congenital variant"]
---

# Carbamazepine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **3** 
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

## Carbamazepina: De Antiepiléptico (Registro INVIMA "Carbamazepina") a Neoplasia del Nervio Trigémino
{: .text-alpha }

## Resumen en Una Frase

Carbamazepina es un antiepiléptico de uso establecido, registrado en Colombia bajo la denominación "carbamazepina" (productos Tegretol), cuyo uso conocido incluye el tratamiento de convulsiones y de la neuralgia del trigémino.
El modelo TxGNN predice que podría ser efectivo para **neoplasia del nervio trigémino**, con **0 ensayos clínicos** y **20 publicaciones** recuperadas, casi todas reportes de caso o revisiones sobre neuralgia del trigémino secundaria a tumores.
La relación es sintomática e indirecta: el fármaco alivia el dolor neuropático, pero no tiene efecto antineoplásico.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Carbamazepina (el registro INVIMA no detalla la indicación; uso conocido: epilepsia y neuralgia del trigémino) |
| Nueva Indicación Predicha | Neoplasia del nervio trigémino |
| Puntaje de Predicción TxGNN | 1.0000 |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 1) |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada para este informe. Según el conocimiento farmacológico general, carbamazepina bloquea los canales de sodio dependientes de voltaje, lo que reduce las descargas neuronales repetitivas. Es tratamiento de primera línea en la neuralgia del trigémino y se usa en epilepsia focal.

La literatura recuperada trata de neuralgia del trigémino causada por tumores o lesiones compresivas (schwannoma, meningioma, lipoma, quiste dermoide, linfoma, melanoma). En esos casos carbamazepina se usa para controlar el dolor, y en varios reportes el control fue insuficiente o el tumor siguió progresando. No hay evidencia de que actúe sobre el tumor.

Por ello, el puntaje alto del modelo probablemente refleja la asociación del fármaco con la neuralgia del trigémino y no una actividad contra la neoplasia. La plausibilidad mecanística es **sintomática e indirecta**.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Se muestran las publicaciones más relevantes de las 20 recuperadas (la evidencia es de bajo nivel; predominan reportes de caso).

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36824641](https://pubmed.ncbi.nlm.nih.gov/36824641/) | 2022 | Revisión | Acta Clinica Croatica | Opciones de tratamiento de la neuralgia del trigémino, que puede deberse a compresión vascular o a un proceso tumoral |
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Revisión | Expert Rev Neurother | Revisión de los tratamientos médicos y quirúrgicos de la neuralgia del trigémino |
| [30741017](https://pubmed.ncbi.nlm.nih.gov/30741017/) | 2023 | Reporte de caso | Br J Neurosurg | Linfoma primario del nervio trigémino con dolor facial; carbamazepina no mejoró los síntomas |
| [25142539](https://pubmed.ncbi.nlm.nih.gov/25142539/) | 2014 | Reporte de caso | Rinsho Shinkeigaku | Linfoma con diseminación perineural; el dolor mejoró inicialmente con carbamazepina y luego dejó de responder |
| [15235745](https://pubmed.ncbi.nlm.nih.gov/15235745/) | 2004 | Reporte de caso | Arq Neuropsiquiatr | Melanoma primario de la cavidad de Meckel; dolor no aliviado por carbamazepina |
| [25433061](https://pubmed.ncbi.nlm.nih.gov/25433061/) | 2014 | Reporte de caso/revisión | No Shinkei Geka | Lipoma del ángulo pontocerebeloso; dolor mal controlado por efectos secundarios de carbamazepina |
| [33989821](https://pubmed.ncbi.nlm.nih.gov/33989821/) | 2021 | Reporte de caso | World Neurosurg | Meningioma petroclival con neuralgia del trigémino, resecado por abordaje de Kawase |
| [32454201](https://pubmed.ncbi.nlm.nih.gov/32454201/) | 2020 | Reporte de caso | World Neurosurg | Resección endoscópica de schwannoma de la fosa pterigopalatina |
| [3181365](https://pubmed.ncbi.nlm.nih.gov/3181365/) | 1988 | Preclínico (rata) | Exp Neurol | Carbamazepina inhibe la actividad espontánea en neuromas experimentales |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 226679 (cancelado) | TEGRETOL® 2% SUSPENSION | Suspensión oral | CARBAMAZEPINA |
| 227365 (cancelado) | TEGRETOL® RETARD DE 400 MG | Tableta de liberación prolongada | CARBAMAZEPINA |

Ambos registros pertenecen a Novartis Pharma AG y están cancelados; no hay registros vigentes.

---

## Consideraciones de Seguridad

- **Contraindicaciones y condiciones de riesgo (según relaciones del grafo de conocimiento, no texto del prospecto):** trastornos hematológicos (neutropenia, agranulocitosis, pancitopenia, trombocitopenia, anemia), enfermedad hepática y de la vesícula biliar, enfermedad renal y función renal alterada, trastornos de la conducción cardíaca (bloqueo auriculoventricular), enfermedad coronaria, hipertensión, glaucoma e hipertensión ocular, y síndrome de secreción inadecuada de ADH.
- **Interacciones farmacológicas:** la consulta se completó y solo registró una interacción farmacológica con el receptor FZD8 (sin nivel de gravedad). No se identificaron interacciones con otros medicamentos. La literatura menciona además que carbamazepina es inductor enzimático hepático, con interacciones relevantes, por ejemplo con anticonceptivos hormonales.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia es de nivel L4: no hay ensayos clínicos y la literatura consiste en reportes de caso y revisiones. Carbamazepina trata el dolor de la neuralgia del trigémino pero no la neoplasia, por lo que el reposicionamiento como terapia contra el tumor no está respaldado. Además, el mercado colombiano solo tiene registros cancelados.

**Para avanzar se necesita:**
- Definir si el objetivo es el control sintomático del dolor (indicación ya conocida) o un efecto antitumoral (sin respaldo).
- Obtener el prospecto oficial para advertencias y contraindicaciones.
- Confirmar el mecanismo de acción con datos de DrugBank.
- Verificar el estado regulatorio, dado que los dos registros están cancelados.
- Revisar candidatos alternativos con mayor respaldo, como epilepsias reflejas (startle, lectura), donde existen series clínicas con carbamazepina, aunque también con evidencia de nivel L4.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

