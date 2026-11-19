---
layout: default
title: Insulin Glargine
parent: Solo Predicción del Modelo (L5)
nav_order: 346
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
description: "Insulin Glargine: nueva indicación predicha, Ooforitis autoinmune (nivel de evidencia L5). Indicación original: Insulina glargina"
monitor_inn: "Insulin glargine"
predicted_indications: ["autoimmune oophoritis", "thiamine-responsive dysfunction syndrome", "focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia", "pancreatic agenesis", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy"]
---

# Insulin Glargine
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

## Insulina glargina: De Diabetes Mellitus (Insulina Glargina) a Ooforitis Autoinmune
{: .text-alpha }

## Resumen en Una Frase

La insulina glargina es una insulina basal de acción prolongada, registrada en Colombia para el control de la glucemia (según el registro, como insulina glargina sola o combinada con lixisenatida).
El modelo TxGNN predice que podría ser efectiva para **ooforitis autoinmune**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Insulina glargina (el registro sanitario no detalla una enfermedad específica) |
| Nueva Indicación Predicha | Ooforitis autoinmune |
| Puntaje de Predicción TxGNN | 0.9988 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 5 de 5) |
| Número de Registros Sanitarios | 5 (vigentes: 5) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Insulin Glargine (traducción no oficial): «La actividad principal de la insulina, incluidos los productos de insulina glargina, es la regulación del metabolismo de la glucosa. La insulina y sus análogos disminuyen la glucemia al estimular la captación periférica de glucosa, especialmente por el músculo esquelético y el tejido adiposo, y al inhibir la producción hepática de glucosa.» Texto original en inglés: "The primary activity of insulin, including insulin glargine products, is regulation of glucose metabolism. Insulin and its analogs lower blood glucose by stimulating peripheral glucose uptake, especially by skeletal muscle and fat, and by inhibiting hepatic glucose production." ([DailyMed: Langlara (insulin glargine-aldy) prescribing information, Lanexa Biologics, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5328761e-59d3-ca7a-e063-6394a90ae810), versión del 2026-10-15; consultado el 2026-11-19). Según la información conocida, la insulina glargina actúa sobre el receptor de insulina para regular el metabolismo de la glucosa.

Para la ooforitis autoinmune **no se identifica un vínculo mecanístico directo** con este fármaco. No existe una vía establecida que conecte la insulina glargina con la patología autoinmune del ovario. El puntaje alto de TxGNN (0.9988) proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica ni un efecto terapéutico demostrado.

Por lo tanto, esta predicción debe considerarse una hipótesis sin respaldo y no una oportunidad de reposicionamiento validada.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para ooforitis autoinmune.

---

## Otras Predicciones del Modelo (Contexto)

Para dar contexto, estas son las demás indicaciones predichas. Ninguna cuenta con ensayos clínicos.

| Rango | Indicación Predicha | Puntaje TxGNN | Nivel | Comentario |
|---|---|---|---|---|
| 2 | Síndrome de disfunción sensible a tiamina | 0.9961 | L5 | La insulina podría manejar la diabetes asociada (control sintomático), sin evidencia aportada |
| 3 | Síndrome de rigidez focal de extremidad | 0.9960 | L5 | Probable artefacto por asociación autoinmune/anti-GAD con diabetes |
| 4 | Síndrome clásico de persona rígida | 0.9960 | L5 | La insulina trata la diabetes comórbida, no la enfermedad neurológica |
| 5 | Opsismodisplasia | 0.9959 | L5 | Vínculo teórico vía INPPL1/vía de señalización de insulina, no probado |
| 6 | Agenesia pancreática | 0.9943 | L4 | Reemplazo hormonal racional, pero no es reposicionamiento propiamente; literatura solo indirecta |
| 7 | Lipodistrofia localizada inducida por fármacos | 0.9942 | L5 | La insulina inyectada puede causar esta condición; uso no recomendable |
| 8 | Lipodistrofia centrífuga | 0.9939 | L5 | Puntaje del modelo TxGNN (deep learning); puede reflejar similitudes aprendidas entre enfermedades, sin evidencia biológica |
| 9 | Lipoatrofia localizada inducida por presión | 0.9938 | L5 | Racional teórico débil; las inyecciones se asocian a lipodistrofia |
| 10 | Lipodistrofia localizada idiopática | 0.9934 | L5 | Probable asociación por lipodistrofia relacionada con insulina |

La única predicción con literatura asociada es la **agenesia pancreática**; esta consiste en revisiones sobre terapia con insulina en diabetes tipo 2 y diabetes secundaria, un estudio en gatos diabéticos y un caso de MODY5 tratado con un agonista del receptor de GLP-1. Ninguna es un ensayo en agenesia pancreática.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 19914262 | LANTUS® 100 U/ML | Solución inyectable | Insulina glargina | Vigente |
| 20060088 | GLARITUS 100UI/ML | Solución inyectable | Insulina glargina | Vigente |
| 20128168 | SOLIQUA® 30-60 | Solución inyectable | Insulina glargina + lixisenatida | Vigente |

---

## Consideraciones de Seguridad

**Interacciones Farmacológicas:** se identificaron 100 interacciones potenciales; las más relevantes de la muestra compilada son:

- **Moderadas:** fenilefrina, acebutolol, acetazolamida, formoterol, pseudoefedrina, doxiciclina, epinefrina, etinilestradiol, hidrocortisona, albiglutida, salbutamol, etanol, hidroclorotiazida, alogliptina, metformina, pioglitazona, estradiol y alpelisib. Estas pueden alterar el control glucémico (hipo o hiperglucemia).
- **Menores:** hidrocortisona tópica y alclometasona tópica.

Consultar el prospecto para información adicional de advertencias y contraindicaciones.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para ooforitis autoinmune es solo computacional (L5), sin ensayos ni literatura, y sin vínculo mecanístico plausible.

<!-- review:begin co-lic-20261105-insulin_glargine-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción para ooforitis autoinmune es solo computacional (L5), sin ensayos ni literatura, y sin vínculo mecanístico plausible. Además, no hay registros sanitarios vigentes en Colombia." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 5 registros sanitarios (vigentes: 5); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-insulin_glargine-1 -->

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank
- Advertencias y contraindicaciones del prospecto de INVIMA (brecha de datos bloqueante para el tamizaje de seguridad)
- Revisión sistemática de la literatura sobre insulina y ooforitis autoinmune
- Si se desea priorizar otra indicación, evaluar la agenesia pancreática (L4) entendiéndola como reemplazo hormonal, no como reposicionamiento
- Confirmar la situación regulatoria en Colombia

<!-- review:begin co-lic-20261105-insulin_glargine-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Confirmar la situación regulatoria en Colombia, ya que los tres registros están cancelados" Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 5 registros sanitarios (vigentes: 5); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-insulin_glargine-2 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Además, no hay registros sanitarios vigentes en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "ya que los tres registros están cancelados" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Langlara (insulin glargine-aldy) prescribing information, Lanexa Biologics, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5328761e-59d3-ca7a-e063-6394a90ae810) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

