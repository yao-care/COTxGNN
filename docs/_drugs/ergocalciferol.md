---
layout: default
title: Ergocalciferol
parent: Solo Predicción del Modelo (L5)
nav_order: 260
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ergocalciferol: nueva indicación predicha, Hipoparatiroidismo aislado familiar por alteración de la secreción de… (nivel de evidencia L5). Indicación original: Combinaciones"
monitor_inn: "Ergocalciferol"
predicted_indications: ["familial isolated hypoparathyroidism due to impaired PTH secretion", "acromesomelic dysplasia, Campailla Martinelli type", "renal tubular acidosis", "craniofacial conodysplasia", "Dahlberg-Borer-Newcomer syndrome", "hypophosphatemia (disease)", "renal osteodystrophy", "calcium-alkali syndrome", "vitamin D-dependent rickets"]
---

# Ergocalciferol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Ergocalciferol: De Combinaciones (indicación no especificada) a Hipoparatiroidismo aislado familiar por alteración de la secreción de PTH

## Resumen en Una Frase

Ergocalciferol (vitamina D2) cuenta en Colombia con un único registro sanitario, hoy cancelado, correspondiente a una emulsión inyectable de combinación de vitaminas (VITALIPID® N - ADULT). El registro describe su indicación solo como "COMBINACIONES".
El modelo TxGNN predice que podría ser efectivo para el **hipoparatiroidismo aislado familiar por alteración de la secreción de PTH**, con **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción específica.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Combinaciones (el registro no detalla la indicación) |
| Nueva Indicación Predicha | Hipoparatiroidismo aislado familiar por alteración de la secreción de PTH |
| Puntaje de Predicción TxGNN | 99.85% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 (0 vigentes, 1 cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este fármaco. Según la información conocida, el ergocalciferol es un precursor de la vitamina D2. Necesita activarse en el hígado y el riñón para elevar el calcio sérico, y su uso en hipoparatiroidismo tiene antecedentes históricos.

El hipoparatiroidismo se caracteriza por una secreción insuficiente de PTH, y con ello por hipocalcemia. En este cuadro la hidroxilación renal en posición 1-alfa está poco estimulada. Por eso la vitamina D2 nativa es una opción débil frente a calcitriol o alfacalcidol, que no dependen de esa activación. El vínculo es plausible, pero se apoya solo en razonamiento farmacológico.

El puntaje del modelo es muy alto, pero es solo una predicción. En los datos compilados para este informe no hay ensayos clínicos ni literatura sobre esta indicación específica. Tampoco se pudo comparar la indicación original con la nueva, porque el registro colombiano no la detalla.

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
| 19900781 (cancelado) | VITALIPID® N - ADULT (Fresenius Kabi AB) | Emulsión inyectable | Combinaciones |

---

## Consideraciones de Seguridad

No se dispone de advertencias ni contraindicaciones del prospecto en los datos compilados. Se presenta la información disponible de otras fuentes.

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** el grafo de conocimiento de TxGNN asocia el fármaco con enfermedades en las que su uso podría ser inadecuado. Las más relevantes para esta evaluación son:
  - Hipercalcemia, hiperparatiroidismo, nefrocalcinosis y enfermedades del metabolismo del fósforo.
  - Enfermedad renal y enfermedad hepática.
  - Sarcoidosis, hipertensión y fibrilación auricular.
  - Diabetes mellitus y cetoacidosis diabética.
  - Hiperlipidemia, cáncer de próstata y carcinoma de mama femenino.
  - Enfermedades de la coagulación, anemia falciforme, hemocromatosis hereditaria y enfermedad de Wilson.
  
  Estas asociaciones deben verificarse contra fuentes regulatorias.
- **Interacciones farmacológicas:** se identificaron 55 interacciones. Entre las mostradas:
  - **Mayores:** colecalciferol, calcifediol, calcitriol y doxercalciferol. Combinar análogos de vitamina D aumenta el riesgo de hipercalcemia.
  - **Moderadas:** hidroclorotiazida, clortalidona, clorotiazida, digoxina, carbamazepina, amobarbital, butalbital, rifabutina, colestiramina, colestipol, colesevelam, sevelamer, óxido de magnesio y calcipotriol y calcitriol tópicos.
  - **Menores:** cimetidina.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para hipoparatiroidismo aislado familiar tiene un puntaje alto, pero no cuenta con ningún ensayo clínico ni publicación (nivel L5). Además, el ergocalciferol es una opción farmacológicamente débil en la ausencia de PTH. El único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y del prospecto (advertencias y contraindicaciones), que no estaban disponibles.
- Revisión de la literatura específica sobre vitamina D en hipoparatiroidismo y comparación con calcitriol o alfacalcidol.
- Definir una vía de acceso en Colombia, dado que no hay registros vigentes.
- Un plan de monitoreo de calcio, fósforo, PTH y 25-OH vitamina D, por el riesgo de hipercalcemia.

**Nota sobre otras predicciones del mismo fármaco:** entre las 10 indicaciones predichas, la **osteodistrofia renal** (puntaje 99.67%) es la que cuenta con más respaldo. Tiene un ensayo de Fase 4 (NCT01799317, n=60, estado desconocido), un estudio pediátrico que compara ergocalciferol con calcitriol y múltiples revisiones. Alcanza nivel L3 y una recomendación de "Proceed with Guardrails". Se sugiere priorizarla en una evaluación posterior, con monitoreo de calcio, fosfato, PTH y 25-OH vitamina D.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

