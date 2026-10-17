---
layout: default
title: Obinutuzumab
parent: Solo Predicción del Modelo (L5)
nav_order: 475
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Obinutuzumab: nueva indicación predicha, Leucemia linfocítica crónica/linfoma linfocítico de células pequeñas… (nivel de evidencia L5). Indicación original: No especificada de forma útil"
monitor_inn: "OBINUTUZUMAB"
predicted_indications: ["follicular lymphoma"]
---

# Obinutuzumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Obinutuzumab: De una Indicación No Especificada en el Registro a Leucemia Linfocítica Crónica/Linfoma Linfocítico de Células Pequeñas (subtipo con hipermutación somática de IGHV)

## Resumen en Una Frase

Obinutuzumab es un anticuerpo monoclonal anti-CD20 usado en neoplasias de células B. En Colombia, el texto de indicación de su registro solo repite el nombre del fármaco, por lo que no permite identificar la indicación original.
El modelo TxGNN predice que podría ser efectivo para **leucemia linfocítica crónica/linfoma linfocítico de células pequeñas con hipermutación somática del gen de la región variable de la cadena pesada de inmunoglobulina**. Para este subtipo **no hay ensayos clínicos ni publicaciones** en los datos compilados, así que la predicción no tiene respaldo clínico propio.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada de forma útil (el registro solo indica "obinutuzumab") |
| Nueva Indicación Predicha | Leucemia linfocítica crónica/linfoma linfocítico de células pequeñas con hipermutación somática de IGHV |
| Puntaje de Predicción TxGNN | 99.21% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según lo conocido, obinutuzumab es un anticuerpo anti-CD20 de tipo II glicoingeniería. Actúa por muerte celular directa, citotoxicidad celular dependiente de anticuerpos (ADCC) y fagocitosis celular dependiente de anticuerpos (ADCP) contra linfocitos B CD20 positivos.

Las células malignas de la leucemia linfocítica crónica/linfoma linfocítico de células pequeñas (LLC/LLCP) son linfocitos B que expresan CD20. Por eso, mecanísticamente, el tratamiento anti-CD20 es plausible.

Hay dos matices importantes:
- El puntaje de TxGNN es idéntico (99.21%) para este subtipo y para otro subtipo de LLC/LLCP (germinal previo). Esto sugiere que el modelo está asociando el fármaco con el nodo general de LLC/LLCP y no con información específica del subtipo.
- Obinutuzumab ya está establecido en LLC en general, por lo que este subtipo probablemente queda cubierto por la indicación más amplia. No debe interpretarse como un hallazgo nuevo de reposicionamiento.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para este subtipo específico.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para este subtipo específico.

---

## Otra Indicación Predicha con Evidencia: Linfoma Folicular

Entre las predicciones del modelo, el **linfoma folicular** (puntaje TxGNN 99.18%) es la que tiene respaldo clínico. Tiene nivel de evidencia **L1** y una recomendación preliminar de **Proceed with Guardrails**. Hay decenas de ensayos clínicos y 19 publicaciones. Se presentan los más relevantes:

| Referencia | Tipo / Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT05100862](https://clinicaltrials.gov/study/NCT05100862) | Fase 3 | Activo, sin reclutar | 799 | Zanubrutinib + anticuerpo anti-CD20 vs. lenalidomida + rituximab en linfoma folicular recaído/refractario |
| [NCT03817853](https://clinicaltrials.gov/study/NCT03817853) | Fase 4 | Completado | 114 | Seguridad de la infusión corta de obinutuzumab en linfoma folicular avanzado sin tratamiento previo |
| [NCT02871219](https://clinicaltrials.gov/study/NCT02871219) | Fase 2 | Completado | 96 | Obinutuzumab + lenalidomida en linfoma folicular sin tratamiento previo |
| [PMID 29856692](https://pubmed.ncbi.nlm.nih.gov/29856692/) (2018, ECA, J Clin Oncol) | GALLIUM | n/a | 1,202 | Obinutuzumab prolongó la supervivencia libre de progresión frente a rituximab con distintos esquemas de quimioterapia |
| [PMID 37404773](https://pubmed.ncbi.nlm.nih.gov/37404773/) (2023, ECA, HemaSphere) | GALLIUM, análisis final | n/a | n/a | Resultados finales de obinutuzumab vs. rituximab con inmunoquimioterapia en linfoma indolente sin tratamiento previo |
| [PMID 37506346](https://pubmed.ncbi.nlm.nih.gov/37506346/) (2023, ECA, J Clin Oncol) | ROSEWOOD, Fase 2 | n/a | n/a | Zanubrutinib + obinutuzumab vs. obinutuzumab solo en linfoma folicular recaído/refractario |

Como obinutuzumab ya es una terapia establecida en linfoma folicular, esta evidencia confirma un uso existente más que una señal nueva de reposicionamiento.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20065694 (cancelado) | GAZYVA® concentrado para solución para infusión 1000 mg/vial 40 ml (F. Hoffmann-La Roche Ltd.) | Solución concentrada para infusión | Solo figura "obinutuzumab" |

El estado "solo cancelado" debe verificarse, porque contrasta con el uso clínico vigente del fármaco.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Inmunoterapia (anticuerpo monoclonal anti-CD20), no citotóxico convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto (en general, para esta clase se vigilan neutropenia y trombocitopenia) |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal, vigilancia de reacciones a la infusión y de infecciones |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 81 interacciones en total. Entre las de nivel **mayor** están deferiprona, samario-153 lexidronam, adalimumab, baricitinib, certolizumab pegol, cladribina y clozapina. Entre las de nivel **moderado** están estroncio-89, roflumilast, cloranfenicol (incluido el oftálmico), zidovudina, alemtuzumab, anakinra, azatioprina, canakinumab y varias vacunas (toxoide tetánico, ántrax, cólera vivo). Muchas se relacionan con inmunosupresión y riesgo de infección.

No se dispone de advertencias ni contraindicaciones del prospecto en los datos compilados. Consultar el prospecto para información de seguridad adicional.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para este subtipo de LLC/LLCP solo existe la predicción del modelo (nivel L5), sin ensayos ni literatura propios. Además, la indicación probablemente ya está cubierta por el uso establecido de obinutuzumab en LLC, de modo que no constituye una señal real de reposicionamiento.

**Para avanzar se necesita:**
- Aclarar la indicación original, porque el registro solo repite el nombre del fármaco.
- Verificar el estado de mercado en Colombia, pues el único registro figura como cancelado.
- Obtener el prospecto de INVIMA con advertencias y contraindicaciones, y los datos del mecanismo de acción (DrugBank).
- Evaluar la indicación de linfoma folicular (nivel L1), que sí tiene evidencia clínica sólida, como candidata a "Proceed with Guardrails". Esto requiere confirmar la indicación aprobada y la línea de tratamiento frente a la etiqueta vigente, y revisar la carga de interacciones (81) y los riesgos de reacciones a la infusión e infecciones.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

