---
layout: default
title: Modafinil
parent: Evidencia Moderada (L3-L4)
nav_order: 289
evidence_level: L4
indication_count: 1
---

# Modafinil
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **1** 
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

# Modafinilo: De Somnolencia Excesiva (uso conocido) a Insomnio

## Resumen en Una Frase

Modafinilo es un agente promotor de la vigilia, conocido por su uso en la somnolencia excesiva de la narcolepsia, la apnea obstructiva del sueño y el trastorno del sueño por turnos de trabajo.
El modelo TxGNN predice que podría ser efectivo para **Insomnio**, pero la predicción no tiene respaldo farmacológico claro: se recuperaron **29 ensayos clínicos** y **20 publicaciones**, y casi todos tratan el insomnio o la fatiga como síntoma comórbido, no como objetivo de tratamiento con modafinilo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto del registro solo dice «MODAFINIL»). El uso conocido es la somnolencia excesiva. |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99.85% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, modafinilo es un agente promotor de la vigilia, farmacológicamente distinto de otros estimulantes. Su eficacia está comprobada en la somnolencia excesiva asociada a narcolepsia, apnea obstructiva del sueño y trastorno del sueño por turnos.

Aquí la predicción es débil. Tanto la indicación original como el insomnio pertenecen al dominio sueño-vigilia, y eso probablemente explica el puntaje alto del modelo, que es una predicción basada en grafos y no en una razón farmacológica. Además, un fármaco que promueve la vigilia debería empeorar el insomnio, y el insomnio figura como efecto adverso descrito del producto. Lo más probable es que el vínculo sea un artefacto del grafo de conocimiento.

Los ensayos y publicaciones recuperados mencionan el insomnio como síntoma comórbido o desenlace. Casi todos evalúan la fatiga o la somnolencia diurna. Como el registro no trae indicaciones originales, no es posible una comparación de referencia.

## Evidencia de Ensayos Clínicos

Los ensayos más cercanos al tema son los que nombran el insomnio de forma explícita. Casi todos usan armodafinilo (enantiómero R del modafinilo), lo que los hace evidencia indirecta. Ninguno tiene calificación de relevancia completada, salvo NCT01091974 (grado B).

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00124384](https://clinicaltrials.gov/study/NCT00124384) | Fase 4 | Completado | 40 | Modafinilo solo o con terapia cognitivo-conductual para el insomnio (TCC-I) en insomnio primario. Evalúa función diurna y gravedad del insomnio. Es el único que prueba modafinilo directamente en insomnio, pero es pequeño. |
| [NCT01019187](https://clinicaltrials.gov/study/NCT01019187) | Fase 2 | Completado | 226 | TCC con o sin armodafinilo para insomnio y fatiga tras quimioterapia en sobrevivientes de cáncer. |
| [NCT01091974](https://clinicaltrials.gov/study/NCT01091974) | Fase 2 | Completado | 138 | ECA de cuatro brazos de TCC-I y armodafinilo en pacientes con cáncer de mama con trastornos del sueño. Calificado B (indirecto: el fármaco apunta a la fatiga, no al inicio del sueño). |
| [NCT01011218](https://clinicaltrials.gov/study/NCT01011218) | Fase 2 | Completado | 70 | Piloto de terapia conductual breve o TCC-I, con o sin armodafinilo 150 mg/día, para insomnio en cáncer de mama. |
| [NCT02552303](https://clinicaltrials.gov/study/NCT02552303) | N/A | Completado | 39 | Armodafinilo y/o TCC-I en insomnio comórbido con apnea del sueño; mide continuidad del sueño y adherencia a CPAP. |
| [NCT00626210](https://clinicaltrials.gov/study/NCT00626210) | Fase 4 | Terminado | 2 | Modafinilo para alteraciones sueño-vigilia en adultos mayores. Terminado con solo 2 participantes, sin valor estadístico. |
| [NCT06404099](https://clinicaltrials.gov/study/NCT06404099) | Fase 2 | Activo, no recluta | 361 | Protocolo de plataforma RECOVER-SLEEP para alteraciones del sueño en COVID prolongado. |
| [NCT06404086](https://clinicaltrials.gov/study/NCT06404086) | Fase 2 | Completado | 830 | Segundo protocolo de la plataforma RECOVER-SLEEP, mismo objetivo. |
| [NCT00582491](https://clinicaltrials.gov/study/NCT00582491) | N/A | Completado | 44 | Modafinilo, sueño y cognición en dependencia de cocaína, con 16 noches de internación. |
| [NCT00917748](https://clinicaltrials.gov/study/NCT00917748) | Fase 3 | Completado | 84 | Modafinilo para fatiga en cáncer de mama o próstata con docetaxel. El trastorno del sueño es un desenlace secundario. |

Los ensayos de Fase 3 recuperados con armodafinilo (NCT01305408, NCT01072630, NCT01072929) son de depresión bipolar y no aportan evidencia para insomnio.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [15824337](https://pubmed.ncbi.nlm.nih.gov/15824337/) | 2005 | ECA | Neurology | Modafinilo frente a placebo para la fatiga en esclerosis múltiple. |
| [18219235](https://pubmed.ncbi.nlm.nih.gov/18219235/) | 2008 | ECA | J Head Trauma Rehabil | Modafinilo para fatiga y somnolencia diurna en lesión cerebral traumática crónica. |
| [24312590](https://pubmed.ncbi.nlm.nih.gov/24312590/) | 2013 | Metaanálisis | PLoS One | Eficacia y seguridad de modafinilo en fatiga y somnolencia diurna asociadas a trastornos neurológicos. |
| [27010071](https://pubmed.ncbi.nlm.nih.gov/27010071/) | 2016 | Metaanálisis | Parkinsonism Relat Disord | Intervenciones farmacológicas para somnolencia y trastornos del sueño en Parkinson. |
| [18729534](https://pubmed.ncbi.nlm.nih.gov/18729534/) | 2008 | Revisión | Drugs | Revisión basada en evidencia de los usos aprobados y en investigación de modafinilo. |
| [22021174](https://pubmed.ncbi.nlm.nih.gov/22021174/) | 2011 | Revisión | Mov Disord | Revisión de la Movement Disorder Society sobre tratamientos de síntomas no motores del Parkinson. |
| [24272458](https://pubmed.ncbi.nlm.nih.gov/24272458/) | 2014 | Revisión | Neurotherapeutics | Tratamiento de los trastornos del sueño en Parkinson; para el insomnio la evidencia preliminar favorece TCC y terapia de luz. |
| [39535843](https://pubmed.ncbi.nlm.nih.gov/39535843/) | 2024 | Revisión | Expert Opin Pharmacother | Manejo farmacológico y no farmacológico de las alteraciones del sueño en Parkinson. |
| [17181377](https://pubmed.ncbi.nlm.nih.gov/17181377/) | 2006 | Revisión | Drugs | Carga y manejo del trastorno del sueño por turnos de trabajo. |
| [17060310](https://pubmed.ncbi.nlm.nih.gov/17060310/) | 2006 | Serie de casos | Am J Hosp Palliat Care | Modafinilo reduce la fatiga en Charcot-Marie-Tooth tipo 1A. |

Ninguna de estas publicaciones prueba modafinilo como tratamiento del insomnio.

## Información de Mercado en Colombia

El registro reporta 20 entradas, pero las cinco recuperadas son idénticas (mismo registro sanitario), por lo que se muestran una sola vez.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19968570 | VIGIA® 100 MG (PROCAPS S.A.) | Cápsula blanda | MODAFINIL (el registro no detalla la indicación) |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de TxGNN (99.85%) no tiene sustento farmacológico. Modafinilo promueve la vigilia y puede causar insomnio, y ningún ensayo grande y directo lo respalda para tratar el insomnio. Solo NCT00124384 lo prueba directamente, con 40 pacientes, y el resto es evidencia indirecta con armodafinilo. Por eso el nivel de evidencia se mantiene en L4.

**Para avanzar se necesita:**
- Revisar los resultados de NCT00124384 y calificar su relevancia, que sigue pendiente. El resumen del Evidence Pack indica que ningún estudio prueba modafinilo en insomnio, lo cual contradice este ensayo.
- Obtener el mecanismo de acción desde DrugBank para analizar el vínculo mecanístico.
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones), requisito bloqueante para el tamizaje de seguridad.
- Aclarar la indicación original aprobada en Colombia, ya que el registro solo muestra el nombre del fármaco.
- Sin un ECA propio de modafinilo en insomnio con resultados favorables, no se recomienda avanzar.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

