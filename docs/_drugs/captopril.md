---
layout: default
title: Captopril
parent: Solo Predicción del Modelo (L5)
nav_order: 134
evidence_level: L5
indication_count: 3
monitor_inn: "CAPTOPRIL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia"]
last_modified_at: 2026-11-25
description: "Captopril: nueva indicación predicha, Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) (nivel de evidencia L5). Indicación original: CAPTOPRIL"
---

# Captopril
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Captopril: inhibidor de la enzima convertidora de angiotensina (ECA) → Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)
{: .text-alpha }

## Resumen en Una Frase

Captopril es un inhibidor de la ECA que cuenta con registros sanitarios en Colombia.
El modelo TxGNN predice que podría ser útil para la **enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)**.
Hasta ahora **no hay ensayos clínicos** y solo hay **1 publicación** (un reporte de caso diagnóstico) que no aporta evidencia terapéutica directa.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | CAPTOPRIL |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) |
| Puntaje de Predicción TxGNN | 0,9928 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 5 de 5) |
| Número de Registros Sanitarios | 5 (vigentes: 5) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción. Según el conocimiento general, captopril pertenece a la clase de los inhibidores de la ECA: bloquea la conversión de angiotensina I en angiotensina II y, con ello, reduce la vasoconstricción y la presión arterial.

La hipertensión maligna con compromiso renal se asocia a una activación marcada del sistema renina-angiotensina (SRA). Por eso, desde el punto de vista mecanístico, bloquear este eje es plausible.

Esta relación sigue siendo una hipótesis. La única publicación recuperada describe un caso de renografía con captopril positiva en un paciente con carcinoma renal de células cromófobas. Es un uso diagnóstico, no terapéutico. La predicción se apoya sobre todo en el puntaje del modelo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [28902735](https://pubmed.ncbi.nlm.nih.gov/28902735/) | 2017 | Reporte de caso (diagnóstico) | Clinical Nuclear Medicine | Renografía con captopril positiva sin estenosis de la arteria renal, causada por un carcinoma renal de células cromófobas; la hipertensión dependiente de renina se resolvió tras la nefrectomía. No evalúa un efecto terapéutico en la enfermedad predicha. |

## Información de Mercado en Colombia

Registros sanitarios disponibles.

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 31803 | CAPTOPRIL25 MG | TABLETA | CAPTOPRIL | Vigente |
| 32119 | CAPTOPRIL 50 MG | TABLETA | CAPTOPRIL | Vigente |
| 54972 | CAPTOPRIL 25 MG TABLETAS | TABLETA | CAPTOPRIL | Vigente |
| 54973 | CAPTOPRIL TABLETAS 50 MG | TABLETA | CAPTOPRIL | Vigente |
| 19956814 | CAPTOPRIL 50MG TABLETA | TABLETA | CAPTOPRIL | Vigente |

Se muestran los 5 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

<!-- review:begin co-lic-20261124b-captopril-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "La lista puede ser parcial." Eliminado: advertía que la lista de registros podría ser parcial. La tabla de Información de Mercado en Colombia se genera a partir de los datos del INVIMA (Código Único de Medicamentos, datos al 2026-11-23) e indica cuántos registros muestra del total. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261124b-captopril-1 -->

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. Entre las listadas, la mayoría son de nivel moderado:
  - Corticoides: hidrocortisona, dexametasona, betametasona, triamcinolona y budesonida.
  - Antidiabéticos: metformina, alogliptina, canagliflozina, dapagliflozina, empagliflozina, ertugliflozina, exenatida, clorpropamida y acetohexamida.
  - Otros: bupropión, morfina, ácido acetilsalicílico y dronabinol.
  - Antiácidos (hidróxido de aluminio y carbonato de calcio): interacción de nivel menor.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
- No hay ensayos clínicos ni estudios que evalúen captopril en la enfermedad renal hipertensiva maligna. La única publicación es un reporte de caso diagnóstico, por lo que el nivel de evidencia es L5 y la predicción se apoya solo en el modelo y en un mecanismo plausible.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción.
- Revisión sistemática de la literatura sobre inhibidores de la ECA en hipertensión maligna con compromiso renal.
- Información de seguridad del prospecto aprobado, en especial en pacientes con insuficiencia renal.
- Estudios clínicos o datos observacionales que evalúen directamente esta indicación.
- Verificación de la vigencia de cada registro sanitario.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-24 | Eliminado: "La lista puede ser parcial." | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

