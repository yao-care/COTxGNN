---
layout: default
title: Cholecalciferol
parent: Solo Predicción del Modelo (L5)
nav_order: 155
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Cholecalciferol: nueva indicación predicha, Hipoparatiroidismo aislado familiar por alteración de la secreción de… (nivel de evidencia L5). Indicación original: Multivitaminas y otros minerales, incl…"
monitor_inn: "Cholecalciferol"
predicted_indications: ["familial isolated hypoparathyroidism due to impaired PTH secretion", "acromesomelic dysplasia, Campailla Martinelli type", "craniofacial conodysplasia", "Dahlberg-Borer-Newcomer syndrome", "hypophosphatemic rickets", "renal osteodystrophy", "renal tubular acidosis"]
---

# Cholecalciferol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

# Colecalciferol: De Multivitaminas y Minerales en Combinación a Hipoparatiroidismo Aislado Familiar por Alteración de la Secreción de PTH

## Resumen en Una Frase

El colecalciferol (vitamina D3) está registrado en Colombia como multivitamínico y suplemento de calcio en combinación.
El modelo TxGNN predice que podría ser efectivo para el **hipoparatiroidismo aislado familiar por alteración de la secreción de PTH**,
pero **no hay ensayos clínicos ni publicaciones** que respalden esta indicación específica; la predicción se basa solo en el modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Multivitaminas y otros minerales, incluidas combinaciones |
| Nueva Indicación Predicha | Hipoparatiroidismo aislado familiar por alteración de la secreción de PTH |
| Puntaje de Predicción TxGNN | 99.79% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, el colecalciferol es un precursor de la vitamina D: en el hígado y el riñón se convierte en la forma activa (calcitriol), que regula la absorción de calcio y fósforo. Su uso en deficiencia de vitamina D y en trastornos del metabolismo del calcio está bien establecido.

El hipoparatiroidismo se caracteriza por una secreción insuficiente de hormona paratiroidea (PTH) y por un desequilibrio del calcio. La vitamina D se usa clínicamente en el hipoparatiroidismo para mantener la homeostasis del calcio, lo que explica el vínculo que detecta el modelo entre una vitamina que regula el calcio y una enfermedad del eje calcio-PTH.

Hay una limitación importante. En el hipoparatiroidismo, la conversión del colecalciferol a su forma activa depende de la PTH (la 1-alfa-hidroxilación renal) y está alterada. Por eso en la práctica se usan análogos activos como el calcitriol, y no el colecalciferol. El puntaje alto del modelo es solo una predicción, sin respaldo clínico propio para esta forma familiar.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19908281 | SUPRAVITAL (PROCAPS S.A.) | Cápsula blanda | Multivitaminas y otros minerales, incluidas combinaciones |
| 20037895 | CALCIBON D SOYA FORTE TABLETAS (FARMA DE COLOMBIA S.A.S.) | Tableta | Calcio (diferentes sales en combinación) |

Ambos registros figuran como **cancelados**; actualmente no hay registros vigentes.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** el grafo de conocimiento de TxGNN asocia el colecalciferol con enfermedades en las que su uso podría ser desaconsejable. Entre ellas:
  - Hipercalcemia, hiperparatiroidismo, nefrocalcinosis y enfermedades del metabolismo del fósforo.
  - Enfermedad renal, enfermedad hepática y enfermedad de la vesícula biliar.
  - Sarcoidosis, hipertensión y fibrilación auricular.
  - Diabetes mellitus y cetoacidosis diabética.
  - Hiperoxaluria primaria, hemocromatosis hereditaria y enfermedad de Wilson.
  - Cáncer de próstata y carcinoma de mama femenino.
  - Hiperlipidemia, trastornos de la coagulación y anemia falciforme.
- **Interacciones farmacológicas:** solo hay un registro, de tipo farmacológico: el metabolito de la vitamina D3 actúa sobre el receptor X farnesoide-β (estudio en ratón). No corresponde a una interacción con otro medicamento de relevancia clínica establecida.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto (99.79%), pero no cuenta con ensayos ni literatura propios (nivel L5). Además, el mecanismo de la enfermedad hace que el colecalciferol sea menos adecuado que los análogos activos de la vitamina D. Tampoco hay registros sanitarios vigentes en Colombia.

**Para avanzar se necesita:**
- Datos sobre el mecanismo de acción del fármaco.
- Evidencia clínica o preclínica específica en hipoparatiroidismo aislado familiar, y una comparación con los análogos activos de la vitamina D (calcitriol, alfacalcidol).
- El prospecto vigente, con advertencias y contraindicaciones, y la situación regulatoria actual (registros cancelados).
- Un plan de monitoreo de calcio sérico y calciuria, por el riesgo de hipercalcemia y nefrocalcinosis.
- Evaluar otras indicaciones predichas con más sustento. La osteodistrofia renal, por ejemplo, cuenta con ensayos clínicos y literatura y alcanza un nivel L2.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

