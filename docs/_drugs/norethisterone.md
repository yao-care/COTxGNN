---
layout: default
title: Norethisterone
parent: Evidencia Moderada (L3-L4)
nav_order: 472
evidence_level: L4
indication_count: 1
last_modified_at: 2026-10-28
description: "Norethisterone: nueva indicación predicha, Amenorrea (nivel de evidencia L4). Indicación original: Noretisterona y estrógeno"
monitor_inn: "Norethisterone"
predicted_indications: ["amenorrhea (disease)"]
---

# Norethisterone
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **1** 
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

## Noretisterona: De Noretisterona y Estrógeno a Amenorrea
{: .text-alpha }

## Resumen en Una Frase

Noretisterona es un progestágeno sintético, registrado en Colombia en una combinación con estrógeno (producto PRIMOSISTON®, hoy cancelado).
El modelo TxGNN predice que podría ser efectiva para **amenorrea**,
pero actualmente no hay ensayos clínicos registrados y la literatura disponible trata sobre todo de anticoncepción, donde la amenorrea aparece como efecto secundario y no como objetivo terapéutico.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Noretisterona y estrógeno |
| Nueva Indicación Predicha | Amenorrea |
| Puntaje de Prediccion TxGNN | 0.9960 |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la noretisterona es un progestágeno sintético derivado de la 19-nortestosterona, con fuerte actividad progestogénica. Según los datos farmacológicos disponibles, actúa sobre el receptor de progesterona (gen PGR) y se usa como anticonceptivo y para tratar trastornos menstruales como la endometriosis o el sangrado vaginal anormal por desequilibrio hormonal.

Mecanísticamente, la aplicación en amenorrea es plausible: en mujeres con estímulo estrogénico previo, la suspensión de un progestágeno puede inducir el desprendimiento del endometrio, y los regímenes con progestágeno pueden restaurar el sangrado cíclico. Sin embargo, este razonamiento se basa en el conocimiento general de la farmacología de los progestágenos y no en los datos aportados.

Conviene ser cautos: la literatura recopilada se centra en anticonceptivos hormonales, donde la amenorrea es un efecto adverso o un cambio del patrón de sangrado. El puntaje alto de TxGNN (0.996) es solo una predicción computacional y no constituye evidencia clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Se priorizan las revisiones sistemáticas y los estudios con diseño más robusto. La mayoría de las publicaciones tratan sobre anticoncepción hormonal, no sobre el tratamiento de la amenorrea.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38530848](https://pubmed.ncbi.nlm.nih.gov/38530848/) | 2024 | Ensayo aleatorizado (WHICH) | PLoS One | Compara el efecto de DMPA-IM y NET-EN inyectables sobre niveles de estradiol y medidas menstruales, psicológicas y conductuales |
| [8336583](https://pubmed.ncbi.nlm.nih.gov/8336583/) | 1993 | Ensayo aleatorizado | Med J Aust | Eficacia y aceptabilidad de terapia hormonal continua con dosis bajas de estrógeno y progestágeno |
| [23641480](https://pubmed.ncbi.nlm.nih.gov/23641480/) | 2013 | Revisión sistemática (Cochrane) | Cochrane Database Syst Rev | Anticonceptivos inyectables combinados: método eficaz y reversible; su aceptabilidad puede limitarse por cambios en el patrón de sangrado |
| [18843662](https://pubmed.ncbi.nlm.nih.gov/18843662/) | 2008 | Revisión sistemática (Cochrane) | Cochrane Database Syst Rev | Versión previa de la revisión sobre anticonceptivos inyectables combinados |
| [41489365](https://pubmed.ncbi.nlm.nih.gov/41489365/) | 2026 | Cohorte/Observacional | Biol Reprod | Los inyectables afectan de forma distinta el eje hipotálamo-hipófisis-gónadas; más amenorrea con DMPA-IM que con NET-EN |
| [6786825](https://pubmed.ncbi.nlm.nih.gov/6786825/) | 1981 | Ensayo de Fase I | Contraception | En 20 mujeres cubanas, enantato y acetato de noretisterona suprimieron los picos preovulatorios de LH y FSH; se observaron trastornos menstruales, incluida amenorrea |
| [3695501](https://pubmed.ncbi.nlm.nih.gov/3695501/) | 1987 | Estudio de formulación | J Steroid Biochem | Microesferas de noretisterona anticonceptivas; alteraciones del ciclo con episodios cortos de sangrado, manchado y amenorrea |
| [6230212](https://pubmed.ncbi.nlm.nih.gov/6230212/) | 1983 | Encuesta | Contraception | Manejo de alteraciones menstruales con anticonceptivos inyectables (DMPA, NET-EN) según 35 investigadores |
| [31056890](https://pubmed.ncbi.nlm.nih.gov/31056890/) | 2019 | Reporte de caso | JBRA Assist Reprod | Hipotiroidismo autoinmune e insuficiencia ovárica intermitente en mujer de 35 años con amenorrea secundaria |
| [12317413](https://pubmed.ncbi.nlm.nih.gov/12317413/) | 1987 | Revisión | Current Therapeutics | Revisión general de anticonceptivos orales |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 38690 | PRIMOSISTON® (estado: vigente) | Tableta | Noretisterona y estrógeno |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: el grafo de conocimiento asocia la noretisterona con contraindicación en las siguientes condiciones:
  - Cardiovasculares y metabólicas: hipertensión, diabetes mellitus, cetoacidosis diabética, hiperglucemia, hipertrigliceridemia.
  - Hepáticas, biliares y renales: enfermedad hepática, enfermedad de la vesícula biliar, enfermedad renal.
  - Neurológicas y psiquiátricas: epilepsia, trastornos de ansiedad, trastornos neuróticos, trastorno distímico.
  - Porfirias: porfiria hereditaria, trastornos del metabolismo de porfirinas.
  - Endocrinas y del metabolismo mineral: hipotiroidismo, mixedema, hipotiroidismo congénito, hipercalcemia, hipercalcemia humoral de la malignidad, nefrocalcinosis, trastornos del metabolismo del fósforo.
  - Inmunológicas y respiratorias: lupus eritematoso sistémico (incluido el pediátrico), asma (intrínseca y alérgica).
  - Oncológicas: carcinoma de mama femenino.
- **Interacciones farmacológicas**: solo se registró la interacción farmacológica con el receptor de progesterona (diana principal), sin interacciones con otros fármacos.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el modelo computacional (nivel de evidencia L4), sin ensayos clínicos y con literatura que aborda la amenorrea como efecto adverso de anticonceptivos. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA para completar advertencias y contraindicaciones, necesario antes de cualquier evaluación de seguridad.
- Completar los datos del mecanismo de acción (por ejemplo, consultando DrugBank).
- Buscar estudios que evalúen la noretisterona como tratamiento de la amenorrea (primaria o secundaria).
- Evaluar la compatibilidad de vías y formas farmacéuticas, y confirmar si existen productos vigentes con noretisterona en Colombia.
- Valorar las contraindicaciones señaladas por el grafo de conocimiento frente a la población objetivo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

