---
layout: default
title: Rotigotine
parent: Evidencia Moderada (L3-L4)
nav_order: 351
evidence_level: L4
indication_count: 10
---

# Rotigotine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
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

# Rotigotina: De Enfermedad de Parkinson a Trastorno por Déficit de Atención e Hiperactividad (TDAH)

## Resumen en Una Frase

Rotigotina es un agonista dopaminérgico de administración transdérmica, utilizado originalmente en la enfermedad de Parkinson y el síndrome de piernas inquietas.
El modelo TxGNN predice que podría ser efectivo para **TDAH**, pero **no hay ensayos clínicos** y solo **3 publicaciones** indirectas (dos revisiones sobre piernas inquietas y un estudio básico de receptores D4). Ninguna prueba la rotigotina en TDAH.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad de Parkinson y síndrome de piernas inquietas (según la farmacología; el texto del registro INVIMA solo dice «Rotigotina») |
| Nueva Indicación Predicha | Trastorno por déficit de atención e hiperactividad (TDAH) |
| Puntaje de Predicción TxGNN | 99.997% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados del mecanismo de acción en el paquete de evidencia. Según la información conocida, la rotigotina actúa sobre los receptores de dopamina D1, D2, D3, D4 y D5. Un estudio estructural de 2023 (Cell Research) la describe como agonista pan-dopaminérgico. Su eficacia en Parkinson y piernas inquietas está establecida, y mecanísticamente podría ser aplicable al TDAH.

El TDAH se asocia con la señalización dopaminérgica. En particular, se han vinculado variantes del receptor D4 (DRD4) y del receptor adrenérgico α2A con este trastorno. Como la rotigotina activa también el receptor D4, existe una base biológica para la hipótesis. Además, las piernas inquietas se describen en la literatura como una condición a menudo comórbida con el TDAH, lo que explica en parte por qué el modelo asocia ambas indicaciones.

Esta relación es **indirecta**. Ninguno de los estudios recuperados evalúa la rotigotina en TDAH, y el puntaje del modelo es solo una predicción. El mecanismo se infiere del conocimiento general de la clase farmacológica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [18656214](https://pubmed.ncbi.nlm.nih.gov/18656214/) | 2008 | Revisión | Revue neurologique | Revisión del síndrome de piernas inquietas (2-3% de la población occidental). No evalúa la rotigotina en TDAH. |
| [21476956](https://pubmed.ncbi.nlm.nih.gov/21476956/) | 2011 | Revisión | Current pharmaceutical design | Revisión de opciones farmacológicas para piernas inquietas en niños. Es una fuente indirecta. |
| [34182128](https://pubmed.ncbi.nlm.nih.gov/34182128/) | 2021 | Preclínico | Pharmacological research | Los heterómeros entre el receptor α2A y variantes del receptor D4 muestran diferencias farmacológicas y funcionales. Relevante para el TDAH, pero sin rotigotina. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20019919 | NEUPRO® 6 MG/24 H (UCB Pharma S.A.) | Sistemas de liberación | Rotigotina (el registro no detalla la indicación) |

Nota: el paquete reporta 20 registros en total, pero los 5 principales corresponden al mismo registro 20019919, repetido.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Las 5 entradas de "interacciones" del paquete corresponden a los receptores diana de la rotigotina (D1 a D5), no a interacciones con otros fármacos. No hay datos de interacciones farmacológicas propiamente dichas.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo y en literatura indirecta: no hay ensayos, y ningún estudio prueba la rotigotina en TDAH. Además, faltan las advertencias y contraindicaciones del prospecto de INVIMA, un vacío de seguridad bloqueante para avanzar.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones).
- Obtener el mecanismo de acción detallado desde DrugBank.
- Realizar una búsqueda dirigida de estudios de rotigotina u otros agonistas dopaminérgicos en TDAH.
- Evaluar la relación beneficio-riesgo de un agonista dopaminérgico en población con TDAH, incluida la pediátrica.

**Otras predicciones del modelo (para referencia):** esquizofrenia tiene nivel L4, con una revisión de clase sobre fármacos prodopaminérgicos y sin ensayos con rotigotina. Los agonistas dopaminérgicos podrían empeorar los síntomas psicóticos, por lo que exige un encuadre de riesgo cuidadoso. Las otras 8 predicciones principales son L5 (solo predicción del modelo) y quedan en Hold.

*Los resultados de este informe son solo de referencia para investigación y no constituyen consejo médico. Todo candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

