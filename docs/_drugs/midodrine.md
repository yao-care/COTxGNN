---
layout: default
title: Midodrine
parent: Solo Predicción del Modelo (L5)
nav_order: 443
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
description: "Midodrine: nueva indicación predicha, Prionopatía sensible a proteasa de forma variable (nivel de evidencia L5). Indicación original: \"MIDODRINA\""
monitor_inn: "midodrine"
predicted_indications: ["variably protease-sensitive prionopathy", "faciodigitogenital syndrome", "attention deficit-hyperactivity disorder", "hypotensive disorder", "attention deficit hyperactivity disorder, inattentive type", "sinoatrial node disease", "monogenic obesity", "specific developmental disorder", "obsolete hypertelorism (disease)", "sinoatrial block"]
---

# Midodrine
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

## Midodrina: De una Indicación No Detallada en el Registro a Prionopatía Sensible a Proteasa de Forma Variable
{: .text-alpha }

## Resumen en Una Frase

La midodrina es un agonista alfa-1 adrenérgico de acción periférica. En Colombia sus registros sanitarios solo figuran con el nombre del principio activo, sin detallar la indicación. El modelo TxGNN predice que podría ser efectiva para **prionopatía sensible a proteasa de forma variable**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | "MIDODRINA" (el registro sanitario no detalla la indicación aprobada) |
| Nueva Indicación Predicha | Prionopatía sensible a proteasa de forma variable |
| Puntaje de Predicción TxGNN | 0.9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 2 de 2) |
| Número de Registros Sanitarios | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

**No se identifica un vínculo mecanístico plausible.** La midodrina actúa a través de su metabolito activo, la desglimidodrina, un agonista selectivo alfa-1 adrenérgico. Este metabolito aumenta el tono vascular arterial y venoso y eleva la presión arterial. Es un efecto periférico y no tiene relevancia conocida para el plegamiento anómalo de la proteína priónica ni para la neurodegeneración.

El puntaje tan alto del modelo (0.9999) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica de una relación farmacológica real. No hay datos que relacionen la indicación original con esta enfermedad. Los datos compilados para este informe tampoco incluyen una similitud formal entre ambas indicaciones.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20202650 | SYNCOPGOR® | Tableta | MIDODRINA | Vigente |
| 20022446 | MIDODRINA 5 MG | Tableta recubierta | MIDODRINA | Vigente |

Ambos registros corresponden a monofármacos de administración oral.

<!-- review:begin co-lic-20261105-midodrine-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Ambos registros corresponden a monofármacos de administración oral. Actualmente no hay registros vigentes." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 2 registros sanitarios (vigentes: 2); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-midodrine-1 -->

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas por el grafo de conocimiento (no provienen del prospecto):** feocromocitoma (de glándula suprarrenal), cáncer de duodeno, cáncer de intestino delgado, cáncer de corazón, cáncer de glándula suprarrenal, paraganglioma simpático, tirotoxicosis, hipertiroidismo y enfermedad de Graves.
- **Interacciones farmacológicas:** se identificaron 81 interacciones en total. Entre las de nivel moderado destacan:
  - vasoconstrictores y simpaticomiméticos: epinefrina (incluidas las formas oftálmica y tópica), efedrina (incluida la nasal) e isometepteno;
  - anorexígenos y estimulantes: fentermina, dietilpropión, mazindol, sibutramina y lorcaserina;
  - otros: bupropión, trospio, rolapitant y fenilbutirato de glicerol.

  Entre las de nivel menor figuran ranitidina, cimetidina y metformina.
- **Riesgos relacionados con el perfil farmacológico (según el análisis del caso):** la midodrina puede causar bradicardia refleja, lo que es relevante en enfermedades del nodo sinusal.

Para advertencias y contraindicaciones oficiales, consultar el prospecto aprobado por INVIMA.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo, sin ensayos clínicos, sin literatura y sin un mecanismo plausible (nivel L5). Esta predicción no debe avanzar.

<!-- review:begin co-lic-20261105-midodrine-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, el producto no tiene registros sanitarios vigentes en Colombia. Esta predicción no debe avanzar." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 2 registros sanitarios (vigentes: 2); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-midodrine-2 -->

**Para avanzar se necesita:**
- Un fundamento mecanístico que justifique la relación entre la agonista alfa-1 periférica y la patología priónica. Hoy no existe.
- Datos preclínicos o clínicos que respalden la hipótesis.
- Obtener el prospecto de INVIMA para completar el análisis de seguridad.
- Aclarar la situación regulatoria.

<!-- review:begin co-lic-20261105-midodrine-3 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Aclarar la situación regulatoria, ya que los dos registros están cancelados." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 2 registros sanitarios (vigentes: 2); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-midodrine-3 -->

**Nota sobre otras predicciones del mismo fármaco:** entre las predicciones evaluadas, la de **trastorno hipotensivo** (puntaje 0.9990) tiene el respaldo más sólido. Cuenta con un ensayo de Fase 2 completado en lesión medular (NCT02893553, n=21), con múltiples revisiones y guías sobre hipotensión ortostática, y un vínculo mecanístico directo (nivel L2, "Proceed with Guardrails"). Sin embargo, esta predicción coincide en gran medida con el uso ya conocido de la midodrina, por lo que valida el modelo más que constituir un reposicionamiento novedoso. Si se busca una candidata con potencial real, conviene evaluarla en un informe específico.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Actualmente no hay registros vigentes" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Además, el producto no tiene registros sanitarios vigentes en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "ya que los dos registros están cancelados" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

