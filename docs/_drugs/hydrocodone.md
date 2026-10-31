---
layout: default
title: Hydrocodone
parent: Evidencia Moderada (L3-L4)
nav_order: 327
evidence_level: L4
indication_count: 1
last_modified_at: 2026-10-31
description: "Hydrocodone: nueva indicación predicha, Enfermedad de la cavidad nasal (nivel de evidencia L4). Indicación original: Paracetamol. Combinaciones con psicolépticos"
monitor_inn: "hydrocodone"
predicted_indications: ["nasal cavity disease"]
---

# Hydrocodone
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **1** 
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

## Hidrocodona: De Paracetamol en Combinaciones con Psicolépticos a Enfermedad de la Cavidad Nasal
{: .text-alpha }

## Resumen en Una Frase

La hidrocodona es un opioide que, en Colombia, se registró dentro de un producto combinado con paracetamol (indicación registrada: "Paracetamol. Combinaciones con psicolépticos").
El modelo TxGNN predice que podría ser efectiva para **enfermedad de la cavidad nasal**, pero **no hay ensayos clínicos** y solo existe **1 publicación**, un reporte de caso que describe daño nasal por mal uso del fármaco, no un beneficio terapéutico.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Paracetamol. Combinaciones con psicolépticos |
| Nueva Indicación Predicha | Enfermedad de la cavidad nasal |
| Puntaje de Predicción TxGNN | 0.9988 |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 1) |
| Número de Registros Sanitarios | al menos 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este informe. Según la información conocida, la hidrocodona es un agonista de los receptores opioides mu, con efectos analgésicos y antitusivos.

En este caso, la predicción **no resulta mecanísticamente razonable**. No se conoce ningún mecanismo por el cual un opioide trate una enfermedad estructural o inflamatoria de la cavidad nasal. La única publicación disponible describe necrosis de la cavidad nasal y la faringe por abuso intranasal de hidrocodona-paracetamol, es decir, evidencia de daño y no de beneficio.

El puntaje alto (0.9988) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. La similitud con la indicación original no ha sido evaluada.


---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [22965281](https://pubmed.ncbi.nlm.nih.gov/22965281/) | 2012 | Reporte de caso (evento adverso / mal uso) | The Laryngoscope | El abuso intranasal de hidrocodona-paracetamol (tabletas trituradas e inhaladas) produjo necrosis de la cavidad nasal y la faringe. Es evidencia de daño, no de beneficio terapéutico. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20113430 (cancelado) | SINALGEN MAXTABLETAS. | Tableta | Paracetamol. Combinaciones con psicolépticos |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se registraron 525 interacciones. Entre las principales, de nivel **mayor**: alvimopán, aprepitant, bupropión, cimetidina, claritromicina, clotrimazol, dexametasona, morfina (incluida la liposomal) y naltrexona. De nivel **moderado**: hiosciamina, loperamida, atropina, atapulgita, clidinio, dronabinol, fenfluramina, metoclopramida, miconazol y naloxona.
- **Enfermedades asociadas a contraindicación según el grafo de conocimiento** (no provienen del prospecto): hipertensión, insuficiencia hepática, epilepsia, EPOC, úlcera gástrica y péptica, enfermedad renal, pancreatitis, enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia, hipotiroidismo y mixedema, enfermedad inflamatoria intestinal, diabetes y cetoacidosis diabética, hiperplasia prostática benigna, hipotensión, gota, abuso o dependencia de sustancias, trastornos de la coagulación, rabdomiólisis, hemofilia, enfermedad coronaria e infarto de miocardio.

Consultar el prospecto para las advertencias y contraindicaciones oficiales, que no están disponibles en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El puntaje alto del modelo no está respaldado por un mecanismo terapéutico plausible, y la única publicación documenta daño nasal, no beneficio. Además, el perfil de riesgo de los opioides es desfavorable y el producto registrado en Colombia está cancelado.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (consulta a DrugBank) para evaluar el vínculo mecanístico.
- Advertencias y contraindicaciones oficiales del prospecto de INVIMA.
- Evidencia clínica o preclínica que muestre un beneficio, y no un daño, en la cavidad nasal o en la laringofaringitis aguda.
- Evaluación de la compatibilidad de vía de administración (la presentación registrada fue oral, en tabletas) y de la similitud con la indicación original.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

