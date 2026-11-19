---
layout: default
title: Filgrastim
parent: Solo Predicción del Modelo (L5)
nav_order: 285
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
description: "Filgrastim: nueva indicación predicha, Trastorno primario de liberación plaquetaria (nivel de evidencia L5). Indicación original: FILGRASTIM"
monitor_inn: "FILGRASTIM"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "Scott syndrome", "hemorrhagic disorder due to a constitutional thrombocytopenia", "bleeding diathesis due to a collagen receptor defect", "C1 inhibitor deficiency", "serpinopathy with toxic serpin polymerization", "fetal and neonatal alloimmune thrombocytopenia", "platelet-type bleeding disorder"]
---

# Filgrastim
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

## Filgrastim: De Indicación No Especificada a Trastorno primario de liberación plaquetaria
{: .text-alpha }

## Resumen en Una Frase

Filgrastim es un análogo del factor estimulante de colonias de granulocitos (G-CSF) que actúa sobre el linaje de los neutrófilos. En el registro sanitario colombiano disponible, su indicación original aparece únicamente como "FILGRASTIM", sin una descripción clínica detallada.
El modelo TxGNN predice que podría ser efectivo para el **trastorno primario de liberación plaquetaria**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | FILGRASTIM (el registro no detalla la indicación clínica) |
| Nueva Indicación Predicha | Trastorno primario de liberación plaquetaria |
| Puntaje de Predicción TxGNN | 1.0000 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 2 de 2) |
| Número de Registros Sanitarios | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Filgrastim (traducción no oficial): «Los factores estimulantes de colonias son glucoproteínas que actúan sobre las células hematopoyéticas uniéndose a receptores específicos de la superficie celular y estimulando la proliferación, el compromiso de diferenciación y cierta activación funcional de las células terminales. El G-CSF endógeno es un factor estimulante de colonias específico de linaje que producen los monocitos, los fibroblastos y las células endoteliales.» Texto original en inglés: "Colony-stimulating factors are glycoproteins which act on hematopoietic cells by binding to specific cell surface receptors and stimulating proliferation‚ differentiation commitment‚ and some end-cell functional activation. Endogenous G-CSF is a lineage-specific colony-stimulating factor that is produced by monocytes‚ fibroblasts, and endothelial cells." ([DailyMed: Releuko (filgrastim) prescribing information, Amneal Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=74e1ec6e-1630-4654-895c-2bd355f939e7), versión del 2026-11-10; consultado el 2026-11-19). Según la información conocida, filgrastim es un análogo del G-CSF que se une al receptor de G-CSF y estimula la producción, maduración y función de los neutrófilos.

Los trastornos de liberación plaquetaria primaria son defectos funcionales de las plaquetas (alteración de la secreción de gránulos), sin una relación evidente con la señalización del G-CSF. El puntaje alto de TxGNN proviene de relaciones en la red de conocimiento y no de un respaldo mecanístico o clínico.

Por ello, la plausibilidad biológica de esta predicción es baja. Las otras indicaciones predichas por el modelo (pseudo-enfermedad de von Willebrand, trombastenia de Glanzmann, síndrome de Scott, entre otras) tampoco muestran un vínculo mecanístico con el G-CSF, y todas se mantienen en nivel L5 sin ensayos ni literatura.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para el trastorno primario de liberación plaquetaria.

*Nota:* para la indicación de rango 10 ("trastorno hemorrágico de tipo plaquetario") se identificaron siete ensayos de trasplante de células madre hematopoyéticas en neoplasias hematológicas, en los que filgrastim probablemente participa solo como agente de apoyo (movilización o recuperación de neutrófilos). Ninguno evalúa trastornos de la función plaquetaria y todos se calificaron con relevancia baja (C), por lo que no respaldan la indicación principal.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20002046 | FILGRASTIM 300 MCG/ML SOLUCIÓN INYECTABLE (MEGALABS COLOMBIA S.A.S) | Solución inyectable | FILGRASTIM |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas:** se identificaron 100 interacciones potenciales, y las principales listadas son de nivel moderado: yobenguano (I-131), fludesoxiglucosa (18F), ibritumomab tiuxetán, tositumomab (con y sin I-131), levamisol, trimetrexato, mercaptopurina, abemaciclib, paclitaxel, acalabrutinib, aldesleukina, alemtuzumab, altretamina, trióxido de arsénico, asparaginasa de *E. coli*, avapritinib, azacitidina, belantamab mafodotina y bendamustina.

Para advertencias y contraindicaciones, consultar el prospecto del producto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5), sin ensayos ni literatura, y no existe un vínculo mecanístico plausible entre el G-CSF y los defectos de la liberación plaquetaria.

<!-- review:begin co-lic-20261105-filgrastim-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción se basa solo en el modelo (L5), sin ensayos ni literatura, y no existe un vínculo mecanístico plausible entre el G-CSF y los defectos de la liberación plaquetaria. Además, el único registro sanitario en Colombia está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 2 registros sanitarios (vigentes: 2); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-filgrastim-2 -->

**Para avanzar se necesita:**
- Datos del mecanismo de acción del fármaco y una evaluación mecanística de su relación con la función plaquetaria
- Estudios preclínicos o de mecanismo que justifiquen la hipótesis
- Revisión de literatura dirigida a G-CSF en trastornos plaquetarios
- Obtener el prospecto con advertencias y contraindicaciones para el análisis de seguridad

<!-- review:begin co-lic-20261031-filgrastim-1 -->

> **Corrección de revisión (2026-10-31)**: Texto original: "Obtener el prospecto con advertencias y contraindicaciones para el análisis de seguridad / Aclarar la situación regulatoria en Colombia (registro cancelado) y la disponibilidad de productos con registro vigente" Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-10-31. El medicamento tiene 2 registros sanitarios (vigentes: 2); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261031-filgrastim-1 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-10-31 | Eliminado: "Aclarar la situación regulatoria en Colombia (registro cancelado) y la disponibilidad de productos con registro vigente" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Además, el único registro sanitario en Colombia está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Releuko (filgrastim) prescribing information, Amneal Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=74e1ec6e-1630-4654-895c-2bd355f939e7) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

