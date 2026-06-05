---
layout: default
title: Pemetrexed
parent: 僅模型預測 (L5)
nav_order: 194
evidence_level: L5
indication_count: 10
---

# Pemetrexed
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

# PEMETREXED: De Mesotelioma Pleural Maligno a Mesotelioma Peritoneal Maligno

## Resumen en Una Frase

Pemetrexed es un antifolato multidiana reconocido globalmente como tratamiento estándar de primera línea para el mesotelioma pleural maligno en combinación con cisplatino, aunque actualmente no cuenta con registro sanitario en Colombia.
El modelo TxGNN predice que podría ser efectivo para el **Mesotelioma Peritoneal Maligno**,
con **11 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Ítem | Contenido |
|------|------|
| Indicación Original | Mesotelioma pleural maligno (estándar global; sin registro INVIMA en Colombia) |
| Nueva Indicación Predicha | Mesotelioma Peritoneal Maligno |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Pemetrexed es un antifolato de múltiples dianas que inhibe simultáneamente tres enzimas clave en el metabolismo del folato: timidilato sintasa (TS), dihidrofolato reductasa (DHFR) y glicinamida ribonucleótido formiltransferasa (GARFT). Al bloquear estas vías, interrumpe la síntesis de novo de nucleótidos de timidina y purinas, esenciales para la replicación del ADN en células tumorales de alta proliferación.

La relación biológica entre el mesotelioma pleural y el mesotelioma peritoneal maligno (MPeM) es muy estrecha: ambas neoplasias se originan de células mesoteliales con alta expresión de TS como principal dependencia proliferativa, comparten características histológicas y moleculares similares, y han demostrado perfiles de respuesta comparables a los esquemas basados en platino. La vía de administración intraperitoneal (PIPAC/HIPEC) permite además alcanzar concentraciones locales de pemetrexed muy superiores a las obtenidas por vía intravenosa, lo que es especialmente relevante para una neoplasia de diseminación predominantemente intracavitaria.

Varios estudios retrospectivos japoneses y europeos (PMID 28594258, PMID 31287877, PMID 41133016) confirman que el esquema cisplatino + pemetrexed, extrapolado desde el mesotelioma pleural, logra respuestas objetivas documentadas en mesotelioma peritoneal avanzado con perfiles de toxicidad manejables. Adicionalmente, ensayos clínicos de Fase 2 en curso evalúan activamente combinaciones de pemetrexed con inmunoterapia (atezolizumab, sintilimab) y con cirugía citorreductora, lo que refuerza la solidez de la predicción del modelo TxGNN.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT06057935](https://clinicaltrials.gov/study/NCT06057935) | Fase 2 | Reclutando | 64 | ICARuS II: RCT multicéntrico que compara quimioterapia intraperitoneal vs intravenosa tras cirugía citorreductora + HIPEC; evaluación directa del manejo perioperatorio en MPeM |
| [NCT03875144](https://clinicaltrials.gov/study/NCT03875144) | Fase 2 | Suspendido | 66 | MESOTIP: PIPAC + quimioterapia sistémica (cisplatino + pemetrexed) vs quimioterapia sistémica sola como tratamiento de primera línea en MPeM; resultados pendientes de evaluación |
| [NCT05001880](https://clinicaltrials.gov/study/NCT05001880) | Fase 2 | Reclutando | 66 | Carboplatino + pemetrexed + bevacizumab con o sin atezolizumab en mesotelioma peritoneal neoadyuvante o paliativo; evalúa sinergia quimio-inmunoterapia |
| [NCT06543069](https://clinicaltrials.gov/study/NCT06543069) | Fase 2 | Reclutando | 28 | Sintilimab + bevacizumab + pemetrexed + cisplatino en MPeM irresecable; exploración de biomarcadores de eficacia y seguridad |
| [NCT04462809](https://clinicaltrials.gov/study/NCT04462809) | Fase 2 | Desconocido | 40 | Talazoparib como mantenimiento tras quimioterapia de primera línea basada en platino en mesotelioma pleural o peritoneal; pemetrexed como tratamiento de inducción |
| [NCT02535312](https://clinicaltrials.gov/study/NCT02535312) | Fase 1/2 | Activo sin reclutamiento | 30 | TRC102 (metoxiamina) + cisplatino + pemetrexed en tumores sólidos avanzados; Fase 2 específica para pacientes refractarios a pemetrexed + platino |
| [NCT02029690](https://clinicaltrials.gov/study/NCT02029690) | Fase 1 | Terminado | 85 | ADI-PEG 20 + pemetrexed + cisplatino en tumores con dependencia de arginina, incluido mesotelioma peritoneal avanzado (cohorte de escalada de dosis) |
| [NCT00402766](https://clinicaltrials.gov/study/NCT00402766) | Fase 1 | Completado | 19 | Cisplatino + pemetrexed + imatinib en mesotelioma maligno metastásico; determinó dosis máxima tolerada y confirmó viabilidad de la combinación |
| [NCT00061477](https://clinicaltrials.gov/study/NCT00061477) | Fase 2 | Completado | 48 | Pemetrexed (ALIMTA) + gemcitabina como quimioterapia de primera línea en mesotelioma pleural o peritoneal; evaluó seguridad y supervivencia global |
| [NCT03564691](https://clinicaltrials.gov/study/NCT03564691) | Fase 1 | Completado | 470 | MK-4830 solo y en combinación con pembrolizumab en tumores sólidos avanzados; pemetrexed utilizado como quimioterapia de fondo en cohortes seleccionadas |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [28594258](https://pubmed.ncbi.nlm.nih.gov/28594258/) | 2017 | Retrospectivo | Expert Rev Anticancer Ther | Evaluación retrospectiva de la eficacia del esquema pemetrexed + cisplatino de primera línea en MPeM; documenta respuestas objetivas extrapoladas desde el mesotelioma pleural |
| [31287877](https://pubmed.ncbi.nlm.nih.gov/31287877/) | 2019 | Retrospectivo | Jpn J Clin Oncol | Eficacia y seguridad de pemetrexed + cisplatino como primera línea en MPeM avanzado; confirma tasa de respuesta objetiva y perfil de toxicidad manejable |
| [41133016](https://pubmed.ncbi.nlm.nih.gov/41133016/) | 2025 | Retrospectivo | Clin Med Insights Oncol | Comparación directa de pemetrexed-platino vs gemcitabina-platino como primera línea en MPeM; pemetrexed con ventaja en supervivencia global |
| [38806763](https://pubmed.ncbi.nlm.nih.gov/38806763/) | 2024 | Cohorte multicéntrica | Ann Surg Oncol | Análisis de estrategias terapéuticas y resultados en población heterogénea de MPeM; caracteriza opciones sistémicas incluyendo pemetrexed en estadios avanzados |
| [31417959](https://pubmed.ncbi.nlm.nih.gov/31417959/) | 2019 | Cohorte/Prospectivo | Pleura Peritoneum | Quimioterapia bidireccional con pemetrexed permitió conversión a cirugía + HIPEC en MPeM inicialmente irresecable; impacto en resecabilidad |
| [23291819](https://pubmed.ncbi.nlm.nih.gov/23291819/) | 2013 | Reporte de caso | BMJ Case Reports | MPeM con buena respuesta inicial y re-desafío exitoso con cisplatino + pemetrexed en recaída; documenta posibilidad de retratamiento |
| [33743636](https://pubmed.ncbi.nlm.nih.gov/33743636/) | 2021 | Retrospectivo | BMC Cancer | Eficacia de segunda línea y factores pronósticos en MPeM avanzado tras primera línea con cisplatino + pemetrexed; define el papel del tratamiento secuencial |
| [35407498](https://pubmed.ncbi.nlm.nih.gov/35407498/) | 2022 | Revisión | J Clin Med | Revisión actualizada del tratamiento del MPeM; CRS+HIPEC como preferencia en candidatos quirúrgicos, pemetrexed-platino como alternativa sistémica estándar |
| [36765620](https://pubmed.ncbi.nlm.nih.gov/36765620/) | 2023 | Revisión | Cancers | Vía diagnóstica y terapéutica en DMPM; supervivencia óptima con CRS+HIPEC (mediana OS 34-92 meses); pemetrexed en enfermedad sistémica irresecable |
| [34723916](https://pubmed.ncbi.nlm.nih.gov/34723916/) | 2022 | Reporte de caso | J Immunother | MPeM no respondedor a platino tratado con quimio-inmunoterapia combinada tras fracaso de pemetrexed; describe estrategias de rescate en enfermedad resistente |

---

## Citotoxicidad

| Ítem | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional — Antifolato multidiana (clase: inhibidor de TS / DHFR / GARFT) |
| Riesgo de Mielosupresión | Moderado-Alto (neutropenia y trombocitopenia son toxicidades limitantes de dosis; la suplementación obligatoria con ácido fólico 400–1000 µg/día y vitamina B12 1000 µg IM cada 9 semanas reduce significativamente esta toxicidad) |
| Clasificación de Emetogenicidad | Baja a moderada (menor que cisplatino en monoterapia; la combinación pemetrexed + cisplatino eleva el riesgo a moderado-alto) |
| Ítems de Monitoreo | Hemograma completo con diferencial (antes de cada ciclo), creatinina sérica y aclaramiento de creatinina (≥45 mL/min requerido), función hepática (ALT/AST/bilirrubina), niveles séricos de ácido fólico y vitamina B12 previo al inicio del tratamiento |
| Protección en Manejo | Preparación exclusiva en cabina de seguridad biológica de clase II; equipo de protección personal completo (guantes dobles, bata, mascarilla); disposición de residuos según normativa de citotóxicos; notificación de exposición accidental según protocolos institucionales |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Pemetrexed en combinación con cisplatino constituye el esquema sistémico más estudiado en el mesotelioma peritoneal maligno, con múltiples estudios retrospectivos, ensayos de Fase 2 activos y una base mecanística sólida sustentada en la homología biológica entre el mesotelioma pleural y peritoneal. La barrera principal para Colombia es la ausencia total de registro sanitario INVIMA, lo que impide el acceso regulatorio directo y obliga a rutas de importación o uso compasivo.

**Para avanzar se necesita:**
- Gestión de registro sanitario INVIMA en Colombia para pemetrexed (actualmente sin comercialización aprobada)
- Obtención de datos de mecanismo de acción completos (MOA desde DrugBank) para análisis de interacciones farmacológicas
- Revisión de la ficha técnica o prospecto completo para evaluar advertencias, contraindicaciones y perfil de seguridad en población colombiana
- Confirmación de la capacidad institucional local para administración de pemetrexed en combinación con HIPEC/CRS, dado que el beneficio máximo se obtiene en esquemas multimodales
- Evaluación farmacoeconómica para determinar viabilidad de acceso en el contexto del sistema de salud colombiano
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

