---
layout: default
title: Apixaban
parent: Solo Predicción del Modelo (L5)
nav_order: 60
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "APIXABAN"
predicted_indications: ["migraine disorder"]
description: "Apixaban: nueva indicación predicha, Trastorno de migraña (migraine disorder) (nivel de evidencia L5). Indicación original: INHIBIDORES DIRECTOS DEL FACTOR XA"
---

# Apixaban
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

## Apixaban: Trastorno de migraña (migraine disorder)
{: .text-alpha }

## Resumen en Una Frase

Apixabán es un anticoagulante oral que inhibe directamente el factor Xa de la coagulación.
El modelo TxGNN predice que podría ser útil para el **trastorno de migraña (migraine disorder)**, pero la evidencia actual es de nivel **L5**: no hay ensayos clínicos ni publicaciones que respalden su eficacia en migraña, y los casos descritos muestran empeoramiento o ausencia de mejoría con apixabán.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | INHIBIDORES DIRECTOS DEL FACTOR XA |
| Nueva Indicación Predicha | Trastorno de migraña (migraine disorder) |
| Puntaje de Predicción TxGNN | 0.9902 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 18) |
| Número de Registros Sanitarios | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Apixaban (traducción no oficial): «El apixabán es un inhibidor selectivo del FXa. No requiere antitrombina III para ejercer su actividad antitrombótica. El apixabán inhibe el FXa libre y el unido al coágulo, así como la actividad de la protrombinasa. El apixabán no tiene ningún efecto directo sobre la agregación plaquetaria, pero inhibe indirectamente la agregación plaquetaria inducida por la trombina.» Texto original en inglés: "Apixaban is a selective inhibitor of FXa. It does not require antithrombin III for antithrombotic activity. Apixaban inhibits free and clot-bound FXa, and prothrombinase activity. Apixaban has no direct effect on platelet aggregation, but indirectly inhibits platelet aggregation induced by thrombin." ([DailyMed: Eliquis (apixaban) prescribing information, Aphena Pharma Solutions - Tennessee, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=41a133ef-e461-48ad-8221-b735bdd0ec25), versión del 2026-09-24; consultado el 2026-11-19). Por su clase, apixabán bloquea el factor Xa y reduce la formación de trombina y de coágulos.

La hipótesis que podría vincularlo con la migraña es que, en la migraña con aura, sobre todo en personas con foramen oval permeable o anticuerpos antifosfolípidos, microtrombos o embolias paradójicas contribuirían a las crisis. En teoría, anticoagular podría reducir los episodios.

Sin embargo, este vínculo es débil e indirecto. Los casos publicados son contradictorios y apuntan en sentido negativo: una migraña con aura empeoró tras iniciar apixabán, y otra no se resolvió con apixabán pero sí con warfarina. El puntaje alto del modelo es una predicción computacional, no una prueba de eficacia clínica.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Fase 3 | Completado | 664 | Cierre del foramen oval permeable o anticoagulantes frente a antiagregantes para prevenir la recurrencia de ictus. No evalúa migraña como objetivo ni prueba apixabán específicamente. |

Este ensayo no estudia directamente la migraña, por lo que no aporta evidencia de eficacia de apixabán para esta indicación.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37582651](https://pubmed.ncbi.nlm.nih.gov/37582651/) | 2023 | Reporte de caso con revisión | The Neurologist | Migraña con aura que empeoró tras iniciar apixabán; la literatura sobre anticoagulantes orales directos en migraña es escasa y controvertida. |
| [28960288](https://pubmed.ncbi.nlm.nih.gov/28960288/) | 2017 | Reporte de caso | Headache | Mujer de 55 años con remisión de la migraña con aura durante 12 años con warfarina; los síntomas reaparecieron con apixabán y cedieron al reanudar warfarina. |
| [33402037](https://pubmed.ncbi.nlm.nih.gov/33402037/) | 2021 | Estudio retrospectivo (75 pacientes) | Lupus | Respuesta a terapia antitrombótica en migraña refractaria con anticuerpos antifosfolípidos; no es específico de apixabán. |

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 20040898 | ELIQUIS® 2.5MGTABLETAS RECUBIERTAS | TABLETA RECUBIERTA | INHIBIDORES DIRECTOS DEL FACTOR XA | Vigente |
| 20056956 | ELIQUIS® 5 MG | TABLETA RECUBIERTA | INHIBIDORES DIRECTOS DEL FACTOR XA | Vigente |
| 20128791 | KEIXA 5MG TABLETAS RECUBIERTAS | TABLETA RECUBIERTA | INHIBIDORES DIRECTOS DEL FACTOR XA | Vigente |
| 20139305 | KEIXA 2.5 MG TABLETAS RECUBIERTAS | TABLETA RECUBIERTA | INHIBIDORES DIRECTOS DEL FACTOR XA | Vigente |
| 20155907 | XALUTEM ® 5 MG TABLETAS RECUBIERTAS | TABLETA RECUBIERTA | INHIBIDORES DIRECTOS DEL FACTOR XA | Vigente |

Se muestran 5 de al menos 20 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes. Los datos de este informe solo incluyen parte de los registros.

<!-- licenses:end -->

<!-- review:begin co-lic-20261124b-apixaban-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "La lista de registros puede estar incompleta." Eliminado: advertía que la lista de registros podría ser parcial. La tabla de Información de Mercado en Colombia se genera a partir de los datos del INVIMA (Código Único de Medicamentos, datos al 2026-11-23) e indica cuántos registros muestra y que los datos de este informe solo incluyen parte de los registros. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261124b-apixaban-1 -->

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. Entre las de nivel mayor figuran ácido acetilsalicílico, cobicistat, deferasirox, ibritumomab tiuxetán y tositumomab. Entre las de nivel moderado figuran aprepitant, claritromicina, clotrimazol, dexametasona, miconazol, rolapitant y sugammadex.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Ningún estudio respalda el uso de apixabán en migraña (nivel de evidencia L5): los reportes de caso describen empeoramiento o falta de resolución con apixabán, y el ensayo de Fase 3 identificado no evalúa migraña. El puntaje del modelo no compensa esta ausencia de evidencia.

**Para avanzar se necesita:**
- Estudios clínicos que evalúen directamente apixabán en migraña, idealmente en subgrupos con migraña con aura, foramen oval permeable o anticuerpos antifosfolípidos
- Datos del mecanismo de acción para analizar el vínculo mecanístico
- Revisión del prospecto con advertencias y contraindicaciones
- Evaluación del riesgo de sangrado frente a un beneficio no demostrado

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Eliquis (apixaban) prescribing information, Aphena Pharma Solutions - Tennessee, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=41a133ef-e461-48ad-8221-b735bdd0ec25) |
| 2026-11-24 | Eliminado: "La lista de registros puede estar incompleta." | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

