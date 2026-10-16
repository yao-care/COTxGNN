---
layout: default
title: Fentanyl
parent: Solo Predicción del Modelo (L5)
nav_order: 281
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Fentanyl: nueva indicación predicha, Síndrome nefrogénico de antidiuresis inapropiada (nivel de evidencia L5). Indicación original: No especificada en el registro (el texto aprobado solo indica \"Fent…"
---

# Fentanyl
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Fentanilo: De Fentanilo (indicación no detallada en el registro) a Síndrome Nefrogénico de Antidiuresis Inapropiada

## Resumen en Una Frase

Fentanilo es un opioide inyectable cuyos registros sanitarios en Colombia no detallan una indicación específica (solo figura el nombre del principio activo).
El modelo TxGNN predice que podría ser efectivo para el **síndrome nefrogénico de antidiuresis inapropiada**, pero **no existen ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto aprobado solo indica "Fentanyl") |
| Nueva Indicación Predicha | Síndrome nefrogénico de antidiuresis inapropiada |
| Puntaje de Predicción TxGNN | 99.46% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 3 (0 vigentes, 3 cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según el conocimiento general, el fentanilo es un agonista del receptor opioide mu, utilizado como analgésico y en anestesia.

Los opioides pueden influir en la liberación de vasopresina y en el equilibrio hídrico a través de vías centrales. Sin embargo, el síndrome nefrogénico de antidiuresis inapropiada es causado por mutaciones con ganancia de función en el receptor V2 de vasopresina (AVPR2), que actúan de forma independiente de la vasopresina.

Por ello, no se establece un vínculo mecanístico sólido: es poco probable que la vía opioide corrija un defecto a nivel del receptor. El puntaje alto del modelo (0.995) es solo una predicción computacional sin respaldo clínico ni bibliográfico.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20216065 | Fentanilo 0.1 mg/2 mL solución inyectable | Solución inyectable | FENTANYL | Cancelado |
| 19908145 | Fentanilo solución inyectable | Solución inyectable | FENTANYL | Cancelado |
| 20027082 | Lanzapin® solución inyectable | Solución inyectable | FENTANYL | Cancelado |

---

## Consideraciones de Seguridad

- **Contraindicaciones en el grafo de conocimiento (PrimeKG, no provienen del prospecto)**: hipertensión, hipotensión, hipotensión ortostática, síndrome de taquicardia postural ortostática, atrofia multisistémica, síndrome de QT largo (incluida la forma familiar), torsades de pointes, insuficiencia y enfermedad hepática, enfermedad renal, pancreatitis, enfermedad de la vesícula biliar, enfermedad inflamatoria intestinal, EPOC, asma (intrínseca y alérgica), trastornos de ansiedad y neuróticos, trastorno distímico, enfermedades de los ganglios basales, distonía focal de la mano, blefaroespasmo, deficiencia de potasio, hiperplasia prostática benigna, piouréter y abuso/dependencia de sustancias.
- **Interacciones farmacológicas**: se identificaron **327 interacciones** conocidas. Entre las de nivel **mayor** figuran alvimopán, aprepitant, bupropión, claritromicina, clotrimazol, dexametasona, dexfenfluramina, dolasetrón, fenfluramina, granisetrón y lorcaserina. Entre las de nivel **moderado**: atropina, cimetidina, clidinio, diciclomina, dronabinol, eluxadolina, fenilbutirato de glicerol, glicopirronio e hiosciamina.
- **Riesgos generales del fármaco**: depresión respiratoria, dependencia y abuso.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción carece de ensayos clínicos y literatura (nivel L5), el vínculo mecanístico es débil (el defecto está en el receptor V2, no en la vía opioide), todos los registros en Colombia están cancelados y el perfil de seguridad es complejo (327 interacciones, riesgo de depresión respiratoria y dependencia).

**Para avanzar se necesita:**
- Datos del mecanismo de acción desde DrugBank
- Prospecto de INVIMA con advertencias y contraindicaciones
- Evidencia preclínica o de mecanismo que vincule la vía opioide con la función del receptor AVPR2
- Revisión de la factibilidad regulatoria, dado que no hay registros vigentes
- Evaluación de la segunda predicción (síndrome de Tourette, puntaje 99.05%, también nivel L5 y Hold) solo si surge evidencia nueva
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

