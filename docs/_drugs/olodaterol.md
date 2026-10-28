---
layout: default
title: Olodaterol
parent: Solo Predicción del Modelo (L5)
nav_order: 482
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
description: "Olodaterol: nueva indicación predicha, Bronquitis (nivel de evidencia L5). Indicación original: Olodaterol y bromuro de tiotropio"
monitor_inn: "OLODATEROL"
predicted_indications: ["bronchitis"]
---

# Olodaterol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Olodaterol: De Olodaterol y Bromuro de Tiotropio a Bronquitis
{: .text-alpha }

## Resumen en Una Frase

Olodaterol es un agonista beta-2 de acción prolongada (LABA), registrado en Colombia en combinación con bromuro de tiotropio (Spiolto® Respimat®) en solución para inhalación.
El modelo TxGNN predice que podría ser efectivo para **bronquitis**, aunque no hay ensayos clínicos específicos en bronquitis y solo **2 publicaciones** indirectas (sobre EPOC) respaldan esta dirección.
La segunda predicción, **enfermedad pulmonar obstructiva** (EPOC), corresponde a la indicación ya establecida del fármaco, con **más de 30 ensayos clínicos** y **19 publicaciones**.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Olodaterol y bromuro de tiotropio |
| Nueva Indicación Predicha | Bronquitis |
| Puntaje de Predicción TxGNN | 0.9984 |
| Nivel de Evidencia | L5 (para bronquitis; la evidencia es indirecta y proviene de EPOC) |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos consultada. Según la información conocida, olodaterol es un agonista beta-2 adrenérgico de acción prolongada: la activación de los receptores beta-2 del músculo liso de las vías respiratorias eleva el AMPc intracelular y produce broncodilatación sostenida con una dosis diaria.

La bronquitis crónica es un componente de la EPOC, por lo que la broncodilatación podría aliviar la obstrucción del flujo de aire en ese fenotipo. Sin embargo, el puntaje tan alto del modelo (0.9984) probablemente refleja la cercanía entre "bronquitis" y "EPOC" en la ontología, más que evidencia independiente. No hay ensayos que incluyan específicamente pacientes con bronquitis, y la bronquitis aguda no cuenta con respaldo.

Cabe aclarar que la segunda predicción (enfermedad pulmonar obstructiva/EPOC) es la indicación aprobada del olodaterol y de la combinación tiotropio/olodaterol. No es un reposicionamiento real, sino una confirmación de que el modelo recupera una indicación conocida.

---

## Evidencia de Ensayos Clínicos

No hay ensayos clínicos registrados específicamente para bronquitis. A continuación se muestran los ensayos más relevantes de la segunda predicción (enfermedad pulmonar obstructiva/EPOC), que respaldan el uso establecido del fármaco:

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01431274](https://clinicaltrials.gov/study/NCT01431274) | Fase 3 | Completado | 2624 | TOnado 1: 52 semanas, tiotropio + olodaterol en combinación fija vs. componentes individuales en EPOC |
| [NCT00796653](https://clinicaltrials.gov/study/NCT00796653) | Fase 3 | Completado | 937 | Olodaterol 5 y 10 µg una vez al día vs. placebo y formoterol durante 48 semanas en EPOC |
| [NCT00793624](https://clinicaltrials.gov/study/NCT00793624) | Fase 3 | Completado | 906 | Estudio gemelo de 48 semanas de olodaterol vs. placebo y formoterol en EPOC |
| [NCT00782509](https://clinicaltrials.gov/study/NCT00782509) | Fase 3 | Completado | 644 | Olodaterol 5 y 10 µg vs. placebo durante 48 semanas en EPOC |
| [NCT01525615](https://clinicaltrials.gov/study/NCT01525615) | Fase 3 | Completado | 404 | Torracto: efecto de la combinación sobre la tolerancia al ejercicio a las 12 semanas |
| [NCT01694771](https://clinicaltrials.gov/study/NCT01694771) | Fase 3 | Completado | 1134 | Olodaterol + tiotropio vs. tiotropio solo durante 12 semanas sobre la función pulmonar |
| [NCT01533935](https://clinicaltrials.gov/study/NCT01533935) | Fase 3 | Completado | 291 | Efecto de 6 semanas de la combinación sobre hiperinsuflación y resistencia al ejercicio |
| [NCT01040689](https://clinicaltrials.gov/study/NCT01040689) | Fase 3 | Completado | 108 | Perfil de VEF1 de 24 horas de olodaterol vs. tiotropio en EPOC |
| [NCT03240575](https://clinicaltrials.gov/study/NCT03240575) | Fase 4 | Completado | 302 | ENERGITO 2: tiotropio/olodaterol vs. fluticasona/salmeterol en función pulmonar |
| [NCT05402020](https://clinicaltrials.gov/study/NCT05402020) | N/A | Completado | 17018 | Estudio observacional con datos del seguro de salud de Taiwán: tiotropio/olodaterol vs. ICS/LABA |

Además, existen ensayos de Fase 2 en asma (p. ej., [NCT01013753](https://clinicaltrials.gov/study/NCT01013753) y [NCT01311661](https://clinicaltrials.gov/study/NCT01311661)), que no corresponden a bronquitis.

---

## Evidencia de Literatura

Para bronquitis solo hay dos publicaciones, ambas sobre EPOC (evidencia indirecta):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Guía clínica | Basic & Clinical Pharmacology & Toxicology | Guías finlandesas para el diagnóstico y tratamiento farmacológico de la EPOC estable |
| [27354040](https://pubmed.ncbi.nlm.nih.gov/27354040/) | 2016 | Revisión | Am J Health-Syst Pharm | Farmacología, farmacocinética, eficacia y seguridad de olodaterol en EPOC |

Publicaciones adicionales relevantes de la predicción de EPOC:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31119643](https://pubmed.ncbi.nlm.nih.gov/31119643/) | 2019 | Revisión | Drugs | Combinación tiotropio/olodaterol para el mantenimiento a largo plazo de la EPOC |
| [26683033](https://pubmed.ncbi.nlm.nih.gov/26683033/) | 2016 | Revisión | Drugs | Varios estudios de Fase 3 (6-52 semanas) respaldan la eficacia de la combinación una vez al día |
| [25114521](https://pubmed.ncbi.nlm.nih.gov/25114521/) | 2014 | Comparación indirecta/metaanálisis | Int J COPD | Comparación indirecta de olodaterol e indacaterol |
| [41729543](https://pubmed.ncbi.nlm.nih.gov/41729543/) | 2026 | Estudio de efectividad comparativa | JAMA Internal Medicine | Efectividad y seguridad comparadas de inhaladores LAMA-LABA en EPOC |
| [33095662](https://pubmed.ncbi.nlm.nih.gov/33095662/) | 2021 | Revisión | Curr Med Res Opin | Reducción de exacerbaciones de EPOC con tiotropio + olodaterol |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20082364 (cancelado) | SPIOLTO® RESPIMAT® | Solución para inhalación | Olodaterol y bromuro de tiotropio |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total; las 20 mostradas son de nivel moderado. Entre ellas: epinefrina (incluidas las presentaciones oftálmica y tópica), efedrina (incluida la nasal), isometepteno, fenfluramina, fentermina, dietilpropión, claritromicina, cisaprida, y antieméticos como dolasetrón, palonosetrón y granisetrón. También figuran famotidina, loperamida, y agentes antidiabéticos como albiglutida, semaglutida, canagliflozina y ertugliflozina.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para bronquitis no hay ensayos clínicos específicos y el puntaje de 0.9984 probablemente refleja la relación ontológica con la EPOC. Además, el único registro sanitario en Colombia está cancelado. La predicción de EPOC, aunque tiene evidencia sólida (L1, múltiples ensayos de Fase 3 completados), corresponde a una indicación ya conocida y no constituye reposicionamiento.

**Para avanzar se necesita:**
- Definir si el interés es el fenotipo de bronquitis crónica dentro de la EPOC (más plausible) o la bronquitis en general; la bronquitis aguda no tiene respaldo.
- Análisis post hoc o subgrupos de los ensayos de EPOC en pacientes con bronquitis crónica.
- Datos del mecanismo de acción confirmados (p. ej., desde DrugBank).
- Obtener y revisar el prospecto de INVIMA para advertencias y contraindicaciones.
- Aclarar la situación regulatoria en Colombia (registro cancelado) y la disponibilidad de productos con olodaterol.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

