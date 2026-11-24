---
layout: default
title: Febuxostat
parent: Evidencia Moderada (L3-L4)
nav_order: 278
evidence_level: L4
indication_count: 3
last_modified_at: 2026-11-24
description: "Febuxostat: nueva indicación predicha, Hipouricemia renal (nivel de evidencia L4). Indicación original: No especificada en el registro (el texto aprobado solo indica \"Febuxo…"
monitor_inn: "FEBUXOSTAT"
predicted_indications: ["hypouricemia, renal", "hypoxanthine guanine phosphoribosyltransferase partial deficiency", "Lesch-Nyhan syndrome"]
---

# Febuxostat
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **3** 
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

## Febuxostat: De Indicación No Especificada en el Registro a Hipouricemia Renal
{: .text-alpha }

## Resumen en Una Frase

Febuxostat es un inhibidor selectivo no purínico de la xantina oxidasa que reduce el ácido úrico sérico; los registros sanitarios de Colombia no detallan el texto de su indicación aprobada (solo figura el nombre del principio activo).
El modelo TxGNN predice que podría ser efectivo para **hipouricemia renal**, con **1 ensayo clínico** (de relevancia baja) y **2 publicaciones** de revisión/reporte. Sin embargo, el vínculo mecanístico es contradictorio, por lo que la predicción debe tomarse con mucha cautela.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto aprobado solo indica "Febuxostat") |
| Nueva Indicación Predicha | Hipouricemia renal |
| Puntaje de Predicción TxGNN | 0.9999 |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 5 de 6) |
| Número de Registros Sanitarios | 6 (vigentes: 5) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Febuxostat (traducción no oficial): «ULORIC, un inhibidor de la xantina oxidasa, logra su efecto terapéutico al disminuir el ácido úrico sérico. No se espera que ULORIC inhiba otras enzimas implicadas en la síntesis y el metabolismo de las purinas y las pirimidinas a concentraciones terapéuticas.» Texto original en inglés: "ULORIC, a xanthine oxidase inhibitor, achieves its therapeutic effect by decreasing serum uric acid. ULORIC is not expected to inhibit other enzymes involved in purine and pyrimidine synthesis and metabolism at therapeutic concentrations." ([DailyMed: Uloric (febuxostat) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=54de10ef-fe5f-4930-b91d-6bbb04c664bd), versión del 2025-12-24; consultado el 2026-11-19). Según la información conocida, febuxostat es un inhibidor selectivo no purínico de la xantina oxidasa que disminuye la formación de ácido úrico, y se utiliza en trastornos asociados a hiperuricemia.

En el caso de la hipouricemia renal, la lógica es **contraria**: se trata de una condición con ácido úrico ya bajo, causada por una reabsorción renal deficiente de urato (por ejemplo, pérdida de función de URAT1/GLUT9). Reducir aún más el urato no tiene sentido terapéutico, por lo que el puntaje elevado de TxGNN probablemente es un artefacto de la asociación entre el fármaco y el urato, y no un vínculo terapéutico real.

La única conexión plausible, y especulativa, es un reporte de caso de un futbolista adolescente con hipouricemia renal familiar (mutaciones en URAT1) y lesión renal aguda recurrente inducida por ejercicio, en quien se discute el posible uso de inhibidores de la xantina oxidorreductasa no purínicos como profilaxis. Esto no ha sido probado en ensayos clínicos con febuxostat.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Fase 4 | Desconocido | 100 | Estudio prospectivo controlado sobre el efecto del control del ácido úrico en la recurrencia de cálculos y la función renal en pacientes con litiasis e hiperuricemia. Relevancia baja: no se puede confirmar relación directa con hipouricemia renal. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Revisión | Clinical Rheumatology | Actualización sobre hipouricemia (urato sérico < 2 mg/dL) para el reumatólogo: etiología y abordaje. |
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Reporte de caso (clasificado como revisión) | Internal Medicine | Jugador de fútbol de 16 años con hipouricemia renal familiar (mutaciones en URAT1) y lesión renal aguda recurrente por ejercicio; se plantea el uso de inhibidores no purínicos de la xantina oxidorreductasa como profilaxis. |

---

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 20053122 | GOUTEX 120 MG | CAPSULA BLANDA | FEBUXOSTAT | Vigente |
| 20053123 | GOUTEX 80 MG | CAPSULA BLANDA | FEBUXOSTAT | Vigente |
| 20088755 | UREXIL® 80 MG TABLETAS RECUBIERTAS | TABLETA RECUBIERTA | FEBUXOSTAT | Vigente |
| 20122155 | FEBUDAY® 40 MG | TABLETA RECUBIERTA | FEBUXOSTAT | Vigente |
| 20191538 | FEBUDAY® 80 MG | TABLETA RECUBIERTA | FEBUXOSTAT | Vigente |

Se muestran 5 de 6 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no del prospecto)**: el grafo de conocimiento TxGNN (PrimeKG) asocia el fármaco con contraindicación en enfermedad cerebrovascular, accidente cerebrovascular, infarto cerebral, infarto de miocardio, trombosis coronaria y hemoglobinopatías.
- **Interacciones farmacológicas**: se identificaron 22 interacciones; entre las de nivel **mayor** destacan:
  - Mercaptopurina
  - Azatioprina
  - Leflunomida
  - Teriflunomida

  Entre las de nivel moderado se incluyen teofilina, aminofilina, difilina, oxtrifilina, metotrexato, tioguanina, epirrubicina, trabectedina, clofarabina, brentuximab vedotina, asparaginasa, pegaspargasa, naltrexona e interferones beta.

Para advertencias y contraindicaciones del prospecto, consultar el inserto oficial.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La hipouricemia renal es una condición de urato ya bajo, por lo que reducirlo más es mecanísticamente contraproducente. La evidencia disponible se limita a una revisión narrativa, un reporte de caso especulativo y un ensayo de fase 4 sin relación directa confirmada (nivel L4).

**Para avanzar se necesita:**
- Confirmar el mecanismo de acción y revisar si el vínculo terapéutico tiene sustento real o es un artefacto del modelo
- Obtener el inserto del INVIMA para advertencias y contraindicaciones
- Evaluar con especial atención el riesgo cardiovascular y cerebrovascular
- Considerar las otras indicaciones predichas, más coherentes mecanísticamente, como líneas de investigación alternativas:
  - **Deficiencia parcial de HPRT** (puntaje 0.9998, L4): racional biológico coherente, con evidencia solo de reportes de caso. Requiere monitorear el riesgo de nefropatía o litiasis por xantina.
  - **Síndrome de Lesch-Nyhan** (puntaje 0.9968, L4): posible alternativa en pacientes intolerantes a alopurinol; no actúa sobre las manifestaciones neuroconductuales, y existe poca información pediátrica.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Uloric (febuxostat) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=54de10ef-fe5f-4930-b91d-6bbb04c664bd) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

