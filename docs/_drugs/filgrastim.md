---
layout: default
title: Filgrastim
parent: Solo Predicción del Modelo (L5)
nav_order: 285
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
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

## Filgrastim: De Indicación No Especificada a Trastorno Hemorrágico Primario de Liberación Plaquetaria
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
| Puntaje de Predicción TxGNN | 99.998% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, filgrastim es un análogo del G-CSF que se une al receptor de G-CSF y estimula la producción, maduración y función de los neutrófilos.

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
| 20002046 (cancelado) | FILGRASTIM 300 MCG/ML SOLUCIÓN INYECTABLE (MEGALABS COLOMBIA S.A.S) | Solución inyectable | FILGRASTIM |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas:** se identificaron 100 interacciones potenciales, y las principales listadas son de nivel moderado: yobenguano (I-131), fludesoxiglucosa (18F), ibritumomab tiuxetán, tositumomab (con y sin I-131), levamisol, trimetrexato, mercaptopurina, abemaciclib, paclitaxel, acalabrutinib, aldesleukina, alemtuzumab, altretamina, trióxido de arsénico, asparaginasa de *E. coli*, avapritinib, azacitidina, belantamab mafodotina y bendamustina.

Para advertencias y contraindicaciones, consultar el prospecto del producto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5), sin ensayos ni literatura, y no existe un vínculo mecanístico plausible entre el G-CSF y los defectos de la liberación plaquetaria. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Datos del mecanismo de acción del fármaco y una evaluación mecanística de su relación con la función plaquetaria
- Estudios preclínicos o de mecanismo que justifiquen la hipótesis
- Revisión de literatura dirigida a G-CSF en trastornos plaquetarios
- Obtener el prospecto con advertencias y contraindicaciones para el análisis de seguridad
- Aclarar la situación regulatoria en Colombia (registro cancelado) y la disponibilidad de productos con registro vigente
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

