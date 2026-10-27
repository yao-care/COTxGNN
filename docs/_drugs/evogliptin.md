---
layout: default
title: Evogliptin
parent: Solo Predicción del Modelo (L5)
nav_order: 274
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Evogliptin: nueva indicación predicha, Opsismodisplasia (nivel de evidencia L5). Indicación original: Evogliptina tartrato"
monitor_inn: "evogliptin"
predicted_indications: ["opsismodysplasia", "thiamine-responsive dysfunction syndrome", "classic stiff person syndrome", "focal stiff limb syndrome", "drug-induced localized lipodystrophy"]
---

# Evogliptin
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

## Evogliptina: De Evogliptina Tartrato (Diabetes Tipo 2) a Opsismodisplasia
{: .text-alpha }

## Resumen en Una Frase

Evogliptina es un inhibidor de la DPP-4 comercializado en Colombia con el nombre SUGANON®. El registro sanitario indica únicamente "evogliptina tartrato" como indicación; por su clase farmacológica se asocia al tratamiento de la diabetes tipo 2.
El modelo TxGNN predice que podría ser efectivo para **opsismodisplasia**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Se trata solo de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Evogliptina tartrato (el registro no detalla la indicación clínica) |
| Nueva Indicación Predicha | Opsismodisplasia |
| Puntaje de Predicción TxGNN | 99.35% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registro vigente) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, evogliptina pertenece a la clase de los inhibidores de la DPP-4 (gliptinas), que prolongan la acción de las incretinas y mejoran el control de la glucosa. Mecanísticamente, su aplicación a la nueva indicación es solo especulativa.

La opsismodisplasia es una displasia esquelética rara causada por mutaciones en el gen *INPPL1*, que afectan a SHIP2 y a la señalización de PI3K/insulina. El único vínculo posible con la inhibición de DPP-4 sería indirecto, a través del eje incretina/insulina. No se encontró respaldo mecanístico ni clínico directo.

El puntaje alto de TxGNN (99.35%) refleja una predicción computacional basada en el grafo de conocimiento, no evidencia experimental. Debe interpretarse con cautela.

### Otras indicaciones predichas (para referencia)

| Rango | Enfermedad | Puntaje TxGNN | Nivel de Evidencia | Comentario |
|------|------|------|------|------|
| 2 | Síndrome de disfunción sensible a tiamina | 99.32% | L5 | Sin vínculo mecanístico claro con la inhibición de DPP-4 |
| 3 | Síndrome de la persona rígida clásico | 99.30% | L5 | Racional especulativo inmunomodulador (DPP-4/CD26 en linfocitos T) y asociación con autoinmunidad anti-GAD |
| 4 | Síndrome de extremidad rígida focal | 99.30% | L5 | Variante focal del espectro anterior; mismo puntaje, probablemente por vecindad en el grafo |
| 5 | Lipodistrofia localizada inducida por fármacos | 99.01% | L5 | Racional metabólico débil e indirecto |

---

## Informacion de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20188468 (cancelado) | SUGANON® | Tableta recubierta | Evogliptina tartrato |

Fabricante: Eurofarma Colombia S.A.S. El único registro está cancelado, por lo que actualmente no hay producto vigente en el mercado.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas en las consultas realizadas, y tampoco hay contraindicaciones derivadas del grafo de conocimiento para este fármaco.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (nivel L5), sin ensayos clínicos ni literatura, y con un vínculo mecanístico especulativo. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones) para completar la evaluación de seguridad
- Confirmar el mecanismo de acción en DrugBank y analizar su conexión con la vía INPPL1/SHIP2/PI3K
- Realizar estudios preclínicos o de mecanismo que justifiquen la hipótesis en opsismodisplasia
- Aclarar la situación regulatoria (cancelación del registro) y la viabilidad de comercialización en Colombia
- Considerar la necesidad clínica real, dado que se trata de una enfermedad ultrarrara, y si existen alternativas con mejor respaldo
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

