---
layout: default
title: Phenylephrine
parent: Solo Predicción del Modelo (L5)
nav_order: 325
evidence_level: L5
indication_count: 3
---

# Phenylephrine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Fenilefrina: De Combinaciones de Paracetamol (sin Psicolépticos) a Enfermedad de la Cavidad Nasal

## Resumen en Una Frase

La fenilefrina es un agonista alfa-1 adrenérgico que se usa como descongestionante nasal y aparece en muchas combinaciones para el resfriado y la gripe. En Colombia, sus registros sanitarios figuran bajo la categoría "paracetamol, combinaciones excluyendo psicolépticos".
El modelo TxGNN predice que podría ser efectiva para **enfermedad de la cavidad nasal**, con **8 ensayos clínicos** y **8 publicaciones** relacionados.
Solo un ensayo y un ECA prueban directamente una formulación con fenilefrina. Además, el uso descongestionante nasal tópico ya es un uso establecido, por lo que esto se parece más a un uso conocido que a un reposicionamiento novedoso.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Paracetamol, combinaciones excluyendo psicolépticos (categoría de clasificación del registro, no una indicación clínica detallada) |
| Nueva Indicación Predicha | Enfermedad de la cavidad nasal |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L2 (con reservas, ver más abajo) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro de origen. Según la información farmacológica conocida, la fenilefrina es un agonista de los receptores alfa-1 adrenérgicos (subtipos 1A, 1B y 1D). Su aplicación tópica causa vasoconstricción de la mucosa. Esto reduce la congestión y el sangrado y mejora la visión del campo endoscópico o quirúrgico.

Ese efecto encaja de forma natural con las afecciones de la cavidad nasal. La propia información de DrugBank indica que la fenilefrina ya se usa para tratar la congestión nasal, sola en descongestionantes nasales o en combinaciones para el resfriado. Por eso esta predicción está más cerca de un uso establecido que de una indicación realmente nueva.

La "indicación original" que aparece en los registros colombianos es una categoría de clasificación de productos combinados con paracetamol, no una indicación clínica específica. La comparación con la nueva indicación debe leerse con esa salvedad.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03380715](https://clinicaltrials.gov/study/NCT03380715) | N/A | Completado | 106 | Co-fenilcaína (lidocaína + fenilefrina) en aerosol nasal frente a nebulización antes de la nasoendoscopia rígida. Es el único ensayo que prueba directamente una formulación con fenilefrina en la cavidad nasal. |
| [NCT06443255](https://clinicaltrials.gov/study/NCT06443255) | Fase 3 | Completado | 16 | Cocaína, lidocaína/xilometazolina y solución salina para analgesia intranasal. La fenilefrina no es un brazo del estudio, por lo que no cuenta como evidencia L1. |
| [NCT00562120](https://clinicaltrials.gov/study/NCT00562120) | Fase 2 | Completado | 21 | Estudio cruzado doble ciego, controlado con placebo, de un antagonista H3 sobre la congestión tras provocación alérgica nasal. El brazo con fenilefrina no se puede confirmar y requiere verificación. |
| [NCT03228914](https://clinicaltrials.gov/study/NCT03228914) | Fase 4 | Completado | 20 | Oximetazolina tópica frente a otro vasoconstrictor sobre la pérdida de sangre y la visualización en cirugía endoscópica de senos. El comparador podría ser fenilefrina, pero no está confirmado. |
| [NCT06457100](https://clinicaltrials.gov/study/NCT06457100) | Fase 1/2 | Desconocido | 60 | Infusión perioperatoria de esmolol frente a lidocaína en cirugía endoscópica funcional de senos. La fenilefrina no es la intervención. |
| [NCT03962634](https://clinicaltrials.gov/study/NCT03962634) | Fase 2 | Terminado | 3 | Kovanaze (tetracaína/oximetazolina) nasal frente a articaína en anestesia dental. Otro fármaco y otro propósito. |
| [NCT02993770](https://clinicaltrials.gov/study/NCT02993770) | N/A | Desconocido | 120 | Dacriocistorrinostomía endonasal endoscópica frente a externa. Comparación de técnicas quirúrgicas. |
| [NCT04104789](https://clinicaltrials.gov/study/NCT04104789) | Fase 2 | Retirado | 0 | Kovanaze frente a articaína. Retirado sin participantes, por lo que no aporta datos. |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [15854186](https://pubmed.ncbi.nlm.nih.gov/15854186/) | 2005 | ECA | Int J Clin Pract | Doble ciego con 98 pacientes. Co-fenilcaína en aerosol frente a placebo antes de la nasofibroscopia flexible. El procedimiento causó poco dolor en ambos grupos, sin diferencias significativas en dolor ni malestar general. |
| [25133491](https://pubmed.ncbi.nlm.nih.gov/25133491/) | 2014 | ECA | PLoS One | Ácido tranexámico tópico sobre el sangrado y la calidad del campo quirúrgico en cirugía endoscópica de senos por rinosinusitis crónica. No evalúa fenilefrina. |
| [40899890](https://pubmed.ncbi.nlm.nih.gov/40899890/) | 2025 | Estudio experimental y clínico | Vestn Otorinolaringol | Seguridad y eficacia del aerosol Polydexa con fenilefrina en rinosinusitis aguda. Busca aportar evidencia para reducir el uso de antibióticos sistémicos. |
| [37970776](https://pubmed.ncbi.nlm.nih.gov/37970776/) | 2023 | Revisión | Vestn Otorinolaringol | Enfoque patogénico del tratamiento de enfermedades inflamatorias de la nariz y los senos paranasales, para reducir la hiperemia y el edema de la mucosa. |
| [37184554](https://pubmed.ncbi.nlm.nih.gov/37184554/) | 2023 | Observacional/Revisión | Vestn Otorinolaringol | Estado endoscópico de la mucosa nasal tras usar Polydexa con fenilefrina (dexametasona + neomicina + polimixina B + fenilefrina). |
| [9780066](https://pubmed.ncbi.nlm.nih.gov/9780066/) | 1998 | Cohorte | Int J Pediatr Otorhinolaryngol | Evaluación por rinometría acústica de la cavidad nasal y la nasofaringe tras adenoidectomía y amigdalectomía. |
| [1375136](https://pubmed.ncbi.nlm.nih.gov/1375136/) | 1992 | Estudio in vitro | Clin Otolaryngol Allied Sci | Efecto de fármacos usados en enfermedades nasales sobre la frecuencia del batido ciliar in vitro. |
| [7378007](https://pubmed.ncbi.nlm.nih.gov/7378007/) | 1980 | Reporte de caso | Arch Ophthalmol | Toxicidad por cocaína intranasal durante una dacriocistorrinostomía. Un paciente tuvo además una reacción a fenilefrina intranasal (Neo-Synephrine). |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19984 | PAX® DIA GRANULADO (EUROFARMA COLOMBIA S.A.S.) | Gránulos | Paracetamol, combinaciones excluyendo psicolépticos |

Los 5 registros devueltos en los datos son idénticos, por lo que se muestran una sola vez. En total hay 20 registros sanitarios. Las formas farmacéuticas identificadas son gránulos y tableta cubierta con película (vía oral).

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: la consulta terminó sin interacciones con otros medicamentos. Los 3 resultados son datos farmacológicos de dianas: agonismo sobre los receptores alfa-1A, alfa-1B y alfa-1D (genes ADRA1A, ADRA1B, ADRA1D).
- **Señal de seguridad en la literatura**: un reporte de caso de 1980 describe toxicidad con cocaína intranasal y una reacción adicional a fenilefrina intranasal. Advierte del riesgo de combinar simpaticomiméticos o fármacos alfa-moduladores, especialmente en pacientes con enfermedad cardiovascular hipertensiva.
- **Precauciones sugeridas**: limitar el uso a la vía tópica o de corta duración, y vigilar la presión arterial y la congestión de rebote.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
El mecanismo alfa-1 vasoconstrictor es plausible para afecciones nasales, y existe un ECA con una formulación de fenilefrina/lidocaína (co-fenilcaína) y un ensayo completado con formulación que la contiene. Sin embargo, el único ensayo de Fase 3 no prueba fenilefrina, el ensayo de Fase 2 no está confirmado y el uso descongestionante nasal ya es establecido. Por eso el nivel L2 es provisional.

**Para avanzar se necesita:**
- Confirmar el brazo con fenilefrina y la condición estudiada en NCT00562120, y el comparador en NCT03228914.
- Obtener y revisar el prospecto de INVIMA para advertencias y contraindicaciones.
- Completar los datos del mecanismo de acción desde DrugBank.
- Definir un plan de monitoreo de presión arterial y congestión de rebote, con uso tópico y de corta duración.

Las otras dos predicciones quedan en Hold: laringofaringitis aguda (L5, sin ensayos ni literatura) y cefalea autonómica trigeminal (L4, solo estudios pupilométricos diagnósticos, sin evidencia de beneficio terapéutico).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

