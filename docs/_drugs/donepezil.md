---
layout: default
title: Donepezil
parent: Solo Predicción del Modelo (L5)
nav_order: 231
evidence_level: L5
indication_count: 8
---

# Donepezil
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Donepezilo: De Indicación Original (DONEPEZIL) a Trastornos Psicógenos del Movimiento

## Resumen en Una Frase

Donepezilo es un inhibidor de la acetilcolinesterasa registrado en Colombia bajo el texto de indicación "DONEPEZIL", sin una indicación clínica detallada en los registros disponibles.
El modelo TxGNN predice que podría ser efectivo para **trastornos psicógenos del movimiento**, con **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción específica.
La evidencia actual se limita a la predicción del modelo (nivel L5).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | DONEPEZIL (el registro sanitario no detalla una indicación clínica) |
| Nueva Indicación Predicha | Trastornos psicógenos del movimiento |
| Puntaje de Predicción TxGNN | 99.23% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 4 (todos cancelados) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, donepezilo es un inhibidor de la acetilcolinesterasa que aumenta el tono colinérgico central, y su uso en el deterioro cognitivo es ampliamente conocido. Mecanísticamente, la modulación colinérgica podría ser relevante en algunos trastornos del movimiento.

Sin embargo, para los trastornos psicógenos (funcionales) del movimiento no se identificó un vínculo mecanístico específico. La predicción se basa únicamente en el puntaje del modelo (0.992), sin ensayos ni literatura que la sustenten. Debe considerarse una hipótesis exploratoria.

**Otras indicaciones predichas (contexto):** el modelo también predice otras condiciones, algunas con más respaldo que la principal:

| Indicación predicha | Puntaje TxGNN | Nivel | Resumen |
|------|------|------|------|
| Trastorno de tics crónico | 99.19% | L3 | Estudio pediátrico abierto en tics con TDAH, reportes pequeños y trabajo preclínico en ratones; sin ensayos registrados |
| Temblor ortostático primario | 99.17% | L5 | Solo predicción |
| Enfermedad extrapiramidal y del movimiento | 99.16% | L3 | Evidencia mixta: posible beneficio en discinesias tardías, pero una revisión sistemática de 2025 señala que los inhibidores de colinesterasa pueden inducir o empeorar síntomas extrapiramidales |
| Ataques de estremecimiento benignos | 99.16% | L5 | Solo predicción; afección benigna, balance riesgo-beneficio desfavorable sin evidencia |
| Síndrome temblor-nistagmo-úlcera duodenal | 99.15% | L5 | Única publicación indirecta (enfermedad de Behçet); riesgo de úlcera con inhibidores de colinesterasa |
| Mirada tónica ascendente paroxística benigna con ataxia | 99.12% | L5 | Solo predicción; afección rara que suele resolverse sola |
| Discinesia linguo-facial-bucal | 99.02% | L4 | Revisiones Cochrane sobre fármacos colinérgicos en discinesia tardía, no específicas de donepezilo y con evidencia insuficiente |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para trastornos psicógenos del movimiento.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para trastornos psicógenos del movimiento.

## Información de Mercado en Colombia

Los 4 registros sanitarios están cancelados; no hay registros vigentes.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20118656 | ARIZIL 10 MG | Tableta recubierta | DONEPEZIL | Cancelado |
| 19993779 | Donepezilo Clorhidrato 10 mg tabletas recubiertas | Tableta recubierta | DONEPEZIL | Cancelado |
| 19947560 | Donepecilo Clorhidrato 5 mg | Tableta recubierta | DONEPEZIL | Cancelado |
| 19946097 | ALZIT® 10 MG | Tableta recubierta | DONEPEZIL | Cancelado |

## Consideraciones de Seguridad

- **Contraindicaciones / condiciones de precaución (grafo de conocimiento, no texto de prospecto):** epilepsia, asma (incluido asma intrínseco y alérgico), obstrucción del cuello vesical, enfermedad ulcerosa péptica activa, síndrome del seno enfermo (incluida la forma familiar) y bloqueo auriculoventricular.
- **Interacciones farmacológicas:** se identificaron 257 interacciones. Entre las listadas:
  - **Mayor:** bupropión.
  - **Moderada:** famotidina, ranitidina, cimetidina, hiosciamina, atropina (incluida la oftálmica), glicopirronio, clidinio, diciclomina (anticolinérgicos, con efecto farmacodinámico opuesto), loperamida, dexametasona, metronidazol, dolasetrón, ácido picosulfúrico y polietilenglicol 3350 con electrolitos.
  - **Menor:** aprepitant, ácido acetilsalicílico, lorcaserina, claritromicina.
- **Riesgo específico señalado en la literatura:** los inhibidores de colinesterasa pueden inducir o empeorar síntomas extrapiramidales (temblor mandibular, síndrome de Pisa), lo cual es relevante al considerar trastornos del movimiento.

No se dispone de advertencias del prospecto de INVIMA; consultar el prospecto para información de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal (trastornos psicógenos del movimiento) se basa solo en el modelo, sin ensayos ni literatura, y no existe un vínculo mecanístico específico. Además, el donepezilo no tiene registros vigentes en Colombia y puede empeorar síntomas extrapiramidales.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (consulta a DrugBank).
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), requisito previo para un tamizaje de seguridad.
- Priorizar la revisión de **trastorno de tics crónico** (L3), el candidato con mayor respaldo: revisar los diseños completos de los estudios y evaluar la factibilidad de un estudio controlado.
- Para movimientos extrapiramidales, evaluar el balance beneficio-riesgo, dada la evidencia mixta.
- Aclarar el estado regulatorio: determinar si algún registro puede reactivarse o si se requeriría un nuevo registro.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

