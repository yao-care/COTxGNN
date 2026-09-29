---
layout: default
title: Ocrelizumab
parent: Solo Predicción del Modelo (L5)
nav_order: 299
evidence_level: L5
indication_count: 5
---

# Ocrelizumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Ocrelizumab: De Indicación No Especificada en el Registro a Carcinoma de Mama HER2 Positivo

## Resumen en Una Frase

Ocrelizumab es un anticuerpo monoclonal anti-CD20 que depleta linfocitos B. El registro sanitario colombiano solo lista el nombre del principio activo y no detalla la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **carcinoma de mama HER2 positivo**, pero con **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. La predicción se basa únicamente en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el campo solo indica "OCRELIZUMAB") |
| Nueva Indicación Predicha | Carcinoma de mama HER2 positivo |
| Puntaje de Predicción TxGNN | 99.89% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 8 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro de origen. Lo que se sabe es que ocrelizumab es un anticuerpo anti-CD20 que depleta células B.

No se identifica un vínculo creíble con el carcinoma de mama HER2 positivo. No se conoce que las células tumorales de este subtipo expresen CD20 como diana terapéutica. El puntaje alto (0.999) es una predicción basada en grafos de conocimiento y no debe interpretarse como evidencia de eficacia.

Las otras cuatro predicciones del modelo también son subtipos de cáncer de mama (receptor de progesterona positivo, subtipo similar a mama normal, luminal A/B y receptor de progesterona negativo), todas con puntajes cercanos a 0.998. Dos de ellas tienen puntajes idénticos, lo que sugiere propagación por vecindad en la ontología y no señales independientes. Una hipótesis futura solo podría apoyarse en la biología de los linfocitos B infiltrantes de tumor, y hoy no existe ningún estudio que la sustente.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

Nota: para la cuarta predicción (tumor de mama luminal A o B) se recuperaron publicaciones, pero corresponden a coincidencias por la letra "B" (biología de células B, vacunas contra hepatitis B, alelos HLA-B, bacterioclorofila b). Ninguna trata sobre ocrelizumab, CD20 ni cáncer de mama, por lo que no elevan el nivel de evidencia.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20115374 | OCREVUS® concentrado para solución para infusión 300 mg/10 mL (F. Hoffmann-La Roche Ltd.) | Solución concentrada para infusión | No detallada (el registro solo indica "OCRELIZUMAB") |

Nota: el registro devuelve varias entradas duplicadas del mismo número de registro sanitario, por lo que se muestra una sola fila.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se obtuvieron advertencias ni contraindicaciones, y no se encontraron interacciones farmacológicas registradas.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (L5), sin ensayos clínicos ni literatura pertinente, y sin un mecanismo plausible que conecte la depleción de células B con el cáncer de mama HER2 positivo. Además, faltan datos de seguridad y del mecanismo de acción, por lo que no se justifica avanzar.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA para obtener advertencias y contraindicaciones (brecha bloqueante para el tamizaje de seguridad).
- Obtener el mecanismo de acción desde DrugBank.
- Confirmar la indicación aprobada en Colombia, ya que el registro solo indica el nombre del principio activo.
- Realizar una búsqueda bibliográfica dirigida (ocrelizumab/anti-CD20 y cáncer de mama, linfocitos B infiltrantes de tumor) que reemplace los resultados irrelevantes actuales.
- Evaluar si existe alguna base preclínica antes de reconsiderar la decisión.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

