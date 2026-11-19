---
layout: default
title: Pitavastatin
parent: Solo Predicción del Modelo (L5)
nav_order: 519
evidence_level: L5
indication_count: 4
monitor_inn: "pitavastatin"
predicted_indications: ["cholesterol-ester transfer protein deficiency", "HIV infectious disease", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "feline acquired immunodeficiency syndrome"]
last_modified_at: 2026-11-20
description: "Pitavastatin: nueva indicación predicha, Deficiencia de la proteína de transferencia de ésteres de colesterol (nivel de evidencia L5). Indicación original: Pitavastatina"
---

# Pitavastatin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

## Pitavastatina: De Pitavastatina (indicación sin detallar en el registro) a Deficiencia de la proteína de transferencia de ésteres de colesterol
{: .text-alpha }

## Resumen en Una Frase

Pitavastatina es una estatina comercializada en Colombia, y el registro sanitario solo indica el nombre del principio activo, sin detallar la indicación. El modelo TxGNN predice que podría ser efectiva para la **deficiencia de la proteína de transferencia de ésteres de colesterol (CETP)**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Pitavastatina (el registro no detalla el texto de la indicación) |
| Nueva Indicación Predicha | Deficiencia de la proteína de transferencia de ésteres de colesterol |
| Puntaje de Predicción TxGNN | 0.9998 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 3 de 3) |
| Número de Registros Sanitarios | 3 (vigentes: 3) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Pitavastatin (traducción no oficial): «La pitavastatina es un inhibidor de la 3-hidroxi-3-metilglutaril-coenzima A (HMG-CoA) reductasa, la enzima que cataliza la conversión de HMG-CoA en mevalonato, un paso limitante de la velocidad en la vía biosintética del colesterol. En consecuencia, se acelera la expresión de los receptores de LDL, seguida de la captación de LDL desde la sangre hacia el hígado, y a continuación disminuye el CT plasmático.» Texto original en inglés: "Pitavastatin is an inhibitor of 3-hydroxy-3-methylglutaryl-coenzyme A (HMG-CoA) reductase, the enzyme that catalyzes the conversion of HMG-CoA to mevalonate, a rate-limiting step in the biosynthetic pathway for cholesterol. As a result, the expression of LDL-receptors followed by the uptake of LDL from blood to liver is accelerated and then the plasma TC decreases." ([DailyMed: Livalo (pitavastatin calcium) prescribing information, Kowa Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=44dcbf97-99ec-427c-ba50-207e0069d6d2), versión del 2026-03-31; consultado el 2026-11-19). Pitavastatina pertenece a la clase de las estatinas, que reducen el colesterol LDL al inhibir la enzima HMG-CoA reductasa. Su uso en el control de lípidos está bien establecido, y mecanísticamente podría tener relación con trastornos del metabolismo de lipoproteínas como la deficiencia de CETP.

La deficiencia de CETP es una condición genética que se caracteriza por niveles muy altos de colesterol HDL y un metabolismo alterado de las lipoproteínas. Existe un vínculo plausible a través de la vía de los lípidos. Sin embargo, esta condición normalmente no requiere tratamiento, y no está claro que una estatina aporte un beneficio clínico.

El puntaje de 0.9998 es solo una predicción computacional. No hay estudios que la confirmen, por lo que debe interpretarse con cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

La lista es parcial: se muestran 3 registros vigentes y puede haber más. Todos son productos de un solo principio activo.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20250238 | ALTACOR® 2 MG tableta recubierta | Tableta recubierta | Pitavastatina |
| 20250244 | ALTACOR® 4 MG tabletas recubiertas | Tableta recubierta | Pitavastatina |
| 20250209 | ALTACOR® 1 MG tabletas recubiertas | Tableta recubierta | Pitavastatina |

## Consideraciones de Seguridad

- **Relaciones de contraindicación en el grafo de conocimiento** (no provienen del texto del prospecto): enfermedad hepática, enfermedad de la vesícula biliar, hipotiroidismo, mixedema, hipotiroidismo congénito, miopatía, enfermedades musculares, enfermedad del músculo esquelético, parálisis periódica familiar, trastornos hipotensivos, rabdomiólisis, fascitis nodular, función renal alterada y lesiones.
- **Interacciones farmacológicas**: se registraron 86 interacciones. Entre las 20 que se listan en los datos compilados:
  - **Mayor**: eritromicina.
  - **Moderada**: rosuvastatina, simvastatina, cobicistat, eltrombopag, metronidazol, tinidazol, secnidazol, benznidazol, etanol, disulfiram, cloroquina, hidroxicloroquina, cloranfenicol, dapsona, zafirlukast, eluxadolina y naltrexona.
  - **Menor**: warfarina y dicumarol.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para la deficiencia de CETP se basa solo en el modelo, sin ensayos ni publicaciones (nivel L5). Además, esta condición normalmente no requiere tratamiento y no hay evidencia de que una estatina aporte beneficio clínico.

**Para avanzar se necesita:**
- Una revisión de la literatura que evalúe si existe un beneficio clínico real de las estatinas en la deficiencia de CETP.
- Datos del mecanismo de acción y del prospecto aprobado por INVIMA (advertencias y contraindicaciones).
- Una justificación clínica de que esta condición requiere tratamiento.

**Nota sobre otras predicciones:** la segunda indicación predicha, "enfermedad por VIH", tiene más respaldo (nivel L1, con la recomendación Proceed with Guardrails). Incluye el ensayo REPRIEVE (NEJM 2023, PMID 37486775), que mostró que pitavastatina reduce los eventos cardiovasculares mayores en personas con VIH. Se trata de prevención cardiovascular en personas con VIH, no de tratamiento de la infección viral. Si se quiere priorizar un reposicionamiento con evidencia, conviene evaluar esa línea por separado, con medidas de resguardo: población objetivo definida, vigilancia de diabetes y miopatía, y revisión de interacciones con los antirretrovirales.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Livalo (pitavastatin calcium) prescribing information, Kowa Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=44dcbf97-99ec-427c-ba50-207e0069d6d2) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

