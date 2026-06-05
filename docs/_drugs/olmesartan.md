---
layout: default
title: Olmesartan
parent: 僅模型預測 (L5)
nav_order: 183
evidence_level: L5
indication_count: 10
---

# Olmesartan
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

# Olmesartan: De Hipertensión Arterial a Angina de Prinzmetal

## Resumen en Una Frase

Olmesartan es un bloqueador selectivo del receptor AT1 de angiotensina II (ARB), utilizado como antihipertensivo de primera línea en el contexto global.
El modelo TxGNN predice que podría ser efectivo para la **Angina de Prinzmetal** con un puntaje de 99.84%,
sin embargo, actualmente **no existen ensayos clínicos ni publicaciones** que respalden directamente esta indicación, limitando la evidencia al nivel de predicción computacional pura.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Hipertensión arterial |
| Nueva Indicación Predicha | Angina de Prinzmetal |
| Puntaje de Predicción TxGNN | 99.84% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, Olmesartan es un antagonista selectivo del receptor AT1 de angiotensina II: al bloquear este receptor, previene la vasoconstricción inducida por angiotensina II y la retención de sodio mediada por aldosterona, con el resultado neto de reducción de la resistencia vascular periférica y la presión arterial.

La Angina de Prinzmetal (angina vasoespástica) se caracteriza por espasmos coronarios espontáneos que producen oclusión transitoria de arterias coronarias, habitualmente sin enfermedad aterosclerótica subyacente significativa. Existe una base teórica mínima: el sistema renina-angiotensina participa en la regulación del tono vascular coronario, y el bloqueo del AT1 podría atenuar en alguna medida la vasoconstricción coronaria mediada por angiotensina II.

Sin embargo, la fisiopatología central de la Angina de Prinzmetal involucra espasmos idiopáticos de la musculatura lisa coronaria, cuyo desencadenante principal es independiente del eje renina-angiotensina. El tratamiento de primera línea establecido —bloqueadores de canales de calcio y nitratos— actúa directamente sobre la musculatura vascular coronaria. Los ARBs carecen de evidencia farmacológica directa para la inhibición del espasmo coronario, y la señal del modelo TxGNN probablemente refleja efectos de proximidad en el grafo de conocimiento (KG proximity) más que una relación causal clínicamente demostrable.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

Olmesartan no cuenta con registros sanitarios vigentes en Colombia. El fármaco no se encuentra comercializado en el mercado colombiano a la fecha de corte del presente informe (2026-06-05).

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Aunque el puntaje TxGNN es elevado (99.84%), la señal corresponde únicamente a una predicción computacional sin ningún respaldo en estudios preclínicos ni clínicos para Angina de Prinzmetal; adicionalmente, la fisiopatología de esta condición (espasmo coronario idiopático) no se alinea con el mecanismo principal de los ARBs, y el fármaco carece completamente de presencia regulatoria en Colombia.

**Para avanzar se necesita:**
- Búsqueda dirigida en modelos animales de espasmo coronario para evaluar el efecto de olmesartan sobre la reactividad vascular coronaria (cierre de DG002)
- Revisión sistemática del rol del eje renina-angiotensina en la fisiopatología específica de la Angina de Prinzmetal
- Datos de MOA completos obtenidos vía DrugBank API (pendiente, severidad High, DG002)
- Información de advertencias y contraindicaciones del prospecto oficial (pendiente, severidad Blocking, DG001)
- Evaluación de viabilidad regulatoria en Colombia ante la ausencia total de registros sanitarios
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

