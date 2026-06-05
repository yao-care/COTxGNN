---
layout: default
title: Selpercatinib
parent: 僅模型預測 (L5)
nav_order: 213
evidence_level: L5
indication_count: 3
---

# Selpercatinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# SELPERCATINIB: De Cáncer con Alteración RET a Hipertensión Pulmonar

## Resumen en Una Frase

Selpercatinib es un inhibidor selectivo de RET kinasa, originalmente utilizado para el tratamiento de tumores con fusiones o mutaciones del gen RET, incluyendo cáncer de pulmón no microcítico (NSCLC) y carcinoma medular de tiroides.
El modelo TxGNN predice que podría ser efectivo para **Hipertensión Pulmonar**, con **0 ensayos clínicos** y **3 publicaciones** que actualmente respaldan esta dirección.
Actualmente no cuenta con registros sanitarios en Colombia, lo que representa una barrera regulatoria adicional para su desarrollo local.

---

## Resumen Rápido

| Ítem | Contenido |
|------|------|
| Indicación Original | Cáncer con alteración RET (NSCLC RET fusión-positivo, carcinoma medular de tiroides) |
| Nueva Indicación Predicha | Hipertensión Pulmonar |
| Puntaje de Predicción TxGNN | 99.18% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, selpercatinib es un inhibidor selectivo de RET (Rearranged during Transfection) kinasa aprobado por la FDA para tumores con alteraciones del gen RET. Las publicaciones identificadas en este paquete confirman su uso en NSCLC RET fusión-positivo y en carcinoma medular de tiroides con mutación RET M918T, lo que respalda su perfil como agente de terapia dirigida oncológica.

La conexión mecanística propuesta con la hipertensión arterial pulmonar (HAP) se basa en la expresión de RET y su correceptor GFRα en células endoteliales vasculares pulmonares y células de músculo liso arterial. La vía de señalización GDNF/RET participa en procesos de remodelado vascular (vascular remodeling), que es precisamente el mecanismo patológico central en la HAP: proliferación anormal del músculo liso de la arteria pulmonar que conduce al aumento progresivo de la resistencia vascular. En teoría, la inhibición de RET podría interferir con esta proliferación patológica.

Sin embargo, esta conexión es una inferencia indirecta derivada de la biología de redes, no de datos experimentales directos. Las 3 publicaciones identificadas no investigan selpercatinib en HAP: corresponden a farmacovigilancia en oncología y reportes de caso. No existe evidencia preclínica ni clínica que evalúe directamente esta hipótesis, por lo que la predicción del modelo TxGNN se sustenta en similitud de redes biológicas.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39372206](https://pubmed.ncbi.nlm.nih.gov/39372206/) | 2024 | Farmacovigilancia | Frontiers in Pharmacology | Comparación del perfil de eventos adversos entre pralsetinib y selpercatinib usando datos del sistema FAERS; no evalúa hipertensión pulmonar como indicación terapéutica |
| [34178121](https://pubmed.ncbi.nlm.nih.gov/34178121/) | 2021 | Cohorte retrospectiva | Therapeutic Advances in Medical Oncology | Eficacia real de selpercatinib en NSCLC RET fusión-positivo tratados en programa de acceso; confirma actividad terapéutica en la indicación oncológica original |
| [41918669](https://pubmed.ncbi.nlm.nih.gov/41918669/) | 2026 | Reporte de caso | Cureus | Carcinoma medular de tiroides metastásico en MEN2B con mutación RET M918T; describe desafíos del manejo a largo plazo con terapia dirigida incluyendo selpercatinib |

> **Nota:** Ninguna de estas publicaciones investiga selpercatinib directamente en hipertensión pulmonar. Su relevancia es contextual: perfilan el fármaco en el entorno de inhibición RET oncológica.

---

## Citotoxicidad

| Ítem | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida — Inhibidor selectivo de RET kinasa (no citotóxico convencional) |
| Riesgo de Mielosupresión | Bajo a moderado (menor que quimioterapia citotóxica; puede presentar linfopenia y neutropenia leve) |
| Clasificación de Emetogenicidad | Baja (agente oral; categoría de bajo potencial emetogénico según guías ASCO/MASCC) |
| Ítems de Monitoreo | Hemograma completo con diferencial, función hepática (ALT/AST/bilirrubina), función renal (creatinina), intervalo QTc en ECG, presión arterial |
| Protección en Manejo | Fármaco oral de terapia dirigida; seguir precauciones estándar para agentes antineoplásicos orales según normativa institucional |

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción del modelo TxGNN se apoya en una conexión mecanística indirecta y teórica (expresión de RET en vasculatura pulmonar), sin respaldo de ensayos clínicos ni de literatura científica específicamente orientada a selpercatinib en hipertensión pulmonar. El nivel de evidencia L4, la ausencia total de registros sanitarios en Colombia y la falta de datos de seguridad formales (MOA, advertencias de prospecto) no justifican avanzar en esta etapa.

**Para avanzar se necesita:**
- Estudios preclínicos que validen el efecto de la inhibición de RET en modelos establecidos de HAP (modelos de monocrotalina o hipoxia crónica en roedores)
- Datos de expresión y actividad de RET en tejido vascular pulmonar humano de pacientes con HAP
- Obtención del mecanismo de acción formal (MOA) y advertencias del prospecto para completar la evaluación de seguridad (gaps DG001 y DG002 pendientes)
- Gestión de registro sanitario en Colombia como requisito previo para cualquier ensayo clínico local
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

