---
layout: default
title: Dasatinib
parent: Solo Predicción del Modelo (L5)
nav_order: 150
evidence_level: L5
indication_count: 10
---

# Dasatinib
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

# Dasatinib: De Indicación Original No Especificada en el Registro a Sarcoma de Ewing

## Resumen en Una Frase

El registro sanitario de INVIMA solo lista el nombre "DASATINIB" y no detalla su indicación original. Según el propio Evidence Pack, es un inhibidor multiquinasa comercializado, con datos de leucemia mieloide crónica (LMC).
El modelo TxGNN predice que podría ser efectivo para **Sarcoma de Ewing**, con **3 ensayos clínicos registrados** (solo 2 evalúan dasatinib) y **9 publicaciones**, la mayoría preclínicas o de revisión.
La evidencia clínica directa es escasa y una revisión señala que dasatinib **fracasó como agente único** en Ewing y rabdomiosarcoma.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto del registro solo dice "DASATINIB") |
| Nueva Indicación Predicha | Sarcoma de Ewing |
| Puntaje de Predicción TxGNN | 99.90% (posición 1257) |
| Nivel de Evidencia | L2 (con reservas: ensayo Fase 2 completado, no aleatorizado, de múltiples histologías y sin resultados específicos para Ewing) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la ficha del fármaco. Según la información del Evidence Pack, dasatinib es un inhibidor multiquinasa que bloquea BCR-ABL y las quinasas de la familia SRC (también c-KIT y PDGFR). Su eficacia en leucemia mieloide crónica está respaldada por un ECA de Fase 3 (DASISION).

El vínculo con el sarcoma de Ewing es principalmente preclínico. Los estudios muestran que la señalización Src/FAK participa en la invasión, la formación de invadopodios y la migración de las células de Ewing. En líneas celulares, dasatinib tiene actividad antiproliferativa y antimigratoria. Además, inhibe la migración y la invasión en distintas líneas de sarcoma humano.

Sin embargo, la revisión de van Erp et al. (2022) indica que dasatinib como agente único no funcionó en Ewing ni en rabdomiosarcoma en un estudio de Fase 2. El vínculo mecanístico es plausible, pero el beneficio clínico no está confirmado. Las combinaciones (por ejemplo, con inhibidores de FAK o con quimioterapia) son la vía que la literatura propone explorar.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00788125](https://clinicaltrials.gov/study/NCT00788125) | Fase 1/2 | Terminado | 7 | Dasatinib con ifosfamida, carboplatino y etopósido en tumores sólidos pediátricos. Terminó con solo 7 pacientes, por lo que la evidencia es muy limitada. |
| [NCT00464620](https://clinicaltrials.gov/study/NCT00464620) | Fase 2 | Completado | 366 | Dasatinib como agente único en sarcomas avanzados (respuesta y supervivencia libre de progresión a 6 meses). Los resultados específicos de Ewing no están en los datos proporcionados. |
| [NCT06500819](https://clinicaltrials.gov/study/NCT06500819) | Fase 1 | Reclutando | 41 | CAR-T anti-B7-H3 en tumores sólidos pediátricos. No involucra dasatinib y no aporta evidencia para este fármaco. |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35655525](https://pubmed.ncbi.nlm.nih.gov/35655525/) | 2022 | Revisión | Sarcoma | Dasatinib como agente único fracasó en Ewing y rabdomiosarcoma en un estudio de Fase 2. Se revisa el complejo FAK-Src como blanco combinado. |
| [26170970](https://pubmed.ncbi.nlm.nih.gov/26170970/) | 2015 | Revisión | Oncol Lett | Src participa en proliferación, invasión y metástasis, y es un posible blanco en sarcomas. |
| [17363602](https://pubmed.ncbi.nlm.nih.gov/17363602/) | 2007 | Preclínico | Cancer Res | Dasatinib inhibe la migración e invasión en líneas de sarcoma e induce apoptosis en sarcomas óseos dependientes de SRC. |
| [18202781](https://pubmed.ncbi.nlm.nih.gov/18202781/) | 2008 | Preclínico | Oncol Rep | Actividad antiproliferativa y antimigratoria in vitro de dasatinib en líneas de neuroblastoma y sarcoma de Ewing. |
| [27566104](https://pubmed.ncbi.nlm.nih.gov/27566104/) | 2016 | Preclínico | Neoplasia | El estrés microambiental activa invadopodios y migración en Ewing de forma dependiente de Src. |
| [31521948](https://pubmed.ncbi.nlm.nih.gov/31521948/) | 2019 | Preclínico | Neoplasia | Tenascina C y Src cooperan para promover invadopodios en Ewing. |
| [35190971](https://pubmed.ncbi.nlm.nih.gov/35190971/) | 2022 | Revisión | Curr Treat Options Oncol | Terapia sistémica del condrosarcoma. Relación indirecta con el fármaco. |
| [29776413](https://pubmed.ncbi.nlm.nih.gov/29776413/) | 2018 | Preclínico | Cell Commun Signal | Plerixafor promueve la proliferación de líneas de Ewing. No evalúa dasatinib. |
| [32999666](https://pubmed.ncbi.nlm.nih.gov/32999666/) | 2020 | Reporte de caso | Case Rep Oncol | Anomalía cromosómica en crisis blástica de LMC. Sin relación directa con Ewing. |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20002502 | SPRYCEL ® 100 MG TABLETA RECUBIERTA (Bristol Myers Squibb de Colombia S.A.) | Tableta recubierta (vía oral) | Solo figura "DASATINIB"; el registro no detalla la indicación |

Nota: los cinco registros listados en el Evidence Pack son idénticos (mismo número 20002502). Se muestran una sola vez. El total de registros reportado es 20.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor multiquinasa de BCR-ABL y familia SRC) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto (como mínimo, hemograma y función hepática y renal) |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto y las normas institucionales de manejo de antineoplásicos |

## Consideraciones de Seguridad

- **Señales reportadas en la literatura recuperada (en pacientes con LMC, no en Ewing):** derrame pleural, quilotórax, neumonitis intersticial e infecciones de piel y tejidos blandos en adolescentes. Estas señales provienen de reportes y series de casos, y deben confirmarse en el prospecto.

No se dispone de datos de advertencias, contraindicaciones ni interacciones farmacológicas en el Evidence Pack. Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El mecanismo (inhibición de SRC) es plausible y el puntaje TxGNN es alto. Aun así, la evidencia clínica directa es mínima: un ensayo terminado con 7 pacientes y un ensayo Fase 2 de sarcomas mixtos sin resultados específicos de Ewing. La literatura indica además que dasatinib como agente único no funcionó en Ewing.

**Para avanzar se necesita:**
- Resultados por subtipo (Ewing) del ensayo NCT00464620 y de NCT00788125.
- Datos de mecanismo de acción y de seguridad (prospecto de INVIMA, que sigue pendiente).
- Evaluación de estrategias combinadas (por ejemplo, con inhibidores de FAK o con quimioterapia) antes de considerar un estudio clínico.
- Definir la indicación original aprobada en Colombia, ya que el registro solo lista el nombre del fármaco.

*Este informe es solo una referencia de investigación y no constituye consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de cualquier uso.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

