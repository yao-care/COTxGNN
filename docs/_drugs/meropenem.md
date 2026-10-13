---
layout: default
title: Meropenem
parent: Evidencia Moderada (L3-L4)
nav_order: 431
evidence_level: L4
indication_count: 10
---

# Meropenem
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
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

# Meropenem: De Indicación No Especificada en el Registro a Bacteriana Artritis (Artritis Bacteriana)

## Resumen en Una Frase

Meropenem es un antibiótico carbapenémico de amplio espectro; en el único registro sanitario hallado en Colombia, el texto de indicación aprobada solo repite el nombre del fármaco, sin detallar el uso original.
El modelo TxGNN predice que podría ser efectivo para **artritis bacteriana**, pero hasta ahora no hay ensayos clínicos registrados y solo **20 publicaciones** de apoyo indirecto (casi todas reportes de casos, revisiones y estudios de sensibilidad o farmacocinética).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto aprobado solo indica "MEROPENEM") |
| Nueva Indicación Predicha | Artritis bacteriana |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registro vigente) |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base consultada. Según el conocimiento general, meropenem es un carbapenémico de amplio espectro que inhibe la síntesis de la pared celular bacteriana al unirse a las proteínas fijadoras de penicilina (PBP). Tiene actividad contra bacterias Gram negativas y Gram positivas, así como contra *Burkholderia pseudomallei*.

Como antibiótico de amplio espectro, su uso original abarca infecciones bacterianas graves. La artritis bacteriana (séptica) es también una infección bacteriana, por lo que la relación entre ambas indicaciones es conceptualmente cercana: el mismo mecanismo antibacteriano podría aplicarse a patógenos articulares.

La literatura recuperada incluye un reporte de artritis séptica por *Klebsiella pneumoniae* productora de BLEE tratada con éxito con meropenem y amikacina, además de una cohorte retrospectiva de melioidosis osteoarticular en la que todos los aislamientos fueron sensibles a meropenem. Aun así, la evidencia es limitada y ningún ensayo registrado evalúa esta indicación.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para artritis bacteriana.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35146367](https://pubmed.ncbi.nlm.nih.gov/35146367/) | 2021 | Cohorte retrospectiva | Le infezioni in medicina | Caracterización de pacientes con melioidosis osteoarticular, una enfermedad poco reconocida |
| [39489417](https://pubmed.ncbi.nlm.nih.gov/39489417/) | 2024 | Revisión retrospectiva | Indian J Med Microbiol | 22 casos de melioidosis musculoesquelética (osteomielitis y artritis séptica); todos los aislamientos fueron sensibles a meropenem |
| [11869242](https://pubmed.ncbi.nlm.nih.gov/11869242/) | 1997 | Revisión | Clin Microbiol Infect | Terapia de la sepsis y criterios de definición para ensayos de antibióticos |
| [36804370](https://pubmed.ncbi.nlm.nih.gov/36804370/) | 2023 | Revisión | Int J Antimicrob Agents | Uso fuera de indicación frente a recomendaciones formales de antibióticos en infecciones por bacterias multirresistentes |
| [36678359](https://pubmed.ncbi.nlm.nih.gov/36678359/) | 2022 | Revisión | Pathogens | Opciones terapéuticas para melioidosis: antibióticos frente a terapia con fagos |
| [17433752](https://pubmed.ncbi.nlm.nih.gov/17433752/) | 2007 | Reporte de caso | Joint Bone Spine | Dos pacientes inmunocomprometidos con artritis séptica por *K. pneumoniae* BLEE, tratados con meropenem y amikacina más lavado artroscópico |
| [39380073](https://pubmed.ncbi.nlm.nih.gov/39380073/) | 2024 | Reporte de caso | J Med Case Rep | Melioidosis diseminada con artritis séptica, mal diagnosticada inicialmente |
| [38375100](https://pubmed.ncbi.nlm.nih.gov/38375100/) | 2024 | Reporte de caso | Infect Drug Resist | Meningitis supurativa con artritis por *Streptococcus suis* |
| [39193962](https://pubmed.ncbi.nlm.nih.gov/39193962/) | 2024 | Cohorte | Clin Lab | Distribución de patógenos y resistencia antimicrobiana en infecciones óseas y articulares en niños pequeños |
| [37713001](https://pubmed.ncbi.nlm.nih.gov/37713001/) | 2024 | Estudio de antibiograma | Eur J Orthop Surg Traumatol | Antibiograma para tratamiento empírico de infecciones ortopédicas no espinales |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20159905 (cancelado) | MEROPENEM 0.5 G | Polvo estéril para reconstituir a solución inyectable | MEROPENEM |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no proviene del prospecto)**: epilepsia, enfermedad renal, piouréter, trombocitopenia, colitis por *Clostridium difficile* y enterocolitis necrosante perinatal.
- **Interacciones farmacológicas** (14 identificadas):
  - **Mayores**: bupropión, iohexol, iopamidol.
  - **Moderadas**: ácido picosulfúrico, polietilenglicol 3350 con electrolitos, nitisinona, sulfato de sodio, lindano, etinilestradiol, alpelisib, encorafenib, ácido micofenólico, pemetrexed y teriflunomida.

No se dispone de advertencias ni contraindicaciones del prospecto de INVIMA; es necesario consultarlo.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de TxGNN es muy alta (99.92%), pero la evidencia se limita a reportes de casos, una cohorte retrospectiva y estudios de sensibilidad o farmacocinética, sin ensayos clínicos para artritis bacteriana. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), actualmente un vacío bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Estudios comparativos o guías clínicas que respalden meropenem en artritis séptica, particularmente en patógenos multirresistentes (BLEE, *Burkholderia*).
- Verificar la situación regulatoria: no hay registro vigente en Colombia, por lo que se requeriría un nuevo registro o importación.
- Revisar riesgos de seguridad relevantes (epilepsia, insuficiencia renal, trombocitopenia, colitis por *C. difficile*) y las interacciones mayores.
- Definir lineamientos de uso racional de antimicrobianos, reservando meropenem para infecciones resistentes.

**Nota adicional:** Entre las otras indicaciones predichas, la **infección del tracto urinario complicada** presenta la evidencia más sólida (nivel L1, varios ensayos de Fase 3 con meropenem como comparador y ECAs publicados), aunque corresponde en gran medida a un uso ya establecido más que a un reposicionamiento novedoso. Podría evaluarse como alternativa prioritaria, con salvaguardas (reserva para BLEE o multirresistencia, ajuste renal y política de uso racional).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

