---
layout: default
title: Eculizumab
parent: Solo Predicción del Modelo (L5)
nav_order: 244
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
description: "Eculizumab: nueva indicación predicha, Hematopoyesis cíclica (nivel de evidencia L5). Indicación original: ECULIZUMAB"
monitor_inn: "ECULIZUMAB"
predicted_indications: ["cyclic hematopoiesis", "autosomal recessive severe congenital neutropenia due to JAGN1 deficiency", "X-linked severe congenital neutropenia", "congenital neutropenia-myelofibrosis-nephromegaly syndrome", "adult idiopathic neutropenia", "autosomal recessive severe congenital neutropenia due to CXCR2 deficiency", "primary immunodeficiency syndrome due to p14 deficiency", "autosomal recessive severe congenital neutropenia due to CSF3R deficiency", "severe congenital neutropenia", "primary release disorder of platelets"]
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

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Eculizumab: De Indicación No Especificada en el Registro a Hematopoyesis Cíclica
{: .text-alpha }

## Resumen en Una Frase

Eculizumab es un anticuerpo monoclonal inhibidor del complemento (C5). En el registro sanitario colombiano figura solo con el nombre del principio activo, sin una indicación detallada.
El modelo TxGNN (aprendizaje profundo) predice que podría ser efectivo para **hematopoyesis cíclica**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción; se trata únicamente de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | ECULIZUMAB (el registro no detalla la indicación) |
| Nueva Indicación Predicha | Hematopoyesis cíclica |
| Puntaje de Prediccion TxGNN | 0.9997 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 3 de 3) |
| Número de Registros Sanitarios | 3 (vigentes: 3) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según el conocimiento general, eculizumab es un anticuerpo monoclonal humanizado que inhibe la proteína C5 del complemento y bloquea la cascada terminal del complemento. Su eficacia está documentada en enfermedades mediadas por complemento, como la hemoglobinuria paroxística nocturna (HPN), el síndrome hemolítico urémico atípico (SHUa) y la miastenia gravis.

La neutropenia cíclica, en cambio, se debe principalmente a mutaciones en el gen *ELANE* y no es una enfermedad mediada por complemento. Por ello, **no existe una justificación mecanística clara** para inhibir C5 en esta condición. El puntaje alto (0.9997) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica ni clínica.

Las otras nueve predicciones principales (distintas formas de neutropenia congénita, neutropenia idiopática del adulto, deficiencia de p14 y trastorno de liberación plaquetaria) tienen puntajes similares (0.9994–0.9996) y presentan la misma falta de plausibilidad mecanística.

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
| 20164753 | ELIZARIA® 10 MG/ML | Solución concentrada para infusión | ECULIZUMAB | Vigente |
| 20254329 | BKEMV® 300 MG | Solución concentrada para infusión | ECULIZUMAB | Vigente |
| 20028870 | SOLIRIS® 300 MG | Solución concentrada para infusión | ECULIZUMAB | Vigente |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 4 interacciones de nivel **menor** con inmunoglobulina G humana (intravenosa, subcutánea, intramuscular y combinación intravenosa/subcutánea).
- **Riesgo adicional (según el análisis de la predicción)**: la inhibición del complemento aumenta el riesgo de infecciones, en particular meningocócicas. Esto es especialmente preocupante en poblaciones con neutropenia o inmunodeficiencia.

Consultar el prospecto para información sobre advertencias y contraindicaciones.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo TxGNN (aprendizaje profundo) (L5), sin ensayos ni literatura directa. La neutropenia cíclica no es una enfermedad mediada por complemento, y el riesgo de infección por la inhibición de C5 en pacientes neutropénicos es un problema de seguridad importante. Además, los tres registros sanitarios en Colombia están cancelados.

**Para avanzar se necesita:**
- Una hipótesis mecanística que vincule la inhibición de C5 con la neutropenia cíclica (hoy inexistente)
- Revisión del prospecto de INVIMA para completar advertencias y contraindicaciones
- Confirmación del mecanismo de acción desde fuentes como DrugBank
- Estudios preclínicos que respalden la plausibilidad biológica antes de considerar ensayos clínicos
- Aclarar la situación regulatoria en Colombia (3 de 3 registros vigentes)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

