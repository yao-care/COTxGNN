---
layout: default
title: Treprostinil
parent: 僅模型預測 (L5)
nav_order: 230
evidence_level: L5
indication_count: 10
---

# Treprostinil
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

# Treprostinil: De Hipertensión Arterial Pulmonar a Malformación Arteriovenosa Pulmonar

## Resumen en Una Frase

Treprostinil es un análogo estable de la prostaciclina (PGI₂), aprobado internacionalmente para el tratamiento de la hipertensión arterial pulmonar (HAP) en sus diversas formas, aunque actualmente sin registro sanitario en Colombia. El modelo TxGNN predice que podría ser efectivo para la **Malformación Arteriovenosa Pulmonar (MAVP)**, sin embargo, **no existe ningún ensayo clínico ni publicación** que respalde directamente esta dirección. La preocupación mecanística adicional —vasodilatación de cortocircuitos de baja resistencia con posible agravamiento de la hipoxemia— hace que esta predicción requiera cautela especial antes de cualquier avance.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial pulmonar (aprobación internacional; sin registro en Colombia) |
| Nueva Indicación Predicha | Malformación arteriovenosa pulmonar (MAVP) |
| Puntaje de Predicción TxGNN | 99.70% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Treprostinil es un análogo sintético de la prostaciclina con mayor estabilidad química que el epoprostenol, lo que le permite administrarse por vías subcutánea, intravenosa, inhalada y oral. Su mecanismo central implica la activación de los receptores IP (IP receptor) y DP1, elevando el AMPc intracelular en las células del músculo liso vascular y las plaquetas. Esto produce vasodilatación pulmonar sostenida, inhibición de la agregación plaquetaria y efectos antiproliferativos sobre el remodelado vascular. La literatura incluida en este Evidence Pack (ensayos para HAP asociada a cardiopatía congénita, enfermedad del tejido conectivo e infección por VIH) confirma este perfil farmacológico bien establecido.

La malformación arteriovenosa pulmonar (MAVP) es una anomalía estructural congénita o adquirida en la que arterias y venas pulmonares se comunican directamente, eludiendo la circulación capilar. A diferencia de la HAP —donde la vasodilatación es el objetivo terapéutico central—, en la MAVP no existe hipertensión arterial pulmonar ni disfunción del músculo liso como mecanismo primario. La lesión es esencialmente anatómica: un cortocircuito de baja resistencia.

Aquí reside la preocupación mecanística clave: Treprostinil, al producir vasodilatación pulmonar generalizada, podría aumentar el flujo sanguíneo a través del cortocircuito malformado en lugar de corregirlo, con el riesgo de **agravar la hipoxemia** en lugar de mejorarla. El alto puntaje TxGNN (99.70%) probablemente refleja la proximidad topológica entre los nodos de "prostaciclina" y "vasculatura pulmonar" en el grafo de conocimiento, más que una predicción biológica validada para MAVP específicamente. No existe ningún respaldo clínico ni preclínico que contradiga o confirme esta hipótesis.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

Treprostinil no cuenta con registros sanitarios vigentes ante el INVIMA. No hay productos comercializados en Colombia para este ingrediente farmacéutico activo.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción TxGNN para MAVP carece de todo respaldo empírico (nivel L5) y presenta una preocupación mecanística activa: la vasodilatación pulmonar inducida por Treprostinil podría aumentar el flujo a través del cortocircuito de baja resistencia y empeorar la hipoxemia, lo que invierte la dirección terapéutica esperada.

**Para avanzar se necesita:**
- Estudios preclínicos (modelos animales de MAVP) que evalúen el efecto hemodinámico de agonistas del receptor IP
- Confirmación del mecanismo de acción detallado (MOA) de Treprostinil obtenida de fuentes regulatorias primarias (DrugBank, TFDA)
- Evaluación de seguridad específica para la fisiopatología de MAVP: monitoreo de saturación de oxígeno y parámetros hemodinámicos bajo vasodilatación pulmonar
- **Considerar prioritariamente** las indicaciones con mayor soporte en este mismo Evidence Pack:
  - **Rango 2 — HAP asociada a cardiopatía congénita (CHD-PAH)**: Nivel L2, evidencia directa con Treprostinil subcutáneo/IV, decisión *Proceed with Guardrails*
  - **Rango 3 — HAP asociada a enfermedad del tejido conectivo (CTD-PAH)**: Nivel L2, cohorte clínica directa desde 2004, decisión *Proceed with Guardrails*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

