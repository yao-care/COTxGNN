---
layout: default
title: Epirubicin
parent: Evidencia Moderada (L3-L4)
nav_order: 258
evidence_level: L4
indication_count: 7
last_modified_at: 2026-10-14
description: "Epirubicin: nueva indicación predicha, Linfoma pulmonar primario (nivel de evidencia L4). Indicación original: Epirrubicina"
monitor_inn: "epirubicin"
predicted_indications: ["primary pulmonary lymphoma", "well-differentiated fetal adenocarcinoma of the lung", "small cell lung carcinoma", "pulmonary blastoma", "lung mixed small cell and squamous cell carcinoma", "myeloid leukemia", "upper aerodigestive tract neoplasm"]
---

# Epirubicin
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **7** 
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

## Epirubicina: De Epirrubicina (indicación sin detallar) a Linfoma Pulmonar Primario
{: .text-alpha }

## Resumen en Una Frase

Epirubicina es una antraciclina citotóxica, con un registro sanitario en Colombia cuyo texto de indicación aprobada solo dice "EPIRRUBICINA", sin detallar la enfermedad.
El modelo TxGNN predice que podría ser efectiva para **linfoma pulmonar primario**, pero no hay ensayos clínicos registrados para esta indicación y solo **6 publicaciones**, en su mayoría reportes de caso, series pequeñas y revisiones.
Entre las otras indicaciones predichas, el **carcinoma pulmonar de células pequeñas** cuenta con respaldo más sólido (5 ensayos clínicos, incluidos 3 de Fase 3).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Epirrubicina (el registro no detalla la enfermedad; se trata de un antineoplásico) |
| Nueva Indicación Predicha | Linfoma pulmonar primario |
| Puntaje de Predicción TxGNN | 99.71% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo cancelado (sin registros vigentes) |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según el conocimiento general de la clase, epirubicina es una antraciclina, epímero de la doxorubicina, que actúa como intercalante del ADN e inhibidor de la topoisomerasa II. Su eficacia en tumores sólidos como el cáncer de mama y el gástrico está bien documentada.

La relación con el linfoma pulmonar primario es de clase: las antraciclinas forman parte de esquemas de linfoma como CHOP y, en la literatura recuperada, un esquema con epirubicina (VEBEP) se estudió en enfermedad de Hodgkin avanzada. Sin embargo, el tratamiento estándar actual en linfomas B (R-CHOP, Pola-R-CHP) utiliza doxorubicina, no epirubicina. La literatura sobre linfoma pulmonar primario consiste sobre todo en reportes de caso, series retrospectivas pequeñas y revisiones. El puntaje alto del modelo (99.71%) es solo una predicción y no sustituye evidencia clínica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para linfoma pulmonar primario.

Como referencia, para otras indicaciones predichas sí existen ensayos. El carcinoma pulmonar de células pequeñas (puesto 3 de la lista) tiene, entre otros:

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00003606](https://clinicaltrials.gov/study/NCT00003606) | Fase 3 | Completado | 216 | Cisplatino-etopósido con o sin epirubicina y ciclofosfamida en enfermedad extensa; evalúa directamente el aporte de epirubicina |
| [NCT00011921](https://clinicaltrials.gov/study/NCT00011921) | Fase 3 | Desconocido | 430 | Quimioterapia secuencial de dosis altas frente a estándar; falta confirmar si incluye epirubicina |
| [NCT00658580](https://clinicaltrials.gov/study/NCT00658580) | Fase 3 | Completado | 361 | Cisplatino-etopósido frente a régimen con etopósido sin platino; relación indirecta con epirubicina |
| [NCT03755115](https://clinicaltrials.gov/study/NCT03755115) | Fase 2 | Desconocido | 40 | SHR-1210 (camrelizumab) más epirubicina tras fallo de primera línea |
| [NCT00154739](https://clinicaltrials.gov/study/NCT00154739) | Fase 2 | Completado | 86 | Gemcitabina/cisplatino frente a gemcitabina/epirubicina; el título sugiere cáncer de pulmón de células no pequeñas, relevancia incierta |

---

## Evidencia de Literatura

Literatura recuperada para linfoma pulmonar primario:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [7686469](https://pubmed.ncbi.nlm.nih.gov/7686469/) | 1993 | Revisión | Drugs | Farmacología y uso terapéutico de epirubicina; eficacia equivalente a doxorubicina en varios tumores |
| [10526668](https://pubmed.ncbi.nlm.nih.gov/10526668/) | 1999 | Cohorte | Cancer Journal | Régimen intensivo VEBEP más radioterapia en enfermedad de Hodgkin avanzada |
| [39192408](https://pubmed.ncbi.nlm.nih.gov/39192408/) | 2024 | Cohorte retrospectiva | Zhongguo Shi Yan Xue Ye Xue Za Zhi | Características clínicas y pronóstico de linfoma B difuso de células grandes extranodal primario en la era del rituximab |
| [40728626](https://pubmed.ncbi.nlm.nih.gov/40728626/) | 2025 | Subanálisis de ensayo | Annals of Hematology | Pola-R-CHP en LDCBG de primera línea; usa doxorubicina, no epirubicina |
| [36237246](https://pubmed.ncbi.nlm.nih.gov/36237246/) | 2022 | Reporte de caso | Translational Cancer Research | Linfoma MALT primario de pleura mal diagnosticado |
| [1866500](https://pubmed.ncbi.nlm.nih.gov/1866500/) | 1991 | Reporte de caso | Rev Invest Clin | Linfoma no Hodgkin primario de pulmón |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20063700 (cancelado) | EPIRUBICINA 50 MG (Blau Farmacéutica Colombia S.A.S.) | Polvo liofilizado para reconstituir a solución inyectable | EPIRRUBICINA |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (antraciclina; inhibidor de topoisomerasa II) |
| Riesgo de Mielosupresión | Alto (las contraindicaciones del grafo de conocimiento incluyen neutropenia, trombocitopenia y agranulocitosis) |
| Clasificación de Emetogenicidad | Moderada (según la categoría del fármaco) |
| Items de Monitoreo | Hemograma con diferencial, funciones hepática y renal, función cardíaca (p. ej., fracción de eyección) |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas por el grafo de conocimiento de TxGNN (no provienen del prospecto):** insuficiencia y enfermedad hepática, enfermedad renal, enfermedad de la vesícula biliar, trombocitopenia, neutropenia, agranulocitosis, infarto de miocardio y trombosis coronaria, miocardiopatías (incluida la hipertrófica), fibrosis endomiocárdica, trastornos de conducción cardíaca, paro cardíaco súbito, hemoglobinopatía, piouréter y estomatitis.
- **Interacciones farmacológicas:** se identificaron 487 interacciones. Entre las de nivel mayor figuran cimetidina y dolasetrón. Hay muchas de nivel moderado, por ejemplo acarbosa, famotidina, pioglitazona, loperamida, bupropión, claritromicina, levofloxacino, minociclina, naltrexona y palonosetrón.
- **Señal de seguridad adicional:** la literatura asocia epirubicina con leucemia mieloide aguda y síndrome mielodisplásico secundarios en ensayos adyuvantes de cáncer de mama, además de la cardiotoxicidad propia de las antraciclinas.

Consultar el prospecto para las advertencias y contraindicaciones oficiales.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para linfoma pulmonar primario no hay ensayos clínicos, la literatura se limita a reportes de caso, series pequeñas y revisiones, y el estándar actual emplea doxorubicina. Además, el único registro sanitario está cancelado y el perfil de seguridad (cardiotoxicidad, mielosupresión, leucemia secundaria) exige cautela.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y del prospecto oficial (advertencias y contraindicaciones), cuya ausencia bloquea el cribado de seguridad.
- Estudios clínicos o series que comparen epirubicina con doxorubicina en linfoma pulmonar primario.
- Evaluar prioritariamente la indicación mejor respaldada, el carcinoma pulmonar de células pequeñas (L1): confirmar los brazos y resultados de NCT00003606 y NCT00011921 y definir si epirubicina tiene un papel en enfermedad recidivante o refractaria frente al estándar actual de platino-etopósido con inmunoterapia.
- Aclarar la situación regulatoria: no hay registro vigente en Colombia, por lo que cualquier uso requeriría un nuevo registro o la importación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

