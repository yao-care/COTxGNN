---
layout: default
title: Penciclovir
parent: Solo Predicción del Modelo (L5)
nav_order: 507
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Penciclovir: nueva indicación predicha, Fascioliasis (nivel de evidencia L5). Indicación original: Penciclovir"
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

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Penciclovir: De Penciclovir (indicación no detallada) a Fascioliasis

## Resumen en Una Frase

Penciclovir es un análogo nucleósido de la guanosina con actividad antiviral contra herpesvirus, comercializado en Colombia como crema tópica (registro hoy cancelado).
El modelo TxGNN predice que podría ser efectivo para **fascioliasis**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Penciclovir (el registro sanitario no detalla la indicación aprobada) |
| Nueva Indicación Predicha | Fascioliasis |
| Puntaje de Predicción TxGNN | 99.06% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción registrado del fármaco. Según el conocimiento farmacológico general, penciclovir es un análogo nucleósido de la guanosina que, tras ser fosforilado por la timidina quinasa viral, inhibe la ADN polimerasa viral. Su actividad es específica contra herpesvirus (VHS-1, VHS-2 y VVZ).

Con la información disponible, **no se identifica un vínculo mecanístico plausible** con la fascioliasis. Fasciola es un trematodo parásito que carece de la timidina quinasa viral necesaria para activar el fármaco, y su ADN polimerasa difiere de la viral. Los tratamientos establecidos para la fascioliasis (por ejemplo, triclabendazol) actúan por mecanismos completamente distintos.

El puntaje alto de TxGNN (0.99) probablemente refleja la proximidad en la red del grafo de conocimiento y no una justificación biológica. Debe interpretarse con cautela.

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
| 20205701 (cancelado) | PENCIVIRAL® CREMA | Crema tópica | PENCICLOVIR |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico plausible entre un antiviral específico de herpesvirus y un parásito trematodo. Además, el único registro sanitario en Colombia está cancelado y la forma farmacéutica es tópica, lo que no es compatible con una infección hepática parasitaria.

**Para avanzar se necesita:**
- Obtener el mecanismo de acción desde DrugBank y analizar su relación con la biología de Fasciola.
- Descargar y revisar el prospecto de INVIMA para completar advertencias y contraindicaciones (requisito previo al tamizaje de seguridad).
- Buscar evidencia preclínica (in vitro o in vivo) que sustente alguna actividad antiparasitaria.
- Evaluar la compatibilidad de vía de administración, dado que solo existió una presentación tópica.
- Contrastar con los tratamientos establecidos (p. ej., triclabendazol) antes de considerar cualquier inversión adicional.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

