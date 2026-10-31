---
layout: default
title: Interferon Beta-1B
parent: Solo Predicción del Modelo (L5)
nav_order: 349
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-31
description: "Interferon Beta-1B: nueva indicación predicha, Leucemia de células pilosas (hairy cell leukemia) (nivel de evidencia L5). Indicación original: Interferón beta-1b"
monitor_inn: "INTERFERON BETA-1B"
predicted_indications: ["hairy cell leukemia", "autoimmune disease of central nervous system"]
---

# Interferon Beta-1B
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Interferón beta-1b: De Esclerosis Múltiple (indicación registrada como "Interferón beta-1b") a Leucemia de Células Pilosas
{: .text-alpha }

## Resumen en Una Frase

Interferón beta-1b es un inmunomodulador registrado en Colombia bajo el producto Betaferon, utilizado en la práctica clínica para la esclerosis múltiple. El modelo TxGNN predice que podría ser efectivo para **leucemia de células pilosas**, pero hasta ahora **no hay ensayos clínicos ni publicaciones** que respalden esta dirección. Por separado, la segunda predicción del modelo (enfermedad autoinmune del sistema nervioso central) corresponde en la práctica a la esclerosis múltiple, indicación ya conocida, con **6 ensayos clínicos** y **17 publicaciones**.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Interferón beta-1b (el registro sanitario no detalla el texto de la indicación) |
| Nueva Indicación Predicha | Leucemia de células pilosas (hairy cell leukemia) |
| Puntaje de Predicción TxGNN | 0.9916 |
| Nivel de Evidencia | L5 (solo predicción del modelo) |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

> Nota: la segunda predicción (enfermedad autoinmune del sistema nervioso central, puntaje 0.9902) tiene nivel de evidencia L1 y recomendación "Proceed with Guardrails". Se presenta más abajo como información complementaria, ya que corresponde al uso conocido del fármaco (esclerosis múltiple) y no a un reposicionamiento real.

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, el interferón beta-1b es un interferón tipo I con efectos inmunomoduladores y antiproliferativos, y su eficacia en esclerosis múltiple ha sido ampliamente estudiada.

Para la leucemia de células pilosas, el vínculo es indirecto: el interferón alfa, otro interferón tipo I, tiene uso histórico en esta enfermedad. El modelo podría estar captando la señalización compartida de los interferones tipo I (efecto antiproliferativo e inmunomodulador). Es una inferencia a partir de un fármaco relacionado y **no constituye evidencia directa** para el interferón beta-1b.

La predicción es puramente computacional. Aunque el puntaje es muy alto, no existen datos clínicos ni bibliográficos que la respalden.

## Evidencia de Ensayos Clínicos

Para leucemia de células pilosas: actualmente no hay ensayos clínicos relacionados registrados.

Como información complementaria, para la enfermedad autoinmune del sistema nervioso central (esclerosis múltiple):

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00185211](https://clinicaltrials.gov/study/NCT00185211) | Fase 3 | Completado | 468 | Extensión abierta del estudio BENEFIT: seguimiento a largo plazo del tratamiento temprano vs. tardío con interferón beta-1b en esclerosis múltiple e inicio de la enfermedad |
| [NCT01333501](https://clinicaltrials.gov/study/NCT01333501) | Fase 4 | Completado | 151 | Fingolimod vs. interferón beta-1b sobre síntomas cognitivos en EMRR (aleatorizado, evaluador ciego) |
| [NCT01158183](https://clinicaltrials.gov/study/NCT01158183) | N/A | Completado | 226 | Estudio observacional ROBUST: resultados en práctica real con Betaseron durante 12 meses |
| [NCT00893217](https://clinicaltrials.gov/study/NCT00893217) | Fase 2 | Completado | 71 | Seguridad y tolerabilidad de Betaseron 500 mcg vs. 250 mcg (doble ciego) |
| [NCT01111656](https://clinicaltrials.gov/study/NCT01111656) | Fase 2 | Completado | 28 | Seguimiento de atorvastatina combinada con interferón beta-1b en EM (muestra pequeña) |
| [NCT01701856](https://clinicaltrials.gov/study/NCT01701856) | Fase 4 | Terminado | 5 | Desescalada de natalizumab a interferón beta-1b; terminado con solo 5 participantes, sin poder para conclusiones |

## Evidencia de Literatura

Para leucemia de células pilosas: actualmente no hay literatura relacionada disponible.

Como información complementaria (esclerosis múltiple), publicaciones principales:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38032059](https://pubmed.ncbi.nlm.nih.gov/38032059/) | 2023 | Metaanálisis en red | Cochrane Database Syst Rev | Efectos adversos de las inmunoterapias para esclerosis múltiple |
| [19794123](https://pubmed.ncbi.nlm.nih.gov/19794123/) | 2009 | Cohorte/Análisis | Neurology | Relación entre carga lesional T2 y discapacidad en EM |
| [17439988](https://pubmed.ncbi.nlm.nih.gov/17439988/) | 2007 | Cohorte | Brain | Heterogeneidad de la autoinmunidad anti-acuaporina-4 en EM en pacientes japoneses; sugiere precaución en el espectro de NMO |
| [9266420](https://pubmed.ncbi.nlm.nih.gov/9266420/) | 1997 | Revisión | J Neural Transm Suppl | Papel de los interferones en enfermedades desmielinizantes; interferón beta-1b redujo recaídas y progresión en RMN |
| [8808634](https://pubmed.ncbi.nlm.nih.gov/8808634/) | 1996 | Revisión | Clin Immunol Immunopathol | Interferón beta-1b reduce la frecuencia de ataques y la carga en RMN; modulador inmunitario |
| [8069001](https://pubmed.ncbi.nlm.nih.gov/8069001/) | 1994 | Revisión | Ann Pharmacother | Farmacología, eficacia, efectos adversos y dosificación de interferón beta-1b en EMRR |
| [27640189](https://pubmed.ncbi.nlm.nih.gov/27640189/) | 2016 | Revisión | Neurol Ther | Esclerosis múltiple pediátrica: conceptos y opciones de tratamiento |
| [25482255](https://pubmed.ncbi.nlm.nih.gov/25482255/) | 2014 | Seguimiento | Neurol Neurochir Pol | Efecto del interferón beta sobre la supervivencia a partir del seguimiento del ensayo pivotal |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 202595 (cancelado) | BETAFERON | Polvo liofilizado para reconstituir a solución inyectable | INTERFERON BETA-1B |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. Entre las listadas:
  - **Mayor**: bupropión.
  - **Moderadas** (selección): acarbosa, pioglitazona, rosiglitazona, claritromicina, levofloxacino, minociclina, naltrexona, rosuvastatina, simvastatina, orlistat, clotrimazol, nicotinamida, oxandrolona, oximetolona, estanozolol.
- **Precaución en espectro de NMO**: la literatura sugiere que en neuromielitis óptica el interferón beta podría empeorar la enfermedad, por lo que requeriría evaluación separada.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para leucemia de células pilosas tiene un puntaje alto (0.9916), pero no cuenta con ningún ensayo clínico ni publicación; su única base es una analogía con el interferón alfa. Además, el único registro sanitario en Colombia está cancelado. (Para la esclerosis múltiple, que es el uso conocido, la evidencia es L1 con recomendación "Proceed with Guardrails", pero no es un reposicionamiento nuevo.)

**Para avanzar se necesita:**
- Revisión bibliográfica dirigida sobre interferón beta (frente a interferón alfa) en leucemia de células pilosas y estudios preclínicos
- Datos del mecanismo de acción del fármaco
- Obtener el prospecto con advertencias y contraindicaciones
- Evaluar la comparación con tratamientos establecidos para leucemia de células pilosas antes de considerar estudios clínicos
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

