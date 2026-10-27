---
layout: default
title: Hydrocortisone
parent: Solo Predicción del Modelo (L5)
nav_order: 328
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Hydrocortisone: nueva indicación predicha, Alopecia areata (nivel de evidencia L5). Indicación original: HIDROCORTISONA"
monitor_inn: "Hydrocortisone"
predicted_indications: ["alopecia areata", "alopecia mucinosa", "telogen effluvium", "Quinquaud's folliculitis decalvans", "alopecia antibody deficiency", "hereditary hypotrichosis with recurrent skin vesicles", "alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome", "atrichia with papular lesions", "alopecia universalis onychodystrophy vitiligo"]
---

# Hydrocortisone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Hidrocortisona: De Hidrocortisona (indicación no detallada en el registro) a Alopecia Areata
{: .text-alpha }

## Resumen en Una Frase

La hidrocortisona es un glucocorticoide con registros sanitarios en Colombia en forma de cremas y lociones tópicas, aunque el texto de indicación del registro solo indica el nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para **alopecia areata**, con **1 ensayo clínico** (Fase 3, en el que la hidrocortisona fue el comparador) y **20 publicaciones** recuperadas, de las cuales solo una es un ensayo aleatorizado y gran parte son series de casos antiguas.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | HIDROCORTISONA (el registro sanitario no detalla la indicación) |
| Nueva Indicación Predicha | Alopecia areata |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L2 (ver nota) |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 5 (los 5 cancelados) |
| Decisión Recomendada | Hold |

*Nota sobre el nivel de evidencia:* los datos compilados asignan L1, pero según las reglas del informe L1 exige al menos 2 ECAs de Fase 3 completados. Aquí hay un solo ensayo de Fase 3 completado (n=41), por lo que el nivel que corresponde es L2. Además, la hidrocortisona fue el brazo comparador y no el brazo en investigación, lo que debilita aún más el respaldo.

---

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, la hidrocortisona es un glucocorticoide con efectos antiinflamatorios e inmunosupresores.

La alopecia areata es una enfermedad autoinmune mediada por linfocitos T que atacan los folículos pilosos. Por ello, la acción glucocorticoide local (reducir el infiltrado inmune alrededor del folículo) es mecanísticamente plausible, y los corticoides tópicos o intralesionales se usan en la práctica para esta enfermedad.

Sin embargo, hay una limitación importante: en el único ensayo directo, la hidrocortisona al 1% fue el comparador de baja potencia frente a clobetasol al 0.05%, y la publicación asociada (JAMA Dermatology, 2014, en niños) favorece al clobetasol. La eficacia propia de la hidrocortisona parece modesta. Los informes históricos de inyecciones intralesionales (décadas de 1950 a 1970) sugieren cierta actividad, pero son de baja calidad.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01453686](https://clinicaltrials.gov/study/NCT01453686) | Fase 3 | Completado | 41 | Ensayo aleatorizado en niños con alopecia areata que compara crema de clobetasol 0.05% con crema de hidrocortisona 1%; la hidrocortisona actúa como comparador de baja potencia |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [24226568](https://pubmed.ncbi.nlm.nih.gov/24226568/) | 2014 | ECA | JAMA Dermatology | Clobetasol 0.05% frente a hidrocortisona 1% en niños con alopecia areata; favorece al clobetasol |
| [15692503](https://pubmed.ncbi.nlm.nih.gov/15692503/) | 2005 | Reporte de casos | J Am Acad Dermatol | 4 casos de alopecia areata congénita tratados con minoxidil y corticoides tópicos, con periodos prolongados de quiescencia |
| [13368875](https://pubmed.ncbi.nlm.nih.gov/13368875/) | 1956 | Serie de casos | Medical Times | Tratamiento de alopecia areata con cortisona, hidrocortisona y sus análogos |
| [13610145](https://pubmed.ncbi.nlm.nih.gov/13610145/) | 1958 | Serie de casos | Der Hautarzt | Crecimiento de pelo tras inyección intracutánea de hidrocortisona |
| [13743659](https://pubmed.ncbi.nlm.nih.gov/13743659/) | 1960 | Serie de casos | Dermatologische Wochenschrift | Inyecciones subcutáneas de hidrocortisona en alopecia areata |
| [4755919](https://pubmed.ncbi.nlm.nih.gov/4755919/) | 1973 | Serie de casos | Przegl Dermatol | Inyecciones intralesionales de suspensión de acetato de hidrocortisona en formas graves |
| [24326563](https://pubmed.ncbi.nlm.nih.gov/24326563/) | 2013 | Preclínico | J Invest Dermatol Symp Proc | Análogos de hormona paratiroidea en modelo murino; no evalúa hidrocortisona |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19995931 | Hidrocortisona crema 1% | Crema tópica | HIDROCORTISONA |
| 19979968 | Hidrocortisona 1.0% | Crema tópica | HIDROCORTISONA |
| 19976372 | Hidrocortisona 1% crema | Crema tópica | HIDROCORTISONA |
| 20001046 | Cortisolona® loción 0.5% | Loción | HIDROCORTISONA |
| 20151048 | Suiphar Hidrotex loción | Loción | HIDROCORTISONA |

Los cinco registros figuran como cancelados; actualmente no hay registros vigentes.

---

## Consideraciones de Seguridad

- **Contraindicaciones (según relaciones del grafo de conocimiento, no según prospecto):** hipertensión, epilepsia, úlcera gástrica, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, hiperglucemia, infecciones virales (verrugas comunes, infección anogenital por virus del papiloma humano, sarampión, queratitis por herpes simple) y diversas deficiencias hipofisarias o hipogonadismos hipogonadotrópicos.
- **Interacciones farmacológicas:** se identificaron 100 interacciones, de las cuales se muestran 20. La de mayor gravedad es **adalimumab (Mayor)**. Entre las moderadas figuran zidovudina, isotretinoína, acarbosa, acebutolol, acetazolamida, ketorolaco, nifedipino, ibuprofeno, etinilestradiol, aldesleukina, alemtuzumab y algunas vacunas. Salbutamol y formoterol son de nivel menor.

No se dispone de advertencias del prospecto; consultar el prospecto para información de seguridad adicional.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Aunque el puntaje del modelo es alto y el mecanismo es plausible, la única evidencia directa es un ensayo pequeño en el que la hidrocortisona fue el comparador y resultó menos eficaz que un corticoide más potente. Además, no hay registros vigentes en Colombia y faltan datos de seguridad del prospecto. Los otros candidatos predichos (alopecia mucinosa, efluvio telógeno, entre otros) carecen de evidencia real y quedan en Hold.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto del INVIMA (advertencias y contraindicaciones).
- Completar los datos del mecanismo de acción desde DrugBank.
- Evidencia de ensayos en los que la hidrocortisona sea el brazo en investigación, o una comparación con corticoides de mayor potencia que justifique su uso.
- Evaluar si un corticoide de mayor potencia ya disponible es una opción más racional que la hidrocortisona para esta indicación.
- Aclarar la situación regulatoria, ya que los cinco registros están cancelados.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

