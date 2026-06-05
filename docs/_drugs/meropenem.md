---
layout: default
title: Meropenem
parent: 僅模型預測 (L5)
nav_order: 169
evidence_level: L5
indication_count: 10
---

# Meropenem
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Meropenem: De Infecciones Bacterianas Graves a Artritis Bacteriana

## Resumen en Una Frase

Meropenem es un antibiótico carbapenem de amplio espectro, utilizado como tratamiento de reserva para infecciones bacterianas graves causadas por microorganismos multirresistentes (incluyendo neumonía hospitalaria, infecciones intraabdominales complicadas y meningitis bacteriana).
El modelo TxGNN predice que podría ser efectivo para **Artritis Bacteriana**,
con **1 ensayo clínico** y **20 publicaciones** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sin registros en Colombia; carbapenem IV de amplio espectro para infecciones bacterianas graves por gram-negativos |
| Nueva Indicación Predicha | Artritis bacteriana |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | Sin comercializar |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los registros consultados. Con base en la clase farmacológica conocida, meropenem es un carbapenem que actúa inhibiendo la síntesis de la pared celular bacteriana al unirse a proteínas de unión a penicilina (PBP), con espectro que cubre la mayoría de gram-negativos aerobios —incluyendo cepas productoras de ESBL— y muchos anaerobios. Su eficacia en infecciones graves sistémicas está ampliamente comprobada, y mecanisticamente es aplicable a artritis bacteriana.

La artritis bacteriana (artritis séptica) puede ser causada por microorganismos gram-negativos multirresistentes como *Klebsiella pneumoniae* productora de ESBL, *Pseudomonas aeruginosa*, y *Burkholderia pseudomallei* (agente de la melioidosis). Para todos estos patógenos, meropenem representa la opción de tratamiento de elección o rescate. Existe evidencia directa en la literatura: casos documentados de artritis séptica por ESBL-*Klebsiella* tratados exitosamente con meropenem, y series retrospectivas de melioidosis osteoarticular donde todos los aislamientos fueron susceptibles a meropenem.

La penetración de meropenem en tejidos articulares y óseos ha sido estudiada indirectamente a través de modelos PK: la tasa de penetración en tejido blando es comparable a la de líquidos corporales de baja proteína, y las concentraciones en líquido sinovial se estiman entre el 50-80% de las concentraciones plasmáticas, superando la MIC para los patógenos relevantes. El uso en cementos óseos de PMMA con fines locales también ha sido evaluado experimentalmente, confirmando estabilidad térmica adecuada.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01371656](https://clinicaltrials.gov/study/NCT01371656) | Fase 3 | Completado | 624 | Estudio de levofloxacino para prevención de bacteremia en niños con leucemia aguda o trasplante de células madre; relevancia indirecta (bacteremia puede diseminarse a articulaciones) |

> **Nota:** El único ensayo recuperado evalúa levofloxacino, no meropenem, y su objetivo es profilaxis de bacteremia en oncología pediátrica — no es un estudio de artritis bacteriana. No existen ensayos clínicos registrados que evalúen meropenem directamente en artritis bacteriana.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [17433752](https://pubmed.ncbi.nlm.nih.gov/17433752/) | 2007 | Reporte de caso | Joint Bone Spine | Artritis séptica aguda por *Klebsiella pneumoniae* productora de ESBL; tratamiento exitoso con meropenem + amikacina + lavado artroscópico |
| [39489417](https://pubmed.ncbi.nlm.nih.gov/39489417/) | 2024 | Revisión retrospectiva | Indian J Med Microbiology | 22 casos de melioidosis musculoesquelética; todos los aislamientos susceptibles a meropenem; artritis séptica confirmada en 9 casos |
| [35146367](https://pubmed.ncbi.nlm.nih.gov/35146367/) | 2021 | Cohorte retrospectiva | Le Infezioni in Medicina | Melioidosis osteoarticular: caracterización de pacientes con compromiso articular y óseo; meropenem como pilar terapéutico |
| [39380073](https://pubmed.ncbi.nlm.nih.gov/39380073/) | 2024 | Reporte de caso | J Med Case Reports | Melioidosis diseminada con artritis séptica, inicialmente confundida con tuberculosis; rescate con meropenem |
| [39288382](https://pubmed.ncbi.nlm.nih.gov/39288382/) | 2024 | Reporte de caso + Rev. sistemática | J Infect Developing Countries | Coinfección leptospirosis-melioidosis con osteomielitis; revisión sistemática de coinfecciones similares |
| [38139869](https://pubmed.ncbi.nlm.nih.gov/38139869/) | 2023 | Reporte de caso | Pharmaceuticals | Artritis séptica nativa de cadera por *Bacillus pumilus* y *Paenibacillus barengoltzii*; revisión de antibióticos de rescate incluyendo carbapenems |
| [38134096](https://pubmed.ncbi.nlm.nih.gov/38134096/) | 2023 | Reporte de caso | Medicine | Absceso del psoas por *Campylobacter fetus* en paciente con artritis gotosa; revisión de opciones antibióticas |
| [33857030](https://pubmed.ncbi.nlm.nih.gov/33857030/) | 2021 | Estudio de laboratorio | J Bone Joint Surg Am | Estabilidad térmica y cinética de elución de meropenem en cemento óseo PMMA; confirma utilidad para infecciones ortopédicas locales |
| [39193962](https://pubmed.ncbi.nlm.nih.gov/39193962/) | 2024 | Estudio clínico retrospectivo | Clinical Laboratory | Distribución de patógenos y resistencia antimicrobiana en infecciones óseas y articulares en niños <4 años; meropenem figura entre los antibióticos con mayor cobertura |
| [36804370](https://pubmed.ncbi.nlm.nih.gov/36804370/) | 2023 | Revisión sistemática/narrativa | Int J Antimicrob Agents | Uso fuera de indicación vs. recomendaciones formales de antibióticos convencionales y novedosos para infecciones por bacterias MDR; contexto de carbapenems como respaldo |

---

## Información de Mercado en Colombia

Meropenem no cuenta con registros sanitarios activos en Colombia según los datos disponibles. No hay productos comercializados bajo esta denominación común internacional en el sistema de licencias consultado.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de TxGNN es biológicamente plausible y hay evidencia clínica indirecta sólida (especialmente en melioidosis osteoarticular y artritis séptica por gram-negativos MDR), pero la base de evidencia actual se limita a reportes de casos y estudios retrospectivos de series pequeñas (L3), sin ensayos clínicos controlados que evalúen meropenem directamente en artritis bacteriana como indicación primaria. Adicionalmente, meropenem no tiene registro en Colombia, lo que representa una barrera regulatoria significativa.

**Para avanzar se necesita:**
- Datos de mecanismo de acción (MOA) completos desde DrugBank
- Datos de seguridad (advertencias, contraindicaciones, interacciones farmacológicas) desde el prospecto INVIMA o FDA
- Estudio de penetración en líquido sinovial: razón líquido sinovial/plasma documentada en humanos
- Prospective cohort o estudio observacional multicéntrico que evalúe meropenem en artritis séptica por gram-negativos MDR (diseño realista dado que un RCT es poco factible en esta indicación)
- Análisis de uso compasivo/fuera de indicación existente en Colombia o región para establecer base regulatoria
- Obtención de registro sanitario en Colombia como condición previa a cualquier aplicación clínica formal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

