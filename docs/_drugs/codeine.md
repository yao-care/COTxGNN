---
layout: default
title: Codeine
parent: Solo Predicción del Modelo (L5)
nav_order: 178
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-28
description: "Codeine: nueva indicación predicha, Enfermedad de la cavidad nasal (nivel de evidencia L4). Indicación original: Paracetamol, combinaciones excluyendo psicolépticos"
monitor_inn: "Codeine"
predicted_indications: ["nasal cavity disease", "trigeminal autonomic cephalalgia", "allergic urticaria"]
---

# Codeine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Codeína: De Combinaciones de Paracetamol (excluyendo psicolépticos) a Enfermedad de la Cavidad Nasal
{: .text-alpha }

## Resumen en Una Frase

La codeína se registró en Colombia dentro de un producto clasificado como "combinaciones de paracetamol excluyendo psicolépticos" (ALGIMIDE TABLETAS), y es un opioide usado para el dolor, la tos y la diarrea.
El modelo TxGNN predice que podría ser efectiva para **enfermedad de la cavidad nasal**, pero no hay ensayos clínicos y solo existe **1 publicación** (un reporte de caso que describe un efecto adverso, no un beneficio terapéutico).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Paracetamol, combinaciones excluyendo psicolépticos |
| Nueva Indicación Predicha | Enfermedad de la cavidad nasal |
| Puntaje de Predicción TxGNN | 0.9993 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 1) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, la codeína es un opioide natural que actúa como agonista del receptor opioide mu (OPRM1). Se usa para tratar el dolor sistémico y, de forma adicional, como antidiarreico y antitusivo.

Con los datos disponibles **no se sustenta un mecanismo terapéutico** para la enfermedad de la cavidad nasal. La única publicación es un reporte de caso de rinolitiasis formada alrededor de un cuerpo extraño que resultó ser una mezcla endurecida de codeína y opio (un "opioma"). Esto describe un evento incidental o adverso relacionado con el fármaco, no un beneficio.

El puntaje alto del modelo (0.9993) no está corroborado por ninguna evidencia clínica de eficacia. Proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. No debe interpretarse como potencial terapéutico demostrado.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [17315836](https://pubmed.ncbi.nlm.nih.gov/17315836/) | 2007 | Reporte de caso | Ear, Nose & Throat Journal | Rinolito unilateral en un hombre de 21 años, formado alrededor de un cuerpo extraño que era una mezcla endurecida de codeína y opio envuelta en nailon. Describe una causa inusual de rinolitiasis, no un tratamiento. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 58027 | ALGIMIDE TABLETAS | Tableta | Paracetamol, combinaciones excluyendo psicolépticos | Vigente |

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (relaciones fármaco-enfermedad del modelo, no texto de prospecto):
  - Cardiovasculares y respiratorias: hipertensión, enfermedad pulmonar obstructiva crónica (EPOC).
  - Hepáticas, renales y digestivas: insuficiencia hepática, enfermedad hepática, enfermedad renal, pancreatitis, enfermedad de la vesícula biliar, úlcera péptica, enfermedad inflamatoria intestinal, gastritis.
  - Neurológicas y psiquiátricas: epilepsia, insomnio, trastornos de ansiedad, trastorno neurótico, trastorno distímico, trastornos psicóticos, esquizofreniforme y esquizoafectivo, trastorno mental.
  - Metabólicas y endocrinas: porfiria (incluida la hereditaria) y otros trastornos del metabolismo de porfirinas, hipotiroidismo, mixedema, hipotiroidismo congénito.
  - Hematológicas y dermatológicas: trombocitopenia, dermatitis herpetiforme.
- **Interacciones farmacológicas**: solo se registró la interacción farmacológica con el receptor opioide mu (OPRM1), que corresponde al mecanismo farmacológico principal; no hay interacciones con otros fármacos.
- **Riesgos de la clase opioide**: dependencia y abuso potencial.

Para advertencias y contraindicaciones del prospecto, consultar el prospecto del producto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La única evidencia es un reporte de caso que describe un efecto adverso (un rinolito formado alrededor de una mezcla de codeína y opio), sin ensayos clínicos ni datos de eficacia. El único producto registrado en Colombia está cancelado.

**Para avanzar se necesita:**
- Datos del mecanismo de acción que sustenten un vínculo con la patología de la cavidad nasal.
- Estudios clínicos o preclínicos que muestren un beneficio terapéutico real.
- Obtener el prospecto del INVIMA para completar el análisis de seguridad.
- Evaluar la relación beneficio-riesgo dado el perfil de dependencia de los opioides y las numerosas contraindicaciones.

---

## Otras Predicciones Evaluadas (Referencia)

| Indicación Predicha | Puntaje TxGNN | Nivel de Evidencia | Observación | Decisión |
|------|------|------|------|------|
| Cefalea autonómica trigeminal | 0.9943 | L4 | Dos publicaciones (una experiencia clínica pediátrica y un reporte de caso por mal uso de cocaína) que no muestran eficacia de la codeína. Los opioides conllevan riesgo de cefalea por uso excesivo de medicación y dependencia. | Hold |
| Urticaria alérgica | 0.9937 | L4 | La literatura señala a la codeína como **inductora** de urticaria (liberadora directa de histamina en mastocitos, usada como modelo de prueba cutánea), no como tratamiento. El reposicionamiento está desaconsejado por la evidencia disponible. | Hold |
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

