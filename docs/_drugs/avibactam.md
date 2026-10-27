---
layout: default
title: Avibactam
parent: Solo Predicción del Modelo (L5)
nav_order: 79
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Avibactam: nueva indicación predicha, Neumonía estreptocócica (nivel de evidencia L5). Indicación original: Ceftazidima e inhibidor de betalactamasa"
monitor_inn: "avibactam"
predicted_indications: ["influenza, severe, susceptibility to", "ureter tuberculosis", "urinary schistosomiasis", "polyclonal hyperviscosity syndrome", "hyperamylasemia"]
---

# Avibactam
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Avibactam: De Inhibidor de Betalactamasas (con Ceftazidima) a Neumonía Estreptocócica
{: .text-alpha }

## Resumen en Una Frase

Avibactam es un inhibidor de betalactamasas que se utiliza únicamente en combinación con ceftazidima (producto ZAVICEFTA) para tratar infecciones bacterianas.
El modelo TxGNN predice que podría ser efectivo para **neumonía estreptocócica**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata solo de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Ceftazidima e inhibidor de betalactamasa |
| Nueva Indicación Predicha | Neumonía estreptocócica |
| Puntaje de Predicción TxGNN | 99.70% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, avibactam es un inhibidor de betalactamasas no betalactámico (enzimas de clase A, C y algunas de clase D) que se usa exclusivamente junto con ceftazidima. No tiene actividad antibacteriana propia significativa.

La relación con la nueva indicación es débil. *Streptococcus pneumoniae* resiste a los betalactámicos principalmente por alteración de las proteínas fijadoras de penicilina, y no por producción de betalactamasas, que es justamente el blanco de avibactam. El puntaje alto del modelo probablemente refleja la asociación del fármaco con indicaciones antibacterianas y respiratorias (por ejemplo, ceftazidima-avibactam en neumonía intrahospitalaria) y no constituye evidencia independiente.

En conclusión, el fundamento mecanístico para un beneficio de avibactam por sí solo en esta indicación es limitado y debe considerarse con cautela.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20157002 (cancelado) | ZAVICEFTA | Polvo estéril para reconstituir a solución inyectable | Ceftazidima e inhibidor de betalactamasa |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Otras Predicciones Evaluadas

Todas las predicciones adicionales tienen nivel de evidencia L5, sin ensayos clínicos ni literatura, y recomendación Hold:

| Posición | Indicación Predicha | Puntaje TxGNN | Valoración del Mecanismo |
|------|------|------|------|
| 2 | Susceptibilidad a influenza grave | 99.28% | Sin mecanismo directo plausible; avibactam no tiene actividad antiviral. Probable artefacto del grafo de conocimiento. |
| 3 | Tuberculosis ureteral | 99.11% | Racional teórico y preclínico (inhibición in vitro de la betalactamasa BlaC de *M. tuberculosis*); dependería del betalactámico asociado y de regímenes multifármaco estándar. |
| 4 | Esquistosomiasis urinaria | 99.06% | Sin base mecanística; es un parásito sin blanco betalactamasa. El tratamiento establecido es praziquantel. |
| 5 | Síndrome de hiperviscosidad policlonal | 99.01% | Sin vínculo identificable; probable artefacto del modelo. |
| 6 | Hiperamilasemia | 99.01% | Es un hallazgo de laboratorio, no una enfermedad tratable con avibactam. |

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos ni literatura que respalden la predicción de neumonía estreptocócica (nivel L5), y el fundamento mecanístico es débil. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Datos del mecanismo de acción desde fuentes complementarias.
- Revisión del prospecto oficial (advertencias y contraindicaciones) para completar la evaluación de seguridad.
- Evidencia clínica o preclínica que demuestre un beneficio independiente de la combinación con ceftazidima.
- Aclarar la situación regulatoria actual de ceftazidima-avibactam en Colombia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

