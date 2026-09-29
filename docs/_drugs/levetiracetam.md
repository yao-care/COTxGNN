---
layout: default
title: Levetiracetam
parent: Solo Predicción del Modelo (L5)
nav_order: 254
evidence_level: L5
indication_count: 10
---

# Levetiracetam
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

# Levetiracetam: De Indicación Original No Especificada en el Registro a Epilepsia Visual

## Resumen en Una Frase

Levetiracetam es un antiepiléptico comercializado en Colombia. Los registros sanitarios revisados solo repiten el nombre del principio activo y no detallan su indicación aprobada. El modelo TxGNN predice que podría ser efectivo para **epilepsia visual** (crisis desencadenadas por estímulos visuales), pero los **8 ensayos clínicos** y las **20 publicaciones** identificados son de epilepsia en general y ninguno es específico de esta condición. Es una predicción respaldada solo de forma indirecta.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el campo solo dice "LEVETIRACETAM") |
| Nueva Indicación Predicha | Epilepsia visual |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L4 (solo evidencia indirecta y de mecanismo; ningún estudio específico para epilepsia visual) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

El campo de mecanismo de acción (MOA) del Evidence Pack está vacío. El análisis mecanístico asociado a la predicción indica que levetiracetam actúa principalmente uniéndose a la proteína de vesícula sináptica 2A (SV2A). Esto modula la liberación presináptica de neurotransmisores y reduce el disparo neuronal hipersincrónico.

La epilepsia visual, o fotosensible, se caracteriza por descargas hipersincrónicas provocadas por luces intermitentes o patrones visuales. Un fármaco que amortigua esa hipersincronía es una hipótesis plausible.

Hay que ser cauteloso: el puntaje TxGNN es muy alto, pero probablemente refleja la asociación genérica entre fármacos antiepilépticos y las convulsiones, no una evidencia específica. De hecho, siete subtipos de crisis reflejas comparten exactamente el mismo puntaje (99.95%), lo que sugiere un efecto de proximidad en la ontología. La evidencia debe tratarse como indirecta, a nivel de clase de fármacos.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03107507](https://clinicaltrials.gov/study/NCT03107507) | Fase 4 | Desconocido | 40 | Eficacia de levetiracetam en el control de convulsiones neonatales. Misma clase de resultado, pero población distinta |
| [NCT00203216](https://clinicaltrials.gov/study/NCT00203216) | N/A | Completado | 31 | Estudio abierto de un solo centro sobre profilaxis de migraña con o sin aura (alteraciones visuales). No es específico de epilepsia visual |
| [NCT04277936](https://clinicaltrials.gov/study/NCT04277936) | Fase 2 | Terminado | 1 | Modulación de la hiperactividad del hipocampo en psicosis. Terminado con 1 participante; no relevante |
| [NCT07336992](https://clinicaltrials.gov/study/NCT07336992) | Fase 3 | No reclutando aún | 580 | Levetiracetam profiláctico tras hemorragia intracerebral. Previene crisis sintomáticas agudas, no epilepsia refleja; sin resultados |
| [NCT00855738](https://clinicaltrials.gov/study/NCT00855738) | Fase 4 | Completado | 111 | Estudio observacional de nuevos antiepilépticos como primera biterapia en epilepsia focal. Efectividad general |
| [NCT00105040](https://clinicaltrials.gov/study/NCT00105040) | Fase 2 | Completado | 87 | Estudio de seguridad cognitiva, controlado con placebo, en niños con crisis parciales refractarias. Sin población con desencadenante visual |
| [NCT04559529](https://clinicaltrials.gov/study/NCT04559529) | Fase 2 | Completado | 62 | Hiperactividad del hipocampo en trastornos psicóticos. Enfermedad distinta |
| [NCT04573803](https://clinicaltrials.gov/study/NCT04573803) | Fase 3 | No reclutando aún | 1649 | Ensayo MAST: manejo de crisis tras traumatismo craneoencefálico (fenitoína vs. levetiracetam). Indirecto y sin resultados |

Además, el pack incluye NCT04833907 (terapia génica AVASPA en enfermedad de Canavan), que no evalúa levetiracetam y se excluyó de la tabla.

## Evidencia de Literatura

Ninguna de las publicaciones aborda la epilepsia visual. Se listan las de mayor nivel de evidencia sobre levetiracetam en epilepsia en general.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [32385134](https://pubmed.ncbi.nlm.nih.gov/32385134/) | 2020 | ECA | Pediatrics | Levetiracetam vs. fenobarbital en convulsiones neonatales: evalúa eficacia y seguridad |
| [35963261](https://pubmed.ncbi.nlm.nih.gov/35963261/) | 2022 | ECA (Fase 3) | The Lancet Neurology | Ensayo PEACH: levetiracetam profiláctico para prevenir crisis en la fase aguda de hemorragia intracerebral |
| [38678766](https://pubmed.ncbi.nlm.nih.gov/38678766/) | 2024 | ECA | Seizure | Fenitoína vs. levetiracetam en crisis sintomáticas agudas de niños con síndrome de encefalitis aguda |
| [30487494](https://pubmed.ncbi.nlm.nih.gov/30487494/) | 2018 | ECA | Mymensingh Med J | Fenobarbital vs. levetiracetam en epilepsia infantil: eficacia y tolerabilidad |
| [34286461](https://pubmed.ncbi.nlm.nih.gov/34286461/) | 2022 | Revisión sistemática/metaanálisis | Neurocritical Care | Levetiracetam como profilaxis de crisis en cuidados neurocríticos (hemorragia intracerebral, TCE, neurocirugía, HSA) |
| [37378757](https://pubmed.ncbi.nlm.nih.gov/37378757/) | 2023 | Revisión sistemática/metaanálisis en red | Journal of Neurology | Comparación de eficacia y seguridad de fármacos antiepilépticos en epilepsias generalizadas idiopáticas |
| [40450767](https://pubmed.ncbi.nlm.nih.gov/40450767/) | 2025 | Revisión sistemática/metaanálisis | Epilepsy & Behavior | Levetiracetam frente a otros fármacos en crisis mioclónicas de epilepsia generalizada idiopática, en especial epilepsia mioclónica juvenil |
| [30884401](https://pubmed.ncbi.nlm.nih.gov/30884401/) | 2019 | Revisión sistemática | Epilepsy & Behavior | Levetiracetam vs. carbamazepina en epilepsia rolándica infantil |
| [38316735](https://pubmed.ncbi.nlm.nih.gov/38316735/) | 2024 | Guía clínica | Neurocritical Care | Guía de profilaxis de crisis en adultos con TCE moderado-grave |
| [34260837](https://pubmed.ncbi.nlm.nih.gov/34260837/) | 2021 | Revisión | N Engl J Med | Manejo inicial de una crisis epiléptica en adultos |

## Información de Mercado en Colombia

Se listan los registros únicos, porque el pack repite el mismo registro en varias filas.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20122152 | LEVETIRACETAM 1000 MG TABLETAS RECUBIERTAS (Laboratorios Lapроff S.A.S.) | Tableta recubierta | No detallada (solo figura "LEVETIRACETAM") |
| 20098490 | CONVULAM SOLUCIÓN ORAL (Saluspharma Labs S.A.S.) | Solución oral | No detallada (solo figura "LEVETIRACETAM") |

En total hay 20 registros sanitarios. También existen presentaciones de solución inyectable.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún ensayo ni publicación específica de epilepsia visual. El puntaje TxGNN alto parece un artefacto de proximidad con otras crisis reflejas, y el respaldo se limita a la plausibilidad del mecanismo (SV2A) y a evidencia general de epilepsia. Aunque el pack la clasifica como "Research Question" (pregunta de investigación), no hay base para avanzar.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA (advertencias y contraindicaciones), requisito bloqueante para el tamizaje de seguridad, y confirmar las indicaciones aprobadas en Colombia.
- Consultar el mecanismo de acción en DrugBank para completar el análisis mecanístico.
- Buscar evidencia específica en epilepsia fotosensible o desencadenada por estímulos visuales (series de casos, estudios de provocación fotoparoxística).
- Priorizar otras indicaciones predichas mejor respaldadas. **Estado epiléptico** tiene evidencia L1 (ensayos de Fase 3 como ESETT, PMID 31774955), aunque corresponde a una práctica ya establecida y no a un reposicionamiento novedoso. **Epilepsia por sobresalto** tiene evidencia L3 con datos clínicos específicos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

