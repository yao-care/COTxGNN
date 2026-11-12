---
layout: default
title: Laronidase
parent: Solo Predicción del Modelo (L5)
nav_order: 381
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
monitor_inn: "laronidase"
predicted_indications: ["Sanfilippo syndrome"]
description: "Laronidase: nueva indicación predicha, Síndrome de Sanfilippo (Sanfilippo syndrome) (nivel de evidencia L5). Indicación original: LARONIDASA"
---

# Laronidase
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

## Laronidase: Síndrome de Sanfilippo (Sanfilippo syndrome)
{: .text-alpha }

## Resumen en Una Frase

Laronidasa es una terapia de reemplazo enzimático basada en alfa-L-iduronidasa recombinante, comercializada actualmente en Colombia.
El modelo TxGNN predice que podría ser efectiva para el **síndrome de Sanfilippo (Sanfilippo syndrome)**, pero la evidencia es débil: **0 ensayos clínicos** y **8 publicaciones**, ninguna de las cuales estudia directamente esta enfermedad.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | LARONIDASA |
| Nueva Indicación Predicha | Síndrome de Sanfilippo (Sanfilippo syndrome) |
| Puntaje de Predicción TxGNN | 0.9922 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la literatura consultada, laronidasa es una enzima alfa-L-iduronidasa recombinante que se administra por vía intravenosa para reemplazar la enzima deficiente en la enfermedad para la que se desarrolló.

El síndrome de Sanfilippo (mucopolisacaridosis tipo III) y esa enfermedad comparten la acumulación de heparán sulfato. Esto probablemente explica el puntaje alto del modelo.

Sin embargo, esta relación es débil desde el punto de vista mecanístico:
- El síndrome de Sanfilippo se debe a la deficiencia de otras enzimas de la degradación del heparán sulfato (SGSH, NAGLU, HGSNAT o GNS), no de alfa-L-iduronidasa. Por eso laronidasa no repone la enzima que falta, y compartir el sustrato no implica que pueda eliminar los intermediarios bloqueados propios de esta enfermedad.
- El síndrome de Sanfilippo se caracteriza sobre todo por compromiso del sistema nervioso central, y las enzimas administradas por vía intravenosa no atraviesan la barrera hematoencefálica de forma apreciable.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Todas las publicaciones disponibles se refieren a otra mucopolisacaridosis (tipo I) o a modelos celulares. Ninguna aporta evidencia directa en síndrome de Sanfilippo.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [15126990](https://pubmed.ncbi.nlm.nih.gov/15126990/) | 2004 | ECA | The Journal of Pediatrics | Estudio multinacional, doble ciego y controlado con placebo que confirmó la eficacia y seguridad de laronidasa en mucopolisacaridosis tipo I. Evidencia indirecta para Sanfilippo. |
| [40830667](https://pubmed.ncbi.nlm.nih.gov/40830667/) | 2025 | ECA (fase III, cruzado) | Scientific Reports | Compara una laronidasa biosimilar con la de referencia para mantener los glicosaminoglicanos urinarios en mucopolisacaridosis tipo I. Evidencia indirecta. |
| [32340185](https://pubmed.ncbi.nlm.nih.gov/32340185/) | 2020 | Revisión | International Journal of Molecular Sciences | Resume la efectividad y las limitaciones de la terapia de reemplazo enzimático intravenosa en varias mucopolisacaridosis. Los datos posteriores a la comercialización son a veces contradictorios. |
| [31020996](https://pubmed.ncbi.nlm.nih.gov/31020996/) | 2019 | Revisión sistemática | Journal of Inherited Metabolic Disease | Los datos para evaluar la efectividad en el mundo real de la terapia enzimática en mucopolisacaridosis tipo I son limitados. |
| [12196045](https://pubmed.ncbi.nlm.nih.gov/12196045/) | 2002 | Revisión | BioDrugs | Descripción del desarrollo de laronidasa como terapia enzimática de reemplazo. |
| [15794739](https://pubmed.ncbi.nlm.nih.gov/15794739/) | 2005 | Cohorte / experiencia clínica | Expert Opinion on Pharmacotherapy | Primeros cinco años de experiencia clínica con laronidasa en mucopolisacaridosis tipo I. |
| [33139350](https://pubmed.ncbi.nlm.nih.gov/33139350/) | 2021 | Cohorte observacional | Archives of Disease in Childhood | Mejoró el tiempo hasta el tratamiento, pero no el tiempo hasta el diagnóstico en mucopolisacaridosis tipo I. |
| [23251908](https://pubmed.ncbi.nlm.nih.gov/23251908/) | 2012 | In vitro / preclínico | Acta Biochimica Polonica | Compara en cultivos celulares el silenciamiento génico con siRNA frente a la terapia enzimática. Laronidasa no mostró citotoxicidad. |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19961931 | ALDURAZYME® | Solución inyectable | Laronidasa |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 2 interacciones de nivel menor (fuente: DDInter):
  - Cloroquina
  - Procaína

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
- El puntaje del modelo es alto (0,9922), pero no hay ensayos clínicos ni publicaciones que estudien directamente el síndrome de Sanfilippo, por lo que el nivel de evidencia es L5.
- Laronidasa no repone las enzimas deficientes en esta enfermedad y no cruza de forma apreciable la barrera hematoencefálica, por lo que la plausibilidad mecanística es baja.

**Para avanzar se necesita:**
- Estudios preclínicos que muestren si alfa-L-iduronidasa puede degradar los sustratos acumulados en el síndrome de Sanfilippo.
- Evaluación de estrategias para llegar al sistema nervioso central (por ejemplo, vías de administración distintas de la intravenosa).
- Datos del mecanismo de acción.
- Advertencias y contraindicaciones del prospecto aprobado en Colombia, aún no disponibles.

<!-- review:begin co-lic-20261031-laronidase-1 -->

> **Corrección de revisión (2026-10-31)**: Texto original: "Datos del mecanismo de acción / Situación regulatoria vigente en Colombia (registro cancelado)" Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-10-31. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261031-laronidase-1 -->

---

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-10-31 | Eliminado: "Situación regulatoria vigente en Colombia (registro cancelado)" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

