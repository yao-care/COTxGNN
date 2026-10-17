---
layout: default
title: Denosumab
parent: Solo Predicción del Modelo (L5)
nav_order: 202
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Denosumab: nueva indicación predicha, Retinopatía diabética no proliferativa grave (nivel de evidencia L5). Indicación original: Denosumab"
monitor_inn: "DENOSUMAB"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetic retinopathy"]
---

# Denosumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Denosumab: De Denosumab (indicación original no especificada en el registro) a Retinopatía Diabética No Proliferativa Grave

## Resumen en Una Frase

Denosumab es un anticuerpo monoclonal dirigido contra RANKL, comercializado en Colombia bajo las marcas XGEVA® y PROLIA®; el registro sanitario local solo lista el nombre del principio activo como indicación aprobada, sin detallar el uso clínico.
El modelo TxGNN predice que podría ser efectivo para **retinopatía diabética no proliferativa grave**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden directamente esta indicación (la segunda predicción, retinopatía diabética, cuenta con 2 publicaciones indirectas).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Denosumab (el registro sanitario no detalla la indicación aprobada) |
| Nueva Indicación Predicha | Retinopatía diabética no proliferativa grave |
| Puntaje de Predicción TxGNN | 99.63% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según el conocimiento general, denosumab es un anticuerpo monoclonal que inhibe RANKL (ligando del receptor activador del factor nuclear kappa-B), y se utiliza en osteoporosis y otras condiciones de pérdida ósea. Esta descripción del mecanismo proviene de conocimiento general y no de los datos compilados.

Un vínculo hipotético con la retinopatía diabética podría pasar por la señalización RANKL/RANK/OPG, que se ha relacionado con calcificación vascular, inflamación y disfunción microvascular asociada a la diabetes. Sin embargo, este vínculo **no está establecido** por la evidencia disponible: es una predicción computacional sin datos clínicos ni mecanísticos de respaldo.

La similitud entre la indicación original y la nueva indicación queda pendiente de evaluación. Por ahora, el puntaje alto de TxGNN (99.63%) debe interpretarse solo como una señal para priorizar la investigación, no como evidencia de eficacia.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Para la indicación principal (retinopatía diabética no proliferativa grave) no hay literatura relacionada disponible.

Para la segunda predicción, **retinopatía diabética** (puntaje TxGNN 99.23%), se recuperaron dos publicaciones de contexto indirecto. Ninguna evalúa desenlaces retinianos:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38899553](https://pubmed.ncbi.nlm.nih.gov/38899553/) | 2024 | Observacional/Cohorte (con revisión sistemática y metaanálisis) | Diabetes, Obesity & Metabolism | Evalúa si denosumab en osteoporosis, frente a bisfosfonatos, se asocia con menor incidencia de diabetes tipo 2 y con mejores desenlaces a largo plazo (complicaciones microvasculares y macrovasculares, mortalidad por todas las causas). El título reporta menor incidencia de diabetes tipo 2, menos ulceración del pie y menor mortalidad. |
| [36960265](https://pubmed.ncbi.nlm.nih.gov/36960265/) | 2023 | Observacional | Cureus | Evalúa el uso de la herramienta FRAX para estimar el riesgo de fractura en adultos con diabetes tipo 2 y la proporción de pacientes de alto riesgo bajo tratamiento antiosteoporótico. No estudia retinopatía. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20052945 | XGEVA® 120 MG/1.7 ML | Solución inyectable | Denosumab | Cancelado |
| 20028103 | PROLIA® | Solución inyectable | Denosumab | Cancelado |

Ambos registros pertenecen a AMGEN MANUFACTURING LIMITED LLC. Actualmente no hay registros vigentes en Colombia.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la consulta de interacciones se completó y arrojó 100 interacciones registradas. Las primeras 20 listadas son de nivel **moderado**:
  - Corticosteroides: hidrocortisona, triamcinolona (incluida la oftálmica), dexametasona, betametasona, budesonida, prednisolona, prednisona, metilprednisolona.
  - Hormonas adrenocorticotrópicas: corticotropina, tetracosactida.
  - Radiofármacos y anticuerpos relacionados: ibritumomab tiuxetán, iobenguano (I-131), tositumomab (I-131), tositumomab.
  - Inmunomoduladores y antimetabolitos: levamisol, trimetrexato, mercaptopurina, dupilumab, tacrolimus.

Cabe destacar que la triamcinolona oftálmica figura entre las interacciones, un dato relevante si se considerara un uso en enfermedad retiniana.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura que estudien desenlaces retinianos con denosumab. Además, el mercado colombiano solo muestra registros cancelados, lo que complica cualquier vía de acceso inmediata.

**Para avanzar se necesita:**
- Obtener los datos del mecanismo de acción (por ejemplo, consultando DrugBank) y analizar el vínculo RANKL/OPG con la patología retiniana diabética.
- Obtener el prospecto de INVIMA para completar el perfil de advertencias y contraindicaciones (requisito previo para cualquier evaluación de seguridad).
- Realizar una búsqueda dirigida de estudios preclínicos y clínicos de denosumab o la vía RANKL en retinopatía diabética.
- Aclarar el estado regulatorio: verificar si existen otros registros vigentes de denosumab en Colombia (incluidos biosimilares) o si se requeriría una nueva solicitud.
- Evaluar la compatibilidad de la vía de administración (pendiente) para un posible uso en enfermedad retiniana.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

