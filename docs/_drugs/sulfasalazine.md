---
layout: default
title: Sulfasalazine
parent: Evidencia Moderada (L3-L4)
nav_order: 597
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Sulfasalazine: nueva indicación predicha, Osteoartritis (nivel de evidencia L4). Indicación original: No especificada en el registro (el texto aprobado solo dice \"Sulfasal…"
monitor_inn: "Sulfasalazine"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "osteoarthritis susceptibility", "congenital hypotrichosis with juvenile macular dystrophy", "osteoarthritis", "WHIM syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "spondyloarthropathy, susceptibility to", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis"]
---

# Sulfasalazine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
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

# Sulfasalazina: De Indicación No Especificada en el Registro a Osteoartritis

## Resumen en Una Frase

Sulfasalazina es un fármaco antiinflamatorio e inmunomodulador que en Colombia cuenta con registros sanitarios cuyo texto de indicación solo menciona el nombre del principio activo, sin detallar la enfermedad.
El modelo TxGNN predice que podría ser efectivo para **osteoartritis** (puntaje 99.64 %), pero los datos compilados para este reporte incluyen **0 ensayos clínicos** y solo estudios **preclínicos** (in vitro y en animales) como respaldo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto aprobado solo dice "Sulfasalazina") |
| Nueva Indicación Predicha | Osteoartritis |
| Puntaje de Predicción TxGNN | 99.64 % |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

**Nota sobre la selección de la indicación:** la predicción de mayor rango (rank 1) es el síndrome de braquidactilia-sindactilia, con evidencia L5 y sin ningún vínculo mecanístico plausible. Este informe se centra en la osteoartritis, la primera predicción con evidencia real y un mecanismo verosímil. Otra predicción con respaldo es la susceptibilidad a espondiloartropatía (puntaje 99.53 %, L4), que en la práctica corresponde a un uso ya establecido del fármaco más que a un reposicionamiento. Las demás predicciones del top 10 son enfermedades congénitas raras sin evidencia (L5).

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según lo conocido, la sulfasalazina se usa en artritis reumatoide y enfermedad inflamatoria intestinal, y se le atribuyen la inhibición de NF-kB, la inhibición del transportador de cistina/glutamato xCT (SLC7A11) y una acción antiinflamatoria e inmunomoduladora. Su actividad antibacteriana se atribuye a la inhibición de la dihidropteroato sintasa, pero no tiene relación con esta predicción.

La osteoartritis tiene un componente inflamatorio y catabólico en el cartílago y la sinovial, impulsado por citocinas y vías como NF-kB. Los estudios preclínicos respaldan esta lógica: la sulfasalazina bloqueó la liberación de proteoglicanos y colágeno en cartílago estimulado con citocinas y redujo las metaloproteinasas (PMID 19690126). También atenuó la destrucción de cartílago en un modelo animal de transección del ligamento cruzado y meniscectomía mediante la inhibición del antiportador cistina/glutamato (PMID 26466556). Además, una formulación de sulfasalazina con ácido hialurónico redujo la inflamación y la degradación del cartílago en un modelo de osteoartritis en rata (PMID 29548914).

Es importante ser prudente: la evidencia se limita a trabajos in vitro, ex vivo y en animales, más revisiones indirectas sobre artritis inflamatoria. No se identificaron ensayos clínicos en osteoartritis, por lo que el vínculo mecanístico es plausible pero no está demostrado en humanos.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Se muestran las publicaciones más relevantes para la predicción (se excluyen trabajos sin relación con la eficacia en osteoartritis, como telemedicina, enfermedad pulmonar intersticial por antirreumáticos o receptores TAM en artritis reumatoide).

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [26466556](https://pubmed.ncbi.nlm.nih.gov/26466556/) | 2016 | Preclínico (modelo animal) | J Orthop Res | La sulfasalazina atenúa la destrucción de cartílago tras transección del LCA y meniscectomía, mediante inhibición del antiportador cistina/glutamato |
| [29548914](https://pubmed.ncbi.nlm.nih.gov/29548914/) | 2018 | Preclínico (rata) | Int J Biol Macromol | Sulfasalazina con ácido hialurónico: liberación sostenida hasta 60 días y reducción de inflamación y degradación del cartílago |
| [19690126](https://pubmed.ncbi.nlm.nih.gov/19690126/) | 2009 | Preclínico (explante de cartílago) | Rheumatology (Oxford) | Bloquea la liberación de proteoglicanos y colágeno por citocinas y reduce metaloproteinasas |
| [24329131](https://pubmed.ncbi.nlm.nih.gov/24329131/) | 2014 | Preclínico (condrocitos in vitro) | Mod Rheumatol | Sulfasalazina y tofacitinib modifican el perfil de proteínas de condrocitos articulares |
| [1673814](https://pubmed.ncbi.nlm.nih.gov/1673814/) | 1991 | Preclínico (in vitro) | Wien Klin Wochenschr | Efecto de la sulfasalazina y sus metabolitos sobre la liberación de prostaglandinas y leucotrienos en tejido sinovial humano |
| [35958605](https://pubmed.ncbi.nlm.nih.gov/35958605/) | 2022 | Revisión | Front Immunol | La ferroptosis (vía xCT) como vía hipotética en artritis inflamatorias, incluida la osteoartritis |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20168960 (cancelado) | Sulfasalazina 500 mg tableta con cubierta entérica (Genfar S.A.) | Tableta con cubierta entérica (gragea) | Sulfasalazina |
| 201145 (cancelado) | Rosulfant® 500 mg (Ropsohn Therapeutics S.A.S.) | Tableta con recubrimiento entérico | Sulfasalazina |

---

## Consideraciones de Seguridad

- **Contraindicaciones / condiciones de riesgo (según relaciones del grafo de conocimiento TxGNN, no según el prospecto):** porfiria (hereditaria y del metabolismo de porfirinas), enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, asma (intrínseca y alérgica), neutropenia, agranulocitosis, anemia aplásica (idiopática y otras), acetilación lenta, deficiencia de G6PD, enfermedad por depósito de glucógeno, cistinuria, galactosemia, obstrucción de las vías urinarias y piouréter.
- **Interacciones y farmacología:** se registra una interacción con el transportador de folato acoplado a protones (SLC46A1), lo que sugiere posible interferencia con la absorción de folato. No se dispone de interacciones con otros fármacos.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de osteoartritis solo cuenta con evidencia preclínica (L4), sin ensayos clínicos, y en Colombia no hay registros vigentes del fármaco. Además, el perfil de riesgo (hematológico, hepático, renal, G6PD) exige cautela antes de plantear su uso en una enfermedad crónica y prevalente como la osteoartritis. Se considera una pregunta de investigación, no una candidata lista para avanzar.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto oficial (advertencias y contraindicaciones), dado que ese dato falta y bloquea el tamizaje de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Generar o identificar evidencia clínica en osteoartritis (ensayos de fase 2 en humanos) y evaluar vías de administración y formulaciones (por ejemplo, intraarticular con ácido hialurónico).
- Aclarar la situación regulatoria: ambos registros están cancelados, por lo que habría que evaluar un nuevo registro o una vía de importación.
- Evaluar por separado la predicción de espondiloartropatía, que corresponde a un uso ya reconocido de la sulfasalazina y requiere más una clarificación de etiquetas que un reposicionamiento.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

