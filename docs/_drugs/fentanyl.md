---
layout: default
title: Fentanyl
parent: Solo Predicción del Modelo (L5)
nav_order: 281
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-25
description: "Fentanyl: nueva indicación predicha, Síndrome nefrogénico de antidiuresis inapropiada (nivel de evidencia L5). Indicación original: No especificada en el registro (el texto aprobado solo indica \"Fent…"
monitor_inn: "fentanyl"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "Tourette syndrome"]
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

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Fentanilo: De Fentanilo (indicación no detallada en el registro) a Síndrome Nefrogénico de Antidiuresis Inapropiada
{: .text-alpha }

## Resumen en Una Frase

Fentanilo es un opioide inyectable cuyos registros sanitarios en Colombia no detallan una indicación específica (solo figura el nombre del principio activo).
El modelo TxGNN predice que podría ser efectivo para el **síndrome nefrogénico de antidiuresis inapropiada**, pero **no existen ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto aprobado solo indica "Fentanyl") |
| Nueva Indicación Predicha | Síndrome nefrogénico de antidiuresis inapropiada |
| Puntaje de Predicción TxGNN | 0.9946 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 7 de 8) |
| Número de Registros Sanitarios | 8 (vigentes: 7) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Fentanyl (traducción no oficial): «Fentanyl Citrate Injection es un agonista opioide cuyas principales acciones de valor terapéutico son la analgesia y la sedación.» Texto original en inglés: "Fentanyl Citrate Injection is an opioid agonist, whose principal actions of therapeutic value are analgesia and sedation." ([DailyMed: fentanyl citrate prescribing information, Phlow Corp.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=58dcd3f7-e3d8-4929-a186-8f680a51ff11), versión del 2026-10-23; consultado el 2026-11-19). Según el conocimiento general, el fentanilo es un agonista del receptor opioide mu, utilizado como analgésico y en anestesia.

Los opioides pueden influir en la liberación de vasopresina y en el equilibrio hídrico a través de vías centrales. Sin embargo, el síndrome nefrogénico de antidiuresis inapropiada es causado por mutaciones con ganancia de función en el receptor V2 de vasopresina (AVPR2), que actúan de forma independiente de la vasopresina.

Por ello, no se establece un vínculo mecanístico sólido: es poco probable que la vía opioide corrija un defecto a nivel del receptor. El puntaje alto del modelo (0.9946) es solo una predicción computacional sin respaldo clínico ni bibliográfico.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 19908145 | FENTANILO SOLUCIÓN INYECTABLE | SOLUCION INYECTABLE | FENTANYL | Vigente |
| 19931880 | FENTANILO SOLUCION INYECTABLE 0.5 MG/ 10 ML | SOLUCION INYECTABLE | FENTANYL | Vigente |
| 20027082 | LANZAPIN® SOLUCIÓN INYECTABLE | SOLUCION INYECTABLE | FENTANYL | Vigente |
| 20030910 | FENTANILO 500 MCG/10 ML | SOLUCION INYECTABLE | FENTANYL | Vigente |
| 20079574 | FENTANILO 0.5/10ML | SOLUCION INYECTABLE | FENTANYL | Vigente |

Se muestran 5 de 8 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

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
La predicción carece de ensayos clínicos y literatura (nivel L5), el vínculo mecanístico es débil (el defecto está en el receptor V2, no en la vía opioide), el medicamento está comercializado en Colombia con 6 registros vigentes y el perfil de seguridad es complejo (327 interacciones, riesgo de depresión respiratoria y dependencia).

**Para avanzar se necesita:**
- Datos del mecanismo de acción desde DrugBank
- Prospecto de INVIMA con advertencias y contraindicaciones
- Evidencia preclínica o de mecanismo que vincule la vía opioide con la función del receptor AVPR2
- Revisión de la factibilidad regulatoria
- Evaluación de la segunda predicción (síndrome de Tourette, puntaje 0.9905, también nivel L5 y Hold) solo si surge evidencia nueva

<!-- review:begin co-lic-20261105-fentanyl-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Revisión de la factibilidad regulatoria, dado que no hay registros vigentes" Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-fentanyl-1 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "dado que no hay registros vigentes" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-12 | Número de registros vigentes: 3 → 6 | Ya no aparece tras una corrección del programa (2026-11-24: el número de registros sanitarios de esta frase lo actualiza ahora un programa según los datos del INVIMA (scripts/rewrite_license_counts.py), por lo que esta corrección puntual ya no se muestra; antes: Corregido) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: fentanyl citrate prescribing information, Phlow Corp.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=58dcd3f7-e3d8-4929-a186-8f680a51ff11) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

