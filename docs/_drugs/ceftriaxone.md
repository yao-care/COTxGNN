---
layout: default
title: Ceftriaxone
parent: Evidencia Moderada (L3-L4)
nav_order: 144
evidence_level: L3
indication_count: 7
last_modified_at: 2026-10-14
description: "Ceftriaxone: nueva indicación predicha, Otitis media infecciosa (nivel de evidencia L3). Indicación original: Ceftriaxona"
monitor_inn: "Ceftriaxone"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "infectious otitis media", "blood group incompatibility", "suppurative otitis media", "chronic otitis media"]
---

# Ceftriaxone
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **7** 
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

# Ceftriaxona: De Indicación Registrada (Ceftriaxona) a Otitis Media Infecciosa

## Resumen en Una Frase

Ceftriaxona es un antibiótico betalactámico (cefalosporina) registrado en Colombia bajo el nombre del principio activo, sin una indicación detallada en el registro sanitario.
El modelo TxGNN predice que podría ser efectivo para **otitis media infecciosa**, con **1 ensayo clínico** (de contexto, que no evalúa ceftriaxona) y **19 publicaciones** relacionadas.
Esta predicción corresponde en gran medida a un uso antimicrobiano ya conocido, más que a un reposicionamiento novedoso.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Ceftriaxona (el registro no detalla indicaciones específicas) |
| Nueva Indicación Predicha | Otitis media infecciosa |
| Puntaje de Predicción TxGNN | 99.26% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, ceftriaxona es una cefalosporina betalactámica que inhibe la síntesis de la pared celular bacteriana, y su eficacia antibacteriana está bien establecida.

La otitis media aguda es causada principalmente por *Streptococcus pneumoniae*, *Haemophilus influenzae* y *Moraxella catarrhalis*, patógenos contra los cuales ceftriaxona tiene actividad. Una dosis única intramuscular es una alternativa establecida cuando el tratamiento oral falla o no es tolerado.

Por ello, el vínculo mecanístico es sólido, pero se trata de un uso antiinfeccioso esperable de la clase y no de un reposicionamiento propiamente dicho. El estado "solo cancelado" en Colombia indica que se retiró un producto específico, no necesariamente la clase de fármaco.

Otras predicciones del modelo (hiperamilasemia, síndrome de hiperviscosidad policlonal, analbuminemia congénita, incompatibilidad de grupo sanguíneo) carecen de justificación mecanística y probablemente son artefactos de la red del modelo. Otitis media supurativa y otitis media crónica tienen evidencia indirecta y limitada (en la crónica predominan *Pseudomonas*, *S. aureus* y biopelículas, para los que ceftriaxona no es de primera línea).

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02567825](https://clinicaltrials.gov/study/NCT02567825) | N/A | Completado | 250 | Colocación de tubos de timpanostomía vs. manejo no quirúrgico en niños con otitis media aguda recurrente. No evalúa ceftriaxona; relevancia solo contextual. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [8989332](https://pubmed.ncbi.nlm.nih.gov/8989332/) | 1997 | ECA | Pediatrics | Dosis única intramuscular de ceftriaxona vs. 10 días de trimetoprima-sulfametoxazol oral en otitis media aguda |
| [11099083](https://pubmed.ncbi.nlm.nih.gov/11099083/) | 2000 | Estudio clínico | Pediatr Infect Dis J | Eficacia bacteriológica y clínica de ceftriaxona intramuscular de 1 día vs. 3 días en otitis media aguda no respondedora |
| [9877360](https://pubmed.ncbi.nlm.nih.gov/9877360/) | 1998 | Estudio clínico | Pediatr Infect Dis J | Eficacia bacteriológica de ceftriaxona intramuscular por 3 días en otitis media aguda no respondedora |
| [12166789](https://pubmed.ncbi.nlm.nih.gov/12166789/) | 2002 | Consenso | Clin Pediatr | Recomendaciones de consenso para el tratamiento de la otitis media aguda |
| [10688388](https://pubmed.ncbi.nlm.nih.gov/10688388/) | 2000 | Revisión | Clin Ther | Revisión de recomendaciones de tratamiento antimicrobiano de la otitis media aguda |
| [35841649](https://pubmed.ncbi.nlm.nih.gov/35841649/) | 2022 | Cohorte | Int J Pediatr Otorhinolaryngol | Factores asociados al uso de ceftriaxona en otitis media aguda en atención primaria de EE. UU.; preocupación por resistencia antimicrobiana |
| [39361280](https://pubmed.ncbi.nlm.nih.gov/39361280/) | 2024 | Revisión | JAMA Netw Open | Prescripción óptima de antibióticos ambulatorios pediátricos |
| [20802367](https://pubmed.ncbi.nlm.nih.gov/20802367/) | 2010 | Revisión | Otol Neurotol | Prevención y tratamiento de meningitis y otitis media aguda en niños con implantes cocleares |
| [20660544](https://pubmed.ncbi.nlm.nih.gov/20660544/) | 2010 | Revisión | Pediatrics | Infecciones del sitio quirúrgico, otitis media aguda y meningitis en niños con implantes cocleares |
| [32796134](https://pubmed.ncbi.nlm.nih.gov/32796134/) | 2020 | Reporte de caso | Eur J Microbiol Immunol | Otitis media crónica por *Vibrio cholerae* no O1/no O139, tratada con ciprofloxacino y ceftriaxona |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20163214 (cancelado) | CEFTRINOX® 1000 MG | Polvo estéril para reconstituir a solución inyectable | CEFTRIAXONA |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento del modelo** (no provienen del prospecto): enfermedad hepática, enfermedad de la vesícula biliar, ictericia neonatal, colitis por *Clostridium difficile*, enterocolitis necrosante perinatal y anemia hemolítica.
- **Interacciones farmacológicas** (100 interacciones registradas; principales):
  - **Mayores:** cloruro de calcio, glucoheptonato de calcio y gluconato de calcio.
  - **Moderadas:** kanamicina, neomicina, estreptomicina y ácido picosulfúrico.
  - Otras interacciones tienen nivel de gravedad no clasificado (por ejemplo, anfotericina B, ácido acetilsalicílico, amoxicilina y doxiciclina).

Para advertencias y contraindicaciones de etiqueta, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La actividad de ceftriaxona contra los patógenos típicos de la otitis media aguda está respaldada por un ECA comparativo y recomendaciones de consenso, pero se trata de un uso antiinfeccioso ya conocido y no de un reposicionamiento novedoso. No hay ensayos clínicos que evalúen ceftriaxona en esta indicación, y el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Obtener el prospecto vigente (advertencias y contraindicaciones) y confirmar si existen otros registros de ceftriaxona vigentes en Colombia.
- Definir el mecanismo de acción a partir de DrugBank.
- Establecer salvaguardas de uso racional de antimicrobianos: reservar ceftriaxona para falla del tratamiento oral o cuando la vía oral no sea factible, con vigilancia de resistencia.
- Atender las interacciones mayores con calcio (especialmente en neonatos) y las contraindicaciones señaladas (enfermedad hepatobiliar, ictericia neonatal, antecedentes de colitis por *C. difficile*).
- Mantener en espera (Hold) las demás predicciones sin base mecanística; otitis media supurativa y crónica requerirían estudios adicionales, ya que la evidencia disponible es indirecta.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

