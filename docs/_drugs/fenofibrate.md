---
layout: default
title: Fenofibrate
parent: Solo Predicción del Modelo (L5)
nav_order: 279
evidence_level: L5
indication_count: 1
monitor_inn: "Fenofibrate"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-11-24
description: "Fenofibrate: nueva indicación predicha, Deficiencia de la proteína de transferencia de ésteres de colesterol (nivel de evidencia L5). Indicación original: PRAVASTATINA Y FENOFIBRATO"
---

# Fenofibrate
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Fenofibrato: De Pravastatina y Fenofibrato (dislipidemia) a Deficiencia de la proteína de transferencia de ésteres de colesterol
{: .text-alpha }

## Resumen en Una Frase

Fenofibrato es un fármaco registrado en Colombia en una combinación con pravastatina (producto PRAVAFEN® cápsulas), cuyo texto de indicación aprobado solo dice "PRAVASTATINA Y FENOFIBRATO".
El modelo TxGNN predice que podría ser efectivo para la **deficiencia de la proteína de transferencia de ésteres de colesterol**, pero hay **0 ensayos clínicos** y **3 publicaciones** preclínicas o mecanísticas, ninguna de las cuales estudia directamente esta enfermedad en pacientes.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | PRAVASTATINA Y FENOFIBRATO (texto de la licencia; no detalla una enfermedad) |
| Nueva Indicación Predicha | Deficiencia de la proteína de transferencia de ésteres de colesterol |
| Puntaje de Predicción TxGNN | 0.9961 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 3 de 3) |
| Número de Registros Sanitarios | 3 (vigentes: 3) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción del fármaco. Según la información de farmacología disponible, el fenofibrato actúa como agonista del receptor PPARα (la actividad reside en su metabolito activo) y se usa para reducir colesterol y triglicéridos. También se registra una interacción con la proteína de unión a ácidos grasos 1 (dato en rata).

La deficiencia de CETP se caracteriza por HDL muy elevado, con transferencia alterada de ésteres de colesterol. La literatura recuperada muestra solo un vínculo biológico en el metabolismo de las HDL: la combinación de agonismo PPARα e inhibición de CETP modifica los niveles de HDL y LDL en ratones transgénicos (PMID 20332533), y el fenofibrato induce la expresión de PLTP, lo que contribuye al agrandamiento de las HDL en ratones (PMID 11342537).

Sin embargo, la deficiencia de CETP es una condición rara que suele presentarse con HDL alto y no como un estado que requiera corrección, por lo que el fundamento terapéutico del fenofibrato es poco claro. El puntaje alto de TxGNN es una predicción computacional y no está respaldado por evidencia clínica para esta indicación.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [20332533](https://pubmed.ncbi.nlm.nih.gov/20332533/) | 2010 | Preclínico/mecanístico | J Cardiovasc Pharmacol Ther | En ratones transgénicos con ApoB100 y CETP humanas, la inhibición de CETP (torcetrapib) y el agonismo PPARα (fenofibrato) modifican el perfil lipídico, con aumento de HDL y reducción de LDL. |
| [11342537](https://pubmed.ncbi.nlm.nih.gov/11342537/) | 2001 | Preclínico/mecanístico | J Biol Chem | La inducción del gen de la proteína de transferencia de fosfolípidos explica el agrandamiento de las HDL en ratones tratados con fenofibrato. |
| [30271349](https://pubmed.ncbi.nlm.nih.gov/30271349/) | 2018 | Preclínico/mecanístico | Front Physiol | No se observó correlación entre HDL plasmático, colesterol fecal y capacidad de eflujo de colesterol, lo que sugiere la importancia de la función de las HDL. |

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 20024180 | NORTRICOL 200 CAPSULAS | CAPSULA DURA | FENOFIBRATO | Vigente |
| 20057142 | FENOLIP® 200 MG CAPSULA | CAPSULA DURA | FENOFIBRATO | Vigente |
| 20114242 | PRAVAFEN® CAPSULAS | CAPSULA DURA | PRAVASTATINA Y FENOFIBRATO | Vigente |

Se muestran los 3 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

De estos registros, PRAVAFEN® (pravastatina/fenofibrato) es una combinación; su licencia no describe cómo está aprobado el fenofibrato como principio activo único.

<!-- review:begin co-lic-20261124b-fenofibrate-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "La lista puede ser parcial. Este producto es una combinación; su licencia no describe cómo está aprobado el fenofibrato como principio activo único." Corregido según los datos del INVIMA (Código Único de Medicamentos, datos al 2026-11-23): además de PRAVAFEN® (combinación), figuran productos de fenofibrato como único principio activo (NORTRICOL 200 y FENOLIP® 200 MG); se eliminó la advertencia de lista parcial. Las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261124b-fenofibrate-1 -->

## Consideraciones de Seguridad

- **Contraindicaciones registradas en el grafo de conocimiento** (relaciones del grafo, no texto de prospecto): insuficiencia hepática, enfermedad hepática, pancreatitis, enfermedad de la vesícula biliar, colelitiasis y colecistolitiasis, miopatía y enfermedades musculares, rabdomiólisis, trombocitopenia, anemia, leucopenia, agranulocitosis, neutropenia (incluidas formas congénitas), y alteración de la función renal.
- **Interacciones farmacológicas**: los datos disponibles corresponden a interacciones con dianas (PPARα y proteína de unión a ácidos grasos 1), no a interacciones con otros medicamentos.

Consultar el prospecto para la información de advertencias y contraindicaciones oficiales.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni estudios que investiguen directamente la deficiencia de CETP con fenofibrato; solo existen estudios preclínicos sobre metabolismo de HDL, por lo que el nivel de evidencia es L5. Además, el fundamento terapéutico es dudoso, ya que esta condición cursa con HDL elevado.

**Para avanzar se necesita:**
- Aclarar si existe una necesidad clínica real en esta enfermedad rara y qué desenlace se buscaría mejorar.
- Estudios directos en la enfermedad (modelos o pacientes) que respalden la hipótesis.
- Datos del mecanismo de acción y del prospecto de INVIMA (advertencias y contraindicaciones) para el análisis de seguridad.
- Revisión de la seguridad frente a las contraindicaciones del grafo de conocimiento (hepáticas, musculares, renales y hematológicas).

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-24 | Este producto → PRAVAFEN® | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

