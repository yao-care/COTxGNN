---
layout: default
title: Mometasone
parent: Solo Predicción del Modelo (L5)
nav_order: 453
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Mometasone: nueva indicación predicha, Linfoma cutáneo primario de células T (nivel de evidencia L5). Indicación original: Mometasona"
monitor_inn: "mometasone"
predicted_indications: ["primary cutaneous T-cell lymphoma"]
---

# Mometasone
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

# Mometasona: De Mometasona (corticosteroide) a Linfoma Cutáneo Primario de Células T

## Resumen en Una Frase

Mometasona es un corticosteroide sintético, comercializado en Colombia en cremas tópicas y suspensiones nasales, cuyo registro sanitario figura como "mometasona".
El modelo TxGNN predice que podría ser efectivo para el **linfoma cutáneo primario de células T**,
pero actualmente solo existen **0 ensayos clínicos** y **2 publicaciones** (ambos reportes de caso, sin evidencia específica de mometasona) que respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Mometasona (el registro no detalla una indicación clínica específica) |
| Nueva Indicación Predicha | Linfoma cutáneo primario de células T |
| Puntaje de Predicción TxGNN | 99.36% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 6 (todos cancelados) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según lo conocido, mometasona es un corticosteroide potente que actúa sobre el receptor de glucocorticoides (NR3C1), con efectos antiinflamatorios e inmunosupresores. Se utiliza por vía intranasal en asma, rinitis alérgica y pólipos nasales, y por vía tópica en trastornos alérgicos de la piel.

Los corticosteroides tópicos son una terapia dirigida a la piel establecida para el micosis fungoide en etapa temprana, la forma más común de linfoma cutáneo primario de células T. Al suprimir la activación de los linfocitos T y la señalización de citocinas, mecanísticamente podría ser aplicable a esta enfermedad, lo que es coherente con el alto puntaje del modelo.

Sin embargo, esta relación es un efecto de clase plausible y no un efecto demostrado de mometasona. No hay evidencia clínica específica de este fármaco en esta indicación.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [40821495](https://pubmed.ncbi.nlm.nih.gov/40821495/) | 2025 | Reporte de caso | Proceedings (Baylor University Medical Center) | Pseudolinfoma cutáneo refractario en una mujer de 62 años; mometasona y tacrolimus no fueron efectivos y se trató con tapinarof. No respalda la eficacia de mometasona. |
| [25442255](https://pubmed.ncbi.nlm.nih.gov/25442255/) | 2015 | Reporte de caso | Journal of Cutaneous Pathology | Micosis fungoide infantil con inmunofenotipo citotóxico CD8+ CD56+ en un niño de 11 años; ilustra la presentación atípica de estos linfomas en la infancia. |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20019847 | FURODERM CREMA | Crema tópica | Mometasona |
| 20202403 | FURAFAR® 0.1 % CREMA | Crema tópica | Mometasona |
| 214137 | NASONEX® SPRAY NASAL | Suspensión nasal | Mometasona |
| 20205917 | RINIALER® 0.05% SPRAY NASAL | Solución para inhalación | Mometasona |
| 20227452 | MINESTEROL 0.1% CREMA | Crema tópica | Mometasona |

Nota: los 6 registros sanitarios están cancelados; no hay registros vigentes. El sexto registro (DIFENZ®, crema tópica, tetrinoína combinaciones) no se muestra en la tabla por el límite de 5 filas.

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: se identificó una interacción de tipo farmacológico con el receptor de glucocorticoides (NR3C1), que es el blanco terapéutico esperado de mometasona. No se reportaron interacciones con otros fármacos.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto y un fundamento mecanístico plausible (los corticosteroides tópicos se usan en micosis fungoide temprana), pero no hay ensayos clínicos ni evidencia específica de mometasona, solo dos reportes de caso. Además, todos los registros sanitarios en Colombia están cancelados.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA) desde DrugBank
- Prospecto con advertencias y contraindicaciones desde INVIMA
- Revisión de literatura y ensayos específicos de mometasona en micosis fungoide/linfoma cutáneo de células T
- Evaluación de la ruta de administración (tópica) y de la viabilidad de un nuevo registro sanitario vigente en Colombia
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

