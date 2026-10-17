---
layout: default
title: Dactinomycin
parent: Solo Predicción del Modelo (L5)
nav_order: 191
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Dactinomycin: nueva indicación predicha, Esclerosis múltiple remitente-recurrente (nivel de evidencia L5). Indicación original: No especificada en el registro (el texto de indicación aprobada solo…"
monitor_inn: "dactinomycin"
predicted_indications: ["relapsing-remitting multiple sclerosis", "liver sarcoma", "upper aerodigestive tract neoplasm", "head and neck cancer"]
---

# Dactinomycin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

# Dactinomicina: De Indicación Original (sin texto de indicación detallado) a Esclerosis Múltiple Remitente-Recurrente

## Resumen en Una Frase

La dactinomicina (actinomicina D) es un antineoplásico citotóxico que se utiliza en esquemas de quimioterapia para sarcomas pediátricos, y en Colombia su registro sanitario solo indica el nombre del fármaco, sin detalle de indicación.
El modelo TxGNN predice que podría ser efectiva para **esclerosis múltiple remitente-recurrente**, con **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección específica.
Es una predicción basada únicamente en el modelo, y la evidencia disponible se concentra en otras indicaciones oncológicas (rabdomiosarcoma y sarcomas relacionados).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto de indicación aprobada solo dice "DACTINOMICINA") |
| Nueva Indicación Predicha | Esclerosis múltiple remitente-recurrente |
| Puntaje de Predicción TxGNN | 99.58% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la dactinomicina es un antibiótico antitumoral que se intercala en el ADN e inhibe la transcripción, y forma parte de los esquemas VAC/VA (vincristina, actinomicina, ciclofosfamida) para rabdomiosarcoma y otros sarcomas pediátricos.

No se identificó un vínculo mecanístico respaldado por los datos entre este fármaco y la esclerosis múltiple. El puntaje de TxGNN (99.58%) es una predicción del modelo y no equivale a evidencia clínica. Además, la toxicidad sistémica de un citotóxico (mielosupresión, hepatotoxicidad) hace poco plausible su uso crónico en una enfermedad autoinmune sin evidencia sólida que lo respalde.

**Otras predicciones del modelo con mayor respaldo biológico y bibliográfico.** El modelo también predice indicaciones dentro del espectro de los sarcomas, donde sí existe fundamento clínico:

| Indicación predicha | Puntaje TxGNN | Nivel de evidencia | Observación |
|------|------|------|------|
| Rabdomiosarcoma embrionario parameníngeo | 99.48% | L3 | 1 publicación (COG D9803, VAC vs. VAC/VTC) |
| Sarcoma de hígado | 99.42% | L3 | 10 publicaciones, varias solo tangenciales; incluye alertas de hepatopatía |
| Neoplasia del tracto aerodigestivo superior | 99.16% | L3 | 20 publicaciones, la mayoría sobre rabdomiosarcoma de cabeza y cuello |
| Cáncer de cabeza y cuello | 99.16% | L3 | 20 publicaciones, limitadas a rabdomiosarcoma pediátrico |
| Rabdomiosarcoma embrionario de próstata | 99.46% | L4 | Reporte de caso y estudios indirectos |

Estas predicciones reflejan en gran parte el uso ya establecido de la dactinomicina en rabdomiosarcoma, más que un reposicionamiento genuino.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esclerosis múltiple remitente-recurrente.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esclerosis múltiple remitente-recurrente.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 19902428 | DACTINOMICINA 0.5MG INYECCIÓN | Polvo liofilizado para reconstituir a solución inyectable | DACTINOMICINA | Cancelado |

El fabricante registrado fue KOREA UNITED PHARM. INC. No hay registros vigentes en Colombia.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (antibiótico antitumoral; intercalante de ADN e inhibidor de la transcripción) |
| Riesgo de Mielosupresión | Alto (el grafo de conocimiento asocia el fármaco con neutropenia, trombocitopenia, leucopenia, agranulocitosis y anemia aplásica) |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Ítems de Monitoreo | Hemograma con diferencial, función hepática (hepatopatía descrita con esquemas VAC) y función renal |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

- **Enfermedades asociadas como contraindicación en el grafo de conocimiento** (relaciones fármaco-enfermedad del modelo, no texto de prospecto): enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia, neutropenia, agranulocitosis, anemia (incluida la macrocítica y la aplásica idiopática), leucopenia, infección por varicela zóster y herpes zóster, trombosis de la vena hepática y síndrome de Budd-Chiari.
- **Interacciones farmacológicas**: se identificaron 164 interacciones. Entre las de mayor relevancia:
  - **Mayores**: deferiprona, samario (153Sm) lexidronam.
  - **Moderadas**: palifermina, estroncio-89 cloruro, fostamatinib, mercaptopurina, roflumilast, cloranfenicol.
  - **Menores**: levofloxacino.
  - Otras con nivel no clasificado: anfotericina B, calcitriol, ranitidina, granisetrón, ondansetrón, metoclopramida, dexametasona, leucovorina, ácido fólico, gadodiamida y gadoversetamida.
- **Hepatopatía**: la literatura recuperada describe hepatopatía inducida por esquemas con vincristina, dactinomicina y ciclofosfamida, con la edad como factor de riesgo (PMID 15143082), y datos de toxicidad de dactinomicina y vincristina en cáncer infantil (PMID 21671362).

No se obtuvieron advertencias ni contraindicaciones del prospecto; se debe consultar el prospecto para información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para esclerosis múltiple remitente-recurrente se apoya solo en el puntaje del modelo (nivel L5), sin ensayos ni publicaciones, y el perfil citotóxico del fármaco (mielosupresión, hepatotoxicidad) hace difícil justificar su uso crónico en una enfermedad autoinmune. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Datos del mecanismo de acción que sustenten un vínculo con la fisiopatología de la esclerosis múltiple.
- Estudios preclínicos que muestren un efecto inmunomodulador con un margen de seguridad aceptable.
- Obtener y analizar el prospecto (advertencias y contraindicaciones) para completar el tamizaje de seguridad.
- Si el interés es oncológico, priorizar las indicaciones de rabdomiosarcoma y sarcomas pediátricos, donde ya existe uso clínico establecido.
- Aclarar la situación regulatoria en Colombia, dado que no hay registros vigentes.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

