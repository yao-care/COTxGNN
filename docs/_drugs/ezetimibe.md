---
layout: default
title: Ezetimibe
parent: Evidencia Alta (L1-L2)
nav_order: 276
evidence_level: L1
indication_count: 4
last_modified_at: 2026-10-14
description: "Ezetimibe: nueva indicación predicha, Hiperlipoproteinemia (nivel de evidencia L1). Indicación original: Simvastatina, combinaciones, paquetes"
monitor_inn: "EZETIMIBE"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
---

# Ezetimibe
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **4** 
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

# Ezetimiba: De Combinaciones con Simvastatina a Hiperlipoproteinemia

## Resumen en Una Frase

Ezetimiba figura en su registro sanitario colombiano como parte de las combinaciones con simvastatina (producto EZIT-ST 10/10), y su mecanismo conocido es reducir la absorción intestinal de colesterol.
El modelo TxGNN predice que podría ser efectivo para **hiperlipoproteinemia**, con **40 ensayos clínicos** y **20 publicaciones** recuperados para esta indicación. Cabe aclarar que se trata de un uso ya establecido y no de un reposicionamiento novedoso.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Simvastatina, combinaciones, paquetes |
| Nueva Indicación Predicha | Hiperlipoproteinemia |
| Puntaje de Predicción TxGNN | 99.63% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la ezetimiba inhibe la proteína NPC1L1 y con ello la absorción intestinal de colesterol, lo que reduce el colesterol LDL. Su indicación registrada en Colombia es como parte de combinaciones con simvastatina.

La relación con la nueva indicación es muy estrecha. La simvastatina reduce la síntesis hepática de colesterol, mientras que la ezetimiba reduce su absorción intestinal. Ambos mecanismos se complementan, y la hiperlipoproteinemia es precisamente la condición que estos tratamientos buscan controlar.

Por ello, la predicción es mecanísticamente coherente, pero debe interpretarse como confirmación de un uso establecido y no como un hallazgo de reposicionamiento. Las otras predicciones del modelo tienen respaldo mucho más débil: la hipercolesterolemia familiar tiene evidencia de Fase 3 (también como uso establecido), mientras que la hipercolesterolemia por deficiencia de colesterol 7-alfa-hidroxilasa y la deficiencia de la proteína de transferencia de ésteres de colesterol solo cuentan con literatura preclínica o indirecta, sin ensayos clínicos.

---

## Evidencia de Ensayos Clínicos

Se listan los ensayos más relevantes para hiperlipoproteinemia (de 40 recuperados).

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01984424](https://clinicaltrials.gov/study/NCT01984424) | Fase 3 | Completado | 511 | Evolocumab vs ezetimiba en pacientes intolerantes a estatinas por efectos musculares; ezetimiba es comparador |
| [NCT00271817](https://clinicaltrials.gov/study/NCT00271817) | Fase 3 | Completado | 1220 | Ezetimiba/simvastatina con niacina en hiperlipidemia tipo IIa/IIb |
| [NCT00093899](https://clinicaltrials.gov/study/NCT00093899) | Fase 3 | Completado | 611 | Ezetimiba/simvastatina con fenofibrato en hiperlipidemia mixta |
| [NCT00092573](https://clinicaltrials.gov/study/NCT00092573) | Fase 3 | Completado | 576 | Coadministración de fenofibrato y ezetimiba en hiperlipidemia mixta |
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Fase 3 | Completado | 720 | Estudio ENHANCE: ezetimiba más simvastatina en dosis alta vs simvastatina sola en hipercolesterolemia familiar heterocigota |
| [NCT03847506](https://clinicaltrials.gov/study/NCT03847506) | Fase 4 | Completado | 127 | Ezetimiba/rosuvastatina con candesartán/amlodipino en hipertensión e hiperlipidemia; doble ciego, aleatorizado |
| [NCT00753883](https://clinicaltrials.gov/study/NCT00753883) | Fase 4 | Completado | 40 | Ezetimiba sola vs estatina en hipercolesterolemia; abierto y pequeño, evidencia de apoyo |
| [NCT01043380](https://clinicaltrials.gov/study/NCT01043380) | Fase 4 | Completado | 245 | Regresión de placa coronaria con inhibidor de absorción vs inhibidor de síntesis de colesterol |
| [NCT00705211](https://clinicaltrials.gov/study/NCT00705211) | N/A | Completado | 1794 | Estudio posautorización en Japón de 52 semanas con Zetia; apoya seguridad a largo plazo, no aleatorizado |
| [NCT06789432](https://clinicaltrials.gov/study/NCT06789432) | Fase 4 | Retirado | 0 | Combinación atorvastatina/ezetimiba vs atorvastatina sola; sin participantes, no aporta evidencia |

---

## Evidencia de Literatura

Prioridad: ensayos aleatorizados, luego revisiones y estudios observacionales.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [40347969](https://pubmed.ncbi.nlm.nih.gov/40347969/) | 2025 | ECA (Fase 3) | Lancet | Estudio TANDEM: combinación fija de obicetrapib y ezetimiba para reducir el colesterol LDL |
| [25282519](https://pubmed.ncbi.nlm.nih.gov/25282519/) | 2015 | ECA | Lancet | RUTHERFORD-2: evolocumab en hipercolesterolemia familiar heterocigota pese a estatinas con o sin ezetimiba |
| [41206969](https://pubmed.ncbi.nlm.nih.gov/41206969/) | 2026 | ECA | JAMA | Enlicitida oral (inhibidor de PCSK9) en hipercolesterolemia familiar heterocigota |
| [37850379](https://pubmed.ncbi.nlm.nih.gov/37850379/) | 2024 | ECA | Circulation | ORION-5: inclisirán en hipercolesterolemia familiar homocigota |
| [40682836](https://pubmed.ncbi.nlm.nih.gov/40682836/) | 2025 | Revisión | Molecular Medicine Reports | Avances en fármacos actuales dirigidos a la hiperlipidemia |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Revisión | J Am Coll Cardiol | Terapias nuevas y emergentes para reducir LDL-C y apolipoproteína B, sobre la base de estatinas y ezetimiba |
| [35593194](https://pubmed.ncbi.nlm.nih.gov/35593194/) | 2022 | Revisión | J Cardiovasc Pharmacol Ther | Revisión integral de inhibidores de PCSK9 |
| [35101175](https://pubmed.ncbi.nlm.nih.gov/35101175/) | 2022 | Cohorte retrospectiva | Lancet | Experiencia mundial en hipercolesterolemia familiar homocigota |
| [29219151](https://pubmed.ncbi.nlm.nih.gov/29219151/) | 2017 | Revisión | Nat Rev Dis Primers | Hipercolesterolemia familiar: genética, diagnóstico y tratamiento |
| [31538826](https://pubmed.ncbi.nlm.nih.gov/31538826/) | 2019 | Reporte de caso | J Investig Med High Impact Case Rep | Dislipidemia combinada grave con base genética compleja |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20138715 (cancelado) | EZIT-ST 10/10 (HETERO LABS LIMITED) | Tableta | Simvastatina, combinaciones, paquetes |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** pancreatitis, enfermedad hepática, enfermedad de la vesícula biliar, miopatía, enfermedades musculares, enfermedad del músculo esquelético, parálisis periódica familiar, abuso o dependencia de sustancias, rabdomiólisis y fascitis nodular.
- **Interacciones farmacológicas:** se identificaron 100 interacciones potenciales. Las de nivel moderado incluyen:
  - ácido quenodesoxicólico
  - eluxadolina
  - rosuvastatina
  - simvastatina

  Otras (calcitriol, pantoprazol, glimepirida, mesalazina, doxiciclina, metformina, omeprazol y morfina, entre otras) tienen nivel de gravedad no definido.

No se dispone de advertencias ni contraindicaciones del prospecto del INVIMA; se recomienda consultarlo.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen varios ensayos de Fase 3 completados con ezetimiba en hipercolesterolemia e hiperlipidemia mixta, lo que respalda el nivel L1. Sin embargo, es un uso ya establecido y no un reposicionamiento novedoso. Además, el único registro sanitario colombiano está cancelado y faltan datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto del INVIMA (advertencias y contraindicaciones), requisito previo para el tamizaje de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Confirmar si existen productos con ezetimiba vigentes en Colombia, ya que el único registro hallado está cancelado.
- Precaución con la combinación con estatinas por el riesgo muscular y hepático señalado en el grafo de conocimiento.
- No priorizar las predicciones de deficiencia de colesterol 7-alfa-hidroxilasa (L4) ni de deficiencia de CETP (L5), que quedan en "Hold" por falta de evidencia clínica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

