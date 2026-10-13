---
layout: default
title: Tazobactam
parent: Evidencia Alta (L1-L2)
nav_order: 608
evidence_level: L1
indication_count: 2
---

# Tazobactam
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **2** 
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

# Tazobactam: De Piperacilina con Inhibidor Enzimático a Neumonía

## Resumen en Una Frase

Tazobactam es un inhibidor de beta-lactamasas que se registró en Colombia combinado con piperacilina, originalmente como antibiótico inyectable.
El modelo TxGNN predice que podría ser efectivo para **neumonía**,
con **20 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección. Es importante tener en cuenta que tazobactam nunca se administra solo, por lo que la evidencia corresponde a combinaciones (piperacilina-tazobactam, ceftolozano-tazobactam).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Piperacilina e inhibidor enzimático |
| Nueva Indicación Predicha | Neumonía |
| Puntaje de Predicción TxGNN | 99.46% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según el conocimiento general, tazobactam es un inhibidor de beta-lactamasas que protege a su antibiótico acompañante (piperacilina, ceftolozano) de la degradación enzimática, y restaura su actividad frente a bacterias Gram negativas productoras de estas enzimas, como *Pseudomonas aeruginosa* y enterobacterias productoras de BLEE.

La indicación original (combinación con piperacilina como antibacteriano) y la neumonía comparten el mismo mecanismo antibacteriano. Estas bacterias son causas frecuentes de neumonía nosocomial y asociada a ventilador, por lo que el uso en neumonía es una extensión de un papel antibacteriano ya establecido, no un mecanismo nuevo.

Una limitación importante: como tazobactam siempre se usa en combinación, no es posible aislar su contribución individual. Además, el estado de mercado "solo cancelado" debe aclararse antes de cualquier acción regulatoria.

---

## Evidencia de Ensayos Clínicos

Se muestran los 10 ensayos más relevantes (de 20 identificados).

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02070757](https://clinicaltrials.gov/study/NCT02070757) | Fase 3 | Completado | 726 | Ceftolozano/tazobactam vs. meropenem en neumonía nosocomial con ventilación (ASPECT-NP); objetivo de no inferioridad en mortalidad a 28 días |
| [NCT02493764](https://clinicaltrials.gov/study/NCT02493764) | Fase 3 | Completado | 537 | Imipenem/relebactam vs. piperacilina/tazobactam en neumonía hospitalaria/asociada a ventilador; objetivo de no inferioridad en mortalidad |
| [NCT00253955](https://clinicaltrials.gov/study/NCT00253955) | Fase 3 | Completado | 460 | Levofloxacino vs. piperacilina/tazobactam en neumonía hospitalaria leve a moderada |
| [NCT04223752](https://clinicaltrials.gov/study/NCT04223752) | Fase 1 | Completado | 41 | Seguridad, tolerabilidad y farmacocinética de ceftolozano/tazobactam en niños con neumonía nosocomial |
| [NCT00438269](https://clinicaltrials.gov/study/NCT00438269) | Fase 2 | Completado | 80 | Piloto aleatorizado de terapia antimicrobiana apropiada en cuidados críticos |
| [NCT06977347](https://clinicaltrials.gov/study/NCT06977347) | N/A | Aún no recluta | 100 | Piperacilina/tazobactam solo vs. combinado con fluoroquinolona en neumonía comunitaria grave (sin resultados) |
| [NCT06972537](https://clinicaltrials.gov/study/NCT06972537) | N/A | Reclutando | 42 | Dosificación guiada por modelo vs. empírica de piperacilina-tazobactam en ancianos con neumonía |
| [NCT00435305](https://clinicaltrials.gov/study/NCT00435305) | N/A | Terminado | 40 | Concentraciones de antibióticos en el líquido de revestimiento epitelial pulmonar con infusión continua |
| [NCT02387372](https://clinicaltrials.gov/study/NCT02387372) | Fase 1 | Completado | 37 | Farmacocinética y penetración pulmonar de ceftolozano/tazobactam en pacientes críticos |
| [NCT01853982](https://clinicaltrials.gov/study/NCT01853982) | Fase 3 | Terminado | 4 | Ceftolozano/tazobactam vs. piperacilina/tazobactam en neumonía asociada a ventilador; terminado con solo 4 participantes, sin valor para eficacia |

---

## Evidencia de Literatura

Se muestran las 10 publicaciones más relevantes (de 20 identificadas).

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31563344](https://pubmed.ncbi.nlm.nih.gov/31563344/) | 2019 | ECA | Lancet Infect Dis | ASPECT-NP: ceftolozano-tazobactam vs. meropenem en neumonía nosocomial (no inferioridad, Fase 3) |
| [32785589](https://pubmed.ncbi.nlm.nih.gov/32785589/) | 2021 | ECA | Clin Infect Dis | RESTORE-IMI 2: imipenem/cilastatina/relebactam vs. piperacilina/tazobactam en neumonía hospitalaria/asociada a ventilador |
| [39674398](https://pubmed.ncbi.nlm.nih.gov/39674398/) | 2025 | ECA | Int J Infect Dis | Ensayo Fase 3 de no inferioridad de IMI/REL vs. PIP/TAZ en neumonía bacteriana hospitalaria/asociada a ventilador |
| [38823453](https://pubmed.ncbi.nlm.nih.gov/38823453/) | 2024 | Revisión sistemática y metaanálisis en red | Clin Microbiol Infect | Regímenes antibióticos empíricos en neumonía hospitalaria no asociada a ventilador |
| [36543346](https://pubmed.ncbi.nlm.nih.gov/36543346/) | 2022 | Revisión | Eur Respir Rev | Nuevos antibióticos para neumonía por Gram negativos |
| [35088403](https://pubmed.ncbi.nlm.nih.gov/35088403/) | 2022 | Revisión | Semin Respir Crit Care Med | Nuevos antibióticos para neumonía hospitalaria y asociada a ventilador |
| [32600375](https://pubmed.ncbi.nlm.nih.gov/32600375/) | 2020 | Revisión | Crit Care | Actualización del tratamiento de la neumonía nosocomial en UCI |
| [38971203](https://pubmed.ncbi.nlm.nih.gov/38971203/) | 2024 | Revisión sistemática | Int J Antimicrob Agents | Farmacocinética/farmacodinamia de nuevos beta-lactámicos con inhibidores en neumonía por bacterias resistentes a carbapenémicos |
| [38688353](https://pubmed.ncbi.nlm.nih.gov/38688353/) | 2024 | Revisión | Int J Antimicrob Agents | Guía práctica italo-francesa para infecciones por bacilos Gram negativos multirresistentes |
| [38902935](https://pubmed.ncbi.nlm.nih.gov/38902935/) | 2025 | Cohorte | Clin Infect Dis | Menor aparición de resistencia con ceftolozano-tazobactam (10%) que con ceftazidima-avibactam (40%) en *P. aeruginosa* multirresistente |
| [35699444](https://pubmed.ncbi.nlm.nih.gov/35699444/) | 2022 | Estudio observacional | Antimicrob Agents Chemother | Relación entre la exposición PK/PD de beta-lactámicos y los resultados en neumonía de UCI |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20089767 (cancelado) | AUROTAZ-P 4.5 G | Polvo estéril para reconstituir a solución inyectable | Piperacilina e inhibidor enzimático |

---

## Consideraciones de Seguridad

- **Enfermedades con contraindicación según el grafo de conocimiento** (relaciones fármaco-enfermedad de TxGNN, no texto del prospecto): enfermedad renal, piouréter, neutropenia, agranulocitosis, trastornos de la coagulación, colitis por *Clostridium difficile*, enterocolitis necrotizante perinatal, mononucleosis infecciosa y síndrome de infección crónica por virus de Epstein-Barr.

No se dispone de advertencias ni contraindicaciones del prospecto, ni de datos de interacciones farmacológicas. Consultar el prospecto para información de seguridad adicional.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Varios ensayos Fase 3 completados (ASPECT-NP, RESTORE-IMI 2 y el estudio con levofloxacino) en neumonía involucran regímenes con tazobactam, lo que corresponde a un nivel de evidencia L1, y el mecanismo es coherente con su papel antibacteriano. Sin embargo, tazobactam solo se usa en combinación, el único registro en Colombia está cancelado y faltan datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Aclarar el estado regulatorio: el único registro sanitario está cancelado y no hay productos vigentes.
- Obtener y analizar el prospecto (advertencias y contraindicaciones), pues su ausencia es una brecha de datos crítica.
- Completar los datos del mecanismo de acción desde DrugBank.
- Definir qué combinaciones (piperacilina o ceftolozano) y qué población de neumonía (hospitalaria, asociada a ventilador o comunitaria grave) se evaluarían, dado que no se puede aislar el aporte de tazobactam.
- Guiar el uso con datos de sensibilidad local y criterios de uso racional de antibióticos.
- Evaluar con cautela su uso en pacientes con enfermedad renal, neutropenia o trastornos de la coagulación, y vigilar la aparición de colitis por *C. difficile*.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

