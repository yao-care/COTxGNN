---
layout: default
title: Eculizumab
parent: Solo Predicción del Modelo (L5)
nav_order: 244
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Eculizumab: nueva indicación predicha, Hematopoyesis cíclica (nivel de evidencia L5). Indicación original: ECULIZUMAB"
---

# Eculizumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Eculizumab: De Indicación No Especificada en el Registro a Hematopoyesis Cíclica

## Resumen en Una Frase

Eculizumab es un anticuerpo monoclonal inhibidor del complemento (C5). En el registro sanitario colombiano figura solo con el nombre del principio activo, sin una indicación detallada.
El modelo TxGNN predice que podría ser efectivo para **hematopoyesis cíclica (neutropenia cíclica)**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción; se trata únicamente de una predicción basada en grafos de conocimiento.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | ECULIZUMAB (el registro no detalla la indicación) |
| Nueva Indicación Predicha | Hematopoyesis cíclica |
| Puntaje de Prediccion TxGNN | 99.97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Numero de Registros Sanitarios | 3 (todos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según el conocimiento general, eculizumab es un anticuerpo monoclonal humanizado que inhibe la proteína C5 del complemento y bloquea la cascada terminal del complemento. Su eficacia está documentada en enfermedades mediadas por complemento, como la hemoglobinuria paroxística nocturna (HPN), el síndrome hemolítico urémico atípico (SHUa) y la miastenia gravis.

La neutropenia cíclica, en cambio, se debe principalmente a mutaciones en el gen *ELANE* y no es una enfermedad mediada por complemento. Por ello, **no existe una justificación mecanística clara** para inhibir C5 en esta condición. El puntaje alto (99.97%) refleja una asociación dentro del grafo de conocimiento, no evidencia biológica ni clínica.

Las otras nueve predicciones principales (distintas formas de neutropenia congénita, neutropenia idiopática del adulto, deficiencia de p14 y trastorno de liberación plaquetaria) tienen puntajes similares (99.94%–99.96%) y presentan la misma falta de plausibilidad mecanística.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para hematopoyesis cíclica.

Para otras predicciones del modelo se recuperaron publicaciones, pero corresponden a enfermedades en las que eculizumab ya tiene uso conocido (HPN, SHUa, microangiopatías trombóticas, miastenia gravis, deficiencia de CD59). No evalúan la indicación predicha y su coincidencia parece deberse al fármaco, no a la enfermedad.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20164753 | ELIZARIA® 10 MG/ML | Solución concentrada para infusión | ECULIZUMAB | Cancelado |
| 20254329 | BKEMV® 300 MG | Solución concentrada para infusión | ECULIZUMAB | Cancelado |
| 20028870 | SOLIRIS® 300 MG | Solución concentrada para infusión | ECULIZUMAB | Cancelado |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 4 interacciones de nivel **menor** con inmunoglobulina G humana (intravenosa, subcutánea, intramuscular y combinación intravenosa/subcutánea).
- **Riesgo adicional (según el análisis de la predicción)**: la inhibición del complemento aumenta el riesgo de infecciones, en particular meningocócicas. Esto es especialmente preocupante en poblaciones con neutropenia o inmunodeficiencia.

Consultar el prospecto para información sobre advertencias y contraindicaciones.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el grafo de conocimiento (L5), sin ensayos ni literatura directa. La neutropenia cíclica no es una enfermedad mediada por complemento, y el riesgo de infección por la inhibición de C5 en pacientes neutropénicos es un problema de seguridad importante. Además, los tres registros sanitarios en Colombia están cancelados.

**Para avanzar se necesita:**
- Una hipótesis mecanística que vincule la inhibición de C5 con la neutropenia cíclica (hoy inexistente)
- Revisión del prospecto de INVIMA para completar advertencias y contraindicaciones
- Confirmación del mecanismo de acción desde fuentes como DrugBank
- Estudios preclínicos que respalden la plausibilidad biológica antes de considerar ensayos clínicos
- Aclarar la situación regulatoria en Colombia (todos los registros cancelados)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

