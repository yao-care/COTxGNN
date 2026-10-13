---
layout: default
title: Lacosamide
parent: Evidencia Alta (L1-L2)
nav_order: 370
evidence_level: L1
indication_count: 10
---

# Lacosamide
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **10** 
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

# Lacosamida: De Epilepsia (Crisis Focales) a Migraña

**Nota sobre la selección de la indicación:** el modelo TxGNN genera varias predicciones. La de mayor puntaje es el trastorno bipolar maníaco, pero solo cuenta con evidencia de nivel L3 y sin ensayos clínicos. La indicación con la evidencia más sólida es la **migraña**, y es la que se desarrolla en este informe. La indicación original (epilepsia) no figura en el texto del registro sanitario, que solo dice "LACOSAMIDA"; se indica a partir del conocimiento general del fármaco.

## Resumen en Una Frase

Lacosamida es un antiepiléptico de tercera generación, usado originalmente para tratar crisis epilépticas focales.
El modelo TxGNN predice que podría ser efectivo para **migraña** (puntaje 99.87%), con **4 ensayos clínicos** (3 de ellos en Fase 3 o con diseño comparativo activo) y **17 publicaciones** recuperadas, incluido un ensayo aleatorizado doble ciego publicado en 2026.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Lacosamida (el texto del registro no detalla la indicación; fármaco antiepiléptico) |
| Nueva Indicación Predicha | Migraña (*migraine disorder*) |
| Puntaje de Predicción TxGNN | 99.87% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 3 (todos cancelados) |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados del mecanismo de acción en la información compilada. Según la literatura recuperada, lacosamida potencia la inactivación lenta de los canales de sodio dependientes de voltaje y modula la proteína CRMP2, lo que puede estabilizar la hiperexcitabilidad neuronal.

La migraña y la epilepsia comparten la hiperexcitabilidad neuronal como base fisiopatológica. Otros antiepilépticos, como topiramato y valproato, están establecidos para la prevención de la migraña. Además, hay datos preclínicos en ratones que muestran que lacosamida afecta la depresión cortical propagada, un mecanismo clave de la migraña. También se ha postulado que inhibe la liberación del péptido relacionado con el gen de la calcitonina (CGRP) en el sistema trigeminal.

Por todo ello, el mecanismo podría ser aplicable a la migraña, aunque la confirmación depende de los resultados clínicos.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT05851781](https://clinicaltrials.gov/study/NCT05851781) | Fase 3 | Completado | 600 | Lacosamida vs. propranolol: reducción de días de migraña mensuales y proporción con reducción ≥50%. Parece corresponder al ensayo publicado en 2026 |
| [NCT06243692](https://clinicaltrials.gov/study/NCT06243692) | Fase 3 | Desconocido | 600 | Lacosamida vs. topiramato con los mismos criterios de valoración; sin resultados disponibles |
| [NCT05632133](https://clinicaltrials.gov/study/NCT05632133) | Fase 3 | Completado | 200 | Estudio piloto aleatorizado: efecto de lacosamida 50 mg dos veces al día durante 3 meses sobre el CGRP sérico (criterio de valoración de biomarcador) |
| [NCT00440518](https://clinicaltrials.gov/study/NCT00440518) | Fase 2 | Completado | 218 | Ensayo doble ciego controlado con placebo de lacosamida 100 y 300 mg/día en profilaxis de migraña; falta verificar los resultados |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [41863672](https://pubmed.ncbi.nlm.nih.gov/41863672/) | 2026 | ECA | Molecular Neurobiology | Lacosamida vs. propranolol en migraña episódica, doble ciego; evalúa eficacia y seguridad como alternativa en pacientes que no toleran propranolol |
| [38502425](https://pubmed.ncbi.nlm.nih.gov/38502425/) | 2024 | ECA | Acta Neurologica Belgica | Efecto de lacosamida sobre el CGRP sérico en migraña episódica |
| [22779776](https://pubmed.ncbi.nlm.nih.gov/22779776/) | 2013 | Revisión sistemática y metaanálisis | Epilepsia | Perfil de eventos adversos de lacosamida en ensayos aleatorizados |
| [40670944](https://pubmed.ncbi.nlm.nih.gov/40670944/) | 2025 | Preclínico | J Headache Pain | Efecto de lacosamida sobre la depresión cortical propagada en ratones |
| [27917413](https://pubmed.ncbi.nlm.nih.gov/27917413/) | 2016 | Preclínico | Pain Reports | Eficacia de (S)-lacosamida en modelos de dolor cefálico, mediante CRMP2 e inhibición de la liberación de CGRP |
| [22862686](https://pubmed.ncbi.nlm.nih.gov/22862686/) | 2012 | Revisión | Expert Opin Emerg Drugs | Tratamientos emergentes para migraña crónica y refractaria |
| [35696452](https://pubmed.ncbi.nlm.nih.gov/35696452/) | 2022 | Revisión | Brain | Variantes de ganancia de función de SCN1A y migraña hemipléjica familiar tipo 3 (apoyo indirecto) |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20010104 | VIMPAT® 150 MG TABLETAS (cancelado) | Tableta recubierta | LACOSAMIDA |
| 20187322 | LACOLEP 150 (cancelado) | Tableta recubierta | LACOSAMIDA |
| 20093299 | LACOTEM 50 MG COMPRIMIDOS RECUBIERTOS (cancelado) | Tableta recubierta | LACOSAMIDA |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no del prospecto):** el grafo de conocimiento del modelo asocia lacosamida con enfermedades como bloqueo auriculoventricular, síndrome del seno enfermo, fibrilación y aleteo auricular, enfermedad coronaria, isquemia miocárdica, hipotensión ortostática, síndrome de taquicardia postural ortostática, atrofia multisistémica, enfermedad hepática y enfermedad de la vesícula biliar. Esto sugiere precaución en pacientes con trastornos de conducción o enfermedad cardiovascular.
- **Interacciones farmacológicas:** se identificaron 25 interacciones, de las cuales se listan las principales:
  - **Mayores:** dolasetrón, ceritinib, siponimod.
  - **Moderadas:** claritromicina, etanol, cobicistat, cloroquina, hidroxicloroquina, mefloquina, lidocaína, ketoconazol, pasireotida, alectinib, brigatinib, crizotinib, fingolimod, idelalisib, imatinib, ozanimod, sunitinib.
- **Señal de seguridad en la literatura:** un reporte de caso describe neutropenia precipitada por lacosamida en un paciente con trastorno bipolar y epilepsia.
- Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen dos ensayos de Fase 3 completados y un ECA doble ciego publicado en 2026 sobre migraña, además de un ensayo de Fase 2 controlado con placebo. Sin embargo, los ensayos de Fase 3 usan comparadores activos sin brazo placebo, uno tiene estado desconocido y los resultados requieren confirmación independiente.

**Para avanzar se necesita:**
- Revisar el tamaño del efecto y la replicación de los resultados publicados (PMID 41863672) y verificar los resultados del ensayo de Fase 2 NCT00440518.
- Obtener los datos del mecanismo de acción confirmados desde fuentes oficiales.
- Descargar y analizar el prospecto en INVIMA para advertencias y contraindicaciones oficiales (hoy no disponibles).
- Aclarar la situación regulatoria: los 3 registros sanitarios están cancelados, por lo que no hay producto vigente en Colombia.
- Plan de monitoreo cardiaco (conducción y ritmo) y de control hematológico, dadas las señales de seguridad.

**Otras predicciones del modelo (para referencia):**
- **Trastorno bipolar maníaco** (99.96%, L3, Research Question): apoyo limitado a estudios observacionales pequeños y series de casos.
- **Síndrome miofascial** (99.81%, L2, Research Question): un ensayo de Fase 2 controlado con placebo sin resultados disponibles.
- **Síndrome de Tourette, tricotilomanía, SIAD nefrogénico, insomnio, TOC y conjuntivitis papilar:** solo predicción del modelo, sin respaldo clínico (Hold).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

