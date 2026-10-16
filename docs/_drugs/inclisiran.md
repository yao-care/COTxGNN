---
layout: default
title: Inclisiran
parent: Solo Predicción del Modelo (L5)
nav_order: 340
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Inclisiran: nueva indicación predicha, Deficiencia de potasio (potassium deficiency disease) (nivel de evidencia L5). Indicación original: INCLISIRÁN"
monitor_inn: "inclisiran"
predicted_indications: ["potassium deficiency disease", "esophageal disease", "atypical coarctation of aorta", "migraine disorder", "non-syndromic esophageal malformation", "migraine with brainstem aura", "migraine with or without aura, susceptibility to", "aortic malformation", "esophageal ulcer", "Raynaud disease"]
---

# Inclisiran
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Inclisirán: De Hipercolesterolemia (LDL-C elevado) a Deficiencia de Potasio

## Resumen en Una Frase

Inclisirán es un ARN interferente pequeño (siRNA) que actúa sobre el ARNm de PCSK9 en el hígado y se utiliza para reducir el colesterol LDL (LDL-C). El modelo TxGNN predice que podría ser efectivo para la **deficiencia de potasio**, pero esta predicción no cuenta con **ningún ensayo clínico ni publicación** que la respalde.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | INCLISIRÁN (el registro sanitario no detalla la indicación; el uso conocido del fármaco es la reducción del LDL-C) |
| Nueva Indicación Predicha | Deficiencia de potasio (potassium deficiency disease) |
| Puntaje de Predicción TxGNN | 99.93% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo cancelado (sin registros vigentes) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este reporte. Según la información conocida, inclisirán es un siRNA que silencia el ARNm de PCSK9 en los hepatocitos, lo que aumenta los receptores de LDL y reduce el LDL-C.

No se identifica un vínculo mecanístico plausible con la deficiencia de potasio: inclisirán no tiene un papel conocido en la homeostasis del potasio. El puntaje alto del modelo es solo una predicción computacional, sin ensayos ni literatura que la sustenten, por lo que debe interpretarse con mucha cautela.

Otras indicaciones predichas (esofagopatías, migraña, malformaciones aórticas, enfermedad de Raynaud) tampoco muestran una conexión mecanística establecida. La única con ensayos asociados es la malformación aórtica, pero esos ensayos parecen corresponder a hipercolesterolemia familiar pediátrica y no a esa enfermedad (probable error de mapeo de datos).

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para deficiencia de potasio.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20201339 (cancelado) | SYBRAVA® 284 MG SOLUCIÓN PARA INYECCIÓN | Solución inyectable | INCLISIRÁN |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas en la consulta realizada, y no se dispone de advertencias ni contraindicaciones del prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (L5), sin ensayos, literatura ni mecanismo plausible que la respalde. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto del INVIMA (advertencias y contraindicaciones), indispensable antes de cualquier evaluación de seguridad
- Completar los datos de mecanismo de acción desde DrugBank
- Justificar biológicamente un posible vínculo entre el silenciamiento de PCSK9 y el metabolismo del potasio, o priorizar otra indicación predicha
- Verificar en ClinicalTrials.gov las condiciones de los ensayos NCT06597019 y NCT06597006, que parecen corresponder a hipercolesterolemia familiar pediátrica y no a la indicación predicha
- Aclarar la situación regulatoria (registro cancelado) si se considera una vía local de desarrollo
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

