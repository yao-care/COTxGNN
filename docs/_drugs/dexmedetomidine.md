---
layout: default
title: Dexmedetomidine
parent: Solo Predicción del Modelo (L5)
nav_order: 213
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-31
description: "Dexmedetomidine: nueva indicación predicha, Síndrome nefrogénico de antidiuresis inapropiada (nivel de evidencia L5). Indicación original: Dexmedetomidina"
monitor_inn: "dexmedetomidine"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "migraine disorder", "migraine with brainstem aura", "headache disorder", "trigeminal autonomic cephalalgia"]
---

# Dexmedetomidine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Dexmedetomidina: De Dexmedetomidina (indicación no detallada en el registro) a Síndrome Nefrogénico de Antidiuresis Inapropiada
{: .text-alpha }

## Resumen en Una Frase

Dexmedetomidina es un agonista alfa-2 adrenérgico conocido por su uso en sedación en UCI y sedación de procedimientos. El registro sanitario colombiano solo consigna el nombre del principio activo como indicación.
El modelo TxGNN predice que podría ser efectivo para **síndrome nefrogénico de antidiuresis inapropiada**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dexmedetomidina (el registro solo indica el nombre del principio activo, sin texto de indicación clínica) |
| Nueva Indicación Predicha | Síndrome nefrogénico de antidiuresis inapropiada |
| Puntaje de Predicción TxGNN | 0.9960 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 3) |
| Número de Registros Sanitarios | al menos 5 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Dexmedetomidina es un agonista alfa-2 adrenérgico. Puede suprimir la liberación de vasopresina y favorecer la diuresis, y esa es la base teórica de la predicción del modelo. No se dispone de una descripción detallada del mecanismo de acción, más allá de esta caracterización general.

Sin embargo, el síndrome nefrogénico de antidiuresis inapropiada se origina por mutaciones con ganancia de función en el receptor V2 de vasopresina (AVPR2). Ese defecto actúa por debajo del punto de secreción de la hormona. Un efecto simpaticolítico central sobre la liberación de vasopresina no corregiría una alteración a nivel del receptor.

Por lo tanto, el vínculo mecanístico es débil y la predicción probablemente sea un artefacto del modelo TxGNN (aprendizaje profundo). El puntaje del modelo es muy alto (0.996), pero ninguna evidencia clínica o bibliográfica lo respalda.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

Los 5 registros sanitarios encontrados están **cancelados**; no hay registros vigentes.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20211117 | DEXMECORD® 100 MCG/ML POR 4 ML SOLUCIÓN INYECTABLE | Solución inyectable | Dexmedetomidina |
| 20084133 | PRECEDEX® 400MCG/100ML (4MCG/ML) | Solución inyectable | Dexmedetomidina |
| 20260005 | DEXTOMID-VP® 100 MCG/ML SOLUCIÓN INYECTABLE | Solución inyectable | Dexmedetomidina |
| 20227787 | DELTODELT® 0.1 MG/ML SOLUCIÓN INYECTABLE | Solución inyectable | Dexmedetomidina |
| 20233713 | DELTODELT® DEXMEDETOMIDINA 4 MCG/ML. SOLUCIÓN INYECTABLE. | Inyectables | Dexmedetomidina |

---

## Consideraciones de Seguridad

- **Enfermedades con relación de contraindicación en el grafo de conocimiento** (no provienen del texto del prospecto): trastorno hipertensivo, hipertensión, enfermedad renal, piouréter, enfermedad hepática, enfermedad de la vesícula biliar, diabetes mellitus, cetoacidosis diabética, trastorno hipotensivo y bloqueo auriculoventricular.
- **Interacciones farmacológicas**: se identificaron 59 interacciones. Entre las de nivel moderado destacan morfina (incluida la liposomal), opio, dronabinol, nabilona, papaverina, sibutramina, difenoxilato, etanol, nitrito de amilo, diazóxido y fentolamina. Otras, como pantoprazol, lansoprazol, vancomicina, atropina, anfotericina B, cloruro de potasio, famotidina y ácido ursodesoxicólico, tienen nivel de gravedad no definido.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
- El puntaje del modelo es alto, pero no hay ensayos ni publicaciones. El mecanismo de la enfermedad (defecto del receptor V2) no se corrige con la acción central de un agonista alfa-2, por lo que la predicción es poco creíble.
- El medicamento está comercializado en este país y cuenta con 5 registros sanitarios vigentes.

**Para avanzar se necesita:**
- Estudios preclínicos o de mecanismo que demuestren algún efecto sobre la función del receptor V2 o sobre la antidiuresis en este síndrome.
- Revisión del prospecto oficial para completar la información de seguridad.
- Aclarar la situación regulatoria de los registros cancelados antes de cualquier desarrollo local.

**Nota sobre otras predicciones del mismo fármaco:** la indicación *trastorno de cefalea* (puntaje 0.9930) tiene mayor respaldo. Cuenta con un ensayo de Fase 3 completado (NCT04910477, n=90), un ensayo aleatorizado publicado (PMID 36651373) y una revisión sistemática de 2025 (PMID 41120897). Todo ello se limita a la cefalea pospunción dural con dexmedetomidina nebulizada. Esa vía obtuvo nivel L1 y recomendación *Proceed with Guardrails*, con vigilancia de bradicardia e hipotensión y confirmación en ensayos multicéntricos más grandes. La *migraña* (puntaje 0.9949) se mantiene como pregunta de investigación (L4), con un ensayo en reclutamiento (NCT07769255, n=146).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

