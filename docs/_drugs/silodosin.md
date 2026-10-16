---
layout: default
title: Silodosin
parent: Solo Predicción del Modelo (L5)
nav_order: 586
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Silodosin: nueva indicación predicha, Hipertricosis universal congénita tipo Ambras (nivel de evidencia L5). Indicación original: SILODOSINA"
monitor_inn: "Silodosin"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial isolated trichomegaly"]
---

# Silodosin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Silodosina: De Silodosina (indicación registrada sin detalle) a Hipertricosis universal congénita tipo Ambras

## Resumen en Una Frase

Silodosina es un antagonista selectivo de los receptores alfa-1A adrenérgicos, utilizado clínicamente para mejorar el flujo urinario en pacientes con hiperplasia prostática benigna (HPB).
El modelo TxGNN predice que podría ser efectivo para **hipertricosis universal congénita tipo Ambras**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | SILODOSINA (el registro sanitario no detalla la indicación; el uso clínico conocido es la HPB) |
| Nueva Indicación Predicha | Hipertricosis universal congénita tipo Ambras |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información farmacológica conocida, la silodosina se une de forma selectiva a los receptores adrenérgicos alfa-1A (con interacciones también registradas con los subtipos alfa-1B y alfa-1D), y su eficacia se ha establecido en el alivio de los síntomas urinarios de la HPB.

Sin embargo, no existe un mecanismo establecido que relacione el bloqueo alfa-1A con el síndrome de Ambras, un trastorno genético causado por reordenamientos cromosómicos que afectan regiones reguladoras del gen TRPS1. La relación entre la indicación original (síntomas del tracto urinario inferior) y la nueva indicación (alteración genética del crecimiento del vello) es débil.

El puntaje elevado del modelo (0.9999) refleja probablemente la proximidad en el grafo de conocimiento con nodos de fenotipos relacionados con el cabello, y no una justificación farmacológica. Debe interpretarse como una hipótesis sin respaldo, no como una señal de eficacia.

Otras predicciones del modelo siguen el mismo patrón: hipertricosis (99.99%), síndrome malformativo con componente dental o periodontal (99.99%), síndrome con malformación de Dandy-Walker (99.98%), anomalía genética aislada del tallo piloso (99.98%) y tricomegalia aislada familiar (99.23%). Ninguna cuenta con ensayos clínicos ni literatura.

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
| 20070804 | SILOTRIF® 4 MG CÁPSULAS (MSN Laboratories Private Limited) – **cancelado** | Cápsula dura | SILODOSINA |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** síndrome de atrofia multisistémica, síndrome de taquicardia ortostática postural, hipotensión ortostática, insuficiencia hepática, enfermedad renal, piouréter y síndrome de iris flácido intraoperatorio.
- **Interacciones farmacológicas:** la consulta se completó y devolvió 3 registros, todos de farmacología de dianas (receptores adrenérgicos alfa-1A, alfa-1B y alfa-1D), no interacciones con otros fármacos. No se identificaron interacciones clínicas específicas con otros medicamentos.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos, sin literatura y sin un mecanismo plausible que vincule el bloqueo alfa-1A con el síndrome de Ambras. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones oficiales), actualmente un bloqueo para la evaluación de seguridad.
- Completar los datos de mecanismo de acción desde DrugBank.
- Establecer una hipótesis biológica que conecte el bloqueo alfa-1A con la vía TRPS1 o con el crecimiento del vello.
- Realizar estudios preclínicos (in vitro o en modelos animales) antes de considerar un estudio clínico.
- Evaluar la viabilidad regulatoria y comercial, dado que no hay registro vigente en Colombia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

