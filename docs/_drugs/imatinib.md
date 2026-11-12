---
layout: default
title: Imatinib
parent: Solo Predicción del Modelo (L5)
nav_order: 335
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
description: "Imatinib: nueva indicación predicha, Fibrosarcoma cardíaco (heart fibrosarcoma) (nivel de evidencia L5). Indicación original: IMATINIB"
monitor_inn: "imatinib"
predicted_indications: ["heart fibrosarcoma", "fibroblastic neoplasm", "conventional fibrosarcoma", "kidney fibrosarcoma", "low grade fibromyxoid sarcoma", "liposarcoma", "liver fibrosarcoma", "autosomal recessive familial Mediterranean fever", "ovarian myxoid liposarcoma", "familial rhabdoid tumor"]
---

# Imatinib
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

## Imatinib: De Indicación Original (IMATINIB, sin detalle) a Fibrosarcoma Cardíaco
{: .text-alpha }

## Resumen en Una Frase

Imatinib es un inhibidor de tirosina quinasas (PDGFR, KIT y ABL) comercializado en Colombia como Glivec; el registro sanitario disponible solo indica "IMATINIB" como indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **fibrosarcoma cardíaco**, pero sin ensayos clínicos y con solo **1 publicación** (un comentario, no evidencia robusta) que respalda esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | IMATINIB (el registro no detalla la indicación) |
| Nueva Indicación Predicha | Fibrosarcoma cardíaco (heart fibrosarcoma) |
| Puntaje de Predicción TxGNN | 0.9994 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 7 de 9) |
| Número de Registros Sanitarios | 9 (vigentes: 7) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Imatinib inhibe las quinasas PDGFR, KIT y ABL. Los tumores de tipo fibrosarcoma, en particular el dermatofibrosarcoma protuberans (DFSP) con fusión COL1A1-PDGFB, dependen de la señalización PDGFB/PDGFR, lo que ofrece una justificación plausible a nivel de clase farmacológica. Actualmente no se dispone de datos detallados del mecanismo de acción en la información compilada, por lo que este razonamiento proviene de la literatura general sobre imatinib.

La relación con la indicación original es limitada: el registro colombiano solo menciona "IMATINIB" sin especificar enfermedades. No hay datos específicos de tumores cardíacos. El único documento citado es un comentario sobre la indicación aprobada de DFSP (un boletín farmacéutico que señala "evidencia no robusta"), no evidencia en tumores cardíacos.

Por lo tanto, la predicción es mecanísticamente plausible pero se apoya en una extrapolación indirecta. Se requiere evidencia específica antes de considerarla viable.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para fibrosarcoma cardíaco.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [18623899](https://pubmed.ncbi.nlm.nih.gov/18623899/) | 2008 | Revisión | Prescrire International | Comentario sobre nuevas indicaciones de imatinib; concluye que la evidencia de varias de ellas no es sólida. No aborda tumores cardíacos. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19939440 | GLIVEC® 100 MG COMPRIMIDOS CON CUBIERTA PELICULAR | Tableta cubierta con película | IMATINIB |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasas) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto. Las relaciones del grafo de conocimiento señalan neutropenia, trombocitopenia, agranulocitosis y anemia como condiciones de precaución |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma completo, función hepática y renal, balance de líquidos/peso y función cardíaca |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Condiciones de precaución según el grafo de conocimiento (no provienen del prospecto):** las relaciones fármaco-enfermedad del grafo TxGNN (PrimeKG) señalan, entre otras, insuficiencia hepática y enfermedad hepática, enfermedad renal, insuficiencia cardíaca congestiva y otras cardiopatías (enfermedad valvular, derrame pericárdico, enfermedad coronaria), edema pulmonar y cerebral, trombocitopenia, neutropenia, agranulocitosis, anemia, diabetes y cetoacidosis diabética, hipertensión, hiperbilirrubinemia (incluido el síndrome de Gilbert), úlcera péptica activa, hipofosfatemia y obesidad.
- **Interacciones farmacológicas:** se identificaron 675 interacciones en total. Entre las listadas, de gravedad **mayor**: eliglustat y naloxegol. De gravedad **moderada**: corticoides (hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida), pioglitazona, glimepirida, saxagliptina, aprepitant, morfina, cimetidina, claritromicina, lansoprazol, dexlansoprazol, naltrexona, naldemedina y metreleptina.
- **Reporte de caso relevante:** se describió una reacción de hipersensibilidad grave (DRESS) inducida por imatinib en un paciente con DFSP, que se manejó con desensibilización (señal de seguridad, no de eficacia).

Para advertencias y contraindicaciones formales, consultar el prospecto.

---

## Otras Predicciones Evaluadas

Además de la principal, el modelo propuso otras indicaciones. Ninguna alcanza una recomendación de avance inmediato:

| Indicación Predicha | Puntaje TxGNN | Nivel | Observación |
|------|------|------|------|
| Neoplasia fibroblástica | 0.9994 | L4 | La más prometedora: base mecanística sólida vía DFSP (COL1A1-PDGFB → PDGFR-β), con una guía europea 2025 ([39904126](https://pubmed.ncbi.nlm.nih.gov/39904126/)) que discute imatinib. Sin ensayos vinculados; la evidencia es mayormente de revisiones |
| Fibrosarcoma convencional | 0.9993 | L4 | Vínculo indirecto vía DFSP; un estudio preclínico de liposomas con imatinib |
| Fibrosarcoma renal | 0.9993 | L4 | Solo un ensayo Fase 2 de canasta ([NCT00154388](https://clinicaltrials.gov/study/NCT00154388), n=185, completado) sin datos específicos |
| Sarcoma fibromixoide de bajo grado | 0.9993 | L5 | Mecanismo débil (fusión FUS-CREB3L2/1); la literatura citada no es pertinente |
| Liposarcoma | 0.9988 | L2 | Tres ensayos Fase 1/2 y 2 completados en sarcomas mixtos ([NCT00031915](https://clinicaltrials.gov/study/NCT00031915), [NCT00154388](https://clinicaltrials.gov/study/NCT00154388), [NCT00006357](https://clinicaltrials.gov/study/NCT00006357)); no demuestran eficacia específica en liposarcoma, cuyo motor (MDM2/CDK4) no es PDGFR/KIT |
| Fibrosarcoma hepático | 0.9986 | L4 | Literatura sobre GIST y un reporte de DRESS; no respalda eficacia |
| Fiebre mediterránea familiar autosómica recesiva | 0.9986 | L5 | Solo predicción; sin base mecanística |
| Liposarcoma mixoide ovárico | 0.9985 | L5 | Solo predicción; mecanismo débil |
| Tumor rabdoide familiar | 0.9983 | L5 | Solo predicción; pérdida de SMARCB1 no es diana de imatinib |

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para fibrosarcoma cardíaco no hay ensayos clínicos y la única publicación citada es un comentario que no aborda tumores cardíacos, por lo que solo existe plausibilidad mecanística a nivel de clase. Entre las alternativas, "neoplasia fibroblástica" (DFSP) tiene la base más sólida y merece revisión prioritaria como pregunta de investigación.

<!-- review:begin co-lic-20261105-imatinib-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, en Colombia el único registro de Glivec está cancelado. Entre las alternativas, "neoplasia fibroblástica" (DFSP) tiene la base más sólida y merece revisión prioritaria como pregunta de investigación." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 9 registros sanitarios (vigentes: 7); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-imatinib-1 -->

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), actualmente pendiente y bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Buscar evidencia primaria (ensayos o series de casos) en tumores cardíacos o, de forma más realista, verificar el respaldo clínico en DFSP/neoplasia fibroblástica.
- Definir un plan de monitoreo de seguridad hematológica, hepática, renal y cardíaca, y revisar las interacciones de gravedad mayor.

<!-- review:begin co-lic-20261105-imatinib-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Aclarar el estado regulatorio en Colombia (registro cancelado; verificar si existen otras presentaciones o genéricos de imatinib vigentes). / Definir un plan de monitoreo de seguridad hematológica, hepática, renal y cardíaca, y revisar las interacciones de gravedad mayor." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 9 registros sanitarios (vigentes: 7); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-imatinib-2 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Además, en Colombia el único registro de Glivec está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Aclarar el estado regulatorio en Colombia (registro cancelado; verificar si existen otras presentaciones o genéricos de imatinib vigentes)" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

