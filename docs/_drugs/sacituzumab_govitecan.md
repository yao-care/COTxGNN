---
layout: default
title: Sacituzumab Govitecan
parent: Solo Predicción del Modelo (L5)
nav_order: 576
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-12
description: "Sacituzumab Govitecan: nueva indicación predicha, Osteoporosis inducida por fármacos (nivel de evidencia L5). Indicación original: SACITUZUMAB GOVITECAN"
monitor_inn: "SACITUZUMAB GOVITECAN"
predicted_indications: ["drug-induced osteoporosis", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "diabetic cataract"]
---

# Sacituzumab Govitecan
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

## Sacituzumab Govitecan: De Indicación Original No Especificada a Osteoporosis Inducida por Fármacos
{: .text-alpha }

## Resumen en Una Frase

Sacituzumab govitecan es un conjugado anticuerpo-fármaco (dirigido a Trop-2, con el inhibidor de topoisomerasa I SN-38) citotóxico, registrado en Colombia bajo el nombre comercial TRODELVY®; el registro sanitario no detalla el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **osteoporosis inducida por fármacos**, con un puntaje alto (0.9978).
Actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que se trata solo de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | SACITUZUMAB GOVITECAN (el registro no especifica una indicación en texto) |
| Nueva Indicación Predicha | Osteoporosis inducida por fármacos |
| Puntaje de Predicción TxGNN | 0.9978 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, sacituzumab govitecan es un conjugado anticuerpo-fármaco dirigido a Trop-2 que libera SN-38, un inhibidor de la topoisomerasa I, y pertenece al grupo de agentes antineoplásicos citotóxicos.

Con los datos disponibles, **no se identifica un vínculo mecanístico que respalde esta predicción**. La quimioterapia citotóxica se asocia más frecuentemente con pérdida ósea que con protección ósea, de modo que la relación entre el uso oncológico del fármaco y la osteoporosis inducida por fármacos es, en el mejor de los casos, indirecta (el puntaje del modelo TxGNN (aprendizaje profundo) podría reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, y no una utilidad terapéutica).

El puntaje de 0.9978 proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica ni clínica. Otras predicciones del modelo (retinopatía diabética no proliferativa grave, 0.9969; retinopatía diabética, 0.9960; catarata diabética, 0.9912) tampoco cuentan con ensayos ni literatura, y carecen de una justificación mecanística plausible para un agente citotóxico sistémico.

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
| 20235052 | TRODELVY® | Polvo liofilizado para reconstituir a solución inyectable | SACITUZUMAB GOVITECAN |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Conjugado anticuerpo-fármaco con carga citotóxica (inhibidor de topoisomerasa I, SN-38) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal (según práctica estándar con agentes citotóxicos) |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 40 interacciones en total. Entre las listadas, las de nivel **mayor** incluyen deferiprona, fostamatinib, adalimumab, apalutamida, certolizumab pegol, cladribina, dacomitinib, irinotecán, leflunomida, natalizumab, nilotinib y ozanimod. Las de nivel **moderado** incluyen alefacept, alemtuzumab, anakinra, canakinumab, dimetilfumarato, lorlatinib, ocrelizumab y omacetaxina mepesuccinato. Destacan las combinaciones con otros inmunosupresores o mielosupresores y con irinotecán (cuyo metabolito activo es también SN-38).

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos ni publicaciones que respalden la predicción, no hay un mecanismo plausible (un agente citotóxico se asocia más con pérdida ósea que con protección). El puntaje alto de TxGNN es solo una predicción computacional.

<!-- review:begin co-lic-20261105-sacituzumab_govitecan-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "No existen ensayos clínicos ni publicaciones que respalden la predicción, no hay un mecanismo plausible (un agente citotóxico se asocia más con pérdida ósea que con protección), y el único registro sanitario en Colombia está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-sacituzumab_govitecan-2 -->

**Para avanzar se necesita:**
- Datos del mecanismo de acción del fármaco
- Estudios preclínicos o de mecanismo que justifiquen un vínculo con el metabolismo óseo
- Revisión sistemática de la literatura sobre efectos óseos de este fármaco
- Prospecto con advertencias y contraindicaciones oficiales

<!-- review:begin co-lic-20261031-sacituzumab_govitecan-1 -->

> **Corrección de revisión (2026-10-31)**: Texto original: "Prospecto con advertencias y contraindicaciones oficiales / Aclarar el estado regulatorio actual en Colombia (registro cancelado)" Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-10-31. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261031-sacituzumab_govitecan-1 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-10-31 | Eliminado: "Aclarar el estado regulatorio actual en Colombia (registro cancelado)" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "y el único registro sanitario en Colombia está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

