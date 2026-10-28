---
layout: default
title: Ruxolitinib
parent: Solo Predicción del Modelo (L5)
nav_order: 575
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
monitor_inn: "ruxolitinib"
predicted_indications: ["uterine corpus perivascular epithelioid cell tumor", "benign PEComa", "lymphangiomyoma", "lymphangioleiomyomatosis", "liposarcoma", "familial rhabdoid tumor", "lung PEComa", "ovarian myxoid liposarcoma", "acquired hemophagocytic lymphohistiocytosis associated with malignant disease", "hemophagocytic syndrome associated with an infection"]
description: "Ruxolitinib: nueva indicación predicha, Uterine corpus perivascular epithelioid cell tumor (nivel de evidencia L5). Indicación original: RUXOLITINIB"
---

# Ruxolitinib
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

## Ruxolitinib: Uterine corpus perivascular epithelioid cell tumor
{: .text-alpha }

## Resumen en Una Frase

Ruxolitinib (comercializado como JAKAVI®) es un inhibidor de las quinasas JAK1/JAK2. El registro sanitario colombiano solo menciona el nombre del principio activo, sin detallar la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para el **tumor de células epitelioides perivasculares (PEComa) del cuerpo uterino**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción específica. Se trata de una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | RUXOLITINIB |
| Nueva Indicación Predicha | Uterine corpus perivascular epithelioid cell tumor |
| Puntaje de Predicción TxGNN | 0.9973 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 3) |
| Número de Registros Sanitarios | 3 (todos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción detallado. Según la información conocida, ruxolitinib actúa inhibiendo JAK1 y JAK2, componentes de la vía de señalización JAK-STAT, que regula la respuesta inflamatoria y la proliferación celular.

Para el PEComa uterino, el vínculo mecanístico **no está establecido**. Estos tumores suelen depender de la activación de la vía mTOR, por pérdida de TSC1/TSC2, y no de la vía JAK-STAT. La alta puntuación del modelo probablemente refleja la cercanía en la red de conocimiento con enfermedades relacionadas de la familia PEComa (linfangioleiomiomatosis, PEComa benigno, PEComa de pulmón) y no una relación biológica demostrada.

Por eso esta predicción debe leerse como una hipótesis generada por el modelo. Cualquier contribución de JAK-STAT en estos tumores tendría que demostrarse primero en estudios preclínicos.

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
| 20055293 | JAKAVI® 5 MG TABLETAS | Tableta | Ruxolitinib (sin detalle de indicación) | Vigente |
| 20055348 | JAKAVI® 15 TABLETAS | Tableta | Ruxolitinib (sin detalle de indicación) | Vigente |
| 20083253 | JAKAVI® 10MG TABLETAS | Tableta | Ruxolitinib (sin detalle de indicación) | Vigente |

Los tres registros pertenecen a Novartis Pharma AG y corresponden a la vía oral. Actualmente no hay registros vigentes en Colombia.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 338 interacciones. Las más relevantes son:
  - **Mayores**: claritromicina, cobicistat, deferasirox, deferiprona, ibritumomab tiuxetán, tositumomab y tositumomab (I-131), y lexidronam de samario (153Sm).
  - **Moderadas**: dexametasona, rosuvastatina, dexfenfluramina, fenfluramina, sibutramina, troglitazona, palifermina y cloruro de estroncio Sr-89.
  - **Menores**: aprepitant, cimetidina, miconazol y clotrimazol.

Para advertencias y contraindicaciones, consultar el prospecto, ya que no se dispuso del texto del inserto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para el PEComa uterino tiene un puntaje alto (0.9973), pero carece de ensayos clínicos, literatura y un vínculo mecanístico respaldado (nivel L5). Además, en Colombia no hay registros sanitarios vigentes de ruxolitinib.

**Otras indicaciones predichas:**
- **Mayor respaldo**: la *linfohistiocitosis hemofagocítica* (HLH) asociada a infección tiene un nivel de evidencia L3. La respaldan estudios clínicos pediátricos, series y reportes de casos, y datos preclínicos en modelos murinos que apoyan la inhibición de JAK1/2. La evidencia es de diseño no aleatorizado y de tamaño pequeño, y los diseños deben verificarse con los textos completos. Sería la candidata más sólida para priorizar.
- **Evidencia preclínica**: el *liposarcoma* (mixoide) tiene dos publicaciones preclínicas sobre la vía JAK-STAT y sigue en L5.
- **Evidencia limitada**: la HLH asociada a malignidad tiene nivel L4, con una revisión y un reporte de caso sin evidencia directa.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA (advertencias y contraindicaciones) para completar la evaluación de seguridad.
- Confirmar el mecanismo de acción detallado y la indicación original aprobada.
- Para el PEComa y las enfermedades relacionadas, generar evidencia preclínica que demuestre la participación de JAK-STAT, dado que son tumores dependientes de mTOR.
- Evaluar si conviene priorizar la HLH asociada a infección, verificando los diseños de los estudios y sus resultados.
- Aclarar la situación regulatoria en Colombia, dado que el medicamento está comercializado y cuenta con 3 registros vigentes.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

