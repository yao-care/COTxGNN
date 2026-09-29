---
layout: default
title: Pertuzumab
parent: Evidencia Alta (L1-L2)
nav_order: 323
evidence_level: L1
indication_count: 10
---

# Pertuzumab
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

# Pertuzumab: De Combinación Pertuzumab/Trastuzumab (texto del registro INVIMA) a Cáncer de Mama Positivo para Receptor de Progesterona

## Resumen en Una Frase

Pertuzumab es un anticuerpo monoclonal anti-HER2 comercializado en Colombia, sobre todo en la combinación fija subcutánea con trastuzumab (Phesgo). El modelo TxGNN predice que podría ser efectivo para **cáncer de mama positivo para receptor de progesterona**, con **10 ensayos clínicos** y **20 publicaciones** que respaldan esta dirección. Esta predicción es en realidad un subtipo de receptor dentro del cáncer de mama HER2-positivo, donde pertuzumab ya es una terapia establecida.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Pertuzumab y trastuzumab (el texto del registro solo indica los principios activos, no una indicación clínica detallada) |
| Nueva Indicación Predicha | Cáncer de mama positivo para receptor de progesterona |
| Puntaje de Predicción TxGNN | 99.93% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la fuente de fármacos. Según la información del análisis de reposicionamiento, pertuzumab se une al subdominio II de HER2 y bloquea su dimerización con HER3. Esto suprime las vías de señalización PI3K/AKT y MAPK.

El beneficio de pertuzumab depende del estado de HER2, no del estado del receptor de progesterona (RP). Los tumores RP-positivos son un subconjunto de receptores hormonales dentro del cáncer de mama HER2-positivo (HR+/HER2+). Por eso el puntaje alto de TxGNN es coherente con la práctica clínica actual, pero la "nueva indicación" es una etiqueta de subtipo y no una enfermedad distinta.

Existe además una base biológica para combinar el bloqueo de HER2 con terapia endocrina. Hay comunicación cruzada entre las vías de HER2 y del receptor de estrógeno. Los estudios en tumores HR+/HER2+ exploran pertuzumab más trastuzumab con inhibidores de aromatasa, terapia endocrina o inhibidores de CDK4/6.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04629846](https://clinicaltrials.gov/study/NCT04629846) | Fase 3 | Completado | 517 | Biosimilar QL1209 vs. pertuzumab de referencia, con trastuzumab y docetaxel, en cáncer de mama temprano o localmente avanzado HER2+ y RE/RP negativo |
| [NCT05802225](https://clinicaltrials.gov/study/NCT05802225) | Fase 3 | Activo, sin reclutamiento | 398 | Biosimilar BCD-178 vs. Perjeta como terapia neoadyuvante en HER2+ |
| [NCT03726879](https://clinicaltrials.gov/study/NCT03726879) | Fase 3 | Completado | 454 | IMpassion050: atezolizumab vs. placebo con quimioterapia neoadyuvante seguida de paclitaxel + trastuzumab + pertuzumab (se recomienda verificar el brazo de fármaco, pues el título está truncado) |
| [NCT00545688](https://clinicaltrials.gov/study/NCT00545688) | Fase 2 | Completado | 417 | Compara la respuesta patológica completa de cuatro combinaciones de trastuzumab, docetaxel y pertuzumab (probable diseño NeoSphere) |
| [NCT02326974](https://clinicaltrials.gov/study/NCT02326974) | Fase 2 | Activo, sin reclutamiento | 164 | T-DM1 con pertuzumab en el preoperatorio; efecto de la heterogeneidad de HER2 |
| [NCT02689921](https://clinicaltrials.gov/study/NCT02689921) | Fase 2 | Desconocido | 7 | Inhibidor de aromatasa con pertuzumab/trastuzumab, sin quimioterapia, en HR+/HER2+ (muestra muy pequeña) |
| [NCT04675827](https://clinicaltrials.gov/study/NCT04675827) | Fase 2 | Terminado | 139 | DECRESCENDO: desescalada de quimioterapia con pertuzumab/trastuzumab subcutáneo en HER2+ y RE-negativo |

*Se omitieron tres ensayos de esta lista de 10 por no aportar evidencia de pertuzumab: NCT06131424 (estudio retrospectivo de prevalencia de HER2-bajo), NCT03058939 (retirado, 0 participantes) y NCT00999804 (basado en lapatinib, sin pertuzumab claro).*

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | ECA | Ann Oncol | WSG-ADAPT HER2+/HR-: 12 semanas de bloqueo dual con trastuzumab y pertuzumab ± paclitaxel semanal, con análisis de eficacia, seguridad y marcadores predictivos |
| [37166817](https://pubmed.ncbi.nlm.nih.gov/37166817/) | 2023 | ECA | JAMA Oncol | WSG-TP-II: terapia endocrina más trastuzumab y pertuzumab vs. quimioterapia desescalada en cáncer de mama temprano HR+/HER2+ |
| [38906970](https://pubmed.ncbi.nlm.nih.gov/38906970/) | 2024 | ECA | Br J Cancer | El biosimilar QL1209 fue evaluado frente a pertuzumab de referencia en tratamiento neoadyuvante HER2+ y RE/RP negativo (equivalencia, Fase 3) |
| [30106636](https://pubmed.ncbi.nlm.nih.gov/30106636/) | 2018 | ECA Fase 2 | J Clin Oncol | PERTAIN: trastuzumab más inhibidor de aromatasa, con o sin pertuzumab, en primera línea HER2+ y HR+ metastásico o localmente avanzado |
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | ECA Fase 2 | Lancet Oncol | NeoSphere a 5 años: supervivencia libre de progresión, supervivencia libre de enfermedad y seguridad con pertuzumab y trastuzumab neoadyuvantes |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Guía | J Clin Oncol | Actualización de la guía ASCO sobre terapia sistémica en cáncer de mama avanzado HER2-positivo |
| [40246081](https://pubmed.ncbi.nlm.nih.gov/40246081/) | 2025 | Retrospectivo | Mod Pathol | Estudio multicéntrico sobre el efecto del estado de receptores hormonales y de la expresión de HER2 en la respuesta neoadyuvante |
| [27057657](https://pubmed.ncbi.nlm.nih.gov/27057657/) | 2016 | Revisión | Cancer Treat Rev | Panorama del cáncer de mama HR+/HER2+ y de la comunicación cruzada entre ambas vías |
| [40983817](https://pubmed.ncbi.nlm.nih.gov/40983817/) | 2025 | Revisión | Breast Cancer | Avances en las interacciones de señalización y la traslación clínica en HR+/HER2+ |
| [33662161](https://pubmed.ncbi.nlm.nih.gov/33662161/) | 2021 | Revisión | Eur J Clin Invest | Inhibidores de CDK4/6 y PI3K como opción para HER2+, con base en la interacción entre las vías de ER y HER2 |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20195976 | PHESGO® 600MG/600MG (F. Hoffmann-La Roche Ltd) | Solución inyectable | Pertuzumab y trastuzumab |

Se registran 20 registros en total, pero los cinco primeros son entradas duplicadas del mismo registro 20195976. Además, existe una forma farmacéutica de solución concentrada para infusión.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (anticuerpo monoclonal anti-HER2), no citotóxico convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto. En los esquemas combinados, la mielosupresión suele estar asociada a la quimioterapia acompañante (por ejemplo, docetaxel) |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Función cardíaca (fracción de eyección del ventrículo izquierdo, FEVI), hemograma, función hepática y renal |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto y las normas institucionales de manejo de medicamentos peligrosos |

*La información sobre monitoreo se basa en el guardarraíl del análisis de reposicionamiento (confirmar HER2 y vigilar FEVI) y en criterios generales de la clase. No proviene de datos de toxicidad de la fuente.*

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay varios ensayos de Fase 3 completados y ensayos aleatorizados con pertuzumab en cáncer de mama HER2-positivo, lo que da un nivel de evidencia L1. Sin embargo, el efecto depende de HER2 y no del receptor de progesterona, por lo que la predicción es una etiqueta de subtipo dentro de una indicación ya establecida. Además, la evidencia específica en HR+/HER2+ proviene sobre todo de estudios de Fase 2.

**Para avanzar se necesita:**
- Restringir el uso a tumores con HER2 positivo confirmado y valorar terapia endocrina concomitante.
- Vigilar la función cardíaca (FEVI) durante el tratamiento.
- Obtener del prospecto de INVIMA las advertencias, contraindicaciones e interacciones, que hoy faltan y bloquean el análisis de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Verificar el brazo de fármaco de los ensayos con título truncado (por ejemplo, NCT03726879).

Nota: el resto de las predicciones tiene menos respaldo. Otros subtipos de cáncer de mama (rangos 2 y 4) están en nivel L2 como pregunta de investigación. Las predicciones de rangos 5 a 10 (tumores raros y de vías urinarias) están en nivel L4-L5 y se mantienen en Hold, sin evidencia clínica ni de literatura que las respalde.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

