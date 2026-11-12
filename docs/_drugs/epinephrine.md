---
layout: default
title: Epinephrine
parent: Solo Predicción del Modelo (L5)
nav_order: 257
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-12
description: "Epinephrine: nueva indicación predicha, Enfermedad pulmonar obstructiva (nivel de evidencia L5). Indicación original: Epinefrina"
monitor_inn: "Epinephrine"
predicted_indications: ["obstructive lung disease", "Rienhoff syndrome", "respiratory malformation"]
---

# Epinephrine
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

## Epinefrina: De Indicación Original No Especificada a Enfermedad Pulmonar Obstructiva
{: .text-alpha }

## Resumen en Una Frase

La epinefrina (adrenalina) cuenta en Colombia con 14 registros sanitarios cuyo texto de indicación aprobada se limita al nombre del producto ("Epinefrina"), por lo que no se dispone de una indicación original detallada.
El modelo TxGNN predice que podría ser efectiva para **enfermedad pulmonar obstructiva**,
con **15 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección.

<!-- review:begin co-lic-20261112-epinephrine-1 -->

> **Corrección de revisión (2026-11-12)**: Texto original: "cuenta en Colombia con un registro sanitario cuyo texto" Corregido según los datos del INVIMA (Código Único de Medicamentos, datos al 2026-11-05): 14 registros sanitarios, de los cuales 12 vigentes y 2 vigentes pero temporalmente no comercializados. Las cifras actuales están en el Resumen rápido. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261112-epinephrine-1 -->

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Epinefrina (el registro sanitario no detalla una indicación específica) |
| Nueva Indicación Predicha | Enfermedad pulmonar obstructiva |
| Puntaje de Predicción TxGNN | 0.9971 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 12 de 14) |
| Número de Registros Sanitarios | 14 (vigentes: 12) |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la farmacología conocida, la epinefrina es un agonista adrenérgico no selectivo (alfa y beta). La activación de los receptores beta-2 relaja el músculo liso bronquial y produce broncodilatación, lo que es coherente con el alivio de la obstrucción reversible de la vía aérea en el asma.

Además, la vasoconstricción mucosa mediada por receptores alfa-1 puede reducir el edema de la vía aérea, algo relevante en la bronquiolitis y el crup. El puntaje alto de TxGNN (0.9971) es consistente con esta farmacología.

Cabe señalar que la indicación original y el mecanismo de acción no constan en los datos. Parte de la evidencia corresponde a formulaciones inhaladas (E004, Primatene Mist) o a la vía intramuscular, que no coinciden con la solución inyectable registrada en Colombia.

<!-- review:begin co-lic-20261105-epinephrine-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Cabe señalar que la indicación original y el mecanismo de acción no constan en los datos, y que el único registro sanitario está cancelado, por lo que debe verificarse la situación regulatoria de formulaciones específicas." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 14 registros sanitarios (vigentes: 12); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-epinephrine-1 -->

---

## Evidencia de Ensayos Clínicos

Se listan los 10 ensayos más relevantes (de 15 identificados), priorizando los de mayor fase y relevancia directa.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01357642](https://clinicaltrials.gov/study/NCT01357642) | Fase 3 | Completado | 373 | Eficacia y seguridad a 12 semanas de epinefrina inhalada (HFA-MDI) frente a placebo y Primatene Mist en adolescentes y adultos con asma |
| [NCT01476904](https://clinicaltrials.gov/study/NCT01476904) | Fase 3 | Completado | 208 | Extensión de seguridad de 3 meses (perfil de 6 meses) de epinefrina inhalada frente a placebo en asma |
| [NCT01460511](https://clinicaltrials.gov/study/NCT01460511) | Fase 3 | Completado | 70 | E004 frente a placebo durante 4 semanas en niños de 4 a 11 años con asma |
| [NCT01737905](https://clinicaltrials.gov/study/NCT01737905) | Fase 3 | Completado | 28 | Estudio cruzado de dosis única de E004 en niños con asma |
| [NCT01705964](https://clinicaltrials.gov/study/NCT01705964) | Fase 4 | Completado | 49 | Epinefrina intramuscular como adyuvante de broncodilatadores inhalados en exacerbación grave de asma pediátrica |
| [NCT01834820](https://clinicaltrials.gov/study/NCT01834820) | Fase 4 | Completado | 120 | Piloto de epinefrina, dexametasona y solución salina hipertónica en bronquiolitis infantil |
| [NCT00817466](https://clinicaltrials.gov/study/NCT00817466) | Fase 4 | Desconocido | 500 | Tratamiento inhalado óptimo en bronquiolitis aguda en menores de 12 meses |
| [NCT04207840](https://clinicaltrials.gov/study/NCT04207840) | Fase 4 | Completado | 28 | Exposición sistémica de Primatene Mist frente a epinefrina intramuscular y ProAir en adultos sanos (enfoque farmacocinético) |
| [NCT01255709](https://clinicaltrials.gov/study/NCT01255709) | Fase 2 | Completado | 24 | Estudio farmacocinético cruzado de epinefrina inhalada en voluntarios sanos |
| [NCT00114478](https://clinicaltrials.gov/study/NCT00114478) | No aplica | Desconocido | 600 | Epinefrina frente a albuterol en bronquiolitis |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35093318](https://pubmed.ncbi.nlm.nih.gov/35093318/) | 2022 | ECA | The Journal of Pediatrics | Ensayo pragmático de corticosteroides y epinefrina nebulizada en bronquiolitis en cuidados intensivos pediátricos |
| [33893229](https://pubmed.ncbi.nlm.nih.gov/33893229/) | 2021 | Metaanálisis en red | Pediatrics | Comparación de intervenciones para bronquiolitis en atención aguda |
| [21678340](https://pubmed.ncbi.nlm.nih.gov/21678340/) | 2011 | Revisión sistemática | Cochrane Database Syst Rev | Epinefrina para bronquiolitis |
| [14974006](https://pubmed.ncbi.nlm.nih.gov/14974006/) | 2004 | Revisión sistemática | Cochrane Database Syst Rev | Epinefrina para bronquiolitis (versión anterior) |
| [35953216](https://pubmed.ncbi.nlm.nih.gov/35953216/) | 2022 | Revisión | Emerg Med Clin North Am | Evaluación y manejo de exacerbaciones de asma y EPOC en urgencias |
| [30488718](https://pubmed.ncbi.nlm.nih.gov/30488718/) | 2019 | Revisión | Expert Rev Respir Med | Estrategias terapéuticas en bronquiolitis pediátrica: epinefrina racémica, corticosteroides, solución salina hipertónica y oxigenoterapia de alto flujo |
| [21157348](https://pubmed.ncbi.nlm.nih.gov/21157348/) | 2011 | Revisión | Curr Opin Pediatr | Actualización del manejo de la bronquiolitis |
| [23393929](https://pubmed.ncbi.nlm.nih.gov/23393929/) | 2012 | Revisión | Duodecim | Bronquiolitis: la epinefrina racémica inhalada como opción cuando se requiere |
| [11940264](https://pubmed.ncbi.nlm.nih.gov/11940264/) | 2002 | Revisión | Critical Care | Revisión clínica del asma grave |
| [20876171](https://pubmed.ncbi.nlm.nih.gov/20876171/) | 2010 | Análisis económico | Pediatrics | Costo-efectividad de epinefrina y dexametasona en bronquiolitis |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20032463 | Epinefrina solución inyectable 1 mg/1 mL (Laboratorio Biosano S.A.) | Solución inyectable | Epinefrina |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** el grafo de conocimiento TxGNN (PrimeKG) asocia la epinefrina con contraindicación en las siguientes condiciones: hipertensión, enfermedad cardiovascular y cardiopatía, infarto de miocardio, enfermedad coronaria, fibrilación auricular, trastornos de la conducción cardíaca, paro cardíaco súbito, diabetes mellitus y cetoacidosis diabética, hipertiroidismo, glaucoma de ángulo cerrado, epilepsia, enfermedad hepática e insuficiencia hepática, enfermedad renal, hiperplasia prostática benigna, enfermedad de la vesícula biliar, deficiencia de potasio, miastenia gravis, insuficiencia respiratoria, hemoglobinopatía y deficiencia de butirilcolinesterasa, entre otras.
- **Interacciones farmacológicas:** se identificaron 100 interacciones. Entre las de nivel **mayor** figuran los antidepresivos tricíclicos **amitriptilina** y **amoxapina**. Entre las de nivel **moderado** se incluyen betabloqueadores (acebutolol, atenolol, betaxolol), agonistas beta-2 (formoterol, salbutamol, arformoterol), estimulantes (metilfenidato, anfetamina, atomoxetina, benzfetamina), antidiabéticos (acarbosa, acetohexamida, albiglutida, alogliptina) y antipsicóticos (amisulprida, aripiprazol, asenapina).

Para advertencias y contraindicaciones del prospecto, consultar el inserto del producto, ya que no se dispone de esa información en los datos compilados.

---

## Otras Indicaciones Predichas (Contexto)

| Indicación | Puntaje TxGNN | Nivel de Evidencia | Recomendación |
|------|------|------|------|
| Anafilaxia inducida por ejercicio dependiente de alimentos | 0.9957 | L5 | Pregunta de investigación. La epinefrina ya es el tratamiento estándar de primera línea en anafilaxia, por lo que se trata más de práctica establecida que de reposicionamiento; no hay ensayos específicos |
| Síndrome de Rienhoff | 0.9957 | L5 | Hold. Sin ensayos ni literatura y sin vínculo mecanístico plausible; el agonismo adrenérgico podría implicar riesgo cardiovascular en trastornos del tejido conectivo |
| Malformación respiratoria | 0.9956 | L3 | Pregunta de investigación. Solo un ensayo de Fase 1 en taquipnea transitoria del recién nacido (que no es una malformación estructural); la literatura es heterogénea y poco relacionada |

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Para enfermedad pulmonar obstructiva existen tres ensayos de Fase 3 completados con epinefrina inhalada en asma (más de 600 participantes en conjunto), además de revisiones sistemáticas Cochrane en bronquiolitis. Sin embargo, la evidencia corresponde en gran parte a formulaciones inhaladas, por lo que se recomienda avanzar con salvaguardas.

<!-- review:begin co-lic-20261105-epinephrine-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Sin embargo, la evidencia corresponde en gran parte a formulaciones inhaladas, y el único registro colombiano (solución inyectable) está cancelado, por lo que se recomienda avanzar con salvaguardas." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 14 registros sanitarios (vigentes: 12); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-epinephrine-2 -->

**Para avanzar se necesita:**
- Verificar la situación regulatoria actual de la epinefrina en Colombia y la disponibilidad de formulaciones vigentes (inhalada o inyectable) compatibles con la evidencia.
- Obtener el prospecto en INVIMA para completar advertencias y contraindicaciones.
- Completar los datos del mecanismo de acción desde DrugBank.
- Definir la población objetivo (asma, EPOC o bronquiolitis), ya que la evidencia es heterogénea entre adultos y niños.
- Plan de monitoreo cardiovascular, dadas las numerosas contraindicaciones cardiovasculares y las interacciones mayores con antidepresivos tricíclicos.
- Considerar la anafilaxia inducida por ejercicio dependiente de alimentos solo como línea de investigación secundaria, y mantener en espera el síndrome de Rienhoff.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "y que el único registro sanitario está cancelado, por lo que debe verificarse la situación regulatoria de formulaciones específicas" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "y el único registro colombiano (solución inyectable) está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-12 | Número de registros sanitarios: 1 → 14 | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

