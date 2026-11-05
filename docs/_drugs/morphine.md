---
layout: default
title: Morphine
parent: Solo Predicción del Modelo (L5)
nav_order: 456
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-06
monitor_inn: "morphine"
predicted_indications: ["myofascial pain syndrome", "manic bipolar affective disorder", "Tourette syndrome", "restless legs syndrome", "attention deficit hyperactivity disorder, inattentive type", "migraine disorder", "trichotillomania", "methemoglobinemia", "migraine with brainstem aura", "specific developmental disorder"]
description: "Morphine: nueva indicación predicha, Síndrome de dolor miofascial (myofascial pain syndrome) (nivel de evidencia L5). Indicación original: MORFINA"
---

# Morphine
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

## Morphine: Síndrome de dolor miofascial (myofascial pain syndrome)
{: .text-alpha }

## Resumen en Una Frase

La morfina es un analgésico opioide agonista del receptor mu, con registros sanitarios locales en Colombia en solución oral e inyectable.
El modelo TxGNN predice que podría ser efectiva para el **síndrome de dolor miofascial (myofascial pain syndrome)**, pero ningún estudio recopilado evalúa directamente la morfina en esta enfermedad, por lo que el nivel de evidencia es **L5**.
Los datos compilados para este informe incluyen **0 ensayos clínicos** y **10 publicaciones**, todas indirectas.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | MORFINA |
| Nueva Indicación Predicha | Síndrome de dolor miofascial (myofascial pain syndrome) |
| Puntaje de Predicción TxGNN | 0.9975 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 2 de 2) |
| Número de Registros Sanitarios | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Por conocimiento farmacológico general, la morfina es un agonista del receptor opioide mu con actividad analgésica central, por lo que un vínculo con el dolor musculoesquelético es plausible en teoría.

Sin embargo, los opioides no se recomiendan como tratamiento estándar del dolor miofascial. La literatura recuperada es mayormente indirecta: programas de estiramiento y uso de opioides, dolor de la articulación temporomandibular, síndrome de dolor posterior a cirugía de columna e infiltraciones perioperatorias. El estudio más cercano (2026) compara dexmedetomidina y morfina frente a ropivacaína en infiltración miofascial durante fusión espinal toracolumbar, pero es un ensayo en dolor postoperatorio, con uso local y adyuvante, distinto de la enfermedad predicha.

Por ello, la predicción se apoya sobre todo en el puntaje del modelo y no en evidencia clínica directa.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [41664327](https://pubmed.ncbi.nlm.nih.gov/41664327/) | 2026 | ECA | Asian Spine Journal | Dexmedetomidina y morfina frente a ropivacaína 0.2% en infiltración miofascial en fusión espinal; contexto de dolor postoperatorio, no de síndrome miofascial |
| [35066974](https://pubmed.ncbi.nlm.nih.gov/35066974/) | 2022 | Cohorte retrospectiva | Pain Practice | Programa estructurado de estiramientos y su efecto en el dolor miofascial y el uso de opioides en pacientes con "dolor heredado" |
| [21419546](https://pubmed.ncbi.nlm.nih.gov/21419546/) | 2011 | Revisión | J Oral Maxillofac Surg | Uso de opioides a largo plazo en disfunción de la articulación temporomandibular; no puede respaldarse ni refutarse con la evidencia actual |
| [39793344](https://pubmed.ncbi.nlm.nih.gov/39793344/) | 2025 | Estudio clínico | Eur J Obstet Gynecol Reprod Biol | Bloqueo del nervio pudendo tras inyección de toxina botulínica en dolor pélvico miofascial; la morfina no es el foco |
| [21691691](https://pubmed.ncbi.nlm.nih.gov/21691691/) | 2011 | Estudio descriptivo | Rev Assoc Med Bras | Abordaje terapéutico en 56 pacientes con síndrome de dolor posterior a cirugía de espalda |
| [7478690](https://pubmed.ncbi.nlm.nih.gov/7478690/) | 1995 | Preclínico (rata) | Pain | Dolor visceral por cálculo ureteral y su relación con hiperalgesia muscular lumbar referida |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 218190 | MORFINA CLORHIDRATO AL 3% SOLUCIÓN ORAL | Solución oral | MORFINA |
| 20013906 | MORFINA CLORHIDRATO 10 MG / ML | Solución inyectable | MORFINA |

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: se identificaron 721 interacciones en total. Entre las de nivel mayor figuran fentanilo, dihidrocodeína, codeína, tramadol, butalbital, etanol, alprazolam y dicloralfenazona (depresión aditiva del sistema nervioso central y respiratoria). Entre las de nivel moderado figuran clorfeniramina, acebutolol, nifedipino, hidroclorotiazida, cetirizina y metformina.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Ningún estudio recopilado evalúa la morfina en el síndrome de dolor miofascial, y los opioides no son tratamiento recomendado para esta condición. La predicción se basa solo en el puntaje del modelo (L5).

**Para avanzar se necesita:**
- Estudios clínicos que evalúen directamente la morfina en síndrome de dolor miofascial
- Datos del mecanismo de acción y de advertencias y contraindicaciones del prospecto
- Evaluación del riesgo de dependencia, depresión respiratoria e hiperalgesia inducida por opioides frente a alternativas no opioides

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

