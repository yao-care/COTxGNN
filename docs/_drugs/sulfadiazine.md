---
layout: default
title: Sulfadiazine
parent: Solo Predicción del Modelo (L5)
nav_order: 595
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
description: "Sulfadiazine: nueva indicación predicha, Neumocistosis (nivel de evidencia L4). Indicación original: SULFADIAZINA"
monitor_inn: "Sulfadiazine"
predicted_indications: ["pneumocystosis", "punctate epithelial keratoconjunctivitis"]
---

# Sulfadiazine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Sulfadiazina: De SULFADIAZINA (indicación registrada sin detalle) a Neumocistosis
{: .text-alpha }

## Resumen en Una Frase

Sulfadiazina es una sulfonamida antibacteriana cuyo único registro sanitario en Colombia (LIMISULF® 500 MG TABLETAS) figura con la indicación genérica "SULFADIAZINA".
El modelo TxGNN predice que podría ser efectivo para **neumocistosis**, pero no hay ensayos clínicos registrados y solo se recopilaron **20 publicaciones** de apoyo indirecto (en su mayoría revisiones y reportes sobre infecciones oportunistas y toxoplasmosis).
La evidencia directa para esta nueva indicación es muy limitada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | SULFADIAZINA (el registro no detalla una indicación clínica específica) |
| Nueva Indicación Predicha | Neumocistosis |
| Puntaje de Predicción TxGNN | 0.9939 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la sulfadiazina es una sulfonamida que inhibe la enzima dihidropteroato sintasa en la vía de síntesis del folato. Esta vía es esencial para muchos microorganismos, por lo que su eficacia antiinfecciosa está establecida de forma general.

*Pneumocystis jirovecii* se trata con una sulfonamida relacionada, el sulfametoxazol (combinado con trimetoprima), por lo que existe una justificación mecanística a nivel de clase. Además, la literatura recopilada describe que la combinación pirimetamina-sulfadiazina se ha usado en pacientes con SIDA para tratar neumonía por *Pneumocystis* y toxoplasmosis, y que mutaciones en el gen DHPS de *P. jirovecii* generan resistencia cruzada a las sulfas, lo que confirma que esta enzima es la diana relevante.

Sin embargo, la literatura se centra sobre todo en infecciones por *Toxoplasma*, infecciones oportunistas en SIDA y toxicidad de sulfonamidas, y no evalúa directamente la sulfadiazina sola para neumocistosis. El alto puntaje del modelo probablemente refleja la similitud de clase con las sulfonamidas. Además, la trimetoprima-sulfametoxazol es el tratamiento estándar de primera línea, lo que reduce la necesidad de reposicionar la sulfadiazina.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Se muestran las publicaciones más relevantes (todas son revisiones o estudios no controlados; no se identificaron ECA).

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [2645082](https://pubmed.ncbi.nlm.nih.gov/2645082/) | 1989 | Sin clasificar | Clinical Pharmacy | Uso de pirimetamina-sulfadiazina para neumonía por *Pneumocystis carinii* y toxoplasmosis en SIDA |
| [15673759](https://pubmed.ncbi.nlm.nih.gov/15673759/) | 2005 | Sin clasificar | Antimicrob Agents Chemother | Mutaciones en el gen DHPS de *P. jirovecii* confieren resistencia cruzada a las sulfas |
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Revisión | American Family Physician | Fármacos antiparasitarios; quinina-pirimetamina-sulfadiazina para malaria resistente y trimetoprima-sulfametoxazol para neumonía por *Pneumocystis* |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Revisión | Drugs | Terapia y profilaxis de infecciones protozoarias sistémicas, incluyendo *P. carinii* y *Toxoplasma* |
| [2011633](https://pubmed.ncbi.nlm.nih.gov/2011633/) | 1991 | Revisión | Primary Care | Enfermedades parasitarias asociadas al SIDA; la neumonía por *P. carinii* es la infección oportunista más común |
| [2996829](https://pubmed.ncbi.nlm.nih.gov/2996829/) | 1985 | Revisión | Clinical Pharmacy | Tratamiento de complicaciones infecciosas del SIDA |
| [7909657](https://pubmed.ncbi.nlm.nih.gov/7909657/) | 1994 | Revisión | Annals of Internal Medicine | Avances en el manejo de infecciones oportunistas relacionadas con el SIDA |
| [9122147](https://pubmed.ncbi.nlm.nih.gov/9122147/) | 1997 | Sin clasificar | Presse Medicale | Prevención de infecciones parasitarias en pacientes VIH; trimetoprima-sulfametoxazol es de elección para *Pneumocystis* |
| [2060528](https://pubmed.ncbi.nlm.nih.gov/2060528/) | 1991 | Sin clasificar | Eur J Clin Microbiol Infect Dis | Seguimiento de 35 pacientes con SIDA en terapia de mantenimiento para toxoplasmosis, con recaídas de toxoplasmosis y neumocistosis |
| [9562233](https://pubmed.ncbi.nlm.nih.gov/9562233/) | 1998 | Revisión | Int J Clin Pharmacol Ther | Nefrotoxicidad de antiinfecciosos, incluida la obstrucción tubular por precipitación de sulfonamidas |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20077550 (cancelado) | LIMISULF® 500 MG TABLETAS | Tableta | SULFADIAZINA |

---

## Consideraciones de Seguridad

- **Contraindicaciones y condiciones de riesgo (según el grafo de conocimiento TxGNN, no según prospecto)**: porfiria (hereditaria y de metabolismo de porfirinas), enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, enfermedades hematológicas (trombocitopenia, neutropenia, agranulocitosis, leucopenia, anemia aplásica idiopática y aplásica, anemia macrocítica, anemia por deficiencia de ácido fólico), deficiencia de G6PD, asma (intrínseca y alérgica), acetilación lenta, obstrucción de las vías urinarias, piouréter, enfermedad por depósito de glucógeno, cistinuria, galactosemia y sobreinfección.
- **Interacciones Farmacológicas**: se identificaron 82 interacciones en total; las 20 listadas son de nivel moderado. Destacan los antidiabéticos (riesgo de hipoglucemia): clorpropamida, glimepirida, glipizida, gliburida, tolazamida, repaglinida, nateglinida y múltiples insulinas (aspart, degludec, detemir, glargina, glulisina, lispro, humana en varias presentaciones). También se reportan balsalazida, picosulfato y naltrexona.

No se dispone de advertencias del prospecto; se recomienda consultarlo.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en la similitud de clase de las sulfonamidas y en literatura indirecta, sin ensayos clínicos ni estudios que evalúen la sulfadiazina sola en neumocistosis. Además, el único registro sanitario en Colombia está cancelado y existe una alternativa estándar bien establecida (trimetoprima-sulfametoxazol).

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), pendiente y bloqueante para el cribado de seguridad
- Confirmar el mecanismo de acción en DrugBank
- Estudios preclínicos o clínicos que evalúen directamente la sulfadiazina frente a *Pneumocystis*
- Evaluar la viabilidad comercial dado el registro cancelado y la ausencia de ventaja sobre el tratamiento estándar
- Plan de monitoreo hematológico, renal y hepático, y control de interacciones con antidiabéticos
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

