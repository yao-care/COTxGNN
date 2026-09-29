---
layout: default
title: Docetaxel
parent: Evidencia Alta (L1-L2)
nav_order: 164
evidence_level: L1
indication_count: 10
---

# Docetaxel
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

# Docetaxel: De Indicación Original No Especificada en el Registro a Carcinoma de Mama Femenino

## Resumen en Una Frase

Docetaxel es un antineoplásico del grupo de los taxanos. El registro sanitario colombiano no especifica su indicación original, ya que el texto solo repite el nombre del fármaco.
El modelo TxGNN predice que podría ser efectivo para **carcinoma de mama femenino**, con **50 ensayos clínicos** y **20 publicaciones** recuperados en esta dirección.
Esta predicción probablemente corresponde a un uso ya establecido y no a un reposicionamiento genuino, por lo que conviene confirmarla contra el prospecto aprobado.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro solo indica "DOCETAXEL") |
| Nueva Indicación Predicha | Carcinoma de mama femenino |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 12 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la farmacología general de la clase, docetaxel es un taxano que estabiliza los microtúbulos y bloquea la mitosis. Esto es relevante para tumores que proliferan rápidamente, como el cáncer de mama.

El registro colombiano tampoco detalla la indicación original, así que no es posible comparar formalmente la indicación de origen con la nueva. Aun así, la evidencia clínica recuperada es directa: hay múltiples ensayos de Fase 3 completados en cáncer de mama, en escenarios adyuvante, neoadyuvante y metastásico. El puntaje muy alto de TxGNN (0.999) coincide con esa evidencia.

Es probable que el cáncer de mama ya sea una indicación aprobada de docetaxel. Por eso, esta señal probablemente no representa un reposicionamiento real. Antes de presentarla como indicación nueva, debe confirmarse contra el prospecto aprobado por INVIMA.

## Evidencia de Ensayos Clínicos

Se listan 10 de los 50 ensayos recuperados, priorizando los de Fase 3 y los que evalúan docetaxel directamente. El paquete no incluye resultados de eficacia, solo los resúmenes de diseño.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00193011](https://clinicaltrials.gov/study/NCT00193011) | Fase 3 | Completado | 150 | Docetaxel semanal vs CMF adyuvante en cáncer de mama de alto riesgo en mujeres >65 años o no candidatas a antraciclinas |
| [NCT00002707](https://clinicaltrials.gov/study/NCT00002707) | Fase 3 | Completado | 2411 | AC preoperatorio con o sin docetaxel (antes o después de la cirugía) en cáncer de mama operable estadio II-III |
| [NCT00431080](https://clinicaltrials.gov/study/NCT00431080) | Fase 3 | Completado | 478 | FE75C en dosis densas con G-CSF seguido de docetaxel vs paclitaxel, adyuvante con ganglios positivos |
| [NCT00089479](https://clinicaltrials.gov/study/NCT00089479) | Fase 3 | Completado | 2611 | Tras AC, docetaxel + capecitabina vs docetaxel solo en cáncer de mama de alto riesgo (supervivencia global) |
| [NCT01354522](https://clinicaltrials.gov/study/NCT01354522) | Fase 3 | Completado | 204 | TAC vs TCX (docetaxel, ciclofosfamida, capecitabina) adyuvante en HER2 negativo de alto riesgo |
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Fase 3 | Completado | 3270 | Quimioterapia adyuvante (docetaxel + ciclofosfamida o AC seguido de paclitaxel semanal) con o sin trastuzumab |
| [NCT02003209](https://clinicaltrials.gov/study/NCT02003209) | Fase 3 | Completado | 315 | Docetaxel, carboplatino, trastuzumab y pertuzumab neoadyuvante, con o sin privación estrogénica, en HR+/HER2+ |
| [NCT00002544](https://clinicaltrials.gov/study/NCT00002544) | Fase 3 | Completado | 300 | Mitoxantrona con o sin docetaxel en cáncer de mama metastásico de mal pronóstico |
| [NCT02748213](https://clinicaltrials.gov/study/NCT02748213) | Fase 2 | Completado | 225 | Trastuzumab + docetaxel con o sin capecitabina en cáncer de mama avanzado HER2 positivo |
| [NCT00025493](https://clinicaltrials.gov/study/NCT00025493) | Fase 2 | Terminado anticipadamente | 27 | Docetaxel en monoterapia en mujeres ≥70 años con cáncer de mama metastásico |

## Evidencia de Literatura

Se listan 10 de las 20 publicaciones, con prioridad para ECA y revisiones. Los hallazgos se resumen solo a partir de los resúmenes disponibles.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [28398846](https://pubmed.ncbi.nlm.nih.gov/28398846/) | 2017 | ECA | J Clin Oncol | Ensayos ABC: docetaxel + ciclofosfamida (TC) por 6 ciclos vs regímenes estándar con antraciclina y taxano en cáncer de mama temprano |
| [11481357](https://pubmed.ncbi.nlm.nih.gov/11481357/) | 2001 | Estudio aleatorizado fase IIb | J Clin Oncol | Doxorrubicina y docetaxel en dosis densas con G-CSF, con o sin tamoxifeno, como terapia preoperatoria |
| [15161988](https://pubmed.ncbi.nlm.nih.gov/15161988/) | 2004 | Revisión | Oncologist | Papel de docetaxel y paclitaxel en cáncer de mama: beneficios en enfermedad metastásica, adyuvante y neoadyuvante |
| [7595719](https://pubmed.ncbi.nlm.nih.gov/7595719/) | 1995 | Revisión | J Clin Oncol | Perfil preclínico y clínico de docetaxel |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Revisión | Drug Ther Bull | Revisión de paclitaxel y docetaxel en cáncer de mama y de ovario |
| [12599222](https://pubmed.ncbi.nlm.nih.gov/12599222/) | 2003 | Ensayo fase 2 | Cancer | Capecitabina con docetaxel y epirrubicina (TEX) en primera línea de cáncer de mama avanzado |
| [16020974](https://pubmed.ncbi.nlm.nih.gov/16020974/) | 2005 | Ensayo fase 2 | Oncology | Docetaxel y gemcitabina semanales en primera línea de cáncer de mama metastásico |
| [15585076](https://pubmed.ncbi.nlm.nih.gov/15585076/) | 2004 | Ensayo fase 2 | Clin Breast Cancer | Docetaxel/cisplatino como quimioterapia primaria en cáncer de mama localmente avanzado |
| [26874836](https://pubmed.ncbi.nlm.nih.gov/26874836/) | 2017 | Estudio clínico | Breast Cancer | Docetaxel, ciclofosfamida y trastuzumab neoadyuvantes en cáncer de mama HER2 positivo |
| [27997437](https://pubmed.ncbi.nlm.nih.gov/27997437/) | 2017 | Cohorte retrospectiva | Anti-Cancer Drugs | Relación entre quimioterapia adyuvante con docetaxel y linfedema asociado al cáncer de mama |

## Información de Mercado en Colombia

Los cinco registros recuperados son entradas idénticas del mismo registro sanitario. Se muestran consolidados en una sola fila; el total reportado es de 12 registros.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19969842 | DOCETAXEL 80 MG INYECTABLE (BLAU FARMACEUTICA COLOMBIA S.A.S) | Solución concentrada para infusión | Sin texto de indicación (solo figura "DOCETAXEL") |

También hay presentaciones registradas como solución inyectable.

## Citotoxicidad

Estos datos provienen de la clase farmacológica y no del paquete de evidencia, que no incluye datos de toxicidad. Deben confirmarse con el prospecto.

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (taxano, antimicrotúbulos) |
| Riesgo de Mielosupresión | Alto (neutropenia es la toxicidad típica de la clase) |
| Clasificación de Emetogenicidad | Baja |
| Items de Monitoreo | Hemograma con diferencial, función hepática, función renal, seguimiento de retención de líquidos y neuropatía periférica |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay varios ensayos de Fase 3 completados en cáncer de mama, lo que da un nivel de evidencia L1, y el puntaje de TxGNN es muy alto. Sin embargo, es probable que esta sea una indicación ya establecida y no un reposicionamiento. Además, falta la información de seguridad del prospecto de INVIMA, que es un vacío bloqueante para el tamizaje de seguridad.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones).
- Confirmar si el cáncer de mama figura en la indicación aprobada del registro 19969842 y en los demás registros.
- Obtener el mecanismo de acción desde DrugBank.
- Obtener los resultados de eficacia de los ensayos de Fase 3 clave, ya que el paquete solo trae los diseños.

Entre las otras predicciones del modelo, sarcoma de Ewing y rabdomiosarcoma tienen evidencia L2, casi siempre en combinación con gemcitabina. La predicción de carcinoma de pulmón de células pequeñas parece un desajuste de mapeo, pues la evidencia recuperada corresponde a cáncer de pulmón de células no pequeñas. Los resultados de este informe son solo para investigación y no constituyen consejo médico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

