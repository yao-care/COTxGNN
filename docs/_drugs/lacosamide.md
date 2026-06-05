---
layout: default
title: Lacosamide
parent: 僅模型預測 (L5)
nav_order: 144
evidence_level: L5
indication_count: 10
---

# Lacosamide
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

# Lacosamide: De Epilepsia Focal a Trastorno Afectivo Bipolar Maníaco

## Resumen en Una Frase

Lacosamide es un antiepiléptico de tercera generación (comercializado internacionalmente como Vimpat®), utilizado como tratamiento de crisis epilépticas focales en adultos. El modelo TxGNN predice que podría ser efectivo para el **Trastorno Afectivo Bipolar Maníaco**, con **1 ensayo clínico** y **14 publicaciones** que actualmente respaldan esta dirección. La predicción está sustentada por mecanismos compartidos con estabilizadores del estado de ánimo ya aprobados, así como por evidencia preliminar de estudios piloto realizados directamente en pacientes con trastorno bipolar sin epilepsia comórbida.

---

## Resumen Rápido

| Ítem | Contenido |
|------|------|
| Indicación Original | Epilepsia focal (crisis de inicio focal en adultos) |
| Nueva Indicación Predicha | Trastorno Afectivo Bipolar Maníaco |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos formales de mecanismo de acción en el sistema regulatorio colombiano. Sin embargo, según la información disponible internacionalmente, lacosamide actúa principalmente mediante la **inactivación lenta selectiva de los canales de sodio dependientes de voltaje (Nav)**, promoviendo una estabilización prolongada de la membrana neuronal. Este mecanismo es homólogo al de otros antiepilépticos que ya son pilares del tratamiento del trastorno bipolar, particularmente lamotrigina y carbamazepina, lo que provee una base farmacológica traslacional sólida para el reposicionamiento.

Un segundo mecanismo relevante involucra la proteína **CRMP-2** (*Collapsin Response Mediator Protein-2*): lacosamide se une a CRMP-2 e inhibe su fosforilación, modulando la vía de señalización del factor neurotrófico **BDNF**, que participa directamente en la plasticidad sináptica y la regulación del estado de ánimo. Este eje CRMP-2/BDNF representa un sustrato biológico independiente que refuerza la credibilidad de la predicción de TxGNN más allá de la analogía de clase farmacológica.

Epilepsia y trastorno bipolar comparten una fisiopatología de hiperexcitabilidad neuronal, lo que explica históricamente por qué valproato, lamotrigina y carbamazepina son tratamientos de primera línea en el trastorno bipolar. Estudios observacionales han documentado mejorías en síntomas depresivos y ansiosos en pacientes epilépticos tratados con lacosamide (PMID 29253680), y un ensayo piloto prospectivo de 12 semanas demostró eficacia en depresión bipolar en pacientes **sin** epilepsia comórbida (PMID 33666402), confirmando que el efecto sobre el estado de ánimo no es exclusivamente secundario al control de las crisis.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT07412132](https://clinicaltrials.gov/study/NCT07412132) | Fase 3 | Reclutando | 40 | Evalúa lacosamide como augmentación a tratamiento de primera o segunda línea en episodios depresivos mayores del trastorno bipolar tipo I y II (aleatorizado, doble ciego, controlado). Inicio: enero 2026; finalización estimada: enero 2027. ⚠️ El prefijo NCT «07» es inusual (el máximo actual en ClinicalTrials.gov es ~NCT06); se recomienda verificar la validez del registro antes de citarlo formalmente. Muestra de n=40 es pequeña para un estudio Fase 3 convencional. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33666402](https://pubmed.ncbi.nlm.nih.gov/33666402/) | 2021 | Ensayo Piloto Abierto | J Clin Psychopharmacology | Primer ensayo prospectivo de 12 semanas evaluando eficacia y seguridad de lacosamide específicamente en depresión bipolar, en pacientes sin epilepsia comórbida. |
| [30251375](https://pubmed.ncbi.nlm.nih.gov/30251375/) | 2018 | Cohorte Retrospectiva | Psychiatry Clin Neurosci | Comparación a 30 días de lacosamide frente a otros antiepilépticos en pacientes hospitalizados con trastorno bipolar sin epilepsia; primer estudio con grupo de comparación en esta población. |
| [29253680](https://pubmed.ncbi.nlm.nih.gov/29253680/) | 2018 | Estudio Prospectivo Multicéntrico | Epilepsy & Behavior | Lacosamide mejoró síntomas depresivos y ansiosos en epilepsia focal refractaria, tanto por control de crisis como por efecto intrínseco del fármaco, apoyando un efecto directo sobre el estado de ánimo. |
| [28845834](https://pubmed.ncbi.nlm.nih.gov/28845834/) | 2017 | Reporte de Caso | Acta Bio-Medica Atenei Parmensis | Estabilización clínica con lacosamide en trastorno del estado de ánimo comórbido con PTSD y epilepsia frontotemporal; discute la inactivación lenta de Nav como base del efecto estabilizador del ánimo. |
| [30275630](https://pubmed.ncbi.nlm.nih.gov/30275630/) | 2018 | Reporte de Caso (Señal de Seguridad) | Indian J Psychological Medicine | Neutropenia precipitada por lacosamide en paciente con trastorno bipolar y epilepsia comórbida. Señal de seguridad hematológica relevante para el uso psiquiátrico. |
| [38304661](https://pubmed.ncbi.nlm.nih.gov/38304661/) | 2024 | Reporte de Caso | Cureus | Manejo de trastorno bipolar I con epilepsia y PNES comórbidas durante el embarazo; lacosamide formó parte del régimen evaluado, aportando perspectiva de uso en poblaciones especiales. |
| [40777679](https://pubmed.ncbi.nlm.nih.gov/40777679/) | 2025 | Reporte de Caso | Cureus | Paciente con trastorno bipolar y síndrome de abstinencia de xilazina/fentanilo tratado con lacosamide; ilustra el uso en contextos de comorbilidad psiquiátrica compleja con disregulación autonómica. |
| [32693579](https://pubmed.ncbi.nlm.nih.gov/32693579/) | 2020 | Revisión Mecanística | ACS Chemical Neuroscience | Revisión sobre la drogabilidad de CRMP-2; describe cómo lacosamide, al unirse a CRMP-2, regula el tráfico de canales iónicos y la señalización BDNF, sustentando el mecanismo de acción en trastornos del ánimo. |
| [29957667](https://pubmed.ncbi.nlm.nih.gov/29957667/) | 2018 | Revisión TDM | Therapeutic Drug Monitoring | Actualización 2018 sobre monitoreo terapéutico de antiepilépticos; reconoce el uso emergente de lacosamide en dolor y trastorno bipolar como indicaciones off-label con base clínica. |
| [40072331](https://pubmed.ncbi.nlm.nih.gov/40072331/) | 2025 | Análisis Retrospectivo de Base de Datos | Epilepsia | Análisis de vida real sobre rangos de concentración plasmática de lacosamide y otros anticonvulsivos; referencia de utilidad para establecer rangos de monitoreo terapéutico en uso psiquiátrico. |

---

## Consideraciones de Seguridad

Consultar el prospecto (FDA/EMA) para información completa de advertencias, contraindicaciones e interacciones farmacológicas.

> **Señal de seguridad identificada en evidencia revisada:** PMID 30275630 reporta un caso de **neutropenia** precipitada por lacosamide en un paciente con trastorno bipolar y epilepsia comórbida. Se recomienda incluir monitoreo hematológico de rutina (hemograma completo) en cualquier protocolo de uso psiquiátrico de lacosamide.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La predicción TxGNN está respaldada por una base mecanística farmacológicamente sólida (inactivación lenta de Nav y modulación del eje CRMP-2/BDNF), evidencia piloto prospectiva en depresión bipolar, y un ensayo de Fase 3 actualmente en reclutamiento. Sin embargo, la ausencia de comercialización en Colombia, la falta de datos de seguridad formales disponibles localmente, y la pendiente confirmación del ensayo NCT07412132 obligan a avanzar con cautela y bajo monitoreo estricto.

**Para avanzar se necesita:**
- Verificar la validez del registro NCT07412132 directamente en ClinicalTrials.gov (prefijo «07» inusual) y confirmar su elegibilidad como evidencia de Fase 3
- Obtener el prospecto completo de FDA o EMA para caracterizar el perfil de advertencias, contraindicaciones e interacciones farmacológicas
- Completar el perfil de MOA mediante consulta a DrugBank API (DB06218)
- Establecer plan de monitoreo hematológico ante la señal de neutropenia identificada (PMID 30275630)
- Evaluar la vía regulatoria para importación o registro ante INVIMA dado que lacosamide no está actualmente comercializado en Colombia
- Monitorear los resultados del ensayo de Fase 3 NCT07412132 (finalización estimada: enero 2027)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

