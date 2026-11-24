---
layout: default
title: Theophylline
parent: Solo Predicción del Modelo (L5)
nav_order: 622
evidence_level: L5
indication_count: 6
monitor_inn: "Theophylline"
predicted_indications: ["thrombotic disease", "nasal cavity disease", "laryngotracheitis", "tracheal disease", "pharyngitis", "acute laryngopharyngitis"]
last_modified_at: 2026-11-24
description: "Theophylline: nueva indicación predicha, Enfermedad trombótica (nivel de evidencia L5). Indicación original: El único registro sanitario encontrado solo muestra \"AMBROXOL\" en el…"
---

# Theophylline
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Teofilina: De Obstrucción Reversible de las Vías Respiratorias a Enfermedad Trombótica
{: .text-alpha }

## Resumen en Una Frase

La teofilina es una xantina utilizada clínicamente para la obstrucción reversible de las vías aéreas (asma, enfisema y bronquitis crónica). El modelo TxGNN predice que podría ser efectiva para la **enfermedad trombótica**, pero **no hay ensayos clínicos** y ninguna de las **19 publicaciones** recuperadas estudia la teofilina como tratamiento de la trombosis. La predicción es solo computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | El único registro sanitario encontrado solo muestra "AMBROXOL" en el campo de indicación, que es un principio activo y no una indicación clínica. El uso conocido de la teofilina (obstrucción reversible de las vías aéreas) proviene de datos de farmacología, no del texto de un registro sanitario local. |
| Nueva Indicación Predicha | Enfermedad trombótica |
| Puntaje de Predicción TxGNN | 0.9962 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Theophylline (traducción no oficial): «La teofilina tiene dos acciones diferenciadas en las vías respiratorias de los pacientes con obstrucción reversible: la relajación del músculo liso (es decir, broncodilatación) y la supresión de la respuesta de las vías respiratorias a los estímulos (es decir, efectos profilácticos no broncodilatadores).» Texto original en inglés: "Theophylline has two distinct actions in the airways of patients with reversible obstruction: smooth muscle relaxation (i.e., bronchodilation) and suppression of the response of the airways to stimuli (i.e., non-bronchodilator prophylactic effects)." ([DailyMed: Theo-24 (theophylline anhydrous) prescribing information, ENDO USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7a108fa0-c230-475f-be93-6f864b98a410), versión del 2024-07-08; consultado el 2026-11-19). Los datos farmacológicos compilados indican que la teofilina se une a los receptores de adenosina A1, A2A, A2B y A3. En la literatura general, la teofilina se describe además como inhibidor no selectivo de fosfodiesterasas.

Desde el punto de vista teórico, esas acciones podrían modular los niveles de AMP cíclico en las plaquetas y, con ello, su activación. Este es el único puente mecanístico plausible hacia la trombosis. Sin embargo, es una hipótesis y no un hallazgo demostrado: la relación entre una indicación respiratoria y una indicación vascular/hematológica no es directa.

La literatura recuperada no prueba esta hipótesis. Los artículos tratan sobre la farmacocinética de la ticlopidina, ensayos de biomarcadores plaquetarios (donde la teofilina se usa solo como componente de anticoagulantes de laboratorio) y un sensor analítico para medir teofilina. El puntaje de 0.9962 es una predicción del modelo sin respaldo clínico en los datos disponibles.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Ninguno de los siguientes trabajos evalúa la teofilina como terapia de la trombosis. Se listan como el material más cercano al tema.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Revisión | Clinical Pharmacokinetics | Farmacocinética de la ticlopidina, antiagregante plaquetario; no involucra teofilina como tratamiento. |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Revisión | CRC Critical Reviews in Biochemistry | Prostaglandinas, plaquetas y aterosclerosis; la prostaciclina eleva el AMPc plaquetario (concepto mecanístico general). |
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | Estudio in vitro | General Pharmacology | Milrinona y adenosina inhiben la agregación plaquetaria humana mediante AMPc; no estudia teofilina como terapia. |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | Métodos/Biomarcadores | British Journal of Haematology | Radioinmunoensayo del factor plaquetario 4; la teofilina se usa solo como componente del anticoagulante de muestra. |
| [25856065](https://pubmed.ncbi.nlm.nih.gov/25856065/) | 2015 | Métodos/Biomarcadores | Platelets | Medición de sCLEC-2 en plasma como marcador de activación plaquetaria. |
| [32824700](https://pubmed.ncbi.nlm.nih.gov/32824700/) | 2020 | Métodos/Biomarcadores | Cells | Efecto de la anticoagulación y el procesamiento de muestras sobre microARN sanguíneos. |
| [29220362](https://pubmed.ncbi.nlm.nih.gov/29220362/) | 2017 | Métodos/Biomarcadores | PLoS One | Preparación óptima de plasma para medir moléculas almacenadas en plaquetas. |
| [21719422](https://pubmed.ncbi.nlm.nih.gov/21719422/) | 2011 | Cohorte | Rheumatology (Oxford) | Activación plaquetaria y neutrofílica en la enfermedad de Behçet. |
| [15475744](https://pubmed.ncbi.nlm.nih.gov/15475744/) | 2004 | Cohorte | Inflammatory Bowel Diseases | Agregados plaqueta-leucocito en enfermedad inflamatoria intestinal. |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | Desarrollo analítico | Analytica Chimica Acta | Aptasensor electroquímico para detectar teofilina; sin relación terapéutica con trombosis. |

---

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 20005160 | TRIATUSIC® JARABE | JARABE | AMBROXOL | Vigente |

Se muestra el único registro sanitario de este principio activo en los datos del INVIMA, Código Único de Medicamentos.

<!-- licenses:end -->

<!-- review:begin co-lic-20261124b-theophylline-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "La lista de registros puede ser parcial." Eliminado: advertía que la lista de registros podría ser parcial. La tabla de Información de Mercado en Colombia se genera a partir de los datos del INVIMA (Código Único de Medicamentos, datos al 2026-11-23) e indica cuántos registros muestra del total. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261124b-theophylline-1 -->

El nombre del producto y los datos de origen sugieren que podría ser una asociación de varios principios activos, por lo que este registro no permite describir cómo está aprobada la teofilina como único ingrediente.

---

## Consideraciones de Seguridad

- **Contraindicaciones registradas en el grafo de conocimiento (no provienen del prospecto):** hipertensión, insuficiencia y enfermedad hepática, epilepsia, trastornos de ansiedad y otros trastornos mentales (psicóticos, esquizoafectivos, distímicos, neuróticos), porfiria, enfermedad renal, enfermedad de la vesícula biliar, trombocitopenia, neutropenia y agranulocitosis, hipotiroidismo y mixedema, úlcera péptica, glaucoma de ángulo abierto, diabetes mellitus y cetoacidosis diabética, hiperplasia prostática benigna y dermatitis herpetiforme.
- **Relevancia para la nueva indicación:** la trombocitopenia, junto con la neutropenia y la agranulocitosis, merece atención especial en un contexto hematológico/trombótico.
- **Interacciones farmacológicas:** los datos disponibles solo describen la unión a receptores de adenosina (A1, A2A, A2B, A3), no interacciones con otros medicamentos.

Para advertencias, contraindicaciones oficiales e interacciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto, pero no existe ningún ensayo ni estudio publicado que evalúe la teofilina en trombosis, por lo que el nivel de evidencia es L5. Además, la teofilina tiene un margen terapéutico estrecho y varias contraindicaciones registradas, entre ellas alteraciones hematológicas.

**Para avanzar se necesita:**
- Estudios preclínicos que midan el efecto de la teofilina sobre la agregación plaquetaria y la trombosis in vivo.
- Datos formales del mecanismo de acción (MOA) y su vínculo con la vía del AMPc plaquetario.
- Revisión del prospecto aprobado en Colombia (advertencias, contraindicaciones, interacciones) y aclaración de la composición del producto registrado.
- Evaluación comparativa frente a los antitrombóticos y antiagregantes ya establecidos.
- Si hay respaldo preclínico, diseñar un ensayo exploratorio con monitoreo de niveles séricos de teofilina y parámetros hematológicos.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Theo-24 (theophylline anhydrous) prescribing information, ENDO USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7a108fa0-c230-475f-be93-6f864b98a410) |
| 2026-11-24 | Eliminado: "La lista de registros puede ser parcial." | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

