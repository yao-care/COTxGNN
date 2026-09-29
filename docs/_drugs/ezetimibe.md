---
layout: default
title: Ezetimibe
parent: Evidencia Alta (L1-L2)
nav_order: 194
evidence_level: L1
indication_count: 4
---

# Ezetimibe
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **4** 
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

# Ezetimiba: De Combinaciones con Simvastatina a Hiperlipoproteinemia

## Resumen en Una Frase

Ezetimiba es un inhibidor de la absorción intestinal de colesterol. En Colombia está registrada en combinaciones con simvastatina (registro INVIMA 20138715).
El modelo TxGNN predice que podría ser efectiva para **hiperlipoproteinemia**, con **50 ensayos clínicos** y **19 publicaciones** que respaldan esta dirección.
Esta predicción se parece más a una confirmación de uso ya establecido que a un reposicionamiento real.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Combinaciones de simvastatina (paquetes), según el registro sanitario |
| Nueva Indicación Predicha | Hiperlipoproteinemia |
| Puntaje de Predicción TxGNN | 99.63% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, ezetimiba inhibe la proteína NPC1L1, que media la absorción intestinal de colesterol, y con ello reduce el colesterol LDL (LDL-C). Su acción es aditiva a la de las estatinas, que reducen la síntesis hepática de colesterol.

La indicación registrada en Colombia (combinaciones con simvastatina) ya es de tipo hipolipemiante. La hiperlipoproteinemia es el mismo campo terapéutico. Por eso el puntaje alto del modelo es coherente, y la predicción equivale casi a confirmar un uso ya existente.

Cabe señalar que el paquete de datos no trae indicaciones originales ni mecanismo de acción para este fármaco. Conviene corregir esa carencia antes de usar el resultado en etapas posteriores.

---

## Evidencia de Ensayos Clínicos

Se muestran 10 de los 50 ensayos registrados, elegidos por su relación directa con ezetimiba.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00093899](https://clinicaltrials.gov/study/NCT00093899) | Fase 3 | Completado | 611 | Ezetimiba/simvastatina más fenofibrato en hiperlipidemia mixta |
| [NCT00092560](https://clinicaltrials.gov/study/NCT00092560) | Fase 3 | Completado | 587 | Coadministración de fenofibrato y ezetimiba en hiperlipidemia mixta |
| [NCT00092573](https://clinicaltrials.gov/study/NCT00092573) | Fase 3 | Completado | 576 | Seguridad y eficacia de fenofibrato con ezetimiba en hiperlipidemia mixta |
| [NCT00349284](https://clinicaltrials.gov/study/NCT00349284) | Fase 3 | Completado | 181 | Fenofibrato 145 mg, ezetimiba 10 mg y su combinación en dislipidemia tipo IIb con síndrome metabólico |
| [NCT02451098](https://clinicaltrials.gov/study/NCT02451098) | Fase 3 | Completado | 385 | Atorvastatina + ezetimiba frente a atorvastatina sola en hipercolesterolemia primaria (doble ciego, diseño factorial) |
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Fase 3 | Completado | 720 | ENHANCE: ezetimiba + simvastatina en dosis alta frente a simvastatina sola sobre la progresión de la aterosclerosis carotídea en hipercolesterolemia familiar heterocigota |
| [NCT01043380](https://clinicaltrials.gov/study/NCT01043380) | Fase 4 | Completado | 245 | Regresión de placa coronaria por ultrasonido intravascular: inhibidor de absorción (ezetimiba) frente a inhibidor de síntesis |
| [NCT00092833](https://clinicaltrials.gov/study/NCT00092833) | Fase 3 | Terminado | 49 | Uso de tratamiento de ezetimiba 10 mg/día en hipercolesterolemia familiar homocigota o sitosterolemia homocigota |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Fase 3 | Completado | 50 | Ezetimiba 10 mg con atorvastatina o simvastatina en hipercolesterolemia familiar homocigota |
| [NCT06789432](https://clinicaltrials.gov/study/NCT06789432) | Fase 4 | Reclutando | 500 | Combinación fija atorvastatina/ezetimiba 10/10 mg frente a atorvastatina 20 mg en población de Bangladesh |

---

## Evidencia de Literatura

Se muestran 10 de las 19 publicaciones recuperadas. La única de ellas clasificada como ECA y centrada en ezetimiba es TANDEM (2025).

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [40347969](https://pubmed.ncbi.nlm.nih.gov/40347969/) | 2025 | ECA | Lancet | TANDEM: combinación fija de obicetrapib y ezetimiba para reducir el LDL-C, fase 3 doble ciego controlada con placebo |
| [41206969](https://pubmed.ncbi.nlm.nih.gov/41206969/) | 2026 | ECA | JAMA | Inhibidor oral de PCSK9 (enlicitida) en hipercolesterolemia familiar heterocigota; ezetimiba no es el fármaco evaluado, aporta contexto terapéutico |
| [40682836](https://pubmed.ncbi.nlm.nih.gov/40682836/) | 2025 | Revisión | Mol Med Rep | Avances en fármacos actuales para la hiperlipidemia y su relación con la prevención de enfermedad cardiovascular aterosclerótica |
| [19654419](https://pubmed.ncbi.nlm.nih.gov/19654419/) | 2009 | Revisión | Drug Ther Bull | Actualización sobre ezetimiba: reduce el LDL-C y el colesterol total, sola o con estatina |
| [18376001](https://pubmed.ncbi.nlm.nih.gov/18376001/) | 2008 | Comentario | N Engl J Med | Comentario editorial sobre la reducción de colesterol y ezetiba (sin resumen disponible) |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Revisión | J Am Coll Cardiol | Terapias nuevas y emergentes para reducir LDL-C y apoB, sobre la base de estatinas, ezetimiba e inhibidores de PCSK9 |
| [30702994](https://pubmed.ncbi.nlm.nih.gov/30702994/) | 2019 | Revisión | Circ Res | Panorama de los agentes reductores de colesterol y su eficacia y seguridad |
| [25939291](https://pubmed.ncbi.nlm.nih.gov/25939291/) | 2015 | Revisión | Cardiol Clin | Hipercolesterolemia familiar: estatinas, ezetimiba y otras opciones que reducen el LDL-C |
| [34480646](https://pubmed.ncbi.nlm.nih.gov/34480646/) | 2021 | Revisión | Curr Cardiol Rep | Carga global y abordaje de la hipercolesterolemia familiar |
| [23956253](https://pubmed.ncbi.nlm.nih.gov/23956253/) | 2013 | Guía/Consenso | Eur Heart J | Consenso de la Sociedad Europea de Aterosclerosis sobre el infradiagnóstico y el infratratamiento de la hipercolesterolemia familiar |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20138715 | EZIT-ST 10/10 (Hetero Labs Limited) | Tableta | SIMVASTATINA COMBINACIONES PAQUETES |

El paquete reporta 20 registros en total. Las cinco entradas detalladas corresponden todas al mismo registro 20138715, por lo que se muestra una sola vez.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay múltiples ensayos de Fase 3 completados con ezetimiba (sola o combinada) en hiperlipidemia mixta e hipercolesterolemia, y el fármaco ya está comercializado en Colombia en una combinación hipolipemiante. La evidencia es sólida (L1), pero faltan datos de seguridad locales y el paquete de datos tiene vacíos.

**Para avanzar se necesita:**
- Descargar y revisar el prospecto de INVIMA para obtener advertencias y contraindicaciones (actualmente sin datos).
- Completar los datos del mecanismo de acción (DrugBank) y las indicaciones originales, hoy vacías.
- Confirmar qué indicación exacta cubre el registro colombiano, ya que el texto disponible ("combinaciones de simvastatina") es poco específico.
- Como referencia, la segunda predicción (hipercolesterolemia familiar) también alcanza L1 y Proceed with Guardrails. La tercera (déficit de colesterol 7α-hidroxilasa, L4) es solo una pregunta de investigación. La cuarta (déficit de CETP, L5) queda en Hold, con un vínculo mecanístico débil.

---

*Este informe es solo de referencia para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de aplicarse.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

