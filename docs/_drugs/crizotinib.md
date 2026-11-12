---
layout: default
title: Crizotinib
parent: Solo Predicción del Modelo (L5)
nav_order: 181
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-12
description: "Crizotinib: nueva indicación predicha, Fibromatosis gingival (nivel de evidencia L5). Indicación original: No especificada en el registro (el texto de indicación solo dice \"CRI…"
monitor_inn: "CRIZOTINIB"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung benign neoplasm", "lung germ cell tumor", "pulmonary sulcus neoplasm", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "junctional epidermolysis bullosa", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome"]
---

# Crizotinib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Crizotinib: De Indicación Registrada (Crizotinib) a Fibromatosis Gingival
{: .text-alpha }

## Resumen en Una Frase

Crizotinib es un inhibidor de tirosina quinasa (ALK, ROS1 y MET).
El modelo TxGNN predice que podría ser efectivo para **fibromatosis gingival**, con un puntaje muy alto (0.9981), pero con **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.
Se trata de una predicción del modelo TxGNN (deep learning), cuyo puntaje puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

<!-- review:begin co-lic-20261105-crizotinib-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Crizotinib es un inhibidor de tirosina quinasa (ALK, ROS1 y MET) cuyo único registro sanitario en Colombia (Xalkori®, Pfizer) figura hoy como cancelado, y el texto de indicación registrado solo repite el nombre del principio activo." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 2 registros sanitarios (vigentes: 2); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-crizotinib-2 -->

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto de indicación solo dice "CRIZOTINIB"); en la literatura, cáncer de pulmón de células no pequeñas ALK/ROS1 positivo |
| Nueva Indicación Predicha | Fibromatosis gingival |
| Puntaje de Predicción TxGNN | 0.9981 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 2 de 2) |
| Número de Registros Sanitarios | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, crizotinib inhibe las quinasas ALK, ROS1 y MET, y su eficacia está comprobada en el cáncer de pulmón de células no pequeñas con reordenamientos de ALK o ROS1.

La relación entre la indicación original (un cáncer impulsado por oncogenes quinasa) y la fibromatosis gingival (un sobrecrecimiento fibroso benigno de la encía) **no es evidente**. No se identificó ninguna vía de ALK, ROS1 o MET vinculada con la patología de la fibromatosis gingival, y no hay ensayos ni literatura que apoyen un vínculo.

Por lo tanto, el puntaje alto del modelo debe interpretarse con cautela: proviene del modelo TxGNN (deep learning) y puede reflejar similitudes aprendidas entre enfermedades relacionadas, no una hipótesis mecanística respaldada. Cualquier avance requeriría primero establecer una justificación biológica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20083808 | XALKORI® 200MG CÁPSULAS (Pfizer S.A.S.) | Cápsula dura | CRIZOTINIB (estado: vigente) |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasa ALK/ROS1/MET) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma, función hepática y renal; según la literatura revisada, vigilancia de función hepática y de ritmo/QT cardíaco |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones potenciales. Entre las de nivel **Mayor** destacan claritromicina, cisaprida, dolasetrón, eliglustat y granisetrón. Entre las de nivel **Moderado** figuran famotidina, metformina, loperamida, bupropión, aprepitant, dexametasona, budesonida, bisacodilo, clotrimazol y varios laxantes (ácido picosulfúrico, polietilenglicol, aceite de ricino, glicerina).
- **Señales de la literatura revisada** (casos clínicos en pacientes con cáncer): insuficiencia hepática fulminante fatal, toxicidad cardíaca (bradicardia, prolongación del QT, síndrome del seno enfermo), esofagitis erosiva en un paciente pediátrico y eritema multiforme.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos ni publicaciones, y no existe un vínculo mecanístico plausible entre la inhibición de ALK/ROS1/MET y la fibromatosis gingival. Además, el perfil de seguridad de crizotinib (hepático y cardíaco) es poco favorable para una enfermedad benigna.

<!-- review:begin co-lic-20261105-crizotinib-3 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, el único registro sanitario en Colombia está cancelado y el perfil de seguridad de crizotinib (hepático y cardíaco) es poco favorable para una enfermedad benigna." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 2 registros sanitarios (vigentes: 2); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-crizotinib-3 -->

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción y una hipótesis biológica que conecte las vías ALK/ROS1/MET con la fibromatosis gingival
- Estudios preclínicos que muestren un efecto sobre fibroblastos gingivales o modelos de la enfermedad
- Información de seguridad del prospecto del INVIMA (advertencias y contraindicaciones)
- Evaluar el balance riesgo-beneficio frente a alternativas para una condición benigna

<!-- review:begin co-lic-20261031-crizotinib-1 -->

> **Corrección de revisión (2026-10-31)**: Texto original: "Aclarar el estado regulatorio en Colombia (registro cancelado) y la viabilidad de acceso al producto / Evaluar el balance riesgo-beneficio frente a alternativas para una condición benigna" Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-10-31. El medicamento tiene 2 registros sanitarios (vigentes: 2); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261031-crizotinib-1 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-10-31 | Eliminado: "Aclarar el estado regulatorio en Colombia (registro cancelado) y la viabilidad de acceso al producto" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "cuyo único registro sanitario en Colombia (Xalkori®, Pfizer) figura hoy como cancelado, y el texto de indicación registrado solo repite el n" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "el único registro sanitario en Colombia está cancelado y" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

