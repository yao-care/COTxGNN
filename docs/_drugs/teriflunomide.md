---
layout: default
title: Teriflunomide
parent: Evidencia Alta (L1-L2)
nav_order: 380
evidence_level: L1
indication_count: 1
---

# Teriflunomide
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **1** 
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

# Teriflunomida: De Indicación Original No Registrada a Esclerosis Múltiple Remitente-Recurrente

## Resumen en Una Frase

La teriflunomida es un inmunomodulador oral que inhibe la enzima DHODH. En el registro sanitario colombiano su texto de indicación solo dice "TERIFLUNOMIDA", sin especificar la indicación original.
El modelo TxGNN predice que podría ser efectivo para **esclerosis múltiple remitente-recurrente (EMRR)**, con **29 ensayos clínicos** y **19 publicaciones** que respaldan esta dirección.
La EMRR ya es una indicación conocida del fármaco, por lo que esto confirma un uso existente y no es un reposicionamiento novedoso.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto de INVIMA solo indica "TERIFLUNOMIDA") |
| Nueva Indicación Predicha | Esclerosis múltiple remitente-recurrente |
| Puntaje de Predicción TxGNN | 99.24% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

El registro de datos no incluye el mecanismo de acción del fármaco. Según la farmacología establecida, la teriflunomida (metabolito activo de la leflunomida) inhibe la dihidroorotato deshidrogenasa (DHODH) y bloquea la síntesis de novo de pirimidinas. Esto frena la proliferación de los linfocitos T y B activados, que impulsan la inflamación de la EMRR. Las células en reposo usan la vía de rescate y quedan en gran parte protegidas. La base de datos farmacológica consultada confirma la diana (DHODH) y describe el uso clínico como reducción de brotes en esclerosis múltiple recurrente.

Como la EMRR es una enfermedad mediada por linfocitos activados, el mecanismo es plausible. Además, el fármaco ya está aprobado para EMS recurrente en otros mercados, y esto respalda la predicción del modelo.

Falta el texto de indicación original en el registro colombiano, y el campo `original_indications` está vacío. Este vacío es del registro y no indica ausencia de uso clínico.

## Evidencia de Ensayos Clínicos

Se muestran 10 de 29 ensayos, priorizando los de mayor relevancia para la teriflunomida.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00134563](https://clinicaltrials.gov/study/NCT00134563) | Fase 3 | Completado | 1088 | Doble ciego, controlado con placebo. Evalúa la frecuencia de brotes y la acumulación de discapacidad en EM con brotes. Evidencia pivotal directa |
| [NCT00883337](https://clinicaltrials.gov/study/NCT00883337) | Fase 3 | Completado | 324 | Teriflunomida (dos dosis) vs interferón beta-1a, con evaluador ciego y extensión a largo plazo |
| [NCT00803049](https://clinicaltrials.gov/study/NCT00803049) | Fase 3 | Completado | 742 | Extensión a largo plazo de seguridad y tolerabilidad (7 y 14 mg) |
| [NCT00228163](https://clinicaltrials.gov/study/NCT00228163) | Fase 2 | Completado | 147 | Extensión del estudio de fase II. Seguridad y eficacia a largo plazo |
| [NCT04788615](https://clinicaltrials.gov/study/NCT04788615) | Fase 3 | Completado | 185 | Ofatumumab vs terapia modificadora de primera línea en EMR recién diagnosticada. No se confirma que la teriflunomida esté en el brazo comparador |
| [NCT02490982](https://clinicaltrials.gov/study/NCT02490982) | N/A | Completado | 106 | Efectividad de la teriflunomida en la práctica clínica habitual en EMRR, con seguimiento de al menos 2 años |
| [NCT03302442](https://clinicaltrials.gov/study/NCT03302442) | N/A | Completado | 3000 | Estudio observacional: dimetilfumarato vs teriflunomida en resultados clínicos y de resonancia magnética (cohorte francesa) |
| [NCT02776072](https://clinicaltrials.gov/study/NCT02776072) | N/A | Completado | 2978 | Estudio retrospectivo de resultados en la vida real con cuatro terapias, entre ellas la teriflunomida |
| [NCT01881191](https://clinicaltrials.gov/study/NCT01881191) | N/A | Completado | 50 | Efecto de la teriflunomida sobre la patología de la sustancia gris, medido por resonancia magnética |
| [NCT03768648](https://clinicaltrials.gov/study/NCT03768648) | N/A | Completado | 75 | Cognición cotidiana y marcadores de resonancia magnética en pacientes con EMRR tratados con teriflunomida |

## Evidencia de Literatura

Se muestran 10 de 19 publicaciones. Los ECA de la lista usan la teriflunomida como comparador activo.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [32757523](https://pubmed.ncbi.nlm.nih.gov/32757523/) | 2020 | ECA | N Engl J Med | Ofatumumab vs teriflunomida en esclerosis múltiple |
| [36001711](https://pubmed.ncbi.nlm.nih.gov/36001711/) | 2022 | ECA | N Engl J Med | Ublituximab vs teriflunomida en EM recurrente |
| [33779698](https://pubmed.ncbi.nlm.nih.gov/33779698/) | 2021 | ECA | JAMA Neurol | Estudio OPTIMUM de fase 3: ponesimod vs teriflunomida en EM recurrente |
| [39307151](https://pubmed.ncbi.nlm.nih.gov/39307151/) | 2024 | ECA | Lancet Neurol | Dos ensayos de fase 3: evobrutinib vs teriflunomida como comparador activo |
| [40202623](https://pubmed.ncbi.nlm.nih.gov/40202623/) | 2025 | ECA | N Engl J Med | Tolebrutinib vs teriflunomida en EM recurrente |
| [38174776](https://pubmed.ncbi.nlm.nih.gov/38174776/) | 2024 | Metaanálisis en red | Cochrane Database Syst Rev | Compara inmunomoduladores e inmunosupresores en EMRR. Todos reducen los brotes frente a no tratar |
| [37528262](https://pubmed.ncbi.nlm.nih.gov/37528262/) | 2023 | Metaanálisis | Neurotherapeutics | Dimetilfumarato vs teriflunomida en estudios poscomercialización |
| [31098896](https://pubmed.ncbi.nlm.nih.gov/31098896/) | 2019 | Revisión | Drugs | Revisión de la teriflunomida en EMRR. Inhibe la DHODH y la síntesis de pirimidinas. Eficaz y en general bien tolerada |
| [33620411](https://pubmed.ncbi.nlm.nih.gov/33620411/) | 2021 | Revisión | JAMA | Revisión del diagnóstico y tratamiento de la esclerosis múltiple |
| [26758290](https://pubmed.ncbi.nlm.nih.gov/26758290/) | 2016 | Revisión | CNS Drugs | Revisión de la ficha técnica europea de la teriflunomida en EMRR y su uso práctico |

## Información de Mercado en Colombia

El registro contiene 20 entradas. Las 5 primeras corresponden al mismo registro sanitario y se muestran una sola vez.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20240967 | TREEFLUDA® 14 MG TABLETAS (VESALIUS PHARMA S.A.S.) | Tableta | El registro solo indica "TERIFLUNOMIDA", sin texto de indicación |

También figuran las formas orales "tableta" y "tableta recubierta".

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la consulta de DDI (completada) devolvió 1 registro. No es una interacción con otro fármaco, sino la diana farmacológica de la teriflunomida, la DHODH (gen *DHODH*, humano). No hay interacciones entre fármacos con nivel de gravedad asignado.

No se obtuvieron advertencias ni contraindicaciones del prospecto de INVIMA. Consultar el prospecto para esa información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay evidencia de nivel L1: varios ECA de Fase 3 completados (NCT00134563, NCT00883337, NCT00803049), y la teriflunomida se usa como comparador activo en múltiples ensayos de fase 3 publicados. El producto ya está comercializado en Colombia. Como falta el prospecto de INVIMA, se requieren salvaguardas de seguridad.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones), y confirmar el texto de indicación aprobado en Colombia.
- Obtener los datos del mecanismo de acción desde DrugBank.
- Monitoreo según el prospecto: hepatotoxicidad, teratogenicidad y anticoncepción, y procedimiento de eliminación acelerada.
- Verificar la interacción registrada (DHODH) y las demás interacciones antes de coprescribir.
- Confirmar el papel de la teriflunomida en NCT04788615.

Estos resultados son solo de referencia para investigación y no constituyen consejo médico. Cualquier uso requiere validación clínica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

