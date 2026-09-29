---
layout: default
title: Orlistat
parent: Solo Predicción del Modelo (L5)
nav_order: 308
evidence_level: L5
indication_count: 1
---

# Orlistat
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

# Orlistat: De Indicación No Especificada en el Registro a Hipervitaminosis

## Resumen en Una Frase

Orlistat es un inhibidor de las lipasas gástrica y pancreática que reduce la absorción de grasa de la dieta. En Colombia está registrado y comercializado, pero el texto del registro solo menciona el nombre del principio activo, sin describir una indicación.
El modelo TxGNN predice que podría ser efectivo para **hipervitaminosis**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | "ORLISTAT" (el registro sanitario no incluye un texto de indicación descriptivo) |
| Nueva Indicación Predicha | Hipervitaminosis |
| Puntaje de Predicción TxGNN | 99.42% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos detallados sobre el mecanismo de acción en DrugBank para este farmaco. El análisis del modelo indica que orlistat inhibe las lipasas gástrica y pancreática, con lo que disminuye la absorción de grasa de la dieta.

Como consecuencia, orlistat reduce también la absorción de las vitaminas liposolubles (A, D, E y K), un efecto adverso ya descrito en su etiquetado. Esto da una razón plausible, pero no verificada, para pensar en un posible uso en el exceso de vitaminas liposolubles. No aplicaría a la hipervitaminosis por vitaminas hidrosolubles.

El vínculo no se pudo contrastar con datos curados del farmaco, porque faltan sus indicaciones originales y su mecanismo de acción. Por ahora es solo una hipótesis. Además, el manejo estándar de la hipervitaminosis es retirar la fuente de la vitamina. Cualquier uso de orlistat tendría que sopesarse frente al riesgo de deficiencia de otras vitaminas liposolubles y a los efectos adversos gastrointestinales.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20102710 | FINOBES ® 120 MG. (JOINPHARM S.A.S) | Cápsula dura | ORLISTAT |

Nota: las 5 entradas recibidas corresponden al mismo registro sanitario (20102710) y se muestran una sola vez. El total reportado es de 20 registros.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como dato relevante para esta hipótesis, la reducción de la absorción de vitaminas liposolubles (A, D, E, K) es un efecto adverso conocido de orlistat. No se encontraron interacciones farmacológicas registradas en la consulta realizada.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El puntaje del modelo es muy alto (99.42%), pero no hay ningún ensayo clínico ni publicación que respalde la asociación con hipervitaminosis (nivel L5). Además, el manejo estándar es retirar la fuente de la vitamina, y el efecto de orlistat sobre las vitaminas liposolubles podría causar deficiencias en lugar de un beneficio terapéutico.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA para completar advertencias y contraindicaciones (brecha bloqueante para el tamizaje de seguridad)
- Obtener el mecanismo de acción y las indicaciones originales desde DrugBank
- Hacer una búsqueda sistemática de literatura y ensayos clínicos sobre orlistat en hipervitaminosis por vitaminas liposolubles
- Evaluar el balance riesgo-beneficio: riesgo de deficiencia de otras vitaminas y efectos gastrointestinales
- Aclarar el tipo de hipervitaminosis (liposoluble o hidrosoluble) al que aplicaría la hipótesis

*Este informe es solo para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

