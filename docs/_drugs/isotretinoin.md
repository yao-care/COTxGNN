---
layout: default
title: Isotretinoin
parent: Solo Predicción del Modelo (L5)
nav_order: 232
evidence_level: L5
indication_count: 2
---

# Isotretinoin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Isotretinoína: De Indicación no Especificada en el Registro a Enfermedad Renal Hipertensiva Maligna

## Resumen en Una Frase

Isotretinoína es un retinoide comercializado en Colombia. Los registros sanitarios solo consignan el nombre del principio activo y no una indicación aprobada.
El modelo TxGNN predice que podría ser efectiva para **enfermedad renal hipertensiva maligna**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro solo indica "ISOTETRINOINA", el nombre del principio activo) |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna |
| Puntaje de Predicción TxGNN | 99.01% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la isotretinoína es un retinoide y está comercializada en Colombia como cápsula blanda. Sin embargo, el registro sanitario no detalla para qué indicación fue aprobada, y mecanísticamente su posible aplicación a la enfermedad renal hipertensiva maligna aún no está establecida.

Una hipótesis especulativa es que la señalización de retinoides, en modelos preclínicos, se ha asociado con la supresión de la expresión de renina y con la limitación del daño glomerular. Esta hipótesis no se pudo verificar con los datos disponibles.

TxGNN también predice **hipertensión renovascular maligna** con exactamente el mismo puntaje (99.01%). Esto sugiere que ambas predicciones comparten una misma vía en el grafo de conocimiento y no constituyen señales independientes. La hipertensión maligna es una emergencia médica con tratamiento estándar bien establecido. Por eso, cualquier justificación de reposicionamiento requeriría primero un sólido respaldo preclínico.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Se encontraron 20 registros sanitarios. Los cinco primeros corresponden al mismo registro, por lo que se muestra una sola fila.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20002702 | DERMALONA 20 MG CÁPSULA BLANDA (Laboratorios Bagó de Colombia S.A.S.) | Cápsula blanda | ISOTETRINOINA (sin indicación detallada) |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como referencia, el análisis de racionalidad señala que la isotretinoína tiene una advertencia de teratogenicidad (recuadro negro) y efectos adversos lipídicos y hepáticos. Esto es relevante en una población renal gravemente enferma. No se encontraron interacciones farmacológicas registradas.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción (99.01%) se basa solo en el modelo: no hay ensayos clínicos ni literatura (nivel L5). Además, no se conoce el mecanismo de acción ni la indicación original aprobada, y el perfil de seguridad no se ha evaluado para esta población.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto del INVIMA (advertencias y contraindicaciones), un dato bloqueante para el cribado de seguridad
- Confirmar la indicación aprobada de cada registro sanitario
- Consultar el mecanismo de acción en DrugBank
- Revisar la literatura preclínica sobre retinoides, renina y daño glomerular o vascular
- Evaluar la seguridad (teratogenicidad, dislipidemia, hepatotoxicidad) en pacientes con hipertensión maligna
- Definir la compatibilidad de vía de administración (actualmente pendiente)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

