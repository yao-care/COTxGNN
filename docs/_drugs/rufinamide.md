---
layout: default
title: Rufinamide
parent: Solo Predicción del Modelo (L5)
nav_order: 573
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Rufinamide: nueva indicación predicha, Síndrome de epilepsia relacionada con infección febril (FIRES) (nivel de evidencia L5). Indicación original: RUFINAMIDA"
monitor_inn: "Rufinamide"
predicted_indications: ["febrile infection-related epilepsy syndrome", "perioral myoclonia with absences", "photosensitive occipital lobe epilepsy", "atypical childhood epilepsy with centrotemporal spikes", "cryptogenic late-onset epileptic spasms"]
---

# Rufinamide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Rufinamida: De Rufinamida (indicación original no detallada) a Síndrome de Epilepsia Relacionada con Infección Febril (FIRES)

## Resumen en Una Frase

Rufinamida es un antiepiléptico registrado en Colombia bajo el nombre comercial INOVELON®, cuyo registro sanitario no detalla el texto de la indicación aprobada (solo figura el nombre del principio activo).
El modelo TxGNN predice que podría ser efectivo para el **síndrome de epilepsia relacionada con infección febril (FIRES)**, pero **no hay ensayos clínicos ni publicaciones** que respalden actualmente esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | RUFINAMIDA (el registro no especifica el texto de la indicación) |
| Nueva Indicación Predicha | Síndrome de epilepsia relacionada con infección febril (FIRES) |
| Puntaje de Predicción TxGNN | 99.57% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registro vigente) |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este reporte. Según la información general conocida, rufinamida es un modulador de los canales de sodio dependientes de voltaje: prolonga su estado inactivo y reduce la descarga neuronal repetitiva. Está aprobada a nivel internacional para el síndrome de Lennox-Gastaut.

En teoría, este mecanismo podría ofrecer control sintomático de las crisis en el FIRES, un síndrome epiléptico refractario. Sin embargo, el FIRES está impulsado en buena parte por neuroinflamación, un proceso que el bloqueo de canales de sodio no aborda directamente. Por ello, el vínculo mecanístico es especulativo y se apoya únicamente en el alto puntaje de predicción del modelo (0.996).

Otras indicaciones predichas con puntajes similares (todas con nivel de evidencia L5 y sin ensayos ni literatura) son: mioclonías perorales con ausencias (99.51%), epilepsia occipital fotosensible (99.44%), epilepsia infantil atípica con espigas centrotemporales (99.44%) y espasmos epilépticos criptogénicos de inicio tardío (99.44%). En el caso de las mioclonías perorales con ausencias, cabe advertir que los moduladores de canales de sodio pueden agravar algunos tipos de crisis generalizadas, en particular las ausencias.

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
| 20153553 | INOVELON® 400 MG | Tableta recubierta | RUFINAMIDA | Cancelado |

El fabricante registrado es BIOTOSCANA FARMA S.A. No existe actualmente ningún registro vigente en Colombia.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: el grafo de conocimiento utilizado por el modelo asocia el fármaco con las siguientes condiciones: insuficiencia hepática, enfermedad hepática, enfermedad de la vesícula biliar, leucopenia, trastorno de ansiedad, trastorno neurótico y trastorno distímico. Deben verificarse contra el prospecto oficial.
- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total; las 20 mostradas son de nivel moderado. Entre las principales están:
  - Corticoides: hidrocortisona, prednisona, betametasona, triamcinolona
  - Vitamina D y análogos: colecalciferol, calcifediol, calcitriol
  - Opioides y afines: morfina, difenoxina, difenoxilato
  - Cannabinoides: dronabinol, nabilona
  - Antieméticos y procinéticos: ondansetrón, metoclopramida, rolapitant
  - Otros: pioglitazona, bupropión, eliglustat, naloxegol, nitisinona

  Dado que el listado completo supera lo mostrado, se recomienda revisar las 100 interacciones antes de cualquier uso clínico.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el puntaje del modelo (nivel L5), sin ensayos clínicos ni literatura de respaldo. Además, el mecanismo de acción no explica bien la fisiopatología inflamatoria del FIRES, y el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Obtener los datos del mecanismo de acción desde DrugBank.
- Descargar y analizar el prospecto de INVIMA para completar advertencias y contraindicaciones (brecha de seguridad bloqueante para el tamizaje de seguridad).
- Realizar una revisión sistemática de la literatura sobre rufinamida en FIRES y otras epilepsias refractarias.
- Evaluar la viabilidad de reactivar o tramitar un nuevo registro sanitario, y la compatibilidad de la vía de administración (oral) con la necesidad clínica.
- Verificar las contraindicaciones hepáticas y hematológicas señaladas por el grafo de conocimiento.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

