---
layout: default
title: Sulfacetamide
parent: Solo Predicción del Modelo (L5)
nav_order: 594
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Sulfacetamide: nueva indicación predicha, Vasculitis postinfecciosa (nivel de evidencia L5). Indicación original: Sulfacetamida"
monitor_inn: "sulfacetamide"
predicted_indications: ["postinfectious vasculitis", "post-bacterial disorder", "otitis externa", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "exposure keratitis", "parasitic eyelid infestation"]
---

# Sulfacetamide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Sulfacetamida: De Indicación Original (Sulfacetamida oftálmica) a Vasculitis Postinfecciosa

## Resumen en Una Frase

Sulfacetamida es una sulfonamida antibacteriana de uso tópico, comercializada en Colombia como solución oftálmica al 10% (SULFAOFTAL®).
El modelo TxGNN predice que podría ser efectiva para **vasculitis postinfecciosa**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción; se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sulfacetamida (solución oftálmica; el registro no detalla la indicación clínica) |
| Nueva Indicación Predicha | Vasculitis postinfecciosa |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registro vigente) |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, la sulfacetamida es una sulfonamida tópica que inhibe la dihidropteroato sintasa bacteriana, bloqueando la síntesis de ácido fólico en las bacterias, y su uso establecido es en infecciones oculares bacterianas, como la conjuntivitis.

La vasculitis postinfecciosa es un proceso mediado por el sistema inmune que aparece después de una infección. Un antibacteriano actúa sobre la bacteria activa, no sobre la respuesta inmunitaria secuelar. Por ello, **no se ha establecido un vínculo mecanístico plausible**: el puntaje alto de TxGNN refleja probablemente una asociación en el grafo de conocimiento (fármaco antibacteriano ↔ enfermedades vinculadas a infección) y no una razón farmacológica sólida.

Otras predicciones del modelo tampoco cuentan con respaldo clínico. Las más plausibles biológicamente son **otitis externa** y **queratoconjuntivitis epitelial punctata**, por la naturaleza antibacteriana y oftálmica del fármaco, aunque ambas carecen de ensayos y literatura. Para otitis externa existen además tratamientos tópicos establecidos (gotas de fluoroquinolonas o aminoglucósidos).

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Para la indicación principal (vasculitis postinfecciosa) actualmente no hay literatura relacionada disponible.

En predicciones secundarias se identificaron dos publicaciones, ninguna de las cuales demuestra eficacia:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [3157322](https://pubmed.ncbi.nlm.nih.gov/3157322/) | 1985 | Reporte de caso | American Journal of Ophthalmology | Niño de 8 años con eritema multiforme mayor tras uso tópico de sulfacetamida sódica por conjuntivitis. Es una señal de seguridad, no de eficacia (predicción: queratitis por exposición). |
| [18561612](https://pubmed.ncbi.nlm.nih.gov/18561612/) | 2007 | Observacional/Revisión | Annales Academiae Medicae Stetinensis | Describe el papel de *Demodex* en la blefaritis marginal crónica; trata la etiología de la enfermedad y no evalúa la sulfacetamida (predicción: infestación parasitaria del párpado). |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20022399 (cancelado) | SULFAOFTAL® 10% SOLUCIÓN OFTÁLMICA | Solución oftálmica | Sulfacetamida |

El único registro sanitario existente (Laboratorios Blaskov SAS) está cancelado, por lo que actualmente no hay producto vigente en el mercado colombiano.

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (relaciones fármaco-enfermedad de TxGNN/PrimeKG, no texto de prospecto): hipertensión, porfiria (hereditaria y del metabolismo de porfirinas), enfermedad renal, enfermedad hematológica, enfermedad hepática, enfermedad de la vesícula biliar, exantema, queratitis por herpes simple, glaucoma de ángulo abierto y de ángulo cerrado, hipertensión ocular, diabetes mellitus y cetoacidosis diabética, hiperplasia prostática benigna, enfermedad cardíaca y cardiovascular, enfermedad coronaria, paro cardíaco súbito, trastornos de la conducción cardíaca, deficiencia de G6PD, enfermedad por depósito de glucógeno, cistinuria, galactosemia, dermatitis e hipertiroidismo. Deben verificarse contra el prospecto oficial.
- **Señal de seguridad en la literatura**: reporte de eritema multiforme mayor tras sulfacetamida tópica (1985), reacción cutánea grave propia de las sulfonamidas.
- **Síndrome urémico hemolítico asociado a infección**: las predicciones del modelo para esta condición conllevan preocupaciones de seguridad más que beneficio potencial, pues los antibióticos generalmente no se recomiendan en el SUH por STEC.
- No se encontraron interacciones farmacológicas en la consulta realizada.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el puntaje del modelo (nivel L5), sin ensayos ni literatura, y carece de plausibilidad mecanística, ya que un antibacteriano tópico no actúa sobre una vasculitis inmunomediada. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Obtener el prospecto del INVIMA (advertencias y contraindicaciones), que constituye una brecha bloqueante para la evaluación de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Si se desea continuar, priorizar indicaciones con mayor plausibilidad biológica (otitis externa, queratoconjuntivitis infecciosa) frente a vasculitis postinfecciosa, con revisión sistemática de la literatura y comparación con tratamientos estándar.
- Evaluar la viabilidad regulatoria, dado que no existe registro vigente.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

