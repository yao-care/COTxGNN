---
layout: default
title: Epinastine
parent: Solo Predicción del Modelo (L5)
nav_order: 256
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Epinastine: nueva indicación predicha, Conjuntivitis por rosácea (nivel de evidencia L5). Indicación original: Epinastina"
monitor_inn: "epinastine"
predicted_indications: ["rosacea conjunctivitis", "allergic urticaria"]
---

# Epinastine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Epinastina: De Epinastina (conjuntivitis alérgica oftálmica) a Conjuntivitis por Rosácea
{: .text-alpha }

## Resumen en Una Frase

Epinastina es un antihistamínico H1 de uso oftálmico, registrado en Colombia como solución oftálmica y utilizado en la conjuntivitis alérgica.
El modelo TxGNN predice que podría ser efectivo para **conjuntivitis por rosácea**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden directamente esta indicación; la predicción se basa únicamente en el modelo computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Epinastina (el registro sanitario solo indica el nombre del principio activo, sin texto de indicación detallado) |
| Nueva Indicación Predicha | Conjuntivitis por rosácea |
| Puntaje de Predicción TxGNN | 0.9957 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 2 de 3) |
| Número de Registros Sanitarios | 3 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Epinastine (traducción no oficial): «La epinastina es un antagonista directo del receptor H 1, de acción tópica, y un inhibidor de la liberación de histamina desde el mastocito. La epinastina es selectiva para el receptor H 1 de la histamina y tiene afinidad por el receptor H 2 de la histamina.» Texto original en inglés: "Epinastine is a topically active, direct H 1 -receptor antagonist and an inhibitor of the release of histamine from the mast cell. Epinastine is selective for the histamine H 1 -receptor and has affinity for the histamine H 2 -receptor." ([DailyMed: epinastine hydrochloride prescribing information, Somerset Therapeutics, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0d4ee45c-e58f-4b7c-b389-898f5c27f54d), versión del 2025-03-22; consultado el 2026-11-19). Según la información conocida, la epinastina es un antagonista del receptor de histamina H1 con actividad estabilizadora de mastocitos, y su uso en conjuntivitis alérgica oftálmica está establecido. Mecanísticamente, podría ser aplicable a la inflamación de la superficie ocular.

Existe un vínculo plausible: la histamina y los mediadores de los mastocitos pueden contribuir a la irritación ocular en la rosácea. Sin embargo, la conjuntivitis por rosácea (rosácea ocular) depende principalmente de la disfunción de las glándulas de Meibomio, la inestabilidad de la película lagrimal y factores inmunes innatos y microbianos. Por ello, el mecanismo H1/mastocitos probablemente contribuye solo de forma menor.

El puntaje alto de TxGNN (0.9957) es una predicción computacional y no sustituye evidencia clínica ni bibliográfica, que no está disponible en los datos compilados.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 19964592 | RELESTAT ® | SOLUCION OFTALMICA | EPINASTINA | Vigente |
| 20218995 | ATERGIT® SOLUCIÓN OFTÁLMICA ESTÉRIL | SOLUCION OFTALMICA | EPINASTINA | Vigente |
| 19977977 | ATERGIT® SOLUCION OFTALMICA ESTERIL | SOLUCION OFTALMICA | EPINASTINA | Vencido |

Se muestran los 3 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la consulta se completó y no se identificaron interacciones con otros fármacos. El único registro corresponde a su farmacología: antagonismo del receptor de histamina H1 (gen HRH1), base de su uso en el picor asociado a la conjuntivitis alérgica.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de conjuntivitis por rosácea es solo computacional (nivel L5), sin ensayos ni literatura, y la fisiopatología de la rosácea ocular se relaciona poco con el mecanismo antihistamínico. Además, en Colombia el medicamento está comercializado y cuenta con 2 registros sanitarios vigentes (de 3 registros; el 19977977 figura como vencido).

<!-- review:begin co-lic-20261124-epinastine-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "y cuenta con 3 registros sanitarios vigentes" Corregido según los datos del INVIMA (Código Único de Medicamentos, datos al 2026-11-24): de los 3 registros sanitarios, 2 están vigentes (20218995 y 19964592) y el 19977977 figura como «Vencido». Las cifras actuales están en el Resumen rápido. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261124-epinastine-1 -->

**Para avanzar se necesita:**
- Revisión de literatura y estudios preclínicos o piloto sobre antihistamínicos o estabilizadores de mastocitos en rosácea ocular
- Datos detallados del mecanismo de acción (MOA)
- Obtener las advertencias y contraindicaciones del prospecto del INVIMA
- Comparación con los tratamientos habituales de la rosácea ocular (higiene palpebral, antibióticos tópicos u orales, entre otros)

<!-- review:begin co-lic-20261031-epinastine-1 -->

> **Corrección de revisión (2026-10-31)**: Texto original: "Aclarar la situación regulatoria (registros cancelados) y la viabilidad de una nueva comercialización / Comparación con los tratamientos habituales de la rosácea ocular (higiene palpebral, antibióticos tópicos u orales, entre otros)" Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-10-31. El medicamento tiene 3 registros sanitarios (vigentes: 2); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261031-epinastine-1 -->

---

### Nota: Segunda indicación predicha (urticaria alérgica)

Como referencia, el modelo predijo también **urticaria alérgica** (TxGNN 0.9928, nivel L4, recomendación: pregunta de investigación). La literatura incluye principalmente revisiones y estudios farmacodinámicos de supresión de roncha y eritema inducidos por histamina (por ejemplo, PMID [10442525](https://pubmed.ncbi.nlm.nih.gov/10442525/), [19558008](https://pubmed.ncbi.nlm.nih.gov/19558008/) y [29723372](https://pubmed.ncbi.nlm.nih.gov/29723372/)), sin ensayos en pacientes con urticaria ni ensayos clínicos registrados. Al ser una indicación ya cubierta por muchos antihistamínicos aprobados, su valor de reposicionamiento es limitado.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-10-31 | Eliminado: "Aclarar la situación regulatoria (registros cancelados) y la viabilidad de una nueva comercialización" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: epinastine hydrochloride prescribing information, Somerset Therapeutics, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0d4ee45c-e58f-4b7c-b389-898f5c27f54d) |
| 2026-11-24 | Registro 19977977: estado vigente → vencido | Reemplazado por la tabla de registros generada por programa (antes: Corregido) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-24 | Registros vigentes: 3 → 2 | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

