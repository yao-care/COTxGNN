---
layout: default
title: Fexofenadine
parent: Solo Predicción del Modelo (L5)
nav_order: 283
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
description: "Fexofenadine: nueva indicación predicha, Conjuntivitis por rosácea (nivel de evidencia L5). Indicación original: Fexofenadina (antihistamínico)"
monitor_inn: "Fexofenadine"
predicted_indications: ["rosacea conjunctivitis"]
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

## Fexofenadina: De Antihistamínico para Alergias a Conjuntivitis por Rosácea
{: .text-alpha }

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
| Puntaje de Predicción TxGNN | 0.9985 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 19) |
| Número de Registros Sanitarios | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, fexofenadina es un antagonista selectivo de los receptores H1 de histamina de acción periférica, con eficacia establecida en rinitis alérgica y urticaria crónica.

La hipótesis es que el bloqueo de la inflamación mediada por histamina y de la permeabilidad vascular podría aliviar la inflamación y el enrojecimiento de la superficie ocular que aparecen en la rosácea ocular, de forma similar a lo que ocurre en la conjuntivitis alérgica.

Sin embargo, este vínculo es **hipotético**. La conjuntivitis por rosácea depende principalmente de la disfunción de las glándulas de Meibomio, de factores microbianos o de *Demodex*, y de una desregulación inmune innata y neurovascular. No existe evidencia específica que relacione el antagonismo H1 con esa fisiopatología. El puntaje alto de TxGNN (0.9985) es una predicción computacional, no evidencia clínica.

<!-- review:begin co-lic-20261105-fexofenadine-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Ambos registros están cancelados, por lo que actualmente no hay productos vigentes con este principio activo en el mercado colombiano." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-fexofenadine-1 -->

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20235810 | NASOFREE® | Tableta recubierta | Fexofenadina | Vigente |
| 20191835 | ALERMED® D | Tableta recubierta | Fenilefrina combinaciones | Vigente |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (PrimeKG, no provienen del prospecto):** hipertensión, enfermedad renal, piouréter, diabetes mellitus, cetoacidosis diabética, hiperplasia prostática benigna, enfermedad coronaria, aterosclerosis y arteriosclerosis, glaucoma de ángulo cerrado, hipertiroidismo, enfermedad de Graves y tirotoxicosis. Estas asociaciones probablemente reflejan en gran parte el componente descongestionante (fenilefrina) de las combinaciones, y deben verificarse.
- **Interacciones farmacológicas:** la consulta se completó sin interacciones con otros fármacos; solo se identificó la interacción farmacológica con su diana, el receptor H1 (HRH1), lo cual corresponde a su mecanismo de acción y no a una interacción clínica.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La única base de la propuesta es una predicción computacional (nivel L5) sin ensayos clínicos ni literatura, y el vínculo mecanístico entre el bloqueo H1 y la conjuntivitis por rosácea es hipotético.

<!-- review:begin co-lic-20261105-fexofenadine-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La única base de la propuesta es una predicción computacional (nivel L5) sin ensayos clínicos ni literatura, y el vínculo mecanístico entre el bloqueo H1 y la conjuntivitis por rosácea es hipotético. Además, no hay registros sanitarios vigentes en Colombia." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-fexofenadine-2 -->

**Para avanzar se necesita:**
- Revisión sistemática de literatura sobre antihistamínicos en rosácea ocular y blefaroconjuntivitis
- Datos del mecanismo de acción y estudios preclínicos que vinculen la vía de la histamina con la rosácea ocular
- Evaluación de la compatibilidad de vía de administración (probablemente oftálmica, frente a las formas orales registradas)
- Descargar y revisar el prospecto de INVIMA para obtener advertencias y contraindicaciones oficiales
- Definir la situación regulatoria

<!-- review:begin co-lic-20261105-fexofenadine-3 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Definir la situación regulatoria (nuevo registro o reactivación), dado que los dos registros existentes están cancelados" Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-fexofenadine-3 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Ambos registros están cancelados, por lo que actualmente no hay productos vigentes con este principio activo en el mercado colombiano" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Además, no hay registros sanitarios vigentes en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "(nuevo registro o reactivación), dado que los dos registros existentes están cancelados" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

