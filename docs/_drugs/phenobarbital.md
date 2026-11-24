---
layout: default
title: Phenobarbital
parent: Solo Predicción del Modelo (L5)
nav_order: 511
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
description: "Phenobarbital: nueva indicación predicha, Neoplasia del nervio trigémino (nivel de evidencia L5). Indicación original: Fenobarbital"
monitor_inn: "Phenobarbital"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia", "beta-ketothiolase deficiency"]
---

# Phenobarbital
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Fenobarbital: De Fenobarbital (indicación sin detallar) a Neoplasia del Nervio Trigémino
{: .text-alpha }

## Resumen en Una Frase

Fenobarbital es un barbitúrico utilizado clásicamente como anticonvulsivo; en Colombia sus registros sanitarios solo mencionan "FENOBARBITAL" como indicación, sin mayor detalle.
El modelo TxGNN predice que podría ser efectivo para **neoplasia del nervio trigémino**, pero no hay ensayos clínicos y la única publicación asociada es una serie de casos sobre síndrome de Sturge-Weber, que no respalda un efecto antitumoral.
Esta predicción proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica; no debe considerarse una señal farmacológica real.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Fenobarbital (el registro no detalla la indicación; uso clásico como anticonvulsivo) |
| Nueva Indicación Predicha | Neoplasia del nervio trigémino |
| Puntaje de Predicción TxGNN | 0.9996 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 4 de 4) |
| Número de Registros Sanitarios | 4 (vigentes: 4) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Clinical Pharmacology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Phenobarbital (traducción no oficial): «El mecanismo de acción preciso del fenobarbital para el tratamiento de las crisis convulsivas neonatales no se conoce por completo, pero se cree que implica la potenciación de la inhibición sináptica mediante una acción sobre el receptor GABA A.» Texto original en inglés: "The precise mechanism of action for phenobarbital for the treatment of neonatal seizures is not fully understood, but it is thought to involve potentiation of synaptic inhibition through an action on the GABA A receptor." ([DailyMed: Sezaby (phenobarbital sodium) prescribing information, Sun Pharmaceutical Industries, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8c7d0402-4977-4c25-bc4b-11db91339e9a), versión del 2026-10-23; consultado el 2026-11-19). Según la información farmacológica conocida, el fenobarbital potencia la inhibición mediada por el receptor GABA-A y se usa en todos los tipos de convulsiones, salvo las crisis de ausencia. También se registra como ligando del receptor X de pregnano (PXR, gen NR1I2), lo que explica su efecto inductor enzimático.

En este caso la predicción **no tiene un vínculo mecanístico plausible** con la biología tumoral. El único artículo asociado es una serie de casos de síndrome de Sturge-Weber, un trastorno neurocutáneo en el que el fenobarbital se usa para controlar las crisis, no para tratar una neoplasia. El puntaje alto proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas (el fármaco se relaciona con enfermedades del nervio trigémino y neurológicas), no evidencia biológica ni una señal terapéutica.

Otras predicciones del modelo, de similar puntaje, sí son más coherentes con el mecanismo del fármaco: epilepsias reflejas (epilepsia por sobresalto, convulsiones audiogénicas, por lectura, por alimentación) y neuralgia del trigémino. Se mencionan en las conclusiones como alternativas de investigación.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Serie de casos | Anales Españoles de Pediatría | Experiencia con 14 casos de síndrome de Sturge-Weber a lo largo de 25 años: características clínicas, evolución y respuesta terapéutica. No evalúa el fenobarbital como tratamiento de una neoplasia. |

---

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 19905550 | FENOBARBITAL TABLETAS 50 MG. | TABLETA | FENOBARBITAL | Vigente |
| 20008611 | FENOBARBITALSODICO 40 MG/ML | SOLUCION INYECTABLE | FENOBARBITAL | Vigente |
| 20101277 | FENOBARBITAL 10 MG TABLETAS | TABLETA | FENOBARBITAL | Vigente |
| 20108399 | FENOBARBITAL 0.4 % SOLUCIÓN ORAL | SOLUCION ORAL | FENOBARBITAL | Vigente |

Se muestran los 4 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: se identificó una interacción farmacológica de tipo farmacológico/diana: el fenobarbital actúa sobre el receptor X de pregnano (NR1I2), mecanismo asociado a inducción enzimática hepática, lo que puede alterar los niveles de otros fármacos.
- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad del grafo PrimeKG, no texto de prospecto): porfiria (hereditaria y del metabolismo de porfirinas), insuficiencia y enfermedad hepática, enfermedad renal, enfermedad pulmonar obstructiva crónica, trastornos de ansiedad y neuróticos, distimia, trastornos psicóticos y esquizoafectivos, lupus eritematoso sistémico, trombocitopenia, hipotiroidismo/mixedema, hiperglucemia, hipertensión, úlcera gástrica/péptica y gastritis, enfermedad de la vesícula biliar, insomnio y piouréter.
- **Otras señales de la literatura recuperada**: posibles efectos cognitivos tras el tratamiento temprano (por ejemplo, descenso del CI en niños con convulsiones febriles) y preocupación por neurotoxicidad en el cerebro en desarrollo; síndrome de hipersensibilidad a anticonvulsivantes.

<!-- review:begin co-lic-20261105-phenobarbital-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Los tres registros pertenecen al Fondo Nacional de Estupefacientes (Ministerio de Salud y Protección Social) y están cancelados; actualmente no hay registros vigentes." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 4 registros sanitarios (vigentes: 4); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-phenobarbital-1 -->

No se dispone de advertencias ni contraindicaciones del prospecto; consultar el prospecto para la información de seguridad oficial.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para neoplasia del nervio trigémino solo cuenta con el modelo como respaldo (nivel L5): no hay ensayos clínicos, la única publicación no es pertinente y no existe un vínculo mecanístico plausible.

<!-- review:begin co-lic-20261105-phenobarbital-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción para neoplasia del nervio trigémino solo cuenta con el modelo como respaldo (nivel L5): no hay ensayos clínicos, la única publicación no es pertinente y no existe un vínculo mecanístico plausible. Además, el fármaco no tiene registros vigentes en Colombia." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 4 registros sanitarios (vigentes: 4); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-phenobarbital-2 -->

**Para avanzar se necesita:**
- Descartar esta indicación como candidata o, en su caso, hallar evidencia biológica que relacione el fenobarbital con tumores del nervio trigémino.
- Priorizar, como preguntas de investigación, las indicaciones con respaldo mecanístico más coherente: epilepsias reflejas (audiogénicas, por sobresalto, por lectura, por alimentación, inducidas por micción o por pensamiento) y neuralgia del trigémino, donde la evidencia actual es indirecta, preclínica o de casos.
- Obtener y revisar el prospecto de INVIMA para completar advertencias y contraindicaciones.
- Complementar los datos del mecanismo de acción desde DrugBank.
- Verificar la situación regulatoria actual en Colombia, donde el medicamento está comercializado y los 4 registros están vigentes.

<!-- review:begin co-lic-20261112-phenobarbital-1 -->

> **Corrección de revisión (2026-11-12)**: Texto original: "los 3 registros están vigentes" Corregido según los datos del INVIMA (Código Único de Medicamentos, datos al 2026-11-05): 4 registros sanitarios, de los cuales 4 vigentes. Las cifras actuales están en el Resumen rápido. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261112-phenobarbital-1 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Los tres registros pertenecen al Fondo Nacional de Estupefacientes (Ministerio de Salud y Protección Social) y están cancelados; actualmente" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Además, el fármaco no tiene registros vigentes en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-12 | Número de registros vigentes: 3 → 4 | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Sezaby (phenobarbital sodium) prescribing information, Sun Pharmaceutical Industries, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8c7d0402-4977-4c25-bc4b-11db91339e9a) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

