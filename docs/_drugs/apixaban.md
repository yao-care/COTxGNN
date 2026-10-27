---
layout: default
title: Apixaban
parent: Evidencia Moderada (L3-L4)
nav_order: 60
evidence_level: L4
indication_count: 1
last_modified_at: 2026-10-14
description: "Apixaban: nueva indicación predicha, Trastorno de migraña (nivel de evidencia L4). Indicación original: Inhibidores directos del factor Xa"
monitor_inn: "APIXABAN"
predicted_indications: ["migraine disorder"]
---

# Apixaban
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **1** 
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

## Apixabán: De Inhibidor Directo del Factor Xa a Trastorno de Migraña
{: .text-alpha }

## Resumen en Una Frase

Apixabán es un inhibidor directo del factor Xa, registrado en Colombia como anticoagulante oral.
El modelo TxGNN predice que podría ser efectivo para **trastorno de migraña**, pero la evidencia es muy limitada: **1 ensayo clínico** con relevancia baja (no evalúa apixabán ni migraña de forma directa) y **3 publicaciones** (dos reportes de caso con resultados contradictorios y un estudio retrospectivo).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Inhibidores directos del factor Xa |
| Nueva Indicación Predicha | Trastorno de migraña |
| Puntaje de Predicción TxGNN | 99.02% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, apixabán pertenece a la clase de los inhibidores directos del factor Xa, que bloquean la cascada de coagulación y reducen la formación de trombina y de coágulos.

Una hipótesis plantea que la migraña con aura, sobre todo en pacientes con foramen oval permeable (FOP) o con anticuerpos antifosfolípidos, podría involucrar microtrombos o embolia paradójica. En ese escenario, la anticoagulación podría, en teoría, reducir las crisis.

Sin embargo, el vínculo es débil e indirecto. Los reportes de caso disponibles se contradicen: uno describe empeoramiento de la migraña con aura tras iniciar apixabán, y otro describe resolución del aura con warfarina pero no con apixabán. Esto sugiere ausencia de beneficio consistente y posiblemente una señal negativa. El puntaje alto de TxGNN es una predicción computacional y no refleja eficacia clínica demostrada.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Fase 3 | Completado | 664 | Cierre del foramen oval permeable o anticoagulantes frente a antiplaquetarios para prevenir la recurrencia de ictus. No evalúa migraña como objetivo ni apixabán específicamente; relevancia baja (grado C). |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33402037](https://pubmed.ncbi.nlm.nih.gov/33402037/) | 2021 | Estudio retrospectivo (75 pacientes) | Lupus | Respuesta a terapia antitrombótica en migraña refractaria con anticuerpos antifosfolípidos; no es específico de apixabán. |
| [37582651](https://pubmed.ncbi.nlm.nih.gov/37582651/) | 2023 | Reporte de caso con revisión | The Neurologist | Migraña con aura que empeoró tras iniciar apixabán; la literatura sobre anticoagulantes orales directos y migraña es escasa y controvertida. |
| [28960288](https://pubmed.ncbi.nlm.nih.gov/28960288/) | 2017 | Reporte de caso | Headache | Paciente con migraña con aura en remisión durante 12 años con warfarina; los síntomas reaparecieron con apixabán y cedieron al reanudar warfarina. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20254500 (cancelado) | CARDIOTEC® 2.5 MG TABLETAS RECUBIERTAS | Tableta recubierta | Inhibidores directos del factor Xa |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total; entre las principales mostradas:
  - **Gravedad mayor**: ácido acetilsalicílico, cobicistat, deferasirox, ibritumomab tiuxetán, tositumomab y tositumomab (I-131).
  - **Gravedad moderada**: aprepitant, claritromicina, clotrimazol, dexametasona, dexfenfluramina, eliglustat, fenfluramina, miconazol, rolapitant, sibutramina, troglitazona, yoduro I-123, yoduro I-131 y sugammadex.

Como apixabán es un anticoagulante, el riesgo de sangrado con fármacos que afectan la hemostasia (por ejemplo, ácido acetilsalicílico) debe considerarse con especial cuidado. Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia se limita a un ensayo de baja relevancia y a reportes de caso contradictorios, con una posible señal negativa. El puntaje alto de TxGNN no está respaldado por datos clínicos, y el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Obtener y revisar las advertencias y contraindicaciones del prospecto de INVIMA.
- Completar los datos del mecanismo de acción desde DrugBank para evaluar el vínculo mecanístico.
- Verificar el texto completo del estudio retrospectivo en pacientes con anticuerpos antifosfolípidos.
- Generar evidencia clínica específica de apixabán en migraña (por ejemplo, estudios observacionales o un ensayo piloto en subpoblaciones con FOP o anticuerpos antifosfolípidos).
- Aclarar la situación regulatoria local, dado que el único registro está cancelado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

