---
layout: default
title: Ponatinib
parent: Solo Predicción del Modelo (L5)
nav_order: 523
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-20
description: "Ponatinib: nueva indicación predicha, Fibromatosis gingival (nivel de evidencia L5). Indicación original: No especificada en el registro (el texto aprobado solo indica \"PONATI…"
monitor_inn: "ponatinib"
predicted_indications: ["fibromatosis, gingival", "liposarcoma"]
---

# Ponatinib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Ponatinib: De Indicación No Especificada a Fibromatosis Gingival
{: .text-alpha }

## Resumen en Una Frase

Ponatinib es un inhibidor de tirosina quinasas de acción múltiple que cuenta con un registro sanitario en Colombia (ICLUSIG® 15 mg tabletas recubiertas), cuyo texto de indicación solo consigna el nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para **fibromatosis gingival**, con **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; es una predicción puramente computacional.
Como alternativa, la segunda predicción (liposarcoma) cuenta con **1 publicación preclínica**, pero sin ensayos clínicos.

<!-- review:begin co-lic-20261105-ponatinib-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Ponatinib es un inhibidor de tirosina quinasas de acción múltiple que cuenta con un registro sanitario en Colombia (ICLUSIG® 15 mg tabletas recubiertas), actualmente cancelado, cuyo texto de indicación solo consigna el nombre del principio activo." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-ponatinib-2 -->

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto aprobado solo indica "PONATINIB") |
| Nueva Indicación Predicha | Fibromatosis gingival |
| Puntaje de Predicción TxGNN | 0.9904 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Ponatinib (traducción no oficial): «El ponatinib es un inhibidor de cinasas. El ponatinib inhibió in vitro la actividad tirosina cinasa de ABL y de ABL con la mutación T315I con concentraciones de IC 50 de 0,4 nM y 2,0 nM, respectivamente. El ponatinib inhibió in vitro la actividad de otras cinasas con concentraciones de IC 50 de entre 0,1 nM y 20 nM, incluidos miembros de las familias de cinasas VEGFR, PDGFR, FGFR, receptores EPH y SRC, así como KIT, RET, TIE2 y FLT3.» Texto original en inglés: "Ponatinib is a kinase inhibitor. Ponatinib inhibited the in vitro tyrosine kinase activity of ABL and T315I mutant ABL with IC 50 concentrations of 0.4 nM and 2.0 nM, respectively. Ponatinib inhibited the in vitro activity of additional kinases with IC 50 concentrations between 0.1 nM and 20 nM, including members of the VEGFR, PDGFR, FGFR, EPH receptors and SRC families of kinases, and KIT, RET, TIE2, and FLT3." ([DailyMed: Iclusig (ponatinib hydrochloride) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=16d804b6-4957-43ee-b18c-3b36ec37c5ac), versión del 2026-08-14; consultado el 2026-11-19). Según la información conocida, ponatinib es un inhibidor de tirosina quinasas de acción múltiple (BCR-ABL, FGFR, PDGFR, VEGFR, SRC), y mecanísticamente podría ser aplicable a procesos de proliferación de fibroblastos, aunque esto no está confirmado por los datos disponibles.

La relación con la indicación original no puede evaluarse con precisión, porque el registro sanitario no detalla las indicaciones aprobadas. La vía de proliferación fibroblástica y depósito de matriz extracelular es una hipótesis especulativa que **no está respaldada por ninguna evidencia** en los datos compilados.

Además, la toxicidad vascular conocida de ponatinib (eventos oclusivos arteriales) y el carácter benigno de la fibromatosis gingival hacen que el balance riesgo-beneficio sea desfavorable sin datos de respaldo.

**Predicción secundaria (liposarcoma, puntaje 0.9900, nivel L4):** una publicación preclínica de 2017 (PMID 29132397) realizó perfiles de quinasas con ARNi y cribado de fármacos en liposarcoma e identificó dianas farmacológicas. Con la información disponible no se confirma que ponatinib estuviera entre los agentes eficaces; esto requiere verificación con el texto completo. Ponatinib inhibe FGFR, PDGFR, KIT, SRC y RET, que son dependencias plausibles en sarcomas.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Para fibromatosis gingival, actualmente no hay literatura relacionada disponible.

Para la predicción secundaria (liposarcoma):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [29132397](https://pubmed.ncbi.nlm.nih.gov/29132397/) | 2017 | Preclínico | Journal of Hematology & Oncology | Perfilado de quinasas en liposarcoma mediante ARNi y cribado de fármacos para identificar dianas terapéuticas; el liposarcoma es el tumor de tejidos blandos más común y su enfermedad metastásica tiene opciones limitadas |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20129443 | ICLUSIG® 15 MG TABLETAS RECUBIERTAS | Tableta recubierta | PONATINIB | Vigente |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasas) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma, función hepática y renal; vigilancia de eventos vasculares |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas:** se identificaron 455 interacciones en total. Entre las principales de la muestra disponible:
  - **Mayores:** ácido acetilsalicílico, claritromicina.
  - **Moderadas:** loperamida, aprepitant, dexametasona, naldemedina, naltrexona, metronidazol, miconazol.
  - **Menores:** famotidina, ranitidina, cimetidina, nizatidina, omeprazol, lansoprazol, dexlansoprazol, rabeprazol, pantoprazol, óxido de magnesio, naloxegol.
- **Riesgo conocido:** eventos oclusivos arteriales (toxicidad vascular), según el análisis de riesgo-beneficio de los datos compilados.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para fibromatosis gingival se basa únicamente en el modelo (L5), sin ensayos ni literatura, y la toxicidad vascular de ponatinib no se justifica para una condición benigna.

<!-- review:begin co-lic-20261105-ponatinib-3 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción para fibromatosis gingival se basa únicamente en el modelo (L5), sin ensayos ni literatura, y la toxicidad vascular de ponatinib no se justifica para una condición benigna. Además, el único registro sanitario en Colombia está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-ponatinib-3 -->

**Para avanzar se necesita:**
- Datos del mecanismo de acción (por ejemplo, consulta a DrugBank).
- Obtener y analizar el prospecto aprobado (advertencias y contraindicaciones).
- Verificar con el texto completo del PMID 29132397 si ponatinib mostró actividad en liposarcoma, como posible línea de investigación más sólida (L4).
- Evidencia que vincule ponatinib con fibromatosis gingival, o descartar esta indicación.

<!-- review:begin co-lic-20261031-ponatinib-1 -->

> **Corrección de revisión (2026-10-31)**: Texto original: "Evidencia que vincule ponatinib con fibromatosis gingival, o descartar esta indicación. / Aclarar la situación regulatoria en Colombia (registro cancelado)." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-10-31. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261031-ponatinib-1 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-10-31 | Eliminado: "Aclarar la situación regulatoria en Colombia (registro cancelado)" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "actualmente cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Además, el único registro sanitario en Colombia está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Iclusig (ponatinib hydrochloride) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=16d804b6-4957-43ee-b18c-3b36ec37c5ac) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

