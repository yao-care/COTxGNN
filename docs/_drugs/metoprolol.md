---
layout: default
title: Metoprolol
parent: Solo Predicción del Modelo (L5)
nav_order: 439
evidence_level: L5
indication_count: 6
monitor_inn: "metoprolol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "chronic pulmonary heart disease", "trichotillomania"]
last_modified_at: 2026-10-31
description: "Metoprolol: nueva indicación predicha, Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) (nivel de evidencia L5). Indicación original: METOPROLOL"
---

# Metoprolol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Metoprolol: Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease)
{: .text-alpha }

## Resumen en Una Frase

Metoprolol es un betabloqueante cardioselectivo (beta-1) con cuatro registros sanitarios vigentes en Colombia; el texto del registro solo menciona el nombre del principio activo, sin detallar una indicación.
El modelo TxGNN predice que podría ser efectivo para **enfermedad renal hipertensiva maligna**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección, por lo que se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | METOPROLOL |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna (malignant hypertensive renal disease) |
| Puntaje de Predicción TxGNN | 0.9991 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 4) |
| Número de Registros Sanitarios | al menos 4 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, metoprolol es un bloqueador selectivo de receptores beta-1 que reduce la presión arterial, la frecuencia cardíaca y la liberación de renina.

Mecanísticamente, la reducción de renina y de la presión arterial podría ser relevante en hipertensión grave con afectación renal. Sin embargo, esto es una hipótesis: no existen ensayos ni literatura sobre esta indicación específica, y los betabloqueantes no son tratamiento de primera línea en la nefropatía hipertensiva.

Por ello esta predicción debe tratarse como una hipótesis de investigación.

Otras indicaciones predichas, todas sin respaldo clínico directo suficiente:
- **Hipertensión pulmonar de mecanismo multifactorial incierto** (0.9991): el bloqueo beta generalmente no es beneficioso en hipertensión arterial pulmonar y podría empeorar la función del ventrículo derecho.
- **Hipertensión pulmonar por enfermedad pulmonar o hipoxia** (0.9991): la literatura recuperada trata temas ajenos (intoxicación por betabloqueantes, taquicardia auricular multifocal, modelos animales); ninguna estudia esta indicación.
- **Síndrome de Braddock** (0.9989): enfermedad muy rara, sin datos.
- **Cor pulmonale crónico** (0.9940): hay ensayos y estudios sobre metoprolol en pacientes con EPOC e insuficiencia cardíaca, pero abordan seguridad y tolerabilidad, no tratamiento de esta enfermedad.
- **Tricotilomanía** (0.9905): sin datos ni fundamento mecanístico claro.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para la indicación principal predicha (enfermedad renal hipertensiva maligna).

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal predicha.

## Información de Mercado en Colombia

La lista de registros puede ser parcial (se muestran al menos 4).

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19961415 | Metoprolol Tartrato 50 mg Tabletas | Tableta | Metoprolol |
| 20278182 | Metoprolol Tartrato 5 mg/5 ml Solución Inyectable | Solución inyectable | Metoprolol |
| 19992946 | Metoprolol Tabletas Recubiertas 50 mg | Tableta con cubierta entérica con película | Metoprolol |
| 19927923 | Betaloc ZOK 25 mg | Tableta de liberación prolongada | Metoprolol |

## Consideraciones de Seguridad

- **Relaciones de contraindicación registradas en el grafo de conocimiento** (no provienen del texto del prospecto): trastornos de ansiedad, trastorno neurótico, distimia, pancreatitis, enfermedad hepática, enfermedad de la vesícula biliar, lupus eritematoso sistémico, psoriasis, diabetes mellitus, cetoacidosis diabética, hipotensión, gota, miastenia gravis, feocromocitoma, encefalopatía hepática, hiperparatiroidismo, hipercalcemia, anuria, entre otras.
- **Interacciones farmacológicas**: se identificaron 338 interacciones registradas. Entre las de nivel moderado figuran epinefrina, corticosteroides (hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona), atropina, hiosciamina, glicopirronio, bupropión, morfina, cimetidina, canagliflozina, dapagliflozina, clorpropamida, lorcaserina y sales de calcio. Las de nivel leve incluyen ácido acetilsalicílico y óxido de magnesio.
- **Señales de la literatura**: en ratas, metoprolol redujo la tensión de oxígeno tisular cerebral tras hemodilución aguda (PMID 19809291), lo que constituye una alerta leve relacionada con hipoxia. En EPOC, el ensayo BLOCK-COPD (NCT02587351) fue terminado y la literatura citada indica un aumento de exacerbaciones que requirieron hospitalización con metoprolol.

No se dispone del texto de advertencias y contraindicaciones del prospecto; consultar el prospecto para información de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para enfermedad renal hipertensiva maligna no tiene ensayos clínicos ni literatura que la respalden (nivel L5), y los betabloqueantes no son de primera línea en esta condición. Las demás indicaciones predichas tampoco cuentan con evidencia directa que respalde una decisión favorable.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA para definir las indicaciones aprobadas, advertencias y contraindicaciones.
- Completar los datos del mecanismo de acción.
- Realizar una revisión sistemática de la literatura sobre betabloqueantes en nefropatía hipertensiva maligna.
- Si se prioriza una línea alternativa, evaluar cor pulmonale crónico como pregunta de investigación sobre seguridad y comanejo en EPOC con enfermedad cardiovascular (por ejemplo, NCT06825728), no como afirmación de eficacia.
- Evaluar el perfil de seguridad en poblaciones con contraindicaciones registradas (asma/EPOC, diabetes, hipotensión, feocromocitoma).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

