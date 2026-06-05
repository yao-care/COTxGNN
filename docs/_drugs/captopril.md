---
layout: default
title: Captopril
parent: 僅模型預測 (L5)
nav_order: 82
evidence_level: L5
indication_count: 4
---

# Captopril
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

Usando `txgnn-pipeline` para orientar la generación del informe de reposicionamiento con la estructura correcta para el despliegue en Colombia.

---

# Captopril: De Hipertensión Arterial a Hipertensión Renovascular Maligna

## Resumen en Una Frase

Captopril es el prototipo de los inhibidores de la enzima convertidora de angiotensina (IECA), reconocido mundialmente por su uso en el tratamiento de la hipertensión arterial y la insuficiencia cardíaca congestiva. El modelo TxGNN predice que podría ser efectivo para la **Hipertensión Renovascular Maligna**, con un puntaje de predicción del **99.28%** y **20 publicaciones científicas** que actualmente respaldan esta dirección. No se identificaron ensayos clínicos registrados específicamente para esta indicación.

---

## Resumen Rápido

| Ítem | Contenido |
|------|-----------|
| Indicación Original | Hipertensión arterial (indicación clásica IECA; sin registros INVIMA disponibles) |
| Nueva Indicación Predicha | Hipertensión renovascular maligna |
| Puntaje de Predicción TxGNN | 99.28% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Sin embargo, Captopril es el IECA prototipo: bloquea la enzima convertidora de angiotensina (ECA), impidiendo la conversión de angiotensina I en angiotensina II (Ang II). Esto reduce la vasoconstricción periférica, suprime la secreción de aldosterona y disminuye la retención de sodio y agua, produciendo un descenso sostenido de la presión arterial.

La hipertensión renovascular maligna comparte precisamente este eje fisiopatológico. La estenosis de la arteria renal provoca isquemia renal → secreción excesiva de renina → sobreactivación del sistema renina-angiotensina-aldosterona (SRAA) → sobreproducción de Ang II → vasoconstricción grave y sobrecarga de volumen impulsada por aldosterona. Captopril actúa directamente sobre el paso limitante de esta cascada, lo que otorga una coherencia mecanística muy alta entre el fármaco y la indicación predicha.

No obstante, existe una contraindicación clínica crítica que debe tenerse en cuenta: en pacientes con **estenosis bilateral de arteria renal** o **riñón único funcionante con estenosis**, el uso de IECAs puede eliminar la vasoconstricción compensatoria de la arteriola eferente, precipitando una caída brusca de la tasa de filtración glomerular y un riesgo real de insuficiencia renal aguda. El uso de captopril es apropiado principalmente en estenosis unilateral, con monitoreo estricto de la función renal. Cabe señalar también que la escintigrafía renal con captopril (*captopril renogram*) es una herramienta diagnóstica estándar para confirmar hipertensión renovascular, por lo que una parte de la literatura recuperada corresponde a uso diagnóstico y no al uso terapéutico del fármaco.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [17008836](https://pubmed.ncbi.nlm.nih.gov/17008836/) | 2006 | Revisión | *Minerva Medica* | Revisión de conceptos clínicos de hipertensión renovascular; evalúa el rol diagnóstico y terapéutico del captopril en estenosis de arteria renal |
| [2040938](https://pubmed.ncbi.nlm.nih.gov/2040938/) | 1991 | Revisión | *The Journal of Pediatrics* | Revisión de hipertensión maligna incluyendo fisiopatología y enfoque terapéutico en población pediátrica |
| [3894732](https://pubmed.ncbi.nlm.nih.gov/3894732/) | 1985 | Cohorte observacional | *Japanese Journal of Medicine* | Evalúa la utilidad del test con captopril para el diagnóstico de hipertensión renovascular y aldosteronismo primario en cohorte de pacientes hipertensos |
| [232024](https://pubmed.ncbi.nlm.nih.gov/232024/) | 1979 | Estudio clínico | *Clinical Science (London)* | Demuestra que la hiperreninaemia reactiva al bloqueo con captopril (actividad de renina >14 ng/h/ml) identifica con alta especificidad la hipertensión renovascular frente a la hipertensión esencial |
| [8070421](https://pubmed.ncbi.nlm.nih.gov/8070421/) | 1994 | Serie de casos / Revisión | *Endocrinology & Metabolism Clinics of North America* | Análisis de tumores secretores de renina; documenta caída de presión arterial bajo tratamiento con captopril como criterio diagnóstico-terapéutico clave |
| [10955932](https://pubmed.ncbi.nlm.nih.gov/10955932/) | 2000 | Serie de casos | *Pediatric Nephrology* | Estudio prospectivo en 27 niños con neurofibromatosis tipo 1 (NF1); utiliza test de captopril y Doppler para evaluación de hipertensión renovascular secundaria |
| [6145432](https://pubmed.ncbi.nlm.nih.gov/6145432/) | 1984 | Observación clínica | *Biulleten' VKNTSAMN SSSR* | Uso directo de captopril en hipertensión arterial de curso estable y maligno; observación del efecto antihipertensivo en ambas presentaciones |
| [11334320](https://pubmed.ncbi.nlm.nih.gov/11334320/) | 2001 | Reporte de caso + Revisión | *Clinical Nephrology* | Dos casos de hipertensión renovascular asociada a neurofibromatosis; el test con captopril elevó la actividad de renina plasmática de 2.8 a 12.6 ng/ml/h, confirmando dependencia del SRAA |
| [2887673](https://pubmed.ncbi.nlm.nih.gov/2887673/) | 1987 | Estudio mecanístico | *Japanese Heart Journal* | Investigación neurohormonal en hipertensión bifásica de Goldblatt (fases benigna y maligna) en perros conscientes; caracteriza cambios en renina, Ang II, catecolaminas y vasopresina |
| [1572120](https://pubmed.ncbi.nlm.nih.gov/1572120/) | 1992 | Reporte de caso | *Clinical Nuclear Medicine* | Describe un caso de renograma con captopril falso positivo en hipertensión maligna sin estenosis arterial renal confirmada; discute los límites diagnósticos del método |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La hipertensión renovascular maligna está fisiopatológicamente impulsada por la sobreactivación del SRAA, y captopril —como IECA prototipo— actúa directamente sobre este eje con una coherencia mecanística muy alta. La evidencia de literatura (20 publicaciones, nivel L3) respalda la dirección predicha, aunque se concentra predominantemente en series observacionales, reportes de casos y estudios de uso diagnóstico, sin ensayos clínicos controlados específicos. La ausencia de registros INVIMA en Colombia y la contraindicación crítica en estenosis bilateral de arteria renal obligan a establecer guardianes clínicos estrictos antes de cualquier implementación.

**Para avanzar se necesita:**
- Completar el perfil de seguridad: obtener advertencias, contraindicaciones e interacciones farmacológicas desde el prospecto oficial (cubrir el gap de datos actual)
- Definir protocolo de selección de pacientes que excluya estenosis bilateral de arteria renal o riñón único funcionante con estenosis, previo al inicio del tratamiento
- Establecer plan de monitoreo de función renal (creatinina sérica, BUN, potasio) durante las primeras semanas de terapia
- Diseñar o identificar un ensayo clínico prospectivo o cohorte observacional controlada que evalúe captopril como tratamiento activo en hipertensión renovascular maligna
- Iniciar evaluación regulatoria ante INVIMA para el eventual registro sanitario de captopril en Colombia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

