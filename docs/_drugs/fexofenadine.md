---
layout: default
title: Fexofenadine
parent: Solo Predicción del Modelo (L5)
nav_order: 283
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Fexofenadine: nueva indicación predicha, Conjuntivitis por rosácea (nivel de evidencia L5). Indicación original: Fexofenadina (antihistamínico)"
---

# Fexofenadine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

# Fexofenadina: De Antihistamínico para Alergias a Conjuntivitis por Rosácea

## Resumen en Una Frase

Fexofenadina es un antihistamínico antagonista selectivo de los receptores H1, originalmente registrado en Colombia como fexofenadina sola y en combinación con fenilefrina para el tratamiento de síntomas alérgicos.
El modelo TxGNN predice que podría ser efectivo para **conjuntivitis por rosácea**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Fexofenadina (antihistamínico) |
| Nueva Indicación Predicha | Conjuntivitis por rosácea |
| Puntaje de Predicción TxGNN | 99.85% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, fexofenadina es un antagonista selectivo de los receptores H1 de histamina de acción periférica, con eficacia establecida en rinitis alérgica y urticaria crónica.

La hipótesis es que el bloqueo de la inflamación mediada por histamina y de la permeabilidad vascular podría aliviar la inflamación y el enrojecimiento de la superficie ocular que aparecen en la rosácea ocular, de forma similar a lo que ocurre en la conjuntivitis alérgica.

Sin embargo, este vínculo es **hipotético**. La conjuntivitis por rosácea depende principalmente de la disfunción de las glándulas de Meibomio, de factores microbianos o de *Demodex*, y de una desregulación inmune innata y neurovascular. No existe evidencia específica que relacione el antagonismo H1 con esa fisiopatología. El puntaje alto de TxGNN (0.998) es una predicción computacional, no evidencia clínica.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20235810 | NASOFREE® | Tableta recubierta | Fexofenadina | Cancelado |
| 20191835 | ALERMED® D | Tableta recubierta | Fenilefrina combinaciones | Cancelado |

Ambos registros están cancelados, por lo que actualmente no hay productos vigentes con este principio activo en el mercado colombiano.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (PrimeKG, no provienen del prospecto):** hipertensión, enfermedad renal, piouréter, diabetes mellitus, cetoacidosis diabética, hiperplasia prostática benigna, enfermedad coronaria, aterosclerosis y arteriosclerosis, glaucoma de ángulo cerrado, hipertiroidismo, enfermedad de Graves y tirotoxicosis. Estas asociaciones probablemente reflejan en gran parte el componente descongestionante (fenilefrina) de las combinaciones, y deben verificarse.
- **Interacciones farmacológicas:** la consulta se completó sin interacciones con otros fármacos; solo se identificó la interacción farmacológica con su diana, el receptor H1 (HRH1), lo cual corresponde a su mecanismo de acción y no a una interacción clínica.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La única base de la propuesta es una predicción computacional (nivel L5) sin ensayos clínicos ni literatura, y el vínculo mecanístico entre el bloqueo H1 y la conjuntivitis por rosácea es hipotético. Además, no hay registros sanitarios vigentes en Colombia.

**Para avanzar se necesita:**
- Revisión sistemática de literatura sobre antihistamínicos en rosácea ocular y blefaroconjuntivitis
- Datos del mecanismo de acción y estudios preclínicos que vinculen la vía de la histamina con la rosácea ocular
- Evaluación de la compatibilidad de vía de administración (probablemente oftálmica, frente a las formas orales registradas)
- Descargar y revisar el prospecto de INVIMA para obtener advertencias y contraindicaciones oficiales
- Definir la situación regulatoria (nuevo registro o reactivación), dado que los dos registros existentes están cancelados
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

