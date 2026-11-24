---
layout: default
title: Melphalan
parent: Solo Predicción del Modelo (L5)
nav_order: 426
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-24
description: "Melphalan: nueva indicación predicha, Carcinoma de mama femenino (nivel de evidencia L5). Indicación original: Melphalan"
monitor_inn: "melphalan"
predicted_indications: ["female breast carcinoma", "rectum mucinous adenocarcinoma", "colon mucinous adenocarcinoma", "gallbladder mucinous adenocarcinoma", "cervical mucinous adenocarcinoma", "endometrial mucinous adenocarcinoma"]
---

# Melphalan
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Melfalán: De Indicación Registrada (Melphalan) a Carcinoma de Mama Femenino
{: .text-alpha }

## Resumen en Una Frase

Melfalán es un agente alquilante antineoplásico. El modelo TxGNN predice que podría ser efectivo para **tumor de células germinales gonadal**, con **7 ensayos clínicos** y **1 publicación** de relevancia muy limitada. Los ensayos evalúan regímenes de quimioterapia combinada a dosis altas, por lo que el aporte propio del melfalán no puede aislarse.

<!-- review:begin co-lic-20261105-melphalan-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Melfalán es un agente alquilante antineoplásico que en Colombia contó con registros sanitarios de la sustancia "melphalan" (hoy todos cancelados)." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 7 registros sanitarios (vigentes: 7); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-melphalan-1 -->

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Melphalan (el registro sanitario no detalla la indicación en texto) |
| Nueva Indicación Predicha | Tumor de células germinales gonadal |
| Puntaje de Predicción TxGNN | 0.9967 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 7 de 7) |
| Número de Registros Sanitarios | 7 (vigentes: 7) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Melphalan (traducción no oficial): «El melfalán es un agente alquilante del tipo bis-cloroetilamina. En consecuencia, su citotoxicidad parece estar relacionada con el grado de entrecruzamiento entre cadenas del ADN, probablemente mediante la unión en la posición N 7 de la guanina.» Texto original en inglés: "Melphalan is an alkylating agent of the bischloroethylamine type. As a result, its cytotoxicity appears to be related to the extent of its interstrand cross-linking with DNA, probably by binding at the N 7 position of guanine." ([DailyMed: Evomela (melphalan) prescribing information, Acrotech Biopharma Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=69f55869-dc11-408e-8fc7-47634269a52c), versión del 2026-09-15; consultado el 2026-11-19). Según la información conocida, el melfalán es un agente alquilante bifuncional que entrecruza el ADN e impide la división de las células tumorales.

Los tumores de células germinales son muy sensibles a la quimioterapia. Los regímenes de dosis altas con agentes alquilantes y rescate con células madre autólogas son una estrategia establecida de rescate en enfermedad recidivante. Esto es coherente con el puntaje tan alto del modelo.

Una limitación importante: la evidencia proviene de regímenes combinados a dosis altas (por ejemplo, con gemcitabina, docetaxel y carboplatino), por lo que no se puede atribuir el beneficio al melfalán por sí solo.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00936936](https://clinicaltrials.gov/study/NCT00936936) | Fase 2 | Completado | 64 | Dos ciclos de quimioterapia a dosis altas (gemcitabina, docetaxel, melfalán, carboplatino; luego ifosfamida, carboplatino, etopósido) en tumores germinales recidivantes de mal pronóstico |
| [NCT00060255](https://clinicaltrials.gov/study/NCT00060255) | Fase 2 | Completado | 451 | Trasplante autólogo con ocho regímenes de dosis altas en neoplasias hematológicas y tumores sólidos seleccionados; los tumores germinales son solo un subgrupo |
| [NCT00003425](https://clinicaltrials.gov/study/NCT00003425) | Fase 1/2 | Completado | 25 | Escalada de dosis de melfalán con rescate de células madre y amifostina en tumores sólidos |
| [NCT00638898](https://clinicaltrials.gov/study/NCT00638898) | Fase 1 | Completado | 25 | Busulfán, melfalán y topotecán con trasplante autólogo en tumores avanzados o recurrentes |
| [NCT00536601](https://clinicaltrials.gov/study/NCT00536601) | No aplica | Completado | 174 | Dosis altas con o sin irradiación corporal total antes del trasplante autólogo; población amplia |
| [NCT00002750](https://clinicaltrials.gov/study/NCT00002750) | Fase 1 | Completado | 6 | Melfalán intratecal en meningitis neoplásica recurrente; vía y contexto distintos |
| [NCT00003926](https://clinicaltrials.gov/study/NCT00003926) | Fase 1 | Terminado | 13 | Amifostina como quimioprotector con trasplante; enfoque en cuidados de soporte |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [14151951](https://pubmed.ncbi.nlm.nih.gov/14151951/) | 1964 | Otro (función hipofisaria) | Acta - Unio Internationalis Contra Cancrum | Estudio antiguo sobre la influencia de fármacos hormonales y alquilantes en la función estimulante folicular de la hipófisis; sin resumen disponible y de relevancia clínica limitada |

---

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 20161853 | NOZOMI ® 50 MG | POLVO LIOFILIZADO PARA RECONSTITUIR A SOLUCION INYECTABLE | MELPHALAN | Vigente |
| 20167599 | MELFALAN 50 MG POLVO LIOFILIZADO PARA RECONSTITUIR A SOLUCION INYECTABLE | POLVO LIOFILIZADO PARA RECONSTITUIR A SOLUCION INYECTABLE | MELPHALAN | Vigente |
| 20176265 | MYELKILAN® 50MG POLVO PARA INYECCIÓN | POLVO LIOFILIZADO PARA RECONSTITUIR A SOLUCION INYECTABLE | MELPHALAN | Vigente |
| 20197131 | MELFASEVEN® 50MG POLVO LIOFILIZADO PARA INYECCIÓN | POLVO ESTERIL PARA RECONSTITUIR A SOLUCION INYECTABLE | MELPHALAN | Vigente |
| 20269433 | MELFALÁNPARA INYECCIÓN POLVO 50 MG/VIAL LIOFILIZADO PARA INYECCIÓN | POLVO LIOFILIZADO | MELPHALAN | Vigente |

Se muestran 5 de 7 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (agente alquilante, mostaza nitrogenada) |
| Riesgo de Mielosupresión | Alto. Los datos del grafo de conocimiento asocian el fármaco con contraindicaciones en neutropenia, leucopenia, trombocitopenia y anemia, y los regímenes de dosis altas requieren rescate con células madre |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal; vigilancia de función pulmonar |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

- **Condiciones con relación de contraindicación en el grafo de conocimiento** (no provienen del texto del prospecto): enfermedad renal, trombocitopenia, anemia (incluida la macrocítica y la hemolítica), leucopenia, agranulocitosis, neutropenia (incluidas varias formas congénitas), enfermedad pulmonar intersticial, fibrosis pulmonar, lesión hepática inducida por fármacos y vasculitis.
- **Interacciones farmacológicas**: se identificaron 234 interacciones. Entre las principales:
  - Moderadas: anfotericina B (y sus formulaciones lipídicas, de sulfato de colesterilo y liposomal).
  - Leves: cimetidina, levofloxacino, sulfato de zinc y gluconato de zinc.
  - Nivel desconocido (ejemplos): omeprazol, pantoprazol, prednisona, metformina, morfina y vancomicina.
- Una revisión de 1984 señala que los agentes alquilantes como el melfalán tienen una de las tasas más altas de segundas neoplasias, sobre todo leucemias agudas.

<!-- review:begin co-lic-20261105-melphalan-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Se muestran 5 de los 7 registros; los otros dos (Myelkilan® y Melfaseven®) también están cancelados." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 7 registros sanitarios (vigentes: 7); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-melphalan-2 -->

Las advertencias y contraindicaciones del prospecto no están disponibles; consultar el prospecto para la información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Aunque el puntaje de TxGNN es muy alto y existe un ensayo de Fase 2 completado en tumores germinales recidivantes, se trata de un régimen combinado en el que no se puede aislar el efecto del melfalán. Además, faltan los datos de seguridad del prospecto.

<!-- review:begin co-lic-20261105-melphalan-3 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, hoy no hay ningún registro sanitario vigente en Colombia y faltan los datos de seguridad del prospecto." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 7 registros sanitarios (vigentes: 7); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-melphalan-3 -->

**Para avanzar se necesita:**
- Resultados publicados del ensayo NCT00936936 y análisis de la contribución específica del melfalán.
- Información del prospecto (advertencias y contraindicaciones) y datos del mecanismo de acción.
- Aclarar la situación regulatoria: el medicamento está comercializado, con 7 licencias válidas de 7 en este país; verificar el estado de cada licencia antes de cualquier trámite de registro o importación.
- Comparación con los esquemas actuales de rescate en tumores germinales (por ejemplo, regímenes de dosis altas con carboplatino y etopósido).
- Un plan de monitoreo hematológico, renal y pulmonar para poblaciones de riesgo.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "que en Colombia contó con registros sanitarios de la sustancia "melphalan" (hoy todos cancelados)" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Se muestran 5 de los 7 registros; los otros dos (Myelkilan® y Melfaseven®) también están cancelados" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "hoy no hay ningún registro sanitario vigente en Colombia y" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Evomela (melphalan) prescribing information, Acrotech Biopharma Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=69f55869-dc11-408e-8fc7-47634269a52c) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

