---
layout: default
title: Meclizine
parent: Solo Predicción del Modelo (L5)
nav_order: 421
evidence_level: L5
indication_count: 6
---

# Meclizine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Meclizina: De MECLOZINA (indicación registrada) a Urticaria Alérgica

## Resumen en Una Frase

Meclizina es un antihistamínico H1 de primera generación con actividad anticolinérgica; en Colombia sus registros sanitarios solo indican "MECLOZINA" como indicación aprobada, y actualmente están cancelados.
El modelo TxGNN predice que podría ser efectivo para **urticaria alérgica**, con un puntaje alto (99.67%).
Sin embargo, hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que se trata solo de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | MECLOZINA (el texto del registro no detalla una enfermedad específica) |
| Nueva Indicación Predicha | Urticaria alérgica |
| Puntaje de Predicción TxGNN | 99.67% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin comercialización vigente) |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, la meclizina es una piperazina antagonista de los receptores H1 de primera generación, con actividad anticolinérgica. Su indicación original en los registros colombianos solo aparece como "MECLOZINA", sin una enfermedad especificada.

La urticaria alérgica está mediada por histamina, y los antihistamínicos H1 son una clase farmacológica establecida para esta condición. Por ello, el bloqueo H1 ofrece un vínculo mecanístico plausible, aunque inferido a nivel de clase y no demostrado para la meclizina.

Conviene ser cautos: el puntaje de TxGNN (0.997) es una predicción computacional, no evidencia clínica. Las guías prefieren los antihistamínicos de segunda generación, por lo que el valor adicional de la meclizina es incierto.

Otras indicaciones predichas, todas con nivel L5 y recomendación Hold, fueron: resfriado común (99.49%), enfermedad de la cavidad nasal (99.48%), faringitis (99.45%), laringofaringitis aguda (99.37%) y urticaria por frío (99.22%). Entre ellas, la urticaria por frío comparte el mismo fundamento mecanístico que la urticaria alérgica, mientras que para faringitis y laringofaringitis el vínculo es débil y el efecto anticolinérgico de sequedad podría ser contraproducente.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20208878 | VERMEC® 25MG | Cápsula blanda | MECLOZINA | Cancelado |
| 19963530 | VERTINON® 25 MG | Tableta | MECLOZINA | Cancelado |

---

## Consideraciones de Seguridad

- **Contraindicaciones sugeridas por el grafo de conocimiento** (relaciones fármaco-enfermedad del grafo de conocimiento, no del texto del prospecto): hiperplasia prostática benigna, glaucoma de ángulo cerrado, estenosis pilórica y obstrucción del cuello vesical. Son coherentes con el efecto anticolinérgico del fármaco.
- **Interacciones farmacológicas**: se identificaron 252 interacciones en total. Las de nivel **mayor** incluyen:
  - Citrato de potasio
  - Cloruro de potasio

  Las de nivel **moderado** incluyen principalmente otros anticolinérgicos (hiosciamina, atropina, glicopirronio, diciclomina, trospio, clidinio, mepenzolato, metescopolamina), opioides (morfina, opio, loperamida), metoclopramida, eliglustat, eluxadolina, nabilona y fenilbutirato de glicerol.
- **Consideración adicional**: la sedación y los efectos adversos anticolinérgicos deben sopesarse frente a un beneficio que sería solo sintomático.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos ni literatura para meclizina en urticaria alérgica; el respaldo se limita a un puntaje de predicción y a una inferencia por clase farmacológica. Además, no hay registros vigentes en Colombia y las alternativas de segunda generación son las preferidas por las guías.

**Para avanzar se necesita:**
- Obtener el prospecto del INVIMA para conocer advertencias y contraindicaciones oficiales
- Completar los datos del mecanismo de acción (consulta a DrugBank)
- Realizar una revisión sistemática de la literatura sobre meclizina en urticaria
- Comparar con los antihistamínicos de segunda generación para definir el valor incremental
- Evaluar la viabilidad regulatoria, dado que ambos registros están cancelados
- Evaluar compatibilidad de vías de administración y similitud con la indicación original (actualmente pendientes)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

