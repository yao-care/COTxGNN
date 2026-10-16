---
layout: default
title: Nandrolone
parent: Evidencia Moderada (L3-L4)
nav_order: 459
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Nandrolone: nueva indicación predicha, Enfermedad fibroquística de la mama (nivel de evidencia L4). Indicación original: NANDROLONA"
---

# Nandrolone
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Nandrolona: De Nandrolona (indicación no detallada en el registro) a Enfermedad Fibroquística de la Mama

## Resumen en Una Frase

Nandrolona es un esteroide anabólico androgénico que contaba con un registro sanitario en Colombia, actualmente cancelado, cuyo texto de indicación solo dice "NANDROLONA".
El modelo TxGNN predice que podría ser efectivo para **enfermedad fibroquística de la mama**, pero la evidencia es muy limitada: **0 ensayos clínicos** y **1 publicación** de 1964 que no se puede verificar con estándares actuales.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | NANDROLONA (el registro no detalla la indicación; en la literatura farmacológica se usa en anemias refractarias, cáncer de mama, angioedema hereditario, retraso del crecimiento y síndrome de Turner) |
| Nueva Indicación Predicha | Enfermedad fibroquística de la mama |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 (0 vigentes, 1 cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos consultada. Según la información farmacológica compilada, la nandrolona actúa como ligando del receptor de andrógenos (AR) y es un andrógeno anabólico con actividad antiestrogénica y antigonadotrópica.

Históricamente, los andrógenos se usaron en enfermedad benigna de la mama porque podrían reducir el estímulo hormonal ovárico e hipofisario sobre el tejido mamario. Esto da un vínculo plausible, pero no verificado. La única referencia clínica es un artículo de 1964 sobre tratamiento médico de displasias mamarias.

Además, el producto está cancelado en el mercado y los efectos androgénicos (virilización, hepatotoxicidad, cambios lipídicos) limitarían su uso en una condición benigna. Las demás predicciones del modelo (displasia mamaria benigna, adenosis, absceso mamario, necrosis grasa, eritroblastosis fetal, enfermedad de la lactancia) tienen evidencia nula o un fundamento mecanístico débil, y varias parecen artefactos del grafo de conocimiento. Entre las candidatas, la **osteodistrofia renal** es biológicamente la más plausible (efecto anabólico sobre hueso y músculo, eritropoyesis), aunque sin evidencia en los datos compilados y con alertas de seguridad en enfermedad renal crónica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [14150264](https://pubmed.ncbi.nlm.nih.gov/14150264/) | 1964 | Revisión / reporte clínico histórico (probablemente no controlado) | Revista de la Asociación Médica Argentina | "Displasias mamarias: tratamiento médico". Sin resumen disponible; el diseño y los resultados no pueden verificarse |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19912744 (cancelado) | DECA - DURABOLIN® 50 MG | Solución inyectable | NANDROLONA |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** enfermedad hepática, colestasis, enfermedad de la vesícula biliar, síndrome nefrótico, insuficiencia renal/uremia, diabetes mellitus y cetoacidosis diabética, hiperplasia prostática benigna, cáncer de próstata, enfermedad cardiovascular y coronaria, infarto de miocardio, hipercalcemia (incluida la hipercalcemia humoral de malignidad), nefrocalcinosis, trastornos del metabolismo del fósforo y hemoglobinopatías.
- **Interacciones farmacológicas:** la única interacción registrada es farmacológica, con el receptor de andrógenos (AR), su blanco principal. No se identificaron interacciones con otros fármacos.
- **Riesgos esperados por la clase:** virilización, hepatotoxicidad y alteraciones lipídicas. En embarazo, la exposición a andrógenos implica riesgo de virilización fetal, y en lactancia hay exposición del lactante.

No se dispone de advertencias ni contraindicaciones del prospecto de INVIMA; consultar el prospecto para información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto en TxGNN, pero la evidencia se limita a un artículo histórico de 1964 sin verificación posible (L4). El producto está cancelado en Colombia y el perfil de seguridad androgénico es desfavorable para una enfermedad benigna. La osteodistrofia renal podría plantearse como pregunta de investigación separada.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA para obtener advertencias y contraindicaciones oficiales (brecha bloqueante para el tamizaje de seguridad).
- Completar los datos del mecanismo de acción desde DrugBank.
- Búsqueda sistemática de literatura moderna (ensayos controlados, revisiones) sobre andrógenos en enfermedad benigna de la mama.
- Evaluar la relación beneficio-riesgo frente a las alternativas actuales y la viabilidad regulatoria, dado que el registro está cancelado.
- Si se explora osteodistrofia renal, revisar la evidencia en enfermedad renal crónica y la seguridad (retención de líquidos, lípidos, hepatotoxicidad).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

