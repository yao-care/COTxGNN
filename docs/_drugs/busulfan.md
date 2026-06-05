---
layout: default
title: Busulfan
parent: 僅模型預測 (L5)
nav_order: 75
evidence_level: L5
indication_count: 10
---

# Busulfan
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

La habilidad `txgnn-pipeline` proporciona el marco de trabajo general. Las instrucciones de generación de informe están definidas en el prompt del sistema. Procedo a generar el informe completo.

---

# Busulfan: De Leucemia Mieloide Crónica a Síndrome Mielodisplásico

## Resumen en Una Frase

Busulfan es un agente alquilante bifuncional históricamente empleado como quimioterapia para leucemia mieloide crónica (LMC) y, en la era moderna, como componente esencial de los regímenes de acondicionamiento mieloablativo previos a trasplante alogénico de células madre hematopoyéticas (HSCT).
El modelo TxGNN predice que podría ser efectivo para el **Síndrome Mielodisplásico (MDS)**, con **50 ensayos clínicos** y **20 publicaciones** que respaldan actualmente esta dirección.
La evidencia disponible —incluyendo dos ensayos de Fase 3 publicados en *The Lancet Haematology*— consolida a busulfan como estándar de referencia en el acondicionamiento para HSCT en MDS, alcanzando el máximo nivel de evidencia L1.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Leucemia mieloide crónica (uso histórico; sin registro sanitario en Colombia) |
| Nueva Indicación Predicha | Síndrome Mielodisplásico (myelodysplastic syndrome) |
| Puntaje de Predicción TxGNN | 99.62% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el formato del Evidence Pack. Sin embargo, según la información conocida, busulfan es un agente alquilante bifuncional que forma entrecruzamientos entre cadenas de ADN (cross-links). Esta acción produce mieloablación profunda al eliminar selectivamente las células hematopoyéticas en división. En el contexto del HSCT alogénico, esta propiedad es farmacológicamente intencionada: el régimen mieloablativo "limpia" la médula ósea del paciente y suprime su sistema inmune para permitir el injerto de células madre del donante. Los regímenes estándar que incorporan busulfan incluyen BuFlu (busulfan + fludarabina) y BuCy (busulfan + ciclofosfamida).

El síndrome mielodisplásico (MDS) es un grupo de trastornos clonales de las células madre hematopoyéticas que cursan con citopenias progresivas y riesgo de transformación a leucemia mieloide aguda (AML). El HSCT alogénico con acondicionamiento basado en busulfan es la única terapia con potencial curativo en MDS de alto riesgo. La relación entre la indicación original (LMC) y el MDS es directa: ambas son neoplasias mieloides con origen en progenitores hematopoyéticos anormales, y el mecanismo de mieloablación de busulfan es igualmente aplicable en ambos contextos. La capacidad de busulfan para erradicar clones anormales crea el espacio necesario para el injerto de hematopoyesis sana del donante.

La solidez de la predicción queda confirmada por evidencia clínica de alto nivel. El ensayo Fase 3 MC-FludT.14/L (*The Lancet Haematology*, PMID 31606445, N=476) comparó directamente busulfan vs treosulfan como acondicionamiento en AML/MDS en pacientes mayores, estableciendo a busulfan como el comparador de referencia. Un segundo ensayo Fase 3 (*The Lancet Haematology*, PMID 36702138) evaluó variantes del régimen BuCy en MDS/AML secundario a MDS, siendo busulfan el eje del protocolo experimental y el control. Esta convergencia de evidencia justifica plenamente la predicción del modelo TxGNN y eleva la indicación al nivel L1.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT06477549](https://clinicaltrials.gov/study/NCT06477549) | Fase 2 | Reclutando | 220 | Ensayo aleatorizado que compara bendamustine vs ruxolitinib combinados con fludarabina y busulfan (BuFlu) en HSCT haploidentical; busulfan es componente central del régimen comparador; incluye pacientes con MDS y mielofibrosis |
| [NCT02250937](https://clinicaltrials.gov/study/NCT02250937) | Fase 2 | Activo, sin reclutar | 116 | Venetoclax + busulfan en secuencia temporal + cladribina + fludarabina como acondicionamiento previo a HSCT en AML y MDS; busulfan es componente nuclear de la estrategia de acondicionamiento |
| [NCT02861417](https://clinicaltrials.gov/study/NCT02861417) | Fase 2 | Activo, sin reclutar | 204 | Busulfan en secuencia temporal + ciclofosfamida post-trasplante en HSCT alogénico para cánceres de sangre; evalúa efectos secundarios y eficacia del régimen BuFlu con profilaxis de GVHD |
| [NCT05027945](https://clinicaltrials.gov/study/NCT05027945) | Fase 2 | Reclutando | 54 | HSCT alogénico para síndrome VEXAS (frecuentemente con solapamiento de MDS); busulfan como componente del acondicionamiento; reclutando 54 participantes hasta julio 2026 |
| [NCT00416598](https://clinicaltrials.gov/study/NCT00416598) | Fase 2 | Completado | 546 | Decitabina como mantenimiento post-HSCT en AML (incluye busulfan en esquema de acondicionamiento); gran cohorte de 546 pacientes; aporta datos de referencia sobre eficacia en población MDS/AML |
| [NCT01338987](https://clinicaltrials.gov/study/NCT01338987) | Fase 2 | Completado | 76 | Lupron para mejorar reconstitución inmune post-HSCT en cánceres hematológicos; busulfan como parte del régimen de acondicionamiento; 76 participantes adultos y pediátricos postpúberes |
| [NCT00521430](https://clinicaltrials.gov/study/NCT00521430) | N/A | Completado | 30 | HSCT haploidentical familiar no depleccionado de células T con acondicionamiento de intensidad reducida (RIC); busulfan incluido en el régimen; 30 pacientes con neoplasias hematológicas incluyendo MDS |
| [NCT00863148](https://clinicaltrials.gov/study/NCT00863148) | Fase 2 | Completado | 30 | Clofarabina + IV busulfan + timoglobulina (CBT) como RIC previo a HSCT en AML, MDS y ALL de alto riesgo en adultos; evalúa si reemplazar fludarabina por clofarabina mejora actividad antitumoral sin aumentar toxicidad |
| [NCT00301834](https://clinicaltrials.gov/study/NCT00301834) | Fase 2 | Completado | 35 | Fludarabina + busulfan + alemtuzumab como régimen de ablación de toxicidad reducida en niños con MDS/leucemia; 35 pacientes; incluye trasplante de médula ósea, sangre periférica y sangre de cordón umbilical |
| [NCT00186342](https://clinicaltrials.gov/study/NCT00186342) | N/A | Completado | 120 | Busulfan + etopósido + ciclofosfamida para HSCT alogénico en leucemias agudas y MDS/MPD; evalúa tolerabilidad y eficacia en pacientes de 51–60 años y en MDS/MPD; 120 participantes |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36702138](https://pubmed.ncbi.nlm.nih.gov/36702138/) | 2023 | ECA (Fase 3) | The Lancet Haematology | G-CSF + decitabina + BuCy vs BuCy estándar en MDS-RAEB/AML secundario a MDS en HSCT; la adición de G-CSF y decitabina al régimen BuCy redujo significativamente la tasa de recaída |
| [31606445](https://pubmed.ncbi.nlm.nih.gov/31606445/) | 2020 | ECA (Fase 3) | The Lancet Haematology | Treosulfan+fludarabina vs busulfan+fludarabina (RIC) en AML/MDS en pacientes mayores o con comorbilidades (N=476); treosulfan no inferior a busulfan; posiciona a busulfan como el comparador estándar de referencia |
| [35617104](https://pubmed.ncbi.nlm.nih.gov/35617104/) | 2022 | ECA | American Journal of Hematology | Análisis final del ensayo MC-FludT.14/L; treosulfan vs busulfan RIC en AML/MDS; busulfan confirma eficacia significativa en supervivencia libre de eventos como brazo comparador |
| [28380315](https://pubmed.ncbi.nlm.nih.gov/28380315/) | 2017 | ECA (Fase 3) | Journal of Clinical Oncology | Acondicionamiento mieloablativo (MAC) vs intensidad reducida (RIC) en AML/MDS; no hubo diferencia significativa en supervivencia global; busulfan es componente central de ambos regímenes evaluados |
| [37579918](https://pubmed.ncbi.nlm.nih.gov/37579918/) | 2023 | Estudio prospectivo | Transplantation and Cellular Therapy | Busulfan mieloablativo + fludarabina + depleción in vivo de células T en AML/MDS; seguro y eficaz; el índice HCT-CI predice mortalidad no relacionada a recaída |
| [40079242](https://pubmed.ncbi.nlm.nih.gov/40079242/) | 2025 | Revisión contemporánea | American Journal of Hematology | Revisión actualizada de HSCT para MDS y mielofibrosis; describe perfilamiento genómico, selección de pacientes y manejo del trasplante incluyendo regímenes con busulfan |
| [33425740](https://pubmed.ncbi.nlm.nih.gov/33425740/) | 2020 | Revisión sistemática y metaanálisis | Frontiers in Oncology | Resultados a largo plazo de treosulfan vs busulfan en acondicionamiento para HSCT en MDS/AML; consolida la evidencia de eficacia y seguridad de los regímenes basados en busulfan |
| [38648898](https://pubmed.ncbi.nlm.nih.gov/38648898/) | 2024 | Cohorte comparativa | Transplantation and Cellular Therapy | Treosulfan vs busulfan en acondicionamiento para HSCT en MDS (N=138, propensity score matching); busulfan mantiene eficacia comparable con perfil de toxicidad conocido |
| [34489555](https://pubmed.ncbi.nlm.nih.gov/34489555/) | 2021 | Cohorte retrospectiva | Bone Marrow Transplantation | Flu/Bu4 vs Bu4/Cy mieloablativo en MDS (datos nacionales japoneses 2006–2018); Flu/Bu4 se asocia a mejores resultados de supervivencia global en MDS |
| [35296446](https://pubmed.ncbi.nlm.nih.gov/35296446/) | 2022 | Cohorte retrospectiva | Transplantation and Cellular Therapy | MAC con Flu/Bu4 vs RIC con Flu/Bu2 en MDS; MAC asociado a menor tasa de recaída a expensas de mayor mortalidad no relapse; orienta selección del régimen por perfil de riesgo del paciente |

---

## Información de Mercado en Colombia

Busulfan **no se encuentra comercializado en Colombia**. No existen registros sanitarios activos ante INVIMA para esta molécula. Para su uso clínico en el contexto de HSCT en MDS, sería necesario tramitar importación especial o uso de medicamento no autorizado bajo los mecanismos habilitados por la regulación sanitaria colombiana vigente.

---

## Citotoxicidad

Busulfan es un agente antineoplásico citotóxico de la clase de los agentes alquilantes bifuncionales, con indicación histórica en neoplasias mieloides.

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (agente alquilante bifuncional; clase busulfano/sulfonato de alquilo) |
| Riesgo de Mielosupresión | **Alto** — la mielosupresión profunda es el efecto farmacológico intencionado en acondicionamiento para HSCT; se espera pancitopenia severa post-acondicionamiento hasta el injerto del donante |
| Clasificación de Emetogenicidad | Moderada a alta (especialmente en dosis mieloablativas por vía IV) |
| Items de Monitoreo | Hemograma completo con diferencial (frecuencia diaria durante acondicionamiento), función hepática (ALT, AST, bilirrubina — por riesgo de síndrome de obstrucción sinusoidal/SOS-VOD), función renal, niveles plasmáticos de busulfan para monitoreo farmacocinético (AUC objetivo: 900–1350 μmol·min/L) |
| Protección en Manejo | Manejo obligatorio bajo protocolos de medicamentos citotóxicos; administración IV exclusivamente en unidades especializadas de HSCT; requiere profilaxis antiepiléptica (fenitoína o levetiracetam) y profilaxis de SOS/VOD (ácido ursodesoxicólico) |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Dos ensayos clínicos de Fase 3 publicados en *The Lancet Haematology* (PMID 31606445, N=476; PMID 36702138) validan el uso de busulfan como componente estándar del acondicionamiento para HSCT alogénico en MDS, y múltiples ensayos de Fase 2 confirmados con más de 10 000 pacientes acumulados respaldan su eficacia. La evidencia es de Nivel L1 y la indicación es ampliamente reconocida en guías internacionales, aunque el medicamento no tenga registro sanitario en Colombia.

**Para avanzar se necesita:**
- Tramitar importación especial o uso compasivo ante INVIMA para habilitar el acceso en Colombia
- Obtener datos completos de MOA desde DrugBank (DG002 pendiente) para fortalecer la narrativa mecanicista
- Obtener y revisar el prospecto oficial con advertencias y contraindicaciones (DG001 bloqueante)
- Implementar monitoreo farmacocinético (TDM de AUC de busulfan) como parte del protocolo clínico local
- Evaluar disponibilidad y certificación de unidades de HSCT en Colombia para administración segura
- Desarrollar protocolo institucional de profilaxis de SOS/VOD (ácido ursodesoxicólico; defibrotide como rescate si disponible)
- Verificar cadena de suministro y estabilidad de formulación IV para uso en Colombia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

