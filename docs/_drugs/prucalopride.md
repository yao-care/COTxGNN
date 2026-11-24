---
layout: default
title: Prucalopride
parent: Solo Predicción del Modelo (L5)
nav_order: 542
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Prucalopride: nueva indicación predicha, Hipoalfalipoproteinemia (nivel de evidencia L5). Indicación original: No especificada en el registro (el texto de indicación solo indica \"P…"
monitor_inn: "prucalopride"
predicted_indications: ["hypoalphalipoproteinemia", "homozygous familial hypercholesterolemia", "duodenal ulcer (disease)", "oral candidiasis", "obsolete familial combined hyperlipidemia", "amyloidosis (disease)", "strongyloidiasis", "HIV infectious disease", "primary amyloidosis", "acquired amyloid peripheral neuropathy"]
---

# Prucalopride
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

## Prucaloprida: De Indicación No Especificada en el Registro a Hipoalfalipoproteinemia
{: .text-alpha }

## Resumen en Una Frase

Prucaloprida es un agonista selectivo del receptor 5-HT4 que actúa sobre la motilidad gastrointestinal y el texto de indicación registrado solo dice "PRUCALOPRIDA".
El modelo TxGNN predice que podría ser efectivo para **hipoalfalipoproteinemia**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción.
Se trata de una predicción puramente computacional (nivel L5).

<!-- review:begin co-lic-20261105-prucalopride-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Prucaloprida es un agonista selectivo del receptor 5-HT4 que actúa sobre la motilidad gastrointestinal; en Colombia su único registro sanitario (Resolor®) figura como cancelado y el texto de indicación registrado solo dice "PRUCALOPRIDA"." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-prucalopride-1 -->

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto de indicación solo indica "PRUCALOPRIDA") |
| Nueva Indicación Predicha | Hipoalfalipoproteinemia |
| Puntaje de Predicción TxGNN | 0.9982 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 2) |
| Número de Registros Sanitarios | 2 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Prucalopride (traducción no oficial): «La prucaloprida, un agonista selectivo del receptor de serotonina de tipo 4 (5-HT 4 ), es un agente procinético gastrointestinal (GI) que estimula el peristaltismo colónico (contracciones propagadas de alta amplitud [HAPC]), lo que aumenta la motilidad intestinal. La prucaloprida careció de efectos mediados por los receptores 5-HT 2A, 5-HT 2B, 5-HT 3, de motilina o CCK-A in vitro a concentraciones que superaban en 150 veces o más la afinidad por el receptor 5-HT 4.» Texto original en inglés: "Prucalopride, a selective serotonin type 4 (5-HT 4 ) receptor agonist, is a gastrointestinal (GI) prokinetic agent that stimulates colonic peristalsis (high-amplitude propagating contractions [HAPCs]), which increases bowel motility. Prucalopride was devoid of effects mediated via 5-HT 2A, 5-HT 2B, 5-HT 3, motilin or CCK-A receptors in vitro at concentrations exceeding 5-HT 4 receptor affinity by 150-fold or greater." ([DailyMed: Motegrity (prucalopride) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bca1e4c6-4b2b-4876-8ab3-654629c4ff1b), versión del 2025-07-17; consultado el 2026-11-19). Según la información conocida, prucaloprida es un agonista selectivo del receptor 5-HT4 que estimula la motilidad del tracto gastrointestinal, y se utiliza en trastornos de la motilidad como el estreñimiento crónico.

Sin embargo, la evaluación no identifica un vínculo mecanístico plausible con la hipoalfalipoproteinemia: no existe una conexión conocida entre la agonía 5-HT4 en el sistema nervioso entérico y el metabolismo de las HDL. El puntaje alto (0.9982) proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica; no está respaldado por ensayos ni literatura.

Por lo tanto, esta predicción debe considerarse con mucha cautela; no hay base mecanística ni clínica que la sustente en este momento.

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
| 20038945 | RESOLOR ® TABLETAS RECUBIERTAS DE 2 MG | TABLETA RECUBIERTA | PRUCALOPRIDA | Vigente |
| 20248125 | PRUCAL®1 | TABLETA RECUBIERTA | PRUCALOPRIDA | Temp. no comerc - Vigente |

Se muestran los 2 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

- **Contraindicaciones sugeridas por el grafo de conocimiento** (relaciones fármaco-enfermedad del grafo, no texto de prospecto): colitis ulcerosa, enfermedad inflamatoria intestinal y perforación intestinal.
- **Interacciones Farmacológicas**: se identificaron 98 interacciones en total. Entre las listadas:
  - *Moderadas*: aclidinio, levonorgestrel, noretisterona, hiosciamina, etinilestradiol, atropina, benzatropina, biperideno, glicopirronio, clidinio (varias son anticolinérgicos, cuyo efecto podría oponerse al efecto procinético).
  - *Menores*: nifedipino, afatinib, alpelisib, amiodarona, cobicistat, captopril, diltiazem, espironolactona, carvedilol, conivaptán.

No se dispone de advertencias ni contraindicaciones del prospecto; consultar el prospecto para información de seguridad adicional.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para hipoalfalipoproteinemia carece de ensayos clínicos, literatura y plausibilidad mecanística. No hay base para avanzar.

<!-- review:begin co-lic-20261105-prucalopride-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción para hipoalfalipoproteinemia carece de ensayos clínicos, literatura y plausibilidad mecanística, y el único registro sanitario en Colombia está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-prucalopride-2 -->

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA para completar el análisis de advertencias y contraindicaciones (brecha bloqueante para el tamizaje de seguridad).
- Completar los datos del mecanismo de acción desde DrugBank.
- Evidencia preclínica que conecte la señalización 5-HT4 con el metabolismo de las HDL.
- Como alternativa, priorizar indicaciones con vínculo indirecto más plausible (por ejemplo, amiloidosis con dismotilidad intestinal, actualmente nivel L4, solo como tratamiento sintomático y sin evidencia directa de eficacia de prucaloprida).
- Aclarar el estado regulatorio.

<!-- review:begin co-lic-20261105-prucalopride-3 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Aclarar el estado regulatorio, dado que el registro de Resolor® está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-prucalopride-3 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "en Colombia su único registro sanitario (Resolor®) figura como cancelado" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "y el único registro sanitario en Colombia está cancelado" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "dado que el registro de Resolor® está cancelado" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Motegrity (prucalopride) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bca1e4c6-4b2b-4876-8ab3-654629c4ff1b) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

