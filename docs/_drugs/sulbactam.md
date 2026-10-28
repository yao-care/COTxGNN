---
layout: default
title: Sulbactam
parent: Solo Predicción del Modelo (L5)
nav_order: 593
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Sulbactam: nueva indicación predicha, Artritis bacteriana (nivel de evidencia L3). Indicación original: Ampicilina e inhibidor enzimático"
monitor_inn: "SULBACTAM"
predicted_indications: ["bacterial arthritis"]
---

# Sulbactam
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

## Sulbactam: De Ampicilina con Inhibidor Enzimático a Artritis Bacteriana
{: .text-alpha }

## Resumen en Una Frase

Sulbactam es un inhibidor de betalactamasas que se utiliza junto con ampicilina; su registro sanitario en Colombia lo describe como "ampicilina e inhibidor enzimático".
El modelo TxGNN predice que podría ser efectivo para **artritis bacteriana**, pero no hay ensayos clínicos registrados y la literatura recuperada (19 publicaciones) es en su mayoría antigua, de casos clínicos o indirecta.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Ampicilina e inhibidor enzimático |
| Nueva Indicación Predicha | Artritis bacteriana |
| Puntaje de Predicción TxGNN | 0.9979 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 2) |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según el conocimiento farmacológico general, sulbactam es un inhibidor irreversible de betalactamasas que se combina con ampicilina para ampliar su espectro frente a bacterias productoras de estas enzimas. Además, tiene actividad intrínseca contra *Acinetobacter baumannii* mediante la unión a proteínas fijadoras de penicilina (PBP).

La artritis bacteriana (séptica) está causada principalmente por *Staphylococcus aureus*, estreptococos y bacilos gramnegativos, algunos de los cuales producen betalactamasas. El vínculo mecanístico es plausible. Cabe señalar que esta predicción es más una continuación del uso antibacteriano original que un reposicionamiento propiamente dicho, lo cual es coherente con el puntaje elevado del modelo.

Este razonamiento se basa en farmacología general y no en el registro suministrado, por lo que debe confirmarse con fuentes primarias.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Se priorizaron los estudios con diseño comparativo o clínico sobre casos aislados e informes indirectos.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [2677956](https://pubmed.ncbi.nlm.nih.gov/2677956/) | 1989 | Estudio comparativo aleatorizado | Pediatr Infect Dis J | Ampicilina/sulbactam vs. ceftriaxona en infecciones de tejidos blandos y esqueléticas en niños (incluye 11 casos de artritis supurativa) |
| [3026009](https://pubmed.ncbi.nlm.nih.gov/3026009/) | 1986 | Estudio abierto comparativo aleatorizado | Rev Infect Dis | Sulbactam + ampicilina vs. cefotaxima en infecciones de hueso, articulación y tejidos blandos; curación o mejoría clínica en los 13 pacientes del grupo de sulbactam/ampicilina |
| [3026018](https://pubmed.ncbi.nlm.nih.gov/3026018/) | 1986 | Estudio clínico | Rev Infect Dis | Tratamiento secuencial con sulbactam/ampicilina parenteral y sultamicilina oral en 9 niños con osteomielitis o artritis séptica; patógenos identificados sensibles a la combinación |
| [3252119](https://pubmed.ncbi.nlm.nih.gov/3252119/) | 1988 | Estudio clínico | Mikrobiyol Bul | Ampicilina y sulbactam en 84 pacientes con infecciones diversas, incluidos 5 con artritis séptica y osteomielitis |
| [1745624](https://pubmed.ncbi.nlm.nih.gov/1745624/) | 1991 | Comparación in vitro / revisión | Pharmacotherapy | Comparación de actividad in vitro y eficacia clínica de ampicilina-sulbactam y ticarcilina-clavulánico |
| [36804370](https://pubmed.ncbi.nlm.nih.gov/36804370/) | 2023 | Revisión | Int J Antimicrob Agents | Uso fuera de indicación frente a recomendaciones formales de antibióticos en infecciones por bacterias multirresistentes |
| [39193962](https://pubmed.ncbi.nlm.nih.gov/39193962/) | 2024 | Cohorte retrospectiva | Clin Lab | Distribución de patógenos y resistencia antimicrobiana en infecciones óseas y articulares en niños pequeños |
| [9263167](https://pubmed.ncbi.nlm.nih.gov/9263167/) | 1997 | Reporte de caso | J Rheumatol | Artritis por *Pasteurella multocida* tras mordedura de gato, tratada con ampicilina/sulbactam con resolución de la infección |
| [36550469](https://pubmed.ncbi.nlm.nih.gov/36550469/) | 2022 | Reporte de caso | BMC Infect Dis | Hiperamonemia en artritis por *Ureaplasma parvum* |
| [36533253](https://pubmed.ncbi.nlm.nih.gov/36533253/) | 2022 | Reporte de caso | Infect Drug Resist | Artritis recurrente por *Brucella melitensis* |

**Nota:** varios de los resultados recuperados tienen relación solo indirecta con el tema (por ejemplo, un caso de hemoptisis, un estudio de citotoxicidad en condrocitos caninos y un trabajo de optimización de antibióticos). Según los títulos y resúmenes disponibles, ninguna publicación confirma un ensayo controlado de sulbactam específicamente para artritis bacteriana.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20166596 | AUROPENNZ 3.0 G | Polvo estéril para reconstituir a solución inyectable | Ampicilina e inhibidor enzimático (vigente) |
| 20166599 | AUROPENNZ 1.5 G | Polvo estéril para reconstituir a solución inyectable | Ampicilina e inhibidor enzimático (vigente) |

Ambos registros pertenecen a EUGIA PHARMA SPECIALITIES LIMITED y están cancelados. Pueden existir otros productos de ampicilina-sulbactam comercializados con registros distintos; esto debe verificarse.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (TxGNN/PrimeKG, no provienen del prospecto):** enfermedad renal, piouréter, colitis por *Clostridium difficile*, enterocolitis necrosante perinatal, mononucleosis infecciosa y síndrome de infección crónica por virus de Epstein-Barr.

No se dispone de información de advertencias o contraindicaciones del prospecto, ni de interacciones farmacológicas registradas. Consultar el prospecto para información de seguridad complementaria.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La plausibilidad mecanística es alta y el puntaje del modelo es elevado, pero se trata esencialmente de una extensión del uso antibacteriano existente. La evidencia es L3 (estudios pequeños y antiguos, reportes de caso y apoyo indirecto), no hay ensayos clínicos registrados, los registros sanitarios locales están cancelados y falta la revisión de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto del INVIMA (advertencias y contraindicaciones), lo cual es un requisito previo para el tamizaje de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Verificar si existen otros productos de ampicilina-sulbactam vigentes en Colombia.
- Revisar la literatura para confirmar estudios controlados de sulbactam en artritis bacteriana y descartar los resultados irrelevantes.
- Evaluar los patrones de resistencia locales de los patógenos causantes de artritis séptica.
- Considerar las contraindicaciones del grafo de conocimiento (en particular la enfermedad renal y la colitis por *C. difficile*) en cualquier plan de evaluación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

