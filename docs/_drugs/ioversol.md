---
layout: default
title: Ioversol
parent: Solo Predicción del Modelo (L5)
nav_order: 353
evidence_level: L5
indication_count: 9
monitor_inn: "IOVERSOL"
predicted_indications: ["osteoarthritis", "rheumatoid arthritis", "brachyolmia", "hemoglobinopathy", "brachyolmia-amelogenesis imperfecta syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "myosclerosis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "alopecia"]
last_modified_at: 2026-11-24
description: "Ioversol: nueva indicación predicha, Osteoartritis (nivel de evidencia L5). Indicación original: No especificada en el registro (el texto solo indica \"IOVERSOL\")"
---

# Ioversol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Ioversol: De Indicación no especificada (medio de contraste) a Osteoartritis
{: .text-alpha }

## Resumen en Una Frase

Ioversol es un medio de contraste radiográfico yodado, registrado en Colombia bajo el nombre comercial OPTIRAY® 350; el texto de indicación del registro solo repite el nombre del principio activo.
El modelo TxGNN predice una posible utilidad en **osteoartritis**, pero **no hay ensayos clínicos** y solo **1 publicación** relacionada, que estudia un procedimiento de embolización y no el efecto terapéutico del ioversol.
La predicción debe considerarse una hipótesis de investigación, no una indicación respaldada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto solo indica "IOVERSOL"); por su naturaleza, medio de contraste radiográfico |
| Nueva Indicación Predicha | Osteoartritis |
| Puntaje de Predicción TxGNN | 0.9963 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Ioversol (traducción no oficial): «La inyección intravascular de ioversol opacifica los vasos situados en el trayecto del flujo del medio de contraste, lo que permite la visualización radiográfica de las estructuras internas hasta que se produce una hemodilución significativa. El ioversol puede visualizarse en el parénquima renal entre 30 y 60 segundos después de una inyección intravenosa rápida.» Texto original en inglés: "Intravascular injection of ioversol opacifies those vessels in the path of the flow of the contrast medium, permitting radiographic visualization of the internal structures until significant hemodilution occurs. Ioversol may be visualized in the renal parenchyma within 30 to 60 seconds following rapid intravenous injection." ([DailyMed: Optiray 320 (ioversol) prescribing information, Liebel-Flarsheim Company LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6cb6ca5f-b249-49b0-a9eb-8aa583da7c74), versión del 2025-12-29; consultado el 2026-11-19). Según la información conocida, ioversol es un medio de contraste yodado de uso diagnóstico por imagen; no tiene un mecanismo farmacológico antiartrósico conocido.

La única publicación vinculada (LipioJoint-1, PMID 38102013) evalúa la embolización de arterias geniculares en artrosis de rodilla usando una emulsión a base de aceite etiodizado. Ahí el material yodado actúa como vehículo del procedimiento y no como tratamiento modificador de la enfermedad. Además, es un material distinto del ioversol.

Por ello, el alto puntaje del modelo TxGNN (aprendizaje profundo) probablemente refleja similitudes que el modelo aprendió entre enfermedades relacionadas, y no evidencia biológica ni un efecto terapéutico real. Como ningún estudio citado evalúa directamente el ioversol en osteoartritis, el nivel de evidencia se fija en L5.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38102013](https://pubmed.ncbi.nlm.nih.gov/38102013/) | 2024 | Ensayo clínico de un solo brazo (procedimiento) | Diagnostic and Interventional Imaging | Evalúa la seguridad y eficacia de la embolización transitoria de arterias geniculares con emulsión de aceite etiodizado en artrosis de rodilla. No estudia el ioversol como tratamiento. |

---

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 52944 | OPTIRAY ® 350 | SOLUCION INYECTABLE | IOVERSOL | Vigente |

Se muestra el único registro sanitario de este principio activo en los datos del INVIMA, Código Único de Medicamentos.

<!-- licenses:end -->

<!-- review:begin co-lic-20261124b-ioversol-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "La lista puede ser parcial." Eliminado: advertía que la lista de registros podría ser parcial. La tabla de Información de Mercado en Colombia se genera a partir de los datos del INVIMA (Código Único de Medicamentos, datos al 2026-11-23) e indica cuántos registros muestra del total. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261124b-ioversol-1 -->

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total; entre las mostradas, la mayoría son de nivel **Mayor**, por ejemplo:
  - Metformina
  - Anfotericina B (y sus formulaciones lipídicas y liposomales)
  - Mesalazina, balsalazida, olsalazina y sulfasalazina
  - Vancomicina
  - Aminoglucósidos (kanamicina, neomicina, estreptomicina)
  - Polimixina B
- Con manitol hay una interacción de nivel **Moderado**. Con atropina, famotidina, ácido acetilsalicílico, morfina y omeprazol el nivel es desconocido.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos y la única publicación se refiere a un procedimiento de embolización, no a un efecto terapéutico del ioversol. No existe un mecanismo plausible, por lo que la predicción parece un artefacto del modelo TxGNN (aprendizaje profundo).

**Para avanzar se necesita:**
- Un fundamento mecanístico que justifique un efecto del ioversol en osteoartritis
- Estudios preclínicos o clínicos que evalúen directamente esta indicación
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones)
- Datos del mecanismo de acción del fármaco

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Optiray 320 (ioversol) prescribing information, Liebel-Flarsheim Company LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6cb6ca5f-b249-49b0-a9eb-8aa583da7c74) |
| 2026-11-24 | Eliminado: "La lista puede ser parcial." | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

