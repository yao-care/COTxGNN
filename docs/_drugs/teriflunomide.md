---
layout: default
title: Teriflunomide
parent: Evidencia Alta (L1-L2)
nav_order: 618
evidence_level: L1
indication_count: 1
last_modified_at: 2026-10-14
description: "Teriflunomide: nueva indicación predicha, Esclerosis múltiple remitente-recurrente (nivel de evidencia L1). Indicación original: TERIFLUNOMIDA"
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

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

# Teriflunomida: De Esclerosis Múltiple Recurrente a Esclerosis Múltiple Remitente-Recurrente

## Resumen en Una Frase

Teriflunomida es un inmunomodulador oral registrado en Colombia bajo la denominación "TERIFLUNOMIDA", sin una indicación detallada en el texto del registro.
El modelo TxGNN predice que podría ser efectivo para la **esclerosis múltiple remitente-recurrente**, con **12 ensayos clínicos** y **20 publicaciones** que respaldan esta dirección.
Cabe aclarar que la esclerosis múltiple recurrente ya es una indicación establecida del fármaco, por lo que este caso es más una confirmación de un uso existente que un reposicionamiento propiamente dicho.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | TERIFLUNOMIDA (el texto del registro no detalla la indicación) |
| Nueva Indicación Predicha | Esclerosis múltiple remitente-recurrente |
| Puntaje de Predicción TxGNN | 99.24% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 3 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción original. Según la farmacología establecida, teriflunomida es el metabolito activo de la leflunomida e inhibe la enzima mitocondrial dihidroorotato deshidrogenasa (DHODH), necesaria para la síntesis de novo de pirimidinas. Esto es consistente con el dato de interacción farmacológica registrado, que identifica a DHODH como su diana humana.

Al bloquear esta vía, se limita la proliferación de los linfocitos T y B activados, que se dividen rápidamente, mientras se preservan las células en reposo y las que dependen de la vía de rescate. Así se reduce la inflamación autoinmune del sistema nervioso central característica de la esclerosis múltiple.

La relación entre la indicación original y la predicha es directa: la esclerosis múltiple recurrente ya es el uso aprobado de teriflunomida en otras jurisdicciones. Por ello, la alta puntuación del modelo (0.992) coincide con la evidencia clínica sólida disponible. El estado "solo cancelados" en Colombia parece referirse a registros locales específicos y no refleja la situación clínica ni de mercado global del fármaco; debe verificarse en la jurisdicción de interés.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00134563](https://clinicaltrials.gov/study/NCT00134563) | Fase 3 | Completado | 1088 | ECA doble ciego controlado con placebo sobre eficacia de teriflunomida en reducir recaídas y retrasar la discapacidad en EM recurrente |
| [NCT00883337](https://clinicaltrials.gov/study/NCT00883337) | Fase 3 | Completado | 324 | Comparación directa de dos dosis de teriflunomida frente a interferón beta-1a en EM recurrente, con extensión a largo plazo |
| [NCT00803049](https://clinicaltrials.gov/study/NCT00803049) | Fase 3 | Completado | 742 | Extensión a largo plazo para documentar la seguridad de teriflunomida 7 y 14 mg |
| [NCT04788615](https://clinicaltrials.gov/study/NCT04788615) | Fase 3 | Completado | 185 | Ofatumumab frente a DMT de primera línea (incluye comparadores como teriflunomida) en EM recién diagnosticada |
| [NCT00228163](https://clinicaltrials.gov/study/NCT00228163) | Fase 2 | Completado | 147 | Extensión de seguridad y eficacia a largo plazo de teriflunomida |
| [NCT02490982](https://clinicaltrials.gov/study/NCT02490982) | N/A | Completado | 106 | Estudio observacional de efectividad de teriflunomida en la práctica clínica habitual |
| [NCT03464448](https://clinicaltrials.gov/study/NCT03464448) | N/A | Completado | 30 | Estudio de mecanismo: papel de los linfocitos B reguladores en el efecto de teriflunomida |
| [NCT03561402](https://clinicaltrials.gov/study/NCT03561402) | N/A | Completado | 24 | Estudio observacional de biomarcadores asociados con la actividad de la enfermedad en pacientes tratados con teriflunomida |
| [NCT03500328](https://clinicaltrials.gov/study/NCT03500328) | N/A | Completado | 900 | Ensayo pragmático de terapia temprana agresiva frente a escalonada; evidencia indirecta para teriflunomida |
| [NCT03535298](https://clinicaltrials.gov/study/NCT03535298) | Fase 4 | Activo, sin reclutar | 800 | DELIVER-MS: estrategia intensiva temprana frente a escalonada en EM remitente-recurrente |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [32757523](https://pubmed.ncbi.nlm.nih.gov/32757523/) | 2020 | ECA | N Engl J Med | Ofatumumab frente a teriflunomida en esclerosis múltiple (teriflunomida como comparador activo) |
| [36001711](https://pubmed.ncbi.nlm.nih.gov/36001711/) | 2022 | ECA | N Engl J Med | Ublituximab frente a teriflunomida en EM recurrente |
| [40202623](https://pubmed.ncbi.nlm.nih.gov/40202623/) | 2025 | ECA | N Engl J Med | Tolebrutinib frente a teriflunomida en EM recurrente |
| [39307151](https://pubmed.ncbi.nlm.nih.gov/39307151/) | 2024 | ECA | Lancet Neurol | Evobrutinib frente a teriflunomida (ensayos de fase 3 evolutionRMS1 y 2) |
| [33779698](https://pubmed.ncbi.nlm.nih.gov/33779698/) | 2021 | ECA | JAMA Neurol | Ponesimod frente a teriflunomida en el estudio OPTIMUM, primer fase 3 que compara dos DMT orales |
| [38174776](https://pubmed.ncbi.nlm.nih.gov/38174776/) | 2024 | Metaanálisis en red | Cochrane Database Syst Rev | Comparación de inmunomoduladores e inmunosupresores en EMRR |
| [31098896](https://pubmed.ncbi.nlm.nih.gov/31098896/) | 2019 | Revisión | Drugs | Teriflunomida es eficaz y generalmente bien tolerada en EM recurrente-remitente, con base en ECA y datos del mundo real |
| [33620411](https://pubmed.ncbi.nlm.nih.gov/33620411/) | 2021 | Revisión | JAMA | Revisión del diagnóstico y tratamiento de la esclerosis múltiple |
| [37578431](https://pubmed.ncbi.nlm.nih.gov/37578431/) | 2023 | Cohorte observacional | Eur J Neurol | Comparación de efectividad en la práctica real entre dimetilfumarato y teriflunomida |
| [34046085](https://pubmed.ncbi.nlm.nih.gov/34046085/) | 2021 | Observacional | Ther Adv Neurol Disord | Resultados de teriflunomida 14 mg según edad y tratamiento previo |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20240967 | TREEFLUDA® 14 MG TABLETAS | Tableta | TERIFLUNOMIDA |
| 20194846 | BLUMADIZ® 14 MG TABLETAS RECUBIERTAS | Tableta recubierta | TERIFLUNOMIDA |
| 20056290 | AUBAGIO® | Tableta recubierta | TERIFLUNOMIDA |

Los tres registros figuran como cancelados.

---

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: se identificó una entrada de interacción farmacológica, que corresponde a la diana farmacológica de teriflunomida (dihidroorotato deshidrogenasa, gen DHODH) y no a la interacción con otro medicamento.

Para el resto de la información de seguridad (advertencias y contraindicaciones), consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen varios ensayos de Fase 3 completados, incluido un ECA controlado con placebo con 1088 participantes, además de múltiples ECA publicados con teriflunomida como comparador activo, lo que sitúa la evidencia en el nivel L1. Sin embargo, la esclerosis múltiple recurrente ya es un uso establecido y los tres registros sanitarios colombianos están cancelados, por lo que la decisión depende de la situación regulatoria local.

**Para avanzar se necesita:**
- Verificar el estado regulatorio actual en Colombia y las razones de la cancelación de los tres registros.
- Obtener y revisar el prospecto aprobado (advertencias y contraindicaciones) en el sitio de INVIMA.
- Confirmar los datos del mecanismo de acción en DrugBank.
- Definir un plan de monitoreo de seguridad para poblaciones específicas.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

