---
layout: default
title: Bevacizumab
parent: Solo Predicción del Modelo (L5)
nav_order: 105
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Bevacizumab: nueva indicación predicha, Neoplasia de epiglotis (nivel de evidencia L5). Indicación original: No especificada"
---

# Bevacizumab
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

# Bevacizumab: De Indicación No Especificada en el Registro a Neoplasia de Epiglotis

## Resumen en Una Frase

Bevacizumab es un anticuerpo monoclonal que bloquea el factor de crecimiento endotelial vascular (VEGF). Los registros sanitarios colombianos lo listan solo por su nombre, sin texto de indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **neoplasia de epiglotis**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción específica.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (los registros solo indican "Bevacizumab", sin texto de indicación) |
| Nueva Indicación Predicha | Neoplasia de epiglotis |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 4 (0 vigentes, 4 cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen una descripción estructurada del mecanismo de acción. Aun así, la información conocida indica que bevacizumab neutraliza el VEGF-A e inhibe la formación de nuevos vasos sanguíneos (angiogénesis) que alimentan al tumor.

Los tumores de cabeza y cuello dependen en buena medida de la angiogénesis. Por eso, bloquear el VEGF es mecanísticamente plausible para una neoplasia de epiglotis. El texto de indicación original del registro no permite establecer una relación formal entre la indicación de origen y la nueva.

Es importante aclarar que esta plausibilidad es teórica. No se recuperaron ensayos clínicos ni literatura para esta indicación, de modo que el puntaje alto de TxGNN es una predicción puramente computacional.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

Los 4 registros sanitarios están **cancelados**; no hay ninguno vigente.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20255030 | BEVASTIM ® | Solución concentrada para infusión | Bevacizumab (sin texto de indicación) |
| 20237880 | ABXEDA E | Solución concentrada para infusión | Bevacizumab (sin texto de indicación) |
| 20254120 | VEGZELMA® | Solución concentrada para infusión | Bevacizumab (sin texto de indicación) |
| 19956001 | AVASTIN® concentrado para solución para infusión 400 mg/16 mL | Solución concentrada para infusión | Bevacizumab (sin texto de indicación) |

---

## Citotoxicidad

Esta clasificación se basa en conocimiento farmacológico general, no en datos toxicológicos incluidos en los datos compilados.

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (anticuerpo monoclonal anti-VEGF); no es un citotóxico convencional |
| Riesgo de Mielosupresión | Bajo como agente único; puede aumentar la neutropenia cuando se combina con quimioterapia |
| Clasificación de Emetogenicidad | Baja |
| Items de Monitoreo | Presión arterial, proteinuria, hemograma, función hepática y renal; vigilar sangrado y cicatrización de heridas |
| Protección en Manejo | Consultar el prospecto y las políticas institucionales de manejo de antineoplásicos y biológicos |

---

## Consideraciones de Seguridad

No se dispone de advertencias principales ni contraindicaciones del prospecto. Debe consultarse el prospecto para esa información.

**Interacciones farmacológicas:** se registraron 22 interacciones. Las principales son:

- **Mayores:** deferiprona, samario (153Sm) lexidronam, panitumumab, sunitinib y talidomida.
- **Moderadas:** bisfosfonatos (ácido alendrónico, risedrónico, etidrónico, ibandronato, pamidrónico, tiludrónico), factores estimulantes de colonias (filgrastim, pegfilgrastim, sargramostim), palifermina, idelalisib, romosozumab y radiofármacos (cloruro de estroncio Sr-89, dicloruro de radio Ra 223, fosfato de sodio P32).

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para neoplasia de epiglotis solo tiene respaldo computacional (nivel L5), sin ensayos clínicos ni literatura específica. Además, todos los registros sanitarios en Colombia están cancelados y falta la información de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto en INVIMA (advertencias y contraindicaciones), una brecha que bloquea el tamizaje de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Buscar evidencia clínica o preclínica específica en cáncer de laringe y epiglotis, o en cáncer de cabeza y cuello en general.
- Confirmar la situación regulatoria actual, dado que no hay registros vigentes.
- Considerar otras indicaciones predichas con más respaldo, como "neoplasia quística", que cuenta con un ensayo de Fase 3 en cáncer de ovario y literatura asociada.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

