---
layout: default
title: Imiglucerase
parent: Evidencia Moderada (L3-L4)
nav_order: 336
evidence_level: L4
indication_count: 5
last_modified_at: 2026-10-14
description: "Imiglucerase: nueva indicación predicha, Síndrome de Hurler (MPS I) (nivel de evidencia L4). Indicación original: IMIGLUCERASA"
monitor_inn: "imiglucerase"
predicted_indications: ["Hurler syndrome", "Scheie syndrome", "benign neoplasm of adrenal gland", "autosomal ichthyosis syndrome with fatal disease course", "cholesteryl ester storage disease"]
---

# Imiglucerase
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **5** 
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

# Imiglucerasa: De Enfermedad de Gaucher (imiglucerasa) a Síndrome de Hurler

## Resumen en Una Frase

Imiglucerasa es una enzima recombinante (glucocerebrosidasa) utilizada como terapia de reemplazo enzimático, con registros sanitarios en Colombia bajo el nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para el **Síndrome de Hurler**, pero **no hay ensayos clínicos** y solo **1 publicación** (una revisión general sobre terapias de reemplazo enzimático) se asocia a esta predicción, sin evidencia directa del efecto del fármaco en esta enfermedad.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | IMIGLUCERASA (el registro sanitario no detalla la indicación en texto) |
| Nueva Indicación Predicha | Síndrome de Hurler (MPS I) |
| Puntaje de Predicción TxGNN | 99.52% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 3 (0 vigentes, 3 cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según el conocimiento general, la imiglucerasa es una glucocerebrosidasa (beta-glucosidasa) recombinante que reemplaza la enzima deficiente en la enfermedad de Gaucher.

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

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20166019 | BANTACE® 200 (cancelado) | Polvo liofilizado para reconstituir a solución inyectable | IMIGLUCERASA |
| 20118253 | BANTACE® 400 (cancelado) | Polvo liofilizado para reconstituir a solución inyectable | IMIGLUCERASA |
| 20013754 | CEREZYME® 400U (cancelado) | Polvo liofilizado para reconstituir a solución inyectable | IMIGLUCERASA |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificó una interacción de nivel moderado con **miglustat** (fuente: DDInter).

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el modelo y en una revisión general, sin ensayos clínicos. El mecanismo es poco plausible (la imiglucerasa no degrada los glicosaminoglicanos acumulados) y ya existe un tratamiento específico aprobado. Además, en Colombia todos los registros están cancelados.

**Para avanzar se necesita:**
- Datos del mecanismo de acción del fármaco
- Obtener y analizar el prospecto (advertencias y contraindicaciones) desde INVIMA
- Estudios preclínicos que demuestren actividad de la imiglucerasa sobre los sustratos del síndrome de Hurler
- Evaluar si tiene sentido frente a la laronidasa, ya aprobada para esta enfermedad

---

*Nota: las demás predicciones del modelo (síndrome de Scheie, neoplasia benigna de glándula suprarrenal, síndrome autosómico de ictiosis con curso fatal y enfermedad por almacenamiento de ésteres de colesterilo) tienen nivel de evidencia L4–L5 y también recomendación Hold, por carecer de ensayos clínicos y de un mecanismo plausible.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

