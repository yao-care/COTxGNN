---
layout: default
title: Rufinamide
parent: Solo Predicción del Modelo (L5)
nav_order: 573
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "Rufinamide"
predicted_indications: ["perioral myoclonia with absences"]
description: "Rufinamide: nueva indicación predicha, Perioral myoclonia with absences (nivel de evidencia L5). Indicación original: RUFINAMIDA"
---

# Rufinamide
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

## Rufinamide: Perioral myoclonia with absences
{: .text-alpha }

## Resumen en Una Frase

Rufinamida es un antiepiléptico registrado en Colombia bajo el nombre comercial INOVELON®, cuyo registro sanitario no detalla el texto de la indicación aprobada (solo figura el nombre del principio activo).
El modelo TxGNN (aprendizaje profundo) predice que podría ser efectivo para las **mioclonías perorales con ausencias**, pero **no hay ensayos clínicos ni publicaciones** que respalden actualmente esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | RUFINAMIDA |
| Nueva Indicación Predicha | Perioral myoclonia with absences |
| Puntaje de Predicción TxGNN | 0.9951 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Rufinamide (traducción no oficial): «Se desconoce el mecanismo o los mecanismos precisos por los que la rufinamida ejerce su efecto antiepiléptico. Los resultados de estudios in vitro sugieren que el principal mecanismo de acción de la rufinamida es la modulación de la actividad de los canales de sodio y, en particular, la prolongación del estado inactivo del canal.» Texto original en inglés: "The precise mechanism(s) by which rufinamide exerts its antiepileptic effect is unknown. The results of in vitro studies suggest that the principal mechanism of action of rufinamide is modulation of the activity of sodium channels and, in particular, prolongation of the inactive state of the channel." ([DailyMed: Banzel (rufinamide) prescribing information, Eisai Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0a3fa925-1abd-458a-bd57-4ae780a1ef2d), versión del 2022-12-15; consultado el 2026-11-19). Según la información general conocida, rufinamida es un modulador de los canales de sodio dependientes de voltaje: prolonga su estado inactivo y reduce la descarga neuronal repetitiva. Está aprobada a nivel internacional para el síndrome de Lennox-Gastaut.

Para las mioclonías perorales con ausencias (0.9951), con nivel de evidencia L5 y sin ensayos ni literatura, cabe advertir que los moduladores de canales de sodio pueden agravar algunos tipos de crisis generalizadas, en particular las ausencias.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 20153553 | INOVELON® 400 MG | TABLETA RECUBIERTA | RUFINAMIDA | Vigente |

Se muestra el único registro sanitario de este principio activo en los datos del INVIMA, Código Único de Medicamentos.

<!-- licenses:end -->

El fabricante registrado es BIOTOSCANA FARMA S.A. Actualmente existe 1 registro vigente de 1 en Colombia y el medicamento está comercializado.

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
La predicción se basa únicamente en el puntaje del modelo (nivel L5), sin ensayos clínicos ni literatura de respaldo. Además, el mecanismo de acción no explica bien la fisiopatología inflamatoria del FIRES.

<!-- review:begin co-lic-20261105-rufinamide-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, el mecanismo de acción no explica bien la fisiopatología inflamatoria del FIRES, y el único registro sanitario en Colombia está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-rufinamide-1 -->

**Para avanzar se necesita:**
- Obtener los datos del mecanismo de acción desde DrugBank.
- Descargar y analizar el prospecto de INVIMA para completar advertencias y contraindicaciones (brecha de seguridad bloqueante para el tamizaje de seguridad).
- Realizar una revisión sistemática de la literatura sobre rufinamida en FIRES y otras epilepsias refractarias.
- Evaluar la viabilidad de reactivar o tramitar un nuevo registro sanitario, y la compatibilidad de la vía de administración (oral) con la necesidad clínica.
- Verificar las contraindicaciones hepáticas y hematológicas señaladas por el grafo de conocimiento.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "y el único registro sanitario en Colombia está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Banzel (rufinamide) prescribing information, Eisai Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0a3fa925-1abd-458a-bd57-4ae780a1ef2d) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

