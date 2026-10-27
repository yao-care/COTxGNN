---
layout: default
title: Insulin Glargine
parent: Solo Predicción del Modelo (L5)
nav_order: 346
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
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
| Puntaje de Predicción TxGNN | 99.88% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 3 (todos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción dentro de los datos compilados para este informe. Según la información conocida, la insulina glargina actúa sobre el receptor de insulina para regular el metabolismo de la glucosa.

Para la ooforitis autoinmune **no se identifica un vínculo mecanístico directo** con este fármaco. No existe una vía establecida que conecte la insulina glargina con la patología autoinmune del ovario. El puntaje alto de TxGNN (99.88%) es únicamente una predicción computacional y probablemente refleja asociaciones del grafo de conocimiento, no un efecto terapéutico demostrado.

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
| 2 | Síndrome de disfunción sensible a tiamina | 99.61% | L5 | La insulina podría manejar la diabetes asociada (control sintomático), sin evidencia aportada |
| 3 | Síndrome de rigidez focal de extremidad | 99.60% | L5 | Probable artefacto por asociación autoinmune/anti-GAD con diabetes |
| 4 | Síndrome clásico de persona rígida | 99.60% | L5 | La insulina trata la diabetes comórbida, no la enfermedad neurológica |
| 5 | Opsismodisplasia | 99.59% | L5 | Vínculo teórico vía INPPL1/vía de señalización de insulina, no probado |
| 6 | Agenesia pancreática | 99.43% | L4 | Reemplazo hormonal racional, pero no es reposicionamiento propiamente; literatura solo indirecta |
| 7 | Lipodistrofia localizada inducida por fármacos | 99.42% | L5 | La insulina inyectada puede causar esta condición; uso no recomendable |
| 8 | Lipodistrofia centrífuga | 99.39% | L5 | Asociación probablemente del grafo, sin evidencia |
| 9 | Lipoatrofia localizada inducida por presión | 99.38% | L5 | Racional teórico débil; las inyecciones se asocian a lipodistrofia |
| 10 | Lipodistrofia localizada idiopática | 99.34% | L5 | Probable asociación por lipodistrofia relacionada con insulina |

La única predicción con literatura asociada es la **agenesia pancreática**; esta consiste en revisiones sobre terapia con insulina en diabetes tipo 2 y diabetes secundaria, un estudio en gatos diabéticos y un caso de MODY5 tratado con un agonista del receptor de GLP-1. Ninguna es un ensayo en agenesia pancreática.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 19914262 | LANTUS® 100 U/ML | Solución inyectable | Insulina glargina | Cancelado |
| 20060088 | GLARITUS 100UI/ML | Solución inyectable | Insulina glargina | Cancelado |
| 20128168 | SOLIQUA® 30-60 | Solución inyectable | Insulina glargina + lixisenatida | Cancelado |

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
La predicción para ooforitis autoinmune es solo computacional (L5), sin ensayos ni literatura, y sin vínculo mecanístico plausible. Además, no hay registros sanitarios vigentes en Colombia.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank
- Advertencias y contraindicaciones del prospecto de INVIMA (brecha de datos bloqueante para el tamizaje de seguridad)
- Revisión sistemática de la literatura sobre insulina y ooforitis autoinmune
- Si se desea priorizar otra indicación, evaluar la agenesia pancreática (L4) entendiéndola como reemplazo hormonal, no como reposicionamiento
- Confirmar la situación regulatoria en Colombia, ya que los tres registros están cancelados
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

