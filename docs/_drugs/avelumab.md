---
layout: default
title: Avelumab
parent: Solo Predicción del Modelo (L5)
nav_order: 78
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Avelumab: nueva indicación predicha, Tumor relacionado con el herpesvirus humano 8 (nivel de evidencia L5). Indicación original: No especificada en el registro (el texto solo indica \"Avelumab\")"
---

# Avelumab
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

# Avelumab: De Avelumab (indicación no detallada) a Tumor Relacionado con el Herpesvirus Humano 8

## Resumen en Una Frase

Avelumab es un anticuerpo monoclonal anti-PD-L1 comercializado en Colombia como BAVENCIO®; el registro sanitario disponible no detalla una indicación específica, pues solo repite el nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para **tumor relacionado con el herpesvirus humano 8** (por ejemplo, sarcoma de Kaposi), pero **actualmente no hay ensayos clínicos ni publicaciones** en los datos compilados que respalden esta dirección; la predicción se basa únicamente en el modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto solo indica "Avelumab") |
| Nueva Indicación Predicha | Tumor relacionado con el herpesvirus humano 8 |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registro vigente) |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, avelumab es un anticuerpo anti-PD-L1 (inhibidor de punto de control inmunitario) que bloquea la interacción entre PD-L1 y su receptor PD-1, con lo que restablece la actividad de los linfocitos T contra las células tumorales.

Los tumores relacionados con el herpesvirus humano 8, como el sarcoma de Kaposi, muestran expresión de PD-L1 y evasión inmunitaria impulsada por el virus, por lo que el bloqueo de puntos de control es biológicamente plausible. Sin embargo, este vínculo es solo una hipótesis: no hay ensayos ni literatura en los datos compilados, y la relación con la indicación original no pudo evaluarse porque el registro no detalla una indicación.

Otras predicciones del listado, como las inmunodeficiencias primarias (deficiencia de adenosina desaminasa, disgenesia reticular, inmunodeficiencia combinada no grave e hipoplasia inmunoeritromieloide), carecen de un mecanismo plausible y probablemente son artefactos de la red del modelo. Las predicciones más creíbles por precedente de clase son las del carcinoma urotelial (uretra prostática y pelvis renal con diferenciación sarcomatoide), dado que avelumab tiene uso establecido como terapia de mantenimiento en carcinoma urotelial avanzado. Esas indicaciones podrían solaparse con el uso ya aprobado, por lo que no serían reposicionamiento en sentido estricto.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20131917 | BAVENCIO® (MERCK S.A.) | Solución para infusión | Avelumab | Cancelado |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Inmunoterapia (anticuerpo monoclonal anti-PD-L1) |
| Riesgo de Mielosupresión | Bajo en general; no es un citotóxico convencional. Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Baja |
| Items de Monitoreo | Hemograma, función hepática, renal y tiroidea, por posibles eventos adversos inmunomediados |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 3 interacciones de nivel **Mayor** (fuente: DDInter):
  - Lenalidomida
  - Pomalidomida
  - Talidomida

Para advertencias y contraindicaciones, consultar el prospecto, ya que no se dispone de esa información en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para tumores relacionados con el herpesvirus humano 8 es de nivel L5: solo hay puntaje del modelo, sin ensayos ni literatura. Además, el único registro sanitario en Colombia está cancelado, lo que limita la viabilidad local inmediata.

**Para avanzar se necesita:**
- Búsqueda dirigida de ensayos y literatura sobre avelumab en sarcoma de Kaposi y otros tumores relacionados con HHV-8
- Para carcinoma urotelial de uretra prostática y de pelvis renal sarcomatoide (candidatos más creíbles, marcados como preguntas de investigación): revisión específica de subgrupos del tracto superior y de histología sarcomatoide, y aclarar si se solapan con la indicación ya aprobada
- Datos detallados del mecanismo de acción (consulta a DrugBank)
- Prospecto de INVIMA con advertencias y contraindicaciones para completar el tamizaje de seguridad
- Aclarar el estado regulatorio actual en Colombia (registro cancelado) y la indicación aprobada original
- Evaluar la relevancia clínica de las interacciones mayores con lenalidomida, pomalidomida y talidomida
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

