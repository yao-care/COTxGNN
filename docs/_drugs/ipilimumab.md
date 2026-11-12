---
layout: default
title: Ipilimumab
parent: Solo Predicción del Modelo (L5)
nav_order: 354
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
description: "Ipilimumab: nueva indicación predicha, Coroideremia (nivel de evidencia L5). Indicación original: No especificada"
monitor_inn: "IPILIMUMAB"
predicted_indications: ["choroideremia"]
---

# Ipilimumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Ipilimumab: De Indicación No Especificada en el Registro a Coroideremia
{: .text-alpha }

## Resumen en Una Frase

Ipilimumab es un anticuerpo monoclonal anti-CTLA-4 que potencia la activación de los linfocitos T y es un inmunoterápico oncológico. El registro sanitario colombiano solo consigna el nombre del fármaco como indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **coroideremia**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro solo indica "IPILIMUMAB") |
| Nueva Indicación Predicha | Coroideremia |
| Puntaje de Predicción TxGNN | 0.9906 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Ipilimumab es un anticuerpo anti-CTLA-4. Al bloquear este "freno" inmunológico, favorece la activación y expansión de los linfocitos T contra los tumores. Los datos compilados no incluyen una descripción detallada del mecanismo de acción.

La coroideremia es una degeneración retiniana monogénica ligada al cromosoma X, causada por la pérdida de función del gen *CHM* (proteína REP1). No existe un vínculo mecanístico plausible con el bloqueo de CTLA-4, y el puntaje alto del modelo (0.9906) parece ser un artefacto de la predicción basada en redes de conocimiento.

Además, el bloqueo sistémico de puntos de control inmunitarios conlleva riesgo de eventos adversos oculares de origen inmunitario, como la uveítis. Esto sería indeseable en una enfermedad retiniana degenerativa. Por tanto, esta predicción debe considerarse con mucha cautela.

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
| 20031989 | YERVOY® 5 mg/ml solución inyectable para infusión intravenosa | Solución inyectable | IPILIMUMAB |

Fabricante: Bristol Myers Squibb de Colombia S.A.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Inmunoterapia (anticuerpo monoclonal anti-CTLA-4, inhibidor de punto de control inmunitario) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto; vigilar signos de eventos adversos de origen inmunitario, incluidos los oculares |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Riesgo ocular:** el bloqueo inmunitario sistémico puede causar eventos adversos oculares de origen inmunitario (por ejemplo, uveítis), lo que es especialmente relevante en una enfermedad retiniana.
- **Interacciones farmacológicas:** se identificaron 100 interacciones. Entre las principales se encuentran:
  - **Mayores:** anticoagulantes como apixabán, betrixabán, bivalirudina, dalteparina, desirudina, edoxabán, argatrobán y danaparoide.
  - **Moderadas:**
    - corticosteroides (hidrocortisona, triamcinolona, dexametasona, betametasona, budesonida, prednisolona, prednisona);
    - metronidazol y tinidazol;
    - naltrexona;
    - estatinas (rosuvastatina, simvastatina).

Para advertencias y contraindicaciones, consultar el prospecto, ya que no se dispone de esa información.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción carece de ensayos clínicos y de literatura (nivel L5), no hay un vínculo mecanístico plausible con la coroideremia y existe un riesgo de toxicidad ocular.

<!-- review:begin co-lic-20261105-ipilimumab-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción carece de ensayos clínicos y de literatura (nivel L5), no hay un vínculo mecanístico plausible con la coroideremia y existe un riesgo de toxicidad ocular. Además, el único registro sanitario en Colombia está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-ipilimumab-1 -->

**Para avanzar se necesita:**
- Datos preclínicos o mecanísticos que justifiquen un papel de CTLA-4 en la coroideremia.
- Descripción detallada del mecanismo de acción.
- Advertencias y contraindicaciones del prospecto del INVIMA.

<!-- review:begin co-lic-20261105-ipilimumab-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Advertencias y contraindicaciones del prospecto del INVIMA. / Verificar el estado del registro (solo cancelado) y la indicación aprobada real." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-ipilimumab-2 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Además, el único registro sanitario en Colombia está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Verificar el estado del registro (solo cancelado) y la indicación aprobada real" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

