---
layout: default
title: Indacaterol
parent: Solo Predicción del Modelo (L5)
nav_order: 341
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Indacaterol: nueva indicación predicha, Síndrome nefrogénico de antidiuresis inapropiada (NSIAD) (nivel de evidencia L5). Indicación original: Formoterol y mometasona"
monitor_inn: "INDACATEROL"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "headache disorder", "trigeminal autonomic cephalalgia", "paratenonitis", "calcific tendinitis", "hypertrichosis (disease)", "myositis", "anaphylaxis", "Ambras type hypertrichosis universalis congenita"]
---

# Indacaterol
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

# Indacaterol: De Formoterol y Mometasona (combinación respiratoria) a Síndrome Nefrogénico de Antidiuresis Inapropiada

## Resumen en Una Frase

Indacaterol es un agonista beta-2 adrenérgico de acción ultra-prolongada, cuyo registro sanitario en Colombia lo asocia a una combinación respiratoria (texto registrado: "formoterol y mometasona").
El modelo TxGNN predice que podría ser efectivo para el **síndrome nefrogénico de antidiuresis inapropiada (NSIAD)**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Formoterol y mometasona (texto del registro sanitario) |
| Nueva Indicación Predicha | Síndrome nefrogénico de antidiuresis inapropiada (NSIAD) |
| Puntaje de Predicción TxGNN | 99.54% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información conocida, indacaterol es un agonista beta-2 adrenérgico de acción ultra-prolongada que relaja el músculo liso de las vías respiratorias mediante la vía del receptor beta-2 y el AMPc. Su eficacia en enfermedad obstructiva de las vías aéreas (asma, EPOC) está documentada.

La relación entre la indicación original y la nueva es débil. El NSIAD es causado por variantes de ganancia de función en el gen *AVPR2* (receptor V2 de la vasopresina). Existe un único vínculo especulativo: la agonía beta-2 eleva el AMPc, que también es la señal posterior a la activación del receptor V2. Esta hipótesis **no tiene respaldo en datos**, y no se encontró un vínculo mecanístico establecido.

En conclusión, la predicción se basa únicamente en el modelo y debe considerarse una hipótesis sin confirmar. Puede tratarse de un artefacto del grafo de conocimiento.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20209060 | Atectura® Breezhaler® 150/80 mcg polvo para inhalación | Cápsula dura | Formoterol y mometasona | Cancelado |
| 20208413 | Atectura® Breezhaler® 150/160 mcg polvo para inhalación | Cápsula dura | Formoterol y mometasona | Cancelado |

Ambos registros pertenecen a Novartis Pharma AG y están cancelados, por lo que no hay un producto vigente en Colombia.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad del modelo, no texto del prospecto): hipertensión, síndrome de QT largo (incluido el familiar), epilepsia, hiperglucemia, deficiencia de potasio, diabetes mellitus, cetoacidosis diabética, paro cardíaco súbito, enfermedad de conducción cardíaca, tirotoxicosis/hipertiroidismo/enfermedad de Graves y enfermedad coronaria.
- **Interacciones farmacológicas** (100 registradas; se listan las principales):
  - *Moderadas*: antidiabéticos (acarbosa, metformina, pioglitazona, alogliptina, saxagliptina, albiglutida, canagliflozina, dapagliflozina, clorpropamida), epinefrina, isometepteno, famotidina y claritromicina.
  - *Menores*: corticosteroides (hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida, beclometasona) y aprepitant.

Se recomienda consultar el prospecto para las advertencias y contraindicaciones oficiales.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación predicha de mayor puntaje (NSIAD) solo cuenta con la predicción del modelo, sin ensayos ni literatura, y sin mecanismo plausible establecido. Además, no hay producto vigente en Colombia.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (consulta a DrugBank) y un análisis mecanístico formal del vínculo entre la agonía beta-2 y la señalización del receptor V2.
- Estudios preclínicos que respalden la hipótesis antes de considerar ensayos clínicos.
- Descargar y analizar el prospecto en INVIMA para completar advertencias y contraindicaciones.
- Verificar la disponibilidad regional, dado que solo existen registros cancelados.

**Nota sobre otras predicciones:** de las 10 indicaciones predichas, solo la **enfermedad bronquial** (puntaje 99.18%, posición 7) tiene evidencia real: 24 ensayos clínicos (incluidos varios de Fase 3 completados, como NCT02554786 con 2216 participantes) y 20 publicaciones, con nivel L1 y decisión *Proceed with Guardrails*. Sin embargo, esto equivale en gran medida a reconfirmar el uso respiratorio ya conocido y no a un reposicionamiento genuino. Además, muchos ensayos usan combinaciones de dosis fijas, por lo que no se puede aislar el aporte de indacaterol solo. Un ensayo de Fase 3 (NCT04206761) fue retirado con 0 participantes.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

