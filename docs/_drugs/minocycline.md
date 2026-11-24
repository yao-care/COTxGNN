---
layout: default
title: Minocycline
parent: Solo Predicción del Modelo (L5)
nav_order: 447
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Minocycline: nueva indicación predicha, Queratoconjuntivitis epitelial punteada (nivel de evidencia L5). Indicación original: No especificada"
monitor_inn: "minocycline"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "exposure keratitis"]
---

# Minocycline
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Minociclina: De Indicación No Especificada a Queratoconjuntivitis Epitelial Punteada
{: .text-alpha }

## Resumen en Una Frase

Minociclina es un antibiótico de la familia de las tetraciclinas. El texto de la indicación aprobada solo repite el nombre del fármaco, por lo que no se conoce la indicación original específica.
El modelo TxGNN predice que podría ser efectivo para **queratoconjuntivitis epitelial punteada**, aunque actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; se trata solo de una predicción del modelo.

<!-- review:begin co-lic-20261105-minocycline-3 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "En Colombia contó con un registro sanitario en cápsulas de 100 mg, pero el texto de la indicación aprobada solo repite el nombre del fármaco, por lo que no se conoce la indicación original específica." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-minocycline-3 -->

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro solo indica "MINOCICLINA") |
| Nueva Indicación Predicha | Queratoconjuntivitis epitelial punteada |
| Puntaje de Predicción TxGNN | 0.9963 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Minocycline (traducción no oficial): «Se desconoce el mecanismo de acción de ARESTIN como complemento de los procedimientos de raspado y alisado radicular para la reducción de la profundidad de las bolsas en pacientes con periodontitis del adulto.» Texto original en inglés: "The mechanism of action of ARESTIN as an adjunct to scaling and root planing procedures for reduction of pocket depth in patients with adult periodontitis is unknown." ([DailyMed: Arestin (minocycline hydrochloride) prescribing information, OraPharma, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8515df41-1936-4f3b-86ba-d2bb2a8441fb), versión del 2024-05-31; consultado el 2026-11-19). Según la información conocida, minociclina es una tetraciclina con propiedades antibacterianas, antiinflamatorias e inhibidoras de metaloproteinasas de matriz (MMP). Su eficacia antibacteriana está bien establecida, y mecanísticamente podría ser aplicable a enfermedades inflamatorias de la superficie ocular.

La queratoconjuntivitis epitelial punteada implica daño e inflamación del epitelio corneal y conjuntival. Un fármaco que reduce la inflamación y la actividad de las MMP podría, en teoría, atenuar ese daño. Este razonamiento es solo una hipótesis: no se verificó con ningún ensayo ni publicación en los datos compilados para este informe.

El puntaje del modelo es muy alto (0.9963), pero es una predicción computacional, no evidencia clínica. También se predijo **queraitis por exposición** (puntaje 0.9920), con el mismo nivel de evidencia (L5) y la misma lógica mecanística hipotética.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

<!-- review:begin co-lic-20261105-minocycline-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "No hay registros vigentes actualmente." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-minocycline-1 -->

---

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 19985510 | MINOCICLINA CAPSULAS X 100 MG | CAPSULA DURA | MINOCICLINA | Vigente |

Se muestra el único registro sanitario de este principio activo en los datos del INVIMA, Código Único de Medicamentos.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

- **Contraindicaciones o enfermedades de riesgo (grafo de conocimiento, no texto del prospecto)**: enfermedad renal, piouréter, enfermedad hepática, enfermedad de la vesícula biliar, colitis por *Clostridium difficile*, enterocolitis necrosante perinatal, pseudotumor cerebral, hipertensión intracraneal y disquinesia del esófago.
- **Interacciones Farmacológicas**: se identificaron 272 interacciones. Entre las listadas:
  - **Mayores**: isotretinoína y acitretina.
  - **Moderadas**: etinilestradiol, amoxicilina, ampicilina, citrato de sodio, asparaginasa (*E. coli* y *Erwinia chrysanthemi*), balsalazida, subcitrato de bismuto y potasio, fosfato de calcio, acetato de calcio, brentuximab vedotina, calaspargasa pegol, cannabidiol y ácido aminolevulínico tópico.
  - **Menores**: acetazolamida, hidroclorotiazida, amilorida y bumetanida.

Las advertencias del prospecto no están disponibles; consultar el prospecto para la información completa de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el modelo (nivel L5), sin ensayos ni publicaciones. Tampoco hay datos del prospecto ni del mecanismo de acción que permitan evaluar la seguridad o la plausibilidad con rigor.

<!-- review:begin co-lic-20261105-minocycline-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción se apoya únicamente en el modelo (nivel L5), sin ensayos ni publicaciones, y el único registro sanitario local está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-minocycline-2 -->

**Para avanzar se necesita:**
- Revisión sistemática de la literatura sobre minociclina en queratoconjuntivitis y superficie ocular.
- Datos del mecanismo de acción desde DrugBank.
- Advertencias y contraindicaciones del prospecto en INVIMA.
- Evaluación de la vía de administración: la forma registrada es oral y no se ha determinado compatibilidad con una vía oftálmica.
- Confirmar la situación regulatoria y la disponibilidad de producto en Colombia.
- Evaluación de seguridad de las interacciones mayores y de las enfermedades de riesgo identificadas.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "No hay registros vigentes actualmente" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "y el único registro sanitario local está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "En Colombia contó con un registro sanitario en cápsulas de 100 mg, pero" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Arestin (minocycline hydrochloride) prescribing information, OraPharma, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8515df41-1936-4f3b-86ba-d2bb2a8441fb) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

