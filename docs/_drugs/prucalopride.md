---
layout: default
title: Prucalopride
parent: Solo Predicción del Modelo (L5)
nav_order: 542
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
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

> **Corrección de revisión (2026-11-05)**: Texto original: "Prucaloprida es un agonista selectivo del receptor 5-HT4 que actúa sobre la motilidad gastrointestinal; en Colombia su único registro sanitario (Resolor®) figura como cancelado y el texto de indicación registrado solo dice "PRUCALOPRIDA"." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 2 registros sanitarios (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

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

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, prucaloprida es un agonista selectivo del receptor 5-HT4 que estimula la motilidad del tracto gastrointestinal, y se utiliza en trastornos de la motilidad como el estreñimiento crónico.

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

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20038945 | RESOLOR® tabletas recubiertas de 2 mg | Tableta recubierta | PRUCALOPRIDA |

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

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción para hipoalfalipoproteinemia carece de ensayos clínicos, literatura y plausibilidad mecanística, y el único registro sanitario en Colombia está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 2 registros sanitarios (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-prucalopride-2 -->

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA para completar el análisis de advertencias y contraindicaciones (brecha bloqueante para el tamizaje de seguridad).
- Completar los datos del mecanismo de acción desde DrugBank.
- Evidencia preclínica que conecte la señalización 5-HT4 con el metabolismo de las HDL.
- Como alternativa, priorizar indicaciones con vínculo indirecto más plausible (por ejemplo, amiloidosis con dismotilidad intestinal, actualmente nivel L4, solo como tratamiento sintomático y sin evidencia directa de eficacia de prucaloprida).
- Aclarar el estado regulatorio.

<!-- review:begin co-lic-20261105-prucalopride-3 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Aclarar el estado regulatorio, dado que el registro de Resolor® está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 2 registros sanitarios (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-prucalopride-3 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "en Colombia su único registro sanitario (Resolor®) figura como cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "y el único registro sanitario en Colombia está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "dado que el registro de Resolor® está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

