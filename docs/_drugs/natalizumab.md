---
layout: default
title: Natalizumab
parent: Solo Predicción del Modelo (L5)
nav_order: 463
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
monitor_inn: "NATALIZUMAB"
predicted_indications: ["bronchitis", "parapsoriasis", "psoriasis", "severe nonproliferative diabetic retinopathy", "acute lichenoid pityriasis"]
description: "Natalizumab: nueva indicación predicha, Bronchitis (nivel de evidencia L5). Indicación original: NATALIZUMAB"
---

# Natalizumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Natalizumab: Bronchitis
{: .text-alpha }

## Resumen en Una Frase

Natalizumab es un anticuerpo monoclonal anti-integrina alfa4, con registros sanitarios en Colombia bajo el nombre Tysabri®, actualmente cancelados. El modelo TxGNN predice que podría ser efectivo para **psoriasis**, pero no hay ensayos clínicos registrados y la literatura disponible es de bajo nivel y con resultados contradictorios: hay una serie de casos con mejoría y varios reportes de psoriasis inducida o agravada por el fármaco.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | NATALIZUMAB |
| Nueva Indicación Predicha | Bronchitis |
| Puntaje de Predicción TxGNN | 0.9946 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 2 de 2) |
| Número de Registros Sanitarios | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Natalizumab es un anticuerpo dirigido contra la integrina alfa4, que bloquea la migración de leucocitos hacia los tejidos inflamados. Los datos compilados para este informe no incluyen una descripción formal del mecanismo de acción del fármaco, pero esta función de bloqueo del tráfico leucocitario es la base de su uso conocido en enfermedades inflamatorias mediadas por el sistema inmune.

La psoriasis es una enfermedad inflamatoria de la piel impulsada por linfocitos T. Por ello, bloquear la migración de células T es biológicamente plausible. Además, las revisiones sobre integrinas leucocitarias y terapias anti-adhesión (PMID 25448040, 15955735) respaldan esta lógica general.

Sin embargo, la evidencia clínica apunta en direcciones opuestas. Una serie de 18 pacientes con esclerosis múltiple y psoriasis comórbida describe mejoría con natalizumab, mientras que varios reportes de caso describen psoriasis inducida o agravada por el mismo fármaco. Por tanto, la plausibilidad mecanística no basta para respaldar esta indicación.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Se listan las publicaciones más relevantes, priorizando estudios observacionales y reportes de caso directamente ligados a psoriasis, seguidos de revisiones.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33589543](https://pubmed.ncbi.nlm.nih.gov/33589543/) | 2021 | Observacional / serie de casos | Neurology Neuroimmunology & Neuroinflammation | Observaciones en 18 pacientes con esclerosis múltiple y psoriasis comórbida tratados con natalizumab; reporta mejoría de la psoriasis |
| [35646438](https://pubmed.ncbi.nlm.nih.gov/35646438/) | 2022 | Reporte de caso (evento adverso) | Dermatology Practical & Conceptual | Psoriasis pustulosa de palmas y plantas inducida por natalizumab |
| [28905124](https://pubmed.ncbi.nlm.nih.gov/28905124/) | 2018 | Reporte de caso con revisión | Neurological Sciences | Psoriasis artrítica durante el tratamiento con natalizumab |
| [30323758](https://pubmed.ncbi.nlm.nih.gov/30323758/) | 2018 | Reporte de caso con revisión | Case Reports in Neurology | Psoriasis en placas en un paciente de 33 años durante el tratamiento; discute si natalizumab induce o agrava la enfermedad |
| [40526577](https://pubmed.ncbi.nlm.nih.gov/40526577/) | 2025 | Revisión | Deutsches Ärzteblatt International | Opciones de tratamiento para la comorbilidad de esclerosis múltiple con otras enfermedades inflamatorias crónicas, entre ellas la psoriasis |
| [25448040](https://pubmed.ncbi.nlm.nih.gov/25448040/) | 2015 | Revisión | Pharmacology & Therapeutics | Papel de las integrinas leucocitarias en el reclutamiento de leucocitos y como dianas terapéuticas |
| [15955735](https://pubmed.ncbi.nlm.nih.gov/15955735/) | 2005 | Revisión | Current Opinion in Pharmacology | Terapias anti-adhesión dirigidas a moléculas de adhesión celular |
| [20298966](https://pubmed.ncbi.nlm.nih.gov/20298966/) | 2010 | Revisión (seguridad PML) | The Lancet Neurology | Características clínicas y patogénesis de la leucoencefalopatía multifocal progresiva (LMP) asociada a anticuerpos monoclonales como natalizumab |
| [24136456](https://pubmed.ncbi.nlm.nih.gov/24136456/) | 2013 | Revisión (seguridad PML) | Current Neurology and Neuroscience Reports | LMP en esclerosis múltiple tras la introducción de agentes biológicos como natalizumab |
| [30324046](https://pubmed.ncbi.nlm.nih.gov/30324046/) | 2018 | Mini revisión | Cureus | LMP asociada a natalizumab en pacientes con esclerosis múltiple |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20241992 | TYSABRI® SUBCUTÁNEO 150MG/ML | Solución inyectable | Natalizumab (vigente) |
| 20006016 | TYSABRI® | Solución concentrada para infusión | Natalizumab (vigente) |

## Consideraciones de Seguridad

- **Contraindicaciones (grafo de conocimiento TxGNN, no texto del prospecto)**: leucoencefalopatía multifocal progresiva (LMP). La literatura revisada documenta repetidamente casos de LMP asociados a natalizumab, una infección cerebral grave y a menudo fatal causada por el virus JC.
- **Interacciones farmacológicas**: se identificaron 100 interacciones. Entre las principales:
  - **Mayor**: corticoides (hidrocortisona, triamcinolona, dexametasona, betametasona, budesonida, prednisolona, prednisona), mercaptopurina, levamisol, trimetrexato, ibritumomab tiuxetán, tositumomab (incluido el marcado con I-131) y iobenguano (I-131).
  - **Moderada**: naltrexona.
  - **Menor**: sales de zinc (sulfato, acetato, gluconato, cloruro).
- **Reacciones cutáneas**: los reportes de caso muestran psoriasis inducida o agravada, lo que es una señal de seguridad específica para esta indicación.

Para advertencias y contraindicaciones del prospecto, consultar directamente el prospecto del producto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia se limita a una serie de casos favorable, varios reportes de psoriasis inducida o agravada por natalizumab y revisiones generales, sin ensayos clínicos. Sumado al riesgo de LMP y a que los registros sanitarios en Colombia están cancelados, no hay base para avanzar con esta indicación.

**Para avanzar se necesita:**
- Resolver la contradicción sobre el efecto en psoriasis (mejoría frente a inducción o agravamiento), idealmente con estudios controlados.
- Datos del mecanismo de acción desde DrugBank para fortalecer el análisis mecanístico.
- Obtener y revisar el prospecto de INVIMA con advertencias y contraindicaciones, necesario para el tamizaje de seguridad.
- Evaluar la relación beneficio-riesgo frente a alternativas ya aprobadas para psoriasis, dado el riesgo de LMP.
- Aclarar la situación regulatoria, ya que ambos registros sanitarios están cancelados y no existe comercialización vigente.

**Nota sobre otras indicaciones predichas:** bronquitis, retinopatía diabética no proliferativa grave, parapsoriasis y pitiriasis liquenoide aguda también tienen decisión Hold. Las dos primeras no cuentan con ensayos ni literatura (L5). Las dos últimas solo cuentan con un reporte de caso de eventos adversos cutáneos (L4), que no demuestra beneficio terapéutico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

