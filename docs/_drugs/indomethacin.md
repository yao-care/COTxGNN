---
layout: default
title: Indomethacin
parent: Solo Predicción del Modelo (L5)
nav_order: 342
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Indomethacin: nueva indicación predicha, Síndrome de braquidactilia-sindactilia (nivel de evidencia L5). Indicación original: El texto del registro sanitario solo indica \"INDOMETACINA\"…"
monitor_inn: "Indomethacin"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "WHIM syndrome", "brachyolmia-amelogenesis imperfecta syndrome", "brachyolmia", "myosclerosis", "juvenile idiopathic arthritis", "rheumatoid factor-positive polyarticular juvenile idiopathic arthritis", "rheumatoid nodulosis"]
---

# Indomethacin
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

## Indometacina: De Condiciones Inflamatorias (AINE) a Síndrome de Braquidactilia-Sindactilia
{: .text-alpha }

## Resumen en Una Frase

La indometacina es un antiinflamatorio no esteroideo (AINE) usado ampliamente en condiciones inflamatorias como artritis reumatoide, osteoartritis, espondilitis anquilosante, bursitis, tendinitis y artritis gotosa aguda.
El modelo TxGNN predice que podría ser efectiva para el **síndrome de braquidactilia-sindactilia**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción, que por ahora es solo computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | El texto del registro sanitario solo indica "INDOMETACINA", sin una indicación específica. Su uso clínico conocido es el de un AINE para condiciones inflamatorias |
| Nueva Indicación Predicha | Síndrome de braquidactilia-sindactilia |
| Puntaje de Predicción TxGNN | 0.9997 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción. La indometacina es un inhibidor no selectivo de las enzimas ciclooxigenasa (COX-1 y COX-2), por lo que reduce la síntesis de prostaglandinas y, con ella, la inflamación, el dolor y la fiebre. También se le describe interacción con otras dianas, como el receptor DP2 (PTGDR2), el receptor PPAR-gamma y el transportador de folato acoplado a protones (SLC46A1).

**Con los datos disponibles no se puede sustentar una relación mecanística plausible entre este fármaco y la nueva indicación.** El síndrome de braquidactilia-sindactilia es una malformación esquelética del desarrollo de origen genético. Inhibir las prostaglandinas no debería modificar la patología del desarrollo que lo origina. El puntaje alto de TxGNN (0.9997) es una predicción computacional y no tiene respaldo en estudios clínicos ni en literatura.

Por eso la relación entre la indicación original (inflamación y dolor) y la nueva (una malformación congénita) es débil. No hay una similitud de enfermedad ni de vía biológica que justifique avanzar sin evidencia adicional.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20056703 (cancelado) | NB PEXAIL CÁPSULA BLANDA 25 MG | Cápsula blanda | INDOMETACINA |

La indometacina no cuenta actualmente con ningún registro sanitario vigente en Colombia. Su único registro, de un producto de un solo componente, está cancelado.

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento (TxGNN/PrimeKG).** No provienen del prospecto, que no estuvo disponible. Se asocian a la indometacina las siguientes condiciones:
  - **Cardiovasculares:** hipertensión, infarto de miocardio, trombosis coronaria, enfermedad cardiovascular y cardíaca.
  - **Gastrointestinales:** úlcera gástrica, úlcera duodenal, úlcera péptica activa, colitis ulcerosa, enfermedad inflamatoria intestinal, enterocolitis necrosante y disquinesia esofágica.
  - **Renales, hepáticas y biliares:** enfermedad renal, piouréter, enfermedad hepática y enfermedad de la vesícula biliar.
  - **Hematológicas y hemorrágicas:** trombocitopenia, trastornos de la coagulación, hemoglobinopatía y hemorragia intracerebral.
  - **Respiratorias:** asma (intrínseca y alérgica).
  - **Neurológicas y psiquiátricas:** epilepsia, trastorno de ansiedad, trastorno neurótico y trastorno distímico.
  - **Otras:** enfermedades infecciosas.
- **Dianas farmacológicas descritas:** COX-1, COX-2, receptor DP2, PPAR-gamma y transportador de folato acoplado a protones. Corresponden a su perfil farmacológico y no a interacciones medicamentosas clínicas confirmadas.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para el síndrome de braquidactilia-sindactilia no tiene ensayos clínicos ni literatura (nivel L5), y no existe un vínculo mecanístico plausible entre la inhibición de COX y una malformación esquelética genética. Además, el producto no tiene registro vigente en Colombia.

**Para avanzar se necesita:**
- Evidencia preclínica o mecanística que vincule la vía de las prostaglandinas con la fisiopatología de este síndrome.
- Obtener y revisar el prospecto oficial (INVIMA) para definir advertencias y contraindicaciones.
- Complementar los datos del mecanismo de acción desde DrugBank.
- Considerar candidatos mejor respaldados entre las predicciones de este fármaco. La **artritis idiopática juvenil** (puntaje TxGNN 0.9984, nivel L3) cuenta con literatura que incluye un ensayo doble ciego de 1978 que comparó indometacina con ketoprofeno en artritis crónica juvenil, además de varias revisiones pediátricas sobre AINE. Esto sustenta un uso sintomático histórico, no modificador de la enfermedad, y se trata más de un uso ya establecido que de uno nuevo. Podría ser una línea de investigación más razonable.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

