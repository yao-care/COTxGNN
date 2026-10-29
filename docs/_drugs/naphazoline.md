---
layout: default
title: Naphazoline
parent: Solo Predicción del Modelo (L5)
nav_order: 460
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-29
description: "Naphazoline: nueva indicación predicha, Hipotricosis simple del cuero cabelludo (nivel de evidencia L5). Indicación original: Nafazolina"
monitor_inn: "naphazoline"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "primary hereditary glaucoma", "hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "open-angle glaucoma", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature"]
---

# Naphazoline
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

## Nafazolina: De Indicación Oftálmica (Descongestionante Conjuntival) a Hipotricosis Simple del Cuero Cabelludo
{: .text-alpha }

## Resumen en Una Frase

Nafazolina es un vasoconstrictor oftálmico de uso tópico, registrado en Colombia como solución oftálmica y utilizado habitualmente para aliviar el enrojecimiento ocular.
El modelo TxGNN predice que podría ser efectivo para **hipotricosis simple del cuero cabelludo**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Se trata de una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Nafazolina (el registro sanitario no detalla una indicación más específica; el uso conocido es el alivio del enrojecimiento ocular) |
| Nueva Indicación Predicha | Hipotricosis simple del cuero cabelludo |
| Puntaje de Predicción TxGNN | 0.9983 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 7) |
| Número de Registros Sanitarios | 8 (0 vigentes, 8 cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción detallado del fármaco. Según la información conocida, la nafazolina es un agonista adrenérgico (receptores alfa-1A, alfa-2A y alfa-2C) que produce vasoconstricción y reduce el enrojecimiento ocular al estrechar los vasos sanguíneos inflamados de la conjuntiva.

**La predicción no tiene respaldo mecanístico.** La hipotricosis simple del cuero cabelludo es un trastorno genético del folículo piloso. No existe un mecanismo plausible por el cual un vasoconstrictor tópico modifique ese defecto; en todo caso, la vasoconstricción tendería a reducir la perfusión del cuero cabelludo. El alto puntaje (0.9983) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

Otras predicciones del modelo siguen el mismo patrón. Alopecia, alopecia areata difusa e hipertricosis aparecen todas con puntajes muy altos, aunque el efecto esperado en el pelo sería opuesto (pérdida frente a exceso), lo que sugiere asociaciones inespecíficas. También figuran síndromes malformativos congénitos sin vínculo biológico alguno con el fármaco.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal.

Para la predicción de glaucoma de ángulo abierto (rank 8) existe una publicación vinculada (PMID [1295525](https://pubmed.ncbi.nlm.nih.gov/1295525/), 1992, *Australian and New Zealand Journal of Ophthalmology*). Estudia corticosteroides tópicos y sinequias anteriores periféricas tras trabeculoplastia láser, **no evalúa nafazolina**, por lo que no constituye evidencia directa.

---

## Información de Mercado en Colombia

Los 8 registros sanitarios están cancelados; no hay productos vigentes.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20177412 | DILAOFTAL® | Solución oftálmica | Nafazolina |
| 20211293 | BLUE-ZUL® Solución Oftálmica | Solución oftálmica | Nafazolina |
| 20242858 | OFTACLEAR® | Solución oftálmica | Nafazolina |
| 20217421 | Nafazolina Clorhidrato 1 mg/ml Solución Oftálmica | Solución oftálmica | Nafazolina |
| 20161178 | NAFOLINA® Solución Oftálmica | Solución oftálmica | Nafazolina |

*(Se muestran los 5 principales de 8 registros.)*

---

## Consideraciones de Seguridad

- **Contraindicaciones o condiciones de riesgo según el grafo de conocimiento** (no provienen del prospecto): hipertensión, hiperglucemia, diabetes mellitus, cetoacidosis diabética, glaucoma de ángulo cerrado, enfermedad cardiovascular, enfermedad cardíaca, hipertiroidismo, enfermedad de Graves, tirotoxicosis, infecciones oculares y conjuntivitis.
- **Perfil farmacológico**: actúa sobre los receptores adrenérgicos alfa-1A, alfa-2A y alfa-2C humanos. Estos datos describen sus dianas, no interacciones con otros fármacos.
- **Relevancia para las indicaciones predichas**: los simpaticomiméticos oftálmicos pueden afectar el tamaño pupilar y la dinámica del humor acuoso, y los productos con nafazolina llevan advertencias en glaucoma de ángulo cerrado. Para las predicciones de glaucoma esto representa una preocupación de seguridad, no una justificación terapéutica.

No se dispone de las advertencias y contraindicaciones del prospecto; consultar el prospecto para información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (L5), sin ensayos ni literatura, y carece de plausibilidad biológica. Además, no hay productos vigentes en Colombia y existen alertas de seguridad en patologías oculares y cardiovasculares.

**Para avanzar se necesita:**
- Una hipótesis mecanística creíble que vincule la vasoconstricción alfa-adrenérgica con el ciclo del folículo piloso (hoy inexistente)
- Datos preclínicos (modelos foliculares in vitro o in vivo) antes de plantear cualquier estudio clínico
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), que sigue pendiente
- Completar los datos del mecanismo de acción desde DrugBank
- Evaluar la viabilidad regulatoria y de vía de administración, dado que el medicamento está comercializado con 8 licencias vigentes y la única forma farmacéutica es oftálmica
- Considerar priorizar otros candidatos o indicaciones con mayor plausibilidad biológica
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

