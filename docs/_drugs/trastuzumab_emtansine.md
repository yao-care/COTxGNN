---
layout: default
title: Trastuzumab Emtansine
parent: Solo Predicción del Modelo (L5)
nav_order: 393
evidence_level: L5
indication_count: 4
---

# Trastuzumab Emtansine
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

# Trastuzumab emtansina: De Indicación Original No Especificada a Subtipo "Normal-Like" de Carcinoma de Mama

## Resumen en Una Frase

Trastuzumab emtansina (T-DM1) es un conjugado anticuerpo-fármaco dirigido a HER2, comercializado en Colombia bajo la marca Kadcyla®. Los datos recibidos no describen su indicación original.
El modelo TxGNN predice que podría ser efectivo para el **subtipo normal-like del carcinoma de mama**, con **1 ensayo clínico** (Fase 2, en reclutamiento, sin resultados) y **ninguna publicación** que respalde esta dirección por ahora.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible. El texto registrado en INVIMA solo dice "TRASTUZUMAB EMTANSINA" (nombre del principio activo, sin indicación) |
| Nueva Indicación Predicha | Subtipo normal-like del carcinoma de mama |
| Puntaje de Predicción TxGNN | 99.82% |
| Nivel de Evidencia | L5 (ver nota abajo) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 8 |
| Decisión Recomendada | Hold |

**Nota sobre el nivel de evidencia:** el Evidence Pack asigna L3 a esta predicción. Con las reglas de nivel, hay un solo ensayo de Fase 2 aún en reclutamiento y ninguna publicación, ni observacional ni revisión sistemática. Por eso aquí se clasifica como L5. La evidencia real (Fase 2 en curso) está en el límite entre L5 y L3, pero no cumple los requisitos de L3.

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, T-DM1 es un conjugado anticuerpo-fármaco: trastuzumab (que se une a HER2) unido al inhibidor de microtúbulos DM1. Su eficacia en el cáncer de mama depende de la expresión de HER2, no del subtipo intrínseco del tumor.

Aquí está el punto débil de la predicción. El subtipo normal-like suele ser HER2-bajo o HER2-negativo, así que el vínculo mecanístico es débil, salvo que se confirme positividad de HER2. El puntaje TxGNN tan alto (99.82%) probablemente refleja la cercanía en el grafo con otros nodos de cáncer de mama, no una razón biológica específica para este subtipo.

Por lo tanto, esta predicción debe leerse como una pregunta de investigación. Solo tendría sentido en tumores de este subtipo que resulten HER2-positivos.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT06348134](https://clinicaltrials.gov/study/NCT06348134) | Fase 2 | En reclutamiento | 74 | Terapia anti-HER2 neoadyuvante y adyuvante en mujeres nigerianas con cáncer de mama HER2+. Inicio: marzo de 2025; fin previsto: 2036. Sin resultados. |

Este ensayo solo respalda la factibilidad del enfoque anti-HER2, no la eficacia en este subtipo. El título recibido está truncado, así que no se puede confirmar que use T-DM1 ni cómo se aleatoriza.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Según el campo `total_licenses`, hay 8 registros. El detalle recibido solo muestra 2 números distintos; el resto son repeticiones del mismo número.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20058197 | Kadcyla® 100 mg/vial (F. Hoffmann-La Roche Ltd.) | Polvo liofilizado para reconstituir a solución inyectable | Solo figura "Trastuzumab emtansina" (sin indicación descrita) |
| 20064940 | Kadcyla® 160 mg/vial (F. Hoffmann-La Roche Ltd.) | Polvo liofilizado para reconstituir a solución inyectable | Solo figura "Trastuzumab emtansina" (sin indicación descrita) |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida: conjugado anticuerpo-fármaco anti-HER2 con carga citotóxica (DM1, inhibidor de microtúbulos) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto; por su carga citotóxica, aplicar las regulaciones de manejo de fármacos citotóxicos de la institución |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas en la consulta realizada.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Hay un solo ensayo de Fase 2 en curso, sin resultados y sin confirmación de que use T-DM1. No hay publicaciones. El vínculo mecanístico es débil, porque el subtipo normal-like suele ser HER2-bajo o HER2-negativo, y el puntaje alto de TxGNN parece reflejar cercanía en el grafo más que biología.

**Para avanzar se necesita:**
- Confirmar el estado de HER2 de los tumores normal-like que se quieran tratar. Sin HER2 positivo no hay base mecanística.
- Verificar en el registro completo de NCT06348134 si T-DM1 forma parte del tratamiento.
- Obtener el prospecto de INVIMA para completar indicaciones aprobadas, advertencias y contraindicaciones.
- Obtener los datos del mecanismo de acción desde DrugBank.
- Hacer una búsqueda de literatura específica sobre T-DM1 en el subtipo normal-like.
- Tener en cuenta que otros subtipos del mismo Evidence Pack (por ejemplo, receptor de progesterona negativo con HER2+) cuentan con evidencia mucho más sólida, incluidos ensayos de Fase 3. Vale la pena priorizarlos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

