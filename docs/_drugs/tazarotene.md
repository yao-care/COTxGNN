---
layout: default
title: Tazarotene
parent: Solo Predicción del Modelo (L5)
nav_order: 372
evidence_level: L5
indication_count: 3
---

# Tazarotene
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Tazaroteno: De Acné y Psoriasis en Placas a Dermatitis Seborreica

## Resumen en Una Frase

Tazaroteno es un retinoide tópico que, según fuentes farmacológicas, se usa para el acné, la psoriasis en placas y el fotoenvejecimiento de la piel.
El modelo TxGNN predice que podría ser efectivo para **dermatitis seborreica**,
pero actualmente hay **0 ensayos clínicos relevantes** y **0 publicaciones** que respalden esta dirección: la predicción se apoya solo en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro INVIMA (el campo solo dice "TAZAROTENO"). Según fuente farmacológica: acné y psoriasis en placas |
| Nueva Indicación Predicha | Dermatitis seborreica |
| Puntaje de Predicción TxGNN | 99.79% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

No hay un texto de mecanismo de acción en los datos del fármaco. Sí hay datos farmacológicos de dianas: tazaroteno actúa sobre los receptores del ácido retinoico RAR-α, RAR-β y RAR-γ, con mayor afinidad reportada por RAR-β. Estos receptores regulan la proliferación y la diferenciación de los queratinocitos, y por eso el fármaco se usa en trastornos cutáneos como el acné y la psoriasis.

La dermatitis seborreica es una enfermedad inflamatoria de la piel con recambio epidérmico alterado y descamación. Un efecto normalizador de la queratinización y antiinflamatorio podría, en teoría, ser útil. Esta relación es **especulativa**: se basa únicamente en el puntaje del modelo (0.998) y en la plausibilidad biológica, sin estudios que la confirmen.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT06281782](https://clinicaltrials.gov/study/NCT06281782) | No aplica | Desconocido | 40 | Plasma rico en plaquetas con retinoides tópicos frente a retinoides tópicos solos en acné vulgar. **No evalúa dermatitis seborreica ni prueba tazaroteno**, por lo que no constituye evidencia utilizable (relevancia: grado C) |

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para dermatitis seborreica.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19978012 | TAZAT® GEL 0.05 % (PERCOS S.A) | Gel tópico | Solo figura el principio activo "TAZAROTENO"; no hay texto de indicación |

Los cinco registros devueltos por la consulta corresponden al mismo número sanitario (duplicados), por lo que se muestra una sola fila. El total reportado es de 20 registros.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Los tres elementos que aparecen en el campo de interacciones son en realidad dianas farmacológicas (RARA, RARB y RARG), no interacciones con otros medicamentos. No hay datos de interacciones farmacológicas reales.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para dermatitis seborreica es de nivel L5: tiene un puntaje alto, pero no cuenta con ensayos ni publicaciones que evalúen tazaroteno en esta enfermedad. El único ensayo encontrado trata otra condición (acné).

**Para avanzar se necesita:**
- Hacer una búsqueda dirigida en PubMed y en registros de ensayos sobre tazaroteno o retinoides tópicos en dermatitis seborreica.
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), pendiente para cualquier avance de seguridad.
- Confirmar la indicación aprobada en Colombia, ya que el registro solo muestra el nombre del principio activo.
- Considerar priorizar la segunda predicción, **queratosis seborreica** (L3): existe una revisión sistemática de 2023 y un estudio comparativo de 2004 que parece incluir un brazo con tazaroteno tópico. Ambos deben verificarse para confirmar los resultados y la dirección del efecto.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

