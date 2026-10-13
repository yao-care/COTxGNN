---
layout: default
title: Nefopam
parent: Solo Predicción del Modelo (L5)
nav_order: 465
evidence_level: L5
indication_count: 10
---

# Nefopam
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

# Nefopam: De Analgésico Central a Craniosinostosis con Catarata

## Resumen en Una Frase

Nefopam es un analgésico no opioide de acción central, registrado en Colombia como solución inyectable (ACUPAN).
El modelo TxGNN predice que podría ser efectivo para **craniosinostosis con catarata** (puntaje de 99.98%), pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción.
La única indicación con algo de literatura es la **estenosis espinal lumbar** (4 publicaciones sobre analgesia perioperatoria), y aun así no evalúa el tratamiento de la enfermedad en sí.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | NEFOPAM (el registro sanitario no detalla la indicación; se trata de un analgésico) |
| Nueva Indicación Predicha | Craniosinostosis con catarata (craniostenosis cataract) |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 1 (0 vigentes, 1 cancelado) |
| Decisión Recomendada | Hold |

**Otras predicciones del modelo:** la mayoría son subtipos de catarata (inmadura, madura, asociada a diabetes tipo 2, tetánica, senil nuclear, cortical, senil y diabética), todas con nivel L5 y decisión Hold. Además, la **estenosis espinal lumbar** (puntaje 99.97%) alcanza el nivel L4 y se clasifica como "pregunta de investigación".

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción oficial del fármaco. Según el análisis disponible, nefopam es un analgésico de acción central que se reporta inhibe la recaptación de serotonina, noradrenalina y dopamina, y modula los canales de sodio y calcio dependientes de voltaje.

**Para craniosinostosis con catarata y los demás subtipos de catarata, no se identificó ningún vínculo mecanístico plausible.** Ni la inhibición de la recaptación de monoaminas ni la modulación de canales iónicos tienen relación reconocida con la opacidad del cristalino o con la patología de la craneosinostosis. Es probable que los puntajes altos, idénticos o casi idénticos entre subtipos, reflejen la similitud en la estructura del grafo de conocimiento dentro del grupo de las cataratas y no una señal biológica real.

**La estenosis espinal lumbar es la excepción parcial.** Aquí existe un vínculo plausible: la acción analgésica de nefopam podría ser relevante para el dolor perioperatorio, la disestesia y el ahorro de opioides en cirugía de columna. Sin embargo, la literatura se refiere a pacientes quirúrgicos y analgesia, no al tratamiento de la estenosis en sí.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

La evidencia corresponde a la estenosis espinal lumbar (no a la indicación principal predicha, para la cual no hay literatura).

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38068520](https://pubmed.ncbi.nlm.nih.gov/38068520/) | 2023 | Estudio clínico aleatorizado doble ciego | Journal of Clinical Medicine | 73 pacientes con estenosis lumbar operados; nefopam 20 mg vs. solución salina para evaluar disestesia, dolor postoperatorio y satisfacción |
| [41937571](https://pubmed.ncbi.nlm.nih.gov/41937571/) | 2026 | Ensayo aleatorizado doble ciego controlado con placebo | Asian Spine Journal | Efecto ahorrador de opioides de nefopam intravenoso continuo tras fusión lumbar degenerativa multinivel |
| [31166320](https://pubmed.ncbi.nlm.nih.gov/31166320/) | 2019 | Estudio clínico/revisión (diseño no confirmado) | Zhurnal Voprosy Neirokhirurgii | Efecto de distintos regímenes de analgesia multimodal sobre la tasa de síndrome de cirugía fallida de espalda en estenosis espinal |
| [25535527](https://pubmed.ncbi.nlm.nih.gov/25535527/) | 2014 | Reporte de caso (seguridad) | Journal of Korean Neurosurgical Society | Estado epiléptico causado por nefopam en un paciente de 71 años operado por estenosis lumbar; señal de seguridad, no de eficacia |

*Nota: los títulos y resúmenes disponibles están truncados, por lo que los diseños de los estudios de 2023 y 2026 no pueden confirmarse por completo.*

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20108472 | ACUPAN SOLUCION INYECTABLE (BIOCODEX) | Solución inyectable | NEFOPAM | Cancelado |

---

## Consideraciones de Seguridad

- **Señal de convulsiones:** se reportó un caso de estado epiléptico atribuido a nefopam (PMID 25535527). En la literatura se describen además efectos adversos anticolinérgicos, cardiovasculares y neuropsiquiátricos (confusión, alucinaciones, delirio y convulsiones). Este riesgo debe ponderarse en cualquier propuesta de reposicionamiento.
- No se encontraron interacciones farmacológicas registradas en la consulta realizada.

Para advertencias y contraindicaciones formales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para craniosinostosis con catarata y los demás subtipos de catarata solo existe una predicción del modelo (L5), sin ensayos, sin literatura y sin mecanismo plausible. Además, el único registro sanitario en Colombia está cancelado. La estenosis espinal lumbar (L4) podría explorarse como pregunta de investigación, pero se limita al contexto de analgesia perioperatoria y conlleva un riesgo de convulsiones.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), un vacío de datos que bloquea el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Confirmar los diseños y resultados de los estudios de 2023 y 2026 en estenosis lumbar.
- Aclarar la situación regulatoria: el registro cancelado implica que no hay producto vigente en Colombia.
- Si se continúa con estenosis lumbar, definir si el objetivo es analgesia perioperatoria (uso ya conocido) o un efecto sobre la enfermedad, y diseñar un plan de monitoreo de riesgo de convulsiones.
- Descartar o justificar biológicamente las predicciones de catarata antes de invertir más recursos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

