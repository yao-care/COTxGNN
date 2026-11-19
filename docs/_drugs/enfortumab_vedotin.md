---
layout: default
title: Enfortumab Vedotin
parent: Solo Predicción del Modelo (L5)
nav_order: 251
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-20
description: "Enfortumab Vedotin: nueva indicación predicha, Lepra (nivel de evidencia L5). Indicación original: Enfortumab vedotina"
monitor_inn: "enfortumab vedotin"
predicted_indications: ["leprosy", "multiple endocrine neoplasia", "cytomegalovirus infection", "candidiasis", "cerebral infarction", "HIV infectious disease", "homozygous familial hypercholesterolemia", "malignant catarrh", "infectious bovine rhinotracheitis"]
---

# Enfortumab Vedotin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Enfortumab Vedotina: De Indicación Registrada sin Texto Descriptivo a Lepra (Predicción Computacional)
{: .text-alpha }

## Resumen en Una Frase

Enfortumab vedotina es un conjugado anticuerpo-fármaco dirigido contra Nectin-4. En su registro sanitario colombiano la indicación aparece solo como el nombre del principio activo, sin texto descriptivo. El modelo TxGNN predice que podría ser efectivo para **lepra**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción; se trata únicamente de un resultado computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfortumab vedotina (el registro no detalla una indicación en texto) |
| Nueva Indicación Predicha | Lepra |
| Puntaje de Predicción TxGNN | 0.9953 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Enfortumab Vedotin (traducción no oficial): «El enfortumab vedotina-ejfv es un ADC. El anticuerpo es una IgG1 kappa humana dirigida contra la nectina-4, una proteína de adhesión ubicada en la superficie de las células. La molécula pequeña, MMAE, es un agente que altera los microtúbulos, unido al anticuerpo mediante un conector escindible por proteasas.» Texto original en inglés: "Enfortumab vedotin-ejfv is an ADC. The antibody is a human IgG1 kappa directed against Nectin-4, an adhesion protein located on the surface of cells. The small molecule, MMAE, is a microtubule-disrupting agent, attached to the antibody via a protease-cleavable linker." ([DailyMed: Padcev Ejfv (enfortumab vedotin) prescribing information, SEAGEN INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b5631d3e-4604-4363-8f20-11dfc5a4a8ed), versión del 2026-08-04; consultado el 2026-11-19). Según la información conocida, enfortumab vedotina es un conjugado anticuerpo-fármaco que se dirige a Nectin-4 y libera MMAE, un agente que altera los microtúbulos y es citotóxico. Su uso establecido es oncológico, en carcinoma urotelial.

**La predicción no es razonable desde el punto de vista mecanístico.** La lepra es una infección bacteriana, y no existe una justificación plausible para que un fármaco citotóxico dirigido a células tumorales con Nectin-4 la trate. El puntaje alto (0.9953) es una salida del modelo, sin ensayos ni literatura que lo respalden.

Otras predicciones del mismo modelo (por ejemplo, fiebre catarral maligna y rinotraqueítis infecciosa bovina, ambas enfermedades veterinarias) sugieren que muchos puntajes altos reflejan artefactos del modelo TxGNN (aprendizaje profundo) y no señales terapéuticas reales.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para lepra.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20215692 | DOVIQEV® | Polvo estéril para reconstituir a solución inyectable | Enfortumab vedotina |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Conjugado anticuerpo-fármaco (terapia dirigida con carga citotóxica, MMAE) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma, función hepática y renal, glucemia (por las interacciones con antidiabéticos y la posible hiperglucemia) |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 147 interacciones en la consulta (base DDInter). Las que se muestran a continuación son las listadas en los datos compilados:
  - **Mayor**: claritromicina.
  - **Moderada**: antidiabéticos (acarbosa, albiglutida, alogliptina, metformina, pioglitazona, canagliflozina, clorpropamida, dapagliflozina, saxagliptina, dulaglutida, empagliflozina, linagliptina, acetohexamida, ertugliflozina, exenatida, glimepirida, glipizida, gliburida) y aprepitant.
- **Señales de seguridad en la literatura**: un reporte de caso (2026) describe esofagitis ulcerativa difusa grave tras enfortumab vedotina más pembrolizumab en carcinoma urotelial metastásico, y un análisis de farmacovigilancia (FAERS, 2025) evalúa señales de riesgo de los conjugados anticuerpo-fármaco en cáncer de vejiga. Ambos son evidencia de seguridad, no de beneficio terapéutico.

Para advertencias y contraindicaciones formales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para lepra se basa solo en el puntaje del modelo (L5), sin ensayos clínicos, literatura ni vínculo mecanístico plausible.

<!-- review:begin co-lic-20261105-enfortumab_vedotin-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción para lepra se basa solo en el puntaje del modelo (L5), sin ensayos clínicos, literatura ni vínculo mecanístico plausible. Además, el único registro sanitario en Colombia está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-enfortumab_vedotin-1 -->

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank.
- Prospecto de INVIMA con advertencias y contraindicaciones, para el cribado de seguridad.
- Un fundamento biológico que justifique la relación entre Nectin-4/MMAE y la lepra, que hoy no existe.

<!-- review:begin co-lic-20261105-enfortumab_vedotin-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Un fundamento biológico que justifique la relación entre Nectin-4/MMAE y la lepra, que hoy no existe. / Revisar el estado del registro sanitario cancelado, o considerar otras indicaciones predichas con mayor plausibilidad antes de invertir recursos." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-enfortumab_vedotin-2 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Además, el único registro sanitario en Colombia está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Revisar el estado del registro sanitario cancelado, o considerar otras indicaciones predichas con mayor plausibilidad antes de invertir recu" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Padcev Ejfv (enfortumab vedotin) prescribing information, SEAGEN INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b5631d3e-4604-4363-8f20-11dfc5a4a8ed) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

