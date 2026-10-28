---
layout: default
title: Biperiden
parent: Solo Predicción del Modelo (L5)
nav_order: 108
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Biperiden: nueva indicación predicha, Encefalitis subaguda de Rasmussen (nivel de evidencia L5). Indicación original: Biperideno"
monitor_inn: "biperiden"
predicted_indications: ["Rasmussen subacute encephalitis", "myelitis", "PLA2G6-associated neurodegeneration", "transaldolase deficiency", "fructose-1,6-bisphosphatase deficiency", "progressive supranuclear palsy-corticobasal syndrome", "paralysis agitans, juvenile, of Hunt", "Lewy body dementia", "attention deficit-hyperactivity disorder", "X-linked intellectual disability-ataxia-apraxia syndrome"]
---

# Biperiden
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Biperideno: De Indicación Original (Biperideno) a Encefalitis Subaguda de Rasmussen
{: .text-alpha }

## Resumen en Una Frase

Biperideno es un anticolinérgico oral (comprimidos) que en Colombia se registró con la indicación "Biperideno", sin un texto de indicación más detallado en los registros sanitarios.
El modelo TxGNN predice que podría ser efectivo para **encefalitis subaguda de Rasmussen**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción; se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Biperideno (el registro sanitario no detalla la indicación) |
| Nueva Indicación Predicha | Encefalitis subaguda de Rasmussen |
| Puntaje de Predicción TxGNN | 0.9994 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 2) |
| Número de Registros Sanitarios | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, biperideno es un antagonista muscarínico de acción central, con preferencia por el receptor M1, usado en el parkinsonismo idiopático y el inducido por fármacos.

La encefalitis de Rasmussen es una enfermedad neurológica rara, de origen autoinmune y mediada por linfocitos T, que causa inflamación cerebral crónica, epilepsia y deterioro neurológico. No se ha establecido un vínculo plausible entre el bloqueo muscarínico y esta patología. El puntaje alto de TxGNN parece reflejar una asociación computacional en la red de conocimiento, no un fundamento biológico demostrado.

Por lo tanto, la predicción debe considerarse una hipótesis sin respaldo clínico ni mecanístico.

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
| 32998 | AKINETON® TABLETAS (estado: vigente) | Tableta | Biperideno |
| 19900906 | BIPERIDENO 2 MG (estado: vigente) | Tableta | Biperideno |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 75 interacciones en total. Entre las principales:
  - **Mayores**: cloruro de potasio y citrato de potasio.
  - **Moderadas** (entre otras): otros anticolinérgicos (atropina, hiosciamina, diciclomina, glicopirronio, propantelina, clidinio, mepenzolato, metscopolamina), opioides y relacionados (morfina, loperamida, opio, eluxadolina), cannabinoides (dronabinol, nabilona), metoclopramida y pramlintida.
- **Condiciones de riesgo según el grafo de conocimiento** (relaciones fármaco-enfermedad de contraindicación en TxGNN/PrimeKG, no provienen del prospecto): glaucoma de ángulo abierto y de ángulo cerrado, hiperplasia prostática benigna, miastenia gravis, íleo paralítico, acalasia/megaesófago, hernia de hiato, colitis ulcerosa y enfermedad inflamatoria intestinal, colitis por *Clostridium difficile*, enterocolitis necrosante perinatal, enfermedad coronaria, enfermedad de conducción cardíaca, paro cardíaco súbito, hipertensión, hipotensión, EPOC, úlcera gástrica, enfermedad renal, hepática y de la vesícula biliar, y piourétero.

No se dispone de advertencias ni contraindicaciones del prospecto; se debe consultar el prospecto para esta información.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo computacional (nivel L5), sin ensayos ni literatura, y no existe un vínculo mecanístico plausible entre un antagonista muscarínico y una enfermedad autoinmune mediada por linfocitos T. Además, el fármaco no tiene registros sanitarios vigentes en Colombia.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto aprobado (advertencias y contraindicaciones), que es un vacío bloqueante para el tamizaje de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Evidencia preclínica o clínica que justifique un papel de la vía colinérgica en la encefalitis de Rasmussen.
- Revisar las otras predicciones del modelo con más sustento biológico (por ejemplo, formas de parkinsonismo, como el parkinsonismo juvenil), que tampoco cuentan hoy con evidencia directa.
- Aclarar la situación regulatoria, dado que ambos registros están cancelados.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

