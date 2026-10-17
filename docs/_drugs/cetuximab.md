---
layout: default
title: Cetuximab
parent: Solo Predicción del Modelo (L5)
nav_order: 149
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Cetuximab: nueva indicación predicha, Condroide hamartoma (nivel de evidencia L5). Indicación original: CETUXIMAB"
monitor_inn: "CETUXIMAB"
predicted_indications: ["chondroid hamartoma", "non-seminomatous lesion", "ductal or ductular proliferation", "bronchial adenomas/carcinoids childhood", "tumor of testis and paratestis", "odontogenic cyst", "thyroglossal duct cyst", "cystic neoplasm", "epiglottis neoplasm", "pre-malignant neoplasm"]
---

# Cetuximab
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

# Cetuximab: De Cetuximab (indicación registrada sin detallar) a Condroide Hamartoma

## Resumen en Una Frase

Cetuximab es un anticuerpo monoclonal que bloquea el receptor del factor de crecimiento epidérmico (EGFR), usado en cáncer colorrectal metastásico y cáncer de cabeza y cuello de células escamosas.
El modelo TxGNN predice que podría ser efectivo para **condroide hamartoma**, pero no existen **ensayos clínicos** ni **publicaciones** que respalden esta predicción concreta.
Otras predicciones del mismo modelo tienen algo más de apoyo (por ejemplo, lesiones premalignas y neoplasias quísticas), y se comentan más abajo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | CETUXIMAB (el registro sanitario solo repite el nombre del fármaco, sin indicación detallada) |
| Nueva Indicación Predicha | Condroide hamartoma |
| Puntaje de Predicción TxGNN | 99.95% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registro vigente) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados no incluyen el mecanismo de acción detallado. Según la información farmacológica disponible, cetuximab es un anticuerpo que se une al EGFR y bloquea su señalización. Se usa en cáncer colorrectal metastásico con expresión de EGFR cuando otras quimioterapias no han funcionado, y en cáncer de cabeza y cuello de origen escamoso, en combinación con radioterapia.

Para el condroide hamartoma, una lesión benigna, **no se ha establecido un vínculo mecanístico**. No hay datos que demuestren dependencia de EGFR en esta enfermedad, por lo que el puntaje alto proviene únicamente de la predicción del modelo. La similitud con la indicación original queda pendiente de evaluar.

Otras predicciones del mismo análisis tienen una base algo mejor, aunque todas son indirectas:
- **Neoplasia premaligna** (L2): EGFR está sobreexpresado en lesiones premalignas del tracto aerodigestivo superior y existe un ensayo de Fase 2 completado con cetuximab en monoterapia (NCT00524017), sin resultados disponibles.
- **Neoplasia quística** (L3): la evidencia se centra en carcinoma adenoide quístico y carcinomas de glándulas salivales, con un estudio de Fase 2 (PMID 18804410).
- **Proliferación ductal o ductular** (L4): la literatura trata sobre todo del adenocarcinoma ductal de páncreas, donde los tumores con mutación de KRAS suelen resistir a los anticuerpos anti-EGFR, por lo que el vínculo es indirecto.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para condroide hamartoma.

Como referencia, estos son los ensayos asociados a las predicciones con mayor respaldo:

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00524017](https://clinicaltrials.gov/study/NCT00524017) | Fase 2 | Completado | 35 | Cetuximab en monoterapia en lesiones premalignas de alto riesgo del tracto aerodigestivo superior (neoplasia premaligna). No se proporcionaron resultados |
| [NCT01192087](https://clinicaltrials.gov/study/NCT01192087) | Fase 1/2 | Desconocido | 49 | Cetuximab con IMRT y refuerzo de iones de carbono en carcinoma adenoide quístico (neoplasia quística) |
| [NCT00397384](https://clinicaltrials.gov/study/NCT00397384) | Fase 1 | Completado | 43 | Erlotinib más cetuximab en cáncer avanzado; relación indirecta (neoplasia quística) |
| [NCT00101348](https://clinicaltrials.gov/study/NCT00101348) | Fase 1/2 | Completado | 66 | Erlotinib, cetuximab y bevacizumab en tumores sólidos; relación limitada |
| [NCT01637194](https://clinicaltrials.gov/study/NCT01637194) | Fase 1 | Completado | 12 | Cetuximab más everolimus en tumores sólidos; muestra pequeña |
| [NCT00482222](https://clinicaltrials.gov/study/NCT00482222) | Fase 3 | Desconocido | 340 | Oxaliplatino/fluoropirimidina con o sin cetuximab en metástasis hepáticas colorrectales resecables; relevancia débil |
| [NCT00719199](https://clinicaltrials.gov/study/NCT00719199) | Fase 1 | Terminado | 21 | FOLFIRI, cetuximab e IMO-2055 en cáncer colorrectal; no es enfermedad premaligna |
| [NCT00537823](https://clinicaltrials.gov/study/NCT00537823) | Fase 2 | Terminado | 9 | Neoadyuvancia con FOLFOX antes de resección hepática; no se relaciona con cetuximab en lesiones premalignas |

---

## Evidencia de Literatura

No hay literatura disponible para condroide hamartoma. Como referencia, esta es la literatura más relevante de las otras predicciones:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [18804410](https://pubmed.ncbi.nlm.nih.gov/18804410/) | 2009 | Ensayo Fase 2 | Oral Oncology | Cetuximab en carcinomas de glándulas salivales recurrentes o metastásicos (30 pacientes, 23 con carcinoma adenoide quístico); se evaluó el beneficio clínico |
| [35300246](https://pubmed.ncbi.nlm.nih.gov/35300246/) | 2022 | ECA Fase 2 | Clin Transl Radiat Oncol | Cetuximab, gemcitabina y radioterapia en cáncer de páncreas localmente avanzado (estudio PARC), resultados a largo plazo |
| [24412287](https://pubmed.ncbi.nlm.nih.gov/24412287/) | 2014 | Revisión | Oral Oncology | Papel de EGFR en la quimioprevención del cáncer de cabeza y cuello; las lesiones orales premalignas sobreexpresan EGFR |
| [33243986](https://pubmed.ncbi.nlm.nih.gov/33243986/) | 2020 | Revisión | Nat Rev Dis Primers | Panorama del carcinoma de células escamosas de cabeza y cuello |
| [21552097](https://pubmed.ncbi.nlm.nih.gov/21552097/) | 2012 | Fase 2 | Am J Clin Oncol | Gemcitabina, oxaliplatino y cetuximab en cáncer de páncreas avanzado |
| [22571859](https://pubmed.ncbi.nlm.nih.gov/22571859/) | 2012 | Estudio clínico | Ann Oncol | Cetuximab neoadyuvante, gemcitabina e IMRT en adenocarcinoma de páncreas |
| [27797376](https://pubmed.ncbi.nlm.nih.gov/27797376/) | 2017 | Preclínico | Oncogene | Mecanismo de resistencia a cetuximab en adenocarcinoma ductal de páncreas por señalización de integrina β1 |
| [30141310](https://pubmed.ncbi.nlm.nih.gov/30141310/) | 2018 | Cohorte | Asian Pac J Cancer Prev | Trastornos cutáneos y localización del tumor como factores pronósticos en cáncer colorrectal tratado con cetuximab |
| [21234529](https://pubmed.ncbi.nlm.nih.gov/21234529/) | 2011 | Cohorte retrospectiva | Strahlenther Onkol | Reirradiación con cetuximab concurrente en cáncer de cabeza y cuello recurrente |
| [22246397](https://pubmed.ncbi.nlm.nih.gov/22246397/) | 2012 | Preclínico | Oncol Rep | Cetuximab inhibe el crecimiento de células de carcinoma ovárico mucinoso sin mutación de KRAS |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19953428 (cancelado) | ERBITUX® 5 MG/ML (MERCK S.A.) | Solución inyectable | CETUXIMAB |

Actualmente no hay registros sanitarios vigentes para este fármaco en Colombia.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (anticuerpo monoclonal anti-EGFR); no es un citotóxico convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar el prospecto. La literatura menciona reacciones de infusión graves y trastornos cutáneos como efectos frecuentes |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (20 registradas):
  - **Mayores**: ácido aminolevulínico y talidomida.
  - **Moderadas**: inhibidores de la bomba de protones (rabeprazol, omeprazol, dexlansoprazol, esomeprazol, lansoprazol, pantoprazol); quimioterapia (capecitabina, carboplatino, cisplatino, fluorouracilo, oxaliplatino); y otros (metoxaleno, idelalisib, omacetaxina mepesuccinato, verteporfina, aminolevulinato de metilo tópico y ácido aminolevulínico tópico).
  - También se registra su unión al receptor EGFR como diana farmacológica.
- Reacciones de infusión graves: descritas en la literatura (caso con administración mediante escalada de dosis, PMID 39415301).

No se dispone de advertencias ni contraindicaciones del prospecto. Consultar el prospecto para el resto de la información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para condroide hamartoma se basa solo en el modelo (L5), sin ensayos ni literatura, y no hay evidencia de dependencia de EGFR en esta lesión benigna. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Evidencia biológica de expresión o dependencia de EGFR en condroide hamartoma.
- Datos del mecanismo de acción y del prospecto (advertencias y contraindicaciones).
- Evaluar si conviene priorizar la indicación de neoplasia premaligna (NCT00524017), obteniendo los resultados de ese ensayo de Fase 2.
- Aclarar la situación regulatoria en Colombia, ya que no hay registro vigente.
- Definir la compatibilidad de vía de administración y la similitud con la indicación original, hoy pendientes.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

