---
layout: default
title: Insulin Glulisine
parent: Solo Predicción del Modelo (L5)
nav_order: 347
evidence_level: L5
indication_count: 9
monitor_inn: "insulin glulisine"
predicted_indications: ["thiamine-responsive dysfunction syndrome", "opsismodysplasia", "classic stiff person syndrome", "focal stiff limb syndrome", "autoimmune oophoritis", "pancreatic agenesis", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy"]
last_modified_at: 2026-11-24
description: "Insulin Glulisine: nueva indicación predicha, Síndrome de disfunción sensible a la tiamina (thiamine-responsive dysfunction syndrome) (nivel de evidencia L5). Indicación original: INSULINA GLULISINA"
---

# Insulin Glulisine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Insulina glulisina: análogo de insulina de acción rápida → síndrome de disfunción sensible a la tiamina (thiamine-responsive dysfunction syndrome)
{: .text-alpha }

## Resumen en Una Frase

Insulina glulisina es un análogo de insulina que actúa sobre el receptor de insulina y se comercializa en Colombia bajo la marca APIDRA®.
El modelo TxGNN predice que podría ser efectiva para el **síndrome de disfunción sensible a la tiamina (thiamine-responsive dysfunction syndrome)**, con un puntaje de 0,9947,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | INSULINA GLULISINA |
| Nueva Indicación Predicha | Síndrome de disfunción sensible a la tiamina (thiamine-responsive dysfunction syndrome) |
| Puntaje de Predicción TxGNN | 0,9947 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 2 de 2) |
| Número de Registros Sanitarios | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Insulin Glulisine (traducción no oficial): «La regulación del metabolismo de la glucosa es la actividad principal de las insulinas y los análogos de insulina, incluida la insulina glulisina. Las insulinas disminuyen la glucemia al estimular la captación periférica de glucosa por el músculo esquelético y el tejido adiposo, y al inhibir la producción hepática de glucosa.» Texto original en inglés: "Regulation of glucose metabolism is the primary activity of insulins and insulin analogs, including insulin glulisine. Insulins lower blood glucose by stimulating peripheral glucose uptake by skeletal muscle and fat, and by inhibiting hepatic glucose production." ([DailyMed: Apidra (insulin glulisine) prescribing information, sanofi-aventis U.S. LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e7af6a7a-8046-4fb4-9979-4ec4230b23aa), versión del 2025-11-25; consultado el 2026-11-19). Por su naturaleza, la insulina glulisina es un análogo de insulina que actúa como agonista del receptor de insulina para controlar la glucemia.

El síndrome de anemia megaloblástica sensible a la tiamina incluye diabetes mellitus entre sus manifestaciones. Esa es la vía plausible por la que el modelo asocia el fármaco con esta enfermedad. Sin embargo, no hay evidencia directa de que la insulina glulisina actúe sobre el defecto subyacente del transportador de tiamina.

En consecuencia, cualquier beneficio sería solo sintomático, limitado al control glucémico. La predicción es solo una inferencia del modelo y requiere validación independiente.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 19950478 | APIDRA ® | SOLUCION INYECTABLE | INSULINA GLULISINA | Vigente |
| 19950479 | APIDRA ® | SOLUCION INYECTABLE | INSULINA GLULISINA | Vigente |

Se muestran los 2 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

La lista de registros puede ser parcial.

## Consideraciones de Seguridad

**Interacciones Farmacológicas**: se identificaron 353 interacciones registradas. Entre las principales, de nivel moderado:
- Fenilefrina, acebutolol, acetazolamida, formoterol, pseudoefedrina, doxiciclina, epinefrina y salbutamol.
- Etinilestradiol, estradiol e hidrocortisona.
- Otros antidiabéticos: albiglutida, alogliptina, metformina, pioglitazona y alpelisib.
- Hidroclorotiazida y etanol.

También hay interacciones de nivel leve, por ejemplo con hidrocortisona tópica y alclometasona tópica.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5), sin ensayos ni publicaciones, y el vínculo mecanístico se limita a la diabetes asociada, sin efecto sobre el defecto de fondo.

**Para avanzar se necesita:**
- Datos del mecanismo de acción desde DrugBank.
- Advertencias y contraindicaciones del prospecto de INVIMA.
- Revisión de literatura que estudie directamente esta enfermedad con insulina.
- Confirmar el estado vigente de los registros sanitarios.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Apidra (insulin glulisine) prescribing information, sanofi-aventis U.S. LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e7af6a7a-8046-4fb4-9979-4ec4230b23aa) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

