---
layout: default
title: Chlorthalidone
parent: Solo Predicción del Modelo (L5)
nav_order: 154
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Chlorthalidone: nueva indicación predicha, Glaucoma hereditario primario (nivel de evidencia L5). Indicación original: CLORTALIDONA"
monitor_inn: "Chlorthalidone"
predicted_indications: ["primary hereditary glaucoma", "open-angle glaucoma", "malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "chronic pulmonary heart disease", "acute pulmonary heart disease", "congenital hypotrichosis milia"]
---

# Chlorthalidone
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

# Clortalidona: De Clortalidona (indicación registrada sin detalle) a Glaucoma Hereditario Primario

## Resumen en Una Frase

Clortalidona es un diurético de tipo tiazídico, utilizado principalmente como antihipertensivo y para reducir edemas; en los registros sanitarios de Colombia solo figura con el nombre del principio activo, sin una indicación detallada.
El modelo TxGNN predice que podría ser efectivo para **glaucoma hereditario primario**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que se trata únicamente de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | CLORTALIDONA (el registro no detalla la indicación; el uso conocido es antihipertensivo y diurético) |
| Nueva Indicación Predicha | Glaucoma hereditario primario |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 3 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la clortalidona es un diurético de tipo tiazídico con acción antihipertensiva, y los datos de farmacología compilados muestran que interactúa con varias anhidrasas carbónicas (CA1, CA4, CA7, CA12 y CA14) y con la enzima NAPEPLD.

La única vía mecanística plausible hacia el glaucoma sería la inhibición débil de la anhidrasa carbónica, que teóricamente podría reducir la producción de humor acuoso y la presión intraocular. Sin embargo, esta actividad es secundaria en la clortalidona y no existen datos que la respalden en el ojo.

Además, el glaucoma hereditario primario es en gran parte una alteración estructural o del desarrollo, por lo que es poco probable que un mecanismo diurético sea relevante. Existen terapias antiglaucomatosas establecidas mucho más directas y eficaces. La predicción debe tomarse con mucha cautela.

Otras indicaciones predichas con puntajes similares (glaucoma de ángulo abierto, hipertensión maligna con afectación renal, hipertensión renovascular maligna, varias formas de hipertensión pulmonar y cor pulmonale) tampoco cuentan con evidencia directa. La excepción parcial es el cor pulmonale crónico, que tiene un informe clínico histórico (ver más abajo).

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para glaucoma hereditario primario.

Como referencia, para otras indicaciones predichas solo se identificó lo siguiente:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [5597001](https://pubmed.ncbi.nlm.nih.gov/5597001/) | 1967 | Informe clínico (histórico, probablemente no controlado) | La Clinica terapeutica | Terapia diurética con clortalidona en insuficiencia cardíaca congestiva por cor pulmonale crónico (indicación: cor pulmonale crónico) |
| [28711447](https://pubmed.ncbi.nlm.nih.gov/28711447/) | 2017 | Revisión | JACC. Heart Failure | Actualización sobre la transición de hipertensión a insuficiencia cardíaca; solo contexto general (indicación: cor pulmonale crónico) |
| [14288313](https://pubmed.ncbi.nlm.nih.gov/14288313/) | 1965 | Investigación básica (fisiología de insectos) | Journal of Cellular and Comparative Physiology | Transporte activo en el intestino medio de Cecropia; no relacionado con la enfermedad humana (indicación: hipertensión pulmonar por enfermedad pulmonar o hipoxia) |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20101174 (cancelado) | CARDIOL 25 MG® | Tableta recubierta | CLORTALIDONA |
| 20061697 (cancelado) | HIDROTEN® 25 MG TABLETAS | Tableta | CLORTALIDONA |
| 20126544 (cancelado) | CARDIOL® 12.5 MG | Tableta recubierta | CLORTALIDONA |

Los tres registros corresponden a productos de un solo principio activo, de administración oral, y ninguno está vigente.

---

## Consideraciones de Seguridad

- **Contraindicaciones potenciales según el grafo de conocimiento** (relaciones fármaco-enfermedad del modelo, no texto de prospecto): insuficiencia hepática, enfermedad renal, anuria, gota e hiperuricemia, pancreatitis, úlcera péptica, lupus eritematoso sistémico, asma, deficiencia de potasio, hipercalcemia y nefrocalcinosis, alteraciones del metabolismo del fósforo, diabetes mellitus (incluida la tipo 2), infarto de miocardio y trombosis coronaria, paro cardíaco súbito, hemoglobinopatías, psoriasis, epilepsia, y trastornos de ansiedad y distímicos.
- **Interacciones farmacológicas**: se identificaron 6 interacciones de tipo farmacológico (dianas moleculares), sin nivel de gravedad asignado: NAPEPLD y las anhidrasas carbónicas 1, 4, 7, 12 y 14. No se dispone de interacciones con otros medicamentos.

Las advertencias y contraindicaciones del prospecto de INVIMA no estaban disponibles; consultar el prospecto para la información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para glaucoma hereditario primario tiene un puntaje alto en el modelo (99.92%), pero carece de ensayos clínicos y literatura, y el mecanismo propuesto (inhibición débil de la anhidrasa carbónica) es especulativo y poco probable en una enfermedad principalmente estructural. Además, el producto no tiene registros sanitarios vigentes en Colombia.

**Para avanzar se necesita:**
- Datos del mecanismo de acción confirmados (por ejemplo, desde DrugBank).
- Advertencias y contraindicaciones del prospecto de INVIMA, necesarias para cualquier evaluación de seguridad.
- Estudios preclínicos que evalúen el efecto de la clortalidona sobre la presión intraocular y la dinámica del humor acuoso.
- Una revisión sistemática de la literatura sobre diuréticos tiazídicos y presión intraocular.
- Verificar la situación regulatoria actual (registros cancelados) antes de cualquier consideración local.
- Como alternativa, evaluar si el cor pulmonale crónico (nivel L4, pregunta de investigación) merece priorizarse, aunque la evidencia disponible es antigua y de beneficio solo sintomático.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

