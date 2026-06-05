---
layout: default
title: Dutasteride
parent: 僅模型預測 (L5)
nav_order: 105
evidence_level: L5
indication_count: 10
---

# Dutasteride
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

# Dutasteride: De Hiperplasia Prostática Benigna a Hipertricosis Universal Congénita tipo Ambras

## Resumen en Una Frase

Dutasteride es un inhibidor dual de la 5α-reductasa (tipos I y II), originalmente utilizado para el tratamiento de la hiperplasia prostática benigna y la alopecia androgénica masculina mediante la reducción de los niveles de dihidrotestosterona (DHT).
El modelo TxGNN predice que podría ser efectivo para la **Hipertricosis Universal Congénita tipo Ambras**,
sin embargo, actualmente **no existen ensayos clínicos ni publicaciones científicas** que respalden esta dirección, y el análisis mecanístico identifica baja plausibilidad biológica para esta asociación.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hiperplasia Prostática Benigna / Alopecia Androgénica |
| Nueva Indicación Predicha | Hipertricosis Universal Congénita tipo Ambras |
| Puntaje de Predicción TxGNN | 99.9979% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Dutasteride actúa inhibiendo de forma dual las isoformas tipo I y tipo II de la enzima 5α-reductasa, responsable de convertir la testosterona en dihidrotestosterona (DHT). Al reducir los niveles de DHT tanto a nivel sistémico como tisular, el fármaco suprime el estímulo androgénico sobre los tejidos diana. Este mecanismo explica su eficacia demostrada en la hiperplasia prostática benigna (reducción del volumen glandular) y en la alopecia androgénica masculina (reversión de la miniaturización folicular inducida por DHT). Los datos detallados de MOA en la base DrugBank no están disponibles en este Evidence Pack (brecha de datos DG002), pero el mecanismo descrito está ampliamente documentado en la literatura farmacológica.

La Hipertricosis Universal Congénita tipo Ambras es una enfermedad genética ultrarara causada por la deleción del locus TRPS1 en el cromosoma 8q24. Su patogenia no involucra la vía androgénica: la hipertricosis generalizada en este síndrome es consecuencia de una alteración del desarrollo folicular de determinación genética, completamente independiente de los niveles circulantes o tisulares de DHT. Por tanto, la reducción de DHT mediada por dutasteride no tiene ningún mecanismo de acción aplicable a esta condición estructural.

El análisis de racionalidad mecanística del Evidence Pack señala explícitamente que el elevado puntaje de TxGNN para esta indicación probablemente se origina en una generalización de los nodos de "biología del cabello" dentro del grafo de conocimiento (conexión indirecta no biológicamente validada), más que en una relación farmacológica real. Este patrón constituye una señal de alerta de falso positivo del modelo predictivo y no debe interpretarse como respaldo clínico.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

Dutasteride no cuenta con registros sanitarios activos en Colombia (INVIMA). El medicamento **no está comercializado** en el país bajo ninguna forma farmacéutica ni para ninguna indicación aprobada a la fecha de corte de este informe (2026-06-04).

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

> **Nota:** Los datos de advertencias clave y contraindicaciones presentan brechas de información (DG001 — Severidad: Bloqueante). Se recomienda obtener el prospecto oficial del fabricante antes de cualquier evaluación de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción TxGNN para Hipertricosis Universal Congénita tipo Ambras carece de plausibilidad mecanística demostrable: el síndrome es de origen genético no androgénico (deleción TRPS1/8q24), y dutasteride actúa exclusivamente sobre la vía de conversión testosterona→DHT. No existe ningún ensayo clínico ni publicación científica que respalde esta indicación, y el propio análisis del Evidence Pack identifica el resultado como probable falso positivo derivado de generalización en el grafo de conocimiento. El nivel de evidencia L5 (solo predicción del modelo) no justifica avanzar en esta dirección.

**Para avanzar se necesita:**

- Resolver la brecha de datos DG001 (advertencias y contraindicaciones del prospecto INVIMA/TFDA) antes de cualquier evaluación de seguridad
- Resolver la brecha de datos DG002 (MOA completo desde DrugBank API)
- Evaluar la indicación de rango 2 —**Hipertricosis general (disease)**— con foco exclusivo en subtipos androgeno-dependientes (PCOS-relacionada, inducida por fármacos), única hipótesis con racionalidad mecanística parcial (estadio S1, Research Question)
- Considerar la alopecia androgénica masculina y femenina como indicación de reposicionamiento prioritaria para Colombia, dado que el mecanismo está establecido y el fármaco no está actualmente comercializado en el país
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

