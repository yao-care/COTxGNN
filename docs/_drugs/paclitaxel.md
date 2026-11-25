---
layout: default
title: Paclitaxel
parent: Solo Predicción del Modelo (L5)
nav_order: 492
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-25
monitor_inn: "PACLITAXEL"
predicted_indications: ["parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina"]
description: "Paclitaxel: nueva indicación predicha, Parameningeal embryonal rhabdomyosarcoma (nivel de evidencia L5). Indicación original: PACLITAXEL"
---

# Paclitaxel
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

## Paclitaxel: Parameningeal embryonal rhabdomyosarcoma
{: .text-alpha }

## Resumen en Una Frase

Paclitaxel es un citotóxico de la familia de los taxanos, registrado en Colombia como solución inyectable. Los registros sanitarios disponibles no detallan el texto de la indicación original.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | PACLITAXEL |
| Nueva Indicación Predicha | Parameningeal embryonal rhabdomyosarcoma |
| Puntaje de Predicción TxGNN | 0.9973 |
| Nivel de Evidencia | L5 (≥2 ECA de Fase 3 completados, p. ej. NCT00667251, NCT01822314, NCT00006459, NCT00553358, NCT00513292, NCT00431080, NCT00075270; ver nota en la sección de ensayos) |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 16) |
| Número de Registros Sanitarios | al menos 20 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Paclitaxel (traducción no oficial): «Las partículas de paclitaxel unido a proteínas para suspensión inyectable (unido a albúmina) son un inhibidor de los microtúbulos que promueve el ensamblaje de los microtúbulos a partir de dímeros de tubulina y estabiliza los microtúbulos al impedir su despolimerización. Esta estabilidad produce la inhibición de la reorganización dinámica normal de la red de microtúbulos, que es esencial para las funciones celulares vitales de la interfase y de la mitosis.» Texto original en inglés: "Paclitaxel protein-bound particles for injectable suspension (albumin-bound) is a microtubule inhibitor that promotes the assembly of microtubules from tubulin dimers and stabilizes microtubules by preventing depolymerization. This stability results in the inhibition of the normal dynamic reorganization of the microtubule network that is essential for vital interphase and mitotic cellular functions." ([DailyMed: Paclitaxel Protein-Bound Particles For Injectable Suspension (Albumin-Bound) (paclitaxel) prescribing information, NorthStar Rx LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1e9d5093-fbfc-470a-8520-811c46a8870c), versión del 2025-09-17; consultado el 2026-11-19). Según la información conocida, paclitaxel es un taxano que estabiliza los microtúbulos, bloqueando la división celular (arresto mitótico) e induciendo apoptosis en células que se dividen rápidamente.

El cáncer de mama es una de las indicaciones clásicas de los taxanos: la literatura recuperada describe a paclitaxel y docetaxel como componentes basados en evidencia del tratamiento de carcinomas de mama, pulmón y ovario avanzados, y paclitaxel fue aprobado en EE. UU. para el tratamiento adyuvante del cáncer de mama temprano con ganglios positivos. Por ello, la predicción del modelo coincide con la práctica clínica vigente.

Dado que su acción citotóxica no depende del estado del receptor de estrógeno ni de otros marcadores hormonales, el mecanismo es aplicable a distintos subtipos de cáncer de mama. Esto explica también las demás predicciones del modelo (cáncer de mama ER negativo, ER positivo, resistente a hormonas), que son subtipos de la misma enfermedad.

---

## Evidencia de Ensayos Clínicos

Se listan los ensayos más relevantes (priorizando Fase 3 y Fase 2 con paclitaxel como componente central):

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00006459](https://clinicaltrials.gov/study/NCT00006459) | Fase 3 | Completado | No reportada | Paclitaxel con o sin gemcitabina en cáncer de mama avanzado o metastásico |
| [NCT00667251](https://clinicaltrials.gov/study/NCT00667251) | Fase 3 | Completado | 652 | Quimioterapia con taxano más lapatinib vs. trastuzumab en cáncer de mama metastásico HER2 positivo |
| [NCT01822314](https://clinicaltrials.gov/study/NCT01822314) | Fase 3 | Completado | 632 | Nab-paclitaxel neoadyuvante vs. paclitaxel con solvente en cáncer de mama HER2 negativo de alto riesgo |
| [NCT00553358](https://clinicaltrials.gov/study/NCT00553358) | Fase 3 | Completado | 455 | Neo-ALTTO: lapatinib, trastuzumab o ambos con paclitaxel neoadyuvante en HER2 positivo |
| [NCT00513292](https://clinicaltrials.gov/study/NCT00513292) | Fase 3 | Completado | 280 | Secuencias de FEC y paclitaxel más trastuzumab neoadyuvante en HER2 positivo operable |
| [NCT00431080](https://clinicaltrials.gov/study/NCT00431080) | Fase 3 | Completado | 478 | FE75C seguido de docetaxel vs. paclitaxel adyuvante en cáncer de mama con ganglios positivos |
| [NCT00075270](https://clinicaltrials.gov/study/NCT00075270) | Fase 3 | Completado | 580 | Lapatinib más paclitaxel vs. paclitaxel solo en cáncer de mama avanzado de primera línea |
| [NCT00003539](https://clinicaltrials.gov/study/NCT00003539) | Fase 2 | Completado | 50 | Paclitaxel semanal más trastuzumab en cáncer de mama metastásico (evidencia directa) |
| [NCT00006120](https://clinicaltrials.gov/study/NCT00006120) | Fase 2 | Desconocido | No reportada | Comparación aleatorizada de dos esquemas de docetaxel o paclitaxel en cáncer de mama metastásico |
| [NCT05020860](https://clinicaltrials.gov/study/NCT05020860) | Fase 2 | Reclutando | 185 | Relación entre respuesta clínica y patológica con terapia neoadyuvante que incluye paclitaxel; aún sin resultados |

**Nota:** el nivel L1 se basa en la cantidad de ensayos de Fase 3 completados, pero en la mayoría paclitaxel es el esqueleto de quimioterapia y no el fármaco experimental. La contribución específica de paclitaxel debe confirmarse en los registros de cada ensayo.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [11147586](https://pubmed.ncbi.nlm.nih.gov/11147586/) | 2000 | Ensayo clínico (Fase II) | Cancer | Eficacia y toxicidad de doxorrubicina más paclitaxel en cáncer de mama metastásico; importancia del tratamiento previo con antraciclinas |
| [10791395](https://pubmed.ncbi.nlm.nih.gov/10791395/) | 2000 | Revisión | Lancet | Actualización sobre taxanos: actividad sustancial de paclitaxel y docetaxel en mama, pulmón y ovario |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Revisión | Drug and Therapeutics Bulletin | Paclitaxel y docetaxel en cáncer de mama y ovario |
| [11745249](https://pubmed.ncbi.nlm.nih.gov/11745249/) | 2001 | Revisión | Cancer | Papel de paclitaxel en el tratamiento multimodal del carcinoma mamario inflamatorio |
| [9296218](https://pubmed.ncbi.nlm.nih.gov/9296218/) | 1997 | Estudio de búsqueda de dosis | Annals of Oncology | Dosis máximas tolerables de paclitaxel en infusión corta con ciclofosfamida en cáncer de mama avanzado |
| [10898354](https://pubmed.ncbi.nlm.nih.gov/10898354/) | 2000 | Revisión | Cancer | Avances en la quimioterapia del cáncer de mama |
| [24823476](https://pubmed.ncbi.nlm.nih.gov/24823476/) | 2014 | Estudio genómico | Nature Communications | Variantes de TEKT4 asociadas con resistencia a paclitaxel en cáncer de mama |
| [20665703](https://pubmed.ncbi.nlm.nih.gov/20665703/) | 2011 | Preclínico | Journal of Cellular Physiology | ZD6474 potencia los efectos antiproliferativos y apoptóticos de paclitaxel en células de carcinoma de mama |
| [39317691](https://pubmed.ncbi.nlm.nih.gov/39317691/) | 2024 | Análisis computacional | Chemical Biology & Drug Design | Combinaciones de paclitaxel contra carcinoma de mama e identificación de biomarcadores in vivo |
| [31515668](https://pubmed.ncbi.nlm.nih.gov/31515668/) | 2019 | Preclínico | Cancer Chemotherapy and Pharmacology | La reducción de SRSF3 con oligonucleótidos antisentido sensibiliza células de mama al paclitaxel |

---

## Información de Mercado en Colombia

Existen registros sanitarios vigentes; el medicamento se encuentra comercializado.

<!-- review:begin co-lic-20261125-paclitaxel-1 -->

> **Corrección de revisión (2026-11-25)**: Texto original: "Existen 15 registros sanitarios vigentes; el medicamento se encuentra comercializado." Corregido según los datos del INVIMA: con los registros agregados la cifra fija ya no coincide (los datos solo incluyen parte de los registros); se eliminó la cifra. Las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261125-paclitaxel-1 -->

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 19952097 | PACLITAXEL 100 MG/ 16.7 ML VIAL | SOLUCION INYECTABLE | PACLITAXEL | Vigente |
| 19976518 | PACLITAXEL 30 MG SOLUCION INYECTABLE | SOLUCION INYECTABLE | PACLITAXEL | Vigente |
| 19976519 | PACLITAXEL 100 MG SOLUCIONINYECTABLE | SOLUCION INYECTABLE | PACLITAXEL | Vigente |
| 19991105 | PACLITAXEL 300MG | SOLUCION INYECTABLE | PACLITAXEL | Vigente |
| 20007285 | PACLITAXEL 30 MG/ 5 ML SOLUCION INYECTABLE | SOLUCION INYECTABLE | PACLITAXEL | Vigente |

Se muestran 5 de al menos 20 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes. Los datos de este informe solo incluyen parte de los registros.

<!-- licenses:end -->

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (taxano, estabilizador de microtúbulos) |
| Riesgo de Mielosupresión | Alto; los datos de seguridad asocian el fármaco con neutropenia, trombocitopenia y anemia |
| Clasificación de Emetogenicidad | Baja a moderada (según la categoría del fármaco; consultar el prospecto) |
| Ítems de Monitoreo | Hemograma con diferencial, función hepática y renal, vigilancia de neuropatía periférica y de reacciones de hipersensibilidad |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento del modelo** (relaciones fármaco-enfermedad, no texto de prospecto): neutropenia y agranulocitosis, trombocitopenia, anemia, enfermedad hepática y de vesícula biliar, hiperbilirrubinemia (incluido síndrome de Gilbert), enfermedad renal, neuropatía periférica, infarto de miocardio y paro cardíaco súbito, trastornos hipotensivos, asma, diabetes y cetoacidosis diabética, psoriasis, y trastornos de ansiedad y distimia.
- **Interacciones farmacológicas** (se detectaron 100; principales): interacciones de nivel moderado con aprepitant, rolapitant, cimetidina, claritromicina, dexametasona, clotrimazol, miconazol, metronidazol, tinidazol, eliglustat, rosuvastatina, simvastatina y troglitazona. Nivel menor con ácido ascórbico y levofloxacino.
- Las advertencias y contraindicaciones del prospecto no están disponibles. Consultar el prospecto para información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Paclitaxel tiene evidencia clínica amplia en cáncer de mama, incluidos múltiples ensayos de Fase 3 completados, y es un tratamiento estándar. Sin embargo, faltan los datos de seguridad del prospecto, por lo que se requieren salvaguardas.

<!-- review:begin co-lic-20261105-paclitaxel-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Sin embargo, no hay registros sanitarios vigentes en Colombia y faltan los datos de seguridad del prospecto, por lo que se requieren salvaguardas." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-paclitaxel-1 -->

**Para avanzar se necesita:**
- Verificar si existen registros vigentes o reactivar/renovar un registro sanitario ante INVIMA
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones)
- Confirmar el papel específico de paclitaxel en los ensayos de Fase 3 para validar el nivel L1
- Completar los datos del mecanismo de acción desde DrugBank
- Plan de monitoreo de seguridad hematológica, neurológica y de hipersensibilidad
- Tener presente que otras predicciones del modelo tienen respaldo mucho menor: cáncer de mama ER negativo, ER positivo y resistente a hormonas son subtipos con evidencia de Fase 2-3 (Proceed with Guardrails); mientras que el tumor de Ehrlich (modelo murino), carcinoma de mama bilateral, carcinoma de pezón y los rabdomiosarcomas embrionarios tienen evidencia preclínica, de reportes de caso o solo predicción del modelo (Hold)

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "no hay registros sanitarios vigentes en Colombia y" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-12 | Número de registros vigentes: 4 → 15 | Ya no aparece tras una corrección del programa (2026-11-24: el número de registros sanitarios de esta frase lo actualiza ahora un programa según los datos del INVIMA (scripts/rewrite_license_counts.py), por lo que esta corrección puntual ya no se muestra; antes: Corregido) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Paclitaxel Protein-Bound Particles For Injectable Suspension (Albumin-Bound) (paclitaxel) prescribing information, NorthStar Rx LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1e9d5093-fbfc-470a-8520-811c46a8870c) |
| 2026-11-25 | Eliminado: «15» | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

