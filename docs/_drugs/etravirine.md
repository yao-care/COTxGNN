---
layout: default
title: Etravirine
parent: Solo Predicción del Modelo (L5)
nav_order: 272
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Etravirine: nueva indicación predicha, Síndrome de inmunodeficiencia adquirida felina (nivel de evidencia L5). Indicación original: Etravirina"
monitor_inn: "Etravirine"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "fibroma of prostate", "Brenner tumor", "benign reproductive system neoplasm", "benign prostate phyllodes tumor", "obsolete familial combined hyperlipidemia"]
---

# Etravirine
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

# Etravirina: De Infección por VIH-1 a Síndrome de Inmunodeficiencia Adquirida Felina

## Resumen en Una Frase

Etravirina es un inhibidor no nucleosídico de la transcriptasa inversa (ITINN) del VIH-1, registrado en Colombia bajo el nombre INTELENCE® tabletas 200 mg.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de inmunodeficiencia adquirida felina**, con una puntuación muy alta (99.98%), pero **sin ensayos clínicos ni publicaciones** que respalden esta predicción en los datos compilados para este informe.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Etravirina (el registro sanitario no detalla el texto de la indicación; el uso conocido es VIH-1 en pacientes con experiencia previa al tratamiento) |
| Nueva Indicación Predicha | Síndrome de inmunodeficiencia adquirida felina |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registro vigente) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Etravirina es un inhibidor no nucleosídico de la transcriptasa inversa del VIH-1. Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción, por lo que el análisis se basa en la clase farmacológica conocida.

El virus de la inmunodeficiencia felina (FIV) es un lentivirus emparentado con el VIH, y esa cercanía explica en parte la puntuación alta del modelo. Sin embargo, los ITINN generalmente tienen poca actividad frente a lentivirus distintos del VIH-1, debido a diferencias en el bolsillo de unión de la transcriptasa inversa. La puntuación probablemente refleja proximidad en la red de conocimiento con nodos relacionados con el VIH, y no una actividad validada.

Por lo tanto, la predicción es mecanísticamente débil. No se dispone de ensayos ni literatura que la sustenten.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal (síndrome de inmunodeficiencia adquirida felina).

Como referencia, entre las demás indicaciones predichas, la infección por el virus de inmunodeficiencia simia (rank 2) cuenta con una publicación indirecta:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [26529558](https://pubmed.ncbi.nlm.nih.gov/26529558/) | 2015 | Preclínico/in vitro | Molecular Pharmaceutics | Combinaciones de antirretrovirales en nanopartículas con inhibición sinérgica de la transmisión del VIH; no hay datos específicos de etravirina en SIV |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20065823 (cancelado) | INTELENCE® TABLETAS 200MG | Tableta | ETRAVIRINA |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: hepatitis C crónica, infección por virus de hepatitis C, hepatitis B crónica, enfermedad del sistema nervioso periférico y neuropatía periférica.
- **Interacciones farmacológicas**: se identificaron 100 interacciones en total; las principales mostradas son de nivel moderado e incluyen:
  - Inhibidores de la bomba de protones y antiácidos: omeprazol, rabeprazol, cimetidina (ranitidina es de nivel menor).
  - Corticoides: hidrocortisona, dexametasona, betametasona, triamcinolona.
  - Antidiabéticos: pioglitazona, glimepirida, clorpropamida, saxagliptina, linagliptina.
  - Otros: claritromicina, metronidazol, aprepitant, dronabinol, eliglustat, naldemedina, naloxegol.

No se dispone de advertencias ni contraindicaciones del prospecto; consultar el prospecto para esa información.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura directa, y el mecanismo es poco plausible porque los ITINN suelen ser poco activos contra lentivirus distintos del VIH-1. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Datos de actividad in vitro de etravirina frente a FIV, para confirmar o descartar el mecanismo.
- Descripción detallada del mecanismo de acción (por ejemplo, desde DrugBank).
- Advertencias y contraindicaciones del prospecto en INVIMA.
- Confirmar si se justifica un enfoque veterinario, ya que la indicación predicha corresponde a una enfermedad felina.
- Si el interés es humano, priorizar las indicaciones del espectro VIH-1 (complejo relacionado con el SIDA y VIH congénito, ambas con evidencia observacional L3). Estas se superponen con el uso original, por lo que no son reposicionamiento propiamente dicho, y la disponibilidad comercial es una limitación práctica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

