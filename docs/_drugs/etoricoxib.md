---
layout: default
title: Etoricoxib
parent: Solo Predicción del Modelo (L5)
nav_order: 271
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-29
monitor_inn: "ETORICOXIB"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "atrophoderma vermiculata", "ulerythema ophryogenesis", "pulmonary hypertension", "benign prostatic hyperplasia (disease)", "kyphoscoliotic heart disease", "headache disorder", "trigeminal autonomic cephalalgia"]
description: "Etoricoxib: nueva indicación predicha, Trastorno de migraña (migraine disorder) (nivel de evidencia L5). Indicación original: ETORICOXIB"
---

# Etoricoxib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Etoricoxib: Trastorno de migraña (migraine disorder)
{: .text-alpha }

## Resumen en Una Frase

Etoricoxib es un inhibidor selectivo de la COX-2 (antiinflamatorio no esteroideo). Sus registros sanitarios en Colombia solo mencionan el nombre del principio activo como indicación, sin detallar el uso aprobado. En la literatura científica se utiliza para artritis reumatoide, osteoartritis, dolor lumbar crónico, espondilitis anquilosante, dolor agudo y gota.
El modelo TxGNN predice que podría ser efectivo para **trastorno de migraña**, pero **no hay ensayos clínicos** y solo **1 publicación** (una revisión exploratoria no específica del fármaco) respalda directamente esta predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | ETORICOXIB |
| Nueva Indicación Predicha | Trastorno de migraña (migraine disorder) |
| Puntaje de Predicción TxGNN | 0.9990 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 2) |
| Número de Registros Sanitarios | 3 (0 vigentes, 3 cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos compilada. Según la información conocida, etoricoxib es un inhibidor selectivo de la COX-2 (gen PTGS2), por lo que reduce la producción de prostaglandinas. Su eficacia en dolor e inflamación musculoesquelética está documentada en la literatura.

En la migraña, la prostaglandina E2 dependiente de COX-2 contribuye a la inflamación neurogénica y a la sensibilización trigeminovascular, por lo que la actividad de clase AINE es mecanísticamente plausible. Un estudio preclínico de 2017 en ganglios trigéminos de rata mostró que AINE, incluido etoricoxib, modifican la liberación de CGRP y PGE2; sin embargo, ese estudio está vinculado a otra entidad (susceptibilidad a migraña) y no constituye evidencia clínica.

Es importante subrayar que el puntaje TxGNN muy alto es solo una predicción computacional. La única publicación vinculada directamente a migraña es una revisión exploratoria sobre cefalea por ayuno en Ramadán, que no es específica de etoricoxib y no aporta datos de eficacia.

**Otras predicciones del modelo (todas en nivel L5 o L4):**
- **Cefalea (headache disorder, 0.9931)** y **cefalea trigémino-autonómica (0.9915)**: son las mejor respaldadas (nivel L4), con reportes de casos y series pequeñas de respuesta a etoricoxib en cefalea punzante primaria, cefalea tusígena y cefaleas sensibles a indometacina. No hay ensayos controlados.
- Migraña con aura de tronco encefálico, susceptibilidad a migraña, atrodermia vermiculada, uleritema ofriógenes, hipertensión pulmonar, hiperplasia prostática benigna y cardiopatía cifoescoliótica: sin respaldo clínico. En hipertensión pulmonar y cardiopatía, el perfil de riesgo del fármaco sugiere más daño que beneficio.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Para la indicación principal (trastorno de migraña):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [42841395](https://pubmed.ncbi.nlm.nih.gov/42841395/) | 2026 | Revisión exploratoria | Pain Management | Revisa la cefalea atribuida al ayuno (p. ej., en Ramadán); no es específica de etoricoxib y no ofrece datos de eficacia |

Evidencia relacionada de cefaleas afines (indicaciones secundarias del modelo):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35277974](https://pubmed.ncbi.nlm.nih.gov/35277974/) | 2022 | Serie de casos/Observacional | Headache | Cefaleas sensibles a indometacina que responden a etoricoxib y celecoxib, con menor riesgo gastrointestinal que indometacina |
| [36893522](https://pubmed.ncbi.nlm.nih.gov/36893522/) | 2023 | Reporte de caso | Clin Neurol Neurosurg | Dos pacientes con cefalea tusígena secundaria que respondieron a etoricoxib |
| [18171381](https://pubmed.ncbi.nlm.nih.gov/18171381/) | 2008 | Reporte/serie de casos | Eur J Neurol | Cefalea punzante primaria con respuesta a etoricoxib |
| [17883876](https://pubmed.ncbi.nlm.nih.gov/17883876/) | 2007 | Reporte de caso | J Med Case Rep | Cefalea punzante idiopática tratada con etoricoxib |
| [29209105](https://pubmed.ncbi.nlm.nih.gov/29209105/) | 2017 | Preclínico (animal/in vitro) | Mediators Inflamm | Nimesulida, etoricoxib y ketoprofeno modifican la liberación de CGRP y PGE2 en ganglios trigéminos de rata |
| [25229174](https://pubmed.ncbi.nlm.nih.gov/25229174/) | 2014 | Reporte de caso (evento adverso) | Clin Neuropharmacol | Síndrome de vasoconstricción cerebral reversible posiblemente inducido por etoricoxib (señal de seguridad) |
| [21373319](https://pubmed.ncbi.nlm.nih.gov/21373319/) | 2010 | Reporte de caso (evento adverso) | Int J Emerg Med | Hiperpotasemia grave y disfunción renal aguda inducidas por etoricoxib junto con telmisartán y dieta baja en sodio |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20219448 | XICOX® 60 MG | Tableta recubierta | Etoricoxib (sin detalle de indicación) | Temp. no comerc - Vigente |
| 20226690 | MEDIKET® 90 MG tabletas recubiertas | Tableta recubierta | Etoricoxib (sin detalle de indicación) | Vigente |
| 20070877 | ANEXIA® 60 MG | Tableta cubierta con película | Etoricoxib (sin detalle de indicación) | Vigente |

---

## Consideraciones de Seguridad

- **Interacciones farmacológicas / farmacología:** la consulta se completó y registró una única entrada, que corresponde a la diana farmacológica COX-2 (PTGS2) de etoricoxib, no a una interacción con otro fármaco.
- **Señales de seguridad en la literatura:**
  - Posible síndrome de vasoconstricción cerebral reversible asociado a etoricoxib (reporte de caso, 2014).
  - Hiperpotasemia grave y disfunción renal aguda en un paciente que tomaba telmisartán y seguía una dieta baja en sodio (reporte de caso, 2010).
  - Como clase, los inhibidores de COX-2 se asocian a riesgo cardiovascular, retención de sodio y líquidos, y aumento de la presión arterial; esto es relevante en pacientes mayores.

Consultar el prospecto para información completa sobre advertencias y contraindicaciones, ya que no se dispuso de ese texto para este informe.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para trastorno de migraña tiene un puntaje TxGNN alto, pero se mantiene en nivel L5: no hay ensayos clínicos y la única publicación vinculada no es específica del fármaco ni aporta datos de eficacia. Además, los 3 registros sanitarios en Colombia están cancelados y no se dispuso de las advertencias y contraindicaciones del prospecto. La mejor evidencia se encuentra en cefaleas primarias afines (cefalea y cefalea trigémino-autonómica, nivel L4), aunque se limita a reportes de casos.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto aprobado por INVIMA (advertencias y contraindicaciones), así como confirmar la indicación original registrada.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una búsqueda dirigida de ensayos clínicos y literatura específica de etoricoxib en migraña (aguda y profiláctica).
- Valorar priorizar las cefaleas sensibles a indometacina y trigémino-autonómicas como pregunta de investigación, con un diseño controlado.
- Evaluar el perfil de riesgo cardiovascular, renal y cerebrovascular en la población objetivo.
- Aclarar la situación comercial en Colombia, dado que no hay registros vigentes.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

