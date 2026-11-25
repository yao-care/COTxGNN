---
layout: default
title: Sulfasalazine
parent: Solo Predicción del Modelo (L5)
nav_order: 597
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-25
monitor_inn: "Sulfasalazine"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "congenital hypotrichosis with juvenile macular dystrophy", "osteoarthritis", "WHIM syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis"]
description: "Sulfasalazine: nueva indicación predicha, Brachydactyly-syndactyly syndrome (nivel de evidencia L5). Indicación original: SULFASALAZINA"
---

# Sulfasalazine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

## Sulfasalazine: Brachydactyly-syndactyly syndrome
{: .text-alpha }

## Resumen en Una Frase

Sulfasalazina es un fármaco antiinflamatorio e inmunomodulador que en Colombia cuenta con registros sanitarios cuyo texto de indicación solo menciona el nombre del principio activo, sin detallar la enfermedad.
El modelo TxGNN predice que podría ser efectivo para **osteoartritis** (puntaje 0.9964), pero los datos compilados para este reporte incluyen **0 ensayos clínicos** y solo estudios **preclínicos** (in vitro y en animales) como respaldo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | SULFASALAZINA |
| Nueva Indicación Predicha | Brachydactyly-syndactyly syndrome |
| Puntaje de Predicción TxGNN | 0.9994 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 3 de 5) |
| Número de Registros Sanitarios | 5 (vigentes: 3) |
| Decisión Recomendada | Hold |

**Nota sobre la selección de la indicación:** la predicción de mayor rango (rank 1) es el síndrome de braquidactilia-sindactilia, con evidencia L5 y sin ningún vínculo mecanístico plausible. Este informe se centra en la osteoartritis, la primera predicción con evidencia real y un mecanismo verosímil. Las demás predicciones del top 10 son enfermedades congénitas raras sin evidencia (L5).

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Clinical Pharmacology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Sulfasalazine (traducción no oficial): «El modo de acción de la sulfasalazina (SSZ) o de sus metabolitos, el ácido 5-aminosalicílico (5-ASA) y la sulfapiridina (SP), puede estar relacionado con las propiedades antiinflamatorias y/o inmunomoduladoras observadas en modelos animales e in vitro, con su afinidad por el tejido conjuntivo y/o con la concentración relativamente alta que alcanza en los líquidos serosos, el hígado y las paredes intestinales, como se demostró en estudios autorradiográficos en animales. En la colitis ulcerosa, los estudios clínicos en los que se utilizó la administración rectal de SSZ, SP y 5-ASA han indicado que la acción terapéutica principal podría residir en la fracción 5-ASA.» Texto original en inglés: "The mode of action of sulfasalazine (SSZ) or its metabolites, 5-aminosalicylic acid (5-ASA) and sulfapyridine (SP), may be related to the anti-inflammatory and/or immunomodulatory properties that have been observed in animal and in vitro models, to its affinity for connective tissue, and/or to the relatively high concentration it reaches in serous fluids, the liver and intestinal walls, as demonstrated in autoradiographic studies in animals. In ulcerative colitis, clinical studies utilizing rectal administration of SSZ, SP and 5-ASA have indicated that the major therapeutic action may reside in the 5-ASA moiety." ([DailyMed: Azulfidine En-Tabs (sulfasalazine) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b9ef541a-93c8-4428-ba45-398aa0b327d1), versión del 2026-10-27; consultado el 2026-11-19). Según lo conocido, la sulfasalazina se usa en artritis reumatoide y enfermedad inflamatoria intestinal, y se le atribuyen la inhibición de NF-kB, la inhibición del transportador de cistina/glutamato xCT (SLC7A11) y una acción antiinflamatoria e inmunomoduladora. Su actividad antibacteriana se atribuye a la inhibición de la dihidropteroato sintasa, pero no tiene relación con esta predicción.

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

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 19947421 | SULFASALAZINA 500 MG TABLETAS | TABLETA CON CUBIERTA ENTERICA CON PELICULA | SULFASALAZINA | Vigente |
| 20026114 | SALAZIN® | TABLETA DE LIBERACION RETARDADA | SULFASALAZINA | Vigente |
| 20168960 | SULFASALAZINA 500 MG TABLETA CON CUBIERTA ENTÉRICA | TABLETA CON CUBIERTA ENTERICA(GRAGEA) | SULFASALAZINA | Vigente |
| 201145 | ROSULFANT® 500 MG | TABLETA CON RECUBRIMIENTO ENTÉRICO | SULFASALAZINA | Temp. no comerc - Vigente |
| 20077756 | SULFASALAZINA GRAGEAS | TABLETA CON CUBIERTA ENTERICA(GRAGEA) | SULFASALAZINA | Temp. no comercializado - En Trámite Renov |

Se muestran los 5 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

- **Contraindicaciones / condiciones de riesgo (según relaciones del grafo de conocimiento TxGNN, no según el prospecto):** porfiria (hereditaria y del metabolismo de porfirinas), enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, asma (intrínseca y alérgica), neutropenia, agranulocitosis, anemia aplásica (idiopática y otras), acetilación lenta, deficiencia de G6PD, enfermedad por depósito de glucógeno, cistinuria, galactosemia, obstrucción de las vías urinarias y piouréter.
- **Interacciones y farmacología:** se registra una interacción con el transportador de folato acoplado a protones (SLC46A1), lo que sugiere posible interferencia con la absorción de folato. No se dispone de interacciones con otros fármacos.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de osteoartritis solo cuenta con evidencia preclínica (L4), sin ensayos clínicos. Además, el perfil de riesgo (hematológico, hepático, renal, G6PD) exige cautela antes de plantear su uso en una enfermedad crónica y prevalente como la osteoartritis. Se considera una pregunta de investigación, no una candidata lista para avanzar.

<!-- review:begin co-lic-20261105-sulfasalazine-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción de osteoartritis solo cuenta con evidencia preclínica (L4), sin ensayos clínicos, y en Colombia no hay registros vigentes del fármaco." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-sulfasalazine-1 -->

**Para avanzar se necesita:**
- Obtener y revisar el prospecto oficial (advertencias y contraindicaciones), dado que ese dato falta y bloquea el tamizaje de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Generar o identificar evidencia clínica en osteoartritis (ensayos de fase 2 en humanos) y evaluar vías de administración y formulaciones (por ejemplo, intraarticular con ácido hialurónico).
- Evaluar por separado la predicción de espondiloartropatía, que corresponde a un uso ya reconocido de la sulfasalazina y requiere más una clarificación de etiquetas que un reposicionamiento.

<!-- review:begin co-lic-20261105-sulfasalazine-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Aclarar la situación regulatoria: ambos registros están cancelados, por lo que habría que evaluar un nuevo registro o una vía de importación. / Evaluar por separado la predicción de espondiloartropatía, que corresponde a un uso ya reconocido de la sulfasalazina y requiere más una clarificación de etiquetas que un reposicionamiento." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-sulfasalazine-2 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "y en Colombia no hay registros vigentes del fármaco" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Aclarar la situación regulatoria: ambos registros están cancelados, por lo que habría que evaluar un nuevo registro o una vía de importación" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Azulfidine En-Tabs (sulfasalazine) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b9ef541a-93c8-4428-ba45-398aa0b327d1) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

