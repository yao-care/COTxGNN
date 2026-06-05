---
layout: default
title: Omalizumab
parent: 僅模型預測 (L5)
nav_order: 185
evidence_level: L5
indication_count: 10
---

# Omalizumab
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

# Omalizumab: De Asma Alérgica Severa a Bronquitis

## Resumen en Una Frase

Omalizumab es un anticuerpo monoclonal humanizado anti-IgE aprobado internacionalmente para el tratamiento del asma alérgica moderada a grave y la urticaria espontánea crónica.
El modelo TxGNN predice que podría ser efectivo para **Bronquitis**, con **2 ensayos clínicos** y **8 publicaciones** que actualmente abordan esta dirección.
Sin embargo, la evidencia directa en bronquitis es escasa y la conexión mecanística con la bronquitis general es débil.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Asma alérgica moderada a grave (aprobado por FDA/EMA; sin registro en Colombia) |
| Nueva Indicación Predicha | Bronquitis |
| Puntaje de Predicción TxGNN | 99.999% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Omalizumab actúa bloqueando el eje IgE-FcεRI: se une específicamente al dominio Cε3 de la IgE libre circulante, impidiendo su unión a los receptores de alta afinidad en mastocitos, basófilos y células dendríticas. Esta acción reduce la desgranulación de mastocitos, la infiltración eosinofílica y la cascada inflamatoria tipo Th2 en las vías respiratorias, constituyendo la base de su eficacia aprobada en asma alérgica.

La conexión con la bronquitis reside en que ciertos subtipos —particularmente la **bronquitis eosinofílica de base alérgica**— comparten con el asma el componente inflamatorio mediado por IgE. En pacientes atópicos, la activación del eje IgE puede agravar y perpetuar los episodios bronquíticos recurrentes. El ensayo NCT02049294 evaluó específicamente el efecto ahorrador de corticosteroides de omalizumab en bronquitis eosinofílica persistente, lo que representa el único vínculo clínico directo.

No obstante, la bronquitis común es predominantemente de origen infeccioso o por irritantes ambientales, sin un componente IgE determinante en la patogénesis. El vínculo mecanístico de omalizumab es indirecto y se limita a un subgrupo reducido con bronquitis de base alérgica/eosinofílica. El puntaje TxGNN elevado refleja probablemente la proximidad estructural entre bronquitis y asma en el grafo de conocimiento, más que una relación terapéutica directamente aplicable.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02049294](https://clinicaltrials.gov/study/NCT02049294) | Fase 2/3 | Completado | 11 | ECA doble ciego para evaluar si omalizumab permite reducir la dosis de prednisona en pacientes con asma y bronquitis eosinofílica persistente; muestra muy reducida, evidencia preliminar |
| [NCT02477332](https://clinicaltrials.gov/study/NCT02477332) | Fase 2 | Completado | 382 | Estudio de búsqueda de dosis de QGE031 (anticuerpo anti-IgE) en urticaria espontánea crónica; relacionado indirectamente al mecanismo anti-IgE en enfermedades de vías aéreas |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35369622](https://pubmed.ncbi.nlm.nih.gov/35369622/) | 2022 | Cohorte/Observacional | Postepy Dermatologii i Alergologii | Omalizumab en asma alérgica grave con solapamiento EPOC en pacientes mayores; sugiere beneficio en fenotipos mixtos de obstrucción de vías aéreas |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Revisión | Expert Opinion on Pharmacotherapy | Revisión del manejo del asma asociada con bronquitis crónica y EPOC inducida por tabaco (ACO); el uso de biológicos en este solapamiento es incierto por exclusión de ensayos |
| [26466493](https://pubmed.ncbi.nlm.nih.gov/26466493/) | 2015 | Revisión | Masui. The Japanese Journal of Anesthesiology | Manejo preoperatorio del asma bronquial y la bronquitis crónica; omalizumab citado como opción para asma alérgica grave en contexto perioperatorio |
| [16222080](https://pubmed.ncbi.nlm.nih.gov/16222080/) | 2005 | Revisión | Clinical Reviews in Allergy & Immunology | Revisión de aprobación y experiencia post-comercialización de omalizumab en asma; mecanismo anti-IgE con reducción de inflamación de vías aéreas |
| [21121874](https://pubmed.ncbi.nlm.nih.gov/21121874/) | 2011 | Estudio de seguridad | Current Medical Research and Opinion | Análisis agrupado de seguridad de omalizumab en niños con asma alérgica mediada por IgE; perfil de tolerabilidad favorable |
| [17663923](https://pubmed.ncbi.nlm.nih.gov/17663923/) | 2007 | Revisión | Allergologia et Immunopathologia | Actualización sobre anticuerpos monoclonales en pediatría, incluido omalizumab para enfermedades alérgicas respiratorias |
| [31478531](https://pubmed.ncbi.nlm.nih.gov/31478531/) | 2019 | Reporte de caso | J Investig Allergol Clin Immunol | Caso raro de bronquitis plástica tras termoplastia bronquial; sin tratamiento con omalizumab, relevancia indirecta al contexto de vías aéreas |
| [21163396](https://pubmed.ncbi.nlm.nih.gov/21163396/) | 2010 | Revisión | Revue des Maladies Respiratoires | Revisión de exacerbaciones del asma en el adulto; definición, fisiopatología y tratamiento; contexto de referencia para distinción asma-bronquitis |

---

## Información de Mercado en Colombia

Omalizumab no cuenta con registros sanitarios INVIMA vigentes en Colombia a la fecha de este informe (junio 2026). El medicamento no está comercializado en el país.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia directa de omalizumab en bronquitis es insuficiente para justificar un avance: solo existe un ensayo clínico con 11 pacientes para bronquitis eosinofílica y ningún ECA de Fase 2/3 completado con bronquitis como indicación primaria. La bronquitis en general no está impulsada por mecanismos IgE, lo que limita la aplicabilidad del mecanismo de acción a un subgrupo muy específico y de difícil identificación en la práctica clínica colombiana.

**Para avanzar se necesita:**
- Datos completos del mecanismo de acción (MOA) disponibles en el prospecto oficial
- Definición del subgrupo candidato: pacientes con bronquitis eosinofílica recurrente con IgE elevado y atopia documentada
- Ensayos clínicos de mayor escala con bronquitis como indicación primaria (no como subgrupo de estudios de asma)
- Obtención de registro sanitario INVIMA como requisito previo indispensable para cualquier desarrollo en Colombia
- Información de advertencias y contraindicaciones del prospecto para evaluación de seguridad inicial
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

