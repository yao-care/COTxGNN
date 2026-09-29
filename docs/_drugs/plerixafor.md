---
layout: default
title: Plerixafor
parent: Solo Predicción del Modelo (L5)
nav_order: 327
evidence_level: L5
indication_count: 7
---

# Plerixafor
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Plerixafor: De Movilización de Células Madre Hematopoyéticas a Mieloma de Células Plasmáticas Indolente

## Resumen en Una Frase

Plerixafor es un antagonista del receptor CXCR4 que se usa como agente de movilización de células madre hematopoyéticas. Los datos de INVIMA no detallan la indicación, pues solo repiten el nombre del fármaco.
El modelo TxGNN predice que podría ser efectivo para **mieloma de células plasmáticas indolente**, pero hasta ahora hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta indicación específica.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto solo dice "PLERIXAFOR"). El uso conocido es la movilización de células madre. |
| Nueva Indicación Predicha | Mieloma de células plasmáticas indolente |
| Puntaje de Predicción TxGNN | 99.97% (posición 402 del ranking del modelo) |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 9 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base consultada. Según la información conocida, plerixafor bloquea el eje CXCL12-CXCR4, que retiene las células en la médula ósea. Su uso comprobado es movilizar células madre hacia la sangre para su recolección.

Las células plasmáticas dependen de ese mismo eje para permanecer en la médula ósea, por lo que la hipótesis es plausible. Sin embargo, el papel actual de plerixafor en el mieloma es de apoyo (movilización de células madre para trasplante). Ese uso **no** demuestra actividad contra la enfermedad en sí.

El puntaje de 99.97% es solo una salida del modelo. No hay estudios que confirmen la predicción para esta indicación.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para mieloma de células plasmáticas indolente.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

## Señal Adicional: Leucemia Mieloide (Otra Predicción del Mismo Fármaco)

Entre las predicciones de plerixafor, la **leucemia mieloide** (posición 7, puntaje 99.02%) es la única con evidencia real:

- Hay más de 30 ensayos clínicos, casi todos de Fase 1 o Fase 1/2.
- Ejemplos completados: [NCT00512252](https://clinicaltrials.gov/study/NCT00512252) (n=52, con MEC en LMA refractaria), [NCT01352650](https://clinicaltrials.gov/study/NCT01352650) (n=71, con decitabina en mayores de 60 años) y [NCT00943943](https://clinicaltrials.gov/study/NCT00943943) (n=33, con sorafenib y G-CSF en LMA con FLT3).
- Hay publicaciones de Fase 1/2, como [22308295](https://pubmed.ncbi.nlm.nih.gov/22308295/) (Blood, 2012) y [29724902](https://pubmed.ncbi.nlm.nih.gov/29724902/) (Haematologica, 2018), además de una revisión sistemática con metaanálisis, [32877869](https://pubmed.ncbi.nlm.nih.gov/32877869/) (Leukemia Research, 2020).
- El paquete la clasifica como L2 con recomendación "Research Question". No hay datos aleatorizados que muestren beneficio en supervivencia o remisión.

Las otras predicciones (CMM7, melanomas, bronquitis) son L5, sin ensayos ni literatura, y tienen recomendación Hold.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20255171 | PLERIXAFOR 24 MG SOLUCIÓN INYECTABLE (Avalon Pharmaceutical S.A) | Solución inyectable | PLERIXAFOR (el registro no detalla la indicación) |
| 20056150 | MOZOBIL® (Genzyme Corporation) | Solución inyectable | PLERIXAFOR (el registro no detalla la indicación) |

El paquete informa 9 registros en total, pero solo incluye 5 filas, que corresponden a estos 2 números distintos (el 20255171 aparece 4 veces).

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para mieloma de células plasmáticas indolente solo existe la predicción del modelo (L5), sin ensayos ni publicaciones. Además, el papel de plerixafor en mieloma es de apoyo y no demuestra efecto contra la enfermedad.

**Para avanzar se necesita:**
- Estudios preclínicos o clínicos que evalúen plerixafor como tratamiento del mieloma indolente, y no solo como movilizador.
- Datos de seguridad del prospecto de INVIMA (advertencias y contraindicaciones), que hoy faltan.
- Datos del mecanismo de acción desde DrugBank para fortalecer el análisis mecanístico.
- Si se busca una línea con más respaldo, evaluar la leucemia mieloide, que tiene evidencia de Fase 1/2 pero sin datos aleatorizados.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

