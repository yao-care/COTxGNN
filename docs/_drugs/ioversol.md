---
layout: default
title: Ioversol
parent: Solo Predicción del Modelo (L5)
nav_order: 228
evidence_level: L5
indication_count: 10
---

# Ioversol
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

# Ioversol: De Medio de Contraste Radiográfico a Susceptibilidad a la Osteoartritis

## Resumen en Una Frase

Ioversol es un medio de contraste yodado que se usa en estudios de imagen radiográfica y no tiene una indicación terapéutica original.
El modelo TxGNN predice que podría ser efectivo para **susceptibilidad a la osteoartritis**, pero esta predicción tiene **0 ensayos clínicos** y **0 publicaciones** que la respalden.
La predicción parece un artefacto del grafo de conocimiento y no una señal terapéutica real.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto registrado es solo "IOVERSOL"). Por su clase, es un medio de contraste yodado. |
| Nueva Indicación Predicha | Susceptibilidad a la osteoartritis |
| Puntaje de Predicción TxGNN | 99.67% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, ioversol es un agente de contraste radiográfico yodado. Su función es aumentar la opacidad de los vasos y tejidos en las imágenes, y no tiene farmacología conocida que modifique enfermedades.

La susceptibilidad genética a la osteoartritis no guarda ninguna relación mecanística con un agente de contraste. El puntaje alto (99.67%) probablemente refleja un artefacto del grafo de conocimiento y no una señal biológica. Por eso, esta predicción no es razonable desde el punto de vista mecanístico.

Las osteoartritis "vecinas" en la lista de predicciones sí tienen estudios, pero evalúan la embolización de arterias genicular, un procedimiento, y no el ioversol como tratamiento. En ese contexto el ioversol solo serviría como contraste angiográfico. Las tres secciones siguientes aclaran este punto.

## Evidencia de Ensayos Clínicos

Para la indicación predicha principal (susceptibilidad a la osteoartritis), actualmente no hay ensayos clínicos relacionados registrados.

**Contexto relacionado (osteoartritis, predicción n.º 2):** existen ensayos sobre embolización arterial en osteoartritis. Ninguno evalúa ioversol como agente terapéutico.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT06497140](https://clinicaltrials.gov/study/NCT06497140) | Fase 3 | Reclutando | 130 | Embolización de arterias genicular vs. simulacro en osteoartritis sintomática de rodilla. Evalúa el procedimiento, no ioversol. |
| [NCT06859164](https://clinicaltrials.gov/study/NCT06859164) | Fase 2 | Reclutando | 50 | Estudio piloto aleatorizado con simulacro de embolización genicular para dolor por osteoartritis de rodilla. El agente evaluado no es ioversol. |
| [NCT04733092](https://clinicaltrials.gov/study/NCT04733092) | Fase 1 | Completado | 22 | Seguridad y eficacia de una emulsión de Lipiodol para embolizar hipervascularización inflamatoria en dolor de rodilla. Lipiodol es otro compuesto yodado, por lo que la relación es solo de clase. |
| [NCT06611007](https://clinicaltrials.gov/study/NCT06611007) | Fase 1/2 | Reclutando | 15 | Seguridad de la embolización con Lipiodol en osteoartritis de mano refractaria. Se evalúa Lipiodol, no ioversol. |

## Evidencia de Literatura

Para la indicación predicha principal, actualmente no hay literatura relacionada disponible.

**Contexto relacionado (osteoartritis, predicción n.º 2):**

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38102013](https://pubmed.ncbi.nlm.nih.gov/38102013/) | 2024 | Cohorte | Diagnostic and Interventional Imaging | Resultados del ensayo LipioJoint-1: seguridad y eficacia de la embolización transitoria de arterias genicular con emulsión de aceite etiodizado en osteoartritis de rodilla. No involucra ioversol. |

## Información de Mercado en Colombia

Se listan 5 entradas en los datos. Todas corresponden al mismo registro sanitario y son idénticas, por lo que se muestran una sola vez. El total reportado es de 20 registros.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 52944 | OPTIRAY ® 350 | Solución inyectable | IOVERSOL (el registro no detalla la indicación) |

Fabricante: Liebel-Flarsheim Company LLC.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ensayos ni literatura propios (nivel L5), y no existe un mecanismo plausible que vincule un medio de contraste con la susceptibilidad genética a la osteoartritis. Las otras nueve predicciones tampoco cuentan con evidencia terapéutica. Los estudios de osteoartritis y de hemoglobinopatía encontrados tratan de procedimientos de embolización o de seguridad del contraste, no de beneficio terapéutico.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank, hoy sin información.
- Prospecto de INVIMA con advertencias y contraindicaciones, para el análisis de seguridad.
- Evidencia preclínica o clínica que muestre actividad terapéutica propia del ioversol, si se quisiera reconsiderar esta dirección.

Los resultados de este informe son solo para investigación y no constituyen consejo médico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

