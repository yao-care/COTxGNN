---
layout: default
title: Desvenlafaxine
parent: Evidencia Moderada (L3-L4)
nav_order: 207
evidence_level: L4
indication_count: 10
---

# Desvenlafaxine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
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

# Desvenlafaxina: De Antidepresivo ISRN (indicación registrada sin detalle) a Trastorno Obsesivo-Compulsivo

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
| Puntaje de Predicción TxGNN | 99.91% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo cancelado (sin registros vigentes) |
| Número de Registros Sanitarios | 1 (cancelado) |
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
| 20071330 (cancelado) | DESVENLAFAXINA 50 MG (Laboratorios MK S.A.S.) | Tableta de liberación prolongada | DESVENLAFAXINA (sin indicación detallada) |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad del modelo, no texto del prospecto): hipertensión, epilepsia, trastorno bipolar, trastorno afectivo mayor, enfermedad hepática, enfermedad de la vesícula biliar, trastornos de coagulación, hipertrigliceridemia, función renal alterada, hipertensión ocular, glaucoma de ángulo cerrado, enfermedad cardiovascular, síndrome neuroléptico maligno, síndrome de secreción inadecuada de ADH, enfermedad cerebrovascular, enfermedad pulmonar intersticial y síndrome serotoninérgico.
- **Interacciones farmacológicas**: se identificaron 184 interacciones. Entre las de nivel **mayor** figuran bupropión, lorcaserina, dexfenfluramina, dietilpropión, dolasetrón, fenfluramina, granisetrón y mazindol (varias con riesgo de toxicidad serotoninérgica o prolongación del QT). Entre las de nivel moderado destacan epinefrina, morfina, ácido acetilsalicílico, efedrina y dronabinol.

Consultar el prospecto para las advertencias y contraindicaciones oficiales, que no están disponibles en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto, pero no hay ensayos clínicos ni estudios específicos de desvenlafaxina en TOC, y la evidencia de los ISRN en esta indicación es más débil que la de los ISRS. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto oficial (advertencias y contraindicaciones) del registro sanitario
- Confirmar el mecanismo de acción desde DrugBank
- Estudios preclínicos o clínicos pequeños de desvenlafaxina en TOC, con comparación frente a ISRS
- Evaluar la situación regulatoria (registro cancelado) y la disponibilidad real del producto en Colombia
- Revisar el perfil de seguridad, en especial la hipertensión, las interacciones serotoninérgicas y los antecedentes de trastorno bipolar

---

### Nota sobre otras indicaciones predichas

Entre las demás predicciones, la **distimia** (L3; dos ensayos pequeños completados, uno controlado con placebo con 59 participantes y otro abierto con 30) y la **melancolía** (L3; en esencia dentro de la indicación de depresión mayor) tienen más respaldo que el TOC. Las predicciones restantes (trastornos de personalidad esquizotípico, esquizoide, paranoide e histriónico, síndrome de Ohdo, tortícolis paroxística benigna de la infancia y agorafobia) son L5 y se basan solo en el modelo, sin ensayos ni literatura.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

