---
layout: default
title: Aflibercept
parent: Solo Predicción del Modelo (L5)
nav_order: 30
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Aflibercept: nueva indicación predicha, Esotropía (nivel de evidencia L5). Indicación original: AFLIBERCEPT"
monitor_inn: "AFLIBERCEPT"
predicted_indications: ["esotropia"]
---

# Aflibercept
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

## Aflibercept: De Indicación Original (AFLIBERCEPT, sin descripción detallada) a Esotropía
{: .text-alpha }

## Resumen en Una Frase

Aflibercept es una proteína de fusión recombinante que actúa como "trampa" del VEGF; en el registro sanitario, la indicación aprobada figura únicamente con el nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para **esotropía**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata solo de una predicción del modelo.

<!-- review:begin co-lic-20261105-aflibercept-3 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Aflibercept es una proteína de fusión recombinante que actúa como "trampa" del VEGF y que en Colombia estuvo registrada como solución inyectable intravítrea (Eylia®); en el registro sanitario, la indicación aprobada figura únicamente con el nombre del principio activo." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 2 registros sanitarios (vigentes: 2); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-aflibercept-3 -->

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | AFLIBERCEPT (el registro no detalla la indicación clínica) |
| Nueva Indicación Predicha | Esotropía |
| Puntaje de Predicción TxGNN | 0.9938 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 2 de 2) |
| Número de Registros Sanitarios | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Aflibercept (traducción no oficial): «El factor de crecimiento endotelial vascular A (VEGF-A) y el factor de crecimiento placentario (PlGF) son miembros de la familia VEGF de factores angiogénicos que pueden actuar como factores mitogénicos, quimiotácticos y de permeabilidad vascular para las células endoteliales. El VEGF actúa a través de dos receptores con actividad tirosina cinasa, VEGFR-1 y VEGFR-2, presentes en la superficie de las células endoteliales. […] Los productos de aflibercept actúan como un receptor señuelo soluble que se une al VEGF - A y al PlGF y, de este modo, pueden inhibir la unión y la activación de estos receptores afines del VEGF.» Texto original en inglés: "Vascular endothelial growth factor-A (VEGF-A) and placental growth factor (PlGF) are members of the VEGF family of angiogenic factors that can act as mitogenic, chemotactic, and vascular permeability factors for endothelial cells. VEGF acts via two receptor tyrosine kinases, VEGFR-1 and VEGFR-2, present on the surface of endothelial cells. […] Aflibercept products act as a soluble decoy receptor that binds VEGF - A and PlGF, and thereby can inhibit the binding and activation of these cognate VEGF receptors." ([DailyMed: Pavblu (aflibercept-ayyh) prescribing information, Amgen, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c61062f3-80ec-4a20-8c28-46e468592a06), versión del 2026-10-29; consultado el 2026-11-19). Según la farmacología general, aflibercept es una proteína de fusión recombinante que funciona como trampa de VEGF: se une a VEGF-A, VEGF-B y al factor de crecimiento placentario (PlGF), con lo que reduce la angiogénesis y la permeabilidad vascular.

La esotropía es un trastorno de la alineación ocular, generalmente causado por factores neuromusculares, refractivos o acomodativos. No tiene una patología bien establecida dependiente de VEGF, por lo que el vínculo mecanístico directo es débil.

El puntaje alto (0.9938) probablemente refleja la cercanía en la red de conocimiento con otras enfermedades oculares tratadas con anti-VEGF intravítreo (por ejemplo, retinopatía del prematuro o enfermedad neovascular ocular). Un posible vínculo indirecto sería tratar con anti-VEGF una enfermedad retiniana que cause estrabismo sensorial secundario, lo cual no equivaldría a tratar la esotropía en sí. Por ello, esta predicción debe considerarse con mucha cautela.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 20039088 | EYLIA® SOLUCIÓN PARA INYECCIÓN INTRAVÍTREA | SOLUCION INYECTABLE | AFLIBERCEPT | Vigente |
| 20269865 | EYLIA ® 8MG SOLUCIÓN PARA INYECCIÓN INTRAVÍTREA | SOLUCION INYECTABLE | AFLIBERCEPT | Vigente |

Se muestran los 2 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 78 interacciones en total. Entre las mostradas en los datos compilados:
  - **Mayores**: deferiprona, samario (153Sm) lexidronam, adalimumab, baricitinib, certolizumab pegol, cladribina, clozapina.
  - **Moderadas**: cloruro de estroncio Sr-89, roflumilast, cloranfenicol (incluida la presentación oftálmica), zidovudina, toxoide tetánico, alefacept, alemtuzumab, anakinra, vacuna contra el ántrax, azatioprina, canakinumab y vacuna viva contra el cólera.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y no existe un mecanismo plausible que vincule el bloqueo de VEGF con la esotropía.

<!-- review:begin co-lic-20261105-aflibercept-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción se apoya solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y no existe un mecanismo plausible que vincule el bloqueo de VEGF con la esotropía. Además, el único registro sanitario en Colombia está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 2 registros sanitarios (vigentes: 2); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-aflibercept-2 -->

**Para avanzar se necesita:**
- Datos del mecanismo de acción confirmados (por ejemplo, desde DrugBank).
- Revisión sistemática de la literatura sobre anti-VEGF y estrabismo/esotropía, incluida la posible relación con el estrabismo secundario a enfermedad retiniana.
- Obtener y analizar el prospecto del INVIMA para advertencias y contraindicaciones.
- Evaluación de viabilidad preclínica antes de considerar cualquier estudio clínico.

<!-- review:begin co-lic-20261031-aflibercept-1 -->

> **Corrección de revisión (2026-10-31)**: Texto original: "Aclarar la situación regulatoria actual del producto en Colombia (registro cancelado) y la vía de administración requerida. / Evaluación de viabilidad preclínica antes de considerar cualquier estudio clínico." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-10-31. El medicamento tiene 2 registros sanitarios (vigentes: 2); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261031-aflibercept-1 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-10-31 | Eliminado: "Aclarar la situación regulatoria actual del producto en Colombia (registro cancelado) y la vía de administración requerida" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Además, el único registro sanitario en Colombia está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "y que en Colombia estuvo registrada como solución inyectable intravítrea (Eylia®)" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Pavblu (aflibercept-ayyh) prescribing information, Amgen, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c61062f3-80ec-4a20-8c28-46e468592a06) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

