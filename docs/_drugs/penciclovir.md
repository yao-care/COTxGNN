---
layout: default
title: Penciclovir
parent: Solo Predicción del Modelo (L5)
nav_order: 507
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
description: "Penciclovir: nueva indicación predicha, Fascioliasis (nivel de evidencia L5). Indicación original: Penciclovir"
monitor_inn: "PENCICLOVIR"
predicted_indications: ["fascioliasis"]
---

# Penciclovir
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

## Penciclovir: De Penciclovir (indicación no detallada) a Fascioliasis
{: .text-alpha }

## Resumen en Una Frase

Penciclovir es un análogo nucleósido de la guanosina con actividad antiviral contra herpesvirus.
El modelo TxGNN predice que podría ser efectivo para **fascioliasis**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo.

<!-- review:begin co-lic-20261105-penciclovir-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Penciclovir es un análogo nucleósido de la guanosina con actividad antiviral contra herpesvirus, comercializado en Colombia como crema tópica (registro hoy cancelado)." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-penciclovir-1 -->

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Penciclovir (el registro sanitario no detalla la indicación aprobada) |
| Nueva Indicación Predicha | Fascioliasis |
| Puntaje de Predicción TxGNN | 0.9906 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción registrado del fármaco. Según el conocimiento farmacológico general, penciclovir es un análogo nucleósido de la guanosina que, tras ser fosforilado por la timidina quinasa viral, inhibe la ADN polimerasa viral. Su actividad es específica contra herpesvirus (VHS-1, VHS-2 y VVZ).

Con la información disponible, **no se identifica un vínculo mecanístico plausible** con la fascioliasis. Fasciola es un trematodo parásito que carece de la timidina quinasa viral necesaria para activar el fármaco, y su ADN polimerasa difiere de la viral. Los tratamientos establecidos para la fascioliasis (por ejemplo, triclabendazol) actúan por mecanismos completamente distintos.

El puntaje alto de TxGNN (0.9906) proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. Debe interpretarse con cautela.

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
| 20205701 | PENCIVIRAL® CREMA | Crema tópica | PENCICLOVIR |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico plausible entre un antiviral específico de herpesvirus y un parásito trematodo. Además, la forma farmacéutica es tópica, lo que no es compatible con una infección hepática parasitaria.

<!-- review:begin co-lic-20261105-penciclovir-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, el único registro sanitario en Colombia está cancelado y la forma farmacéutica es tópica, lo que no es compatible con una infección hepática parasitaria." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-penciclovir-2 -->

**Para avanzar se necesita:**
- Obtener el mecanismo de acción desde DrugBank y analizar su relación con la biología de Fasciola.
- Descargar y revisar el prospecto de INVIMA para completar advertencias y contraindicaciones (requisito previo al tamizaje de seguridad).
- Buscar evidencia preclínica (in vitro o in vivo) que sustente alguna actividad antiparasitaria.
- Evaluar la compatibilidad de vía de administración, dado que solo existió una presentación tópica.
- Contrastar con los tratamientos establecidos (p. ej., triclabendazol) antes de considerar cualquier inversión adicional.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "comercializado en Colombia como crema tópica (registro hoy cancelado)" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "el único registro sanitario en Colombia está cancelado y" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

