---
layout: default
title: Imiglucerase
parent: Solo Predicción del Modelo (L5)
nav_order: 336
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-24
description: "Imiglucerase: nueva indicación predicha, Síndrome de Hurler (MPS I) (nivel de evidencia L5). Indicación original: IMIGLUCERASA"
monitor_inn: "imiglucerase"
predicted_indications: ["Hurler syndrome", "Scheie syndrome", "benign neoplasm of adrenal gland", "autosomal ichthyosis syndrome with fatal disease course", "cholesteryl ester storage disease"]
---

# Imiglucerase
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Imiglucerasa: De Enfermedad de Gaucher (imiglucerasa) a Síndrome de Hurler (MPS I)
{: .text-alpha }

## Resumen en Una Frase

Imiglucerasa es una enzima recombinante (glucocerebrosidasa) utilizada como terapia de reemplazo enzimático, con registros sanitarios en Colombia bajo el nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para el **Síndrome de Hurler**, pero **no hay ensayos clínicos** y solo **1 publicación** (una revisión general sobre terapias de reemplazo enzimático) se asocia a esta predicción, sin evidencia directa del efecto del fármaco en esta enfermedad.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | IMIGLUCERASA (el registro sanitario no detalla la indicación en texto) |
| Nueva Indicación Predicha | Síndrome de Hurler (MPS I) |
| Puntaje de Predicción TxGNN | 0.9952 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 3 de 3) |
| Número de Registros Sanitarios | 3 (vigentes: 3) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Imiglucerase (traducción no oficial): «La enfermedad de Gaucher se caracteriza por una deficiencia de la actividad de la β-glucocerebrosidasa, que provoca la acumulación de glucocerebrósido en diversos tejidos, entre ellos el hígado, el bazo y la médula ósea. Los azúcares de manosa de la imiglucerasa median su unión a las células, incluidos los macrófagos, y su internalización por estas.» Texto original en inglés: "Gaucher disease is characterized by a deficiency of β-glucocerebrosidase activity, which results in accumulation of glucocerebroside in various tissues including liver, spleen, and bone marrow. The mannose sugars on imiglucerase mediate binding to and internalization by cells including macrophages." ([DailyMed: Cerezyme (imiglucerase) prescribing information, Genzyme Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=df60f030-866b-4374-a31f-8ae3f6b45c38), versión del 2026-08-27; consultado el 2026-11-19). Según el conocimiento general, la imiglucerasa es una glucocerebrosidasa (beta-glucosidasa) recombinante que reemplaza la enzima deficiente en la enfermedad de Gaucher.

El síndrome de Hurler (MPS I) es causado por la deficiencia de alfa-L-iduronidasa, lo que produce acumulación de glicosaminoglicanos. Ambas son enfermedades de depósito lisosomal tratadas con terapia de reemplazo enzimático, por lo que la relación es solo conceptual, a nivel de clase de enfermedad.

Sin embargo, el vínculo mecanístico es débil: la imiglucerasa no tiene actividad conocida sobre los sustratos acumulados (dermatán y heparán sulfato) y la especificidad enzimática no coincide. El puntaje alto probablemente refleja la cercanía entre enfermedades lisosomales en la red de conocimiento más que un mecanismo bioquímico real. Además, ya existe la enzima específica para esta enfermedad (laronidasa).

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [21211680](https://pubmed.ncbi.nlm.nih.gov/21211680/) | 2010 | Revisión | La Revue de médecine interne | Revisión general de la terapia de reemplazo enzimático en enfermedades lisosomales; describe la evolución desde la alglucerasa hasta la imiglucerasa en Gaucher. No evalúa el efecto de la imiglucerasa en el síndrome de Hurler. |

---

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 20013754 | CEREZYME® 400U | POLVO LIOFILIZADO PARA RECONSTITUIR A SOLUCION INYECTABLE | IMIGLUCERASA | Vigente |
| 20118253 | BANTACE ® 400 | POLVO LIOFILIZADO PARA RECONSTITUIR A SOLUCION INYECTABLE | IMIGLUCERASA | Vigente |
| 20166019 | BANTACE® 200 | POLVO LIOFILIZADO PARA RECONSTITUIR A SOLUCION INYECTABLE | IMIGLUCERASA | Vigente |

Se muestran los 3 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificó una interacción de nivel moderado con **miglustat** (fuente: DDInter).

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el modelo y en una revisión general, sin ensayos clínicos. El mecanismo es poco plausible (la imiglucerasa no degrada los glicosaminoglicanos acumulados) y ya existe un tratamiento específico aprobado. Además, en Colombia el medicamento está comercializado y los 3 registros sanitarios están vigentes (3 de 3).

**Para avanzar se necesita:**
- Datos del mecanismo de acción del fármaco
- Obtener y analizar el prospecto (advertencias y contraindicaciones) desde INVIMA
- Estudios preclínicos que demuestren actividad de la imiglucerasa sobre los sustratos del síndrome de Hurler
- Evaluar si tiene sentido frente a la laronidasa, ya aprobada para esta enfermedad

---

*Nota: las demás predicciones del modelo (síndrome de Scheie, neoplasia benigna de glándula suprarrenal, síndrome autosómico de ictiosis con curso fatal y enfermedad por almacenamiento de ésteres de colesterilo) tienen nivel de evidencia L4–L5 y también recomendación Hold, por carecer de ensayos clínicos y de un mecanismo plausible.*

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Cerezyme (imiglucerase) prescribing information, Genzyme Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=df60f030-866b-4374-a31f-8ae3f6b45c38) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

