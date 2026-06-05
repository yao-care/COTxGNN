---
layout: default
title: Olaparib
parent: 僅模型預測 (L5)
nav_order: 182
evidence_level: L5
indication_count: 1
---

# Olaparib
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

# OLAPARIB: De Cáncer de Ovario a Carcinoma de Mama Femenino

## Resumen en Una Frase

Olaparib es un inhibidor de PARP (poli ADP-ribosa polimerasa) aprobado internacionalmente para el tratamiento de cáncer de ovario con mutación germinal BRCA1/2, actuando mediante el mecanismo de letalidad sintética para destruir células tumorales con deficiencia en reparación del ADN. El modelo TxGNN predice que podría ser efectivo para el **Carcinoma de Mama Femenino**, con múltiples ensayos clínicos de Fase III completados —incluyendo los estudios OlympiAD y OlympiA— y más de 20 publicaciones que respaldan esta dirección. El nivel de evidencia alcanza L1, el más alto posible, respaldado por aprobaciones de FDA y EMA para esta indicación en pacientes con mutación germinal BRCA1/2 HER2-negativas, aunque Colombia aún no cuenta con registro INVIMA disponible.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer de ovario con mutación BRCA1/2 (aprobación internacional) |
| Nueva Indicación Predicha | Carcinoma de Mama Femenino |
| Puntaje de Predicción TxGNN | 99.09% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | ✗ No Comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## Por qué es Razonable esta Predicción?

Olaparib actúa como inhibidor de PARP (poli ADP-ribosa polimerasa), enzima esencial en la reparación de roturas de cadena simple del ADN. Su mecanismo de acción se fundamenta en el concepto de **letalidad sintética**: los genes BRCA1/2 son responsables de la reparación por recombinación homóloga (HRR); cuando una célula tumoral porta mutaciones germinales en BRCA1/2, su capacidad de reparar roturas de doble cadena queda comprometida. Al bloquear simultáneamente la reparación mediada por PARP, se acumula daño de ADN irreparable que desencadena la apoptosis selectiva de las células cancerosas, con relativo respeto por las células normales.

La relación biológica entre cáncer de ovario y carcinoma de mama es sólida y bien establecida: ambos tumores comparten la misma vía de vulnerabilidad genética (mutaciones BRCA1/2), el mismo sustrato molecular (deficiencia en recombinación homóloga, HRD) y la misma sensibilidad a la inhibición de PARP. Las mutaciones germinales en BRCA1/2 elevan significativamente el riesgo de ambas neoplasias, lo que convierte a cáncer de ovario y de mama en candidatos naturales para la misma clase farmacológica. Esta superposición mecanística justifica plenamente la predicción del modelo TxGNN.

La evidencia clínica confirma esta predicción con el máximo nivel de evidencia disponible: los estudios OlympiAD (Fase III, cáncer de mama metastásico HER2-negativo con mutación gBRCA) y OlympiA (Fase III, cáncer de mama temprano de alto riesgo con mutación gBRCA1/2) demostraron beneficios estadísticamente significativos en supervivencia libre de progresión y supervivencia global. Ambas indicaciones cuentan con aprobación de FDA y EMA; la ausencia de registro en Colombia representa una brecha regulatoria, no una brecha científica.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02282020](https://clinicaltrials.gov/study/NCT02282020) | Fase 3 | Completado | 266 | OlympiAD: olaparib monoterapia vs quimioterapia de elección del médico en cáncer de mama metastásico HER2-negativo con mutación germinal BRCA1/2; ensayo pivotal que sustenta la aprobación FDA/EMA |
| [NCT00679783](https://clinicaltrials.gov/study/NCT00679783) | Fase 2 | Completado | 99 | Prueba de concepto de olaparib en cáncer de mama/ovario BRCA-mutado y TNBC; establece la base científica para el diseño de los ensayos de Fase III posteriores |
| [NCT03402841](https://clinicaltrials.gov/study/NCT03402841) | Fase 3 | Completado | 279 | Olaparib como mantenimiento en cáncer de ovario seroso de alto grado no-gBRCAm tras quimioterapia con platino; datos complementarios de eficacia y seguridad de la clase inhibidores PARP |
| [NCT05498155](https://clinicaltrials.gov/study/NCT05498155) | Fase 2 | Activo no reclutando | 50 | Olaparib monoterapia vs olaparib + durvalumab en neoadyuvancia para cáncer de mama HER2-negativo con mutación BRCA en estadio temprano |
| [NCT02418624](https://clinicaltrials.gov/study/NCT02418624) | Fase 1 | Completado | 25 | Carboplatino + olaparib seguido de olaparib monoterapia vs capecitabina en cáncer de mama avanzado BRCA-mutado HER2-negativo de primera línea; establece dosis y seguridad del esquema combinado |
| [NCT04421963](https://clinicaltrials.gov/study/NCT04421963) | Fase 3 | Activo no reclutando | 185 | Estudio de extensión (rollover) para pacientes que continúan beneficiándose de olaparib tras concluir el estudio parental; aporta datos de seguridad a largo plazo |
| [NCT04330040](https://clinicaltrials.gov/study/NCT04330040) | Fase 4 | Completado | 202 | Olaparib en pacientes indios con cáncer de ovario platino-sensible y cáncer de mama metastásico gBRCA-mutado; datos de efectividad y seguridad en población no occidental |
| [NCT05564377](https://clinicaltrials.gov/study/NCT05564377) | Fase 2 | Reclutando | 2900 | ComboMATCH: ensayo canasta de gran escala dirigido por genómica con múltiples brazos que incluyen olaparib en tumores sólidos avanzados, incluyendo cáncer de mama |
| [NCT02503436](https://clinicaltrials.gov/study/NCT02503436) | N/A | Completado | 276 | C-PATROL: estudio no intervencional de vida real en cáncer de ovario/mama BRCA-mutado tratado con olaparib en Alemania; efectividad y patrones de uso en práctica clínica real |
| [NCT01116648](https://clinicaltrials.gov/study/NCT01116648) | Fase 1/2 | Activo no reclutando | 155 | Cediranib + olaparib vs olaparib monoterapia en cáncer de ovario recurrente y cáncer de mama triple negativo recurrente; evalúa combinación antiangiogénica + PARP |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [28578601](https://pubmed.ncbi.nlm.nih.gov/28578601/) | 2017 | ECA Fase III | NEJM | OlympiAD: olaparib prolongó significativamente la SLP (7.0 vs 4.2 meses) vs quimioterapia en cáncer de mama metastásico gBRCA-mutado HER2-negativo; ensayo pivotal de aprobación |
| [30689707](https://pubmed.ncbi.nlm.nih.gov/30689707/) | 2019 | ECA Fase III (SG final) | Annals of Oncology | OlympiAD resultados finales de SG: mediana SG 19.3 meses (olaparib) vs 17.1 meses (quimioterapia); beneficio en SLP confirmado con perfil de tolerabilidad favorable |
| [36893711](https://pubmed.ncbi.nlm.nih.gov/36893711/) | 2023 | ECA Fase III (seguimiento extendido) | European Journal of Cancer | OlympiAD seguimiento extendido (25.7 meses adicionales): datos actualizados de SG y tolerabilidad a largo plazo en cáncer de mama metastásico gBRCA-mutado |
| [34081848](https://pubmed.ncbi.nlm.nih.gov/34081848/) | 2021 | ECA Fase III | NEJM | OlympiA: olaparib adyuvante vs placebo en cáncer de mama temprano de alto riesgo con mutación germinal BRCA1/2; mejora significativa en supervivencia libre de enfermedad invasiva (IDFS) |
| [36228963](https://pubmed.ncbi.nlm.nih.gov/36228963/) | 2022 | ECA Fase III (SG) | Annals of Oncology | OlympiA análisis de SG: confirmación del beneficio en supervivencia global en cáncer de mama temprano de alto riesgo gBRCA-mutado en la primera evaluación provisional pre-especificada |
| [33119476](https://pubmed.ncbi.nlm.nih.gov/33119476/) | 2020 | ECA Fase II | J Clin Oncology | TBCRC 048: olaparib en cáncer de mama metastásico con mutaciones somáticas BRCA1/2 o mutaciones en otros genes de HR distintos de BRCA1/2; amplía el perfil de candidatos al tratamiento |
| [34143979](https://pubmed.ncbi.nlm.nih.gov/34143979/) | 2021 | Fase II (aleatorizado adaptativo) | Cancer Cell | I-SPY2: durvalumab + olaparib + paclitaxel aumentó la tasa de respuesta completa patológica (pCR) del 20% al 37% en cáncer de mama HER2-negativo estadio II/III; beneficio en TNBC y HR+/HER2- |
| [33710534](https://pubmed.ncbi.nlm.nih.gov/33710534/) | 2021 | Revisión | Targeted Oncology | Revisión actualizada de inhibidores de PARP (olaparib, talazoparib) aprobados para cáncer de mama; sintetiza evidencia de Fase III y criterios de selección de pacientes |
| [38112922](https://pubmed.ncbi.nlm.nih.gov/38112922/) | 2024 | Estudio de vida real (Fase IIIb) | Breast Cancer Research & Treatment | LUCY (análisis final): SLP mediana 8.11 meses en cáncer de mama metastásico gBRCA-mutado en práctica clínica real; resultados comparables al ensayo OlympiAD, confirma efectividad en vida real |
| [39520738](https://pubmed.ncbi.nlm.nih.gov/39520738/) | 2024 | Fase 2 | Breast (Edinburgh) | NOBROLA: olaparib monoterapia en TNBC avanzado con HRD sin mutaciones germinales BRCA1/2; explora la expansión de la indicación más allá de portadores gBRCA clásicos |

---

## Información de Mercado en Colombia

Olaparib actualmente **no cuenta con ningún registro INVIMA** y no se encuentra comercializado en Colombia (0 registros sanitarios vigentes). Para acceso a este medicamento en el país, se requeriría tramitar importación bajo régimen especial ante el INVIMA o iniciar un proceso formal de registro sanitario, dado que el producto cuenta con aprobaciones internacionales consolidadas (FDA, EMA) que pueden facilitar el proceso regulatorio local.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida — Inhibidor de PARP (no citotóxico convencional; mecanismo de letalidad sintética selectivo para células BRCA-deficientes) |
| Riesgo de Mielosupresión | Moderado (anemia, neutropenia y trombocitopenia reportadas con frecuencia en ensayos clínicos; anemia es el evento hematológico más común) |
| Clasificación de Emetogenicidad | Baja a moderada |
| Items de Monitoreo | Hemograma completo con diferencial antes de iniciar y mensualmente durante el tratamiento; función renal y hepática periódica; niveles de folato sérico (riesgo de deficiencia reportado) |
| Protección en Manejo | Seguir normativas de manejo de fármacos antineoplásicos orales; no triturar ni abrir las tabletas/cápsulas; uso de equipo de protección personal durante dispensación |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Olaparib cuenta con evidencia de Nivel L1 para carcinoma de mama femenino BRCA1/2-mutado HER2-negativo, sustentada en múltiples ensayos de Fase III completados (OlympiAD para enfermedad metastásica, OlympiA para estadio temprano de alto riesgo) con aprobaciones regulatorias vigentes de FDA y EMA; la predicción TxGNN del 99.09% es consistente con la solidez mecanística y clínica disponible, aunque su introducción en Colombia requiere resolver barreras regulatorias y de acceso.

**Para avanzar se necesita:**
- Inicio del proceso de registro INVIMA en Colombia (actualmente sin comercialización local; las aprobaciones FDA/EMA pueden agilizar el trámite)
- Asegurar disponibilidad de prueba genómica germinal BRCA1/2 validada para la selección de pacientes candidatas
- Definición de plan de manejo de toxicidades hematológicas (anemia, neutropenia) y estrategia de monitoreo periódico
- Evaluación de cobertura por el sistema de salud colombiano (SGSSS/EPS) para terapias de precisión oncológica
- Revisión del prospecto oficial (FDA/EMA) para completar datos de advertencias, contraindicaciones e interacciones farmacológicas (actualmente no disponibles en el Evidence Pack local)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

