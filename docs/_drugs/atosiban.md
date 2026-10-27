---
layout: default
title: Atosiban
parent: Solo Predicción del Modelo (L5)
nav_order: 75
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Atosiban: nueva indicación predicha, Glaucoma hereditario primario (nivel de evidencia L5). Indicación original: Atosiban"
monitor_inn: "ATOSIBAN"
predicted_indications: ["primary hereditary glaucoma", "open-angle glaucoma", "congenital hypotrichosis milia", "alopecia", "hypotrichosis simplex of the scalp", "vascular disease", "diffuse alopecia areata", "arterial thoracic outlet syndrome", "venous thoracic outlet syndrome", "visceral calciphylaxis"]
---

# Atosiban
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

## Atosiban: De Indicación Registrada (Atosiban) a Glaucoma Hereditario Primario
{: .text-alpha }

## Resumen en Una Frase

Atosiban es un antagonista de los receptores de oxitocina y vasopresina V1A, usado como tocolítico para retrasar el parto prematuro; en Colombia sus registros solo declaran "atosiban" como indicación.
El modelo TxGNN predice que podría ser efectivo para **glaucoma hereditario primario**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es solo una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Atosiban (el registro sanitario no detalla una indicación clínica; el uso conocido es tocolítico en amenaza de parto prematuro) |
| Nueva Indicación Predicha | Glaucoma hereditario primario |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información farmacológica conocida, atosiban es un péptido que se une a los receptores de oxitocina (OXTR) y a los receptores de vasopresina V1A, V1B y V2. Se aprueba como tocolítico en la Unión Europea y otros países para retrasar el parto en mujeres embarazadas de 24 a 33 semanas con signos de parto prematuro.

No se ha establecido un vínculo mecanístico entre el antagonismo de los receptores de oxitocina/vasopresina y la dinámica del humor acuoso o la función de la malla trabecular. Cualquier papel en la regulación de la presión intraocular es hipotético. El puntaje alto del modelo refleja asociaciones en el grafo de conocimiento, no evidencia experimental o clínica.

La relación entre la indicación original (uso obstétrico) y el glaucoma es, por tanto, débil y especulativa. Esta predicción debe considerarse solo una hipótesis para generar preguntas de investigación.

### Otras predicciones del modelo

Las siguientes predicciones también carecen de ensayos y literatura, salvo la indicada:

| Posición | Enfermedad | Puntaje TxGNN | Nivel de Evidencia |
|------|------|------|------|
| 2 | Glaucoma de ángulo abierto | 99.92% | L5 |
| 3 | Milia con hipotricosis congénita | 99.89% | L5 |
| 4 | Alopecia | 99.89% | L5 |
| 5 | Hipotricosis simple del cuero cabelludo | 99.89% | L5 |
| 6 | Enfermedad vascular | 99.87% | L4 |
| 7 | Alopecia areata difusa | 99.86% | L5 |
| 8 | Síndrome del desfiladero torácico arterial | 99.86% | L5 |
| 9 | Síndrome del desfiladero torácico venoso | 99.86% | L5 |
| 10 | Calcifilaxis visceral | 99.84% | L5 |

La única predicción con literatura asociada es **enfermedad vascular** (15 publicaciones, casi todas preclínicas sobre oxitocina en cardioprotección en corazón de rata). Esa evidencia es indirecta y la dirección del efecto de un antagonista podría ser desfavorable, dado que la oxitocina parece protectora en esos modelos.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para glaucoma hereditario primario.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20131614 | EVERPREM® solución para infusión 6.75 mg/0.9 mL | Solución para infusión | Atosiban | Cancelado |
| 20131612 | EVERPREM® concentrado para solución para infusión 37.5 mg/5 mL | Solución concentrada para infusión | Atosiban | Cancelado |

Ambos registros pertenecen a Ever Valinject GmbH y están cancelados; actualmente no hay registros vigentes.

---

## Consideraciones de Seguridad

- **Interacciones farmacológicas / farmacología de blancos:** la consulta se completó y devolvió 4 entradas, que corresponden a los blancos farmacológicos de atosiban (receptores V1A, V1B, V2 y de oxitocina), no a interacciones con otros medicamentos.
- **Señal de seguridad indirecta (en la predicción de enfermedad vascular):** una cohorte neonatal (PMID 30646165, 2018) examinó la exposición a tocolíticos y la hemorragia intraventricular y muerte en prematuros. Es una señal de seguridad que requiere interpretación cuidadosa, no evidencia de eficacia.

No se dispone de advertencias ni contraindicaciones del prospecto. Consultar el prospecto para información de seguridad adicional.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para glaucoma hereditario primario se basa únicamente en el modelo (L5), sin ensayos clínicos, literatura ni vínculo mecanístico demostrado. Además, los dos registros sanitarios en Colombia están cancelados y no se dispone de información de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), lo cual es un requisito previo para cualquier evaluación de seguridad
- Complementar los datos del mecanismo de acción desde DrugBank
- Revisión de literatura dirigida sobre receptores de oxitocina/vasopresina y presión intraocular o biología de la malla trabecular
- Evaluar la compatibilidad de la vía de administración: atosiban es un péptido de uso intravenoso, y una indicación oftalmológica probablemente requeriría una formulación y vía distintas
- Valorar si la predicción de enfermedad vascular merece una revisión como pregunta de investigación, considerando que la evidencia disponible sugiere un posible efecto desfavorable de un antagonista
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

