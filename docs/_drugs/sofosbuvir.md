---
layout: default
title: Sofosbuvir
parent: 僅模型預測 (L5)
nav_order: 214
evidence_level: L5
indication_count: 8
---

# Sofosbuvir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# SOFOSBUVIR: De Hepatitis C a Infección por Virus de la Hepatitis B

## Resumen en Una Frase

Sofosbuvir es un prodrug análogo nucleotídico aprobado globalmente como pilar del tratamiento de la infección crónica por el virus de la hepatitis C (VHC), donde actúa como inhibidor de la ARN polimerasa NS5B viral.
El modelo TxGNN predice que podría ser efectivo para la **Infección por Virus de la Hepatitis B (VHB)**,
con **3 ensayos clínicos completados con relevancia directa al VHB** y **19 publicaciones** que actualmente respaldan esta dirección de investigación.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección crónica por Virus de la Hepatitis C (VHC) — no registrado en Colombia |
| Nueva Indicación Predicha | Infección por Virus de la Hepatitis B |
| Puntaje de Predicción TxGNN | 99.77% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el sistema (brecha DG002). Con base en la información conocida, sofosbuvir es un prodrug análogo nucleotídico cuyo metabolito activo, GS-461203 trifosfato, actúa como terminador de cadena al incorporarse a la ARN naciente durante la replicación viral, bloqueando la RdRp NS5B del VHC. La ADN polimerasa/transcriptasa reversa del VHB comparte similitud estructural parcial con las RdRp de virus ARN en ciertos dominios catalíticos del sitio activo, lo que sustenta la hipótesis de una actividad cruzada.

La relación entre la indicación original (VHC) y la nueva indicación predicha (VHB) es biológicamente coherente: ambas son infecciones hepáticas virales crónicas que dependen de polimerasas virales para su replicación, y comparten el órgano diana (hepatocito). Datos observacionales en pacientes con coinfección VHC/VHB tratados con ledipasvir/sofosbuvir han documentado reducciones cuantitativas del HBsAg, y el estudio de Fase 2 (PMID 36045503; NCT03312023) en pacientes VHB monoinfectados confirmó un descenso mensurable del HBsAg y el ADN del VHB tras 12 semanas de tratamiento.

Sin embargo, existe una incertidumbre mecanística clave: aún no se ha determinado si el efecto anti-VHB observado es atribuible principalmente a sofosbuvir, a ledipasvir (cuya estructura de inhibidor NS5A podría interferir con el ensamblaje de la cápside del VHB), o a la combinación. Adicionalmente, el riesgo de reactivación del VHB durante la eliminación del VHC con DAAs constituye una dimensión clínica de seguridad que refuerza la pertinencia del monitoreo sistemático en esta indicación.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02613871](https://clinicaltrials.gov/study/NCT02613871) | Fase 3b | Completado | 111 | LDV/SOF 12 semanas en adultos con VHC genotipo 1/2 y coinfección VHB en Taiwan. Evalúa eficacia antiviral, seguridad y tolerabilidad; el mayor ensayo directo en coinfectados VHC/VHB |
| [NCT03312023](https://clinicaltrials.gov/study/NCT03312023) | Fase 2 | Completado | 21 | Estudio abierto de LDV/SOF 12 semanas específicamente en pacientes con infección por VHB. Evalúa reducción de HBsAg y ADN del VHB como objetivos primario y secundario (correlato de PMID 36045503) |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Fase 2/3 | Completado | 23 | DAA para coinfección crónica VHC/VHB. Determina incidencia, morbilidad y factores predisponentes de reactivación del VHB durante tratamiento anti-VHC directo |
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Fase 4 | Desconocido | 120 | SOF/VEL 12 semanas combinado con TAF profiláctico en coinfectados VHC/VHB (China), con/sin cirrosis compensada. Evalúa seguridad de la estrategia combinada anti-VHB durante clearance VHC |
| [NCT01805882](https://clinicaltrials.gov/study/NCT01805882) | Fase 2 | Completado | 229 | Múltiples combinaciones anti-VHC (GS-7977 con GS-5885, GS-9669 o GS-9451). Subpoblación con coinfección VHB; proporciona datos de seguridad indirecta en contexto hepático mixto |
| [NCT02219685](https://clinicaltrials.gov/study/NCT02219685) | Fase 2 | Completado | 40 | Doble ciego, placebo-controlado, LDV/SOF en VHC crónico. Evalúa metabolismo cerebral y neurocognición post-SVR; incluye evaluación de coinfección VHB subyacente |
| [NCT02597166](https://clinicaltrials.gov/study/NCT02597166) | Fase 3 | Completado | 14 | Efectos de terapia antiviral sobre estado clínico, calidad de vida y supervivencia en cirrosis descompensada por VHC genotipo 1; relevante para el contexto hepatológico avanzado en VHB |
| [NCT02768961](https://clinicaltrials.gov/study/NCT02768961) | Fase 4 | Completado | 64 | Cribado sistemático de VHC, VHB y VIH en instituciones penitenciarias de Cantabria; evalúa efectividad del régimen sin interferón y perfil de coinfección tripartita |
| [NCT03086044](https://clinicaltrials.gov/study/NCT03086044) | Fase 4 | Desconocido | 148 | Trasplante de corazón, pulmón o riñón de donantes VHC+ a receptores VHC negativos; incluye manejo de reactivación VHB en contexto inmunosupresor post-trasplante |
| [NCT02640157](https://clinicaltrials.gov/study/NCT02640157) | Fase 3 | Completado | 506 | ENDURANCE-3: glecaprevir/pibrentasvir vs. SOF+daclatasvir en VHC genotipo 3; referencia comparativa de seguridad para regímenes con sofosbuvir en pacientes con hepatopatía crónica |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36045503](https://pubmed.ncbi.nlm.nih.gov/36045503/) | 2023 | ECA Fase 2 Abierto | J Med Virology | LDV/SOF 12 semanas en VHB monoinfectados: reducción modesta del HBsAg cuantitativo y del ADN VHB. Prueba de concepto más directa disponible para sofosbuvir en VHB |
| [31722032](https://pubmed.ncbi.nlm.nih.gov/31722032/) | 2020 | Cohorte | Trans R Soc Trop Med Hyg | SOF/daclatasvir en pacientes VHC/VHB coinfectados en Egipto: alta tasa de SVR en VHC con perfil de seguridad favorable y manejo del VHB coinfectante documentado |
| [33031326](https://pubmed.ncbi.nlm.nih.gov/33031326/) | 2020 | Serie de casos | Medicine | Reactivación del VHB tras tratamiento exitoso del VHC con SOF+ribavirina: caso raro con revisión de literatura; alerta de seguridad clave para la monitorización |
| [29334502](https://pubmed.ncbi.nlm.nih.gov/29334502/) | 2018 | Observacional | J Clin Gastroenterology | Riesgo de reactivación del VHB en pacientes tratados con LDV-SOF para VHC; examina incidencia y desenlaces clínicos en infectados activos y expuestos previamente |
| [31632097](https://pubmed.ncbi.nlm.nih.gov/31632097/) | 2019 | Observacional | Infect Drug Resist | Manejo de reactivación del VHB post-DAA en coinfección VHC/VHB con seroconversión HBeAg previa; evalúa rol de la terapia antiviral específica contra VHB |
| [31542053](https://pubmed.ncbi.nlm.nih.gov/31542053/) | 2019 | Reporte de caso | J Med Case Reports | Reactivación VHB sostenida por variante inmune-escape durante tratamiento SOF/VEL para VHC; primero en abordar el papel de las mutaciones de escape en este contexto |
| [33523503](https://pubmed.ncbi.nlm.nih.gov/33523503/) | 2021 | Cohorte prospectiva | J Viral Hepatitis | Reactivación VHB en pacientes con cáncer en tratamiento con DAA para VHC coinfectado; primer estudio prospectivo en esta población de riesgo especial |
| [27621502](https://pubmed.ncbi.nlm.nih.gov/27621502/) | 2015 | Reporte de farmacovigilancia | Hospital Pharmacy | Notificación de reactivación VHB con simeprevir y sofosbuvir como reacción adversa reportada al programa MED WATCH de la FDA |
| [40242313](https://pubmed.ncbi.nlm.nih.gov/40242313/) | 2025 | In vitro | JHEP Reports | Sistema in vitro novedoso de coinfección simultánea VHB/VHC/VHD/VHE: herramienta para evaluar reactividad cruzada y sinergia de antivirales como sofosbuvir en infecciones múltiples |
| [37517414](https://pubmed.ncbi.nlm.nih.gov/37517414/) | 2023 | Estudio de modelización | Lancet Gastroenterol Hepatol | Prevalencia global, cascada de atención y cobertura profiláctica del VHB en 2022; contextualiza la magnitud de la necesidad médica insatisfecha para nuevas terapias anti-VHB |

---

## Información de Mercado en Colombia

Sofosbuvir **no cuenta con registros sanitarios activos en Colombia** según los datos consultados (corte: 2026-06-06). No se identificaron licencias, formas farmacéuticas ni indicaciones aprobadas por el INVIMA para este principio activo.

A nivel internacional, sofosbuvir está comercializado bajo las marcas Sovaldi® (monoterapia), Harvoni® (sofosbuvir/ledipasvir), Epclusa® (sofosbuvir/velpatasvir) y Vosevi® (sofosbuvir/velpatasvir/voxilaprevir), todos para tratamiento del VHC. La ausencia de registro en Colombia representa una barrera regulatoria que deberá resolverse antes de cualquier uso clínico.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un ensayo de Fase 3b completado (NCT02613871, n=111) y un estudio piloto de Fase 2 específicamente en VHB (NCT03312023, PMID 36045503) que demuestran reducción cuantificable del HBsAg y ADN del VHB con la combinación ledipasvir/sofosbuvir, respaldados por un mecanismo biológico plausible. Sin embargo, la contribución específica de sofosbuvir frente a ledipasvir al efecto anti-VHB no está dilucidada, y sofosbuvir no está registrado en Colombia, lo que limita la viabilidad operativa inmediata.

**Para avanzar se necesita:**
- Diseñar un ensayo de Fase 2 con sofosbuvir en monoterapia frente a VHB, para aislar la contribución del principio activo en estudio
- Obtener datos de mecanismo de acción (MOA) completos frente a la ADN polimerasa/RT del VHB (gestión de brecha DG002)
- Explorar la vía regulatoria de Colombia (INVIMA) para el registro de sofosbuvir en indicación VHC/VHB, incluyendo la posibilidad de uso bajo programas de acceso temprano
- Establecer protocolo de monitorización de seguridad específico para reactivación del VHB en pacientes coinfectados y trasplantados
- Evaluar si la protección bajo el esquema de medicamento huérfano es aplicable dado el perfil de la indicación
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

