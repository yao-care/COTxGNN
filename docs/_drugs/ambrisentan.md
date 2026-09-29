---
layout: default
title: Ambrisentan
parent: Solo Predicción del Modelo (L5)
nav_order: 41
evidence_level: L5
indication_count: 10
---

# Ambrisentan
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

# Ambrisentán: De Hipertensión Arterial Pulmonar a Malformación Arteriovenosa Pulmonar

## Resumen en Una Frase

Ambrisentán es un antagonista selectivo del receptor de endotelina tipo A, comercializado para la hipertensión arterial pulmonar (HAP).
El modelo TxGNN predice que podría ser efectivo para la **malformación arteriovenosa pulmonar**,
pero hay **0 ensayos clínicos** y solo **1 publicación** (un reporte de caso que trata la HAP como comorbilidad, no la malformación). La predicción se apoya casi solo en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial pulmonar. El texto de INVIMA solo consigna el nombre del principio activo ("AMBRISENTAN"). |
| Nueva Indicación Predicha | Malformación arteriovenosa pulmonar |
| Puntaje de Predicción TxGNN | 99.41% |
| Nivel de Evidencia | L4 (según el Evidence Pack; sin estudios preclínicos ni de mecanismo, solo un reporte de caso tangencial) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la fuente. Por farmacología general, ambrisentán bloquea el receptor de endotelina A (ETA), lo que reduce la vasoconstricción y el remodelado vascular en la HAP. Su eficacia en HAP está comprobada.

Las malformaciones arteriovenosas pulmonares son cortocircuitos estructurales, típicamente asociados a telangiectasia hemorrágica hereditaria (THH). La terapia vasodilatadora o antiproliferativa de la HAP no es un tratamiento establecido para ellas. El único indicio es un reporte de caso de HAP en un paciente con THH. Ese caso trata la HAP como comorbilidad y no la malformación en sí.

El alto puntaje de TxGNN es una predicción basada en grafos de conocimiento y no equivale a evidencia clínica. Por ahora el vínculo mecanístico con esta indicación es débil.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33969094](https://pubmed.ncbi.nlm.nih.gov/33969094/) | 2021 | Reporte de caso | World J Clin Cases | Paciente con telangiectasia hemorrágica hereditaria (THH) que presentó HAP; se describen manifestaciones, tratamiento y análisis genético familiar para crear conciencia sobre esta multimorbilidad poco frecuente y de mal pronóstico. |

## Información de Mercado en Colombia

Hay 20 registros en total. Los 5 primeros corresponden al mismo registro sanitario, por lo que se muestra una sola vez.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20151854 | XETAM® 5 MG TABLETAS RECUBIERTAS (XINETIX PHARMA S.A.S.) | Tableta recubierta | Solo consigna el principio activo: AMBRISENTAN |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: no se encontraron interacciones en la fuente consultada (0 registros). Esto podría ser una limitación de los datos y no ausencia real de interacciones.
- **Nota de riesgo**: el análisis del Evidence Pack indica que ambrisentán tiene una advertencia de toxicidad embriofetal. Los ARE (antagonistas de receptores de endotelina) también pueden empeorar la anemia y la retención de líquidos.

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ensayos clínicos y solo un reporte de caso tangencial. No hay un mecanismo terapéutico establecido para las malformaciones arteriovenosas pulmonares, por lo que el puntaje de TxGNN por sí solo no basta para avanzar.

Para el mismo fármaco, el Evidence Pack contiene candidatas mejor respaldadas: HAP asociada a cardiopatía congénita y HAP asociada a enfermedad del tejido conectivo (ambas L2, "Proceed with Guardrails"). Conviene priorizarlas.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank
- Advertencias y contraindicaciones del prospecto de INVIMA
- Evidencia preclínica o clínica que vincule el bloqueo de ETA con el tratamiento de la malformación arteriovenosa pulmonar (por ejemplo, en pacientes con THH)
- Evaluación de seguridad, incluida la toxicidad embriofetal

*Este informe es solo para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su uso.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

