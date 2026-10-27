---
layout: default
title: Lanreotide
parent: Solo Predicción del Modelo (L5)
nav_order: 378
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Lanreotide: nueva indicación predicha, Hipertricosis (enfermedad) (nivel de evidencia L5). Indicación original: No especificada en el registro (el texto aprobado solo indica \"Lanreo…"
monitor_inn: "lanreotide"
predicted_indications: ["hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "Ambras type hypertrichosis universalis congenita"]
---

# Lanreotide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Lanreotida: De Lanreotida (sin indicación específica registrada) a Hipertricosis
{: .text-alpha }

## Resumen en Una Frase

Lanreotida es un análogo de la somatostatina comercializado en Colombia como inyectable de liberación prolongada (Somatuline Autogel), cuyo registro sanitario no detalla la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **hipertricosis**, con una puntuación alta (99.97%), pero **sin ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto aprobado solo indica "Lanreotido") |
| Nueva Indicación Predicha | Hipertricosis (enfermedad) |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 4 (todos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, lanreotida es un análogo de la somatostatina que suprime la secreción de la hormona de crecimiento (GH), del factor de crecimiento similar a la insulina tipo 1 (IGF-1) y de otras hormonas.

**La evidencia disponible no respalda un vínculo mecanístico claro.** La hipertricosis no es una diana reconocida de la vía de la somatostatina. El análisis del mecanismo concluye que no existe una relación farmacológica establecida, y que la puntuación alta del modelo probablemente refleja la cercanía en el grafo de conocimiento con otros fenotipos relacionados, no un efecto terapéutico real.

Las otras cuatro predicciones mejor clasificadas tampoco tienen sustento: síndrome de malformación con componente dental o periodontal, síndrome con malformación de Dandy-Walker, anomalía genética aislada del tallo del cabello e hipertricosis universal congénita tipo Ambras. Todas son condiciones genéticas o del desarrollo que un análogo de somatostatina no se espera que modifique, y ninguna cuenta con ensayos ni literatura.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

Los cuatro registros sanitarios están **cancelados**; no hay productos vigentes.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19935650 | Somatuline Autogel 60 mg (Ipsen Pharma) | Solución inyectable | Lanreotido |
| 20258943 | Lantera (Adium SAS) | Solución inyectable | Lanreotido |
| 19995723 | Somatuline Autogel 120 mg (Ipsen Pharma) | Solución inyectable | Lanreotido |
| 19935648 | Somatuline Autogel 90 mg (Ipsen Pharma) | Solución inyectable | Lanreotido |

---

## Consideraciones de Seguridad

- **Enfermedades con posible contraindicación o precaución (según el grafo de conocimiento, no el prospecto):** trastornos hipertensivos e hipertensión, enfermedad hepática, enfermedad de la vesícula biliar (colelitiasis, colecistolitiasis, coledocolitiasis), hiperglucemia, hipoglucemia, hipotiroidismo (incluidos mixedema e hipotiroidismo congénito) y deterioro de la función renal.
- **Interacciones farmacológicas:** se identificaron 136 interacciones en total. Entre las revisadas, todas son de nivel **moderado** y corresponden principalmente a antidiabéticos, cuyo control glucémico puede alterarse: acarbosa, albiglutida, alogliptina, metformina, pioglitazona, canagliflozina, clorpropamida, dapagliflozina, dulaglutida, empagliflozina, linagliptina, glimepirida, semaglutida y diversas insulinas (aspart, degludec, detemir, glargina, glulisina, isófana y regular).

No se dispone de las advertencias ni contraindicaciones del prospecto del registro sanitario.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para hipertricosis es solo computacional (nivel L5): no hay ensayos, no hay literatura y no existe un vínculo mecanístico plausible. Además, ya no hay registros sanitarios vigentes en Colombia.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), una brecha de seguridad bloqueante.
- Obtener los datos del mecanismo de acción desde DrugBank.
- Aclarar la indicación original aprobada, ya que el registro solo indica "Lanreotido".
- Justificar biológicamente, mediante estudios preclínicos o de mecanismo, cualquier vínculo entre la vía de la somatostatina y la hipertricosis antes de reconsiderar la candidatura.
- Confirmar la situación comercial y regulatoria actual del producto en Colombia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

