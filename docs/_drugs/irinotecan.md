---
layout: default
title: Irinotecan
parent: Solo Predicción del Modelo (L5)
nav_order: 356
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Irinotecan: nueva indicación predicha, Carcinoma de mama femenino (nivel de evidencia L5). Indicación original: IRINOTECAN"
monitor_inn: "IRINOTECAN"
predicted_indications: ["female breast carcinoma"]
---

# Irinotecan
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

## Irinotecan: De Irinotecan (indicación no detallada en el registro) a Carcinoma de Mama Femenino
{: .text-alpha }

## Resumen en Una Frase

Irinotecan es un fármaco antineoplásico inhibidor de la topoisomerasa I; en Colombia sus registros sanitarios solo lo identifican como "irinotecan", sin detallar la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **carcinoma de mama femenino**, con **9 ensayos clínicos** (solo uno evalúa irinotecan directamente en cáncer de mama avanzado, en fase 1 con 12 pacientes) y **20 publicaciones**, la mayoría indirectas.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | IRINOTECAN (el registro no especifica la indicación) |
| Nueva Indicación Predicha | Carcinoma de mama femenino |
| Puntaje de Predicción TxGNN | 0.9908 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 6 de 6) |
| Número de Registros Sanitarios | 6 (vigentes: 6) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Irinotecan (traducción no oficial): «El irinotecán es un derivado de la camptotecina. Las camptotecinas interactúan específicamente con la enzima topoisomerasa I, que alivia la tensión torsional del ADN al inducir roturas monocatenarias reversibles. El irinotecán y su metabolito activo SN-38 se unen al complejo topoisomerasa I-ADN e impiden la religación de estas roturas monocatenarias.» Texto original en inglés: "Irinotecan is a derivative of camptothecin. Camptothecins interact specifically with the enzyme topoisomerase I, which relieves torsional strain in DNA by inducing reversible single-strand breaks. Irinotecan and its active metabolite SN-38 bind to the topoisomerase I-DNA complex and prevent religation of these single-strand breaks." ([DailyMed: Camptosar (irinotecan hydrochloride) prescribing information, Pharmacia & Upjohn Company LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e518dfc6-7e93-4fee-a66c-51e1ab71c056), versión del 2026-05-12; consultado el 2026-11-19). Según la información conocida, irinotecan es un profármaco de SN-38, un inhibidor de la topoisomerasa I que causa daño al ADN en células que se dividen rápidamente. Este mecanismo citotóxico es coherente con un puntaje alto del modelo (0.9908).

La relación con la nueva indicación se apoya sobre todo en un fármaco derivado: sacituzumab govitecan, un conjugado anticuerpo-fármaco dirigido a Trop-2 cuya carga útil es SN-38. Ha mostrado eficacia en cáncer de mama metastásico HR+/HER2- y triple negativo (diseño del estudio de fase III TROPiCS-02, PMID 32223649). Esto respalda la inhibición de la topoisomerasa I como mecanismo válido en cáncer de mama.

Sin embargo, esa evidencia proviene del conjugado y no del irinotecan libre. Los datos directos de irinotecan en cáncer de mama se limitan a ensayos tempranos y a una revisión de 1998 sobre su actividad en varios tipos de tumor. Una revisión de 2003 describe actividad "marginal" de irinotecan y mitomicina en cáncer de mama, con sinergismo preclínico entre ambos.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00083148](https://clinicaltrials.gov/study/NCT00083148) | Fase 1 | Completado | 12 | Irinotecan seguido de capecitabina en carcinoma de mama avanzado; evalúa seguridad y dosis; estudio pequeño (relevancia directa) |
| [NCT00031681](https://clinicaltrials.gov/study/NCT00031681) | Fase 1 | Completado | 41 | UCN-01 más irinotecan en tumores sólidos resistentes y cáncer de mama triple negativo recurrente |
| [NCT00004095](https://clinicaltrials.gov/study/NCT00004095) | Fase 1 | Completado | 38 | Irinotecan más gemcitabina en tumores sólidos irresecables o metastásicos (mama es uno de varios tipos) |
| [NCT03678883](https://clinicaltrials.gov/study/NCT03678883) | Fase 2 | Activo, no recluta | 350 | 9-ING-41 (inhibidor de GSK-3β) solo o con quimioterapia, incluido irinotecan, en cánceres refractarios; relevancia indirecta |
| [NCT05453825](https://clinicaltrials.gov/study/NCT05453825) | Fase 2 | Desconocido | 180 | Navicixizumab solo o con paclitaxel o irinotecan en tumores sólidos avanzados, con una cohorte de cáncer de mama triple negativo |
| [NCT02419495](https://clinicaltrials.gov/study/NCT02419495) | Fase 1 | Terminado | 221 | Selinexor con varios esquemas de quimioterapia o inmunoterapia en neoplasias avanzadas; datos específicos de irinotecan poco claros |
| [NCT06840886](https://clinicaltrials.gov/study/NCT06840886) | Fase 1 | Reclutando | 426 | PHST001 solo o combinado en tumores sólidos avanzados; papel de irinotecan poco claro |
| [NCT06769425](https://clinicaltrials.gov/study/NCT06769425) | Fase 1 | Reclutando | 157 | HS-10502 (inhibidor de PARP1) en combinación en tumores sólidos avanzados; evidencia indirecta |
| [NCT05238831](https://clinicaltrials.gov/study/NCT05238831) | Fase 1 temprana | Retirado | 0 | Estudio piloto de medicina de precisión SMMART-ACT; sin pacientes inscritos, no aporta evidencia |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [32223649](https://pubmed.ncbi.nlm.nih.gov/32223649/) | 2020 | ECA (diseño fase III) | Future Oncology | TROPiCS-02: sacituzumab govitecan (SN-38, metabolito activo de irinotecan) en cáncer de mama metastásico HR+/HER2- |
| [41371050](https://pubmed.ncbi.nlm.nih.gov/41371050/) | 2026 | Fase 2 | Eur J Cancer | PHENOMENAL: irinotecan liposomal en cáncer de mama HER2-negativo con metástasis cerebrales |
| [40877204](https://pubmed.ncbi.nlm.nih.gov/40877204/) | 2025 | Estudio clínico | Cancer Reports | Etirinotecan pegol (formulación pegilada) en metástasis cerebrales de pulmón o mama |
| [25944802](https://pubmed.ncbi.nlm.nih.gov/25944802/) | 2015 | Fase 1/2 | Clin Cancer Res | Primer estudio en humanos de sacituzumab govitecan en tumores sólidos metastásicos diversos |
| [28558150](https://pubmed.ncbi.nlm.nih.gov/28558150/) | 2017 | Revisión clínica | Cancer | Seguridad y farmacocinética de sacituzumab govitecan en cánceres epiteliales avanzados |
| [9726101](https://pubmed.ncbi.nlm.nih.gov/9726101/) | 1998 | Revisión | Oncology (Williston Park) | Actividad de irinotecan en linfoma, leucemia y cánceres de mama, páncreas, ovario y pulmón de células pequeñas |
| [12800602](https://pubmed.ncbi.nlm.nih.gov/12800602/) | 2003 | Revisión | Oncology (Williston Park) | Fundamento del uso de mitomicina e irinotecan en cáncer de mama avanzado; actividad marginal con sinergismo preclínico |
| [26101915](https://pubmed.ncbi.nlm.nih.gov/26101915/) | 2015 | Preclínico | Oncotarget | Trop-2 como blanco de sacituzumab govitecan; mayor eficacia con alta relación fármaco:anticuerpo |
| [40749148](https://pubmed.ncbi.nlm.nih.gov/40749148/) | 2025 | Fase temprana | J Clin Oncol | DEP-SN38, nanopartícula con SN-38: seguridad y eficacia preliminar en tumores sólidos avanzados |
| [19059062](https://pubmed.ncbi.nlm.nih.gov/19059062/) | 2008 | Revisión | Clin Lab Med | Farmacogenómica de tamoxifeno e irinotecan; toxicidad ligada a la actividad reducida de UGT1A1 |

---

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 19952096 | CLORHIDRATO DE IRINOTECAN TRIHIDRATO 20 MG/ML | SOLUCION INYECTABLE | IRINOTECAN | Vigente |
| 20010926 | IRINOTECAN SOLUCIÓN PARA INYECCION VIAL POR 100 MG/5 ML | SOLUCION INYECTABLE | IRINOTECÁN | Vigente |
| 20012770 | IRINOTECANSOLUCION INYECTABLE100 MG/ 5 ML | SOLUCION INYECTABLE | IRINOTECAN | Vigente |
| 20053624 | IRINOTECAN CLORHIDRATO INYECTABLE 100 MG / 5 ML | SOLUCION INYECTABLE | IRINOTECAN | Vigente |
| 20141121 | ROTECAN100 MG/5 ML SOLUCIÓN INYECTABLE | SOLUCION INYECTABLE | IRINOTECAN | Vigente |

Se muestran 5 de 6 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (inhibidor de la topoisomerasa I) |
| Riesgo de Mielosupresión | Alto (las asociaciones del grafo de conocimiento señalan neutropenia, trombocitopenia, anemia y agranulocitosis como condiciones de precaución) |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal, bilirrubina, electrolitos y vigilancia de diarrea |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

- **Condiciones de precaución según el grafo de conocimiento (no provienen del prospecto):** enfermedad renal, pioureter, pancreatitis, enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia, neutropenia, agranulocitosis, anemia (incluida la macrocítica), íleo, obstrucción intestinal, hiperbilirrubinemia (incluida la hereditaria y el síndrome de Gilbert), enfermedad pulmonar intersticial y enfermedad diarreica.
- **Interacciones farmacológicas:** se identificaron 100 interacciones; entre las principales:
  - **Mayor:** claritromicina.
  - **Moderadas:** aprepitant, dexametasona, cimetidina, miconazol, metreleptina, eluxadolina y múltiples laxantes/osmóticos (bisacodilo, ácido picosulfúrico, sulfato, citrato e hidróxido de magnesio, aceite de ricino, glicerina, lactitol, lactulosa, manitol, aceite mineral, fenolftaleína).
  - **Menor:** levofloxacino.

No se dispone de advertencias ni contraindicaciones del prospecto; consultar el prospecto para esa información.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia directa de irinotecan en cáncer de mama es escasa (un ensayo de fase 1 con 12 pacientes y revisiones antiguas que describen actividad marginal). El respaldo más sólido proviene de sacituzumab govitecan, un conjugado distinto. Además, los 6 registros sanitarios colombianos están vigentes y el fármaco se comercializa, pero falta la información del prospecto, lo que impide completar el tamizaje de seguridad.

<!-- review:begin co-lic-20261112-irinotecan-1 -->

> **Corrección de revisión (2026-11-12)**: Texto original: "los 2 registros sanitarios colombianos están vigentes" Corregido según los datos del INVIMA (Código Único de Medicamentos, datos al 2026-11-05): 6 registros sanitarios, de los cuales 6 vigentes. Las cifras actuales están en el Resumen rápido. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261112-irinotecan-1 -->

**Para avanzar se necesita:**
- Obtener y analizar el prospecto del INVIMA (advertencias y contraindicaciones), que es un vacío bloqueante.
- Completar los datos del mecanismo de acción desde DrugBank.
- Revisar resultados del estudio PHENOMENAL (irinotecan liposomal) y otros datos de irinotecan en cáncer de mama.
- Definir la población objetivo y un plan de monitoreo de seguridad (mielosupresión, diarrea, genotipo UGT1A1) antes de cualquier estudio.

<!-- review:begin co-lic-20261105-irinotecan-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Aclarar la situación regulatoria y la disponibilidad de producto en Colombia (registros cancelados, nueva solicitud o formulaciones alternativas). / Definir la población objetivo y un plan de monitoreo de seguridad (mielosupresión, diarrea, genotipo UGT1A1) antes de cualquier estudio." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 6 registros sanitarios (vigentes: 6); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-irinotecan-1 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Aclarar la situación regulatoria y la disponibilidad de producto en Colombia (registros cancelados, nueva solicitud o formulaciones alternat" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-12 | Número de registros vigentes: 2 → 6 | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Camptosar (irinotecan hydrochloride) prescribing information, Pharmacia & Upjohn Company LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e518dfc6-7e93-4fee-a66c-51e1ab71c056) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

