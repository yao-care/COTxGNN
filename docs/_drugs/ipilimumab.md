---
layout: default
title: Ipilimumab
parent: Solo Predicción del Modelo (L5)
nav_order: 229
evidence_level: L5
indication_count: 2
---

# Ipilimumab
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

# Ipilimumab: De Indicación Original No Especificada en el Registro a Coroideremia

## Resumen en Una Frase

Ipilimumab es un anticuerpo monoclonal que bloquea CTLA-4 y se comercializa en Colombia como YERVOY®. El registro sanitario disponible no detalla su indicación original.
El modelo TxGNN predice que podría ser efectivo para la **coroideremia** (una degeneración hereditaria de la retina), pero hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro solo dice «IPILIMUMAB») |
| Nueva Indicación Predicha | Coroideremia |
| Puntaje de Predicción TxGNN | 99.06% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 6 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base consultada. Por la información conocida, ipilimumab bloquea CTLA-4, un freno de los linfocitos T, y así potencia la respuesta inmunitaria contra los tumores.

La coroideremia es una degeneración retiniana hereditaria ligada al cromosoma X, causada por la pérdida de función del gen CHM (REP1). No es una enfermedad tumoral ni inmunomediada, así que **no se identifica un vínculo mecanístico plausible** con el bloqueo de CTLA-4.

El puntaje alto (0.99) no cuenta con ensayos ni literatura de apoyo, y probablemente es un artefacto del grafo de conocimiento. Además, el bloqueo inmunitario sistémico puede causar eventos adversos oculares inmunomediados (por ejemplo, uveítis), lo que preocuparía en una retina que ya se está degenerando.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para coroideremia.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para coroideremia.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20031989 | YERVOY® 5 MG/ML solución inyectable para infusión intravenosa (Bristol Myers Squibb de Colombia S.A.) | Solución inyectable | Solo figura «IPILIMUMAB» |

Nota: el sistema devolvió cinco entradas idénticas bajo este mismo número de registro, y se consolidaron en una sola fila.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Inmunoterapia (anticuerpo monoclonal anti-CTLA-4) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar el prospecto (como mínimo, hemograma, función hepática y renal) |
| Protección en Manejo | Consultar el prospecto y las normas institucionales de manejo de antineoplásicos |

## Consideraciones de Seguridad

- **Riesgo específico para esta predicción**: el bloqueo inmunitario sistémico puede causar eventos adversos oculares inmunomediados, como uveítis. Esto preocupa en una retina ya degenerada.

Para el resto de la información de seguridad, consultar el prospecto.

## Hallazgo Adicional: Segunda Predicción, Melanoma No Cutáneo

La segunda predicción de TxGNN es el **melanoma no cutáneo** (puntaje 99.02%, nivel de evidencia **L3**). Es la única con evidencia real, por lo que merece atención propia. Se resume aquí porque el resto del informe sigue la primera predicción.

**Fundamento:** el bloqueo de CTLA-4 está validado en melanoma cutáneo. Los melanomas uveal y mucoso tienen menor carga mutacional y un microambiente inmunitario distinto, por lo que las respuestas suelen ser menores. El vínculo es plausible, pero la eficacia por subtipo no está demostrada.

**Ensayos clínicos relevantes (de los 47 registrados; se listan los más pertinentes al subtipo):**

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02626962](https://clinicaltrials.gov/study/NCT02626962) | Fase 2 | Completado | 52 | Nivolumab + ipilimumab en melanoma uveal metastásico sin tratamiento previo (un solo brazo) |
| [NCT01730157](https://clinicaltrials.gov/study/NCT01730157) | Fase 1 temprana | Terminado | 6 | Radioembolización hepática seguida de ipilimumab en melanoma uveal con metástasis hepáticas |
| [NCT03220009](https://clinicaltrials.gov/study/NCT03220009) | Fase 2 | Retirado | 0 | Nivolumab adyuvante tras ipilimumab + nivolumab neoadyuvante en melanoma mucoso de alto riesgo; nunca inscribió pacientes |
| [NCT02939300](https://clinicaltrials.gov/study/NCT02939300) | Fase 2 | Completado | 18 | Ipilimumab + nivolumab en metástasis leptomeníngeas; el tipo de melanoma no está especificado |
| [NCT02224781](https://clinicaltrials.gov/study/NCT02224781) | Fase 3 | Activo, sin reclutar | 267 | DREAMseq: secuencia de ipilimumab/nivolumab frente a dabrafenib/trametinib en melanoma cutáneo BRAF V600; apoya el uso en melanoma solo de forma indirecta |

**Literatura:**

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [24999899](https://pubmed.ncbi.nlm.nih.gov/24999899/) | 2014 | Cohorte | Med J Aust | Evalúa eficacia y tolerabilidad de ipilimumab en melanoma cutáneo, uveal y mucoso previamente tratado, y su asociación con el subtipo |
| [28183255](https://pubmed.ncbi.nlm.nih.gov/28183255/) | 2018 | Revisión | Curr Cancer Drug Targets | Revisión sistemática del tratamiento adyuvante del melanoma; señala que solo cerca del 5% son melanomas no cutáneos |
| [40236344](https://pubmed.ncbi.nlm.nih.gov/40236344/) | 2025 | Reporte de caso | Cureus | Metástasis de melanoma en colon transverso; menciona el riesgo de perforación gastrointestinal con inmunoterapia |

El soporte específico por subtipo se limita a datos retrospectivos u observacionales y a ensayos pequeños. La evidencia de Fase 3 es para melanoma cutáneo.

## Conclusión y Próximos Pasos

**Decisión: Hold** (para coroideremia)

**Justificación:**
No hay mecanismo plausible, ni ensayos, ni literatura que respalden ipilimumab en coroideremia. El puntaje de 0.99 probablemente es un artefacto del modelo, y el riesgo de toxicidad ocular inmunomediada va en contra de usarlo en esta enfermedad.

**Para avanzar se necesita:**
- Descartar la predicción de coroideremia, salvo que aparezca evidencia preclínica que vincule CTLA-4 con la degeneración retiniana por deficiencia de REP1.
- Reorientar el análisis hacia el melanoma no cutáneo (uveal y mucoso), que tiene evidencia nivel L3 y clasificación de «pregunta de investigación», y revisar datos de eficacia por subtipo.
- Descargar y analizar el prospecto de INVIMA para completar advertencias y contraindicaciones.
- Completar los datos del mecanismo de acción y confirmar la indicación aprobada en Colombia, que hoy solo figura como «IPILIMUMAB».

*Este informe es solo para fines de investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

