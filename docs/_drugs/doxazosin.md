---
layout: default
title: Doxazosin
parent: Evidencia Moderada (L3-L4)
nav_order: 234
evidence_level: L4
indication_count: 2
---

# Doxazosin
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **2** 
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

# Doxazosina: De Indicación Original (DOXAZOSINA, sin especificar) a Trastorno de Migraña

## Resumen en Una Frase

Doxazosina es un antagonista selectivo de los receptores adrenérgicos alfa-1; el registro sanitario en Colombia solo menciona "DOXAZOSINA" como indicación, sin detallar la enfermedad.
El modelo TxGNN predice que podría ser efectivo para **trastorno de migraña**, pero la evidencia actual es mínima: **0 ensayos clínicos** y **1 publicación** (una revisión/comentario de 1997).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | DOXAZOSINA (el registro no detalla la enfermedad; el texto solo repite el nombre del fármaco) |
| Nueva Indicación Predicha | Trastorno de migraña |
| Puntaje de Predicción TxGNN | 99.20% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo cancelado (sin registros vigentes) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según el conocimiento general, la doxazosina es un bloqueador selectivo de receptores adrenérgicos alfa-1, y su uso establecido se relaciona con el control del tono vascular.

Una posible conexión con la profilaxis de la migraña es la modulación del tono noradrenérgico y vascular: la señalización simpática y adrenérgica puede influir en la reactividad vascular cerebral y en los circuitos centrales de procesamiento del dolor. Esto es **solo una hipótesis**.

El puntaje TxGNN (0.992) es una predicción computacional y no sustituye la evidencia clínica. La única publicación disponible (1997) discute si los bloqueadores alfa-1 tienen cabida en la profilaxis de la migraña, y por su carácter parece ser una revisión o comentario, no un ensayo controlado. Cabe señalar que la relación con la indicación original no se pudo evaluar, pues el registro no especifica una enfermedad.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [9074296](https://pubmed.ncbi.nlm.nih.gov/9074296/) | 1997 | Revisión | Headache | Basado en la experiencia personal del autor, 10 pacientes con migraña recibieron terazosina o doxazosina. Hubo disminución de la frecuencia y/o gravedad de la migraña en todos menos uno, pero 5 pacientes suspendieron el fármaco por efectos secundarios. No se reportaron reacciones adversas graves. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20248384 | DUOMO® 2 MG | Tableta | DOXAZOSINA | Cancelado |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (TxGNN/PrimeKG, no del prospecto)**: atrofia multisistémica, síndrome de taquicardia postural ortostática, hipotensión ortostática, insuficiencia hepática, enfermedad hepática, enfermedad de la vesícula biliar, trastornos hipotensivos, estenosis pilórica, priapismo, síndrome del iris flácido intraoperatorio y obstrucción intestinal.
- **Interacciones farmacológicas**: se identificaron 185 interacciones en total. Las principales de nivel moderado incluyen corticoides (hidrocortisona, triamcinolona, dexametasona, betametasona, budesonida, prednisolona, prednisona), bupropión, morfina, opio, claritromicina, dronabinol, nabilona y los inhibidores de SGLT2 (canagliflozina, dapagliflozina, empagliflozina, ertugliflozina). También hay interacciones de nivel no definido con calcitriol, clotrimazol y cimetidina.
- **Riesgo propio del bloqueo alfa-1**: hipotensión ortostática y síncope, especialmente relevante en pacientes con síntomas autonómicos.

Para advertencias y contraindicaciones del prospecto, consultar el prospecto del producto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia se limita a una publicación de 1997 de carácter descriptivo, sin ensayos clínicos registrados, de modo que el alto puntaje TxGNN no tiene respaldo clínico. Además, el único registro sanitario está cancelado y hay un alto número de interacciones farmacológicas y un riesgo hipotensor que complican el desarrollo.

**Para avanzar se necesita:**
- Revisión sistemática de la literatura sobre bloqueadores alfa-1 en la profilaxis de la migraña
- Datos del mecanismo de acción y análisis del vínculo mecanístico
- Advertencias y contraindicaciones del prospecto aprobado
- Aclarar la indicación original aprobada y la situación del registro cancelado
- Si se continúa, un ensayo piloto controlado con monitoreo de presión arterial ortostática

---

**Nota sobre la segunda predicción:** la *migraña con aura de tronco encefálico* (puntaje 99.19%) no cuenta con ninguna evidencia clínica o bibliográfica propia (nivel L5). Su puntaje probablemente refleja la cercanía al nodo de migraña general, por lo que se recomienda **Hold**, con especial cautela por el uso de fármacos hipotensores en pacientes con síntomas de tronco encefálico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

