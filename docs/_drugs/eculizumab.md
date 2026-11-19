---
layout: default
title: Eculizumab
parent: Solo Predicción del Modelo (L5)
nav_order: 244
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
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

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Eculizumab (traducción no oficial): «Eculizumab, el principio activo de SOLIRIS, es un anticuerpo monoclonal que se une específicamente y con alta afinidad a la proteína del complemento C5, con lo que inhibe su escisión en C5a y C5b e impide la generación del complejo terminal del complemento C5b-9. SOLIRIS inhibe la hemólisis intravascular mediada por el complemento terminal en pacientes con HPN y la microangiopatía trombótica (MAT) mediada por el complemento en pacientes con SHUa.» Texto original en inglés: "Eculizumab, the active ingredient in SOLIRIS, is a monoclonal antibody that specifically binds to the complement protein C5 with high affinity, thereby inhibiting its cleavage to C5a and C5b and preventing the generation of the terminal complement complex C5b-9. SOLIRIS inhibits terminal complement-mediated intravascular hemolysis in PNH patients and complement-mediated thrombotic microangiopathy (TMA) in patients with aHUS." ([DailyMed: Soliris (eculizumab) prescribing information, Alexion Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ebcd67fa-b4d1-4a22-b33d-ee8bf6b9c722), versión del 2026-07-08; consultado el 2026-11-19). Según el conocimiento general, eculizumab es un anticuerpo monoclonal humanizado que inhibe la proteína C5 del complemento y bloquea la cascada terminal del complemento. Su eficacia está documentada en enfermedades mediadas por complemento, como la hemoglobinuria paroxística nocturna (HPN), el síndrome hemolítico urémico atípico (SHUa) y la miastenia gravis.

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
La predicción se basa solo en el modelo TxGNN (aprendizaje profundo) (L5), sin ensayos ni literatura directa. La neutropenia cíclica no es una enfermedad mediada por complemento, y el riesgo de infección por la inhibición de C5 en pacientes neutropénicos es un problema de seguridad importante.

<!-- review:begin co-lic-20261105-eculizumab-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La neutropenia cíclica no es una enfermedad mediada por complemento, y el riesgo de infección por la inhibición de C5 en pacientes neutropénicos es un problema de seguridad importante. Además, los tres registros sanitarios en Colombia están cancelados." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 3 registros sanitarios (vigentes: 3); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-eculizumab-1 -->

**Para avanzar se necesita:**
- Una hipótesis mecanística que vincule la inhibición de C5 con la neutropenia cíclica (hoy inexistente)
- Revisión del prospecto de INVIMA para completar advertencias y contraindicaciones
- Confirmación del mecanismo de acción desde fuentes como DrugBank
- Estudios preclínicos que respalden la plausibilidad biológica antes de considerar ensayos clínicos
- Aclarar la situación regulatoria en Colombia (3 de 3 registros vigentes)

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Además, los tres registros sanitarios en Colombia están cancelados" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Soliris (eculizumab) prescribing information, Alexion Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ebcd67fa-b4d1-4a22-b33d-ee8bf6b9c722) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

