---
layout: default
title: Aflibercept
parent: Solo Predicción del Modelo (L5)
nav_order: 30
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
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

Aflibercept es una proteína de fusión recombinante que actúa como "trampa" del VEGF y que en Colombia estuvo registrada como solución inyectable intravítrea (Eylia®); en el registro sanitario, la indicación aprobada figura únicamente con el nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para **esotropía**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata solo de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | AFLIBERCEPT (el registro no detalla la indicación clínica) |
| Nueva Indicación Predicha | Esotropía |
| Puntaje de Predicción TxGNN | 0.9938 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 1) |
| Número de Registros Sanitarios | 1 (0 vigentes, 1 cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la farmacología general, aflibercept es una proteína de fusión recombinante que funciona como trampa de VEGF: se une a VEGF-A, VEGF-B y al factor de crecimiento placentario (PlGF), con lo que reduce la angiogénesis y la permeabilidad vascular.

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

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20039088 | EYLIA® SOLUCIÓN PARA INYECCIÓN INTRAVÍTREA (BAYER A.G.) | Solución inyectable | AFLIBERCEPT | Vigente |

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
La predicción se apoya solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y no existe un mecanismo plausible que vincule el bloqueo de VEGF con la esotropía. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Datos del mecanismo de acción confirmados (por ejemplo, desde DrugBank).
- Revisión sistemática de la literatura sobre anti-VEGF y estrabismo/esotropía, incluida la posible relación con el estrabismo secundario a enfermedad retiniana.
- Obtener y analizar el prospecto del INVIMA para advertencias y contraindicaciones.
- Aclarar la situación regulatoria actual del producto en Colombia (registro cancelado) y la vía de administración requerida.
- Evaluación de viabilidad preclínica antes de considerar cualquier estudio clínico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

