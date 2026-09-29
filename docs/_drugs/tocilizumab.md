---
layout: default
title: Tocilizumab
parent: Solo Predicción del Modelo (L5)
nav_order: 388
evidence_level: L5
indication_count: 10
---

# Tocilizumab
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

# Tocilizumab: De Indicación Original No Especificada en el Registro a Espondilitis Anquilosante

## Resumen en Una Frase

Tocilizumab es un anticuerpo monoclonal humanizado contra el receptor de interleucina-6 (IL-6R), comercializado en Colombia como Actemra. El registro sanitario solo repite el nombre del principio activo, así que la indicación original no queda documentada en los datos.
El modelo TxGNN predice que podría ser efectivo para **Espondilitis Anquilosante**, con **9 ensayos clínicos** (solo 2 de ellos evalúan directamente la eficacia, ambos terminados anticipadamente) y **19 publicaciones** relacionadas.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el texto del registro solo dice "TOCILIZUMAB") |
| Nueva Indicación Predicha | Espondilitis anquilosante |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L3 (el pipeline asignó L1, pero los dos ECA de Fase 3 fueron terminados y no completados; ver nota abajo) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 10 |
| Decisión Recomendada | Hold |

**Nota sobre el nivel de evidencia:** el nivel L1 exige al menos 2 ECA de Fase 3 *completados*. Los estudios NCT01209689 y NCT01209702 tienen estado "Terminado" y los datos no muestran resultados de eficacia. Por eso, según las reglas, la evidencia se sostiene en revisiones sistemáticas y metaanálisis (L3).

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, tocilizumab bloquea el receptor de IL-6 (tanto el soluble como el unido a membrana). Está establecido en otras enfermedades reumáticas como la artritis reumatoide, la artritis idiopática juvenil y la arteritis de células gigantes.

La IL-6 participa en la inflamación de las espondiloartritis, junto con el TNF-α y la IL-17, lo que da una base biológica plausible para bloquear su receptor en la espondilitis anquilosante. Una revisión de 2012 sobre el antagonismo de IL-6 en esta enfermedad (PMID 22452603) discute este mismo racional.

Que el mecanismo sea plausible no demuestra que funcione. Los dos ECA controlados con placebo fueron terminados en 2011 y los datos disponibles no muestran sus resultados de eficacia. Cualquier conclusión sobre eficacia requiere revisar antes las publicaciones de esos estudios.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01209689](https://clinicaltrials.gov/study/NCT01209689) | Fase 3 | Terminado | 113 | ECA doble ciego contra placebo: tocilizumab 8 o 4 mg/kg IV cada 4 semanas durante 24 semanas en espondilitis anquilosante con respuesta inadecuada a anti-TNF |
| [NCT01209702](https://clinicaltrials.gov/study/NCT01209702) | Fase 3 | Terminado | 306 | ECA Fase 2/3 continuo, doble ciego, contra placebo, en pacientes sin respuesta a AINE y sin exposición previa a anti-TNF; evalúa signos, síntomas y daño estructural |
| [NCT01965132](https://clinicaltrials.gov/study/NCT01965132) | N/A | En reclutamiento | 10000 | Registro coreano de terapias biológicas; observacional, describe seguridad en la práctica real |
| [NCT05670301](https://clinicaltrials.gov/study/NCT05670301) | N/A | En reclutamiento | 2500 | Estudio de biomarcadores y perfiles de citocinas en enfermedades inflamatorias sistémicas; sin datos de eficacia |
| [NCT02569736](https://clinicaltrials.gov/study/NCT02569736) | N/A | Completado | 60 | Estudio mecanístico del efecto de tocilizumab sobre células T foliculares cooperadoras en artritis reumatoide |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Fase 2 | No reclutando aún | 80 | Manejo perioperatorio de inmunosupresores en pacientes reumatológicos; no evalúa eficacia |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Desconocido | 750000 | Estudio observacional del riesgo de nuevas enfermedades inmunomediadas en pacientes tratados con biológicos |
| [NCT02925338](https://clinicaltrials.gov/study/NCT02925338) | N/A | Completado | 1431 | Observatorio de uso real de un biosimilar de infliximab; no trata de tocilizumab |
| [NCT07477795](https://clinicaltrials.gov/study/NCT07477795) | Fase 2 | No reclutando aún | 52 | ECA de secukinumab en arteritis de Takayasu; el vínculo con tocilizumab y con esta indicación no está confirmado |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [23765873](https://pubmed.ncbi.nlm.nih.gov/23765873/) | 2014 | ECA (publicación de resultados) | Ann Rheum Dis | Evalúa la eficacia sintomática a corto plazo y la seguridad de tocilizumab en los estudios BUILDER-1 y BUILDER-2; el resumen disponible no incluye los resultados |
| [26986130](https://pubmed.ncbi.nlm.nih.gov/26986130/) | 2016 | Revisión sistemática / metaanálisis en red | Medicine | Compara la eficacia de los regímenes biológicos en espondilitis anquilosante a partir de ECA |
| [29290076](https://pubmed.ncbi.nlm.nih.gov/29290076/) | 2018 | Metaanálisis | Clin Rheumatol | Riesgo de infecciones graves con tratamiento biológico en espondilitis anquilosante y espondiloartritis axial no radiográfica |
| [31852268](https://pubmed.ncbi.nlm.nih.gov/31852268/) | 2020 | Revisión sistemática | Expert Rev Clin Immunol | Compara el riesgo de infección entre FAME no biológicos y biológicos en artritis inflamatoria |
| [22452603](https://pubmed.ncbi.nlm.nih.gov/22452603/) | 2012 | Revisión | Inflamm Allergy Drug Targets | Revisión breve del papel de IL-6 y de su antagonismo en espondilitis anquilosante |
| [22450391](https://pubmed.ncbi.nlm.nih.gov/22450391/) | 2012 | Revisión | Curr Opin Rheumatol | Alternativas terapéuticas en espondilitis anquilosante refractaria a inhibidores de TNF |
| [28413099](https://pubmed.ncbi.nlm.nih.gov/28413099/) | 2017 | Revisión | Semin Arthritis Rheum | Optimización del biológico de segunda línea en artritis reumatoide, artritis psoriásica y espondilitis anquilosante |
| [21803631](https://pubmed.ncbi.nlm.nih.gov/21803631/) | 2011 | Revisión | Joint Bone Spine | Agentes biológicos más allá de los antagonistas de TNF-α en espondilitis anquilosante |
| [33981717](https://pubmed.ncbi.nlm.nih.gov/33981717/) | 2021 | Reporte de caso | Front Med | Dos casos de amiloidosis AA en espondilitis anquilosante tratados con tocilizumab, con revisión de la literatura |
| [39963138](https://pubmed.ncbi.nlm.nih.gov/39963138/) | 2025 | Revisión / guía | Front Immunol | Manejo del riesgo de tuberculosis, tamizaje y terapia preventiva en pacientes con artritis autoinmune crónica bajo biológicos |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20002627 | ACTEMRA® CONCENTRADO PARA INFUSION 200 MG/10ML | Solución inyectable | No especificada (el registro solo indica "TOCILIZUMAB") |
| 20062328 | ACTEMRA® SOLUCIÓN INYECTABLE 162MG/0.9ML | Solución inyectable | No especificada (el registro solo indica "TOCILIZUMAB") |

Ambos productos son fabricados por F. Hoffmann-La Roche Ltd. El registro 20002627 aparece repetido varias veces en los datos, por eso se muestra una sola fila.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Los dos ECA de Fase 3 en espondilitis anquilosante fueron terminados en 2011 y los datos disponibles no muestran resultados de eficacia, por lo que el nivel L1 asignado por el pipeline sobrestima la evidencia. Además, hay una brecha de datos bloqueante: no se cuenta con las advertencias y contraindicaciones del prospecto de INVIMA.

**Para avanzar se necesita:**
- Revisar los resultados publicados de BUILDER-1 y BUILDER-2 (PMID 23765873) y verificar por qué se terminaron los estudios.
- Descargar y analizar el prospecto de INVIMA (advertencias, contraindicaciones e interacciones), ya que el filtro de seguridad no puede avanzar sin ello.
- Obtener datos del mecanismo de acción desde DrugBank.
- Confirmar las indicaciones aprobadas en Colombia para Actemra, porque el registro solo muestra el nombre del principio activo.
- Contrastar con el resto de las predicciones. La artritis idiopática juvenil poliarticular (rango 7) tiene múltiples ECA de Fase 3 completados y podría ser un uso ya establecido más que un reposicionamiento. Los rangos 3, 6 y 9 carecen de evidencia y no se recomienda perseguirlos.

*Este informe es solo para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su uso.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

