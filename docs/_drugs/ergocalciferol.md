---
layout: default
title: Ergocalciferol
parent: Solo Predicción del Modelo (L5)
nav_order: 260
evidence_level: L5
indication_count: 6
monitor_inn: "Ergocalciferol"
predicted_indications: ["acromesomelic dysplasia, Campailla Martinelli type", "renal tubular acidosis", "craniofacial conodysplasia", "hypophosphatemia (disease)", "renal osteodystrophy", "calcium-alkali syndrome"]
last_modified_at: 2026-10-23
description: "Ergocalciferol: nueva indicación predicha, Displasia acromesomélica, tipo Campailla-Martinelli (nivel de evidencia L5). Indicación original: COMBINACIONES"
---

# Ergocalciferol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Ergocalciferol: De "Combinaciones" (registro sanitario de un producto multivitamínico) a Displasia acromesomélica, tipo Campailla-Martinelli
{: .text-alpha }

## Resumen en Una Frase

Ergocalciferol (vitamina D2) figura en Colombia como componente del producto multivitamínico inyectable VITALIPID® N - ADULT, cuyo registro indica solo "COMBINACIONES".
El modelo TxGNN predice que podría ser efectivo para la **displasia acromesomélica tipo Campailla-Martinelli**, una displasia esquelética rara.
Actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que es solo una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | COMBINACIONES (texto del registro del producto multivitamínico; no describe un uso específico del ergocalciferol solo) |
| Nueva Indicación Predicha | Displasia acromesomélica tipo Campailla-Martinelli |
| Puntaje de Predicción TxGNN | 0.9983 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 1) |
| Número de Registros Sanitarios | Al menos 1 (la lista puede ser parcial) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, el ergocalciferol es una forma de vitamina D que participa en la absorción intestinal de calcio y fósforo y en la mineralización ósea. En Colombia aparece como parte de un producto de vitaminas en combinación, de modo que el registro no aporta una indicación propia del ergocalciferol solo.

La displasia acromesomélica es un trastorno esquelético raro y de origen genético. La única conexión plausible con la vitamina D es el metabolismo óseo y mineral, y esa relación es especulativa. No hay estudios que la respalden.

El puntaje alto de TxGNN (0.9983) proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. No es evidencia clínica y no demuestra que el fármaco funcione en esta enfermedad. Tampoco se ha evaluado la similitud con el uso original ni la compatibilidad de vías de administración.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19900781 | VITALIPID® N - ADULT (FRESENIUS KABI AB) | Emulsión inyectable | COMBINACIONES |

Se identificó al menos un registro y la lista puede ser parcial. Es un producto en combinación, por lo que no describe cómo está aprobado ni comercializado el ergocalciferol como principio activo único.

## Consideraciones de Seguridad

- **Relaciones de contraindicación en el grafo de conocimiento** (no provienen del texto del prospecto): el grafo registra relaciones de contraindicación con hipertensión, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, gastritis, sarcoidosis, diabetes mellitus y cetoacidosis diabética, fibrilación auricular, hiperparatiroidismo, hipercalcemia, nefrocalcinosis, trastornos del metabolismo del fósforo y de la coagulación, anemia falciforme, hiperoxaluria primaria, hemocromatosis hereditaria y otros trastornos del metabolismo del hierro, enfermedad de Wilson, hiperlipidemia (incluida la familiar), y carcinoma de mama femenino y de próstata. Esta lista requiere verificación con el prospecto.
- **Interacciones farmacológicas**: se identificaron 55 interacciones. Las de nivel **mayor** son con otras formas de vitamina D: colecalciferol, calcifediol, calcitriol y doxercalciferol. Entre las de nivel **moderado** destacan hidroclorotiazida, clortalidona, clorotiazida, carbamazepina, barbitúricos (amobarbital, butalbital), rifabutina, digoxina, resinas secuestradoras de ácidos biliares (colestiramina, colesevelam, colestipol), sevelámero y óxido de magnesio. La interacción con cimetidina es de nivel menor.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para la displasia acromesomélica se basa solo en el puntaje del modelo, sin ensayos, sin publicaciones y sin un mecanismo identificable. No hay base para avanzar hacia una evaluación clínica.

**Para avanzar se necesita:**
- Datos del mecanismo de acción del ergocalciferol y un vínculo mecanístico documentado con esta displasia.
- Estudios preclínicos o clínicos que evalúen directamente esta enfermedad.
- Advertencias y contraindicaciones del prospecto en INVIMA, que no están disponibles.
- Un registro sanitario del ergocalciferol como principio activo único, para evaluar disponibilidad local.

## Otras Indicaciones Predichas en los Datos Compilados

| Enfermedad | Puntaje TxGNN | Nivel de Evidencia | Decisión | Comentario |
|------|------|------|------|------|
| Osteodistrofia renal | 0.9967 | L3 | Proceed with Guardrails | Es la mejor respaldada: 1 ensayo de Fase 4 (NCT01799317, estado desconocido, 60 participantes) y múltiples revisiones, además de un ensayo aleatorizado de ergocalciferol frente a calcitriol en enfermedad renal crónica (PMID 27401037). La vitamina D nutricional puede corregir la deficiencia de 25(OH)D y ayudar a reducir el hiperparatiroidismo secundario. Requiere vigilar calcio, fósforo, PTH y 25(OH)D, y evitar hipercalcemia. |
| Hipofosfatemia | 0.9972 | L4 | Research Question | Solo reportes de casos y revisiones indirectas. La hipofosfatemia por exceso de FGF23 o pérdida renal de fosfato no se corrige con ergocalciferol solo. |
| Acidosis tubular renal | 0.9981 | L5 | Hold | Solo dos reportes de casos no relacionados con el tratamiento. |
| Conodisplasia craneofacial | 0.9981 | L5 | Hold | Sin evidencia ni racional mecanístico. |
| Síndrome de calcio-álcali | 0.9946 | L5 | Hold | La vitamina D puede agravar la hipercalcemia, por lo que existe una posible preocupación de seguridad. |
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

