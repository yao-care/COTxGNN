---
layout: default
title: Deferasirox
parent: Evidencia Moderada (L3-L4)
nav_order: 200
evidence_level: L4
indication_count: 5
last_modified_at: 2026-10-14
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
| Puntaje de Predicción TxGNN | 99.40% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, deferasirox es un quelante de hierro, y mecanísticamente podría ser aplicable a la infección por VIH a través del control de la disponibilidad de hierro.

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

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20176281 | THALADEF® 360 MG TABLETAS RECUBIERTAS (cancelado) | Tableta recubierta | DEFERASIROX |
| 20146047 | FERASIRO 500 MG TABLETA DISPERSABLE (cancelado) | Tableta dispersable | DEFERASIROX |

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
La predicción para VIH tiene un puntaje alto del modelo, pero solo cuenta con un estudio preclínico indirecto y sin ensayos clínicos (nivel L4). Además, los registros en Colombia están cancelados y el perfil de seguridad (toxicidad hepática, renal y hematológica) exige cautela.

**Para avanzar se necesita:**
- Datos del mecanismo de acción del fármaco (por ejemplo, desde DrugBank)
- Prospecto de INVIMA con advertencias y contraindicaciones (bloqueante para el tamizaje de seguridad)
- Estudios preclínicos adicionales y, de ser favorables, ensayos clínicos de deferasirox en VIH
- Aclarar la indicación aprobada original y la situación regulatoria actual en Colombia
- Evaluar el perfil de seguridad en pacientes con VIH, dadas las posibles contraindicaciones hematológicas, hepáticas y renales
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

