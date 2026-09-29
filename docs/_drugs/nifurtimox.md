---
layout: default
title: Nifurtimox
parent: Solo Predicción del Modelo (L5)
nav_order: 294
evidence_level: L5
indication_count: 7
---

# Nifurtimox
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Nifurtimox: De Indicación No Detallada en el Registro a Analbuminemia Congénita

## Resumen en Una Frase

Nifurtimox es un antiprotozoario del grupo de los nitrofuranos. En Colombia está registrado como LAMPIT® (Bayer), pero el texto del registro no detalla su indicación original.
El modelo TxGNN predice que podría ser efectivo para **analbuminemia congénita**, con **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción.
Es una predicción puramente computacional, sin un vínculo mecanístico identificable.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No detallada en el registro (el campo solo dice «NIFURTIMOX») |
| Nueva Indicación Predicha | Analbuminemia congénita |
| Puntaje de Predicción TxGNN | 99.58% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 4 (2 números de registro únicos, cada uno aparece duplicado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

**No se identificó un vínculo mecanístico que la respalde.** Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Nifurtimox es un nitrofurano antiprotozoario cuya actividad depende de la activación por nitrorreductasas del parásito y del estrés oxidativo que esta genera.

La analbuminemia congénita es un defecto genético raro de la síntesis de albúmina. No hay una razón farmacológica plausible por la cual un antiparasitario con este mecanismo pueda corregirla. El puntaje de 0.996 refleja solo la similitud dentro del grafo de conocimiento, no biología demostrada.

Por ello, la predicción debe leerse como una hipótesis del modelo sin sustento clínico, preclínico ni bibliográfico en los datos recibidos.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20215184 | LAMPIT® 30MG COMPRIMIDOS (Bayer AG) | Tableta | NIFURTIMOX (sin detalle de indicación) |
| 20215915 | LAMPIT® 120MG (Bayer AG) | Tableta | NIFURTIMOX (sin detalle de indicación) |

Nota: los datos traen 4 entradas, pero corresponden a solo 2 números de registro; cada uno aparece dos veces.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como dato de contexto, el propio análisis de la predicción señala que la neuropatía periférica es un efecto adverso conocido de nifurtimox. Esto es relevante para cualquier uso en condiciones hematológicas asociadas a neuropatía.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún ensayo clínico ni publicación que respalde la predicción (nivel L5), y no se identificó un mecanismo plausible entre nifurtimox y la analbuminemia congénita. Las otras seis predicciones (hiperamilasemia, síndrome de hiperviscosidad policlonal, incompatibilidad de grupo sanguíneo, gammapatía monoclonal, enfermedad hematológica premaligna y enfermedad hematológica asociada a neuropatía periférica) también tienen nivel L5, tampoco tienen evidencia y quedan en Hold.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), un vacío bloqueante para el tamizaje de seguridad.
- Completar el mecanismo de acción desde DrugBank para poder evaluar un vínculo mecanístico.
- Aclarar la indicación aprobada en los registros de INVIMA, ya que el texto solo repite el nombre del fármaco.
- Realizar una búsqueda dirigida de literatura y ensayos, incluidos estudios preclínicos, antes de reconsiderar la hipótesis.
- Depurar los registros duplicados en los datos de mercado.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

