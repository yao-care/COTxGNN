---
layout: default
title: Carbamazepine
parent: Evidencia Moderada (L3-L4)
nav_order: 135
evidence_level: L4
indication_count: 3
last_modified_at: 2026-11-24
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
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 4 de 5) |
| Número de Registros Sanitarios | 5 (vigentes: 4) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Carbamazepine (traducción no oficial): «Tegretol ha demostrado propiedades anticonvulsivas en ratas y ratones con convulsiones inducidas eléctrica y químicamente. Parece actuar reduciendo las respuestas polisinápticas y bloqueando la potenciación postetánica. […] El metabolito principal de Tegretol, la carbamazepina-10,11-epóxido, tiene actividad anticonvulsiva, según se ha demostrado en varios modelos animales in vivo de convulsiones.» Texto original en inglés: "Tegretol has demonstrated anticonvulsant properties in rats and mice with electrically and chemically induced seizures. It appears to act by reducing polysynaptic responses and blocking the post-tetanic potentiation. […] The principal metabolite of Tegretol, carbamazepine-10,11-epoxide, has anticonvulsant activity as demonstrated in several in vivo animal models of seizures." ([DailyMed: Tegretol (carbamazepine) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8d409411-aa9f-4f3a-a52c-fbcb0c3ec053), versión del 2026-08-20; consultado el 2026-11-19). Según el conocimiento farmacológico general, carbamazepina bloquea los canales de sodio dependientes de voltaje, lo que reduce las descargas neuronales repetitivas. Es tratamiento de primera línea en la neuralgia del trigémino y se usa en epilepsia focal.

La literatura recuperada trata de neuralgia del trigémino causada por tumores o lesiones compresivas (schwannoma, meningioma, lipoma, quiste dermoide, linfoma, melanoma). En esos casos carbamazepina se usa para controlar el dolor, y en varios reportes el control fue insuficiente o el tumor siguió progresando. No hay evidencia de que actúe sobre el tumor.

Por ello, el puntaje alto del modelo probablemente refleja la asociación del fármaco con la neuralgia del trigémino y no una actividad contra la neoplasia. La plausibilidad mecanística es **sintomática e indirecta**.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Se muestran las publicaciones más relevantes de las 20 recuperadas (la evidencia es de bajo nivel; predominan reportes de caso).

<!-- review:begin co-lic-20261105-carbamazepine-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Ambos registros pertenecen a Novartis Pharma AG y están cancelados; no hay registros vigentes." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-carbamazepine-2 -->

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

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 227365 | TEGRETOL® RETARD DE 400 MG | TABLETA DE LIBERACION PROLONGADA | CARBAMAZEPINA | Vigente |
| 227376 | TEGRETOL RETARD DE 200 MG | TABLETA DE LIBERACION PROLONGADA | CARBAMAZEPINA | Vigente |
| 44969 | CARBAMAZEPINA TABLETAS | TABLETA | CARBAMAZEPINA | Vigente |
| 56106 | CARBAMAZEPINA 2% SUSPENSIÓN ORAL | SUSPENSION ORAL | CARBAMAZEPINA | Vigente |
| 226679 | TEGRETOL ® 2% SUSPENSION | SUSPENSION ORAL | CARBAMAZEPINA | Perdida Fuerza Ejec |

Se muestran los 5 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

- **Contraindicaciones y condiciones de riesgo (según relaciones del grafo de conocimiento, no texto del prospecto):** trastornos hematológicos (neutropenia, agranulocitosis, pancitopenia, trombocitopenia, anemia), enfermedad hepática y de la vesícula biliar, enfermedad renal y función renal alterada, trastornos de la conducción cardíaca (bloqueo auriculoventricular), enfermedad coronaria, hipertensión, glaucoma e hipertensión ocular, y síndrome de secreción inadecuada de ADH.
- **Interacciones farmacológicas:** la consulta se completó y solo registró una interacción farmacológica con el receptor FZD8 (sin nivel de gravedad). No se identificaron interacciones con otros medicamentos. La literatura menciona además que carbamazepina es inductor enzimático hepático, con interacciones relevantes, por ejemplo con anticonceptivos hormonales.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia es de nivel L4: no hay ensayos clínicos y la literatura consiste en reportes de caso y revisiones. Carbamazepina trata el dolor de la neuralgia del trigémino pero no la neoplasia, por lo que el reposicionamiento como terapia contra el tumor no está respaldado.

<!-- review:begin co-lic-20261031-carbamazepine-1 -->

> **Corrección de revisión (2026-10-31)**: Texto original: "Carbamazepina trata el dolor de la neuralgia del trigémino pero no la neoplasia, por lo que el reposicionamiento como terapia contra el tumor no está respaldado. Además, el mercado colombiano solo tiene registros cancelados." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-10-31. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261031-carbamazepine-1 -->

**Para avanzar se necesita:**
- Definir si el objetivo es el control sintomático del dolor (indicación ya conocida) o un efecto antitumoral (sin respaldo).
- Obtener el prospecto oficial para advertencias y contraindicaciones.
- Confirmar el mecanismo de acción con datos de DrugBank.
- Verificar el estado regulatorio.
- Revisar candidatos alternativos con mayor respaldo, como epilepsias reflejas (startle, lectura), donde existen series clínicas con carbamazepina, aunque también con evidencia de nivel L4.

<!-- review:begin co-lic-20261105-carbamazepine-3 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Verificar el estado regulatorio, dado que los dos registros están cancelados." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-carbamazepine-3 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-10-31 | Eliminado: "Además, el mercado colombiano solo tiene registros cancelados" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Ambos registros pertenecen a Novartis Pharma AG y están cancelados; no hay registros vigentes" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "dado que los dos registros están cancelados" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Tegretol (carbamazepine) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8d409411-aa9f-4f3a-a52c-fbcb0c3ec053) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

