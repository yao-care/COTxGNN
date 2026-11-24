---
layout: default
title: Esomeprazole
parent: Solo Predicción del Modelo (L5)
nav_order: 263
evidence_level: L5
indication_count: 1
monitor_inn: "Esomeprazole"
predicted_indications: ["duodenal obstruction"]
last_modified_at: 2026-11-24
description: "Esomeprazole: nueva indicación predicha, obstrucción duodenal (duodenal obstruction) (nivel de evidencia L5). Indicación original: ESOMEPRAZOL"
---

# Esomeprazole
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

## Esomeprazol: inhibidor de la bomba de protones (inhibe la H+/K+ ATPasa gástrica, ATP4A) → obstrucción duodenal (duodenal obstruction)
{: .text-alpha }

## Resumen en Una Frase

Esomeprazol es un inhibidor de la bomba de protones que se utiliza para reducir la acidez gástrica.
El modelo TxGNN predice que podría ser efectivo para **obstrucción duodenal (duodenal obstruction)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | ESOMEPRAZOL |
| Nueva Indicación Predicha | obstrucción duodenal (duodenal obstruction) |
| Puntaje de Predicción TxGNN | 0,9945 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 20) |
| Número de Registros Sanitarios | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Esomeprazole (traducción no oficial): «El esomeprazol pertenece a una clase de compuestos antisecretores, los bencimidazoles sustituidos, que suprimen la secreción de ácido gástrico mediante la inhibición específica del sistema enzimático H+/K+ ATPasa en la superficie secretora de la célula parietal gástrica. El esomeprazol se protona y se convierte en el compartimento ácido de la célula parietal, formando el inhibidor activo, la sulfenamida aquiral.» Texto original en inglés: "Esomeprazole belongs to a class of antisecretory compounds, the substituted benzimidazoles, that suppress gastric acid secretion by specific inhibition of the H+/K+ ATPase enzyme system at the secretory surface of the gastric parietal cell. Esomeprazole is protonated and converted in the acidic compartment of the parietal cell forming the active inhibitor, the achiral sulphenamide." ([DailyMed: Nexium (esomeprazole magnesium) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f4853677-1622-4037-688b-fdf533a11d96), versión del 2025-12-19; consultado el 2026-11-19). Según la información conocida, esomeprazol actúa sobre la bomba de protones gástrica (ATP4A) y reduce la secreción de ácido en el estómago.

La obstrucción duodenal es una condición principalmente mecánica, por lo que la supresión de ácido no tiene un papel plausible como tratamiento modificador de la enfermedad. A lo sumo, podría ayudar con la enfermedad péptica secundaria. Es probable que la predicción se deba a la cercanía del modelo con la úlcera duodenal, que puede causar obstrucción como complicación.

Por lo tanto, el puntaje alto (0,9945) debe interpretarse con cautela: refleja una predicción del modelo y no una evidencia real de eficacia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 19915411 | NEXIUM MUPS® 20 MG | TABLETA CON CUBIERTA ENTERICA CON PELICULA | ESOMEPRAZOL | Vigente |
| 19940076 | ESOPRAX ® 40 CAPSULAS | CAPSULA DURA | ESOMEPRAZOL | Vigente |
| 19947032 | ESOMEPRAZOL 20 MG TABLETAS DE LIBERACIÓN RETARDADA. | TABLETA CON CUBIERTA ENTERICA CON PELICULA | ESOMEPRAZOL | Vigente |
| 19948574 | ESOZ 40 MG TABLETAS DE LIBERACIÓN RETARDADA. | TABLETA DE LIBERACION RETARDADA | ESOMEPRAZOL | Vigente |
| 19953919 | ESOMEPRAZOL40 MG | TABLETA CON RECUBRIMIENTO ENTÉRICO | ESOMEPRAZOL | Vigente |

Se muestran 5 de al menos 20 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes. Los datos de este informe solo incluyen parte de los registros.

<!-- licenses:end -->

La lista de registros puede ser parcial.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la consulta se completó y solo se identificó la interacción farmacológica con el blanco ATP4A (bomba de protones gástrica), que corresponde a su mecanismo de acción y no a un fármaco concomitante.

Para el resto de la información de seguridad, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos ni publicaciones sobre esomeprazol en obstrucción duodenal, y el mecanismo de supresión ácida no explica un beneficio en una condición mecánica. La predicción se mantiene solo como hipótesis del modelo (nivel L5).

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción y una justificación biológica plausible
- Revisión de la literatura para confirmar si existe algún estudio en obstrucción duodenal o sus complicaciones pépticas
- Advertencias y contraindicaciones del prospecto aprobado en Colombia
- Evaluación de la compatibilidad de vías de administración para esta condición

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Nexium (esomeprazole magnesium) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f4853677-1622-4037-688b-fdf533a11d96) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

