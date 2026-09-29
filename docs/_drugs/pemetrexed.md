---
layout: default
title: Pemetrexed
parent: Solo Predicción del Modelo (L5)
nav_order: 320
evidence_level: L5
indication_count: 10
---

# Pemetrexed
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

# Pemetrexed: De Mesotelioma Pleural a Mesotelioma Peritoneal Maligno

## Resumen en Una Frase

Pemetrexed es un antifolato multidiana usado en quimioterapia, cuya indicación establecida es el mesotelioma pleural (combinado con platino). El modelo TxGNN predice que podría ser efectivo para el **mesotelioma peritoneal maligno**. Esta dirección cuenta con **11 ensayos clínicos** (en su mayoría fase 2, en curso y mezclados con otras histologías) y **20 publicaciones**, casi todas revisiones y estudios retrospectivos.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro INVIMA (el texto de indicación solo dice "PEMETREXED"). La indicación establecida, según el análisis del Evidence Pack, es el mesotelioma pleural. |
| Nueva Indicación Predicha | Mesotelioma peritoneal maligno |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L3 (ver nota abajo) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 5 filas en el registro (corresponden a 2 registros únicos: 20108592 y 20192961) |
| Decisión Recomendada | Proceed with Guardrails |

**Nota sobre el nivel de evidencia:** el Evidence Pack asignó L2. Aplicando las reglas del informe, no hay un ECA de fase 2/3 completado específico para mesotelioma peritoneal. El único estudio de fase 2 completado (NCT00061477) es de un solo brazo y mezcla mesotelioma pleural y peritoneal. La evidencia clínica disponible es sobre todo observacional (estudios retrospectivos), por lo que el nivel es L3.

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos consultada. Según la farmacología conocida, pemetrexed inhibe varias enzimas dependientes de folato: timidilato sintasa, dihidrofolato reductasa y GARFT. Con ello bloquea la síntesis de purinas y pirimidinas en células que se dividen rápido.

El mesotelioma pleural y el peritoneal comparten histología y biología de la vía del folato. Pemetrexed más platino es el tratamiento de primera línea establecido en el mesotelioma pleural, respaldado por un ECA de fase 3 pivotal (PMID 12860938). Por eso extrapolar este esquema al mesotelioma peritoneal es mecanísticamente plausible.

En la práctica, el esquema pemetrexed-platino ya se usa como quimioterapia sistémica de primera línea en el mesotelioma peritoneal avanzado. Los estudios disponibles son retrospectivos y el nivel de evidencia es menor que en el caso pleural. Además, para el mesotelioma peritoneal el tratamiento de elección en pacientes operables es la cirugía citorreductora con HIPEC. La quimioterapia sistémica se usa sobre todo en enfermedad avanzada.

## Evidencia de Ensayos Clínicos

Se muestran los 10 ensayos más relevantes de 11 registrados.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT06057935](https://clinicaltrials.gov/study/NCT06057935) | Fase 2 | Reclutando | 64 | ICARuS II: quimioterapia intraperitoneal frente a intravenosa tras cirugía citorreductora y HIPEC. Aleatorizado; sin resultados aún. |
| [NCT05001880](https://clinicaltrials.gov/study/NCT05001880) | Fase 2 | Reclutando | 66 | Carboplatino, pemetrexed y bevacizumab con o sin atezolizumab. Aleatorizado; sin resultados aún. |
| [NCT03875144](https://clinicaltrials.gov/study/NCT03875144) | Fase 2 | Suspendido | 66 | MESOTIP: PIPAC más quimioterapia sistémica (cisplatino + pemetrexed) frente a quimioterapia sola en primera línea. Objetivo: supervivencia global. |
| [NCT06543069](https://clinicaltrials.gov/study/NCT06543069) | Fase 2 | Reclutando | 28 | Sintilimab y bevacizumab con pemetrexed y cisplatino en enfermedad irresecable. Un solo brazo, muestra pequeña. |
| [NCT04462809](https://clinicaltrials.gov/study/NCT04462809) | Fase 2 | Desconocido | 40 | Talazoparib de mantenimiento tras platino en mesotelioma pleural o peritoneal. Pemetrexed es tratamiento de base, no el fármaco evaluado. |
| [NCT00061477](https://clinicaltrials.gov/study/NCT00061477) | Fase 2 | Completado | 48 | Pemetrexed más gemcitabina en primera línea, mesotelioma pleural o peritoneal. Evalúa seguridad, respuesta y supervivencia. |
| [NCT02535312](https://clinicaltrials.gov/study/NCT02535312) | Fase 1/2 | Activo, sin reclutar | 30 | TRC102 con cisplatino y pemetrexed en tumores sólidos y mesotelioma, incluido el refractario a pemetrexed. |
| [NCT00402766](https://clinicaltrials.gov/study/NCT00402766) | Fase 1 | Completado | 19 | Cisplatino, pemetrexed e imatinib en mesotelioma maligno irresecable o metastásico. Busca la dosis máxima tolerada. |
| [NCT02029690](https://clinicaltrials.gov/study/NCT02029690) | Fase 1 | Terminado | 85 | ADI-PEG 20 con pemetrexed y cisplatino. El mesotelioma peritoneal solo se incluyó en la cohorte de escalada de dosis. |
| [NCT01353482](https://clinicaltrials.gov/study/NCT01353482) | Fase 1/2 | Retirado | 0 | Vorinostat con pemetrexed-cisplatino en mesotelioma pleural. Nunca inscribió pacientes. |

## Evidencia de Literatura

No se identificaron ECA específicos de mesotelioma peritoneal. Se listan los estudios clínicos retrospectivos más directos y revisiones clave.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [28594258](https://pubmed.ncbi.nlm.nih.gov/28594258/) | 2017 | Estudio retrospectivo | Expert Rev Anticancer Ther | Evalúa la eficacia de pemetrexed más cisplatino sistémico en primera línea en mesotelioma peritoneal. |
| [31287877](https://pubmed.ncbi.nlm.nih.gov/31287877/) | 2019 | Estudio clínico (diseño no especificado) | Jpn J Clin Oncol | Eficacia y seguridad de pemetrexed más cisplatino en primera línea en enfermedad avanzada. Señala que no existe quimioterapia estándar establecida. |
| [33743636](https://pubmed.ncbi.nlm.nih.gov/33743636/) | 2021 | Estudio retrospectivo | BMC Cancer | Eficacia de la segunda línea y factores pronósticos, tras el estudio previo de cisplatino-pemetrexed en primera línea. |
| [41133016](https://pubmed.ncbi.nlm.nih.gov/41133016/) | 2025 | Estudio comparativo | Clin Med Insights Oncol | Compara pemetrexed-platino con gemcitabina-platino en primera línea. Pemetrexed-platino es el esquema sistémico más usado. |
| [38806763](https://pubmed.ncbi.nlm.nih.gov/38806763/) | 2024 | Estudio multicéntrico | Ann Surg Oncol | Analiza características, pronóstico y estrategias de tratamiento en esta población rara y heterogénea. |
| [36765620](https://pubmed.ncbi.nlm.nih.gov/36765620/) | 2023 | Revisión | Cancers | Ruta diagnóstica y terapéutica. La supervivencia es mejor con cirugía citorreductora más HIPEC (mediana de 34 a 92 meses). |
| [35407498](https://pubmed.ncbi.nlm.nih.gov/35407498/) | 2022 | Revisión | J Clin Med | Cirugía citorreductora con HIPEC como tratamiento inicial preferido en pacientes seleccionados. |
| [30450291](https://pubmed.ncbi.nlm.nih.gov/30450291/) | 2018 | Revisión | Transl Lung Cancer Res | Revisión general del mesotelioma peritoneal: tumor muy raro y de mal pronóstico. |
| [34723916](https://pubmed.ncbi.nlm.nih.gov/34723916/) | 2022 | Reporte de casos (2 pacientes) | J Immunother | Quimioinmunoterapia en enfermedad no respondedora a platino. Primera descripción de esta combinación en mesotelioma peritoneal. |
| [23291819](https://pubmed.ncbi.nlm.nih.gov/23291819/) | 2013 | Reporte de caso | BMJ Case Rep | Paciente con buena respuesta a la reexposición a cisplatino y pemetrexed tras progresión. |

## Información de Mercado en Colombia

Las 5 filas del registro corresponden a 2 registros sanitarios únicos, por lo que se muestran sin repetir.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20108592 | REVOTRAIN 100 MG | Polvo liofilizado para reconstituir a solución inyectable | PEMETREXED (el registro no detalla la indicación) |
| 20192961 | AUROPEXAFAR® 500 MG | Polvo liofilizado para reconstituir a solución inyectable | PEMETREXED (el registro no detalla la indicación) |

## Citotoxicidad

Esta información proviene de la farmacología general de pemetrexed. El Evidence Pack no incluye datos de toxicidad de DrugBank.

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (antimetabolito, antifolato) |
| Riesgo de Mielosupresión | Alto a medio (neutropenia, trombocitopenia y anemia son frecuentes). Se usa suplementación con ácido fólico y vitamina B12 para reducir la toxicidad. |
| Clasificación de Emetogenicidad | Baja a moderada |
| Items de Monitoreo | Hemograma con diferencial, función renal (aclaramiento de creatinina), función hepática |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

Consultar además las advertencias y precauciones del prospecto.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Pemetrexed más platino está bien establecido en el mesotelioma pleural y se usa de forma consistente en el peritoneal, con respaldo de estudios retrospectivos y varios ensayos de fase 2 en curso. Falta un ECA completado específico para esta indicación, por eso la evidencia es L3 y no permite un "Go" directo.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), que hoy no está disponible en el paquete de evidencia.
- Esperar resultados de ICARuS II (NCT06057935) y del ensayo NCT05001880, ambos aleatorizados y en reclutamiento.
- Confirmar la indicación oficial aprobada por INVIMA, ya que el registro solo consigna "PEMETREXED".
- Definir el papel de pemetrexed frente a la cirugía citorreductora con HIPEC, que es el tratamiento de elección en pacientes operables.
- Plan de monitoreo hematológico y renal, con suplementación de folato y B12.

*Los resultados son solo para referencia de investigación y no constituyen consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

