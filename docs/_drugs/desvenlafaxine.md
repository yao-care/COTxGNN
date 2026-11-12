---
layout: default
title: Desvenlafaxine
parent: Evidencia Moderada (L3-L4)
nav_order: 207
evidence_level: L4
indication_count: 8
last_modified_at: 2026-11-12
description: "Desvenlafaxine: nueva indicación predicha, Trastorno obsesivo-compulsivo (nivel de evidencia L4). Indicación original: No especificada en el registro sanitario (el texto solo indica \"Desve…"
monitor_inn: "desvenlafaxine"
predicted_indications: ["obsessive-compulsive disorder", "schizotypal personality disorder", "schizoid personality disorder", "paranoid personality disorder", "histrionic personality disorder (disease)", "Ohdo syndrome and variants", "benign paroxysmal torticollis of infancy", "agoraphobia"]
---

# Desvenlafaxine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **8** 
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

## Desvenlafaxina: De Antidepresivo ISRN (indicación registrada sin detalle) a Trastorno Obsesivo-Compulsivo
{: .text-alpha }

## Resumen en Una Frase

Desvenlafaxina es un inhibidor de la recaptación de serotonina y noradrenalina (ISRN), cuyo registro sanitario en Colombia no detalla la indicación aprobada (solo repite el nombre del fármaco).
El modelo TxGNN predice que podría ser efectivo para el **trastorno obsesivo-compulsivo (TOC)**,
pero actualmente hay **0 ensayos clínicos** y solo **3 publicaciones** indirectas, de modo que la evidencia es muy limitada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro sanitario (el texto solo indica "Desvenlafaxina"); el uso conocido del fármaco es el trastorno depresivo mayor |
| Nueva Indicación Predicha | Trastorno obsesivo-compulsivo |
| Puntaje de Predicción TxGNN | 0.9991 |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 7 de 9) |
| Número de Registros Sanitarios | 9 (vigentes: 7) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Desvenlafaxina es un ISRN: bloquea la recaptación de serotonina y noradrenalina. Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción, pero esta clase farmacológica es bien conocida.

La modulación serotoninérgica es la base del tratamiento farmacológico del TOC (ISRS y clomipramina). Por eso existe un mecanismo plausible. Sin embargo, los ISRN tienen evidencia más débil e inconsistente en TOC que los ISRS, y no se dispone de datos específicos de desvenlafaxina en esta indicación.

La predicción debe interpretarse como una hipótesis de investigación, no como una recomendación clínica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta indicación.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [24766145](https://pubmed.ncbi.nlm.nih.gov/24766145/) | 2014 | Revisión | Expert Opin Pharmacother | Revisión de estudios doble ciego con antidepresivos de marcado efecto serotoninérgico en TOC; respalda el papel del sistema serotoninérgico, sin datos de desvenlafaxina |
| [36686097](https://pubmed.ncbi.nlm.nih.gov/36686097/) | 2022 | Revisión | Cureus | Revisión sobre depresión posparto; menciona el TOC solo como complicación posterior, relevancia indirecta |
| [40224942](https://pubmed.ncbi.nlm.nih.gov/40224942/) | 2025 | Estudio clínico (no en TOC) | Psychiatry Clin Psychopharmacol | Aumentación con risperidona en trastorno de síntomas somáticos resistente a antidepresivos; no es un estudio en TOC |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20071330 | DESVENLAFAXINA 50 MG (Laboratorios MK S.A.S.) | Tableta de liberación prolongada | DESVENLAFAXINA (sin indicación detallada) |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad del modelo, no texto del prospecto): hipertensión, epilepsia, trastorno bipolar, trastorno afectivo mayor, enfermedad hepática, enfermedad de la vesícula biliar, trastornos de coagulación, hipertrigliceridemia, función renal alterada, hipertensión ocular, glaucoma de ángulo cerrado, enfermedad cardiovascular, síndrome neuroléptico maligno, síndrome de secreción inadecuada de ADH, enfermedad cerebrovascular, enfermedad pulmonar intersticial y síndrome serotoninérgico.
- **Interacciones farmacológicas**: se identificaron 184 interacciones. Entre las de nivel **mayor** figuran bupropión, lorcaserina, dexfenfluramina, dietilpropión, dolasetrón, fenfluramina, granisetrón y mazindol (varias con riesgo de toxicidad serotoninérgica o prolongación del QT). Entre las de nivel moderado destacan epinefrina, morfina, ácido acetilsalicílico, efedrina y dronabinol.

Consultar el prospecto para las advertencias y contraindicaciones oficiales, que no están disponibles en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto, pero no hay ensayos clínicos ni estudios específicos de desvenlafaxina en TOC, y la evidencia de los ISRN en esta indicación es más débil que la de los ISRS.

<!-- review:begin co-lic-20261105-desvenlafaxine-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción tiene un puntaje alto, pero no hay ensayos clínicos ni estudios específicos de desvenlafaxina en TOC, y la evidencia de los ISRN en esta indicación es más débil que la de los ISRS. Además, el único registro sanitario en Colombia está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 9 registros sanitarios (vigentes: 7); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-desvenlafaxine-2 -->

**Para avanzar se necesita:**
- Obtener y analizar el prospecto oficial (advertencias y contraindicaciones) del registro sanitario
- Confirmar el mecanismo de acción desde DrugBank
- Estudios preclínicos o clínicos pequeños de desvenlafaxina en TOC, con comparación frente a ISRS
- Revisar el perfil de seguridad, en especial la hipertensión, las interacciones serotoninérgicas y los antecedentes de trastorno bipolar

<!-- review:begin co-lic-20261031-desvenlafaxine-1 -->

> **Corrección de revisión (2026-10-31)**: Texto original: "Evaluar la situación regulatoria (registro cancelado) y la disponibilidad real del producto en Colombia / Revisar el perfil de seguridad, en especial la hipertensión, las interacciones serotoninérgicas y los antecedentes de trastorno bipolar" Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-10-31. El medicamento tiene 9 registros sanitarios (vigentes: 7); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261031-desvenlafaxine-1 -->

---

### Nota sobre otras indicaciones predichas

Entre las demás predicciones, la **distimia** (L3; dos ensayos pequeños completados, uno controlado con placebo con 59 participantes y otro abierto con 30) y la **melancolía** (L3; en esencia dentro de la indicación de depresión mayor) tienen más respaldo que el TOC. Las predicciones restantes (trastornos de personalidad esquizotípico, esquizoide, paranoide e histriónico, síndrome de Ohdo, tortícolis paroxística benigna de la infancia y agorafobia) son L5 y se basan solo en el modelo, sin ensayos ni literatura.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-10-31 | Eliminado: "Evaluar la situación regulatoria (registro cancelado) y la disponibilidad real del producto en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Además, el único registro sanitario en Colombia está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

