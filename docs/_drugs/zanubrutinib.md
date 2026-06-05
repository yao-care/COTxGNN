---
layout: default
title: Zanubrutinib
parent: 僅模型預測 (L5)
nav_order: 239
evidence_level: L5
indication_count: 6
---

# Zanubrutinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Zanubrutinib: De Leucemia Linfocítica Crónica a Leucemia Mieloide

## Resumen en Una Frase

Zanubrutinib es un inhibidor selectivo de BTK (Bruton tirosina quinasa) de segunda generación, aprobado internacionalmente para el tratamiento de neoplasias malignas de células B, incluyendo leucemia linfocítica crónica/linfoma linfocítico pequeño (LLC/SLL) y linfoma del manto. El modelo TxGNN predice que podría ser efectivo para **leucemia mieloide**, con **2 ensayos clínicos** y **9 publicaciones** que actualmente informan sobre esta dirección. Sin embargo, ninguno de los ensayos evalúa directamente zanubrutinib en leucemia mieloide, y toda la literatura identificada corresponde a indicaciones de células B, por lo que el fundamento mecanicista es especulativo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Leucemia linfocítica crónica / Linfoma de células B (aprobación internacional; sin registro local) |
| Nueva Indicación Predicha | Leucemia mieloide (Myeloid leukemia) |
| Puntaje de Predicción TxGNN | 99.65% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos sobre el mecanismo de acción en la fuente de datos local. Según la información publicada, zanubrutinib es un inhibidor covalente e irreversible de BTK diseñado para superar las limitaciones de ibrutinib en cuanto a selectividad. Al ocupar el sitio activo de BTK de forma altamente selectiva, bloquea la señalización del receptor de células B (BCR), un eje crítico para la proliferación y supervivencia de neoplasias linfoides B. Su eficacia en LLC/SLL, linfoma del manto y macroglobulinemia de Waldenström ha sido extensamente documentada en ensayos fase 3.

La relación entre la indicación de células B y la leucemia mieloide es indirecta y de naturaleza especulativa. BTK se expresa principalmente en células del linaje B, pero hay evidencia de expresión residual en algunas células progenitoras mieloides. En ciertos subtipos de leucemia mieloide aguda (especialmente variantes con mutaciones FLT3-ITD), podrían activarse vías de señalización convergentes o paralelas que, teóricamente, podrían ser influenciadas por la inhibición de BTK. Sin embargo, esta hipótesis carece de validación clínica directa para zanubrutinib.

El modelo TxGNN probablemente captura similitudes topológicas entre enfermedades hematológicas malignas dentro del grafo de conocimiento biológico (compartición de nodos de genes, proteínas o vías), más que una relación de eficacia demostrada. Los 2 ensayos clínicos identificados utilizan PRT2527 y CG-806 como fármacos principales, y zanubrutinib aparece únicamente como agente comparador o combinado, sin ser el objeto de estudio para AML. La totalidad de la literatura relevante proviene de indicaciones de células B.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT05665530](https://clinicaltrials.gov/study/NCT05665530) | Fase 1 | Completado | 86 | Estudio de escalada de dosis de PRT2527 (inhibidor CDK9) en neoplasias hematológicas R/R. Zanubrutinib aparece como agente de combinación, no como fármaco principal para AML. El fármaco de estudio y zanubrutinib tienen mecanismos completamente distintos; relevancia indirecta (Grado C). |
| [NCT04477291](https://clinicaltrials.gov/study/NCT04477291) | Fase 1 | Terminado | 45 | Estudio de CG-806 (luxeptinib, inhibidor pan-BTK/FLT3) en AML/MDS R/R; terminado prematuramente. Ofrece referencia indirecta sobre la viabilidad del blanco BTK en AML, aunque CG-806 y zanubrutinib difieren significativamente en selectividad y perfil de seguridad (Grado C). |

> ⚠️ Ambos ensayos tienen relevancia **Grado C**: no evalúan directamente zanubrutinib como tratamiento para leucemia mieloide. No existe ningún ensayo clínico que pruebe zanubrutinib en esta indicación.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39647999](https://pubmed.ncbi.nlm.nih.gov/39647999/) | 2025 | ECA (Fase 3) | J Clin Oncol | Seguimiento mediano de 5 años del estudio SEQUOIA: zanubrutinib superior a bendamustina+rituximab en LLC/SLL sin tratamiento previo; confirma beneficio sostenido en supervivencia libre de progresión. |
| [40829104](https://pubmed.ncbi.nlm.nih.gov/40829104/) | 2026 | Análisis Clínico | Blood Advances | Análisis combinado de SEQUOIA y ALPINE (N=301) en LLC/SLL con del(17p) y/o mutación TP53; zanubrutinib demuestra eficacia y seguridad consistentes en esta población de alto riesgo. |
| [40334067](https://pubmed.ncbi.nlm.nih.gov/40334067/) | 2025 | Cohorte | Blood Advances | Zanubrutinib bien tolerado y eficaz en LLC/SLL intolerant a ibrutinib/acalabrutinib; resultados actualizados del estudio fase 2 BGB-3111-215. |
| [36400069](https://pubmed.ncbi.nlm.nih.gov/36400069/) | 2023 | Cohorte Retrospectiva | Lancet Haematology | Zanubrutinib prolonga duración del tratamiento al minimizar toxicidades en pacientes con neoplasias de células B intolerantes a BTKi previos. |
| [36402930](https://pubmed.ncbi.nlm.nih.gov/36402930/) | 2023 | Revisión | Leukemia | Posicionamiento de zanubrutinib como estándar de tratamiento en macroglobulinemia de Waldenström R/R; perfil de seguridad favorable versus ibrutinib. |
| [34959482](https://pubmed.ncbi.nlm.nih.gov/34959482/) | 2021 | Revisión | Pharmaceutics | Revisión de inhibidores de tirosina quinasa en leucemias crónicas: BCR-ABL1 en LMC y señalización BCR en LLC; contexto sobre el rol terapéutico de los TKIs en hematología. |
| [37150651](https://pubmed.ncbi.nlm.nih.gov/37150651/) | 2023 | Revisión de Seguridad | Clin Lymphoma Myeloma Leuk | Reactivación de hepatitis B en pacientes tratados con BTKi (ibrutinib, acalabrutinib, zanubrutinib); alerta de seguridad relevante para la práctica clínica. |
| [36325357](https://pubmed.ncbi.nlm.nih.gov/36325357/) | 2022 | Reporte de Caso | Front Immunol | Caso de coexistencia de macroglobulinemia de Waldenström y leucemia linfoblástica B aguda con mutaciones KMT2D y MECOM; tratado con zanubrutinib como parte del manejo de WM. |
| [38288815](https://pubmed.ncbi.nlm.nih.gov/38288815/) | 2024 | Revisión de Química | Anti-Cancer Agents Med Chem | Revisión de síntesis de fármacos anticancerígenos aprobados por FDA (2018–2021); incluye zanubrutinib únicamente como referencia química, sin datos de eficacia clínica. |

> ⚠️ Toda la literatura identificada corresponde a indicaciones de **células B (LLC/SLL, Waldenström)**. No existe literatura que evalúe directamente zanubrutinib en leucemia mieloide.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor covalente selectivo de BTK — Bruton tirosina quinasa) |
| Riesgo de Mielosupresión | Moderado (neutropenia reportada en ensayos clínicos; menor incidencia que ibrutinib por mayor selectividad off-target) |
| Clasificación de Emetogenicidad | Baja |
| Ítems de Monitoreo | Hemograma completo con diferencial, transaminasas hepáticas, creatinina/función renal, serología de hepatitis B antes del inicio |
| Protección en Manejo | Requiere precauciones estándar para fármacos antineoplásicos orales; consultar regulaciones locales de manejo de citotóxicos |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

> Nota de alerta: Un estudio de seguridad (PMID 37150651) identificó riesgo de **reactivación de hepatitis B** asociado a zanubrutinib y otros BTKi. Se recomienda evaluación serológica de VHB (HBsAg, anti-HBc) antes de iniciar tratamiento.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de TxGNN para zanubrutinib en leucemia mieloide carece de soporte clínico directo: no existen ensayos que evalúen zanubrutinib en AML, toda la literatura identificada corresponde a indicaciones de células B, y el vínculo mecanicista (expresión de BTK en células mieloides) es una hipótesis no validada. La puntuación alta del modelo refleja similitudes estructurales en el grafo de conocimiento, no evidencia de eficacia.

**Para avanzar se necesita:**
- Estudios preclínicos (in vitro / in vivo) que demuestren actividad de zanubrutinib en líneas celulares o modelos murinos de AML
- Análisis de expresión funcional de BTK en subtipos moleculares de leucemia mieloide (especialmente FLT3-ITD, MYD88-mutado)
- Datos de farmacocinética/farmacodinámica en contexto mieloide
- Datos completos de MOA y advertencias del prospecto oficial (actualmente [Data Gap])
- Obtención de registro sanitario en Colombia antes de cualquier uso clínico local
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

