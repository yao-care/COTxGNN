---
layout: default
title: Ravulizumab
parent: Solo Predicción del Modelo (L5)
nav_order: 552
evidence_level: L5
indication_count: 10
---

# Ravulizumab
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

# Ravulizumab: De Indicación Original No Especificada a Neutropenia Congénita Grave por Deficiencia de G6PC3

## Resumen en Una Frase

Ravulizumab es un inhibidor del complemento C5 comercializado en Colombia como Ultomiris®. En el registro sanitario disponible no consta un texto de indicación aprobada, solo el nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para **neutropenia congénita grave autosómica recesiva por deficiencia de G6PC3**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata solo de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (el registro solo indica "Ravulizumab") |
| Nueva Indicación Predicha | Neutropenia congénita grave autosómica recesiva por deficiencia de G6PC3 |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, ravulizumab es un anticuerpo monoclonal que inhibe el componente C5 del complemento, bloqueando la vía terminal del complemento.

La neutropenia congénita por deficiencia de G6PC3 es un trastorno del metabolismo y la supervivencia de los neutrófilos. No se ha establecido un mecanismo mediado por el complemento en esta enfermedad, por lo que no es posible verificar un vínculo mecanístico entre la inhibición de C5 y la nueva indicación.

La alta puntuación (0.9996) refleja únicamente una predicción basada en la red de conocimiento. Sin ensayos, literatura ni datos del mecanismo original, la razonabilidad biológica de esta predicción no está respaldada. Cabe señalar que el modelo generó otras nueve predicciones con puntajes similares (entre 99.80% y 99.94%), en su mayoría trastornos hematológicos raros (por ejemplo, neutropenia cíclica, neutropenia congénita grave, hiperoxaluria primaria), todas también sin evidencia clínica.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20224196 (cancelado) | ULTOMIRIS® | Solución concentrada para infusión | Ravulizumab |

---

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento TxGNN, no texto del prospecto)**: infección meningocócica.
- **Interacciones Farmacológicas**: se identificaron 4 interacciones de nivel menor con inmunoglobulina G humana (intravenosa, subcutánea, intramuscular, e intravenosa/subcutánea).
- **Consideración adicional**: el bloqueo del complemento terminal aumenta el riesgo de infecciones, y esto podría ser más relevante en poblaciones con inmunodeficiencia o neutropenia.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo computacional (nivel L5), sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico plausible entre la inhibición de C5 y la neutropenia por deficiencia de G6PC3. Además, el único registro sanitario en Colombia está cancelado y faltan datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Datos del mecanismo de acción desde DrugBank y análisis del vínculo mecanístico con la nueva indicación
- Obtener y analizar el prospecto del INVIMA (advertencias y contraindicaciones), requisito para el tamizaje de seguridad
- Aclarar la indicación aprobada original y la situación regulatoria del registro cancelado
- Revisión sistemática de literatura y ensayos que evalúen el papel del complemento en la neutropenia congénita
- Evaluación del riesgo de infecciones (especialmente meningocócicas) en una población neutropénica o inmunodeficiente
- Estudios preclínicos que respalden la hipótesis antes de considerar cualquier estudio clínico
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

