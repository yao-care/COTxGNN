---
layout: default
title: Dapsone
parent: Evidencia Alta (L1-L2)
nav_order: 195
evidence_level: L1
indication_count: 1
last_modified_at: 2026-10-14
description: "Dapsone: nueva indicación predicha, Neumocistosis (nivel de evidencia L1). Indicación original: DAPSONA"
---

# Dapsone
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **1** 
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

# Dapsona: De DAPSONA (indicación registrada sin detalle) a Neumocistosis

## Resumen en Una Frase

La dapsona es un fármaco de la clase de las sulfonas, con registros sanitarios en Colombia que hoy están cancelados; la indicación registrada solo figura como "DAPSONA", sin detalle clínico.
El modelo TxGNN predice que podría ser efectivo para **neumocistosis** (neumonía por *Pneumocystis*), con **10 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección.
Cabe señalar que la dapsona ya está establecida en guías clínicas como alternativa para la profilaxis y el tratamiento de esta infección, por lo que más que un reposicionamiento novedoso se trata de un uso respaldado por la práctica.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | DAPSONA (el texto del registro no detalla la indicación) |
| Nueva Indicación Predicha | Neumocistosis |
| Puntaje de Predicción TxGNN | 99.73% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este reporte. Según la farmacología conocida, la dapsona es una sulfona antibacteriana que inhibe la dihidropteroato sintasa en la vía de síntesis de folato, el mismo blanco del componente sulfonamida del trimetoprim-sulfametoxazol (TMP-SMX). Esta interpretación proviene de la farmacología establecida y no del registro suministrado. Además, los datos de farmacología señalan que inhibe la actividad de la dihidrofolato reductasa en *Pneumocystis carinii* in vitro (CI50 de 1,5 µM).

*Pneumocystis jirovecii* depende de la vía del folato, por lo que su inhibición es biológicamente plausible. Esto es coherente con el puntaje muy alto del modelo (0,997). Los usos clínicos conocidos de la dapsona incluyen lepra (como parte de un régimen múltiple), dermatitis herpetiforme y profilaxis de la neumonía por *Pneumocystis* en personas inmunodeprimidas, en particular con sida.

En consecuencia, la predicción coincide con un uso ya reconocido en guías. Los ensayos clínicos de fase 3 comparan la dapsona con otros agentes en prevención y tratamiento de la neumonía por *Pneumocystis*.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00000802](https://clinicaltrials.gov/study/NCT00000802) | Fase 3 | Completado | 700 | Dapsona diaria vs. atovacuona diaria para profilaxis de neumonía por *Pneumocystis* en pacientes con VIH intolerantes a trimetoprim o sulfonamidas |
| [NCT00000991](https://clinicaltrials.gov/study/NCT00000991) | Fase 3 | Completado | 600 | Comparación aleatorizada de tres agentes anti-*Pneumocystis* (incluida dapsona) más zidovudina para prevención primaria en VIH avanzado |
| [NCT00001028](https://clinicaltrials.gov/study/NCT00001028) | Fase 3 | Completado | 400 | Pentamidina aerosolizada mensual vs. dapsona tres veces por semana como profilaxis en pacientes intolerantes a TMP-SMX |
| [NCT00000640](https://clinicaltrials.gov/study/NCT00000640) | Fase 3 | Completado | 290 | Dapsona/trimetoprim y clindamicina/primaquina vs. TMP-SMX en neumonía leve a moderada |
| [NCT00002283](https://clinicaltrials.gov/study/NCT00002283) | NA | Completado | No reportada | Dapsona más trimetoprim vs. TMP-SMX en el primer episodio de neumonía por *Pneumocystis* en sida |
| [NCT00000739](https://clinicaltrials.gov/study/NCT00000739) | Fase 1 | Completado | 96 | Dos regímenes de dapsona oral (diario vs. semanal) para profilaxis en niños con VIH; toxicidad y farmacocinética |
| [NCT00002120](https://clinicaltrials.gov/study/NCT00002120) | Fase 1 | Completado | 20 | Trimetrexato con leucovorina más dapsona vs. TMP-SMX; seguridad y farmacocinética (régimen combinado) |
| [NCT00002043](https://clinicaltrials.gov/study/NCT00002043) | NA | Completado | No reportada | Dapsona 100 mg vs. 50 mg como profilaxis primaria en pacientes con complejo relacionado con el sida |
| [NCT02550080](https://clinicaltrials.gov/study/NCT02550080) | Fase 4 | Desconocido | 3130 | Tamizaje genético de HLA-B*1301 para prevenir el síndrome de hipersensibilidad a dapsona (relevancia indirecta) |
| [NCT00636935](https://clinicaltrials.gov/study/NCT00636935) | Fase 4 | Retirado | 0 | Corticoides orales y fibrosis intersticial en neumonía por *Pneumocystis*; no evalúa dapsona |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38583518](https://pubmed.ncbi.nlm.nih.gov/38583518/) | 2024 | Revisión sistemática / metaanálisis en red de ECA | Clin Microbiol Infect | Eficacia y seguridad comparadas de regímenes de profilaxis (TMP-SMX, regímenes con dapsona, pentamidina, atovacuona) en personas con VIH |
| [39732393](https://pubmed.ncbi.nlm.nih.gov/39732393/) | 2025 | Revisión sistemática / metaanálisis en red de ECA | Clin Microbiol Infect | Comparación de regímenes de tratamiento de la neumonía por *P. jirovecii* en personas con VIH; el TMP-SMX sigue siendo el tratamiento principal |
| [27550992](https://pubmed.ncbi.nlm.nih.gov/27550992/) | 2016 | Guía | J Antimicrob Chemother | Guías ECIL para prevenir la neumonía por *P. jirovecii* en neoplasias hematológicas y trasplante de células madre; TMP-SMX es la opción de elección |
| [33870843](https://pubmed.ncbi.nlm.nih.gov/33870843/) | 2021 | Revisión | Expert Opin Pharmacother | Revisión de *P. jirovecii* con énfasis en prevención y tratamiento |
| [11155588](https://pubmed.ncbi.nlm.nih.gov/11155588/) | 2001 | Revisión (farmacología) | Dermatol Clin | Dapsona y sulfapiridina: útil en profilaxis de neumonía por *Pneumocystis* en VIH, lepra y dermatitis herpetiforme |
| [18971152](https://pubmed.ncbi.nlm.nih.gov/18971152/) | 2008 | Revisión | J Formos Med Assoc | Panorama de la neumonía por *Pneumocystis*, principal infección oportunista en pacientes con sida |
| [9606476](https://pubmed.ncbi.nlm.nih.gov/9606476/) | 1998 | Reporte de caso | Ann Pharmacother | Metahemoglobinemia por dapsona en profilaxis de neumonía por *Pneumocystis* |
| [33280223](https://pubmed.ncbi.nlm.nih.gov/33280223/) | 2021 | Revisión retrospectiva de casos | Pediatr Transplant | Metahemoglobinemia por dapsona en receptores pediátricos de trasplante renal |
| [31631707](https://pubmed.ncbi.nlm.nih.gov/31631707/) | 2021 | Revisión | Drug Chem Toxicol | Complicaciones hepáticas por dapsona más allá de la metahemoglobinemia |
| [32714715](https://pubmed.ncbi.nlm.nih.gov/32714715/) | 2020 | Reporte de caso | Cureus | Hipoxia por metahemoglobinemia inducida por dapsona |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20148515 | DAPSULON® 50 MG (cancelado) | Tableta cubierta con película | DAPSONA |
| 20145596 | DAPSULON® 100 MG (cancelado) | Tableta | DAPSONA |

---

## Consideraciones de Seguridad

- **Contraindicaciones y condiciones de riesgo (según el grafo de conocimiento, no el prospecto):** enfermedad hepática, enfermedad de la vesícula biliar, anemia (incluida la macrocítica), deficiencia de G6PD, enfermedades de depósito de glucógeno, cistinuria, galactosemia, deficiencia de piruvato deshidrogenasa E3 y metahemoglobinemia por deficiencia de metahemoglobina reductasa.
- **Riesgos descritos en la literatura:** metahemoglobinemia e hipoxia, hemólisis, hepatotoxicidad, pancreatitis aguda y síndrome de hipersensibilidad a dapsona (con un ensayo sobre tamizaje de HLA-B*1301).
- **Interacciones farmacológicas:** los datos solo recogen interacciones farmacológicas con blancos moleculares (receptor del gusto TAS2R40 y la enzima dihidropteroato sintasa de *Plasmodium falciparum*), sin interacciones medicamentosas de relevancia clínica.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay varios ensayos de fase 3 completados (NCT00000802, NCT00000991, NCT00001028, NCT00000640) y metaanálisis recientes que respaldan el uso de la dapsona en la neumocistosis, lo que corresponde a un nivel de evidencia L1. Sin embargo, es un uso ya establecido en guías, no un reposicionamiento novedoso, y sus riesgos hematológicos exigen salvaguardas.

**Para avanzar se necesita:**
- Tamizar la deficiencia de G6PD antes del uso y monitorear metahemoglobinemia, hemólisis y función hepática.
- Obtener el prospecto vigente (por ejemplo, de INVIMA) para confirmar advertencias y contraindicaciones oficiales.
- Aclarar la situación regulatoria: ambos registros están cancelados y no hay producto vigente en Colombia.
- Completar los datos detallados del mecanismo de acción (por ejemplo, desde DrugBank).
- Definir el papel de la dapsona frente a TMP-SMX (tratamiento de elección) como alternativa en pacientes intolerantes.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

