---
layout: default
title: Haloperidol
parent: 僅模型預測 (L5)
nav_order: 89
evidence_level: L5
indication_count: 10
---

# Haloperidol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

Usando el skill `txgnn-pipeline` para orientar la generación del informe con las convenciones del pipeline TxGNN — el skill no está disponible como herramienta diferida, pero la tarea es claramente un informe de evaluación de reposicionamiento estándar. Procedo directamente con la generación del informe según el Evidence Pack y el formato especificado.

**Decisión de diseño clave:** Entre las 10 indicaciones predichas, solo **Trastorno Bipolar Maníaco** (rank 10 en el array) alcanza nivel L1 y recomendación "Proceed with Guardrails". El resto son L5 / Hold. El informe se centra en esta indicación, que es la candidata clínicamente accionable.

---

# Haloperidol: De Esquizofrenia y Trastornos Psicóticos a Trastorno Bipolar Maníaco

## Resumen en Una Frase

Haloperidol es un antipsicótico típico de primera generación, utilizado clásicamente en el tratamiento de la esquizofrenia y otros trastornos psicóticos graves. El modelo TxGNN predice que podría ser efectivo para el **Trastorno Bipolar Maníaco**, con **9 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección. Esta predicción es altamente coherente con el uso histórico del fármaco y con las guías internacionales de práctica clínica, donde haloperidol ha actuado como comparador activo validado en múltiples ensayos de Fase 3 para el control de episodios maníacos agudos.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Esquizofrenia y trastornos psicóticos (indicación conocida; sin registro sanitario activo en Colombia) |
| Nueva Indicación Predicha | Trastorno Bipolar Maníaco |
| Puntaje de Predicción TxGNN | 99.83% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | No Comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados del mecanismo de acción desde DrugBank. Según la información farmacológica conocida, haloperidol pertenece a la clase de los antipsicóticos típicos de primera generación, caracterizados por su alta afinidad y bloqueo potente de los receptores dopaminérgicos D2 en el sistema nervioso central. Esta acción ha sido la base de su eficacia comprobada en la esquizofrenia durante más de seis décadas de uso clínico global.

La conexión mecanística con el trastorno bipolar maníaco es sólida y bien sustentada por la **hipótesis de hiperactividad dopaminérgica** (*dopamine hyperactivity hypothesis*): la sobreactivación de los receptores D2 en el sistema límbico se asocia estrechamente con los síntomas cardinales de la manía aguda —euforia, grandiosidad, desinhibición y agitación psicomotora—. Al bloquear con alta afinidad estos receptores D2, haloperidol suprime eficazmente la hiperactividad dopaminérgica límbica, produciendo un efecto antimaníaco directo. El Evidence Pack califica esta vinculación mecanística como de **alta concordancia**.

El respaldo clínico refuerza este razonamiento: haloperidol fue seleccionado como comparador activo de referencia en al menos cuatro ensayos de Fase 3 específicamente diseñados para el tratamiento de la manía aguda en trastorno bipolar I, lo que refleja el consenso científico sobre su eficacia en esta indicación. Su uso está además respaldado por guías de práctica clínica internacionales y por una revisión sistemática con metaanálisis en red publicada en *Molecular Psychiatry* (2022).

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|--------|-------------|----------------------|
| [NCT00097266](https://clinicaltrials.gov/study/NCT00097266) | Fase 3 | Completado | 615 | Ensayo más amplio de la serie; HAL como comparador activo frente a aripiprazol en monoterapia para manía aguda en trastorno bipolar I durante 12 semanas |
| [NCT00253162](https://clinicaltrials.gov/study/NCT00253162) | Fase 3 | Completado | 439 | HAL como comparador activo frente a risperidona vs placebo en episodios maníacos de trastorno bipolar I; validación directa de eficacia en manía hasta semana 12 |
| [NCT00129220](https://clinicaltrials.gov/study/NCT00129220) | Fase 3 | Completado | 224 | Ensayo doble ciego, placebo-controlado y HAL-controlado para olanzapina en episodio maníaco/mixto de trastorno bipolar I; HAL como estándar activo de referencia |
| [NCT00253149](https://clinicaltrials.gov/study/NCT00253149) | Fase 3 | Completado | 158 | HAL (5–15 mg/día) como terapia adyuvante a estabilizadores del ánimo en manía de trastorno bipolar I; evaluación directa de eficacia y seguridad |
| [NCT04327843](https://clinicaltrials.gov/study/NCT04327843) | Fase 3 | Completado | 22 | LAI combinado con programa conductual para adherencia en trastornos psicóticos crónicos en Tanzania; muestra muy pequeña (22 pacientes), datos limitados |
| [NCT00126009](https://clinicaltrials.gov/study/NCT00126009) | Fase 2 | Completado | 120 | Comparación valproato+amisulprida vs valproato+HAL (5–15 mg/día) en episodio maníaco de trastorno bipolar I durante 3 meses |
| [NCT06049953](https://clinicaltrials.gov/study/NCT06049953) | N/A | Reclutando | 200 | Estudio observacional sobre efectos del desarrollo ante exposición prenatal a antipsicóticos en personas con enfermedad mental grave; objetivo indirecto |
| [NCT00767715](https://clinicaltrials.gov/study/NCT00767715) | Fase 4 | Terminado | 11 | Estudio terminado prematuramente (11 pacientes); comparación olanzapina vs antipsicóticos convencionales en manía aguda en Suecia; datos insuficientes |
| [NCT03541031](https://clinicaltrials.gov/study/NCT03541031) | N/A | Desconocido | 120 | Micronutrientes como tratamiento adyuvante en trastorno bipolar; sin relación directa con haloperidol |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [34642461](https://pubmed.ncbi.nlm.nih.gov/34642461/) | 2022 | Revisión Sistemática / NMA | Molecular Psychiatry | Metaanálisis en red de ECAs doble ciego para tratamiento farmacológico de manía bipolar aguda; haloperidol incluido como intervención comparada; evidencia de mayor jerarquía disponible |
| [22134043](https://pubmed.ncbi.nlm.nih.gov/22134043/) | 2012 | ECA | Journal of Affective Disorders | ECA aleatorizado doble ciego, placebo y HAL-controlado, para olanzapina en pacientes japoneses con trastorno bipolar I en episodio maníaco/mixto; HAL como referencia activa |
| [3312180](https://pubmed.ncbi.nlm.nih.gov/3312180/) | 1987 | ECA (histórico) | Journal of Clinical Psychiatry | Ensayo controlado doble ciego comparando clonazepam vs litio vs haloperidol en manía aguda; evidencia histórica seminal del rol de HAL en esta indicación |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Revisión Clínica / Guías | Acta Psychiatrica Scandinavica | Revisión de opciones basadas en evidencia para manía bipolar; propone sugerencias clínicas sobre la elección de estabilizadores del ánimo y antipsicóticos |
| [22070611](https://pubmed.ncbi.nlm.nih.gov/22070611/) | 2012 | Revisión basada en evidencia | CNS Neuroscience & Therapeutics | En pacientes maníacos refractarios con respuesta parcial a litio/valproato/carbamazepina, se recomienda añadir haloperidol como una de las opciones de primera elección |
| [27151529](https://pubmed.ncbi.nlm.nih.gov/27151529/) | 2016 | Revisión Sistemática | Human Psychopharmacology | Metaanálisis de intervenciones farmacológicas a corto plazo para agitación asociada a esquizofrenia o trastorno bipolar; haloperidol evaluado como opción de referencia |
| [36789916](https://pubmed.ncbi.nlm.nih.gov/36789916/) | 2023 | Análisis Comparativo | BMJ Mental Health | Comparación de equivalencias de dosis de antipsicóticos entre manía aguda y esquizofrenia; contextualiza el uso de HAL en ambas indicaciones |
| [18344731](https://pubmed.ncbi.nlm.nih.gov/18344731/) | 2008 | Revisión Sistemática | Journal of Clinical Psychopharmacology | Revisión sobre efectos extrapiramidales (EPS) inducidos por antipsicóticos en trastorno bipolar y esquizofrenia; HAL presenta mayor tasa de EPS que antipsicóticos atípicos; relevante para el plan de monitoreo |
| [19454110](https://pubmed.ncbi.nlm.nih.gov/19454110/) | 2007 | Revisión | BMJ Clinical Evidence | Revisión de opciones terapéuticas para trastorno bipolar, incluyendo antipsicóticos en el manejo agudo de la manía |
| [15147609](https://pubmed.ncbi.nlm.nih.gov/15147609/) | 2004 | Evaluación HTA | Health Technology Assessment | Evaluación sistemática de efectividad clínica y costo-efectividad de tratamientos para manía asociada a trastorno bipolar; HAL empleado como referencia comparativa |

---

## Información de Mercado en Colombia

No se encontraron registros sanitarios activos para Haloperidol en el sistema regulatorio consultado (corte: 2026-05-05). El fármaco figura como **No Comercializado** según los datos disponibles. Se recomienda verificar directamente en INVIMA si existen registros vigentes bajo otras denominaciones, presentaciones o titulares de registro.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Cuatro ensayos clínicos de Fase 3 —incluyendo uno con 615 participantes y otro con 439— posicionan a haloperidol como comparador activo validado en el tratamiento de la manía aguda del trastorno bipolar I, respaldados por una revisión sistemática con metaanálisis en red de Tier 1 (*Molecular Psychiatry*, 2022). La base mecanística (antagonismo D2 frente a hiperdopaminergia límbica) es sólida, reconocida en guías internacionales y calificada como de alta concordancia en el Evidence Pack.

**Para avanzar se necesita:**
- Datos completos del mecanismo de acción (MOA) desde DrugBank (DG002)
- Advertencias, contraindicaciones e interacciones farmacológicas desde el prospecto oficial —priorizar INVIMA si existe registro vigente— (DG001)
- Verificación directa en INVIMA para confirmar si existen registros sanitarios bajo otras denominaciones o presentaciones en Colombia
- Plan de monitoreo de seguridad para efectos extrapiramidales (EPS), discinesia tardía y síndrome neuroléptico maligno, dada la mayor carga de EPS de los antipsicóticos típicos vs atípicos
- Análisis de posicionamiento clínico frente a antipsicóticos de segunda generación en el contexto del sistema de salud colombiano
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

