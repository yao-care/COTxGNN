---
layout: default
title: Alverine
parent: Solo Predicción del Modelo (L5)
nav_order: 43
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-31
description: "Alverine: nueva indicación predicha, Trastorno distímico (nivel de evidencia L5). Indicación original: Alverina combinaciones"
monitor_inn: "alverine"
predicted_indications: ["dysthymic disorder", "neurotic disorder", "anxiety disorder", "migraine disorder", "neurotic depression", "melancholia", "benign paroxysmal torticollis of infancy", "agoraphobia", "congenital isolated adrenocorticotropic hormone deficiency (disease)"]
---

# Alverine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Alverina: De Combinaciones de Alverina (Antiespasmódico) a Trastorno Distímico
{: .text-alpha }

## Resumen en Una Frase

Alverina es un relajante del músculo liso, registrado en Colombia bajo la indicación "Alverina combinaciones" y usado en otros países para el alivio sintomático de trastornos gastrointestinales con espasmo.
El modelo TxGNN predice que podría ser efectivo para **trastorno distímico**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción específica.
La evidencia indirecta más cercana es un estudio preclínico en ratones sobre ansiedad, una indicación predicha distinta.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Alverina combinaciones |
| Nueva Indicación Predicha | Trastorno distímico |
| Puntaje de Predicción TxGNN | 0.9983 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 2) |
| Número de Registros Sanitarios | al menos 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de alverina en los datos compilados para este informe. Se sabe que es un relajante del músculo liso, y se ha descrito actividad antagonista sobre el receptor 5-HT1A, aunque esto último no está respaldado por los datos suministrados. Como dato farmacológico, se registra una interacción con el factor nuclear de hepatocitos 4-alfa (HNF4A), sin relevancia clínica establecida.

La relación entre la indicación original (espasmo gastrointestinal) y el trastorno distímico no es directa. La hipótesis es que la modulación serotoninérgica podría influir en la regulación del ánimo. Esta idea es plausible, pero no está demostrada y el puntaje de 0.9983 es una predicción computacional.

Otras predicciones del modelo tienen algo más de apoyo indirecto, por lo que conviene considerarlas como alternativas de investigación:

| Indicación predicha | Puntaje TxGNN | Nivel | Evidencia disponible |
|------|------|------|------|
| Trastorno de ansiedad | 0.9945 | L4 | Un estudio preclínico en ratones (2014) |
| Depresión neurótica | 0.9916 | L4 | Un estudio computacional de reposicionamiento (2018) |
| Melancolía | 0.9914 | L4 | El mismo estudio computacional (2018), sin corroboración independiente |

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para trastorno distímico.

Como referencia indirecta, para otras indicaciones predichas existen:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [25199966](https://pubmed.ncbi.nlm.nih.gov/25199966/) | 2014 | Preclínico (modelo animal) | European Journal of Pharmacology | El citrato de alverina mostró efectos de tipo ansiolítico en modelos de ansiedad en ratones, coherente con un mecanismo serotoninérgico (5-HT1A). Relacionado con trastorno de ansiedad. |
| [30087074](https://pubmed.ncbi.nlm.nih.gov/30087074/) | 2018 | Estudio computacional | European Neuropsychopharmacology | Estrategia de reposicionamiento basada en redes para descubrir posibles antidepresivos. Indirecto; no se pueden confirmar hallazgos específicos de alverina. Relacionado con depresión neurótica y melancolía. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20152358 | AVARIN | Cápsula blanda | Alverina combinaciones | Vigente |
| 20070928 | METEOSPASMYL® CÁPSULAS BLANDAS | Cápsula blanda | Alverina combinaciones | Vigente |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: Se registra una interacción de tipo farmacológico con el factor nuclear de hepatocitos 4-alfa (HNF4A). No tiene nivel de gravedad asignado ni relevancia clínica establecida.

Consultar el prospecto para información sobre advertencias y contraindicaciones.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para trastorno distímico se basa únicamente en el modelo (L5), sin ensayos ni literatura. Además, los dos registros sanitarios en Colombia están cancelados y faltan datos de seguridad y de mecanismo de acción.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de alverina (advertencias y contraindicaciones).
- Confirmar el mecanismo de acción, en particular la actividad sobre 5-HT1A.
- Evaluar si las indicaciones con algo de respaldo indirecto (ansiedad, depresión) son mejores candidatas que el trastorno distímico.
- Generar evidencia preclínica y clínica específica en trastornos del ánimo.
- Aclarar el estado regulatorio actual en Colombia, dado que no hay registros vigentes.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

