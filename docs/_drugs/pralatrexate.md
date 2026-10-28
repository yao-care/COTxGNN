---
layout: default
title: Pralatrexate
parent: Solo Predicción del Modelo (L5)
nav_order: 526
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "Pralatrexate"
predicted_indications: ["pleural adenomatoid tumor", "relapsing-remitting multiple sclerosis", "pleural biphasic mesothelioma", "pleural epithelioid mesothelioma", "lymphohistiocytoid mesothelioma", "pericardium cancer", "pleural sarcomatoid mesothelioma", "malignant peritoneal mesothelioma", "well differentiated papillary mesothelioma", "pleural mesothelioma"]
description: "Pralatrexate: nueva indicación predicha, Pleural adenomatoid tumor (nivel de evidencia L5). Indicación original: PRALATREXATO"
---

# Pralatrexate
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

## Pralatrexate: Pleural adenomatoid tumor
{: .text-alpha }

## Resumen en Una Frase

Pralatrexato es un antifolato citotóxico que inhibe la enzima dihidrofolato reductasa (DHFR). En Colombia contó con un registro sanitario, hoy cancelado, cuyo texto de indicación solo dice "PRALATREXATO". En el ámbito internacional se usa para el linfoma periférico de células T en recaída o refractario.
El modelo TxGNN predice que podría ser efectivo para **tumor adenomatoide pleural**, pero sin **ningún ensayo clínico** ni **publicación** que respalde esta predicción específica (nivel de evidencia L5).

> **Nota importante:** la primera predicción (tumor adenomatoide pleural) es una lesión benigna y el puntaje alto probablemente refleja cercanía en la red de conocimiento con el mesotelioma, no una señal terapéutica real. Las indicaciones con mayor respaldo son **mesotelioma pleural** y **mesotelioma pleural epitelioide**, descritas en las secciones de evidencia.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | PRALATREXATO |
| Nueva Indicación Predicha | Pleural adenomatoid tumor |
| Puntaje de Predicción TxGNN | 0.9991 |
| Nivel de Evidencia | L5 (para la predicción principal). Las predicciones de mesotelioma pleural y mesotelioma pleural epitelioide alcanzan L3 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este reporte. Según la información conocida, pralatrexato es un análogo del folato que inhibe la DHFR, se internaliza eficientemente a través del transportador RFC-1 y bloquea la síntesis de ADN en células de división rápida. Su eficacia está comprobada en linfoma periférico de células T.

Para el **tumor adenomatoide pleural**, no hay evidencia directa. Se trata de una lesión benigna de origen mesotelial, y la terapia citotóxica no es racional en un tumor benigno. El puntaje alto del modelo probablemente se debe a la proximidad en la red con el mesotelioma, no a una señal terapéutica verdadera.

Distinto es el caso del mesotelioma. Otros antifolatos, como pemetrexed, son tratamiento establecido en mesotelioma epitelioide, lo que da una justificación sólida a nivel de clase. Además, existe un ensayo de Fase II de pralatrexato en mesotelioma pleural maligno irresecable. Esta es la línea de investigación más prometedora entre las predicciones, aunque los datos disponibles no incluyen los resultados de eficacia.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para la indicación predicha principal (tumor adenomatoide pleural), ni para ninguna de las otras 9 indicaciones predichas.

---

## Evidencia de Literatura

Para la indicación principal (tumor adenomatoide pleural) actualmente no hay literatura relacionada disponible. La literatura más relevante corresponde a las predicciones de mesotelioma:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [17409804](https://pubmed.ncbi.nlm.nih.gov/17409804/) | 2007 | Ensayo Fase II | J Thorac Oncol | Pralatrexato en mesotelioma pleural maligno irresecable. El resumen indica que el mesotelioma responde a antifolatos, que pralatrexato tiene un perfil de toxicidad favorable (principalmente estomatitis) y que mostró actividad antitumoral en líneas celulares y xenoinjertos. Los resultados de eficacia no están en los datos disponibles |
| [21301589](https://pubmed.ncbi.nlm.nih.gov/21301589/) | 2010 | Revisión | Cancer Manag Res | Revisión sobre quimioterapia dirigida a la síntesis de folatos; respalda la justificación mecanística de los antifolatos |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20055048 (cancelado) | DIFOLTA 20 MG/ML SOLUCIÓN PARA INFUSIÓN (BIOSIDUS COLOMBIA S.A.S.) | Solución inyectable | PRALATREXATO |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (antifolato, inhibidor de DHFR) |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial, función renal y hepática, y vigilancia de mucositis/estomatitis |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

- **Contraindicaciones o condiciones de riesgo (según el grafo de conocimiento TxGNN, no texto de prospecto):** trombocitopenia, neutropenia, agranulocitosis, anemia, anemia macrocítica, función renal deteriorada y estomatitis.
- **Interacciones farmacológicas:** solo se identificó la interacción farmacológica con su diana, la dihidrofolato reductasa (DHFR), sin nivel de gravedad clínica. No hay interacciones con otros fármacos.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal (tumor adenomatoide pleural) carece de evidencia y es poco racional para una lesión benigna, dada la toxicidad del fármaco (mielosupresión, mucositis). El registro sanitario colombiano está cancelado, lo que supone otra barrera práctica. Las indicaciones de mesotelioma pleural y pleural epitelioide (L3) son mejores candidatas a pregunta de investigación, pero no a decisión de avance.

**Para avanzar se necesita:**
- Obtener los resultados de eficacia y seguridad del ensayo de Fase II (PMID 17409804) y, si es posible, un desglose por histología epitelioide
- Reorientar la evaluación hacia mesotelioma pleural/epitelioide, comparando con pemetrexed como estándar
- Descargar y analizar el prospecto en INVIMA para completar advertencias y contraindicaciones
- Consultar DrugBank para completar el mecanismo de acción
- Evaluar la viabilidad de acceso al fármaco en Colombia, dado que no hay registro vigente
- Verificar la compatibilidad de vía de administración (pendiente)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

