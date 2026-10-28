---
layout: default
title: Rasburicase
parent: Solo Predicción del Modelo (L5)
nav_order: 551
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Rasburicase: nueva indicación predicha, Hipouricemia renal (nivel de evidencia L5). Indicación original: RASBURICASA"
monitor_inn: "rasburicase"
predicted_indications: ["hypouricemia, renal", "hypoxanthine guanine phosphoribosyltransferase partial deficiency", "hepatic porphyria", "idiopathic copper-associated cirrhosis", "early-onset familial noncirrhotic portal hypertension", "primitive portal vein thrombosis", "hepatopulmonary syndrome", "hepatoportal sclerosis", "renal tubular acidosis", "disorder of phenylalanine metabolism"]
---

# Rasburicase
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

## Rasburicasa: De Rasburicasa (indicación sin detallar) a Hipouricemia Renal
{: .text-alpha }

## Resumen en Una Frase

Rasburicasa es una enzima urato oxidasa recombinante, registrada en Colombia bajo el nombre FASTURTEC®, cuyo texto de indicación aprobada solo consigna "RASBURICASA".
El modelo TxGNN predice que podría ser efectivo para **hipouricemia renal**, pero actualmente no hay **ningún ensayo clínico** ni **publicación** que respalde esta dirección, y el análisis mecanístico sugiere que la predicción es contraproducente.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | RASBURICASA (el registro no detalla la indicación clínica) |
| Nueva Indicación Predicha | Hipouricemia renal |
| Puntaje de Predicción TxGNN | 0.9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la rasburicasa es una urato oxidasa recombinante que convierte el ácido úrico en alantoína, lo que reduce el nivel de urato en sangre. Se usa en situaciones de hiperuricemia aguda.

En el caso de la hipouricemia renal, la relación con la indicación original es **inversa**. Esta condición se caracteriza por niveles anormalmente bajos de ácido úrico en suero (por ejemplo, por pérdida de función de URAT1 o GLUT9). Reducir aún más el urato sería mecanísticamente contraproducente y podría empeorar el fenotipo.

Por lo tanto, el puntaje alto del modelo (TxGNN, aprendizaje profundo) puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas con el urato, y no una justificación terapéutica real. Esta predicción no debe interpretarse como una señal de eficacia.

### Otras predicciones del modelo

Las demás predicciones de mayor puntaje también tienen nivel de evidencia L5 y recomendación Hold:

| Enfermedad predicha | Puntaje TxGNN | Comentario sobre el mecanismo |
|------|------|------|
| Deficiencia parcial de hipoxantina-guanina fosforribosiltransferasa | 0.9997 | Plausible solo en crisis hiperuricémicas agudas; el manejo crónico usa inhibidores de xantina oxidasa |
| Porfiria hepática | 0.9997 | Sin vínculo mecanístico claro; la puntuación proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes aprendidas entre enfermedades relacionadas, no evidencia biológica |
| Cirrosis idiopática asociada a cobre | 0.9997 | Sin vínculo identificado |
| Hipertensión portal familiar no cirrótica de inicio temprano | 0.9997 | Sin mecanismo plausible |
| Trombosis primitiva de la vena porta | 0.9997 | Sin actividad antitrombótica conocida |
| Síndrome hepatopulmonar | 0.9997 | Sin vía conocida |
| Esclerosis hepatoportal | 0.9997 | Sin vínculo mecanístico |
| Acidosis tubular renal | 0.9985 | Conexión tangencial no respaldada |
| Trastorno del metabolismo de la fenilalanina | 0.9983 | Sin actividad sobre esta vía |

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
| 20060952 (cancelado) | FASTURTEC® 1.5 MG / ML | Polvo liofilizado para reconstituir a solución inyectable | RASBURICASA |

El producto fue fabricado por Sanofi-Aventis de Colombia S.A. y su registro está cancelado, por lo que actualmente no hay presentaciones vigentes en el mercado colombiano.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 13 interacciones en la consulta realizada.
  - **Mayores**: prilocaína y ácido nitroso.
  - **Moderadas**: anestésicos locales (tetracaína tópica y oftálmica, lidocaína tópica y oftálmica, benzocaína, cocaína tópica y nasal, proparacaína, oxibuprocaína, cinchocaína) e idelalisib.
- **Consideración adicional (del análisis mecanístico)**: se señala que la rasburicasa está contraindicada en deficiencia de G6PD y que es una enzima intravenosa inmunogénica. Este punto debe verificarse con el prospecto oficial.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción carece de ensayos clínicos y literatura (nivel L5), y el mecanismo de acción de la rasburicasa (reducir el ácido úrico) va en contra de lo que requeriría la hipouricemia renal. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Datos del mecanismo de acción confirmados desde fuentes oficiales.
- Prospecto oficial con advertencias y contraindicaciones, que no está disponible y es un vacío bloqueante para el cribado de seguridad.
- Evaluación de si alguna otra predicción (por ejemplo, crisis hiperuricémicas agudas en la deficiencia parcial de HPRT) tiene un fundamento clínico más coherente.
- Revisión del estado regulatorio en Colombia, dado que el registro está cancelado.
- Evidencia preclínica o clínica que justifique cualquier nueva indicación antes de reconsiderar la decisión.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

