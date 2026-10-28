---
layout: default
title: Octreotide
parent: Solo Predicción del Modelo (L5)
nav_order: 477
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Octreotide: nueva indicación predicha, Queratosis folicular invertida vulvar (nivel de evidencia L5). Indicación original: Octreotido"
monitor_inn: "Octreotide"
predicted_indications: ["vulvar inverted follicular keratosis", "seborrheic keratosis"]
---

# Octreotide
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

## Octreotida: De Octreotido (indicación registrada sin detalle) a Queratosis Folicular Invertida Vulvar
{: .text-alpha }

## Resumen en Una Frase

Octreotida es un análogo de la somatostatina que cuenta con un registro sanitario en Colombia (Sandostatin®), actualmente cancelado, cuyo texto de indicación se limita al nombre del principio activo ("Octreotido"). El modelo TxGNN predice que podría ser efectivo para **queratosis folicular invertida vulvar**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción; se trata de una señal puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Octreotido (el registro no detalla la indicación) |
| Nueva Indicación Predicha | Queratosis folicular invertida vulvar |
| Puntaje de Predicción TxGNN | 0.9958 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información farmacológica disponible, octreotida es un péptido análogo de la somatostatina que se une a los receptores de somatostatina SST2, SST3 y SST5. Su uso clínico conocido incluye tumores productores de hormona de crecimiento (acromegalia), tumores hipofisarios secretores de TSH y la obtención de imágenes de medicina nuclear de tumores neuroendocrinos que expresan receptores de somatostatina.

La relación entre estas indicaciones y la queratosis folicular invertida vulvar, una lesión epidérmica benigna, **no está respaldada por los datos disponibles**. Un papel de la señalización de receptores de somatostatina en la proliferación de queratinocitos benignos es meramente especulativo.

El puntaje alto de TxGNN (0.9958) es solo una predicción del modelo. La segunda predicción, queratosis seborreica (0.9955), también proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica independiente. Por tanto, esta predicción debe considerarse una hipótesis exploratoria.

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
| 20007947 (cancelado) | SANDOSTATIN® AMPOLLAS 0.1 MG | Solución inyectable | Octreotido |

El único registro, a nombre de Novartis Pharma AG, está cancelado, por lo que actualmente no hay producto vigente en Colombia con este principio activo según los datos compilados.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida a receptores (análogo peptídico de somatostatina); no es un citotóxico convencional |
| Riesgo de Mielosupresión | Sin datos en la información compilada; consultar el prospecto |
| Clasificación de Emetogenicidad | Sin datos; consultar el prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Contraindicaciones / condiciones de precaución según el grafo de conocimiento (TxGNN/PrimeKG):** estas relaciones provienen del grafo de conocimiento y no del texto del prospecto, por lo que deben verificarse con la ficha técnica oficial. Las condiciones asociadas son:
  - Metabólicas y endocrinas: hiperglucemia, hipoglucemia, diabetes mellitus, cetoacidosis diabética, hipotiroidismo (incluido el congénito), mixedema, deficiencia de vitamina B12.
  - Hepatobiliares: cirrosis hepática, enfermedad hepática, enfermedad de la vesícula biliar, colelitiasis, colecistolitiasis, coledocolitiasis.
  - Gastrointestinales: íleo, obstrucción intestinal.
  - Cardiovasculares: paro cardíaco súbito, enfermedad de la conducción cardíaca.
  - Renales: insuficiencia renal, uremia.
- **Interacciones farmacológicas:** los datos disponibles describen únicamente la afinidad farmacológica de octreotida por los receptores SST2, SST3 y SST5; no se identificaron interacciones con otros fármacos con nivel de gravedad asignado.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura, sin vínculo mecanístico respaldado por los datos y con el único registro sanitario colombiano cancelado. No hay base para avanzar en este momento.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (consulta a DrugBank) y análisis de un posible vínculo entre la señalización de somatostatina y la queratinocitosis benigna.
- Revisión sistemática de literatura y de registros de ensayos para queratosis folicular invertida y queratosis seborreica.
- Obtención y análisis del prospecto oficial (INVIMA u otra fuente) para advertencias y contraindicaciones, necesario antes de cualquier evaluación de seguridad.
- Aclarar el estado regulatorio en Colombia (registro cancelado) y la disponibilidad de otras presentaciones de octreotida.
- Evaluar la compatibilidad de la vía de administración (la presentación conocida es inyectable) con una lesión cutánea/vulvar benigna.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

