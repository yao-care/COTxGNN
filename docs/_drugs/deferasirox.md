---
layout: default
title: Deferasirox
parent: Evidencia Moderada (L3-L4)
nav_order: 200
evidence_level: L4
indication_count: 5
last_modified_at: 2026-11-24
description: "Deferasirox: nueva indicación predicha, Infección por VIH (nivel de evidencia L4). Indicación original: No especificada en los registros (solo figura \"Deferasirox\")"
monitor_inn: "DEFERASIROX"
predicted_indications: ["HIV infectious disease", "chronic hepatitis C virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia", "dermatofibrosarcoma protuberans"]
---

# Deferasirox
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **5** 
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

## Deferasirox: De Indicación No Especificada a Infección por VIH
{: .text-alpha }

## Resumen en Una Frase

Deferasirox es un quelante de hierro de administración oral cuyos registros sanitarios en Colombia no detallan la indicación aprobada (solo figura el nombre del principio activo).
El modelo TxGNN predice que podría ser efectivo para **infección por VIH**, pero actualmente no hay ensayos clínicos y solo se dispone de **2 publicaciones**, una de ellas un estudio preclínico con apoyo indirecto.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en los registros (solo figura "Deferasirox") |
| Nueva Indicación Predicha | Infección por VIH |
| Puntaje de Predicción TxGNN | 0.9940 |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 10 de 13) |
| Número de Registros Sanitarios | 13 (vigentes: 10) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Deferasirox (traducción no oficial): «Exjade (deferasirox) es un quelante activo por vía oral que es selectivo para el hierro (como Fe 3+ ). Es un ligando tridentado que se une al hierro con alta afinidad en una proporción 2:1. Aunque el deferasirox tiene una afinidad muy baja por el zinc y el cobre, se producen disminuciones variables en la concentración sérica de estos oligoelementos tras la administración de deferasirox.» Texto original en inglés: "Exjade (deferasirox) is an orally active chelator that is selective for iron (as Fe 3+ ). It is a tridentate ligand that binds iron with high affinity in a 2:1 ratio. Although deferasirox has very low affinity for zinc and copper there are variable decreases in the serum concentration of these trace metals after the administration of deferasirox." ([DailyMed: Exjade (deferasirox) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3495a70c-870c-4968-940e-8baea152cf85), versión del 2026-01-28; consultado el 2026-11-19). Según la información conocida, deferasirox es un quelante de hierro, y mecanísticamente podría ser aplicable a la infección por VIH a través del control de la disponibilidad de hierro.

Un estudio preclínico de 2021 (PMID 34550543) sugiere que el hierro en los endolisosomas restringe la transactivación del LTR del VIH-1 mediada por la proteína Tat, al aumentar su oligomerización y la expresión de β-catenina. Esto ofrece un fundamento plausible pero **indirecto**: se trata de un estudio in vitro que no evalúa deferasirox en pacientes con VIH.

La otra publicación (PMID 16529348) es una descripción general de nuevos fármacos y no respalda una indicación en VIH. Por ello, la predicción descansa principalmente en el puntaje del modelo.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [34550543](https://pubmed.ncbi.nlm.nih.gov/34550543/) | 2021 | Preclínico/In vitro | Journal of Neurovirology | El hierro endolisosomal restringe la transactivación del LTR del VIH-1 mediada por Tat, al aumentar la oligomerización de Tat y la expresión de β-catenina |
| [16529348](https://pubmed.ncbi.nlm.nih.gov/16529348/) | 2006 | Revisión | J Am Pharm Assoc | Descripción general de nuevos fármacos (ramelteón, tipranavir, nepafenaco y deferasirox); no respalda directamente la indicación en VIH |

---

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 20096376 | JADENU®180 MG TABLETAS RECUBIERTAS | TABLETA RECUBIERTA | DEFERASIROX | Vigente |
| 20096377 | JADENU® 360MG TABLETAS RECUBIERTAS | TABLETA RECUBIERTA | DEFERASIROX | Vigente |
| 20145925 | FERASIRO ® 250 MG TABLETA DISPERSABLE | TABLETA DISPERSABLE | DEFERASIROX | Vigente |
| 20146047 | FERASIRO 500 MG TABLETA DISPERSABLE | TABLETA DISPERSABLE | DEFERASIROX | Vigente |
| 20176281 | THALADEF® 360 MG TABLETAS RECUBIERTAS | TABLETA RECUBIERTA | DEFERASIROX | Vigente |

Se muestran 5 de 13 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no del prospecto)**: el grafo de conocimiento TxGNN (PrimeKG) asocia deferasirox con contraindicación en, entre otras, insuficiencia hepática, enfermedad renal, función renal alterada, cirrosis, trombocitopenia, neutropenia (incluidas formas congénitas), agranulocitosis, anemia, hiperbilirrubinemia, síndrome de Gilbert, úlcera péptica activa, hipertensión ocular, síndrome de disfunción multiorgánica y cáncer. Estos datos no provienen del texto del prospecto y deben verificarse.
- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total; entre las 20 mostradas:
  - **Mayor**: hidrocortisona, dexametasona, betametasona, triamcinolona, ácido acetilsalicílico, mesalazina, balsalazida y las formulaciones de anfotericina B (convencional, complejo lipídico, sulfato de colesterilo y liposomal).
  - **Moderada**: rabeprazol, pioglitazona, alosetrón, aprepitant, claritromicina, saxagliptina, hidróxido de aluminio, cisaprida y dexfenfluramina.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para VIH tiene un puntaje alto del modelo, pero solo cuenta con un estudio preclínico indirecto y sin ensayos clínicos (nivel L4). Además, el perfil de seguridad (toxicidad hepática, renal y hematológica) exige cautela.

<!-- review:begin co-lic-20261105-deferasirox-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, los registros en Colombia están cancelados y el perfil de seguridad (toxicidad hepática, renal y hematológica) exige cautela." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 13 registros sanitarios (vigentes: 10); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-deferasirox-1 -->

**Para avanzar se necesita:**
- Datos del mecanismo de acción del fármaco (por ejemplo, desde DrugBank)
- Prospecto de INVIMA con advertencias y contraindicaciones (bloqueante para el tamizaje de seguridad)
- Estudios preclínicos adicionales y, de ser favorables, ensayos clínicos de deferasirox en VIH
- Aclarar la indicación aprobada original y la situación regulatoria actual en Colombia
- Evaluar el perfil de seguridad en pacientes con VIH, dadas las posibles contraindicaciones hematológicas, hepáticas y renales

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "los registros en Colombia están cancelados y" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Exjade (deferasirox) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3495a70c-870c-4968-940e-8baea152cf85) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

