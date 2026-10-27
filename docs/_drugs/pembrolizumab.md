---
layout: default
title: Pembrolizumab
parent: Solo Predicción del Modelo (L5)
nav_order: 505
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Pembrolizumab: nueva indicación predicha, Fibromatosis gingival (nivel de evidencia L5). Indicación original: No especificada en el registro"
monitor_inn: "PEMBROLIZUMAB"
predicted_indications: ["fibromatosis, gingival", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "hamartoma of lung", "fibroma of lung", "lung benign neoplasm", "ovarioleukodystrophy", "lung germ cell tumor", "pulmonary sulcus neoplasm", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome"]
---

# Pembrolizumab
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

## Pembrolizumab: De Indicación No Especificada en el Registro a Fibromatosis Gingival
{: .text-alpha }

## Resumen en Una Frase

Pembrolizumab (comercializado como KEYTRUDA®) es un anticuerpo monoclonal que bloquea el receptor PD-1. En el registro sanitario colombiano la indicación aparece solo como el nombre del propio fármaco, sin detalle. En el ámbito internacional se usa en cáncer, como melanoma, cáncer de pulmón y otros tumores sólidos.
El modelo TxGNN predice que podría ser efectivo para **fibromatosis gingival**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción: se trata de una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto del registro solo indica "PEMBROLIZUMAB") |
| Nueva Indicación Predicha | Fibromatosis gingival |
| Puntaje de Prediccion TxGNN | 99.40% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Numero de Registros Sanitarios | 1 (cancelado) |
| Decision Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen una descripción formal del mecanismo de acción. Según la información farmacológica disponible, pembrolizumab es un anticuerpo que se une a PD-1 (CD279, gen *PDCD1*). Al bloquear esta vía, restablece la actividad de los linfocitos T contra las células tumorales. Su eficacia está demostrada en múltiples cánceres, como melanoma, cáncer de pulmón de células no pequeñas, cáncer de cabeza y cuello, y tumores con inestabilidad de microsatélites.

La fibromatosis gingival es un sobrecrecimiento del tejido de las encías, de origen hereditario o inducido por fármacos. **No se ha establecido un vínculo mecanístico** con el bloqueo de PD-1, y no se conoce un papel de este bloqueo en esa enfermedad. El puntaje alto del modelo (99.40%) refleja una asociación computacional en el grafo de conocimiento, no evidencia biológica ni clínica.

Por lo tanto, esta predicción debe considerarse una hipótesis sin respaldo. Además, el bloqueo de PD-1 conlleva riesgo de eventos adversos inmunomediados, lo que haría difícil justificar su uso en una condición benigna.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para fibromatosis gingival.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para fibromatosis gingival.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20085509 | KEYTRUDA® 100 MG (MERCK SHARP & DOHME CORP.) | Solución inyectable | PEMBROLIZUMAB | Cancelado |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Inmunoterapia (anticuerpo monoclonal anti-PD-1); no es un citotóxico convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar el prospecto; en la práctica clínica se vigilan función tiroidea, hepática, renal y suprarrenal, dados los eventos adversos inmunomediados |
| Protección en Manejo | Consultar el prospecto y las normas institucionales de manejo de medicamentos oncológicos |

---

## Consideraciones de Seguridad

**Interacciones farmacológicas** (13 registradas):

- **Mayores:** lenalidomida, pomalidomida y talidomida.
- **Moderadas:** corticosteroides (hidrocortisona, triamcinolona, dexametasona, betametasona, budesonida, prednisolona, prednisona, metilprednisolona y deflazacort).
- **Farmacología:** el blanco molecular es PD-1 (CD279).

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para fibromatosis gingival es solo computacional (nivel L5), sin ensayos clínicos ni literatura, y sin un vínculo mecanístico plausible con el bloqueo de PD-1. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y una justificación biológica de por qué el bloqueo de PD-1 sería relevante en la fibromatosis gingival.
- Estudios preclínicos o de mecanismo que respalden la hipótesis.
- Obtener el prospecto y revisar advertencias y contraindicaciones.
- Evaluar el balance riesgo-beneficio frente a los eventos adversos inmunomediados en una enfermedad benigna.

**Nota sobre otras predicciones:** el modelo generó otras nueve predicciones con puntajes similares (99.27%–99.39%), todas con decisión Hold. Las más cercanas al uso establecido de pembrolizumab son el carcinoma del hilio pulmonar y el tumor del surco pulmonar. En el primero, la literatura disponible son solo reportes de caso, y en el segundo no hay evidencia. Para el tumor benigno de pulmón y el tumor de células germinales de pulmón, las evidencias recuperadas se refieren a cánceres de pulmón malignos o a tumores sólidos en general, y no se pueden trasladar directamente. Ninguna de estas predicciones alcanza una evidencia específica suficiente.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

