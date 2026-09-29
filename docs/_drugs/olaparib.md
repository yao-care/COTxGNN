---
layout: default
title: Olaparib
parent: Solo Predicción del Modelo (L5)
nav_order: 303
evidence_level: L5
indication_count: 1
---

# Olaparib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Olaparib: De Inhibidor de PARP (Indicación Original No Especificada en el Registro) a Carcinoma de Mama Femenino

## Resumen en Una Frase

Olaparib es un inhibidor de PARP de administración oral, comercializado en Colombia como Lynparza® 150 mg (AstraZeneca). El registro sanitario solo consigna el nombre del principio activo, sin texto de indicación.
El modelo TxGNN predice que podría ser efectivo para **carcinoma de mama femenino**, con un puntaje de **99.09%**.
Lo respaldan **51 ensayos clínicos** registrados y **20 publicaciones**. La evidencia más sólida viene de los ensayos de Fase 3 OlympiA y OlympiAD, y el beneficio se limita a pacientes con mutaciones germinales BRCA1/2 y enfermedad HER2 negativa.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro colombiano (el texto registrado solo dice «OLAPARIB») |
| Nueva Indicación Predicha | Carcinoma de mama femenino |
| Puntaje de Predicción TxGNN | 99.09% |
| Nivel de Evidencia | L1 (basado en la literatura de ECA de Fase 3; ver nota abajo) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Proceed with Guardrails |

> **Nota sobre el nivel L1:** los ensayos de Fase 3 listados con número NCT son en su mayoría de cáncer de ovario o estudios de extensión. La clasificación L1 se apoya principalmente en las publicaciones de los ECA de Fase 3 OlympiA y OlympiAD, no en los registros NCT.

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los campos suministrados. Según la literatura citada, olaparib inhibe PARP1/2 y atrapa la enzima PARP sobre el ADN. En tumores con mutaciones germinales en BRCA1/BRCA2, la reparación por recombinación homóloga está deficiente. Las roturas de cadena sencilla no reparadas se convierten en roturas de doble cadena en las horquillas de replicación, lo que produce letalidad sintética.

Como BRCA1 y BRCA2 son genes de susceptibilidad al cáncer de mama y ovario, la vulnerabilidad que explota el fármaco existe también en los tumores de mama con esas mutaciones. Este mecanismo es coherente con el puntaje alto de TxGNN.

El beneficio está restringido por biomarcadores: mutación germinal BRCA1/2 y enfermedad HER2 negativa. No se ha demostrado para el cáncer de mama en general. Algunos estudios exploran poblaciones con deficiencia de recombinación homóloga (HRD) sin mutación germinal BRCA, con resultados aún preliminares.

---

## Evidencia de Ensayos Clínicos

De los 51 ensayos identificados, se listan los 10 con mayor relevancia para cáncer de mama.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00679783](https://clinicaltrials.gov/study/NCT00679783) | Fase 2 | Completado | 99 | Estudio no aleatorizado de olaparib (AZD2281) en cáncer de mama y ovario recurrente, con mutación BRCA o triple negativo. Evalúa tasa de respuesta y marcadores. Evidencia directa, pero sin grupo control |
| [NCT05498155](https://clinicaltrials.gov/study/NCT05498155) | Fase 2 | Activo, sin reclutar | 50 | Olaparib solo o con durvalumab como terapia neoadyuvante en cáncer de mama temprano HER2 negativo con mutación BRCA |
| [NCT02418624](https://clinicaltrials.gov/study/NCT02418624) | Fase 1 | Completado | 25 | Carboplatino-olaparib seguido de olaparib frente a capecitabina en cáncer de mama avanzado BRCA1/2, HER2 negativo, primera línea |
| [NCT01116648](https://clinicaltrials.gov/study/NCT01116648) | Fase 1/2 | Activo, sin reclutar | 155 | Cediranib con olaparib frente a olaparib solo en cáncer de ovario recurrente o cáncer de mama triple negativo recurrente |
| [NCT01445418](https://clinicaltrials.gov/study/NCT01445418) | Fase 1 | Completado | 103 | Olaparib con carboplatino en cáncer de mama y ovario con mutación BRCA1/2 o mama triple negativo esporádico |
| [NCT03109080](https://clinicaltrials.gov/study/NCT03109080) | Fase 1 | Completado | 24 | Olaparib con radioterapia en cáncer de mama triple negativo inflamatorio, localmente avanzado, metastásico o con enfermedad residual |
| [NCT02208375](https://clinicaltrials.gov/study/NCT02208375) | Fase 1 | Activo, sin reclutar | 159 | Olaparib con vistusertib o capivasertib en cáncer recurrente de endometrio, mama triple negativo y ovario |
| [NCT04330040](https://clinicaltrials.gov/study/NCT04330040) | Fase 4 | Completado | 202 | Estudio poscomercialización en India, en ovario platino-sensible y cáncer de mama metastásico con mutación germinal BRCA1/2 |
| [NCT07187674](https://clinicaltrials.gov/study/NCT07187674) | N/A | Aún no reclutando | 20 | Estudio exploratorio de un solo brazo: QL1706 con olaparib y paclitaxel, neoadyuvante en cáncer de mama triple negativo HRD positivo |
| [NCT05209529](https://clinicaltrials.gov/study/NCT05209529) | Fase 2 | Retirado | 0 | Olaparib con o sin durvalumab neoadyuvante en cáncer de mama triple negativo asociado a BRCA. Nunca inscribió pacientes |

Varios ensayos de Fase 3 listados (por ejemplo NCT02282020 y NCT03402841) corresponden a cáncer de ovario y no se cuentan como evidencia directa en mama.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [34081848](https://pubmed.ncbi.nlm.nih.gov/34081848/) | 2021 | ECA (Fase 3) | N Engl J Med | OlympiA: olaparib adyuvante en cáncer de mama temprano con mutación BRCA1/2 |
| [36228963](https://pubmed.ncbi.nlm.nih.gov/36228963/) | 2022 | ECA (Fase 3) | Ann Oncol | Análisis de supervivencia global de OlympiA: olaparib adyuvante frente a placebo en cáncer de mama temprano de alto riesgo con variantes germinales BRCA1/2 |
| [28578601](https://pubmed.ncbi.nlm.nih.gov/28578601/) | 2017 | ECA (Fase 3) | N Engl J Med | OlympiAD: olaparib en cáncer de mama metastásico con mutación germinal BRCA |
| [30689707](https://pubmed.ncbi.nlm.nih.gov/30689707/) | 2019 | ECA (Fase 3) | Ann Oncol | OlympiAD, supervivencia global final y tolerabilidad frente a quimioterapia a elección del médico |
| [36893711](https://pubmed.ncbi.nlm.nih.gov/36893711/) | 2023 | ECA (Fase 3) | Eur J Cancer | OlympiAD con seguimiento extendido. En el análisis final la mediana de supervivencia global fue 19.3 meses con olaparib frente a 17.1 con quimioterapia (P = 0.513) |
| [33119476](https://pubmed.ncbi.nlm.nih.gov/33119476/) | 2020 | Fase 2, un brazo | J Clin Oncol | TBCRC 048: olaparib en cáncer de mama metastásico con mutaciones somáticas BRCA1/2 o en otros genes de recombinación homóloga |
| [34143979](https://pubmed.ncbi.nlm.nih.gov/34143979/) | 2021 | Fase 2 aleatorizado | Cancer Cell | I-SPY2: durvalumab, olaparib y paclitaxel elevaron la tasa de respuesta patológica completa en cáncer de mama HER2 negativo (del 20% al 37%) |
| [39520738](https://pubmed.ncbi.nlm.nih.gov/39520738/) | 2024 | Fase 2 | Breast | NOBROLA: olaparib en cáncer de mama triple negativo avanzado con HRD y sin mutación germinal BRCA1/2 |
| [38112922](https://pubmed.ncbi.nlm.nih.gov/38112922/) | 2024 | Fase 3b, mundo real | Breast Cancer Res Treat | LUCY, análisis final de supervivencia global y seguridad en cáncer de mama metastásico BRCA mutado, HER2 negativo |
| [33710534](https://pubmed.ncbi.nlm.nih.gov/33710534/) | 2021 | Revisión | Target Oncol | Panorama de los inhibidores de PARP (olaparib y talazoparib) en cáncer de mama con mutación germinal BRCA, HER2 negativo |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20124752 | LYNPARZA® 150 MG (AstraZeneca Colombia S.A.S.) | Tableta recubierta (oral) | No especificada; el registro solo indica «OLAPARIB» |

Los datos muestran 20 registros en total, pero las entradas disponibles corresponden todas al mismo número de registro sanitario, por lo que se presenta una sola fila.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de PARP) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma completo y funciones hepática y renal; ajustar según el prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Los ECA de Fase 3 OlympiA (adyuvante) y OlympiAD (metastásico) respaldan a olaparib en cáncer de mama con mutación germinal BRCA1/2 y HER2 negativo, y el mecanismo de letalidad sintética es coherente. Sin embargo, el beneficio se limita a esa población, la lista de ensayos NCT es mayormente no específica de mama y faltan los datos de seguridad locales.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA para advertencias y contraindicaciones, requisito previo al tamizaje de seguridad.
- Confirmar si la indicación de mama figura en el registro sanitario colombiano, ya que el texto registrado solo dice «OLAPARIB».
- Obtener el mecanismo de acción desde DrugBank para completar el análisis mecanístico.
- Definir criterios de selección por biomarcadores (mutación germinal BRCA1/2, HER2 negativo) y disponibilidad de pruebas genéticas.
- Completar la evaluación de relevancia de los ensayos y publicaciones pendientes, y verificar los títulos truncados.
- Aclarar el beneficio en pacientes sin mutación germinal BRCA (HRD, triple negativo), donde los datos aún son preliminares.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

