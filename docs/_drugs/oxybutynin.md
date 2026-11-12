---
layout: default
title: Oxybutynin
parent: Solo Predicción del Modelo (L5)
nav_order: 490
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-12
description: "Oxybutynin: nueva indicación predicha, Síndrome de piernas inquietas (nivel de evidencia L5). Indicación original: No especificada en el registro (el texto indica solo \"OXIBUTININA\")"
monitor_inn: "Oxybutynin"
predicted_indications: ["restless legs syndrome", "gastroduodenitis", "peptic ulcer disease"]
---

# Oxybutynin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Oxibutinina: De Indicación No Especificada en el Registro a Síndrome de Piernas Inquietas
{: .text-alpha }

## Resumen en Una Frase

Oxibutinina es un antiespasmódico musculotrópico con acción anticolinérgica moderada, utilizado clínicamente para la vejiga hiperactiva; su único registro sanitario en Colombia solo menciona "OXIBUTININA" como indicación.
El modelo TxGNN predice que podría ser efectiva para el **síndrome de piernas inquietas**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.
La predicción se basa únicamente en el modelo (nivel L5).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto indica solo "OXIBUTININA"); uso clínico conocido: vejiga hiperactiva |
| Nueva Indicación Predicha | Síndrome de piernas inquietas |
| Puntaje de Predicción TxGNN | 0.9974 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 5 de 5) |
| Número de Registros Sanitarios | 5 (vigentes: 5) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información farmacológica disponible, la oxibutinina actúa sobre los receptores muscarínicos M1 a M5 (CHRM1–CHRM5) y se usa en la vejiga hiperactiva.

Un vínculo hipotético sería que su actividad antimuscarínica modulara el equilibrio colinérgico/dopaminérgico central, lo cual es **especulativo**. Además, en general se reporta que los fármacos anticolinérgicos empeoran, y no mejoran, los síntomas de piernas inquietas, lo que va en contra de la predicción.

Por lo tanto, el puntaje alto proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica; no cuenta con respaldo mecanístico ni clínico verificable.

### Otras predicciones del modelo

| Posición | Indicación Predicha | Puntaje TxGNN | Nivel de Evidencia | Recomendación |
|------|------|------|------|------|
| 2 | Gastroduodenitis | 0.9962 | L5 | Hold |
| 3 | Enfermedad ulcerosa péptica | 0.9931 | L5 | Hold |

Para la gastroduodenitis no hay ensayos ni publicaciones. Para la úlcera péptica solo existen estudios indirectos y antiguos (un estudio clínico de 1964, una revisión farmacológica de 1965 y un reporte de caso de 1990 sobre esofagitis por reflujo inducida por oxibutinina, que es una señal de seguridad en contra del uso gastrointestinal alto).

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para el síndrome de piernas inquietas.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para el síndrome de piernas inquietas.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20099350 | SINORIN® | Tableta cubierta con película | OXIBUTININA | Vigente |

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (no provienen del texto del prospecto): hipertensión, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, hiperplasia prostática benigna, enfermedad coronaria, paro cardíaco súbito, enfermedad de conducción cardíaca, glaucoma de ángulo cerrado, miastenia gravis, colitis ulcerosa y enfermedad inflamatoria intestinal, hipertiroidismo (enfermedad de Graves, tirotoxicosis), hernia de hiato, íleo paralítico y obstrucción intestinal, obstrucción del cuello vesical, megacolon tóxico, reflujo gastroesofágico y esofagitis.
- **Interacciones farmacológicas**: los datos compilados solo muestran la unión a los receptores muscarínicos M1–M5; no hay interacciones con otros fármacos con nivel de gravedad definido.
- **Señal de seguridad relevante**: un reporte de caso (1990) asoció la oxibutinina con esofagitis por reflujo, por disminución del tono del esfínter esofágico inferior.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5), sin ensayos ni literatura, y el perfil anticolinérgico del fármaco sugiere que podría empeorar el síndrome de piernas inquietas.

<!-- review:begin co-lic-20261105-oxybutynin-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción se basa solo en el modelo (L5), sin ensayos ni literatura, y el perfil anticolinérgico del fármaco sugiere que podría empeorar el síndrome de piernas inquietas. Además, el único registro sanitario en Colombia está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 5 registros sanitarios (vigentes: 5); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-oxybutynin-1 -->

**Para avanzar se necesita:**
- Obtener el prospecto del INVIMA para completar la revisión de advertencias y contraindicaciones.
- Completar los datos del mecanismo de acción desde DrugBank.
- Revisar la literatura sobre anticolinérgicos y síndrome de piernas inquietas, incluyendo evidencia de empeoramiento de síntomas.
- Si se desea explorar alternativas, priorizar el análisis de las otras predicciones (gastroduodenitis, úlcera péptica), valorando la señal de seguridad de reflujo esofágico.
- Evaluar la viabilidad regulatoria.

<!-- review:begin co-lic-20261105-oxybutynin-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Evaluar la viabilidad regulatoria, dado que no hay registros vigentes en Colombia." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 5 registros sanitarios (vigentes: 5); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-oxybutynin-2 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Además, el único registro sanitario en Colombia está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "dado que no hay registros vigentes en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

