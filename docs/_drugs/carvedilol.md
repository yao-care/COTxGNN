---
layout: default
title: Carvedilol
parent: 僅模型預測 (L5)
nav_order: 84
evidence_level: L5
indication_count: 5
---

# Carvedilol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Carvedilol: De Hipertensión y Falla Cardíaca a Hipertensión Renovascular Maligna

## Resumen en Una Frase

Carvedilol es un bloqueador adrenérgico dual α₁/β ampliamente establecido en el manejo de la hipertensión arterial, la insuficiencia cardíaca crónica y la disfunción ventricular izquierda post-infarto de miocardio. El modelo TxGNN predice que podría ser efectivo para la **Hipertensión Renovascular Maligna**, con un puntaje de predicción del **99.55%**. Sin embargo, actualmente **no existen ensayos clínicos ni publicaciones científicas** que respalden específicamente esta nueva indicación, lo que sitúa la evidencia en el nivel más bajo (L5).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en registros locales (fármaco no comercializado en Colombia) |
| Nueva Indicación Predicha | Hipertensión Renovascular Maligna |
| Puntaje de Predicción TxGNN | 99.55% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por Qué es Razonable esta Predicción?

Carvedilol actúa mediante un bloqueo adrenérgico dual: bloquea los receptores α₁ (reduciendo la resistencia vascular periférica) y los receptores β no selectivamente (disminuyendo la frecuencia cardíaca, el gasto cardíaco y la secreción de renina). A diferencia de otros betabloqueadores, Carvedilol también posee propiedades antioxidantes significativas, que le confieren efectos protectores adicionales sobre órganos diana. Esta combinación de acciones farmacológicas justifica en parte la predicción del modelo.

La hipertensión renovascular maligna se origina por una activación severa del eje renina-angiotensina-aldosterona (SRAA) secundaria a hipoperfusión renal, típicamente causada por estenosis de la arteria renal. El bloqueo β de Carvedilol sobre las células yuxtaglomerulares suprime directamente la secreción de renina, mientras que el bloqueo α₁ reduce la carga presorial sistémica. Este mecanismo dual representa una conexión teórica coherente con la fisiopatología de la indicación predicha.

No obstante, existe una limitación clínica relevante que el modelo no pondera directamente: en pacientes con estenosis bilateral de arteria renal o riñón único funcionante, la reducción del gasto cardíaco inducida por el bloqueo β puede comprometer gravemente la perfusión glomerular. Por esta razón, aunque la predicción es mecanísticamente plausible, Carvedilol no sería una opción de primera línea en este contexto, y su uso requeriría selección cuidadosa de pacientes y validación clínica específica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para Carvedilol en Hipertensión Renovascular Maligna.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible específicamente para Carvedilol en Hipertensión Renovascular Maligna.

---

## Información de Mercado en Colombia

Carvedilol no cuenta con registros sanitarios activos en Colombia según la base de datos consultada (INVIMA). No existen licencias registradas ni formas farmacéuticas aprobadas para comercialización local.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción TxGNN presenta un puntaje elevado (99.55%) y una base mecanística plausible (supresión de renina vía bloqueo β y reducción de resistencia vascular vía bloqueo α₁), pero la ausencia total de ensayos clínicos, publicaciones científicas, datos de seguridad locales y registros en Colombia impide avanzar en cualquier etapa de desarrollo. El nivel de evidencia L5 indica que la predicción descansa únicamente en el modelo computacional, sin respaldo clínico o preclínico específico.

**Para avanzar se necesita:**
- Obtener el mecanismo de acción completo (MOA) desde DrugBank API para reforzar el análisis de relación mecanística
- Revisar la ficha técnica oficial (INVIMA / EMA / FDA) para extraer advertencias, contraindicaciones y perfiles de seguridad relevantes
- Realizar una búsqueda bibliográfica ampliada sobre Carvedilol en modelos preclínicos de hipertensión renovascular o estudios de función renal en pacientes hipertensos tratados con carvedilol
- Evaluar estudios observacionales o análisis de subgrupos de ensayos de insuficiencia cardíaca que incluyan pacientes con compromiso renovascular
- Iniciar proceso de registro sanitario ante INVIMA como prerequisito para cualquier planificación de uso clínico local
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

