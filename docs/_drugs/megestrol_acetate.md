---
layout: default
title: Megestrol Acetate
parent: Evidencia Alta (L1-L2)
nav_order: 424
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-14
description: "Megestrol Acetate: nueva indicación predicha, Carcinoma endometrial del cuerpo uterino (nivel de evidencia L2). Indicación original: MEGESTROL"
monitor_inn: "Megestrol acetate"
predicted_indications: ["hereditary breast ovarian cancer syndrome", "borderline epithelial tumor of ovary", "uterine carcinosarcoma", "placenta cancer", "ovarian clear cell adenocarcinoma", "ovarian cancer", "malignant dysgerminomatous germ cell tumor of ovary"]
---

# Megestrol Acetate
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **10** 
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

# Acetato de Megestrol: De Indicación Original (MEGESTROL) a Carcinoma Endometrial del Cuerpo Uterino

## Resumen en Una Frase

El acetato de megestrol es una progestina sintética cuyo registro sanitario en Colombia (ya cancelado) lo identifica solo con el texto "MEGESTROL", sin una indicación más detallada.
El modelo TxGNN predice que podría ser efectivo para el **carcinoma endometrial del cuerpo uterino**, con **1 ensayo clínico** (Fase 2, completado) y **ninguna publicación** asociada directamente a esta indicación.
Cabe aclarar que se trata de un uso hormonal ya reconocido en la práctica clínica, más que de un reposicionamiento verdaderamente novedoso.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | MEGESTROL (el registro no detalla la indicación aprobada) |
| Nueva Indicación Predicha | Carcinoma endometrial del cuerpo uterino |
| Puntaje de Predicción TxGNN | 99.94% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | Solo cancelado (sin registros vigentes) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada para este informe. Según el conocimiento farmacológico general, el acetato de megestrol es una progestina sintética que actúa sobre los receptores de progesterona.

El endometrio es un tejido sensible a hormonas: los estrógenos estimulan el crecimiento de las células endometriales, mientras que las progestinas ejercen efectos antiproliferativos y de diferenciación. Por eso, la terapia con progestinas es una opción hormonal establecida en el carcinoma endometrial, sobre todo en enfermedad bien diferenciada y con receptores hormonales positivos.

Conviene señalar que el único ensayo disponible evalúa megestrol como parte de un régimen combinado (con tamoxifeno), frente a temsirolimus. Además, no hay publicaciones asociadas a esta indicación en los datos compilados, por lo que la evidencia se limita a un único estudio.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00729586](https://clinicaltrials.gov/study/NCT00729586) | Fase 2 | Completado | 73 | Ensayo aleatorizado que compara temsirolimus solo frente a temsirolimus combinado con terapia hormonal (acetato de megestrol y citrato de tamoxifeno) en mujeres con cáncer endometrial avanzado, persistente o recurrente. El megestrol no es el único agente en investigación. |

---

## Informacion de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20004640 (cancelado) | MEGETRAL | Tableta | MEGESTROL |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia hormonal (progestina), no citotóxico convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto. Dados los antecedentes de la base de conocimiento, considerar glucemia, presión arterial, función hepática y renal, y función suprarrenal |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Contraindicaciones o precauciones según el grafo de conocimiento** (relaciones fármaco-enfermedad, no texto de prospecto): trastornos hipertensivos e hipertensión, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, hiperglucemia, diabetes mellitus, cetoacidosis diabética, insuficiencia suprarrenal y enfermedad de Addison, hipogonadismo masculino, eunucoidismo, menopausia prematura, síndrome de insensibilidad a los andrógenos y piouréter.
- **Interacciones farmacológicas**: se identificaron 100 interacciones. Las 20 mostradas son de nivel moderado y corresponden en su mayoría a antidiabéticos: acarbosa, albiglutida, alogliptina, metformina, pioglitazona, canagliflozina, clorpropamida, dapagliflozina, dulaglutida, empagliflozina, linagliptina, glimepirida, repaglinida, semaglutida, saxagliptina, sitagliptina e insulinas (aspart, degludec). También figuran aprepitant y claritromicina. El patrón sugiere vigilar el control glucémico cuando se combine con antidiabéticos.

No se dispone de texto de prospecto con advertencias y contraindicaciones; consultar el prospecto para información de seguridad adicional.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un ensayo aleatorizado de Fase 2 completado en cáncer endometrial con un régimen que incluye megestrol, y el mecanismo progestínico es coherente con la indicación. Sin embargo, la evidencia se limita a un solo estudio con megestrol como parte de una combinación, y el producto no tiene registros vigentes en Colombia.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones) para completar la evaluación de seguridad.
- Confirmar los resultados publicados del ensayo NCT00729586 y buscar literatura específica sobre megestrol en cáncer endometrial.
- Completar los datos del mecanismo de acción (por ejemplo, consultando DrugBank).
- Definir la situación regulatoria: no hay registro vigente en Colombia, por lo que habría que evaluar un nuevo registro o la reactivación del existente.
- Establecer un plan de monitoreo para pacientes con diabetes, hipertensión o enfermedad hepática o renal, y para quienes usen antidiabéticos.

**Otras indicaciones predichas (referencia breve):**
- **Cáncer de ovario** (L1, ensayo Fase 3 NCT00005975, n=288): ese ensayo evaluó megestrol para los sofocos tras tratamiento de cáncer de mama, no la actividad antitumoral en cáncer de ovario. Existen estudios de Fase 2 con dosis altas en enfermedad refractaria a platino, pero el beneficio antitumoral es modesto y no es estándar de tratamiento. Requiere verificación antes de cualquier recomendación.
- **Carcinosarcoma uterino** (L4): solo evidencia indirecta (expresión de receptores y un reporte de caso).
- **Resto de predicciones** (por ejemplo, carcinoma de células transicionales endometrial, síndrome hereditario de cáncer de mama y ovario, tumor epitelial limítrofe de ovario, cáncer de placenta, adenocarcinoma de células claras de ovario, disgerminoma y tumor neuroendocrino de bajo grado del cuerpo uterino): L5 y recomendación Hold, sin ensayos ni literatura que las respalden.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

