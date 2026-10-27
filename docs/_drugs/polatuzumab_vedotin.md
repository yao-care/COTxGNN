---
layout: default
title: Polatuzumab Vedotin
parent: Solo Predicción del Modelo (L5)
nav_order: 521
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Polatuzumab Vedotin: nueva indicación predicha, Carcinoma de mama HER2 positivo (nivel de evidencia L5). Indicación original: No especificada en el registro"
monitor_inn: "polatuzumab vedotin"
predicted_indications: ["HER2 positive breast carcinoma"]
---

# Polatuzumab Vedotin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Polatuzumab vedotin: De Indicación Original No Especificada a Carcinoma de Mama HER2 Positivo
{: .text-alpha }

## Resumen en Una Frase

Polatuzumab vedotin (marca POLIVY®) es un conjugado anticuerpo-fármaco registrado en Colombia, aunque el registro sanitario disponible no detalla su indicación original.
El modelo TxGNN predice que podría ser efectivo para **carcinoma de mama HER2 positivo**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto registrado solo repite el nombre del principio activo) |
| Nueva Indicación Predicha | Carcinoma de mama HER2 positivo |
| Puntaje de Predicción TxGNN | 99.34% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Polatuzumab vedotin es un conjugado anticuerpo-fármaco que se dirige a CD79b, un componente del receptor de células B, y libera el agente que interrumpe los microtúbulos monometil auristatina E (MMAE). Los datos compilados para este informe no incluyen el mecanismo de acción detallado, por lo que esta descripción se basa en conocimiento general del fármaco y no puede verificarse con los datos suministrados.

La relación con la nueva indicación es débil. CD79b no es un blanco reconocido en el carcinoma de mama HER2 positivo, por lo que el alto puntaje de TxGNN (0.993) debe interpretarse solo como una predicción computacional. Un posible vínculo indirecto es que el MMAE se utiliza como carga citotóxica en otros conjugados anticuerpo-fármaco, y que las células de cáncer de mama son sensibles a agentes que actúan sobre los microtúbulos. Sin embargo, esto no respalda un mecanismo dirigido por CD79b.

No se aportó evidencia preclínica ni clínica que apoye la hipótesis, y la similitud con la indicación original queda pendiente de evaluación.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20167788 (cancelado) | POLIVY® | Polvo liofilizado para reconstituir a solución inyectable | POLATUZUMAB VEDOTIN |

El único registro sanitario existente figura como cancelado (fabricante: F. Hoffmann-La Roche Ltd.), por lo que actualmente no hay registros vigentes.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Conjugado anticuerpo-fármaco con carga citotóxica (MMAE, inhibidor de microtúbulos) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar el prospecto; en general, hemograma completo y función hepática |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

**Interacciones Farmacológicas:** se identificaron 131 interacciones potenciales. Entre las de nivel **Mayor** se encuentran:
- Claritromicina
- Cobicistat
- Deferiprona
- Samario (153Sm) lexidronam

Entre las de nivel **Moderado** se encuentran aprepitant, cimetidina, naltrexona, metronidazol, miconazol, rosuvastatina, simvastatina, tinidazol, clotrimazol, estroncio-89, ticagrelor, cloroquina, disulfiram, secnidazol, hidroxicloroquina y benznidazol.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (nivel L5), sin ensayos clínicos ni literatura. Además, el mecanismo dirigido a CD79b no se corresponde con el carcinoma de mama HER2 positivo y el registro sanitario local está cancelado.

**Para avanzar se necesita:**
- Datos del mecanismo de acción desde DrugBank
- Prospecto de INVIMA con advertencias y contraindicaciones
- Evidencia preclínica que explore la actividad en líneas celulares de cáncer de mama HER2 positivo
- Revisión de literatura y de ensayos clínicos sobre conjugados con MMAE en cáncer de mama
- Aclarar la indicación original y la situación regulatoria del registro cancelado
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

