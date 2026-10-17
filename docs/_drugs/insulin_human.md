---
layout: default
title: Insulin Human
parent: Solo Predicción del Modelo (L5)
nav_order: 348
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
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

# Insulina humana: De Insulina (humana) a Encefalomielitis... Ooforitis Autoinmune

> Nota: el título se ajusta al formato requerido a continuación.

# Insulina humana: De Insulina (humana) a Ooforitis Autoinmune

## Resumen en Una Frase

La insulina humana es una hormona de reemplazo utilizada originalmente para el tratamiento de la diabetes (registro INVIMA: "Insulina (humana)").
El modelo TxGNN predice que podría ser efectiva para **ooforitis autoinmune**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; se trata solo de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Insulina (humana) |
| Nueva Indicación Predicha | Ooforitis autoinmune |
| Puntaje de Predicción TxGNN | 99.84% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo cancelado (sin registros vigentes) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Por conocimiento general, la insulina humana reemplaza la hormona endógena y regula el metabolismo de la glucosa mediante la vía de señalización insulina/PI3K-Akt.

En el caso de la ooforitis autoinmune, **no se establece un vínculo mecanístico directo**. La insulina participa en la esteroidogénesis de las células de la granulosa y de la teca, pero esta enfermedad se debe a la destrucción autoinmune de células esteroidogénicas, y la insulina no tiene un papel inmunomodulador conocido. El puntaje alto probablemente refleja la cercanía en la red de conocimiento con enfermedades endocrinas autoinmunes (por ejemplo, síndromes poliglandulares autoinmunes asociados a diabetes tipo 1), y no un mecanismo terapéutico.

Por ello, la predicción debe interpretarse con cautela: es una señal estadística del modelo sin respaldo clínico en los datos disponibles.

---

## Otras Indicaciones Predichas (contexto)

Las demás predicciones de mayor puntaje tampoco cuentan con ensayos ni publicaciones en los datos compilados:

| Indicación | Puntaje TxGNN | Nivel | Comentario |
|------|------|------|------|
| Síndrome de extremidad rígida focal | 99.81% | L5 | Asociación indirecta por autoinmunidad anti-GAD65 y comorbilidad con diabetes tipo 1 |
| Síndrome de persona rígida clásico | 99.81% | L5 | Mismo razonamiento; probable artefacto del grafo |
| Síndrome de disfunción sensible a tiamina | 99.80% | L5 | Manejo sintomático de la diabetes asociada, no de la enfermedad de base |
| Opsismodisplasia | 99.79% | L5 | Vínculo teórico por SHIP2 en la vía de insulina; sin efecto terapéutico demostrado |
| Lipodistrofia localizada inducida por fármacos | 99.72% | L5 | Probable causalidad inversa: la insulina puede causar lipodistrofia en el sitio de inyección |
| Lipodistrofia centrífuga | 99.70% | L5 | Sin evidencia clínica |
| Lipoatrofia localizada inducida por presión | 99.70% | L5 | Efecto adverso, no señal terapéutica |
| Agenesia pancreática | 99.70% | L4 | Único caso con mecanismo coherente: reemplazo de la hormona ausente en diabetes neonatal; es práctica clínica estándar, no un reposicionamiento novedoso |
| Lipodistrofia localizada idiopática | 99.68% | L5 | Probable asociación del grafo por efecto adverso conocido |

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20061253 (cancelado) | WOSULIN N 100UI/ML SUSPENSIÓN INYECTABLE | Suspensión inyectable | Insulina (humana) |

Fabricante: Elixym Biopharmaceutical S.A.S. No hay registros vigentes para este fármaco en los datos compilados.

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
No existe evidencia clínica ni literatura que respalde el uso de insulina en ooforitis autoinmune, y el puntaje del modelo parece reflejar proximidad en la red con enfermedades autoinmunes endocrinas, sin mecanismo terapéutico establecido. Además, no hay registros sanitarios vigentes en Colombia.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de DrugBank y una hipótesis inmunológica plausible para la ooforitis autoinmune.
- Revisión sistemática de literatura que confirme o descarte un papel terapéutico.
- Advertencias y contraindicaciones del prospecto de INVIMA para completar el análisis de seguridad.
- Si se busca una alternativa con mejor fundamento, evaluar la agenesia pancreática (L4), teniendo en cuenta que es reemplazo hormonal estándar y no un reposicionamiento novedoso.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

