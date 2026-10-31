---
layout: default
title: Pirfenidone
parent: Solo Predicción del Modelo (L5)
nav_order: 517
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-31
monitor_inn: "pirfenidone"
predicted_indications: ["extracutaneous mastocytoma", "dermatofibrosarcoma protuberans", "aggressive systemic mastocytosis", "heart fibrosarcoma", "conventional fibrosarcoma", "autosomal recessive familial Mediterranean fever", "kidney fibrosarcoma", "hepatic infarction", "fibroblastic neoplasm", "low grade fibromyxoid sarcoma"]
description: "Pirfenidone: nueva indicación predicha, Extracutaneous mastocytoma (nivel de evidencia L5). Indicación original: PIRFENIDONA"
---

# Pirfenidone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Pirfenidone: Extracutaneous mastocytoma
{: .text-alpha }

## Resumen en Una Frase

Pirfenidona es un fármaco antifibrótico registrado en Colombia bajo el nombre ESBRIET®, cuyos registros sanitarios figuran actualmente como cancelados. El modelo TxGNN predice que podría ser efectivo para **neoplasia fibroblástica**, pero la evidencia es muy limitada: **ningún ensayo clínico** y **6 publicaciones**, todas preclínicas, reportes de caso o un estudio piloto de relevancia no confirmada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | PIRFENIDONA |
| Nueva Indicación Predicha | Extracutaneous mastocytoma |
| Puntaje de Predicción TxGNN | 0.9971 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 2) |
| Número de Registros Sanitarios | al menos 3 |
| Decisión Recomendada | Hold |

**Nota sobre la selección de la indicación:** la primera predicción del modelo (rank 1) es *mastocitoma extracutáneo* (0.9971), pero no tiene ningún respaldo clínico ni bibliográfico (L5). Se presenta aquí la predicción de rank 9, *neoplasia fibroblástica*, por ser la única de las 10 predicciones con literatura asociada. Las demás predicciones se resumen al final de la sección de conclusión.

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, la pirfenidona es un agente antifibrótico y antiinflamatorio oral no citotóxico. Los estudios compilados indican que inhibe la acción de factores de crecimiento como TGF-β1, PDGF, EGF y FGF, lo que reduce la activación de fibroblastos y la síntesis de colágeno.

La relación con la nueva indicación se basa en esa biología compartida: las neoplasias fibroblásticas implican proliferación de fibroblastos, y la pirfenidona frena la transformación de fibroblastos en miofibroblastos inducida por TGF-β1. En fibroblastos derivados de la enfermedad de Dupuytren (un trastorno fibroproliferativo benigno) se observó esta inhibición, incluida la de vías de señalización no-SMAD.

Esta plausibilidad es **indirecta y preclínica**. Funciona para trastornos fibroblásticos benignos, pero no demuestra actividad contra tumores malignos. Además, dos reportes de caso describen un posible **señal de seguridad en sentido contrario** (un sarcoma pleomórfico indiferenciado tras el uso de pirfenidona y dermatofibromas eruptivos agravados por pirfenidona más micofenolato).

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [12907346](https://pubmed.ncbi.nlm.nih.gov/12907346/) | 2003 | Estudio clínico piloto (relevancia sin confirmar) | Am J Gastroenterol | Proyecto piloto sobre tumores desmoides en poliposis adenomatosa familiar para evaluar la eficacia de la pirfenidona, antifibrótico no citotóxico |
| [27835939](https://pubmed.ncbi.nlm.nih.gov/27835939/) | 2016 | Estudio in vitro | BMC Musculoskelet Disord | La pirfenidona inhibe la acción mediada por TGF-β1 en fibroblastos derivados de la enfermedad de Dupuytren |
| [30927912](https://pubmed.ncbi.nlm.nih.gov/30927912/) | 2019 | Estudio mecanístico in vitro | BMC Musculoskelet Disord | Efecto de la pirfenidona sobre vías no-SMAD estimuladas por TGF-β1 en fibroblastos de Dupuytren |
| [35129055](https://pubmed.ncbi.nlm.nih.gov/35129055/) | 2022 | Estudio preclínico/traslacional | Pharm Dev Technol | Evalúa la pirfenidona como antifibrótico inyectable local para la enfermedad de Dupuytren |
| [29702057](https://pubmed.ncbi.nlm.nih.gov/29702057/) | 2018 | Reporte de caso (posible señal de seguridad) | Perm J | Sarcoma pleomórfico indiferenciado tras el uso de pirfenidona |
| [32572469](https://pubmed.ncbi.nlm.nih.gov/32572469/) | 2020 | Reporte de caso (posible señal de seguridad) | Rheumatology (Oxford) | Dermatofibromas eruptivos múltiples agravados por micofenolato y pirfenidona en un paciente con esclerosis sistémica |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20093425 | ESBRIET® cápsulas duras 267 mg (vigente) | Cápsula dura | Pirfenidona |
| 20251036 | FIBROPER® 801 mg tableta recubierta (vigente) | Tableta recubierta | Pirfenidona |
| 20258933 | HETOPIR® 801 mg tabletas recubiertas (vigente) | Tableta recubierta | Pirfenidona |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas:** se identificaron 109 interacciones registradas; las 20 primeras listadas son de nivel moderado: bupropión, omeprazol, cimetidina, eliglustat, ácido obeticólico, oxandrolona, naltrexona, lansoprazol, miconazol, nitisinona, esomeprazol, fenilbutirato de glicerol, rolapitant, deferasirox, ticlopidina, lumefantrina, disulfiram, primaquina, tiabendazol e ivacaftor.
- **Señales de la literatura:** dos reportes de caso (sarcoma pleomórfico indiferenciado y dermatofibromas agravados) sugieren una posible señal de seguridad que requiere evaluación antes de considerar el uso en tumores fibroblásticos.
- **Hepatotoxicidad:** la pirfenidona conlleva una advertencia de hepatotoxicidad, relevante en enfermedad hepática.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en evidencia preclínica indirecta y en reportes de caso que incluso apuntan a un posible riesgo. No hay ensayos clínicos; el medicamento está comercializado en Colombia y cuenta con 3 registros sanitarios vigentes.

**Para avanzar se necesita:**
- Obtener las advertencias y contraindicaciones del prospecto de INVIMA y los datos del mecanismo de acción desde DrugBank.
- Estudios preclínicos en modelos tumorales (no solo fibróticos benignos) que confirmen o descarten actividad antitumoral.
- Evaluar con detalle la señal de seguridad de los reportes de caso (sarcoma y dermatofibromas).
- Aclarar el estatus regulatorio en Colombia (motivo de la cancelación y posibilidad de nuevo registro).
- Confirmar la relevancia del piloto en tumores desmoides (PMID 12907346).

**Otras predicciones del modelo (todas L5, Hold, sin ensayos ni literatura):** mastocitoma extracutáneo (0.9971), dermatofibrosarcoma protuberans (0.9941), mastocitosis sistémica agresiva (0.9933), fibrosarcoma de corazón (0.9929), fibrosarcoma convencional (0.9926), fiebre mediterránea familiar autosómica recesiva (0.9925), fibrosarcoma de riñón (0.9924), infarto hepático (0.9924) y sarcoma fibromixoide de bajo grado (0.9919). En varias de ellas existen terapias establecidas (por ejemplo, imatinib en dermatofibrosarcoma; colchicina y bloqueadores de IL-1 en fiebre mediterránea familiar).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

