---
layout: default
title: Minocycline
parent: Solo Predicción del Modelo (L5)
nav_order: 447
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
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

Minociclina es un antibiótico de la familia de las tetraciclinas. En Colombia contó con un registro sanitario en cápsulas de 100 mg, pero el texto de la indicación aprobada solo repite el nombre del fármaco, por lo que no se conoce la indicación original específica.
El modelo TxGNN predice que podría ser efectivo para **queratoconjuntivitis epitelial punteada**, aunque actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; se trata solo de una predicción del modelo.

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

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, minociclina es una tetraciclina con propiedades antibacterianas, antiinflamatorias e inhibidoras de metaloproteinasas de matriz (MMP). Su eficacia antibacteriana está bien establecida, y mecanísticamente podría ser aplicable a enfermedades inflamatorias de la superficie ocular.

La queratoconjuntivitis epitelial punteada implica daño e inflamación del epitelio corneal y conjuntival. Un fármaco que reduce la inflamación y la actividad de las MMP podría, en teoría, atenuar ese daño. Este razonamiento es solo una hipótesis: no se verificó con ningún ensayo ni publicación en los datos compilados para este informe.

El puntaje del modelo es muy alto (0.9963), pero es una predicción computacional, no evidencia clínica. También se predijo **queraitis por exposición** (puntaje 0.9920), con el mismo nivel de evidencia (L5) y la misma lógica mecanística hipotética.

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
| 19985510 (cancelado) | MINOCICLINA CAPSULAS X 100 MG (GENFAR S.A) | Cápsula dura | MINOCICLINA |

No hay registros vigentes actualmente.

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
La predicción se apoya únicamente en el modelo (nivel L5), sin ensayos ni publicaciones, y el único registro sanitario local está cancelado. Tampoco hay datos del prospecto ni del mecanismo de acción que permitan evaluar la seguridad o la plausibilidad con rigor.

**Para avanzar se necesita:**
- Revisión sistemática de la literatura sobre minociclina en queratoconjuntivitis y superficie ocular.
- Datos del mecanismo de acción desde DrugBank.
- Advertencias y contraindicaciones del prospecto en INVIMA.
- Evaluación de la vía de administración: la forma registrada es oral y no se ha determinado compatibilidad con una vía oftálmica.
- Confirmar la situación regulatoria y la disponibilidad de producto en Colombia.
- Evaluación de seguridad de las interacciones mayores y de las enfermedades de riesgo identificadas.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

