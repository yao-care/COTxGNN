---
layout: default
title: Insulin Glargine
parent: Solo Predicción del Modelo (L5)
nav_order: 223
evidence_level: L5
indication_count: 10
---

# Insulin Glargine
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

# Insulina Glargina: De Diabetes Mellitus a Ooforitis Autoinmune

## Resumen en Una Frase

La insulina glargina es una insulina basal de acción prolongada que se usa para controlar la glucosa en la diabetes. El modelo TxGNN predice que podría ser efectiva para **ooforitis autoinmune**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción. Se trata solo de una señal del grafo de conocimiento, sin un vínculo mecanístico plausible.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Insulina glargina (el registro solo indica el principio activo y no detalla la indicación) |
| Nueva Indicación Predicha | Ooforitis autoinmune |
| Puntaje de Predicción TxGNN | 99.88% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, la insulina glargina es un análogo de insulina basal que actúa sobre el receptor de insulina para regular el metabolismo de la glucosa.

**Esta predicción no tiene una base mecanística plausible.** La insulina glargina no tiene acción inmunomoduladora conocida sobre la autoinmunidad ovárica. El puntaje alto (99.88%) refleja únicamente una asociación en el grafo de conocimiento. No respalda un efecto terapéutico real y no debe interpretarse como tal.

**Otras predicciones del modelo, para contexto:**
- **Agenesia pancreática (puntaje 99.43%, nivel L4):** es la única biológicamente coherente. La deficiencia de insulina justifica el reemplazo con insulina basal. Es más cercana al manejo habitual de la diabetes que a un reposicionamiento real. Las 6 publicaciones encontradas son indirectas: revisiones generales, reportes veterinarios y un caso de MODY5. Ninguna evalúa la insulina glargina en esta condición.
- **Lipodistrofias localizadas (ranks 7 a 10):** probablemente son asociaciones invertidas. La lipohipertrofia y la lipoatrofia en el sitio de inyección son efectos adversos conocidos de la insulina subcutánea. Son una señal de seguridad, no una oportunidad terapéutica.
- **Síndromes de rigidez (ranks 3 y 4), síndrome sensible a tiamina (rank 2) y opsismodisplasia (rank 5):** las asociaciones se explican por comorbilidad con diabetes autoinmune (anti-GAD65) o por la vía INPPL1/SHIP2. No indican un beneficio de la insulina exógena.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Los 5 registros listados en el paquete corresponden al mismo número de registro, por lo que se muestra una sola fila. El total de registros sanitarios del fármaco es 20.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19914262 | LANTUS ® 100 U / ML (SANOFI-AVENTIS DE COLOMBIA S.A.) | Solución inyectable | Insulina glargina |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para ooforitis autoinmune es solo del modelo (nivel L5), sin ensayos ni literatura, y no tiene un mecanismo plausible. No hay base para avanzar.

**Para avanzar se necesita:**
- Obtener el mecanismo de acción desde DrugBank.
- Descargar y revisar el prospecto de INVIMA para advertencias y contraindicaciones.
- Solo si se desea explorar una alternativa, plantear la agenesia pancreática como pregunta de investigación. Requiere evidencia específica, por ejemplo casos neonatales o congénitos.
- Tratar las predicciones de lipodistrofia como señales de seguridad, no como oportunidades terapéuticas.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

