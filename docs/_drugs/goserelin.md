---
layout: default
title: Goserelin
parent: Solo Predicción del Modelo (L5)
nav_order: 321
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Goserelin: nueva indicación predicha, Amenorrea (nivel de evidencia L5). Indicación original: GOSERELINA"
monitor_inn: "goserelin"
predicted_indications: ["amenorrhea (disease)", "renal hypoplasia (disease)", "renal hypoplasia, bilateral"]
---

# Goserelin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Goserelina: De Indicación No Especificada en el Registro a Amenorrea (Supresión Ovárica Controlada)
{: .text-alpha }

## Resumen en Una Frase

Goserelina es un análogo de la hormona liberadora de gonadotropinas (GnRH), comercializado en Colombia como implante (ZOLADEX® LA 10.8 mg); el registro sanitario solo consigna el nombre del principio activo, sin detallar la indicación original.
El modelo TxGNN predice que podría ser efectivo para **amenorrea**, con **1 ensayo clínico** y **15 publicaciones** que respaldan esta dirección.
Conviene aclarar que esta "indicación" corresponde más a la inducción controlada de amenorrea (supresión ovárica) que al tratamiento de una amenorrea patológica.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | GOSERELINA (el registro no detalla la indicación) |
| Nueva Indicación Predicha | Amenorrea |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L1 (parcial: el único ensayo de Fase 3 no está completado y la amenorrea no es su desenlace principal) |
| Estado de Mercado en Colombia | Solo cancelado |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Goserelina es un agonista de GnRH. Su administración continua desensibiliza los receptores de GnRH de la hipófisis, lo que reduce la secreción de LH y FSH y la producción ovárica de estradiol. El resultado es una amenorrea reversible, conocida como supresión ovárica médica. Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción; la explicación anterior corresponde a la farmacología conocida del fármaco.

Por lo tanto, la amenorrea es un efecto farmacológico esperado y no un mecanismo novedoso. Se presenta sobre todo en el cáncer de mama premenopáusico, la endometriosis y la protección ovárica durante la quimioterapia. La literatura revisada respalda este enfoque, por ejemplo la publicación sobre la inducción de amenorrea (PMID 1533675), los estudios de goserelina en cáncer de mama premenopáusico (PMID 12488406 y 14679153) y el ensayo OPTION sobre protección ovárica con agonistas de GnRH (PMID 28472240).

Las otras dos predicciones (hipoplasia renal e hipoplasia renal bilateral) tienen puntajes altos (cerca de 99%), pero no muestran un vínculo mecanístico plausible ni ensayos ni publicaciones. Se consideran solo predicciones computacionales y se recomienda mantenerlas en espera (Hold).

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02132390](https://clinicaltrials.gov/study/NCT02132390) | Fase 3 | Desconocido | 300 | Toremifeno adyuvante con o sin goserelina en mujeres premenopáusicas con cáncer de mama en estadio I-IIIA con receptores hormonales positivos, con o sin amenorrea inducida por quimioterapia. La amenorrea no es el desenlace principal. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [12488406](https://pubmed.ncbi.nlm.nih.gov/12488406/) | 2002 | ECA | J Clin Oncol | Goserelina frente a CMF como terapia adyuvante en cáncer de mama premenopáusico con ganglios positivos (estudio ZEBRA) |
| [14679153](https://pubmed.ncbi.nlm.nih.gov/14679153/) | 2003 | ECA | J Natl Cancer Inst | Quimioterapia seguida de goserelina frente a cada modalidad por separado en cáncer de mama premenopáusico con ganglios negativos (IBCSG VIII) |
| [28472240](https://pubmed.ncbi.nlm.nih.gov/28472240/) | 2017 | Metaanálisis | Ann Oncol | Ensayo OPTION: los agonistas de GnRH durante la quimioterapia reducen el riesgo de insuficiencia ovárica prematura |
| [17159194](https://pubmed.ncbi.nlm.nih.gov/17159194/) | 2007 | Análisis secundario de ECA | J Clin Oncol | Impacto en amenorrea, sofocos y calidad de vida de quimioterapia seguida de goserelina (IBCSG VIII) |
| [8513962](https://pubmed.ncbi.nlm.nih.gov/8513962/) | 1993 | ECA | Fertil Steril | Agonista de GnRH frente a anticonceptivo oral de baja dosis para el dolor pélvico por endometriosis |
| [25187267](https://pubmed.ncbi.nlm.nih.gov/25187267/) | 2015 | Cohorte | Cancer Res Treat | La ablación ovárica con goserelina mejora la supervivencia en cáncer de mama estadio II/III sin amenorrea inducida por quimioterapia |
| [1533675](https://pubmed.ncbi.nlm.nih.gov/1533675/) | 1992 | Revisión | J R Army Med Corps | Inducción de amenorrea; la goserelina se describe como un método muy eficaz frente a los anticonceptivos orales continuos |
| [12353820](https://pubmed.ncbi.nlm.nih.gov/12353820/) | 2002 | Revisión | Breast Cancer Res Treat | Agonistas de LHRH en cáncer de mama temprano y beneficios de la ablación ovárica reversible |
| [12734855](https://pubmed.ncbi.nlm.nih.gov/12734855/) | 2003 | Revisión | Br J Surg | Métodos de ablación ovárica en el tratamiento adyuvante del cáncer de mama |
| [26951320](https://pubmed.ncbi.nlm.nih.gov/26951320/) | 2016 | Revisión | J Clin Oncol | Necesidad de monitorizar estradiol en mujeres con supresión ovárica por cáncer de mama |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 201182 (cancelado) | ZOLADEX® LA 10.8 MG (AstraZeneca Colombia S.A.S.) | Implante | GOSERELINA |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia hormonal (agonista de GnRH); no es un citotóxico convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** hipertensión, hiperglucemia, diabetes mellitus, cetoacidosis diabética, hipercalcemia, nefrocalcinosis, trastornos del metabolismo del fósforo, obesidad (incluida la monogénica) y obstrucción de las vías urinarias.
- **Interacciones farmacológicas:** se identificaron 371 interacciones potenciales. Las principales son:
  - **Mayor:** dolasetrón.
  - **Moderadas:** antidiabéticos (acarbosa, metformina, glimepirida, clorpropamida, canagliflozina, dapagliflozina, empagliflozina, alogliptina, linagliptina, saxagliptina, albiglutida, dulaglutida), claritromicina, famotidina, loperamida, bisacodilo, ácido picosulfúrico, polietilenglicol con electrolitos y palonosetrón.

  El patrón con antidiabéticos es coherente con las contraindicaciones del grafo relacionadas con hiperglucemia y diabetes.
- Las advertencias y contraindicaciones del prospecto no están disponibles. Consultar el prospecto para esta información.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La supresión ovárica con goserelina, que causa amenorrea reversible, tiene un sustento farmacológico sólido y respaldo en ECA y metaanálisis, sobre todo en cáncer de mama premenopáusico. Sin embargo, la amenorrea es un efecto esperado y no una indicación terapéutica independiente. El único ensayo de Fase 3 tiene estado desconocido y no evalúa la amenorrea como desenlace principal. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Definir con precisión la indicación objetivo (inducción de amenorrea o supresión ovárica, y no amenorrea patológica).
- Obtener el prospecto de INVIMA para completar las advertencias y contraindicaciones.
- Confirmar los datos detallados del mecanismo de acción en DrugBank.
- Aclarar la situación regulatoria: el registro 201182 está cancelado y no hay registros vigentes.
- Elaborar un plan de seguridad para pacientes con hipertensión, diabetes, alteraciones del calcio u obstrucción urinaria, y para el uso concomitante con antidiabéticos y fármacos que prolongan el QT (dolasetrón).
- Mantener en espera (Hold) las predicciones de hipoplasia renal por ausencia de evidencia y de vínculo mecanístico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

