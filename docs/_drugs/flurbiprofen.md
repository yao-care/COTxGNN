---
layout: default
title: Flurbiprofen
parent: Solo Predicción del Modelo (L5)
nav_order: 299
evidence_level: L5
indication_count: 8
monitor_inn: "flurbiprofen"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "hypermobility of coccyx"]
last_modified_at: 2026-11-24
description: "Flurbiprofen: nueva indicación predicha, Displasia acromesomélica tipo Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type) (nivel de evidencia L5). Indicación original: FLURBIPROFENO"
---

# Flurbiprofen
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

## Flurbiprofeno: antiinflamatorio no esteroideo (inhibidor de la COX) → displasia acromesomélica tipo Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type)
{: .text-alpha }

## Resumen en Una Frase

Flurbiprofeno es un antiinflamatorio no esteroideo que se comercializa en Colombia en presentaciones bucofaríngeas (tabletas bucales y solución en spray).
El modelo TxGNN predice que podría ser efectivo para la **displasia acromesomélica tipo Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type)**,
pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | FLURBIPROFENO |
| Nueva Indicación Predicha | Displasia acromesomélica tipo Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type) |
| Puntaje de Predicción TxGNN | 0,9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 4 de 4) |
| Número de Registros Sanitarios | 4 (vigentes: 4) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Flurbiprofen (traducción no oficial): «El flurbiprofeno tiene propiedades analgésicas, antiinflamatorias y antipiréticas. El mecanismo de acción del flurbiprofeno, al igual que el de otros AINE, no se conoce por completo, pero implica la inhibición de la ciclooxigenasa (COX-1 y COX-2).» Texto original en inglés: "Flurbiprofen has analgesic, anti-inflammatory, and antipyretic properties. The mechanism of action of flurbiprofen, like that of other NSAIDs, is not completely understood but involves inhibition of cyclooxygenase (COX-1 and COX-2)." ([DailyMed: Lurbiro (flurbiprofen) prescribing information, IPG Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7ebf7427-eaae-4035-a6b2-0ea6381e8763), versión del 2026-10-05; consultado el 2026-11-19). Según la información conocida, el flurbiprofeno es un inhibidor no selectivo de la COX-1 y la COX-2, que reduce la síntesis de prostaglandinas y, con ello, la inflamación y el dolor.

La displasia acromesomélica tipo Hunter-Thompson es una displasia esquelética genética, asociada a mutaciones en el gen *CDMP1/GDF5*. Su origen no guarda una relación farmacológica conocida con la inhibición de la COX. El puntaje alto del modelo (0,9999) probablemente refleja cercanía en las relaciones de datos del modelo y no una base farmacológica.

En consecuencia, no hay un argumento mecanístico plausible que sustente esta predicción. Un AINE podría, como mucho, aliviar síntomas dolorosos, pero no modificaría la enfermedad de fondo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 20071641 | STREPSILS INTENSIVE® MIEL & LIMON | TABLETA BUCAL | FLURBIPROFENO | Vigente |
| 20091945 | STREPSILS INTENSIVE NARANJA LIBRE DE AZUCAR | TABLETA BUCAL | FLURBIPROFENO | Vigente |
| 20199308 | STREPSILS INTENSIVE SOLUCION EN SPRAY SABOR A MIEL Y LIMON | SOLUCION BUCOFARINGUEA | FLURBIPROFENO | Vigente |
| 20268366 | MYNTZ® | TABLETA BUCAL | FLURBIPROFENO | Vigente |

Se muestran los 4 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

La lista de registros puede ser parcial.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 352 interacciones registradas. Entre ellas, de nivel moderado: ácido acetilsalicílico, metformina, glimepirida, clorpropamida, mesalazina, balsalazida, aprepitant y los corticoesteroides (hidrocortisona, dexametasona, betametasona, triamcinolona y budesonida), además de sales de potasio (citrato y bicarbonato) y algunos preparados de limpieza intestinal (picosulfato, polietilenglicol con electrolitos, sulfato de sodio). De nivel leve: famotidina, cimetidina y linaclotida.

Para el resto de la información de seguridad (advertencias y contraindicaciones), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no cuenta con ensayos clínicos ni literatura, carece de un vínculo mecanístico plausible con la inhibición de la COX y corresponde a una enfermedad genética del esqueleto cuyo origen no se aborda con un AINE.

**Para avanzar se necesita:**
- Datos de mecanismo de acción que justifiquen una relación biológica entre la inhibición de la COX y la vía de *GDF5*
- Estudios preclínicos que evalúen el efecto del flurbiprofeno en modelos de esta displasia
- Revisión del prospecto aprobado para completar la información de advertencias y contraindicaciones

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Lurbiro (flurbiprofen) prescribing information, IPG Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7ebf7427-eaae-4035-a6b2-0ea6381e8763) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

