---
layout: default
title: Busulfan
parent: Evidencia Alta (L1-L2)
nav_order: 123
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Busulfan: nueva indicación predicha, Síndrome mielodisplásico (nivel de evidencia L1). Indicación original: No especificada en los registros"
monitor_inn: "BUSULFAN"
predicted_indications: ["myelodysplastic syndrome", "refractory cytopenia of childhood", "unclassified myelodysplastic syndrome", "partial deletion of the long arm of chromosome 5", "aregenerative anemia", "severe congenital hypochromic anemia with ringed sideroblasts", "HIV infectious disease", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "seborrheic keratosis", "feline acquired immunodeficiency syndrome"]
---

# Busulfan
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

# Busulfán: De Indicación Registrada No Especificada a Síndrome Mielodisplásico

## Resumen en Una Frase

Busulfán es un agente alquilante bifuncional que cuenta con registros sanitarios en Colombia, aunque el texto de indicación aprobada solo repite el nombre del fármaco, por lo que no es posible precisar su uso original según los registros.
El modelo TxGNN predice que podría ser efectivo para el **síndrome mielodisplásico (SMD)**, con **más de 40 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección, casi siempre como agente de acondicionamiento previo al trasplante de células madre hematopoyéticas.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en los registros (el texto registrado solo dice "BUSULFAN") |
| Nueva Indicación Predicha | Síndrome mielodisplásico |
| Puntaje de Predicción TxGNN | 99.62% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 4 (todos cancelados) |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este reporte. Según el conocimiento farmacológico general, el busulfán es un agente alquilante bifuncional que genera enlaces cruzados en el ADN y produce mieloablación. Su eficacia como agente citotóxico sobre las células hematopoyéticas está ampliamente comprobada.

En el síndrome mielodisplásico, el busulfán no se usa como tratamiento modificador de la enfermedad por sí solo. Es la base de muchos regímenes de acondicionamiento previos al trasplante alogénico de células madre hematopoyéticas (alo-TCMH), que es la única opción potencialmente curativa. El fármaco erradica el clon maligno y crea espacio en la médula ósea para que prospere el injerto del donante.

Por ello, la predicción es razonable en términos mecanísticos, pero debe interpretarse como "busulfán como componente del acondicionamiento para trasplante en SMD", no como un nuevo tratamiento independiente.

---

## Evidencia de Ensayos Clínicos

Se muestran los ensayos más relevantes (de un total superior a 40 registrados para esta indicación):

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00005866](https://clinicaltrials.gov/study/NCT00005866) | Fase 3 | Completado | 240 | Compara busulfán-TBI frente a ciclofosfamida-TBI en SMD avanzado o LMA relacionada con SMD, con trasplante de hermano HLA idéntico |
| [NCT00822393](https://clinicaltrials.gov/study/NCT00822393) | Fase 3 | Completado | 570 | Acondicionamiento con treosulfán frente a busulfán de intensidad reducida en LMA o SMD no aptos para regímenes estándar |
| [NCT04708054](https://clinicaltrials.gov/study/NCT04708054) | Fase 2/3 | Reclutando | 324 | Venetoclax añadido a régimen fraccionado de busulfán en LMA y SMD de alto riesgo |
| [NCT05453552](https://clinicaltrials.gov/study/NCT05453552) | Fase 2/3 | Desconocido | 242 | G-CSF + decitabina + BuCy frente a G-CSF + decitabina + BuF en SMD de alto riesgo |
| [NCT04713956](https://clinicaltrials.gov/study/NCT04713956) | Fase 2/3 | Desconocido | 242 | Mismo esquema comparativo en RAEB-1, RAEB-2 y LMA secundaria a SMD |
| [NCT00502905](https://clinicaltrials.gov/study/NCT00502905) | Fase 2 | Completado | 200 | Busulfán intravenoso con fludarabina antes de trasplante alogénico en LMA y SMD |
| [NCT02250937](https://clinicaltrials.gov/study/NCT02250937) | Fase 2 | Activo, sin reclutar | 116 | Venetoclax con busulfán, cladribina y fludarabina en secuencia temporal en LMA y SMD |
| [NCT01168219](https://clinicaltrials.gov/study/NCT01168219) | Fase 2 | Completado | 68 | Azacitidina añadida a acondicionamiento de intensidad reducida (busulfán, fludarabina, ATG) en SMD y LMA de pacientes mayores |
| [NCT06247917](https://clinicaltrials.gov/study/NCT06247917) | Fase 2 | Desconocido | 59 | FLU-BU-MEL como acondicionamiento en SMD, estudio de un solo brazo |
| [NCT01643668](https://clinicaltrials.gov/study/NCT01643668) | Fase 2 | Completado | 34 | Acondicionamiento de intensidad reducida con busulfán/clofarabina; estudio pequeño de un solo brazo |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31606445](https://pubmed.ncbi.nlm.nih.gov/31606445/) | 2020 | ECA (Fase 3) | The Lancet Haematology | Treosulfán más fludarabina frente a busulfán de intensidad reducida más fludarabina en pacientes mayores con LMA o SMD; diseño de no inferioridad |
| [42285355](https://pubmed.ncbi.nlm.nih.gov/42285355/) | 2026 | ECA (Fase 2) | Transplantation and Cellular Therapy | Dos esquemas de fraccionamiento de busulfán mieloablativo con fludarabina y cladribina en LMA o SMD |
| [36702138](https://pubmed.ncbi.nlm.nih.gov/36702138/) | 2023 | Ensayo Fase 3 aleatorizado | The Lancet Haematology | G-CSF + decitabina + BuCy frente a BuCy para reducir recaída en SMD o LMA secundaria |
| [35617104](https://pubmed.ncbi.nlm.nih.gov/35617104/) | 2022 | Análisis final de ensayo aleatorizado | American Journal of Hematology | Treosulfán frente a busulfán de intensidad reducida: mejores resultados en pacientes mayores con LMA/SMD |
| [33425740](https://pubmed.ncbi.nlm.nih.gov/33425740/) | 2020 | Revisión sistemática y metaanálisis | Frontiers in Oncology | Resultados a largo plazo de acondicionamientos con treosulfán frente a busulfán en SMD y LMA |
| [34692485](https://pubmed.ncbi.nlm.nih.gov/34692485/) | 2021 | Metaanálisis de ECA | Frontiers in Oncology | Acondicionamiento de intensidad reducida frente a mieloablativo en LMA y SMD |
| [40079242](https://pubmed.ncbi.nlm.nih.gov/40079242/) | 2025 | Revisión | American Journal of Hematology | Revisión contemporánea del trasplante alogénico en mielofibrosis y SMD |
| [34489555](https://pubmed.ncbi.nlm.nih.gov/34489555/) | 2021 | Análisis de registro (emparejado por puntaje de propensión) | Bone Marrow Transplantation | Flu/Bu4 frente a Bu/Cy como acondicionamiento mieloablativo en SMD |
| [35296446](https://pubmed.ncbi.nlm.nih.gov/35296446/) | 2022 | Análisis de registro (emparejado por puntaje de propensión) | Transplantation and Cellular Therapy | Flu/Bu4 mieloablativo frente a Flu/Bu2 de intensidad reducida en SMD |
| [38197938](https://pubmed.ncbi.nlm.nih.gov/38197938/) | 2024 | Cohorte (Fase 1) | Blood Advances | Mantenimiento profiláctico con venetoclax/azacitidina tras acondicionamiento Ven/FluBu2 en SMD/LMA de alto riesgo |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20158009 | Busulfan solución inyectable 60 mg/10 mL | Solución inyectable | BUSULFAN (cancelado) |
| 20254653 | Busadvan | Solución inyectable | BUSULFAN (cancelado) |
| 20152745 | Alsulfan® | Solución concentrada para infusión | BUSULFAN (cancelado) |
| 20205961 | Buslera® | Solución inyectable | BUSULFAN (cancelado) |

Los cuatro registros figuran como cancelados, por lo que actualmente no hay producto con registro vigente en Colombia.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (agente alquilante bifuncional) |
| Riesgo de Mielosupresión | Alto (mieloablación es el efecto buscado en el acondicionamiento; se asocian neutropenia, trombocitopenia y anemia) |
| Clasificación de Emetogenicidad | Consultar el prospecto; no hay datos específicos en la información compilada |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal, electrolitos; vigilancia de toxicidad pulmonar y hepática |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

- **Contraindicaciones en el grafo de conocimiento (no provienen del prospecto)**: el grafo de conocimiento TxGNN asocia busulfán con epilepsia, trombocitopenia, hiperglucemia, infecciones fúngicas e infecciones en general, dermatofitosis, deficiencia de potasio, hiperuricemia, neutropenia, agranulocitosis, anemia (incluida la macrocítica y la anemia de Fanconi) y fibrosis pulmonar (incluida la posinflamatoria). Deben verificarse contra el prospecto oficial.
- **Interacciones farmacológicas**: se identificaron 100 interacciones potenciales. Las principales son:
  - **Mayor**: metronidazol.
  - **Moderada**: aprepitant y miconazol.
  - **Menor**: levofloxacino.
  - Otras interacciones de nivel no clasificado incluyen anfotericina B, vancomicina, corticoides (prednisona, hidrocortisona, prednisolona, dexametasona), inhibidores de bomba de protones y antagonistas H2, antieméticos (ondansetrón, granisetrón, metoclopramida), manitol y morfina.
- **Riesgo de segunda neoplasia**: la literatura señala que la incidencia de neoplasias secundarias asociadas a busulfán es baja pero poco caracterizada (PMID 37856098).

No se dispone de advertencias del prospecto; consultar el prospecto para información de seguridad complementaria.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen al menos dos ensayos de Fase 3 completados que incluyen regímenes con busulfán en SMD (NCT00005866 y NCT00822393), además de ensayos de Fase 2/3 en curso y ECA publicados. La evidencia respalda su papel como agente de acondicionamiento previo al trasplante, no como terapia independiente, y los cuatro registros colombianos están cancelados.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), actualmente un vacío bloqueante para el tamizaje de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Aclarar la situación regulatoria: reactivar o tramitar un nuevo registro sanitario vigente.
- Definir el contexto de uso (acondicionamiento para alo-TCMH en centros especializados) y un plan de monitoreo de toxicidad (mielosupresión, hepática, pulmonar y neurológica, incluido el riesgo de convulsiones).
- Revisar el manejo de las interacciones relevantes, en particular metronidazol, azoles y otros fármacos concomitantes del trasplante.

---

### Otras Indicaciones Predichas (referencia breve)

- **Citopenia refractaria de la infancia** (L2, Proceed with Guardrails): subtipo pediátrico de SMD tratado con alo-TCMH; evidencia basada en protocolos de acondicionamiento mixtos.
- **Anemia aregenerativa/aplásica** (L1, Proceed with Guardrails): evidencia indirecta; en anemia aplásica grave los regímenes con ciclofosfamida siguen siendo el estándar y el busulfán se usa sobre todo en contextos de donante alternativo o refractarios.
- **SMD no clasificado** (L3, Research Question), **infección por VIH** (L3, Research Question; busulfán solo como acondicionamiento para terapia celular génica, sin acción antiviral): evidencia limitada.
- **Deleción parcial del brazo largo del cromosoma 5, anemia sideroblástica congénita grave, trastorno del neurodesarrollo con marcha atáxica, queratosis seborreica y síndrome de inmunodeficiencia adquirida felina** (L5, Hold): solo predicción computacional, sin evidencia ni vínculo mecanístico plausible.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

