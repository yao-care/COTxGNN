---
layout: default
title: Busulfan
parent: Solo Predicción del Modelo (L5)
nav_order: 103
evidence_level: L5
indication_count: 10
---

# Busulfan
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

# Busulfán: De Agente Alquilante de Acondicionamiento a Síndrome Mielodisplásico

## Resumen en Una Frase

Busulfán es un agente alquilante bifuncional usado como base del acondicionamiento mieloablativo antes del trasplante de células madre. El registro sanitario colombiano no detalla su indicación original.
El modelo TxGNN predice que podría ser efectivo para el **Síndrome Mielodisplásico (SMD)**, con **50 ensayos clínicos** y **20 publicaciones** que respaldan esta dirección. La evidencia es directa pero no exclusiva de busulfán: proviene de regímenes de acondicionamiento basados en busulfán.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No registrada en el paquete de evidencia (el texto del registro INVIMA solo dice "BUSULFAN"). Uso descrito: acondicionamiento mieloablativo previo a trasplante |
| Nueva Indicación Predicha | Síndrome mielodisplásico |
| Puntaje de Predicción TxGNN | 99.62% |
| Nivel de Evidencia | L1 (con salvedad: aplica al acondicionamiento basado en busulfán, no a busulfán en monoterapia) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 8 (3 registros únicos en el listado detallado) |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Los datos de mecanismo de acción del campo original están vacíos. Según el análisis del paquete de evidencia, busulfán es un agente alquilante bifuncional que forma enlaces cruzados en el ADN y es mieloablativo. Su efecto en el SMD no proviene de una modulación específica de la enfermedad, sino de eliminar el clon displásico y crear espacio en la médula ósea para el injerto.

El trasplante alogénico de células madre es la única opción potencialmente curativa para el SMD. Busulfán se usa como columna vertebral del acondicionamiento (Bu/Flu, Bu/Cy) antes de ese trasplante. Por eso la relación con la indicación original es de uso: es el mismo fármaco, con el mismo mecanismo, en un contexto de trasplante donde el SMD es una de las enfermedades tratadas.

Los ECA de Fase 3 disponibles comparan treosulfán contra busulfán (busulfán es el brazo comparador) o acondicionamiento mieloablativo contra de intensidad reducida en poblaciones de SMD/LMA. Son evidencia directa, pero no exclusiva de busulfán.

---

## Evidencia de Ensayos Clínicos

Se listan 10 de los 50 ensayos registrados.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02250937](https://clinicaltrials.gov/study/NCT02250937) | Fase 2 | Activo, no recluta | 116 | Trasplante alogénico con venetoclax y busulfán/cladribina/fludarabina secuenciales en LMA y SMD |
| [NCT06477549](https://clinicaltrials.gov/study/NCT06477549) | Fase 2 | Reclutando | 220 | Bendamustina vs ruxolitinib con acondicionamiento Flu/Bu en trasplante haploidéntico; busulfán es la base fija |
| [NCT00226512](https://clinicaltrials.gov/study/NCT00226512) | Fase 3 | Retirado | 203 | Fludarabina + busulfán no mieloablativo con o sin anticuerpos antilinfocitos en LMA o SMD |
| [NCT00002989](https://clinicaltrials.gov/study/NCT00002989) | Fase 3 | Desconocido | 207 | Intensificación del acondicionamiento para trasplante alogénico en leucemia o SMD de alto riesgo de recaída |
| [NCT02861417](https://clinicaltrials.gov/study/NCT02861417) | Fase 2 | Activo, no recluta | 204 | Busulfán secuencial, fludarabina y ciclofosfamida postrasplante en cáncer de sangre |
| [NCT00301834](https://clinicaltrials.gov/study/NCT00301834) | Fase 2 | Completado | 35 | Fludarabina, busulfán y alemtuzumab de toxicidad reducida en niños con SMD, fallo medular o defectos de células madre |
| [NCT00863148](https://clinicaltrials.gov/study/NCT00863148) | Fase 2 | Completado | 30 | Clofarabina con busulfán IV y timoglobulina como acondicionamiento de intensidad reducida en LMA, SMD o LLA de alto riesgo |
| [NCT03412266](https://clinicaltrials.gov/study/NCT03412266) | Fase 2 | Desconocido | 50 | Acondicionamiento de intensidad reducida en SMD de riesgo bajo e intermedio con trasplante haploidéntico |
| [NCT05027945](https://clinicaltrials.gov/study/NCT05027945) | Fase 2 | Reclutando | 54 | Trasplante alogénico en síndrome VEXAS, frecuentemente asociado a SMD; el acondicionamiento no está confirmado |
| [NCT01177371](https://clinicaltrials.gov/study/NCT01177371) | Fase 2 | Completado | 13 | Busulfán y ciclofosfamida en dosis altas con trasplante alogénico en leucemia, SMD, mieloma y linfoma |

---

## Evidencia de Literatura

Se listan 10 de las 20 publicaciones, con prioridad para ECA, revisiones y metaanálisis.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31606445](https://pubmed.ncbi.nlm.nih.gov/31606445/) | 2020 | ECA Fase 3 | Lancet Haematol | Treosulfán + fludarabina vs busulfán de intensidad reducida + fludarabina como acondicionamiento en pacientes mayores con LMA o SMD (no inferioridad) |
| [28380315](https://pubmed.ncbi.nlm.nih.gov/28380315/) | 2017 | ECA Fase 3 | J Clin Oncol | Acondicionamiento mieloablativo vs de intensidad reducida en LMA y SMD |
| [35617104](https://pubmed.ncbi.nlm.nih.gov/35617104/) | 2022 | ECA (análisis final) | Am J Hematol | Análisis final del estudio de treosulfán vs busulfán de intensidad reducida en pacientes mayores o con comorbilidades con LMA/SMD |
| [36702138](https://pubmed.ncbi.nlm.nih.gov/36702138/) | 2023 | ECA Fase 3 | Lancet Haematol | G-CSF + decitabina + busulfán-ciclofosfamida vs busulfán-ciclofosfamida para reducir la recaída en SMD o LMA secundaria |
| [34692485](https://pubmed.ncbi.nlm.nih.gov/34692485/) | 2021 | Metaanálisis | Front Oncol | Acondicionamiento de intensidad reducida vs mieloablativo en LMA y SMD, sobre ECA |
| [33425740](https://pubmed.ncbi.nlm.nih.gov/33425740/) | 2020 | Revisión sistemática y metaanálisis | Front Oncol | Resultados a largo plazo de acondicionamiento con treosulfán vs busulfán en SMD y LMA |
| [40079242](https://pubmed.ncbi.nlm.nih.gov/40079242/) | 2025 | Revisión | Am J Hematol | Revisión contemporánea del trasplante alogénico en mielofibrosis y SMD; único tratamiento potencialmente curativo |
| [34489555](https://pubmed.ncbi.nlm.nih.gov/34489555/) | 2021 | Cohorte (registro, emparejamiento por puntaje de propensión) | Bone Marrow Transplant | Fludarabina/busulfán vs busulfán/ciclofosfamida mieloablativo en SMD |
| [35296446](https://pubmed.ncbi.nlm.nih.gov/35296446/) | 2022 | Cohorte (registro) | Transplant Cell Ther | Fludarabina/busulfán mieloablativo vs de intensidad reducida en SMD |
| [33471943](https://pubmed.ncbi.nlm.nih.gov/33471943/) | 2021 | Cohorte | Cancer | Busulfán mieloablativo fraccionado en pacientes mayores con LMA y SMD |

---

## Información de Mercado en Colombia

Se muestran los registros únicos. El paquete lista 8 registros en total, pero el detalle repite dos de ellos.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20158009 | BUSULFAN SOLUCIÓN INYECTABLE 60 MG/10 ML (HB Human Bioscience) | Solución inyectable | BUSULFAN (sin texto de indicación) |
| 20254653 | BUSADVAN (Advance Scientific de Colombia) | Solución inyectable | BUSULFAN (sin texto de indicación) |
| 20152745 | ALSULFAN® (AL Pharma) | Solución concentrada para infusión | BUSULFAN (sin texto de indicación) |

---

## Citotoxicidad

Los datos de toxicidad no están en el paquete de evidencia. Lo siguiente se basa en la clase del fármaco (agente alquilante antineoplásico) y debe confirmarse con el prospecto.

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (agente alquilante bifuncional) |
| Riesgo de Mielosupresión | Alto (es mieloablativo por diseño; requiere rescate con trasplante de células madre) |
| Clasificación de Emetogenicidad | Media |
| Items de Monitoreo | Hemograma con diferencial, función hepática y bilirrubina (riesgo de enfermedad venooclusiva), función renal, monitoreo farmacocinético |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. El paquete no contiene advertencias, contraindicaciones ni interacciones farmacológicas documentadas para los registros colombianos.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay ECA de Fase 3 que incluyen regímenes con busulfán en poblaciones de SMD, y el fármaco está comercializado en Colombia. Sin embargo, la evidencia respalda el acondicionamiento basado en busulfán dentro del trasplante, no busulfán en monoterapia, y busulfán suele ser el brazo comparador. Las otras nueve indicaciones predichas tienen evidencia más débil (L3 a L5) y no se recomiendan por ahora.

**Para avanzar se necesita:**
- Uso restringido a centros de trasplante
- Monitoreo farmacocinético terapéutico
- Vigilancia del riesgo de enfermedad venooclusiva/síndrome de obstrucción sinusoidal y profilaxis de convulsiones
- Intensidad del acondicionamiento ajustada por edad y comorbilidades
- Advertencias, contraindicaciones e interacciones del prospecto INVIMA (brecha bloqueante en los datos)
- Indicación aprobada y mecanismo de acción documentados en la fuente
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

