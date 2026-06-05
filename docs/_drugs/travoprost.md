---
layout: default
title: Travoprost
parent: 僅模型預測 (L5)
nav_order: 229
evidence_level: L5
indication_count: 10
---

# Travoprost
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

# Travoprost: De Glaucoma de Ángulo Abierto a Calcifilaxi Visceral

## Resumen en Una Frase

Travoprost es un análogo sintético de prostaglandina F2α que actúa como agonista del receptor FP, utilizado internacionalmente para reducir la presión intraocular en el glaucoma de ángulo abierto y la hipertensión ocular. El modelo TxGNN predice que podría ser efectivo para la **calcifilaxi visceral**, una enfermedad vascular rara y grave caracterizada por calcificación de la capa media vascular y trombosis oclusiva. Actualmente **no existen ensayos clínicos ni publicaciones científicas** que respalden directamente esta indicación predicha.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Glaucoma de ángulo abierto / Hipertensión ocular (indicación establecida internacionalmente; sin registro en Colombia) |
| Nueva Indicación Predicha | Calcifilaxi visceral (Visceral calciphylaxis) |
| Puntaje de Predicción TxGNN | 99.9998% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en esta indicación específica. Según la información farmacológica conocida, Travoprost es un agonista selectivo del receptor FP (receptor de prostaglandina F2α) que reduce la presión intraocular principalmente aumentando el drenaje uveoescleral del humor acuoso. Estudios clínicos oftálmicos han documentado directamente su capacidad de inducir vasodilatación retiniana y aumentar el flujo sanguíneo coroideo (NCT00308945), lo que confirma una actividad vascular real, aunque restringida al contexto ocular.

La calcifilaxi visceral es una enfermedad rara y potencialmente mortal que involucra calcificación de la capa media de vasos de pequeño y mediano calibre, asociada a trombosis microvascular e isquemia tisular progresiva. Teóricamente, el agonismo del receptor FP podría influir en la señalización de calcio del músculo liso vascular a través de la vía de las prostaglandinas, lo que representaría un nexo mecanístico con la fisiopatología de la calcifilaxi. La vía PGF2α participa en la regulación del tono vascular sistémico, lo que justifica que el modelo TxGNN establezca una conexión de proximidad en el grafo de conocimiento.

Sin embargo, esta conexión es altamente especulativa. El propio análisis del Evidence Pack señala que el alto puntaje de TxGNN probablemente refleja la cercanía de Travoprost a nodos de enfermedades vasculares en el grafo de conocimiento farmacológico, más que una relación farmacológica directa con la calcifilaxi. No existe ningún estudio preclínico ni clínico que valide este vínculo, y los datos de seguridad para administración sistémica de Travoprost son inexistentes.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados con calcifilaxi visceral registrados para Travoprost.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación predicha.

---

## Información de Mercado en Colombia

Travoprost **no cuenta con registros sanitarios activos ante el INVIMA**. El medicamento no se encuentra comercializado en el mercado colombiano a la fecha de este informe (junio 2026). No hay licencias, formas farmacéuticas ni indicaciones aprobadas disponibles para consulta.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. Se advierte que los datos de seguridad disponibles corresponden exclusivamente al uso tópico oftálmico; los perfiles de seguridad para administración sistémica no han sido evaluados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de TxGNN para calcifilaxi visceral es de nivel L5 —solo predicción del modelo, sin ningún respaldo de estudios reales—, combinada con la ausencia total de presencia regulatoria de Travoprost en Colombia, lo que hace inviable el avance en el desarrollo de esta indicación en el contexto colombiano sin pasos previos sustanciales.

**Para avanzar se necesita:**
- Estudios preclínicos que evalúen la actividad del agonismo del receptor FP en modelos de calcificación vascular y trombosis microvascular
- Datos completos del mecanismo de acción (MOA) con evaluación de su aplicabilidad a la patología de calcifilaxi
- Perfil de seguridad sistémica: los datos actuales solo cubren uso oftálmico tópico local y no son extrapolables
- Definición de una ruta de administración viable para alcanzar tejidos viscerales afectados
- Obtención de registro sanitario ante INVIMA como requisito previo a cualquier desarrollo clínico en Colombia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

