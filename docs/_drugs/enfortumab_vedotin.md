---
layout: default
title: Enfortumab Vedotin
parent: Solo Predicción del Modelo (L5)
nav_order: 251
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
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
| Puntaje de Predicción TxGNN | 99.53% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, enfortumab vedotina es un conjugado anticuerpo-fármaco que se dirige a Nectin-4 y libera MMAE, un agente que altera los microtúbulos y es citotóxico. Su uso establecido es oncológico, en carcinoma urotelial.

**La predicción no es razonable desde el punto de vista mecanístico.** La lepra es una infección bacteriana, y no existe una justificación plausible para que un fármaco citotóxico dirigido a células tumorales con Nectin-4 la trate. El puntaje alto (99.53%) es una salida del modelo, sin ensayos ni literatura que lo respalden.

Otras predicciones del mismo modelo (por ejemplo, fiebre catarral maligna y rinotraqueítis infecciosa bovina, ambas enfermedades veterinarias) sugieren que muchos puntajes altos reflejan artefactos del grafo de conocimiento y no señales terapéuticas reales.

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
| 20215692 (cancelado) | DOVIQEV® | Polvo estéril para reconstituir a solución inyectable | Enfortumab vedotina |

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
La predicción para lepra se basa solo en el puntaje del modelo (L5), sin ensayos clínicos, literatura ni vínculo mecanístico plausible. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank.
- Prospecto de INVIMA con advertencias y contraindicaciones, para el cribado de seguridad.
- Un fundamento biológico que justifique la relación entre Nectin-4/MMAE y la lepra, que hoy no existe.
- Revisar el estado del registro sanitario cancelado, o considerar otras indicaciones predichas con mayor plausibilidad antes de invertir recursos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

