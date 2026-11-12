---
layout: default
title: Dacarbazine
parent: Solo Predicción del Modelo (L5)
nav_order: 190
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
monitor_inn: "Dacarbazine"
predicted_indications: ["upper aerodigestive tract neoplasm"]
description: "Dacarbazine: nueva indicación predicha, Neoplasia del tracto aerodigestivo superior (nivel de evidencia L5). Indicación original: No especificada en el registro (el texto aprobado solo indica \"Dacarb"
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

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Dacarbazina: De Indicación No Especificada (Registro INVIMA) a Neoplasia del Tracto Aerodigestivo Superior
{: .text-alpha }

## Resumen en Una Frase

Dacarbazina es un agente alquilante citotóxico cuyos registros sanitarios en Colombia figuran solo con el nombre del principio activo, sin una indicación detallada.
El modelo TxGNN predice que podría ser efectivo para **neoplasia del tracto aerodigestivo superior**,
pero actualmente no hay ensayos clínicos registrados y la literatura recuperada es **indirecta** (20 publicaciones, ninguna con evidencia directa en esta población).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto aprobado solo indica "Dacarbazina") |
| Nueva Indicación Predicha | Neoplasia del tracto aerodigestivo superior |
| Puntaje de Predicción TxGNN | 0.9926 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 4 de 6) |
| Número de Registros Sanitarios | 6 (vigentes: 4) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, dacarbazina es un agente alquilante: un profármaco que se activa a MTIC y metila el ADN. Su eficacia está establecida en melanoma y linfoma de Hodgkin (esquema ABVD), y hay reportes en tumores neuroendocrinos como el carcinoma medular de tiroides y el paraganglioma.

La relación con la nueva indicación es **indirecta y dependiente de la histología**. La literatura recuperada describe tumores sensibles a dacarbazina que pueden surgir o comprometer la cabeza y el cuello: melanoma mucoso, linfoma de Hodgkin de cabeza y cuello y paraganglioma de cabeza y cuello. No hay evidencia de un efecto directo sobre el carcinoma escamocelular, el cáncer dominante del tracto aerodigestivo superior.

El puntaje de 0.9926 es solo una predicción computacional y no está respaldado por ningún ensayo en esta indicación. Debe interpretarse con cautela.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Se priorizan los estudios más relevantes; ninguno evalúa directamente dacarbazina en neoplasia del tracto aerodigestivo superior.

<!-- review:begin co-lic-20261105-dacarbazine-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Los seis registros sanitarios están cancelados; actualmente no hay productos vigentes." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 6 registros sanitarios (vigentes: 4); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-dacarbazine-1 -->

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [41481311](https://pubmed.ncbi.nlm.nih.gov/41481311/) | 2026 | ECA Fase 3 | JAMA Oncol | Toripalimab vs dacarbazina como primera línea en melanoma acral avanzado (dacarbazina como comparador; población no aerodigestiva) |
| [31621203](https://pubmed.ncbi.nlm.nih.gov/31621203/) | 2019 | Observacional prospectivo | Cancer Med | Radioterapia con iones de carbono más quimioterapia DAV (dacarbazina, nimustina, vincristina) en melanoma mucoso de cabeza y cuello, 21 pacientes |
| [7826911](https://pubmed.ncbi.nlm.nih.gov/7826911/) | 1994 | Serie de casos | Ann Oncol | Dacarbazina más 5-fluorouracilo en carcinoma medular de tiroides avanzado |
| [20564093](https://pubmed.ncbi.nlm.nih.gov/20564093/) | 2010 | Cohorte retrospectiva | Cancer | Características y desenlaces del linfoma de Hodgkin en sitios ganglionares y extraganglionares de cabeza y cuello |
| [34654328](https://pubmed.ncbi.nlm.nih.gov/34654328/) | 2024 | Cohorte | Ear Nose Throat J | Paragangliomas malignos de cabeza y cuello: experiencia de una sola institución (6 pacientes) |
| [11815960](https://pubmed.ncbi.nlm.nih.gov/11815960/) | 2002 | Preclínico | Cancer | Combinación de radioinmunoterapia y quimioterapia en xenoinjertos de carcinoma medular de tiroides; dacarbazina mostró la mayor actividad individual |
| [20627492](https://pubmed.ncbi.nlm.nih.gov/20627492/) | 2010 | Revisión | Clin Oncol | Revisión sobre carcinoma medular de tiroides |
| [12113649](https://pubmed.ncbi.nlm.nih.gov/12113649/) | 2002 | Revisión | Am J Clin Dermatol | Conceptos actuales en el manejo del melanoma |
| [20138008](https://pubmed.ncbi.nlm.nih.gov/20138008/) | 2010 | Revisión | Transfus Apher Sci | Linfoma de Hodgkin asociado a VIH, con frecuente compromiso extraganglionar de cabeza y cuello |
| [12845209](https://pubmed.ncbi.nlm.nih.gov/12845209/) | 2003 | Serie de casos | Onkologie | Metástasis mucosas de melanoma maligno (esófago, estómago, vejiga y amígdala palatina) |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20211561 | NEGORIX 200 MG | Polvo liofilizado para reconstituir a solución inyectable | Dacarbazina |
| 20080268 | CARBAVEN 200 | Polvo liofilizado para reconstituir a solución inyectable | Dacarbazina |
| 19961319 | DACARBAZINA 200 MG (Blau Farmacéutica) | Polvo liofilizado para reconstituir a solución inyectable | Dacarbazina |
| 224892 | DACARBAZINE (Medac GmbH) | Polvo liofilizado para reconstituir a solución inyectable | Dacarbazina |
| 20194844 | TREXTECH 200 MG | Polvo liofilizado para reconstituir a solución inyectable | Dacarbazina |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (agente alquilante) |
| Riesgo de Mielosupresión | Alto: los antecedentes de leucopenia, trombocitopenia y anemia figuran entre las contraindicaciones del grafo de conocimiento |
| Clasificación de Emetogenicidad | Alta (según la categoría general del fármaco) |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

- **Contraindicaciones relacionadas (grafo de conocimiento TxGNN, no texto de prospecto)**: enfermedad renal, piouréter, enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia, anemia (incluida la macrocítica), leucopenia, trombosis de la vena hepática y síndrome de Budd-Chiari.
- **Interacciones Farmacológicas**: se identificaron 100 interacciones. Las clasificadas son naltrexona (moderada) y levofloxacino (menor). Otras, como pantoprazol, morfina, metformina, omeprazol, palonosetrón, prednisona, simvastatina, aprepitant y ondansetrón, no tienen nivel de gravedad definido.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L4), sin ensayos clínicos y con literatura indirecta, centrada en melanoma, linfoma de Hodgkin y tumores neuroendocrinos. El carcinoma escamocelular, que predomina en esta región, no está respaldado. Además, falta información de seguridad del prospecto.

<!-- review:begin co-lic-20261105-dacarbazine-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, no hay registros vigentes en Colombia y falta información de seguridad del prospecto." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 6 registros sanitarios (vigentes: 4); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-dacarbazine-2 -->

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA con advertencias y contraindicaciones (brecha bloqueante para el tamizaje de seguridad).
- Completar el mecanismo de acción desde DrugBank.
- Definir las histologías específicas del tracto aerodigestivo superior donde dacarbazina podría ser relevante (p. ej., melanoma mucoso).
- Buscar estudios clínicos directos en esta población.
- Aclarar la viabilidad regulatoria y comercial, dado que el medicamento está comercializado y cuenta con 4 licencias vigentes.

<!-- review:begin co-lic-20261112-dacarbazine-1 -->

> **Corrección de revisión (2026-11-12)**: Texto original: "6 licencias vigentes" Corregido según los datos del INVIMA (Código Único de Medicamentos, datos al 2026-11-05): 6 registros sanitarios, de los cuales 4 vigentes y 1 vigentes pero temporalmente no comercializados; 1 perdieron fuerza ejecutoria o fueron cancelados. Las cifras actuales están en el Resumen rápido. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261112-dacarbazine-1 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Los seis registros sanitarios están cancelados; actualmente no hay productos vigentes" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "no hay registros vigentes en Colombia y" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-12 | Número de registros vigentes: 6 → 4 | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

