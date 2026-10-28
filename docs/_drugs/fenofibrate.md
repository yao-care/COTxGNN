---
layout: default
title: Fenofibrate
parent: Solo Predicción del Modelo (L5)
nav_order: 279
evidence_level: L5
indication_count: 1
monitor_inn: "Fenofibrate"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-10-23
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
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 1) |
| Número de Registros Sanitarios | Al menos 1 (la lista puede ser parcial) |
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

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20114242 | PRAVAFEN® CÁPSULAS | Cápsula dura | PRAVASTATINA Y FENOFIBRATO |

La lista puede ser parcial. Este producto es una combinación; su licencia no describe cómo está aprobado el fenofibrato como principio activo único.

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
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

