---
layout: default
title: Fluvoxamine
parent: Solo Predicción del Modelo (L5)
nav_order: 301
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Fluvoxamine: nueva indicación predicha, Trastorno de personalidad paranoide (nivel de evidencia L5). Indicación original: Fluvoxamina"
monitor_inn: "fluvoxamine"
predicted_indications: ["paranoid personality disorder", "schizotypal personality disorder", "histrionic personality disorder (disease)", "schizoid personality disorder", "benign paroxysmal torticollis of infancy", "dependent personality disorder", "narcissistic personality disorder", "endogenous depression"]
---

# Fluvoxamine
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

# Fluvoxamina: De Fluvoxamina (indicación no especificada en el registro) a Trastorno de Personalidad Paranoide

## Resumen en Una Frase

Fluvoxamina es un inhibidor selectivo de la recaptación de serotonina (ISRS), comercializado en Colombia en tabletas recubiertas de 100 mg; el registro sanitario no detalla el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **trastorno de personalidad paranoide** (puntaje 99.99%), pero esta predicción se basa solo en el modelo: **0 ensayos clínicos** y **2 publicaciones** indirectas, ninguna de las cuales evalúa fluvoxamina para esta condición.
Dentro de las demás predicciones del análisis, las mejor respaldadas son **trastornos de ansiedad**, **agorafobia** y **depresión endógena**.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Fluvoxamina (el registro sanitario solo repite el nombre del principio activo, sin texto de indicación) |
| Nueva Indicación Predicha | Trastorno de personalidad paranoide |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, fluvoxamina es un ISRS y agonista del receptor sigma-1; su eficacia en trastornos de ansiedad, trastorno obsesivo-compulsivo (TOC) y depresión está documentada en la literatura.

Para el trastorno de personalidad paranoide, **no hay un vínculo mecanístico respaldado por los datos**. El puntaje tan alto del modelo es una predicción basada en el grafo de conocimiento. Las dos publicaciones asociadas son indirectas: un estudio de rasgos de personalidad en pacientes con trastorno dismórfico corporal (donde 26 sujetos participaron en un estudio de tratamiento con fluvoxamina) y una revisión sobre trastornos mentales inducidos por interferón alfa. Ninguna evalúa fluvoxamina como tratamiento de esta condición.

Cabe señalar que el mismo puntaje (99.99%) se asignó a otros trastornos de personalidad (esquizotípico, histriónico, esquizoide), lo que sugiere un patrón del modelo más que una señal específica. Entre las predicciones analizadas, las más plausibles son las de espectro ansioso y depresivo, que corresponden en gran medida a usos ya establecidos de la clase ISRS (ver sección de Conclusión).

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para trastorno de personalidad paranoide.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10929788](https://pubmed.ncbi.nlm.nih.gov/10929788/) | 2000 | Cohorte | Comprehensive Psychiatry | Evaluó trastornos y rasgos de personalidad en 148 pacientes con trastorno dismórfico corporal, 26 de ellos en un estudio de tratamiento con fluvoxamina. No evalúa eficacia en trastorno paranoide. |
| [11686052](https://pubmed.ncbi.nlm.nih.gov/11686052/) | 2001 | Revisión | L'Encéphale | Revisión de complicaciones psiquiátricas (incluidos trastornos de personalidad) por interferón alfa. No trata fluvoxamina. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20202309 | ANSIVOX® 100 MG TABLETAS RECUBIERTAS (estado: cancelado) | Tableta recubierta | Fluvoxamina |
| 59491 | LUVOX 100 MG TABLETAS RECUBIERTAS (estado: cancelado) | Tableta recubierta | Fluvoxamina |

Ambos registros figuran como cancelados, por lo que no hay actualmente un producto vigente con registro sanitario en los datos compilados.

---

## Consideraciones de Seguridad

- **Contraindicaciones y enfermedades de riesgo (grafo de conocimiento, no texto del prospecto)**: epilepsia, trastorno bipolar, trastorno afectivo mayor, enfermedad hepática, enfermedad de la vesícula biliar, trastornos de la coagulación, síndrome neuroléptico maligno, síndrome de secreción inadecuada de ADH, síndrome nefrogénico de antidiuresis inapropiada y síndrome serotoninérgico.
- **Interacciones farmacológicas**: se registran 283 interacciones. Entre las de nivel **mayor** figuran alosetrón, dietilpropión, dolasetrón y bupropión. Entre las de nivel **moderado** figuran rabeprazol, hidrocortisona, aprepitant, ácido acetilsalicílico, claritromicina, morfina, pioglitazona y varios corticoides (betametasona, budesonida, triamcinolona, dexametasona).
- La literatura del análisis también señala interacciones relevantes (por ejemplo, con metadona y con fenotiazinas, con riesgo de convulsiones) y la aplicabilidad de guías farmacogenéticas CPIC. Fluvoxamina es un inhibidor potente de CYP1A2 y CYP2C19.

No se dispone de las advertencias y contraindicaciones del prospecto; consultar el prospecto para información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para trastorno de personalidad paranoide solo existe una predicción del modelo (nivel L5), sin ensayos clínicos ni literatura que respalde el uso de fluvoxamina, y los registros sanitarios en Colombia están cancelados.

**Otras predicciones del análisis (referencia):**
- **Trastornos de ansiedad** (L1, Proceed with Guardrails): fase 3 completados en TOC pediátrico (NCT01933919) y ansiedad pediátrica (NCT00000389), más metaanálisis en red. Es en gran parte un uso establecido de la clase, con poca novedad como reposicionamiento.
- **Agorafobia / trastorno de pánico** (L1, Proceed with Guardrails): ECA controlados con placebo y metaanálisis en red de 2023; sin ensayos registrados para esta indicación.
- **Depresión endógena** (L2, Proceed with Guardrails): un único ensayo de fase 2 (NCT04160377) con estado desconocido; el respaldo es principalmente de clase.
- **Trastornos de personalidad esquizotípico, esquizoide, dependiente y narcisista, tortícolis paroxística benigna de la infancia e histriónico**: evidencia nula o indirecta (L4–L5, Hold).

**Para avanzar se necesita:**
- Estudios que evalúen directamente fluvoxamina en trastorno de personalidad paranoide (o priorizar las indicaciones de ansiedad y depresión, mejor respaldadas)
- Datos del mecanismo de acción y de advertencias/contraindicaciones del prospecto de INVIMA
- Verificar la disponibilidad real del producto en Colombia, dado que ambos registros están cancelados
- Plan de manejo de interacciones (CYP1A2/CYP2C19) y de farmacogenética según guías CPIC
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

