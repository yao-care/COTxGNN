---
layout: default
title: Triazolam
parent: 僅模型預測 (L5)
nav_order: 231
evidence_level: L5
indication_count: 1
---

# Triazolam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Triazolam: De Hipnótico Benzodiacepínico de Acción Corta a Trastorno del Sueño con Dificultad para Iniciar y Mantener el Sueño

---

## Resumen en Una Frase

Triazolam es un hipnótico benzodiacepínico de acción corta, con aprobación establecida por la FDA (EE. UU.) y la PMDA (Japón) para el tratamiento a corto plazo del insomnio, aunque actualmente no se encuentra comercializado en Colombia.
El modelo TxGNN predice que podría ser efectivo para **el trastorno del sueño con dificultad para iniciar y mantener el sueño**, indicación que coincide con su mecanismo de acción ya documentado.
Esta predicción está respaldada por **0 ensayos clínicos registrados** en la búsqueda actual, pero cuenta con **20 publicaciones científicas** — incluyendo la guía clínica oficial de la AASM, dos meta-análisis de red y múltiples revisiones sistemáticas — que refuerzan sólidamente esta dirección.

---

## Resumen Rápido

| Ítem | Contenido |
|------|-----------|
| Indicación Original | Insomnio a corto plazo (aprobado FDA/PMDA; no registrado en Colombia) |
| Nueva Indicación Predicha | Trastorno del sueño con dificultad para iniciar y mantener el sueño |
| Puntaje de Predicción TxGNN | 99.72% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Triazolam (Halcion®, Upjohn/Pfizer) es un benzodiacepínico triazolobenzodiazepínico de vida media corta (2–5 horas), con un mecanismo de acción bien establecido en la literatura farmacológica: actúa como modulador alostérico positivo del receptor GABA-A, aumentando la frecuencia de apertura de los canales de cloruro en la membrana neuronal. Este efecto potencia la neurotransmisión inhibitoria central en estructuras como el hipotálamo, el tálamo y la formación reticular —regiones clave en la regulación del ciclo sueño-vigilia— lo que se traduce directamente en reducción de la latencia del sueño y disminución de los despertares nocturnos.

La relación entre la indicación ya aprobada y la predicha por TxGNN no es una extrapolación, sino una confirmación mecanística: la entidad clínica *"sleep disorder, initiating and maintaining sleep"* (CIE: insomnio con dificultad de inicio y mantenimiento) corresponde exactamente a la indicación para la cual triazolam recibió aprobación regulatoria en múltiples jurisdicciones. La guía clínica de la AASM (PMID 27998379), el meta-análisis en red de *Sleep* (PMID 33249496) y la revisión sistemática de 2025 en *Psychiatry and Clinical Neurosciences* (PMID 40110890) lo mencionan explícitamente como agente de referencia en esta clase terapéutica.

El contexto de este análisis es, por tanto, un escenario de **introducción a mercado** más que de reposicionamiento primario. Triazolam no se comercializa actualmente en Colombia (0 registros sanitarios), a pesar de contar con décadas de evidencia clínica internacional. La predicción de TxGNN funciona aquí como validación cuantitativa del potencial terapéutico del fármaco en la indicación objetivo, respaldando la evaluación regulatoria de su ingreso al mercado colombiano con una base de evidencia consolidada.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados en ClinicalTrials.gov ni en el ICTRP para triazolam en esta indicación dentro del período de búsqueda.

> **Nota:** La ausencia de ensayos registrados refleja que triazolam es un compuesto clásico cuya evidencia clínica fue generada predominantemente antes de la era de registro obligatorio de ensayos (pre-2000). La base de evidencia se encuentra íntegramente en la literatura publicada detallada a continuación.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [27998379](https://pubmed.ncbi.nlm.nih.gov/27998379/) | 2017 | Guía Clínica (AASM) | J Clin Sleep Med | Guía oficial de la AASM para tratamiento farmacológico del insomnio crónico en adultos; triazolam evaluado individualmente como hipnótico de referencia |
| [40110890](https://pubmed.ncbi.nlm.nih.gov/40110890/) | 2025 | Revisión Sistemática / Meta-análisis | Psychiatry Clin Neurosci | Meta-análisis de ECAs doble ciego: eficacia y seguridad de benzodiacepinas (incluido triazolam) vs. otras clases de hipnóticos en insomnio con depresión mayor comórbida |
| [39932761](https://pubmed.ncbi.nlm.nih.gov/39932761/) | 2025 | Revisión (Seminar Lancet) | Minerva Medica | Seminar de actualización integral sobre el trastorno de insomnio; epidemiología, diagnóstico y opciones farmacológicas incluyendo benzodiacepinas |
| [33249496](https://pubmed.ncbi.nlm.nih.gov/33249496/) | 2021 | Meta-análisis en Red | Sleep | Comparación de eficacia y seguridad de hipnóticos en adultos mayores; triazolam incluido como comparador activo en análisis de red |
| [30058034](https://pubmed.ncbi.nlm.nih.gov/30058034/) | 2018 | Revisión (población anciana) | Drugs & Aging | Revisión de manejo farmacológico del insomnio en pacientes ≥65 años; discusión de perfil riesgo-beneficio de triazolam vs. alternativas |
| [27751669](https://pubmed.ncbi.nlm.nih.gov/27751669/) | 2016 | Revisión (seguridad anciana) | Clinical Therapeutics | Evaluación sistemática de seguridad y eficacia de hipnóticos en adultos mayores; análisis farmacocinético de triazolam |
| [19682231](https://pubmed.ncbi.nlm.nih.gov/19682231/) | 2010 | ECA Cruzado (humanos) | J Sleep Research | ECA cruzado en humanos: efectos retrógrados de triazolam y zolpidem sobre el aprendizaje motor dependiente del sueño; confirma eficacia hipnótica de triazolam |
| [9161660](https://pubmed.ncbi.nlm.nih.gov/9161660/) | 1997 | Revisión Comparativa | Ann Pharmacother | Comparación directa de zolpidem vs. triazolam en eficacia y seguridad; establece perfil diferencial de triazolam como hipnótico de corta duración |
| [2567741](https://pubmed.ncbi.nlm.nih.gov/2567741/) | 1989 | Revisión Crítica | J Clin Psychopharmacol | Revisión crítica del insomnio de rebote tras suspensión de triazolam; estudios en laboratorio del sueño con polisomnografía |
| [1319429](https://pubmed.ncbi.nlm.nih.gov/1319429/) | 1992 | Revisión Farmacológica | J Clin Psychiatry | Revisión histórica del papel de triazolam en la "segunda revolución" del tratamiento farmacológico del insomnio; posicionamiento frente a flurazepam y temazepam |

---

## Información de Mercado en Colombia

No hay registros sanitarios disponibles para triazolam en Colombia. El fármaco figura como **no comercializado** en el mercado colombiano al corte de datos (2026-06-06).

> Para consulta comparativa: triazolam cuenta con aprobación vigente de la FDA (EE. UU.) bajo la marca Halcion® y de la PMDA (Japón) para el tratamiento a corto plazo del insomnio. Su eventual ingreso al mercado colombiano requeriría presentación ante el INVIMA con el dossier completo de registro sanitario.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

> **Alerta de clase:** Triazolam pertenece a la clase benzodiacepínica, asociada a riesgo de dependencia, tolerancia, insomnio de rebote al suspender, y deterioro cognitivo/psicomotor especialmente en adultos mayores. La ausencia de datos de seguridad locales en este paquete de evidencia (DG001: datos de advertencias TFDA no disponibles) constituye una brecha **bloqueante** que debe resolverse antes de la evaluación regulatoria formal ante el INVIMA.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Triazolam posee el mayor nivel de evidencia posible para su indicación predicha (L1): está aprobado por la FDA y la PMDA para el tratamiento a corto plazo del insomnio, con décadas de estudios clínicos, guías de práctica clínica de sociedades científicas de primer nivel (AASM) y meta-análisis en red que respaldan su eficacia. La predicción de TxGNN (99.72%) confirma cuantitativamente la solidez de la relación fármaco-indicación. El escenario no es de reposicionamiento exploratorio, sino de evaluación de ingreso a un mercado donde el fármaco aún no está registrado.

**Para avanzar se necesita:**

- **[Bloqueante]** Obtener y revisar el prospecto oficial (hoja de datos del fabricante o ficha técnica FDA/EMA/PMDA) para completar el perfil de advertencias, contraindicaciones e interacciones farmacológicas — requerido para la evaluación S1 de seguridad ante el INVIMA
- **[Alta prioridad]** Confirmar el mecanismo de acción (MOA) formal en DrugBank (DB00897) para completar la sección de análisis de mecanismo en el dossier regulatorio
- Evaluar el perfil de riesgo-beneficio específico para la población colombiana, con énfasis en adultos mayores (riesgo de caídas, dependencia, deterioro cognitivo) dado que múltiples revisiones identifican esta subpoblación como de riesgo elevado con benzodiacepinas
- Revisar la clasificación regulatoria colombiana aplicable (probable Lista IV de sustancias controladas, equivalente a Schedule IV DEA) y obtener los permisos de importación/comercialización ante el Fondo Nacional de Estupefacientes (FNE)
- Considerar si el perfil de seguridad de triazolam es competitivo frente a alternativas ya registradas en Colombia (zolpidem, eszopiclona, melatonina, orexin antagonistas) antes de iniciar el proceso formal de registro
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

