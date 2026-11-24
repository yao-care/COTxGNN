---
layout: default
title: Lanreotide
parent: Solo Predicción del Modelo (L5)
nav_order: 378
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-24
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
El modelo TxGNN predice que podría ser efectivo para **hipertricosis**, con una puntuación alta (0.9997), pero **sin ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto aprobado solo indica "Lanreotido") |
| Nueva Indicación Predicha | Hipertricosis (enfermedad) |
| Puntaje de Predicción TxGNN | 0.9997 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 4 de 4) |
| Número de Registros Sanitarios | 4 (vigentes: 4) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Lanreotide (traducción no oficial): «La lanreotida, el componente activo de SOMATULINE DEPOT, es un análogo octapeptídico de la somatostatina natural. Se cree que el mecanismo de acción de la lanreotida es similar al de la somatostatina natural.» Texto original en inglés: "Lanreotide, the active component of SOMATULINE DEPOT is an octapeptide analog of natural somatostatin. The mechanism of action of lanreotide is believed to be similar to that of natural somatostatin." ([DailyMed: Somatuline Depot (lanreotide acetate) prescribing information, Ipsen Biopharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6e4a41fd-a753-4362-87ee-8cc56ed3660d), versión del 2024-10-11; consultado el 2026-11-19). Según la información conocida, lanreotida es un análogo de la somatostatina que suprime la secreción de la hormona de crecimiento (GH), del factor de crecimiento similar a la insulina tipo 1 (IGF-1) y de otras hormonas.

**La evidencia disponible no respalda un vínculo mecanístico claro.** La hipertricosis no es una diana reconocida de la vía de la somatostatina. El análisis del mecanismo concluye que no existe una relación farmacológica establecida, y que la puntuación alta proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

Las otras cuatro predicciones mejor clasificadas tampoco tienen sustento: síndrome de malformación con componente dental o periodontal, síndrome con malformación de Dandy-Walker, anomalía genética aislada del tallo del cabello e hipertricosis universal congénita tipo Ambras. Todas son condiciones genéticas o del desarrollo que un análogo de somatostatina no se espera que modifique, y ninguna cuenta con ensayos ni literatura.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

<!-- review:begin co-lic-20261105-lanreotide-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Los cuatro registros sanitarios están **cancelados**; no hay productos vigentes." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-lanreotide-1 -->

---

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 19935648 | SOMATULINE ® AUTOGEL 90MG | SOLUCION INYECTABLE | LANREOTIDO | Vigente |
| 19935650 | SOMATULINE ® AUTOGEL ® 60 MG | SOLUCION INYECTABLE | LANREOTIDO | Vigente |
| 19995723 | SOMATULINE®AUTOGEL 120 MG | SOLUCION INYECTABLE | LANREOTIDO | Vigente |
| 20258943 | LANTERA | SOLUCION INYECTABLE | LANREOTIDO | Vigente |

Se muestran los 4 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

- **Enfermedades con posible contraindicación o precaución (según el grafo de conocimiento, no el prospecto):** trastornos hipertensivos e hipertensión, enfermedad hepática, enfermedad de la vesícula biliar (colelitiasis, colecistolitiasis, coledocolitiasis), hiperglucemia, hipoglucemia, hipotiroidismo (incluidos mixedema e hipotiroidismo congénito) y deterioro de la función renal.
- **Interacciones farmacológicas:** se identificaron 136 interacciones en total. Entre las revisadas, todas son de nivel **moderado** y corresponden principalmente a antidiabéticos, cuyo control glucémico puede alterarse: acarbosa, albiglutida, alogliptina, metformina, pioglitazona, canagliflozina, clorpropamida, dapagliflozina, dulaglutida, empagliflozina, linagliptina, glimepirida, semaglutida y diversas insulinas (aspart, degludec, detemir, glargina, glulisina, isófana y regular).

No se dispone de las advertencias ni contraindicaciones del prospecto del registro sanitario.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para hipertricosis es solo computacional (nivel L5): no hay ensayos, no hay literatura y no existe un vínculo mecanístico plausible.

<!-- review:begin co-lic-20261105-lanreotide-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción para hipertricosis es solo computacional (nivel L5): no hay ensayos, no hay literatura y no existe un vínculo mecanístico plausible. Además, ya no hay registros sanitarios vigentes en Colombia." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-lanreotide-2 -->

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), una brecha de seguridad bloqueante.
- Obtener los datos del mecanismo de acción desde DrugBank.
- Aclarar la indicación original aprobada, ya que el registro solo indica "Lanreotido".
- Justificar biológicamente, mediante estudios preclínicos o de mecanismo, cualquier vínculo entre la vía de la somatostatina y la hipertricosis antes de reconsiderar la candidatura.
- Confirmar la situación comercial y regulatoria actual del producto en Colombia.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Los cuatro registros sanitarios están **cancelados**; no hay productos vigentes" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Además, ya no hay registros sanitarios vigentes en Colombia" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Somatuline Depot (lanreotide acetate) prescribing information, Ipsen Biopharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6e4a41fd-a753-4362-87ee-8cc56ed3660d) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

