---
layout: default
title: Desmopressin
parent: Solo Predicción del Modelo (L5)
nav_order: 204
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Desmopressin: nueva indicación predicha, Deficiencia congénita de protrombina (nivel de evidencia L5). Indicación original: Desmopresina"
monitor_inn: "desmopressin"
predicted_indications: ["congenital prothrombin deficiency", "inherited thrombophilia", "Glanzmann thrombasthenia", "primary release disorder of platelets", "Scott syndrome", "flood factor deficiency"]
---

# Desmopressin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Desmopresina: De Desmopresina (registro sin indicación detallada) a Deficiencia Congénita de Protrombina

## Resumen en Una Frase

La desmopresina es un análogo sintético de la vasopresina. En Colombia sus registros sanitarios solo indican el nombre del principio activo, sin detallar la indicación aprobada.
El modelo TxGNN predice que podría ser efectiva para **deficiencia congénita de protrombina**, pero esta predicción cuenta con **0 ensayos clínicos** y solo **1 publicación** (una revisión general de 1993) que no demuestra un efecto de la desmopresina sobre esta enfermedad.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Desmopresina (el registro no detalla la indicación) |
| Nueva Indicación Predicha | Deficiencia congénita de protrombina |
| Puntaje de Predicción TxGNN | 99.70% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según el conocimiento farmacológico general, la desmopresina actúa sobre el receptor V2 y libera el factor VIII y el factor de von Willebrand (VWF) desde los depósitos del endotelio. Por eso se usa como agente hemostático en trastornos hemorrágicos.

La protrombina (factor II) no se libera por esta vía, de modo que **no existe un fundamento mecanístico claro** para usar desmopresina en su deficiencia congénita. El puntaje del modelo es muy alto (0.997), pero probablemente refleja la cercanía en el grafo de conocimiento entre este fármaco y otros trastornos hemorrágicos, y no un efecto terapéutico demostrado.

La única publicación vinculada es una revisión general sobre trastornos hemorrágicos congénitos, que no muestra efecto de la desmopresina en la deficiencia de protrombina. La predicción debe tratarse como una hipótesis sin respaldo.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [7684674](https://pubmed.ncbi.nlm.nih.gov/7684674/) | 1993 | Revisión | Drugs | Revisión general de opciones terapéuticas racionales en trastornos hemorrágicos congénitos (hemofilia A, enfermedad de von Willebrand, entre otros). No demuestra efecto de la desmopresina en la deficiencia de protrombina. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20057862 (cancelado) | HEMOSPEP | Solución inyectable | DESMOPRESINA |
| 20080728 (cancelado) | DICPRESINA® SPRAY NASAL | Solución nasal | DESMOPRESINA |

Ambos registros están cancelados y no hay registros vigentes.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad de TxGNN/PrimeKG, no texto de prospecto): trastorno hipertensivo, hipertensión, rinitis alérgica, rinitis vasomotora, enfermedad arterial coronaria, deterioro de la función renal, faringitis, resfriado común, fibrosis quística, infecciones del tracto respiratorio, enfermedad de von Willebrand, diabetes insípida dipsogénica, polidipsia e intoxicación hídrica.
- **Interacciones farmacológicas**: se identificaron 172 interacciones en total. Entre las listadas:
  - **Mayores**: hidrocortisona, triamcinolona, dexametasona, beclometasona dipropionato, betametasona, budesonida, prednisolona y prednisona.
  - **Moderadas**: epinefrina, loperamida, morfina (incluida la liposomal), opio y clorpropamida.
  - **Menores**: ácido acetilsalicílico.
  - **Nivel desconocido**: lactulosa, simvastatina, pantoprazol, metformina y omeprazol.
- Para advertencias y contraindicaciones de etiqueta, consultar el prospecto.
- La hiponatremia es un riesgo conocido de la desmopresina. Además, su efecto de aumento de VWF/FVIII podría incrementar el riesgo trombótico.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción solo cuenta con el puntaje del modelo, sin ensayos clínicos ni estudios que muestren un efecto de la desmopresina en la deficiencia de protrombina, y sin un mecanismo plausible. Además, los dos registros sanitarios en Colombia están cancelados.

**Para avanzar se necesita:**
- Evidencia mecanística o clínica específica que vincule la desmopresina con la deficiencia de protrombina. Sin ella, no se recomienda continuar con esta indicación.
- Datos de mecanismo de acción y de seguridad del prospecto (advertencias y contraindicaciones).
- Aclarar la situación regulatoria, ya que no hay registros vigentes en Colombia.
- Considerar otras indicaciones predichas con mejor respaldo. La más prometedora es el **trastorno primario de liberación plaquetaria** (nivel L3, "Proceed with Guardrails"): tiene un mecanismo plausible y revisiones y estudios pediátricos que respaldan el uso de la desmopresina. Requeriría una infusión de prueba para confirmar la respuesta, monitoreo de sodio por riesgo de hiponatremia y restricción de líquidos.
- Otras indicaciones predichas, como trombofilia hereditaria, enfermedad de von Willebrand pseudo-tipo plaquetario y síndrome de Scott, son mecanísticamente débiles o potencialmente perjudiciales.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

