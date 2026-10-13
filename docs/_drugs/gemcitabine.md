---
layout: default
title: Gemcitabine
parent: Evidencia Alta (L1-L2)
nav_order: 311
evidence_level: L1
indication_count: 10
---

# Gemcitabine
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Gemcitabina: De Indicación Registrada (sin detalle) a Carcinoma de Mama Femenino

## Resumen en Una Frase

Gemcitabina es un análogo de nucleósido citotóxico, con registros sanitarios en Colombia que hoy figuran como cancelados y cuyo texto de indicación solo repite el nombre del fármaco.
El modelo TxGNN predice que podría ser efectivo para **carcinoma de mama femenino**, con **más de 35 ensayos clínicos registrados** (varios de Fase 3 completados) y **20 publicaciones** que respaldan esta dirección. Cabe aclarar que se trata de un uso oncológico ya establecido, no de una señal nueva de reposicionamiento.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro sanitario (el texto aprobado solo dice "GEMCITABINA") |
| Nueva Indicación Predicha | Carcinoma de mama femenino |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 5 (0 vigentes, 5 cancelados) |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Gemcitabina es un análogo de nucleósido (antimetabolito de pirimidina). Inhibe la síntesis de ADN y la enzima ribonucleótido reductasa, lo que le confiere actividad citotóxica amplia contra tumores sólidos de rápida división. Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción, por lo que esta explicación se basa en el conocimiento farmacológico general del fármaco.

La indicación original no está detallada en los registros colombianos, pero gemcitabina es un quimioterápico ampliamente usado en tumores sólidos. Su aplicación en cáncer de mama está respaldada por ensayos clínicos y revisiones que la evalúan sola o combinada con paclitaxel, docetaxel, platinos, antraciclinas, vinorelbina y trastuzumab.

Por ello, la predicción de TxGNN es coherente con el historial clínico existente y no representa un hallazgo mecanístico nuevo.

---

## Evidencia de Ensayos Clínicos

Se muestran los ensayos más relevantes para cáncer de mama (de más de 35 registrados).

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00006459](https://clinicaltrials.gov/study/NCT00006459) | Fase 3 | Completado | No informada | Paclitaxel con o sin gemcitabina en cáncer de mama avanzado o metastásico irresecable |
| [NCT00093795](https://clinicaltrials.gov/study/NCT00093795) | Fase 3 | Completado | 4894 | Tres regímenes adyuvantes en cáncer de mama con ganglios positivos, uno con gemcitabina añadida a paclitaxel |
| [NCT00408408](https://clinicaltrials.gov/study/NCT00408408) | Fase 3 | Desconocido | 1206 | Neoadyuvancia: capecitabina o gemcitabina añadidas a docetaxel antes de AC, con o sin bevacizumab |
| [NCT00070278](https://clinicaltrials.gov/study/NCT00070278) | Fase 3 | Desconocido | 800 | Epirubicina/ciclofosfamida seguida de paclitaxel con o sin gemcitabina, neoadyuvancia en cáncer temprano de mal pronóstico |
| [NCT00039546](https://clinicaltrials.gov/study/NCT00039546) | Fase 3 | Desconocido | No informada | Estudio tAnGo: gemcitabina añadida a quimioterapia adyuvante en cáncer temprano ER/PgR-pobre |
| [NCT00006007](https://clinicaltrials.gov/study/NCT00006007) | Fase 2 | Completado | 59 | Pemetrexed más gemcitabina en cáncer de mama metastásico |
| [NCT00110084](https://clinicaltrials.gov/study/NCT00110084) | Fase 2 | Completado | 50 | Nab-paclitaxel semanal más gemcitabina en cáncer de mama metastásico |
| [NCT00244933](https://clinicaltrials.gov/study/NCT00244933) | Fase 2 | Completado | 19 | Gemcitabina más genisteína en cáncer de mama metastásico (muestra pequeña) |
| [NCT07528768](https://clinicaltrials.gov/study/NCT07528768) | Fase 2 | Aún sin reclutar | 750 | Gemcitabina vs. paclitaxel en cáncer de mama triple negativo metastásico en mujeres de ascendencia africana |
| [NCT06027268](https://clinicaltrials.gov/study/NCT06027268) | Fase 2 | Activo, sin reclutar | 36 | Trilaciclib, pembrolizumab, gemcitabina y carboplatino en cáncer de mama triple negativo |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [15685819](https://pubmed.ncbi.nlm.nih.gov/15685819/) | 2004 | Revisión | Oncology (Williston Park) | Gemcitabina y paclitaxel son activos en cáncer de mama metastásico; la combinación es segura según datos de Fase I y se evaluó en Fase II y III |
| [15685821](https://pubmed.ncbi.nlm.nih.gov/15685821/) | 2004 | Revisión | Oncology (Williston Park) | Gemcitabina con platinos aporta beneficio clínico y tasas de respuesta en cáncer de mama metastásico |
| [15685820](https://pubmed.ncbi.nlm.nih.gov/15685820/) | 2004 | Revisión | Oncology (Williston Park) | Combinación gemcitabina-docetaxel con toxicidades parcialmente no solapadas en cáncer de mama metastásico |
| [14768404](https://pubmed.ncbi.nlm.nih.gov/14768404/) | 2003 | Revisión | Oncology (Williston Park) | Combinaciones de gemcitabina con antraciclinas y taxanos en cáncer de mama avanzado |
| [12138397](https://pubmed.ncbi.nlm.nih.gov/12138397/) | 2002 | Revisión | Seminars in Oncology | Gemcitabina sola logra respuestas de 16% a 37%; las combinaciones muestran tasas mayores |
| [14754469](https://pubmed.ncbi.nlm.nih.gov/14754469/) | 2004 | Revisión | Clinical Breast Cancer | Fundamento y datos clínicos de gemcitabina más trastuzumab en cáncer de mama HER2 positivo |
| [40779028](https://pubmed.ncbi.nlm.nih.gov/40779028/) | 2025 | Estudio clínico (Fase I) | Breast Cancer Research and Treatment | Carboplatino, gemcitabina y mifepristona en cáncer de mama avanzado y ovario recurrente |
| [12057045](https://pubmed.ncbi.nlm.nih.gov/12057045/) | 2002 | Revisión | Clinical Breast Cancer | Gemcitabina neoadyuvante en cáncer de mama, con perfil de toxicidad favorable |
| [36047536](https://pubmed.ncbi.nlm.nih.gov/36047536/) | 2022 | Preclínico | Drug Dev Ind Pharm | Nanopartículas lipídicas dirigidas a integrina αvβ3 mejoran la actividad antitumoral de gemcitabina en mama |
| [28961673](https://pubmed.ncbi.nlm.nih.gov/28961673/) | 2017 | Reporte de caso | Retina | Retinopatía inducida por gemcitabina (evento adverso) |

---

## Información de Mercado en Colombia

Los cinco registros sanitarios están **cancelados**; actualmente no hay registros vigentes.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20062273 | GEMCITABINA 1.0 G (Blau Farmacéutica Colombia) | Polvo liofilizado para reconstituir a solución inyectable | GEMCITABINA |
| 20011867 | GEMCITABINA 1.0 G/VIAL (Venus Remedies) | Polvo liofilizado para reconstituir a solución inyectable | GEMCITABINA |
| 20063548 | GEMTIN® 1000 MG (Hetero Labs) | Polvo liofilizado para reconstituir a solución inyectable | GEMCITABINA |
| 215185 | GEMZAR LILLY® 200 MG (Cheplapharm) | Polvo liofilizado para reconstituir a solución inyectable | GEMCITABINA |
| 20165644 | VIRULIZIN SOLUCIÓN INYECTABLE (AL Pharma) | Solución concentrada para infusión | GEMCITABINA |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (antimetabolito, análogo de nucleósido de pirimidina) |
| Riesgo de Mielosupresión | Medio a alto. Las asociaciones del grafo de conocimiento con leucopenia, trombocitopenia y anemia señalan la médula ósea como órgano de riesgo |
| Clasificación de Emetogenicidad | Baja a moderada |
| Items de Monitoreo | Hemograma con diferencial (leucocitos, plaquetas, hemoglobina), función hepática y renal, y vigilancia de síntomas pulmonares |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos (preparación en cabina, guantes y bata de protección) |

---

## Consideraciones de Seguridad

- **Contraindicaciones y condiciones de riesgo (grafo de conocimiento, no texto de prospecto)**: enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia, anemia (incluida la macrocítica), leucopenia, enfermedad pulmonar intersticial, síndrome hemolítico urémico (incluida la forma típica), enfermedades infecciosas y piouréter.
- **Interacciones farmacológicas**: se identificaron 339 posibles interacciones. Entre las principales con nivel clasificado están naltrexona (moderada) y levofloxacino (menor). Otras, como calcitriol, doxiciclina, pantoprazol, omeprazol, morfina y metformina, figuran con nivel no determinado.
- **Evento adverso documentado**: la literatura describe un caso de retinopatía inducida por gemcitabina.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen varios ensayos de Fase 3 completados (por ejemplo NCT00006459 y NCT00093795) y numerosas revisiones que respaldan gemcitabina en cáncer de mama, lo que sustenta un nivel de evidencia L1. Sin embargo, no hay registros vigentes en Colombia y faltan datos del prospecto, por lo que se requieren salvaguardas antes de avanzar.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA para advertencias y contraindicaciones oficiales.
- Confirmar el mecanismo de acción con una fuente como DrugBank.
- Definir la ruta regulatoria, ya que los cinco registros están cancelados y no hay producto vigente en el país.
- Establecer un plan de monitoreo hematológico, renal y hepático, y de manejo seguro de citotóxicos.
- Aclarar el subtipo de cáncer de mama objetivo (por ejemplo triple negativo o HER2 positivo) y la línea de tratamiento.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

