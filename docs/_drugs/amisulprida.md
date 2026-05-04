---
layout: default
title: Amisulprida
parent: 僅模型預測 (L5)
nav_order: 31
evidence_level: L5
indication_count: 0
---

# Amisulprida
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Amisulprida: Evaluación de Reposicionamiento — Datos Insuficientes para Predicción

## Resumen en Una Frase

Amisulprida es un fármaco con aprobaciones reconocidas en otros mercados, sin embargo el Evidence Pack actual no contiene indicaciones originales registradas ni indicaciones nuevas predichas por TxGNN. El análisis de reposicionamiento no puede completarse en esta versión debido a brechas críticas de datos en mecanismo de acción, perfil de seguridad e indicaciones base. Se requiere enriquecer el Evidence Pack antes de emitir una recomendación de reposicionamiento.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Sin datos disponibles en este Evidence Pack |
| Nueva Indicación Predicha | Sin predicciones generadas |
| Puntaje de Predicción TxGNN | N/A |
| Nivel de Evidencia | L5 — Solo predicción del modelo, sin estudios reales |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | **Hold** |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción ni sobre las indicaciones originales aprobadas. El campo `original_moa` del Evidence Pack está marcado como dato faltante, y el arreglo `original_indications` se encuentra vacío.

Sin mecanismo de acción definido, no es posible evaluar la plausibilidad biológica de ninguna indicación nueva, ni establecer la relación fisiopatológica entre una indicación original y una candidata de reposicionamiento.

El modelo TxGNN no generó predicciones en esta ejecución (`predicted_indications: []`), lo que puede deberse a la ausencia de nodos bien caracterizados en el grafo de conocimiento para este fármaco. Es necesario verificar si Amisulprida está correctamente indexada en el Knowledge Graph con su DrugBank ID correspondiente antes de repetir la predicción.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados en este Evidence Pack.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible en este Evidence Pack.

---

## Información de Mercado en Colombia

Amisulprida no cuenta con registros sanitarios activos en Colombia según los datos de consulta INVIMA disponibles en este Evidence Pack. La búsqueda realizada el 2026-03-29 retornó 0 resultados.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. Los datos de advertencias clave, contraindicaciones e interacciones farmacológicas no están disponibles en la versión actual del Evidence Pack.

> **Nota:** La consulta DDI (Drug-Drug Interaction) retornó estado `not_found`. Se recomienda verificar fuentes secundarias como DrugBank, Lexicomp o Micromedex antes de cualquier evaluación clínica.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El Evidence Pack de Amisulprida presenta dos brechas bloqueantes — ausencia de mecanismo de acción (severidad: High) y ausencia de datos de seguridad (severidad: Blocking) — que impiden completar la evaluación de reposicionamiento. Adicionalmente, TxGNN no generó predicciones de indicaciones, lo que elimina el objeto central del informe de reposicionamiento.

**Para avanzar se necesita:**

1. **DrugBank ID confirmado** — Obtener el identificador DrugBank de Amisulprida (probablemente DB01244) para indexación correcta en el Knowledge Graph de TxGNN
2. **Mecanismo de acción (MOA)** — Consultar DrugBank API para recuperar datos de MOA; Amisulprida es un antagonista de receptores D2/D3 dopaminérgicos con actividad antipsicótica/antidepresiva reconocida en la literatura farmacológica
3. **Indicaciones originales** — Registrar las indicaciones aprobadas en jurisdicciones de referencia (EMA, FDA, ANMAT) para completar el campo `original_indications`
4. **Datos de seguridad** — Descargar y parsear el prospecto de INVIMA/TFDA para extraer advertencias, contraindicaciones y categorías de riesgo
5. **Re-ejecución de TxGNN** — Una vez completados los datos del nodo farmacológico, repetir la predicción para obtener `predicted_indications` y habilitar el análisis de reposicionamiento completo
6. **Registro sanitario en Colombia** — Evaluar si existe interés comercial en tramitar registro INVIMA dado el estado actual de no comercialización en el país
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

