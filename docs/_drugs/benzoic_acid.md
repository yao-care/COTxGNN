---
layout: default
title: Benzoic Acid
parent: Solo Predicción del Modelo (L5)
nav_order: 101
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
description: "Benzoic Acid: nueva indicación predicha, Bronquitis (nivel de evidencia L5). Indicación original: Ácido salicílico, ácido benzoico"
monitor_inn: "benzoic acid"
predicted_indications: ["bronchitis", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "dry eye syndrome", "palmar fibromatosis", "Ledderhose disease", "infantile digital fibromatosis", "hereditary angioedema with C1Inh deficiency", "posterior leukoencephalopathy syndrome", "C1 inhibitor deficiency"]
---

# Benzoic Acid
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

## Ácido Benzoico: De Ácido Salicílico/Aminobenzoico (uso tópico) a Bronquitis
{: .text-alpha }

## Resumen en Una Frase

El ácido benzoico se registró en Colombia en productos de uso tópico (ungüento y solución), asociado a ácido salicílico y ácido aminobenzoico.
El modelo TxGNN predice que podría ser efectivo para **bronquitis**,
pero actualmente **no hay ensayos clínicos** y solo **2 publicaciones**, ninguna de las cuales estudia el ácido benzoico, por lo que la predicción carece de respaldo real.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Ácido salicílico, ácido benzoico (el registro no detalla una enfermedad específica) |
| Nueva Indicación Predicha | Bronquitis |
| Puntaje de Predicción TxGNN | 0.9998 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 5 de 5) |
| Número de Registros Sanitarios | 5 (vigentes: 5) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, el ácido benzoico se ha usado en preparaciones dermatológicas tópicas, normalmente combinado con ácido salicílico, y no existe un vínculo mecanístico establecido con la bronquitis.

Las dos publicaciones recuperadas para esta predicción tratan sobre repaglinida en diabetes tipo 2 y sobre un inhibidor de la epóxido hidrolasa soluble en EPOC inducida por humo de tabaco. Ninguna estudia el ácido benzoico. El puntaje alto proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica ni clínica directa.

Además, existe una diferencia importante de vía: los productos registrados son tópicos (ungüento y solución), mientras que la bronquitis requeriría una vía respiratoria u oral. La compatibilidad de vía aún no se ha evaluado.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [11577798](https://pubmed.ncbi.nlm.nih.gov/11577798/) | 2001 | Revisión | Drugs | Revisión del uso terapéutico de repaglinida (derivado del ácido benzoico) en diabetes tipo 2; no estudia el ácido benzoico ni la bronquitis |
| [22180869](https://pubmed.ncbi.nlm.nih.gov/22180869/) | 2012 | Preclínico (animal) | Am J Respir Cell Mol Biol | Inhibidor de epóxido hidrolasa soluble en EPOC inducida por humo; no involucra ácido benzoico |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19930281 | NIXODERM UNGUENTO | Ungüento tópico | Ácido salicílico, ácido benzoico (vigente) |
| 20028320 | DERMICOX | Solución tópica | Ácido aminobenzoico (vigente) |

---

## Consideraciones de Seguridad

No se dispone de advertencias ni contraindicaciones de prospecto ni de interacciones farmacológicas registradas. Consultar el prospecto para información de seguridad.

Como señal de alerta adicional, el grafo de conocimiento (no el texto del prospecto) asocia al fármaco con contraindicaciones en las siguientes condiciones:
- **Cardiovasculares:** hipertensión, enfermedad coronaria, paro cardíaco súbito, enfermedad de conducción cardíaca, enfermedad cardiovascular y cardiopatía.
- **Hepáticas y renales:** insuficiencia hepática, enfermedad hepática, enfermedad renal, enfermedad de la vesícula biliar y piouréter.
- **Metabólicas:** diabetes mellitus, cetoacidosis diabética, enfermedad por almacenamiento de glucógeno, cistinuria y galactosemia.
- **Hematológicas:** trastornos de la coagulación, hemofilia, anemia, anemia macrocítica y deficiencia de G6PD.
- **Neuromusculares:** miastenia gravis, miastenia gravis de inicio en la adultez y enfermedad de la unión neuromuscular.
- **Gastrointestinales y otras:** gastritis, acalasia, megaesófago, anorexia nerviosa e hiperplasia prostática benigna.

Estas relaciones provienen de predicciones del modelo TxGNN (aprendizaje profundo) y deben verificarse con fuentes regulatorias antes de cualquier uso.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo, sin ensayos clínicos ni literatura que estudie el ácido benzoico en bronquitis (nivel L5). Además, los productos eran tópicos, lo que limita la viabilidad inmediata.

<!-- review:begin co-lic-20261105-benzoic_acid-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, los registros sanitarios en Colombia están cancelados y los productos eran tópicos, lo que limita la viabilidad inmediata." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 5 registros sanitarios (vigentes: 5); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-benzoic_acid-1 -->

**Para avanzar se necesita:**
- Datos del mecanismo de acción (consulta a DrugBank) que justifiquen un vínculo con la bronquitis.
- Prospecto de INVIMA con advertencias y contraindicaciones para completar el análisis de seguridad (dato bloqueante).
- Estudios preclínicos o clínicos que evalúen directamente el ácido benzoico en bronquitis.
- Evaluación de compatibilidad de vía de administración (tópica frente a respiratoria u oral).
- Revisión de las contraindicaciones señaladas por el grafo de conocimiento.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "los registros sanitarios en Colombia están cancelados y" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

