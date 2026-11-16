---
layout: default
title: Alopurinol
parent: Solo Predicción del Modelo (L5)
nav_order: 39
evidence_level: L5
indication_count: 10
drugbank_id: DB00437
monitor_inn: "Allopurinol"
predicted_indications: ["hepatic porphyria", "idiopathic copper-associated cirrhosis", "hepatoportal sclerosis", "early-onset familial noncirrhotic portal hypertension", "primitive portal vein thrombosis", "hepatopulmonary syndrome", "disorder of phenylalanine metabolism", "immune-mediated necrotizing myopathy", "antisynthetase syndrome", "idiopathic eosinophilic myositis"]
last_modified_at: 2026-11-16
description: "Alopurinol: nueva indicación predicha, porfiria hepática (hepatic porphyria) (nivel de evidencia L5). Indicación original: ALOPURINOL"
---

# Alopurinol
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

## Alopurinol: porfiria hepática (hepatic porphyria)
{: .text-alpha }

## Resumen en Una Frase

Alopurinol es un medicamento oral de uso consolidado en Colombia, con nueve registros sanitarios vigentes. El modelo TxGNN predice que podría ser efectivo para **porfiria hepática (hepatic porphyria)**, pero actualmente no hay ensayos clínicos y solo **2 publicaciones** preclínicas o de hipótesis, ninguna con datos en humanos que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | ALOPURINOL |
| Nueva Indicación Predicha | porfiria hepática (hepatic porphyria) |
| Puntaje de Predicción TxGNN | 0.9995 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 9 de 9) |
| Número de Registros Sanitarios | 9 (vigentes: 9) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Alopurinol es un fármaco de administración oral, conocido como inhibidor de la xantina oxidasa, y su relación con la porfiria hepática es únicamente indirecta e hipotética.

La literatura recuperada sugiere que el alopurinol puede interactuar con el metabolismo del hemo hepático. Un artículo de hipótesis de 2019 plantea que inhibir la utilización del hemo o modular la 5-aminolevulinato sintasa (ALAS1) podría ser una estrategia para las porfirias hepáticas agudas. Sin embargo, el efecto del alopurinol sobre los precursores de porfirinas en humanos no está establecido, y algunos reportes antiguos indican que incluso podría alterar la síntesis del hemo. La dirección del efecto es incierta.

El puntaje elevado (0.9995) es solo una predicción computacional. Ningún estudio citado evalúa directamente el alopurinol en porfiria hepática, por lo que el nivel de evidencia se limita a L5, aunque el análisis preliminar lo había clasificado como L4.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Hipótesis/Revisión | Medical Hypotheses | Propone la modulación metabólica de la ALAS1 mediante triptófano o inhibidores de la utilización del hemo por la triptófano 2,3-dioxigenasa como posible terapia de las porfirias hepáticas agudas. No evalúa alopurinol directamente. |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Preclínico (rata) | Biochemical Pharmacology | Estudia el efecto de la carbamazepina sobre el metabolismo del hemo en hígado de rata, en relación con su capacidad de agravar las porfirias hepáticas. No evalúa alopurinol. |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 11415 | ALOPURINOL 300 MG | Tableta | ALOPURINOL |
| 18777 | UROCUAD® TABLETAS 100 MG. | Tableta | ALOPURINOL |
| 19966240 | ALLO TABLETA | Tableta | ALOPURINOL |
| 20049088 | ALOPURINOL 100 MG TABLETA | Tableta | ALOPURINOL |
| 20222454 | ZYLOPRIM 100MG TABLETAS | Tableta | ALOPURINOL |

Se muestran 5 de los 9 registros vigentes.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni estudios que evalúen directamente el alopurinol en porfiria hepática. La literatura disponible es preclínica o de hipótesis, y la dirección del efecto es incierta, con indicios de que el fármaco podría incluso perturbar la síntesis del hemo. El puntaje del modelo es una predicción computacional únicamente.

**Para avanzar se necesita:**
- Datos del mecanismo de acción del alopurinol y su efecto sobre ALAS1 y los precursores de porfirinas.
- Estudios preclínicos que evalúen específicamente el alopurinol en modelos de porfiria hepática.
- Revisión de las advertencias y contraindicaciones del prospecto aprobado por INVIMA.
- Evaluación de seguridad en pacientes con porfiria, dado el riesgo potencial de empeorar el metabolismo del hemo.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Esto puede deberse a que el producto está comercializado bajo nombres comerciales no indexados con el INN "ALOPURINOL", o bien a que efectiv" | Ya no aparece tras regenerar el informe (2026-11-16: el informe se regeneró en noviembre de 2026 y ya no contiene esta afirmación; antes: Corregido) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

