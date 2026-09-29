---
layout: default
title: Dutasteride
parent: Solo Predicción del Modelo (L5)
nav_order: 171
evidence_level: L5
indication_count: 10
---

# Dutasteride
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Dutasterida: De Hiperplasia Prostática Benigna a Hipertricosis Universal Congénita Tipo Ambras

## Resumen en Una Frase

Dutasterida es un inhibidor de la 5-alfa reductasa que se usa clínicamente para la hiperplasia prostática benigna. El texto de indicación en los registros de Colombia solo dice "DUTASTERIDA", así que esta indicación proviene del conocimiento farmacológico general y no de los datos del registro.
El modelo TxGNN predice que podría ser efectivo para **hipertricosis universal congénita tipo Ambras**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto dice solo "DUTASTERIDA"); por conocimiento general, hiperplasia prostática benigna |
| Nueva Indicación Predicha | Hipertricosis universal congénita tipo Ambras |
| Puntaje de Predicción TxGNN | 99.998% (posición 59) |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

No hay datos del mecanismo de acción (MOA) en el paquete de evidencia. Según el conocimiento farmacológico general, la dutasterida inhibe la 5-alfa reductasa de tipos 1 y 2, lo que reduce la dihidrotestosterona (DHT). Por esa reducción de DHT también se usa para conservar el cabello en la alopecia androgenética.

La relación con la nueva indicación es débil. El síndrome de Ambras es una condición congénita ligada a un reordenamiento cromosómico en 8q22 que altera la regulación del gen *TRPS1*, y no depende principalmente de la DHT. Como la dutasterida ayuda a retener cabello en el cuero cabelludo, ni siquiera está claro en qué dirección podría actuar sobre un exceso de vello. Hoy no existe un mecanismo plausible establecido.

Por lo tanto, el puntaje alto del modelo debe leerse con cautela. Podría reflejar asociaciones del grafo de conocimiento (por ejemplo, entre fármacos y enfermedades del folículo piloso) y no un vínculo biológico real.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20128081 | DUTASVITAE® 0.5 MG cápsulas blandas (GALENICUM HEALTH COLOMBIA S.A.S.) | Cápsula blanda | Solo figura "DUTASTERIDA" (sin texto de indicación) |

Los datos devuelven este mismo registro repetido varias veces. Se muestra una sola vez. El total reportado es de 20 registros sanitarios, con formas de cápsula blanda y cápsula dura.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción está en nivel L5, sin ensayos ni publicaciones, y el mecanismo conocido no explica un beneficio en la hipertricosis de Ambras. Tampoco hay datos de seguridad locales, por lo que no se puede pasar a una evaluación de seguridad.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA para obtener advertencias y contraindicaciones (brecha bloqueante).
- Confirmar el mecanismo de acción desde DrugBank y analizar si hay un vínculo real con la vía de *TRPS1* o con el folículo piloso.
- Hacer una búsqueda de literatura dirigida a dutasterida e hipertricosis. Las 20 publicaciones recuperadas para la predicción de malformación con componente periodontal tratan de periodontitis en general y ninguna menciona dutasterida, por lo que no aportan evidencia.
- Priorizar, si se quiere explorar el tema, la predicción de **hipotricosis simple del cuero cabelludo** (clasificada como pregunta de investigación). Tiene mayor plausibilidad parcial por el uso de dutasterida en alopecia androgenética, aunque sigue sin ensayos ni literatura.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su uso.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

