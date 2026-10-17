---
layout: default
title: Docetaxel
parent: Solo Predicción del Modelo (L5)
nav_order: 228
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Docetaxel: nueva indicación predicha, Carcinoma de mama femenino (nivel de evidencia L5). Indicación original: No especificada"
monitor_inn: "DOCETAXEL"
predicted_indications: ["Ewing sarcoma", "primary pulmonary lymphoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "pulmonary blastoma", "rhabdomyosarcoma (disease)", "embryonal extrahepatic bile duct rhabdomyosarcoma", "parameningeal embryonal rhabdomyosarcoma"]
---

# Docetaxel
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

# Docetaxel: De Docetaxel (indicación original no especificada) a Carcinoma de Mama Femenino

## Resumen en Una Frase

Docetaxel es un fármaco antineoplásico de la clase de los taxanos; en los registros sanitarios colombianos consultados solo figura el nombre del fármaco como indicación, sin detalle de la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **carcinoma de mama femenino**, con **más de 40 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección.
Cabe aclarar que en cáncer de mama el docetaxel ya es un tratamiento establecido, por lo que no se trata de un reposicionamiento en sentido estricto.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro solo indica "Docetaxel") |
| Nueva Indicación Predicha | Carcinoma de mama femenino |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L1 (≥2 ECA de Fase 3 completados: NCT00003519, NCT00021255, NCT00333775, NCT00887536, entre otros) |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Proceed with Guardrails |

> Nota: el análisis automatizado de los datos asignó nivel L2 a esta indicación. Al revisar los ensayos listados, hay varios ECA de Fase 3 completados, lo que cumple el criterio de L1. Se recomienda verificar este punto manualmente.

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, el docetaxel es un taxano que estabiliza los microtúbulos e impide la progresión de la mitosis, lo que afecta a las células tumorales que se dividen con rapidez.

La indicación original no está detallada en el registro colombiano, pero el fármaco pertenece a la quimioterapia citotóxica. El cáncer de mama es un tumor de proliferación celular activa, por lo que la lógica mecanística es directa. La literatura describe al docetaxel como un agente establecido en cáncer de mama avanzado, y los ensayos incluyen su uso en combinación con antraciclinas, ciclofosfamida, trastuzumab y bevacizumab.

Un punto a tener en cuenta: gran parte de los ensayos de Fase 3 evalúan regímenes combinados, donde docetaxel forma parte del esquema y el objetivo del estudio suele ser otro componente (por ejemplo, bevacizumab o lapatinib). Por eso, la contribución individual del docetaxel se infiere de la práctica clínica establecida más que de estos ensayos por separado.

---

## Evidencia de Ensayos Clínicos

Se listan los ensayos más relevantes, priorizando estudios completados de Fase 3 y Fase 2 con inscripción informativa.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00003519](https://clinicaltrials.gov/study/NCT00003519) | Fase 3 | Completado | 2778 | Adriamicina/docetaxel vs. adriamicina/ciclofosfamida como tratamiento adyuvante en cáncer de mama con ganglios positivos o de alto riesgo |
| [NCT00021255](https://clinicaltrials.gov/study/NCT00021255) | Fase 3 | Completado | 3222 | AC-T vs. AC-TH vs. TCH (docetaxel, carboplatino, trastuzumab) en cáncer de mama HER2 positivo operable |
| [NCT00003782](https://clinicaltrials.gov/study/NCT00003782) | Fase 3 | Completado | 5351 | Comparación de tres regímenes adyuvantes (AC-T, AT, ATC) con docetaxel en cáncer de mama con ganglios positivos |
| [NCT00002707](https://clinicaltrials.gov/study/NCT00002707) | Fase 3 | Completado | 2411 | Quimioterapia preoperatoria AC con o sin docetaxel antes o después de la cirugía |
| [NCT00333775](https://clinicaltrials.gov/study/NCT00333775) | Fase 3 | Completado | 736 | Bevacizumab + docetaxel vs. docetaxel + placebo en primera línea de cáncer de mama metastásico HER2 negativo |
| [NCT00887536](https://clinicaltrials.gov/study/NCT00887536) | Fase 3 | Completado | 1613 | TC + bevacizumab vs. TC solo vs. TAC en cáncer de mama HER2 negativo |
| [NCT00667251](https://clinicaltrials.gov/study/NCT00667251) | Fase 3 | Completado | 652 | Quimioterapia con taxano + lapatinib vs. trastuzumab en cáncer de mama metastásico HER2 positivo |
| [NCT03588091](https://clinicaltrials.gov/study/NCT03588091) | Fase 3 | Completado | 355 | Pirotinib + trastuzumab + docetaxel vs. placebo + trastuzumab + docetaxel en terapia neoadyuvante HER2 positivo |
| [NCT00431080](https://clinicaltrials.gov/study/NCT00431080) | Fase 3 | Completado | 478 | FE75C seguido de docetaxel vs. paclitaxel con dosis densas en cáncer de mama con ganglios positivos |
| [NCT00321633](https://clinicaltrials.gov/study/NCT00321633) | Fase 2 | Completado | 148 | Ensayo aleatorizado de carboplatino vs. docetaxel en cáncer de mama metastásico con mutación genética (BRCA) |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [28398846](https://pubmed.ncbi.nlm.nih.gov/28398846/) | 2017 | ECA | J Clin Oncol | Ensayos ABC: comparación de docetaxel + ciclofosfamida (TC) con regímenes de antraciclinas + taxano en cáncer de mama temprano |
| [10791395](https://pubmed.ncbi.nlm.nih.gov/10791395/) | 2000 | Revisión | Lancet | Los taxanos (paclitaxel y docetaxel) tienen actividad sustancial en cáncer de mama, pulmón y ovario |
| [21872996](https://pubmed.ncbi.nlm.nih.gov/21872996/) | 2012 | Revisión | Cancer Treat Rev | Docetaxel combinado con terapias dirigidas en cáncer de mama metastásico |
| [12868800](https://pubmed.ncbi.nlm.nih.gov/12868800/) | 2003 | Revisión | Breast Cancer Res Treat | Combinaciones de docetaxel y antraciclinas en cáncer de mama metastásico |
| [12868802](https://pubmed.ncbi.nlm.nih.gov/12868802/) | 2003 | Revisión | Breast Cancer Res Treat | Docetaxel neoadyuvante en cáncer de mama localmente avanzado |
| [9775340](https://pubmed.ncbi.nlm.nih.gov/9775340/) | 1998 | Revisión | Am J Health Syst Pharm | Farmacología, ensayos clínicos y efectos adversos del docetaxel en cáncer de mama metastásico |
| [16020974](https://pubmed.ncbi.nlm.nih.gov/16020974/) | 2005 | Fase 2 | Oncology | Docetaxel semanal + gemcitabina como primera línea en cáncer de mama metastásico |
| [26874836](https://pubmed.ncbi.nlm.nih.gov/26874836/) | 2017 | Estudio clínico | Breast Cancer | Docetaxel, ciclofosfamida y trastuzumab como quimioterapia neoadyuvante en cáncer de mama HER2 positivo |
| [27997437](https://pubmed.ncbi.nlm.nih.gov/27997437/) | 2017 | Cohorte | Anti-Cancer Drugs | Asociación entre quimioterapia adyuvante con docetaxel y linfedema relacionado con cáncer de mama |
| [12599222](https://pubmed.ncbi.nlm.nih.gov/12599222/) | 2003 | Estudio clínico | Cancer | Capecitabina con docetaxel y epirrubicina en cáncer de mama avanzado sin tratamiento previo |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19969842 (cancelado) | DOCETAXEL 80 MG INYECTABLE | Solución concentrada para infusión | DOCETAXEL |
| 20151870 (cancelado) | DOCETAXEL 10 MG/ML | Solución inyectable | DOCETAXEL |

Ambos registros sanitarios están cancelados, por lo que actualmente no hay registros vigentes de docetaxel en los datos consultados.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (clase taxano, antimitótico que estabiliza microtúbulos) |
| Riesgo de Mielosupresión | Alto. Las relaciones de seguridad conocidas incluyen neutropenia, trombocitopenia, anemia y agranulocitosis |
| Clasificación de Emetogenicidad | Baja a moderada |
| Items de Monitoreo | Hemograma con diferencial, función hepática (incluida bilirrubina), función renal, electrolitos, signos de neuropatía periférica y retención de líquidos |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

- **Contraindicaciones y condiciones de riesgo (según el grafo de conocimiento, no según el prospecto):** enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia, neutropenia, agranulocitosis, neuropatía periférica y otras enfermedades del sistema nervioso periférico, anemia, hiperbilirrubinemia (incluido el síndrome de Gilbert), enfermedad diarreica, edema pulmonar, estomatitis, neuritis y taponamiento cardíaco.
- **Interacciones Farmacológicas:** se identificaron 100 interacciones en total; las más relevantes de la muestra son:
  - **Mayor:** claritromicina.
  - **Moderadas:** aprepitant, metronidazol, cimetidina, eliglustat, miconazol, rolapitant, rosuvastatina, simvastatina, tinidazol y troglitazona.
  - **Menores:** dexametasona, levofloxacino, prednisolona y prednisona.
  - Algunas interacciones tienen nivel desconocido (calcitriol, clotrimazol, manitol, clorhexidina, ácido acetilsalicílico).

Para advertencias y contraindicaciones formales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen múltiples ensayos de Fase 3 completados y grandes (miles de pacientes) en cáncer de mama que incluyen docetaxel, además de literatura abundante, lo que respalda la predicción. Sin embargo, no es un reposicionamiento propiamente dicho, no hay registros vigentes en Colombia y faltan datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA con advertencias y contraindicaciones formales.
- Confirmar la indicación aprobada real de los registros y el estado regulatorio actual (registros cancelados; evaluar necesidad de nuevo registro o importación).
- Completar los datos del mecanismo de acción desde DrugBank.
- Aclarar qué parte del beneficio en los ensayos combinados corresponde al docetaxel.
- Definir un plan de monitoreo hematológico y de neuropatía, y revisar interacciones con inhibidores del CYP3A4 (por ejemplo, claritromicina).

---

### Otras indicaciones predichas (referencia)

Las demás predicciones del modelo tienen evidencia más débil: sarcoma de Ewing (L2, pregunta de investigación; ensayos de Fase 2 con gemcitabina/docetaxel), carcinoma pulmonar de células pequeñas (evidencia centrada en cáncer de pulmón no microcítico, sin beneficio directo demostrado), rabdomiosarcoma (L2, datos escasos) y varias indicaciones raras con solo reportes de casos o ninguna evidencia (Hold).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

