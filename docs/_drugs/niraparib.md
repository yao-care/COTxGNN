---
layout: default
title: Niraparib
parent: Solo Predicción del Modelo (L5)
nav_order: 469
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Niraparib: nueva indicación predicha, Neoplasia quística (cystic neoplasm) (nivel de evidencia L5). Indicación original: No especificada"
monitor_inn: "niraparib"
predicted_indications: ["epiglottis neoplasm", "cystic neoplasm", "benign neoplasm of hypopharynx", "benign neoplasm of tongue", "benign neoplasm of floor of mouth", "cervical neuroblastoma", "tumor of testis and paratestis", "inner ear neoplasm", "pre-malignant neoplasm", "schwannoma of jugular foramen"]
---

# Niraparib
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

# Niraparib: De Indicación Original (no especificada) a Neoplasia Quística

## Resumen en Una Frase

Niraparib es un inhibidor de PARP que contó con un registro sanitario en Colombia (hoy cancelado), cuyo texto de indicación solo consigna el nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para **neoplasia quística**, con **3 ensayos clínicos** (todos en cáncer endometrial seroso o de alto grado) y **10 publicaciones** centradas sobre todo en carcinoma seroso de ovario, que respaldan esta dirección solo de forma indirecta.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro solo indica "NIRAPARIB") |
| Nueva Indicación Predicha | Neoplasia quística (cystic neoplasm) |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 según la regla estricta (ningún ECA de Fase 3 completado); el análisis de evidencia le asigna L2 por la existencia de ensayos de Fase 2 |
| Estado de Mercado en Colombia | Solo cancelado (sin registros vigentes) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

> **Nota sobre la indicación predicha:** la primera predicción por puntaje (neoplasia de epiglotis) no tiene ningún ensayo ni publicación. Este informe se centra en la segunda predicción (neoplasia quística), que es la única con evidencia disponible. Las demás predicciones (rangos 3 a 10) no cuentan con evidencia clínica ni bibliográfica.

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, niraparib inhibe PARP1/2 y causa letalidad sintética en tumores con deficiencia de recombinación homóloga (HRD), como el carcinoma seroso de ovario de alto grado con mutación de BRCA o HRD positivo.

La literatura recuperada se centra en carcinomas serosos de ovario y endometrio (pruebas de HRD, resistencia a inhibidores de PARP por metilación de RAD51C, mantenimiento con niraparib). Estos tumores son de tipo seroso o quístico, por lo que el vínculo con la etiqueta amplia "neoplasia quística" es **indirecto** y pasa por la histología serosa.

Niraparib ya está aprobado en otros países como mantenimiento en cáncer de ovario. Por ello, esta predicción es más una extensión a histologías ginecológicas relacionadas que un reposicionamiento genuino. La similitud con la indicación original no pudo evaluarse.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04716686](https://clinicaltrials.gov/study/NCT04716686) | Fase 2 | Reclutando | 83 | Niraparib en monoterapia como mantenimiento y tratamiento de recurrencia en carcinoma seroso de endometrio; estudio multicéntrico, abierto (relevancia A) |
| [NCT04159155](https://clinicaltrials.gov/study/NCT04159155) | Fase 2/3 | Terminado | 11 | Ensayo canadiense aleatorizado multibrazo en cáncer de endometrio seroso o con p53 mutante; terminado con solo 11 participantes, aporta pocos datos de eficacia (relevancia B) |
| [NCT05289648](https://clinicaltrials.gov/study/NCT05289648) | Fase temprana 1 | Retirado | 0 | Niraparib preoperatorio en cáncer de endometrio de alto grado; retirado sin inscripción, sin datos (relevancia C) |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [40473279](https://pubmed.ncbi.nlm.nih.gov/40473279/) | 2025 | Protocolo de ensayo Fase 2 | BMJ Open | Protocolo de mantenimiento con niraparib en carcinoma seroso uterino en estadio III/IV, recurrente sin quimioterapia previa o recurrente sensible a platino |
| [41323499](https://pubmed.ncbi.nlm.nih.gov/41323499/) | 2025 | Cohorte | Pathol Oncol Res | El perfil genómico integral (FoundationOne CDx) para HRD orienta las recomendaciones de inhibidores de PARP en cáncer de ovario seroso de alto grado |
| [42157333](https://pubmed.ncbi.nlm.nih.gov/42157333/) | 2026 | Cohorte | Clin Epigenetics | Nomograma basado en metilación de promotores de genes HRR para predecir eficacia de inhibidores de PARP y supervivencia libre de progresión |
| [42442041](https://pubmed.ncbi.nlm.nih.gov/42442041/) | 2026 | Cohorte | Gynecol Oncol | Utilidad de las pruebas de HRD en carcinoma seroso de alto grado BRCA salvaje; la amplificación de MYC como posible marcador sustituto |
| [40702505](https://pubmed.ncbi.nlm.nih.gov/40702505/) | 2025 | Cohorte | J Ovarian Res | Subtipos basados en células madre tumorales y modelo pronóstico en cáncer de ovario seroso de alto grado |
| [41520277](https://pubmed.ncbi.nlm.nih.gov/41520277/) | 2026 | Preclínico | Cancer Biol Ther | Eficacia de carboplatino combinado con inhibidores de PARP en esferoides y organoides de carcinoma seroso de alto grado |
| [41465250](https://pubmed.ncbi.nlm.nih.gov/41465250/) | 2025 | Preclínico | Int J Mol Sci | Efectos poli-farmacológicos de los inhibidores de PARP mediante proteómica global en células de cáncer de ovario seroso |
| [41214101](https://pubmed.ncbi.nlm.nih.gov/41214101/) | 2025 | Preclínico | Sci Rep | Claudina-4 como regulador de la estabilidad genómica y la evasión inmune en carcinoma seroso de alto grado |
| [34321239](https://pubmed.ncbi.nlm.nih.gov/34321239/) | 2021 | Preclínico | Cancer Res | La pérdida adquirida de metilación del promotor de RAD51C causa resistencia a inhibidores de PARP en carcinoma seroso de ovario |
| [31466953](https://pubmed.ncbi.nlm.nih.gov/31466953/) | 2019 | Reporte de caso | BMJ Case Rep | Niraparib como terapia de mantenimiento en una paciente con cáncer de ovario y metástasis cerebrales |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20213253 (cancelado) | ZEJULA® 100 MG TABLETAS RECUBIERTAS | Tableta recubierta | NIRAPARIB (el registro no detalla la indicación) |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de PARP) |
| Riesgo de Mielosupresión | Medio a alto; la mielosupresión (por ejemplo, trombocitopenia, anemia, neutropenia) es una toxicidad conocida de la clase. Consultar el prospecto para detalles |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma completo con diferencial, presión arterial, función hepática y renal |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto y las regulaciones locales de manejo de antineoplásicos orales |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas:** se identificaron 351 interacciones registradas. Entre las mostradas hay interacciones de nivel **Mayor** con deferiprona y samario (153Sm) lexidronam, probablemente por efectos mielosupresores aditivos. Hay numerosas interacciones de nivel **Moderado**, entre ellas:
  - Anticoagulantes y antiagregantes: ácido acetilsalicílico, apixabán, betrixabán, bivalirudina, cangrelor, cilostazol, dipiridamol, abciximab, alteplasa, antitrombina III y caplacizumab.
  - Radiofármacos y anticuerpos radiomarcados: iobenguano (I-131), ibritumomab tiuxetán, tositumomab (con y sin I-131) y cloruro de estroncio Sr-89.
  - Otros: rolapitant y palifermina.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia es indirecta: los ensayos son de Fase 2 (uno reclutando, uno terminado con muy pocos participantes y uno retirado) y están centrados en carcinoma seroso endometrial, no en "neoplasia quística" como entidad. Además, el único registro sanitario en Colombia está cancelado y faltan datos de seguridad y de mecanismo de acción.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto del INVIMA para completar advertencias y contraindicaciones (brecha de datos bloqueante para el tamizaje de seguridad).
- Obtener los datos del mecanismo de acción desde DrugBank.
- Definir con precisión qué tipo de neoplasia quística o serosa se busca tratar y evaluar su relación con HRD.
- Esperar los resultados del ensayo NCT04716686 (Fase 2, finalización prevista a fines de 2026).
- Aclarar la situación regulatoria en Colombia (registro cancelado) y evaluar la viabilidad de un nuevo registro.
- Evaluar con rigor la relación riesgo-beneficio, dada la mielosupresión y las múltiples interacciones.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

