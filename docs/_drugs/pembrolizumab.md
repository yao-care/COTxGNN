---
layout: default
title: Pembrolizumab
parent: Solo Predicción del Modelo (L5)
nav_order: 319
evidence_level: L5
indication_count: 10
---

# Pembrolizumab
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

# Pembrolizumab: De Indicación Oncológica (no detallada en el registro) a Fibromatosis Gingival

## Resumen en Una Frase

Pembrolizumab (Keytruda®) es un anticuerpo monoclonal que se comercializa en Colombia. El registro sanitario solo indica el nombre del principio activo y no detalla la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **fibromatosis gingival**, con **0 ensayos clínicos** y **0 publicaciones** que respalden actualmente esta dirección. Es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el texto del registro solo dice "PEMBROLIZUMAB") |
| Nueva Indicación Predicha | Fibromatosis gingival |
| Puntaje de Predicción TxGNN | 99.40% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 4 (todos corresponden al mismo número de registro, 20085509) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la literatura recuperada para otras predicciones del mismo fármaco, pembrolizumab es un anticuerpo anti-PD-1 que restaura la actividad antitumoral de los linfocitos T. Su eficacia está comprobada en cáncer de pulmón no microcítico y otros tumores malignos.

La fibromatosis gingival es un sobrecrecimiento fibrótico de la encía. No hay una relación con la vía PD-1 respaldada por los datos disponibles. El puntaje alto (0.994) refleja solo la cercanía en el grafo de conocimiento del modelo, no una razón biológica demostrada. Sin datos de mecanismo de acción no es posible evaluar la plausibilidad mecanística, y la similitud con la indicación original queda pendiente de análisis.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Los cuatro registros del paquete de evidencia son idénticos, por lo que se muestran una sola vez.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20085509 | KEYTRUDA® 100 MG (MERCK SHARP & DOHME CORP.) | Solución inyectable | PEMBROLIZUMAB (el texto no detalla la indicación) |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Inmunoterapia (anticuerpo monoclonal anti-PD-1) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos ni publicaciones para esta indicación, y no hay una razón mecanística que la respalde. El puntaje del modelo es la única evidencia (L5), por lo que no justifica avanzar.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA con advertencias y contraindicaciones, y el texto completo de la indicación aprobada.
- Obtener datos del mecanismo de acción desde DrugBank.
- Encontrar alguna evidencia preclínica o clínica que vincule PD-1 con la fibromatosis gingival. Si no aparece, descartar la candidatura.
- Priorizar otras predicciones del mismo fármaco, como el carcinoma del hilio pulmonar (nivel L4). Tienen una relación mecanística más plausible con la indicación oncológica conocida.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

