---
layout: default
title: Prucalopride
parent: Solo Predicción del Modelo (L5)
nav_order: 542
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-31
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

Prucaloprida es un agonista selectivo del receptor 5-HT4 que actúa sobre la motilidad gastrointestinal; en Colombia su único registro sanitario (Resolor®) figura como cancelado y el texto de indicación registrado solo dice "PRUCALOPRIDA".
El modelo TxGNN predice que podría ser efectivo para **hipoalfalipoproteinemia**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción.
Se trata de una predicción puramente computacional (nivel L5).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto de indicación solo indica "PRUCALOPRIDA") |
| Nueva Indicación Predicha | Hipoalfalipoproteinemia |
| Puntaje de Predicción TxGNN | 0.9982 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 1) |
| Número de Registros Sanitarios | al menos 1 |
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
| 20038945 (cancelado) | RESOLOR® tabletas recubiertas de 2 mg | Tableta recubierta | PRUCALOPRIDA |

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
La predicción para hipoalfalipoproteinemia carece de ensayos clínicos, literatura y plausibilidad mecanística, y el único registro sanitario en Colombia está cancelado. No hay base para avanzar.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA para completar el análisis de advertencias y contraindicaciones (brecha bloqueante para el tamizaje de seguridad).
- Completar los datos del mecanismo de acción desde DrugBank.
- Evidencia preclínica que conecte la señalización 5-HT4 con el metabolismo de las HDL.
- Como alternativa, priorizar indicaciones con vínculo indirecto más plausible (por ejemplo, amiloidosis con dismotilidad intestinal, actualmente nivel L4, solo como tratamiento sintomático y sin evidencia directa de eficacia de prucaloprida).
- Aclarar el estado regulatorio, dado que el registro de Resolor® está cancelado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

