---
layout: default
title: Paclitaxel
parent: Evidencia Alta (L1-L2)
nav_order: 311
evidence_level: L1
indication_count: 10
---

# Paclitaxel
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

# Paclitaxel: De Indicación No Especificada en el Registro a Carcinoma de Mama Femenino

## Resumen en Una Frase

Paclitaxel es un antineoplásico citotóxico (taxano) que cuenta con registro sanitario vigente en Colombia, pero el texto de indicación aprobada solo repite el nombre del principio activo. El modelo TxGNN predice que podría ser efectivo para **carcinoma de mama femenino**, con **50 ensayos clínicos** y **20 publicaciones** asociados. Es una señal confirmatoria: el cáncer de mama es un uso establecido de paclitaxel, no un reposicionamiento nuevo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro solo dice "PACLITAXEL") |
| Nueva Indicación Predicha | Carcinoma de mama femenino |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, paclitaxel estabiliza los microtúbulos, lo que provoca detención mitótica y apoptosis en células tumorales de rápida división. Ese mecanismo no depende de receptores hormonales ni de dianas específicas.

El cáncer de mama es un escenario de uso consolidado de paclitaxel. La literatura recuperada lo describe como tratamiento de primera línea frecuente y uno de los antineoplásicos más utilizados. Por eso la predicción no representa un hallazgo nuevo, sino que confirma un uso ya establecido. Los ensayos de fase 3 incluyen paclitaxel como parte de esquemas adyuvantes y neoadyuvantes en cáncer de mama.

Como el registro colombiano no detalla la indicación aprobada, conviene verificar en el prospecto de INVIMA si el cáncer de mama figura de forma explícita.

---

## Evidencia de Ensayos Clínicos

Se listan 10 de los 50 ensayos, priorizando fase 3 completados y estudios con paclitaxel como componente directo.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00003088](https://clinicaltrials.gov/study/NCT00003088) | Fase 3 | Completado | 2005 | Doxorrubicina, ciclofosfamida y paclitaxel en esquemas secuenciales o concurrentes, con intervalos de 14 o 21 días, en cáncer de mama con ganglios positivos |
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Fase 3 | Completado | 3270 | Quimioterapia adyuvante (incluye paclitaxel semanal) con o sin trastuzumab en cáncer de mama HER2-bajo |
| [NCT00431080](https://clinicaltrials.gov/study/NCT00431080) | Fase 3 | Completado | 478 | Docetaxel frente a paclitaxel tras FEC en esquema de dosis densa, como adyuvancia en cáncer de mama con ganglios positivos |
| [NCT00513292](https://clinicaltrials.gov/study/NCT00513292) | Fase 3 | Completado | 280 | Comparación de dos secuencias neoadyuvantes (FEC seguido de paclitaxel + trastuzumab, y la secuencia inversa) en cáncer de mama HER2-positivo |
| [NCT00281658](https://clinicaltrials.gov/study/NCT00281658) | Fase 3 | Completado | 444 | Lapatinib + paclitaxel frente a placebo + paclitaxel en cáncer de mama metastásico ErbB2 amplificado |
| [NCT00016276](https://clinicaltrials.gov/study/NCT00016276) | Fase 3 | Terminado | 396 | AC con o sin dexrazoxano, seguido de paclitaxel semanal con o sin trastuzumab, en cáncer de mama HER2+ etapa IIIA/IIIB/IV |
| [NCT00455533](https://clinicaltrials.gov/study/NCT00455533) | Fase 2 | Completado | 384 | Ixabepilona frente a paclitaxel tras AC en cáncer de mama temprano, con biomarcadores |
| [NCT00003992](https://clinicaltrials.gov/study/NCT00003992) | Fase 2 | Completado | 200 | Paclitaxel + trastuzumab adyuvante en cáncer de mama temprano HER2 positivo |
| [NCT00054028](https://clinicaltrials.gov/study/NCT00054028) | Fase 1/2 | Completado | 31 | Suramina combinada con paclitaxel en cáncer de mama metastásico avanzado |
| [NCT01848197](https://clinicaltrials.gov/study/NCT01848197) | No aplica | Desconocido | 1000 | Paclitaxel cada 2 semanas frente a semanal como tratamiento adyuvante |

Algunos ensayos del listado completo no evalúan paclitaxel como intervención principal, por ejemplo los de cuidados de soporte o de otros tipos de cáncer. En varios títulos truncados el papel exacto de paclitaxel no está confirmado.

---

## Evidencia de Literatura

Se listan 10 de las 20 publicaciones. Se excluyen los estudios de laboratorio, salvo dos que ayudan a explicar el mecanismo y la resistencia.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [15305399](https://pubmed.ncbi.nlm.nih.gov/15305399/) | 2004 | ECA | Cancer | Administración concomitante frente a secuencial de epirrubicina y paclitaxel como primera línea en cáncer de mama metastásico (diseño de no inferioridad) |
| [11751485](https://pubmed.ncbi.nlm.nih.gov/11751485/) | 2001 | ECA fase II | Clin Cancer Res | Doxorrubicina seguida de paclitaxel y ciclofosfamida, secuencial frente a concurrente, en adyuvancia con dosis densas (resultados a 5 años) |
| [31783552](https://pubmed.ncbi.nlm.nih.gov/31783552/) | 2019 | Revisión | Biomolecules | Mecanismos de acción de paclitaxel y efectos clínicos en cáncer de mama; la resistencia es una barrera importante |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Revisión | Drug Ther Bull | Revisión de paclitaxel y docetaxel en cáncer de mama y ovario, con la ampliación de la licencia a cáncer de mama metastásico |
| [11147586](https://pubmed.ncbi.nlm.nih.gov/11147586/) | 2000 | Estudio clínico fase II | Cancer | Eficacia y toxicidad de doxorrubicina + paclitaxel en cáncer de mama metastásico; papel del tratamiento previo con antraciclinas |
| [32461977](https://pubmed.ncbi.nlm.nih.gov/32461977/) | 2020 | Estudio de mundo real | Biomed Res Int | Quimioterapia neoadyuvante con epirrubicina/ciclofosfamida y paclitaxel semanal + trastuzumab en cáncer de mama HER2+ |
| [24068539](https://pubmed.ncbi.nlm.nih.gov/24068539/) | 2013 | Fase I-II | Breast Cancer Res Treat | Tipifarnib con paclitaxel semanal y AC en cáncer de mama localmente avanzado |
| [11745249](https://pubmed.ncbi.nlm.nih.gov/11745249/) | 2001 | Estudio clínico | Cancer | Papel de paclitaxel en el tratamiento multimodal del carcinoma inflamatorio de mama |
| [39009452](https://pubmed.ncbi.nlm.nih.gov/39009452/) | 2024 | Mecanismo | J Immunother Cancer | Efecto de paclitaxel sobre macrófagos asociados a tumor y su relación con la potenciación del bloqueo de PD-1 en cáncer de mama triple negativo |
| [24823476](https://pubmed.ncbi.nlm.nih.gov/24823476/) | 2014 | Preclínico/genómico | Nat Commun | Variantes de TEKT4 asociadas a resistencia de cáncer de mama a paclitaxel |

---

## Información de Mercado en Colombia

Los 5 registros mostrados en el paquete de evidencia corresponden al mismo número de registro sanitario. El total reportado es de 20 registros.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19976519 | PACLITAXEL 100 MG SOLUCIÓN INYECTABLE | Solución inyectable | PACLITAXEL (sin indicación descrita; el texto solo repite el nombre del principio activo) |

Fabricante: Fresenius Kabi Oncology Limited (Baddi).

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (taxano, agente antimicrotúbulo) |
| Riesgo de Mielosupresión | Alto según la clase (la neutropenia es habitual y limitante de dosis); el paquete no incluye datos de toxicidad |
| Clasificación de Emetogenicidad | Baja, según la categoría del fármaco |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal, signos de neuropatía periférica y de reacciones de hipersensibilidad |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

Estos datos provienen de la clase farmacológica y no del paquete de evidencia. Consultar las advertencias y precauciones del prospecto.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Los ensayos incluidos señalan la neuropatía periférica inducida por paclitaxel como la principal toxicidad limitante de dosis. Hay estudios de prevención y manejo (NCT07109817, NCT03022162).

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay múltiples ensayos de fase 3 completados con paclitaxel en cáncer de mama (por ejemplo NCT00003088, NCT00431080, NCT00513292 y NCT00281658), lo que sostiene el nivel de evidencia L1. Se avanza con salvaguardas porque no es un reposicionamiento novedoso y porque faltan datos regulatorios y de seguridad locales.

**Para avanzar se necesita:**
- Descargar y revisar el prospecto de INVIMA para confirmar la indicación aprobada en cáncer de mama y obtener advertencias y contraindicaciones (bloqueante para el tamizaje de seguridad)
- Datos del mecanismo de acción desde DrugBank
- Confirmar el rol de paclitaxel en los ensayos con títulos truncados
- Plan de monitoreo hematológico y de neuropatía, y verificación del manejo como fármaco citotóxico
- Las predicciones de menor rango (ER-negativo y ER-positivo en L1; carcinoma de Ehrlich, bilateral, nipple, y los dos rabdomiosarcomas en Hold) requieren evaluación aparte. Los dos rabdomiosarcomas no tienen ninguna evidencia recuperada
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

