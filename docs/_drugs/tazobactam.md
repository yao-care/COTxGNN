---
layout: default
title: Tazobactam
parent: Evidencia Alta (L1-L2)
nav_order: 373
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

# Tazobactam: De Combinación Piperacilina/Inhibidor Enzimático a Neumonía

## Resumen en Una Frase

Tazobactam es un inhibidor de betalactamasas que en Colombia se comercializa junto con piperacilina (registro sanitario: "piperacilina e inhibidor enzimático").
El modelo TxGNN predice que podría ser efectivo para **neumonía**,
con **50 ensayos clínicos** y **20 publicaciones** relacionados. Casi toda la evidencia corresponde a combinaciones fijas (piperacilina/tazobactam, ceftolozano/tazobactam), no a tazobactam solo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Piperacilina e inhibidor enzimático (texto del registro sanitario; no describe una enfermedad específica) |
| Nueva Indicación Predicha | Neumonía |
| Puntaje de Predicción TxGNN | 99.46% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 16 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, tazobactam es un inhibidor de betalactamasas sin actividad antibacteriana propia. Protege al antibiótico betalactámico con el que se combina (piperacilina o ceftolozano) de la hidrólisis por enzimas de clase A y algunas de clase C en bacterias Gram negativas.

Esas bacterias son causa frecuente de neumonía nosocomial y asociada a ventilador. Por eso el mecanismo es aplicable a la nueva indicación, y el puntaje alto de TxGNN (99.46%) es coherente con él.

Este caso es en gran parte **uso ya aprobado, no reposicionamiento novedoso**. Las combinaciones con tazobactam ya se usan y comercializan para neumonía. La evidencia respalda las combinaciones fijas, no tazobactam como agente único.

## Evidencia de Ensayos Clínicos

Se registraron 50 ensayos relacionados. Se listan los 10 más relevantes, priorizando los que evalúan regímenes con tazobactam. En varios, piperacilina/tazobactam es el comparador y no el agente en prueba.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02070757](https://clinicaltrials.gov/study/NCT02070757) | Fase 3 | Completado | 726 | Ceftolozano/tazobactam vs meropenem en neumonía nosocomial ventilada; objetivo principal: no inferioridad en mortalidad por todas las causas a día 28 |
| [NCT02493764](https://clinicaltrials.gov/study/NCT02493764) | Fase 3 | Completado | 537 | Imipenem/cilastatina/relebactam vs piperacilina/tazobactam en neumonía nosocomial o asociada a ventilador; no inferioridad en mortalidad |
| [NCT03583333](https://clinicaltrials.gov/study/NCT03583333) | Fase 3 | Completado | 274 | Estudio multinacional doble ciego: imipenem/relebactam vs piperacilina/tazobactam en HABP/VABP |
| [NCT00253955](https://clinicaltrials.gov/study/NCT00253955) | Fase 3 | Completado | 460 | Levofloxacino 750 mg vs piperacilina/tazobactam 4 g/500 mg cada 8 h en neumonía nosocomial leve a moderada; no inferioridad |
| [NCT01796717](https://clinicaltrials.gov/study/NCT01796717) | Fase 2/3 | Desconocido | 50 | Infusión prolongada vs regular de piperacilina/tazobactam en neumonía nosocomial en UCI; respuesta clínica, farmacocinética y seguridad |
| [NCT01853982](https://clinicaltrials.gov/study/NCT01853982) | Fase 3 | Terminado | 4 | Ceftolozano/tazobactam vs piperacilina/tazobactam en neumonía asociada a ventilador; terminado con solo 4 participantes |
| [NCT03581370](https://clinicaltrials.gov/study/NCT03581370) | Fase 3 | Reclutando | 80 | Infusión corta vs prolongada de ceftolozano/tazobactam en neumonía asociada a ventilador por *P. aeruginosa*; comparación de exposición farmacocinética |
| [NCT06977347](https://clinicaltrials.gov/study/NCT06977347) | N/A | Aún no reclutando | 100 | Piperacilina/tazobactam solo vs combinado con fluoroquinolona en neumonía comunitaria grave (Corea del Sur) |
| [NCT06972537](https://clinicaltrials.gov/study/NCT06972537) | N/A | Reclutando | 42 | Dosificación guiada por modelo vs empírica de piperacilina/tazobactam en neumonía de adultos mayores |
| [NCT04276480](https://clinicaltrials.gov/study/NCT04276480) | N/A | Completado | 9 | Piperacilina/tazobactam empírica en neumonía asociada a ventilador con colonización por Enterobacterias BLEE; muestra muy pequeña |

## Evidencia de Literatura

Se encontraron 20 publicaciones. Se listan las 10 más relevantes, con prioridad para ECA, revisiones y cohortes.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31563344](https://pubmed.ncbi.nlm.nih.gov/31563344/) | 2019 | ECA | Lancet Infect Dis | ASPECT-NP: ceftolozano/tazobactam vs meropenem en neumonía nosocomial por Gram negativos; Fase 3 de no inferioridad |
| [32785589](https://pubmed.ncbi.nlm.nih.gov/32785589/) | 2021 | ECA | Clin Infect Dis | RESTORE-IMI 2: imipenem/cilastatina/relebactam vs piperacilina/tazobactam en HABP/VABP |
| [39674398](https://pubmed.ncbi.nlm.nih.gov/39674398/) | 2025 | ECA | Int J Infect Dis | Fase 3 de no inferioridad de imipenem/relebactam vs piperacilina/tazobactam en HABP/VABP |
| [38823453](https://pubmed.ncbi.nlm.nih.gov/38823453/) | 2024 | Revisión sistemática | Clin Microbiol Infect | Metaanálisis en red de ECA sobre regímenes empíricos en neumonía nosocomial no asociada a ventilador |
| [38971203](https://pubmed.ncbi.nlm.nih.gov/38971203/) | 2024 | Revisión sistemática | Int J Antimicrob Agents | Farmacocinética y farmacodinamia de nuevos betalactámicos y combinaciones con inhibidores en neumonía por bacterias Gram negativas resistentes a carbapenémicos |
| [39701120](https://pubmed.ncbi.nlm.nih.gov/39701120/) | 2025 | Cohorte | Lancet Infect Dis | CACTUS: efectividad de ceftazidima-avibactam vs ceftolozano-tazobactam en *P. aeruginosa* multirresistente (estudio observacional retrospectivo) |
| [38902935](https://pubmed.ncbi.nlm.nih.gov/38902935/) | 2025 | Cohorte | Clin Infect Dis | Menor resistencia emergente con ceftolozano-tazobactam que con ceftazidima-avibactam (10% vs 40%) en bacteriemia o neumonía por *P. aeruginosa* multirresistente |
| [38862579](https://pubmed.ncbi.nlm.nih.gov/38862579/) | 2024 | Observacional | Sci Rep | Cefepima vs piperacilina/tazobactam en neumonía comunitaria grave en UCI (2026 pacientes, estimación por máxima verosimilitud dirigida) |
| [34158237](https://pubmed.ncbi.nlm.nih.gov/34158237/) | 2021 | Observacional | J Infect Chemother | Ceftriaxona vs piperacilina/tazobactam y carbapenémicos en neumonía por aspiración (pareamiento por puntaje de propensión) |
| [41305690](https://pubmed.ncbi.nlm.nih.gov/41305690/) | 2025 | Reporte de caso | Medicine | Linfohistiocitosis hemofagocítica inducida por piperacilina-tazobactam en un paciente con neumonía comunitaria; señal de seguridad rara pero grave |

## Información de Mercado en Colombia

Hay 16 registros sanitarios en total. Los registros del extracto corresponden todos al mismo producto, que se lista una sola vez.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20089767 | AUROTAZ-P 4.5 G | Polvo estéril para reconstituir a solución inyectable | Piperacilina e inhibidor enzimático |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay varios ECA de Fase 3 completados con regímenes que contienen tazobactam en neumonía nosocomial y asociada a ventilador (nivel L1), y las combinaciones ya están comercializadas en Colombia. La evidencia aplica solo a combinaciones fijas. En varios ensayos piperacilina/tazobactam es el comparador, y el uso ya está en gran parte aprobado, por lo que no es reposicionamiento novedoso.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), que actualmente falta
- Confirmar que el registro sanitario colombiano incluya neumonía como indicación aprobada; el texto actual no la detalla
- Datos detallados del mecanismo de acción (MOA) desde DrugBank
- Confirmar los brazos de tratamiento de los ensayos con títulos truncados
- Incluir en el plan de monitoreo de seguridad la reacción adversa rara pero grave reportada (linfohistiocitosis hemofagocítica), que puede quedar enmascarada por una procalcitonina elevada
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

