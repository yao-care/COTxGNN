---
layout: default
title: Insulin Human
parent: Solo Predicción del Modelo (L5)
nav_order: 348
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Insulin Human: nueva indicación predicha, Ooforitis autoinmune (nivel de evidencia L5). Indicación original: Insulina (humana)"
monitor_inn: "insulin human"
predicted_indications: ["autoimmune oophoritis", "focal stiff limb syndrome", "classic stiff person syndrome", "thiamine-responsive dysfunction syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "pancreatic agenesis", "idiopathic localized lipodystrophy"]
---

# Insulin Human
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

## Insulina humana: De Insulina (humana) a Ooforitis Autoinmune
{: .text-alpha }

## Resumen en Una Frase

La insulina humana es una hormona de reemplazo utilizada originalmente para el tratamiento de la diabetes (registro INVIMA: "Insulina (humana)").
El modelo TxGNN predice que podría ser efectiva para **ooforitis autoinmune**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; se trata solo de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Insulina (humana) |
| Nueva Indicación Predicha | Ooforitis autoinmune |
| Puntaje de Predicción TxGNN | 0.9984 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Insulin Human (traducción no oficial): «La regulación del metabolismo de la glucosa es la actividad principal de las insulinas, incluida HUMULIN R U-500. Las insulinas reducen la glucosa en sangre al estimular la captación periférica de glucosa por el músculo esquelético y el tejido adiposo, y al inhibir la producción hepática de glucosa.» Texto original en inglés: "Regulation of glucose metabolism is the primary activity of insulins, including HUMULIN R U-500. Insulins lower blood glucose by stimulating peripheral glucose uptake by skeletal muscle and fat, and by inhibiting hepatic glucose production." ([DailyMed: Humulin R U-500 Kwikpen (insulin human) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b60e8dd0-1d48-4dc9-87fd-e14675255e8c), versión del 2026-07-01; consultado el 2026-11-19). Por conocimiento general, la insulina humana reemplaza la hormona endógena y regula el metabolismo de la glucosa mediante la vía de señalización insulina/PI3K-Akt.

En el caso de la ooforitis autoinmune, **no se establece un vínculo mecanístico directo**. La insulina participa en la esteroidogénesis de las células de la granulosa y de la teca, pero esta enfermedad se debe a la destrucción autoinmune de células esteroidogénicas, y la insulina no tiene un papel inmunomodulador conocido. El puntaje alto probablemente refleja la cercanía en la red de conocimiento con enfermedades endocrinas autoinmunes (por ejemplo, síndromes poliglandulares autoinmunes asociados a diabetes tipo 1), y no un mecanismo terapéutico.

Por ello, la predicción debe interpretarse con cautela: es una señal estadística del modelo sin respaldo clínico en los datos disponibles.

---

## Otras Indicaciones Predichas (contexto)

Las demás predicciones de mayor puntaje tampoco cuentan con ensayos ni publicaciones en los datos compilados:

| Indicación | Puntaje TxGNN | Nivel | Comentario |
|------|------|------|------|
| Síndrome de extremidad rígida focal | 0.9981 | L5 | Asociación indirecta por autoinmunidad anti-GAD65 y comorbilidad con diabetes tipo 1 |
| Síndrome de persona rígida clásico | 0.9981 | L5 | Mismo razonamiento; la puntuación proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica |
| Síndrome de disfunción sensible a tiamina | 0.9980 | L5 | Manejo sintomático de la diabetes asociada, no de la enfermedad de base |
| Opsismodisplasia | 0.9979 | L5 | Vínculo teórico por SHIP2 en la vía de insulina; sin efecto terapéutico demostrado |
| Lipodistrofia localizada inducida por fármacos | 0.9972 | L5 | Probable causalidad inversa: la insulina puede causar lipodistrofia en el sitio de inyección |
| Lipodistrofia centrífuga | 0.9970 | L5 | Sin evidencia clínica |
| Lipoatrofia localizada inducida por presión | 0.9970 | L5 | Efecto adverso, no señal terapéutica |
| Agenesia pancreática | 0.9970 | L4 | Único caso con mecanismo coherente: reemplazo de la hormona ausente en diabetes neonatal; es práctica clínica estándar, no un reposicionamiento novedoso |
| Lipodistrofia localizada idiopática | 0.9968 | L5 | La puntuación proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica, por efecto adverso conocido |

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 20061253 | WOSULIN N 100UI/ML SUSPENSIÓN INYECTABLE | SUSPENSION INYECTABLE | INSULINA (HUMANA) | Vigente |

Se muestra el único registro sanitario de este principio activo en los datos del INVIMA, Código Único de Medicamentos.

<!-- licenses:end -->

Fabricante: Elixym Biopharmaceutical S.A.S.

<!-- review:begin co-lic-20261105-insulin_human-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Fabricante: Elixym Biopharmaceutical S.A.S. No hay registros vigentes para este fármaco en los datos compilados." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-insulin_human-1 -->

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 297 interacciones. Entre las listadas, la mayoría son de nivel moderado:
  - Agonistas adrenérgicos/simpaticomiméticos: fenilefrina, epinefrina, pseudoefedrina, salbutamol.
  - Betabloqueadores e inhibidores de la ECA: acebutolol, benazepril.
  - Otros antidiabéticos: metformina, pioglitazona, alogliptina, albiglutida.
  - Hormonas y corticoides: etinilestradiol, estradiol, hidrocortisona.
  - Otros: acetazolamida, doxiciclina, hidroclorotiazida, alpelisib, etanol.
  - De nivel leve: hidrocortisona tópica y alclometasona tópica.

Para advertencias y contraindicaciones, consultar el prospecto. Adicionalmente, la insulina es una causa conocida de lipodistrofia en el sitio de inyección, lo que es relevante para varias de las indicaciones predichas.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe evidencia clínica ni literatura que respalde el uso de insulina en ooforitis autoinmune, y el puntaje del modelo parece reflejar proximidad en la red con enfermedades autoinmunes endocrinas, sin mecanismo terapéutico establecido.

<!-- review:begin co-lic-20261105-insulin_human-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "No existe evidencia clínica ni literatura que respalde el uso de insulina en ooforitis autoinmune, y el puntaje del modelo parece reflejar proximidad en la red con enfermedades autoinmunes endocrinas, sin mecanismo terapéutico establecido. Además, no hay registros sanitarios vigentes en Colombia." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-insulin_human-2 -->

**Para avanzar se necesita:**
- Datos del mecanismo de acción de DrugBank y una hipótesis inmunológica plausible para la ooforitis autoinmune.
- Revisión sistemática de literatura que confirme o descarte un papel terapéutico.
- Advertencias y contraindicaciones del prospecto de INVIMA para completar el análisis de seguridad.
- Si se busca una alternativa con mejor fundamento, evaluar la agenesia pancreática (L4), teniendo en cuenta que es reemplazo hormonal estándar y no un reposicionamiento novedoso.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "No hay registros vigentes para este fármaco en los datos compilados" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Además, no hay registros sanitarios vigentes en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Humulin R U-500 Kwikpen (insulin human) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b60e8dd0-1d48-4dc9-87fd-e14675255e8c) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

