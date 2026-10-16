---
layout: default
title: Methylphenidate
parent: Solo Predicción del Modelo (L5)
nav_order: 436
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Methylphenidate: nueva indicación predicha, Trastorno del desarrollo específico (nivel de evidencia L5). Indicación original: METILFENIDATO"
monitor_inn: "methylphenidate"
predicted_indications: ["faciodigitogenital syndrome", "chondromyxoid fibroma", "specific developmental disorder", "dysthymic disorder"]
---

# Methylphenidate
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Metilfenidato: De Metilfenidato (indicación registrada sin especificar) a Trastorno del Desarrollo Específico

## Resumen en Una Frase

Metilfenidato es un estimulante del sistema nervioso central registrado en Colombia bajo el nombre de Ritalina y otros productos, cuyo texto de indicación en el registro sanitario solo indica "METILFENIDATO".
El modelo TxGNN predice que podría ser efectivo para **trastorno del desarrollo específico**, con **0 ensayos clínicos** y **18 publicaciones** recuperadas, en su mayoría revisiones y estudios sobre TDAH (una indicación ya establecida del fármaco, no una indicación nueva).
La evidencia es débil: se trata más de una cuestión de clasificación de la enfermedad que de una señal real de reposicionamiento.

> **Nota sobre la selección de la indicación:** Las dos primeras predicciones por puntaje (síndrome faciodigitogenital y fibroma condromixoide) no tienen ensayos ni literatura y carecen de vínculo mecanístico plausible. Este informe se centra en la primera predicción con literatura disponible (trastorno del desarrollo específico) y menciona las demás en la conclusión.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | METILFENIDATO (el registro no detalla la indicación clínica) |
| Nueva Indicación Predicha | Trastorno del desarrollo específico (rank 3; la rank 1 es síndrome faciodigitogenital) |
| Puntaje de Prediccion TxGNN | 99.99% (0.99988) para trastorno del desarrollo específico; 99.998% para la predicción rank 1 |
| Nivel de Evidencia | L4 (L5 para las predicciones rank 1 y 2) |
| Estado de Mercado en Colombia | Solo cancelados (sin registros vigentes) |
| Numero de Registros Sanitarios | 4 (0 vigentes, 4 cancelados) |
| Decision Recomendada | Hold |

---

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, el metilfenidato bloquea los transportadores de dopamina y noradrenalina, y es un tratamiento de primera línea para el trastorno por déficit de atención e hiperactividad (TDAH). La literatura recuperada respalda este mecanismo, por ejemplo un estudio PET en adultos con TDAH que midió el efecto del metilfenidato de liberación prolongada sobre ambos transportadores (PMID 41128391).

La relación entre la indicación original y la nueva es indirecta. El TDAH es un trastorno del neurodesarrollo, y la etiqueta "trastorno del desarrollo específico" es amplia. Casi todos los artículos recuperados tratan sobre TDAH, que ya es una indicación establecida del metilfenidato. La evidencia sobre trastornos específicos del aprendizaje es solo indirecta (por ejemplo, un estudio de EEG cuantitativo en TDAH con dificultades de aprendizaje, PMID 33012168).

Por ello, esta predicción parece reflejar un problema de etiquetado o mapeo en el grafo de conocimiento más que un hallazgo genuino de reposicionamiento. Para las otras dos predicciones de mayor puntaje, no hay vínculo mecanístico respaldado: en el síndrome faciodigitogenital (Aarskog-Scott) el fármaco solo podría, en teoría, aliviar síntomas conductuales tipo TDAH, y en el fibroma condromixoide no existe relevancia conocida.

---

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Se recuperaron 18 publicaciones para esta predicción. Se listan las más relevantes, priorizando estudios clínicos y de cohorte sobre revisiones.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [41128391](https://pubmed.ncbi.nlm.nih.gov/41128391/) | 2026 | Estudio de imagen clínica | Psychiatry Clin Neurosci | PET con doble trazador: efecto del metilfenidato de liberación prolongada sobre los transportadores de dopamina y noradrenalina en adultos con TDAH |
| [40527386](https://pubmed.ncbi.nlm.nih.gov/40527386/) | 2025 | Cohorte | Prog Neuropsychopharmacol Biol Psychiatry | Estudio longitudinal de RM: efectos de la exposición acumulada a metilfenidato sobre la estructura cerebral y los síntomas en jóvenes con TDAH |
| [41655471](https://pubmed.ncbi.nlm.nih.gov/41655471/) | 2026 | Cohorte (genética) | Psychiatry Res | Metaanálisis sobre predicción poligénica de la respuesta al tratamiento del TDAH |
| [33012168](https://pubmed.ncbi.nlm.nih.gov/33012168/) | 2021 | Observacional | Clin EEG Neurosci | EEG cuantitativo en TDAH infantil y dificultades de aprendizaje |
| [22449217](https://pubmed.ncbi.nlm.nih.gov/22449217/) | 2012 | Revisión | Expert Rev Neurother | Psicoestimulantes para síntomas tipo TDAH en trastornos del espectro autista |
| [22923783](https://pubmed.ncbi.nlm.nih.gov/22923783/) | 2015 | Revisión | J Atten Disord | Acciones del metilfenidato en cerebro adulto frente a juvenil: eficacia, seguridad y dosis |
| [19627998](https://pubmed.ncbi.nlm.nih.gov/19627998/) | 2009 | Revisión | Neuropharmacology | Neurobiología del TDAH |
| [41057091](https://pubmed.ncbi.nlm.nih.gov/41057091/) | 2025 | Preclínico | Prog Neuropsychopharmacol Biol Psychiatry | Guanfacina oral mejora síntomas tipo TDAH por exposición a manganeso en modelo animal |

Los demás artículos recuperados son revisiones generales, estudios cualitativos o de interacciones con sustancias psicoactivas, sin relación directa con la nueva indicación. No se dispone de ECA para esta indicación.

---

## Informacion de Mercado en Colombia

Todos los registros sanitarios están cancelados; actualmente no hay productos vigentes.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 227970 | RITALINA 10 MG COMPRIMIDOS | Tableta | METILFENIDATO (cancelado) |
| 20242636 | ATEXAM® XR 54 | Tableta de liberación prolongada | METILFENIDATO (cancelado) |
| 20242665 | ATEXAM® XR 27 | Tableta de liberación prolongada | METILFENIDATO (cancelado) |
| 20242646 | ATEXAM® XR 18 | Tableta de liberación prolongada | METILFENIDATO (cancelado) |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** el grafo de conocimiento asocia el metilfenidato con contraindicación en:
  - **Cardiovasculares y cerebrovasculares:** hipertensión, enfermedad coronaria, infarto de miocardio, trombosis coronaria, accidente cerebrovascular, infarto cerebral, paro cardíaco súbito, enfermedades de la conducción cardíaca.
  - **Psiquiátricas:** trastorno bipolar, trastorno afectivo mayor, trastornos psicóticos, esquizoafectivo y esquizofreniforme, trastorno mental, abuso o dependencia de sustancias, anorexia nerviosa.
  - **Neurológicas y hematológicas:** epilepsia, trombocitopenia, leucopenia, anemia, hemoglobinopatía.
  - **Otras:** glaucoma, hipertiroidismo, enfermedad de Graves, tirotoxicosis.
- **Interacciones farmacológicas:** se identificaron 137 interacciones. Entre las principales:
  - **Mayor:** bupropión.
  - **Moderadas:** isometepteno, efedrina, epinefrina, polietilenglicol con electrolitos, ácido picosulfúrico, sulfato de sodio.
  - Otras interacciones tienen gravedad no determinada (por ejemplo, metformina, omeprazol, morfina, simvastatina, prednisona).
- Las advertencias y contraindicaciones del prospecto no están disponibles; consultar el prospecto para esa información.

---

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificación:**
Para trastorno del desarrollo específico no hay ensayos clínicos, y la literatura es indirecta y se centra en TDAH, indicación ya establecida, por lo que no constituye una señal real de reposicionamiento (L4). Las predicciones con mayor puntaje (síndrome faciodigitogenital y fibroma condromixoide) solo tienen respaldo computacional (L5), y la de trastorno distímico (L4) se apoya en evidencia indirecta. Además, no hay registros vigentes en Colombia y existe un perfil amplio de contraindicaciones e interacciones.

**Para avanzar se necesita:**
- Aclarar si "trastorno del desarrollo específico" corresponde a una indicación ya cubierta (TDAH) o a una entidad distinta, para descartar un artefacto de mapeo.
- Obtener el prospecto de INVIMA con advertencias y contraindicaciones (brecha de datos bloqueante para el cribado de seguridad).
- Completar los datos del mecanismo de acción desde DrugBank.
- Revisar la situación regulatoria: confirmar por qué los cuatro registros están cancelados y si hay otros productos con metilfenidato vigentes.
- Buscar estudios controlados en la indicación específica antes de reconsiderar la decisión.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

