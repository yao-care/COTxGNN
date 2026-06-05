---
layout: default
title: Cabazitaxel
parent: 僅模型預測 (L5)
nav_order: 76
evidence_level: L5
indication_count: 10
---

# Cabazitaxel
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

La skill `txgnn-pipeline` confirma el contexto del proyecto. Ahora procedo a redactar el informe con el Evidence Pack proporcionado.

---

# Cabazitaxel: De Cáncer de Próstata Resistente a la Castración a Carcinoma de Mama Femenino

## Resumen en Una Frase

Cabazitaxel es un taxano de segunda generación aprobado por la FDA (2010) para el tratamiento del cáncer de próstata metastásico resistente a la castración (mCRPC) en pacientes con progresión tras docetaxel.
El modelo TxGNN predice que podría ser efectivo para **Carcinoma de Mama Femenino**,
con **0 ensayos clínicos registrados** en bases de datos actuales (ClinicalTrials.gov/ICTRP) y **20 publicaciones** —incluyendo un ECA de Fase 2 y un estudio de Fase 1/II identificados en literatura— que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Ítem | Contenido |
|------|-----------|
| Indicación Original | Cáncer de próstata metastásico resistente a la castración (mCRPC) — aprobación FDA/EMA; sin registro en Colombia |
| Nueva Indicación Predicha | Carcinoma de mama femenino |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Cabazitaxel pertenece a la clase de los taxanos y actúa como estabilizador de microtúbulos: se une a la tubulina polimerizada, inhibe la despolimerización del huso mitótico y bloquea la división celular en la fase G2/M. Su ventaja clave respecto a paclitaxel y docetaxel es su baja afinidad por la P-glicoproteína (P-gp), la bomba de eflujo responsable de la resistencia múltiple a fármacos (MDR) más prevalente en tumores que han progresado bajo taxanos de primera generación. Estudios mecanísticos en líneas MCF-7 demostraron que la resistencia cruzada con cabazitaxel es 15 veces menor que con paclitaxel (200×), lo que constituye una diferenciación clínica relevante (PMID 25416788).

El carcinoma de mama, especialmente el subtipo triple negativo (TNBC) y los casos con resistencia adquirida a taxanos, comparte con el mCRPC la dependencia en la actividad de microtúbulos para la proliferación celular. El TNBC carece de dianas moleculares (ER/PR/HER2), por lo que la quimioterapia citotóxica sigue siendo el eje principal del tratamiento. La baja resistencia cruzada de cabazitaxel representa una diferenciación clínica relevante para pacientes que han agotado opciones con paclitaxel o docetaxel. Además, estudios preclínicos recientes han identificado un efecto inmunomodulador sobre macrófagos asociados a tumor (TAMs), abriendo potenciales sinergias con inmunoterapia anti-CD47 en TNBC (PMID 33753567).

La evidencia clínica directa incluye el ensayo GENEVIEVE (Phase 2 RCT, PMID 28768217), que comparó cabazitaxel vs paclitaxel semanal como neoadyuvante en cáncer de mama HER2-negativo, y un estudio de Fase 1/II (PMID 21339064) en cáncer de mama metastásico previamente tratado con taxanos y antraciclinas. Aunque estos estudios no están indexados en ClinicalTrials.gov bajo el término de búsqueda utilizado, su existencia en literatura revisada por pares justifica el nivel de evidencia L2 y respalda la razonabilidad de la predicción.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados en ClinicalTrials.gov ni en el ICTRP para la combinación cabazitaxel + carcinoma de mama femenino con los criterios de búsqueda actuales. Los estudios clínicos identificados (GENEVIEVE Fase 2 y el estudio Fase 1/II de Villanueva et al.) aparecen únicamente en literatura publicada — véase la sección siguiente.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [28768217](https://pubmed.ncbi.nlm.nih.gov/28768217/) | 2017 | ECA Fase 2 | Eur J Cancer | Estudio GENEVIEVE: cabazitaxel vs paclitaxel semanal como neoadyuvante en cáncer de mama HER2-negativo (TNBC y luminal B); comparó tasa de respuesta patológica completa (pCR) |
| [21339064](https://pubmed.ncbi.nlm.nih.gov/21339064/) | 2011 | Fase 1/II | Eur J Cancer | Cabazitaxel + capecitabina en cáncer de mama metastásico resistente a taxanos y antraciclinas; evaluó dosis máxima tolerada, seguridad, farmacocinética y actividad antitumoral |
| [25416788](https://pubmed.ncbi.nlm.nih.gov/25416788/) | 2015 | Revisión Mecanística | Mol Cancer Ther | Cabazitaxel muestra 15× menor resistencia cruzada vs paclitaxel (200×) en modelo MCF-7 MDR; el mecanismo de superación de MDR se asocia a baja afinidad por P-gp |
| [33247980](https://pubmed.ncbi.nlm.nih.gov/33247980/) | 2021 | Revisión PK Clínica | Br J Clin Pharmacol | Revisión de monitoreo terapéutico para taxanos; describe parámetros PK/PD de cabazitaxel en tumores sólidos avanzados y bases para ajuste de dosis personalizado |
| [33753567](https://pubmed.ncbi.nlm.nih.gov/33753567/) | 2021 | Preclínico (in vivo + in vitro) | J Immunother Cancer | Cabazitaxel modula macrófagos asociados a tumor (TAMs), potenciando la inmunoterapia anti-CD47 en TNBC; propone sinergia entre quimioterapia e inmunoterapia en modelo preclínico |
| [21076710](https://pubmed.ncbi.nlm.nih.gov/21076710/) | 2010 | Revisión | Drugs Today | Caracterización de cabazitaxel como nuevo taxano con perfil PK favorable y menor susceptibilidad a P-gp; activo en líneas celulares resistentes incluyendo modelos de cáncer de mama |
| [36918084](https://pubmed.ncbi.nlm.nih.gov/36918084/) | 2023 | Preclínico (in vivo) | J Control Release | Nanomedicina redox-responsiva (CS-DTM-CTX) con cabazitaxel inhibe la invasión mediada por fibroblastos asociados a cáncer (CAFs) en modelo in vivo de cáncer de mama |
| [30529259](https://pubmed.ncbi.nlm.nih.gov/30529259/) | 2019 | Preclínico (PDX) | J Control Release | Nanopartículas PACA con cabazitaxel lograron remisión completa en 6/8 tumores en modelo PDX de cáncer de mama basal-like; eficacia superior al fármaco libre |
| [38562610](https://pubmed.ncbi.nlm.nih.gov/38562610/) | 2024 | Preclínico (in vitro + in vivo) | Int J Nanomedicine | Variantes de nanopartículas PACA con cabazitaxel muestran eficacia preclínica en modelos de cáncer de mama con modulación del microambiente tumoral y reducción de macrófagos M2 |
| [34309357](https://pubmed.ncbi.nlm.nih.gov/34309357/) | 2021 | Preclínico (entrega dirigida) | Bioconjugate Chem | Cabazitaxel conjugado a péptido penetrante cíclico (cCPP) con entrega dirigida por integrinas y EDB-Fn; evaluado en modelos de cáncer de mama y próstata |

---

## Información de Mercado en Colombia

Cabazitaxel **no cuenta con registros sanitarios activos en Colombia** (INVIMA). El fármaco no se encuentra comercializado en el mercado colombiano a la fecha de corte de datos (2026-05-06). Cualquier uso requeriría importación bajo régimen especial o protocolo de uso compasivo, sujeto a aprobación de INVIMA caso por caso.

---

## Citotoxicidad

| Ítem | Contenido |
|------|-----------|
| Clasificación de Citotoxicidad | Citotóxico convencional — Clase Taxano (estabilizador de microtúbulos, segunda generación) |
| Riesgo de Mielosupresión | **Alto** — neutropenia es la toxicidad limitante de dosis más frecuente y grave (incluye neutropenia febril); trombocitopenia y anemia también reportadas |
| Clasificación de Emetogenicidad | Baja (los taxanos son clasificados como agentes de bajo riesgo emetogénico según guías MASCC/ESMO/ASCO) |
| Ítems de Monitoreo | Hemograma completo con diferencial (antes de cada ciclo y durante el tratamiento); función hepática (TGO, TGP, bilirrubinas); función renal (creatinina, clearance de creatinina); evaluación de neuropatía periférica; signos de hipersensibilidad |
| Protección en Manejo | Preparación obligatoria en campana de flujo laminar vertical (Clase II tipo B); personal con EPP completo (doble guante, mascarilla FFP2, bata impermeable); eliminación como residuo citotóxico según normativa vigente |

---

## Consideraciones de Seguridad

Consultar el prospecto oficial para información completa de advertencias, precauciones y contraindicaciones. Los datos de seguridad específicos para Colombia no están disponibles en las fuentes consultadas (INVIMA), dado que el fármaco no tiene registro sanitario local. Se recomienda remitirse al etiquetado FDA/EMA aprobado para cabazitaxel (Jevtana®) como referencia de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe evidencia clínica de Fase 2 (GENEVIEVE) y Fase 1/II en cáncer de mama que, junto a una sólida racionalidad mecanística basada en la superación de MDR por baja afinidad a P-gp, justifica avanzar con cautela. Sin embargo, la ausencia de registro sanitario en Colombia y los vacíos de datos en MOA y seguridad local requieren que cualquier avance esté estrictamente respaldado por protocolos de investigación clínica formales.

**Para avanzar se necesita:**
- Obtener MOA detallado desde DrugBank API (Data Gap DG002) para completar el análisis de racionalidad mecanística
- Recuperar y analizar el prospecto oficial (FDA/EMA) para advertencias, contraindicaciones e interacciones (Data Gap DG001)
- Evaluar viabilidad de importación bajo régimen de uso especial o protocolo de investigación clínica ante INVIMA
- Ampliar la búsqueda de ensayos clínicos activos por subtipo específico (TNBC, cáncer de mama HER2-negativo resistente a taxanos)
- Definir la subpoblación objetivo prioritaria (TNBC resistente a taxanos de primera línea) para delimitar el alcance del protocolo de uso
- Revisar datos de seguridad en poblaciones especiales relevantes para Colombia (función hepática alterada, adultos mayores)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

