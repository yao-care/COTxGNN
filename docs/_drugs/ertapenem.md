---
layout: default
title: Ertapenem
parent: Evidencia Moderada (L3-L4)
nav_order: 262
evidence_level: L4
indication_count: 2
last_modified_at: 2026-10-14
description: "Ertapenem: nueva indicación predicha, Artritis bacteriana (nivel de evidencia L4). Indicación original: Ertapenem"
---

# Ertapenem
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **2** 
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

# Ertapenem: De Antibiótico Carbapenémico (indicación no detallada en el registro) a Artritis Bacteriana

## Resumen en Una Frase

Ertapenem es un antibiótico carbapenémico inyectable. Sus registros sanitarios en Colombia solo consignan el nombre del principio activo, sin una indicación detallada. El modelo TxGNN predice que podría ser efectivo para **artritis bacteriana**, pero hoy no hay **ningún ensayo clínico** para esta indicación y la literatura disponible (**10 publicaciones**) consiste sobre todo en reportes de caso, estudios observacionales y estudios in vitro.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Ertapenem (el registro solo menciona el nombre del principio activo, sin indicación detallada) |
| Nueva Indicación Predicha | Artritis bacteriana |
| Puntaje de Predicción TxGNN | 99.72% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos detallados sobre el mecanismo de acción en la base de datos consultada. Por conocimiento general, ertapenem es un carbapenémico de amplio espectro. Inhibe la síntesis de la pared celular bacteriana al unirse a las proteínas fijadoras de penicilina, y actúa contra bacterias grampositivas, gramnegativas y anaerobias. Además, alcanza una penetración en hueso y articulaciones suficiente para su uso en terapia parenteral ambulatoria.

La artritis bacteriana (séptica) la causan microorganismos como *Klebsiella pneumoniae*, *Prevotella*, *Citrobacter* y enterobacterias productoras de BLEE, que están dentro del espectro de ertapenem. Por eso la predicción es plausible desde el punto de vista mecanístico. Sin embargo, se trata de una extensión de su actividad antibacteriana ya conocida y no de un mecanismo nuevo de reposicionamiento.

El puntaje de 99.72% es solo una predicción del modelo. No sustituye la evidencia clínica, y no hay ensayos registrados para esta indicación.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para artritis bacteriana.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [24709258](https://pubmed.ncbi.nlm.nih.gov/24709258/) | 2014 | Cohorte retrospectiva | Antimicrob Agents Chemother | Seguridad y eficacia de ertapenem ambulatorio a largo plazo en 306 pacientes. Las indicaciones incluyeron infecciones óseas y articulares, pero no es específico de artritis. |
| [22233826](https://pubmed.ncbi.nlm.nih.gov/22233826/) | 2011 | Reporte de caso | J Chemother | Artritis séptica de muñeca por *Klebsiella pneumoniae* tratada con éxito con ertapenem y levofloxacino. |
| [31352398](https://pubmed.ncbi.nlm.nih.gov/31352398/) | 2019 | Reporte de caso | BMJ Case Rep | Osteomielitis por *Citrobacter koseri* con artritis séptica en pie diabético, tratada con éxito con ertapenem. |
| [31220276](https://pubmed.ncbi.nlm.nih.gov/31220276/) | 2019 | Cohorte (10 pacientes) | J Antimicrob Chemother | Terapia supresora subcutánea con β-lactámicos en infecciones óseas y articulares. Ertapenem no es el único foco. |
| [31585203](https://pubmed.ncbi.nlm.nih.gov/31585203/) | 2020 | Reporte de caso con revisión | Anaerobe | Artritis séptica y osteomielitis de hombro por *Clostridium paraputrificum*. Es contexto de la enfermedad, no evalúa ertapenem directamente. |
| [37578166](https://pubmed.ncbi.nlm.nih.gov/37578166/) | 2023 | Reporte de caso con revisión | J Investig Med High Impact Case Rep | Artritis séptica por *Prevotella bivia*. Es contexto de la enfermedad. |
| [38924836](https://pubmed.ncbi.nlm.nih.gov/38924836/) | 2024 | In vitro / preclínico | Diagn Microbiol Infect Dis | Auranofina restablece la sensibilidad de *E. coli* resistente a carbapenémicos frente a ertapenem. |
| [39193962](https://pubmed.ncbi.nlm.nih.gov/39193962/) | 2024 | Epidemiología retrospectiva | Clin Lab | Distribución de patógenos y resistencia en infecciones óseas y articulares en niños. Evidencia indirecta. |
| [41878879](https://pubmed.ncbi.nlm.nih.gov/41878879/) | 2026 | Observacional retrospectivo | J Antimicrob Chemother | Temocilina como alternativa a los carbapenémicos en infecciones óseas y articulares por enterobacterias resistentes. Ertapenem no es la intervención. |

Una décima publicación sobre hidradenitis supurativa (PMID 29183082) se excluyó de la tabla por no ser relevante para artritis bacteriana.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20117466 | ERTAGRAM® 1 G | Polvo liofilizado para reconstituir a solución inyectable | ERTAPENEM |
| 20163864 | ERTAPENEM 1G/VIAL | Polvo estéril para reconstituir a solución inyectable | ERTAPENEM |

Los dos registros figuran como **cancelados**, por lo que actualmente no hay registros vigentes de ertapenem en Colombia en los datos compilados.

---

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no según el prospecto):** epilepsia, enfermedad renal, piouréter, colitis por *Clostridium difficile* y enterocolitis necrosante perinatal.
- **Interacciones farmacológicas:** se identificaron 38 interacciones en total, de las cuales se dispone de detalle para 20.
  - **Mayor:** bupropión.
  - **Moderadas:** ácido picosulfúrico, polietilenglicol 3350 con electrolitos y sulfato de sodio.
  - **Nivel no determinado:** entre otros, vancomicina, metronidazol, doxiciclina, morfina, metformina, omeprazol, pantoprazol y prednisona.

Para advertencias y contraindicaciones oficiales, consultar el prospecto, que no estuvo disponible para este informe.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos para artritis bacteriana. La evidencia consiste en reportes de caso, cohortes indirectas y estudios in vitro, y el puntaje alto del modelo es solo una predicción. Además, todos los registros sanitarios en Colombia están cancelados.

**Para avanzar se necesita:**
- Ensayos clínicos o estudios comparativos de ertapenem específicos en artritis séptica.
- Obtener y analizar el prospecto (advertencias y contraindicaciones), cuya ausencia bloquea el tamizaje de seguridad.
- Confirmar los datos del mecanismo de acción en DrugBank.
- Aclarar la situación regulatoria en Colombia, pues no hay registros vigentes.
- Verificar la compatibilidad de vía y forma farmacéutica para la nueva indicación.

Como nota adicional, la segunda indicación predicha (infección por *Staphylococcus aureus*, en combinación con cefazolina) tiene más respaldo, con un ensayo de Fase 2 (NCT04886284) y uno de Fase 4 (NCT07148960) en curso. Podría evaluarse como alternativa.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

