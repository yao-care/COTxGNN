---
layout: default
title: Lovastatin
parent: Solo Predicción del Modelo (L5)
nav_order: 414
evidence_level: L5
indication_count: 1
monitor_inn: "Lovastatin"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-10-23
description: "Lovastatin: nueva indicación predicha, Deficiencia de la proteína de transferencia de ésteres de colesterol (nivel de evidencia L5). Indicación original: Lovastatina"
---

# Lovastatin
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

## Lovastatina: De Hipercolesterolemia a Deficiencia de la Proteína de Transferencia de Ésteres de Colesterol
{: .text-alpha }

## Resumen en Una Frase

Lovastatina es una estatina con registro sanitario vigente en Colombia en tabletas orales; según la información farmacológica compilada, se utiliza en hipercolesterolemia y dislipidemia mixta. El modelo TxGNN predice que podría ser efectivo para la **deficiencia de la proteína de transferencia de ésteres de colesterol (CETP)**, pero **no hay ensayos clínicos** y solo hay **1 publicación preclínica** que no estudia directamente esta enfermedad, por lo que la predicción carece de respaldo clínico.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Lovastatina (el texto del registro sanitario solo indica el nombre del principio activo, sin indicación detallada) |
| Nueva Indicación Predicha | Deficiencia de la proteína de transferencia de ésteres de colesterol |
| Puntaje de Predicción TxGNN | 0.9942 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 2) |
| Número de Registros Sanitarios | Al menos 2 (la lista puede estar incompleta) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro de origen. Según la información farmacológica compilada, lovastatina inhibe la enzima HMG-CoA reductasa (HMGCR) y también aparece asociada al receptor X de pregnano (NR1I2). Reduce el colesterol LDL y se utiliza en hipercolesterolemia y dislipidemia mixta.

La deficiencia de CETP es una condición genética que eleva el colesterol HDL y altera la remodelación de lipoproteínas. Existe un vínculo plausible por compartir vías del metabolismo lipídico, pero es **indirecto**. No se conoce que las estatinas traten esta deficiencia, que tiene un fenotipo en gran medida benigno o de alteración lipídica.

El puntaje alto de TxGNN (0.9942) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica; es una predicción computacional, no evidencia clínica. Dado que falta el dato del mecanismo original, el razonamiento mecanístico no puede validarse contra la fuente.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [19965609](https://pubmed.ncbi.nlm.nih.gov/19965609/) | 2010 | Preclínico (modelo animal) | Journal of Lipid Research | La eliminación dirigida de StARD4, una proteína de transferencia de lípidos, produce una reducción modesta de peso y alteraciones menores del metabolismo lipídico en ratones. No estudia lovastatina ni la deficiencia de CETP. |

## Información de Mercado en Colombia

La lista puede estar incompleta (se indican al menos 2 registros).

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 38340 | LOVASTATINA 20 MG TABLETAS (Tecnoquímicas S.A., Planta Yumbo) | Tableta | LOVASTATINA (sin indicación detallada) |
| 1981959 | LOVASTATINA 20 MG TABLETAS (Novamed S.A.S.) | Tableta | LOVASTATINA (sin indicación detallada) |

## Consideraciones de Seguridad

- **Relaciones de contraindicación registradas en el grafo de conocimiento** (no provienen del texto del prospecto): enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia, hiperglucemia, úlcera péptica, miopatía y enfermedades musculares, rabdomiólisis, diabetes mellitus, cetoacidosis diabética, trastornos hipotensivos, gota, abuso o dependencia de sustancias, trastornos de la coagulación, síndrome coronario agudo, enfermedad coronaria, infarto de miocardio, trombosis coronaria, hemoglobinopatía, lesiones, hipofosfatemia, fascitis nodular y parálisis periódica familiar. Deben verificarse contra el prospecto oficial.
- **Interacciones farmacológicas**: la consulta se completó, pero solo devolvió relaciones farmacológicas con dianas (HMG-CoA reductasa y receptor X de pregnano), no interacciones clínicas con otros medicamentos.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La puntuación proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica (nivel L5). No hay ensayos clínicos ni estudios que evalúen lovastatina en la deficiencia de CETP, y el vínculo mecanístico es indirecto. Además, esta condición no se considera una enfermedad que requiera tratamiento hipolipemiante.

**Para avanzar se necesita:**
- Establecer si la deficiencia de CETP constituye una necesidad clínica que justifique tratamiento
- Estudios preclínicos o de mecanismo que evalúen directamente lovastatina en este contexto
- Datos del mecanismo de acción de la fuente original
- Prospecto oficial de INVIMA con advertencias y contraindicaciones
- Texto de indicación aprobada de los registros sanitarios, que solo muestran el nombre del principio activo
- Perfil de seguridad, en especial riesgos musculares y hepáticos, para esta población
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

