---
layout: default
title: Naproxen
parent: Solo Predicción del Modelo (L5)
nav_order: 292
evidence_level: L5
indication_count: 4
---

# Naproxen
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Naproxeno: De Combinaciones con Tiocolchicósido a Síndrome de Braquidactilia-Sindactilia

## Resumen en Una Frase

El naproxeno es un antiinflamatorio no esteroideo (AINE) que en Colombia se comercializa, entre otros productos, en una combinación con tiocolchicósido. Sus usos clásicos son la artritis reumatoide, la osteoartritis, la espondilitis anquilosante, la tendinitis, la bursitis, la gota aguda y la dismenorrea primaria.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de braquidactilia-sindactilia**, pero hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Combinaciones con tiocolchicósido (texto del registro INVIMA) |
| Nueva Indicación Predicha | Síndrome de braquidactilia-sindactilia |
| Puntaje de Predicción TxGNN | 99.35% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información farmacológica disponible, el naproxeno es un inhibidor no selectivo de COX-1 (PTGS1) y COX-2 (PTGS2), y por eso reduce la síntesis de prostaglandinas. Su eficacia como analgésico y antiinflamatorio en las indicaciones mencionadas está bien establecida.

Sin embargo, **no se ha establecido un vínculo mecanístico** con la nueva indicación. El síndrome de braquidactilia-sindactilia es una malformación congénita de las extremidades. Los datos no conectan la inhibición de prostaglandinas con su patogénesis. El único respaldo es el puntaje del modelo TxGNN (0.994). Como la información de mecanismo de acción del registro está ausente, tampoco se pudo revisar si el fármaco y los genes de la enfermedad comparten dianas. La similitud con la indicación original queda pendiente de evaluar.

Un puntaje alto por sí solo no indica un efecto terapéutico plausible. Otras tres predicciones del modelo (síndrome de microftalmia colobomatosa con displasia rizomélica, displasia acromesomélica tipo Hunter-Thompson y síndrome de braquiolmia con amelogénesis imperfecta) también son síndromes congénitos raros. Todas tienen puntajes de 0.991 a 0.992, sin evidencia adicional ni vínculo mecanístico.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20240091 | MIDOL ® (ANGLOPHARMA S.A.) | Tableta recubierta | Combinaciones tiocolchicósido |

Los datos recibidos repiten este mismo registro cinco veces, por lo que aquí aparece una sola vez. El total reportado es de 20 registros sanitarios. También hay formas farmacéuticas orales (tableta recubierta) y otras (cápsula blanda).

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el puntaje del modelo (nivel L5), sin ensayos clínicos, sin literatura y sin un mecanismo plausible que conecte la inhibición de COX con una malformación congénita de las extremidades. Además, la información de seguridad del prospecto de INVIMA no está disponible, lo que impide avanzar a la evaluación de seguridad.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones).
- Completar el mecanismo de acción desde DrugBank y hacer un análisis independiente de dianas y vías frente a los genes de la enfermedad.
- Buscar literatura y ensayos que relacionen AINE o prostaglandinas con este síndrome.
- Definir la vía de administración requerida y confirmar su compatibilidad con las formas disponibles en Colombia.

*Los resultados son solo para fines de investigación y no constituyen consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

