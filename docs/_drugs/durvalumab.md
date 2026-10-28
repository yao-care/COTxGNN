---
layout: default
title: Durvalumab
parent: Solo Predicción del Modelo (L5)
nav_order: 242
evidence_level: L5
indication_count: 6
monitor_inn: "DURVALUMAB"
predicted_indications: ["uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
last_modified_at: 2026-10-23
description: "Durvalumab: nueva indicación predicha, Adenocarcinoma del ligamento uterino (nivel de evidencia L5). Indicación original: Sin indicación detallada en la licencia"
---

# Durvalumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Durvalumab: De la indicación registrada en INVIMA a Adenocarcinoma del ligamento uterino
{: .text-alpha }

## Resumen en Una Frase

Durvalumab es un anticuerpo monoclonal comercializado en Colombia como Imfinzi®; en la licencia local solo figura el nombre del principio activo como texto de indicación, por lo que no se dispone de una indicación aprobada detallada.
El modelo TxGNN predice que podría ser efectivo para **adenocarcinoma del ligamento uterino**, pero no hay ningún ensayo clínico ni publicación que respalde directamente esta predicción.
La enfermedad con más evidencia entre las predichas es el **carcinoma endocervical** (1 ensayo clínico de Fase 1 y 2 publicaciones relacionadas de forma indirecta).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sin indicación detallada en la licencia (el texto registrado solo dice "DURVALUMAB") |
| Nueva Indicación Predicha | Adenocarcinoma del ligamento uterino |
| Puntaje de Predicción TxGNN | 0.9992 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, durvalumab es un inhibidor de PD-L1 (un anticuerpo que bloquea el punto de control inmunitario y permite que los linfocitos T reconozcan las células tumorales), y su uso se ubica en el campo de la inmunoterapia oncológica.

El puntaje del modelo TxGNN (aprendizaje profundo) es muy alto (0.9992), pero proviene del modelo y puede reflejar similitudes que este aprendió entre enfermedades relacionadas, como otros adenocarcinomas ginecológicos, y no evidencia biológica. Una justificación mecanística solo sería plausible si los tumores expresan PD-L1 o presentan inestabilidad de microsatélites (MSI-H/dMMR), algo que no ha sido verificado.

Para esta indicación específica no hay ensayos ni literatura. Por ello, la predicción debe considerarse una hipótesis de partida.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para adenocarcinoma del ligamento uterino.

A modo de contexto, para otra enfermedad predicha (carcinoma endocervical, posición 2) existe un ensayo de Fase 1; no estudia directamente la indicación principal de este informe:

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03452332](https://clinicaltrials.gov/study/NCT03452332) | Fase 1 | Completado | 20 | Radioterapia hipofraccionada con durvalumab y tremelimumab en cáncer cervical, vaginal o vulvar recurrente o metastásico. Apoya factibilidad y seguridad, no eficacia. |

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para adenocarcinoma del ligamento uterino.

Literatura de contexto asociada a la enfermedad en posición 2 (carcinoma endocervical), sin relación directa con la indicación principal:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37467967](https://pubmed.ncbi.nlm.nih.gov/37467967/) | 2023 | Revisión | Biomedical Journal | Carcinoma neuroendocrino de células pequeñas del cuello uterino: tumor raro y agresivo asociado a VPH; la evidencia se limita a series y reportes de casos. |
| [42518016](https://pubmed.ncbi.nlm.nih.gov/42518016/) | 2026 | Ensayo clínico no aleatorizado | Oncology and Therapy | Ceralasertib más durvalumab en pacientes chinos con tumores sólidos avanzados (Fase 1): evalúa seguridad, farmacocinética y actividad antitumoral. |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20143749 | IMFINZI® 50 MG/ML CONCENTRADO PARA SOLUCIÓN PARA INFUSIÓN | Solución concentrada para infusión | DURVALUMAB (sin detalle de indicación en el registro) |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Inmunoterapia (inhibidor del punto de control PD-L1) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 81 interacciones en total. Entre las principales:
  - **Mayor**: adalimumab.
  - **Moderada**: corticosteroides (hidrocortisona, triamcinolona, dexametasona, betametasona, budesonida, prednisolona, prednisona, metilprednisolona, deflazacort), roflumilast, alefacept, alemtuzumab, anakinra, toxoide tetánico y vacuna contra el ántrax.
  - **Menor**: sales de zinc (acetato, gluconato, sulfato y cloruro).

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún ensayo ni publicación que estudie directamente el adenocarcinoma del ligamento uterino, por lo que el nivel de evidencia es L5 y la predicción se apoya solo en el modelo. Los estudios disponibles se refieren a otras enfermedades ginecológicas y son de fase temprana.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y del prospecto (advertencias y contraindicaciones) del registro INVIMA.
- Evaluación de la expresión de PD-L1 y del estado MSI-H/dMMR en este tipo de tumor.
- Revisión sistemática de la literatura y de registros de ensayos específicos para esta histología.
- Valorar si la línea de investigación con mayor soporte (carcinoma endocervical, Fase 1) merece priorizarse como pregunta de investigación.
- Plan de monitoreo de seguridad, incluyendo las interacciones con corticosteroides y adalimumab.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

