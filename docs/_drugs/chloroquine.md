---
layout: default
title: Chloroquine
parent: Solo Predicción del Modelo (L5)
nav_order: 152
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-28
description: "Chloroquine: nueva indicación predicha, Artritis idiopática juvenil poliarticular con factor reumatoide positivo (nivel de evidencia L5). Indicación original: No especificada en los registros"
monitor_inn: "chloroquine"
predicted_indications: ["rheumatoid factor-positive polyarticular juvenile idiopathic arthritis", "rheumatoid nodulosis", "juvenile chronic polyarthritis", "juvenile idiopathic arthritis"]
---

# Chloroquine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

## Cloroquina: De Indicación Original (no especificada) a Artritis Idiopática Juvenil Poliarticular con Factor Reumatoide Positivo
{: .text-alpha }

## Resumen en Una Frase

La cloroquina es un antimalárico con actividad inmunomoduladora; en Colombia sus registros sanitarios no detallan una indicación específica.
El modelo TxGNN predice que podría ser efectiva para **artritis idiopática juvenil poliarticular con factor reumatoide positivo**,
pero actualmente hay **0 ensayos clínicos** y solo **1 publicación** relacionada, que además trata de otro fármaco (leflunomida), por lo que la evidencia directa es nula.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en los registros (el texto registrado solo dice "CLOROQUINA") |
| Nueva Indicación Predicha | Artritis idiopática juvenil poliarticular con factor reumatoide positivo |
| Puntaje de Predicción TxGNN | 0.9941 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 2 de 2) |
| Número de Registros Sanitarios | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, la cloroquina es un antimalárico con efectos inmunomoduladores: inhibe la acidificación lisosomal y la autofagia, reduce la presentación de antígenos, disminuye la señalización de los receptores TLR y la producción de citocinas proinflamatorias.

Estas acciones son plausibles en la artritis autoinmune. Los antimaláricos (cloroquina e hidroxicloroquina) se han usado históricamente como antirreumáticos de acción lenta, incluida la artritis juvenil. Por ello, mecanísticamente podría ser aplicable a esta indicación.

Sin embargo, el puntaje alto de TxGNN es solo una predicción computacional. La única publicación recuperada para esta indicación específica estudia leflunomida, no cloroquina, por lo que no aporta respaldo directo.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [24334641](https://pubmed.ncbi.nlm.nih.gov/24334641/) | 2014 | Cohorte prospectiva | The Journal of Rheumatology | Experiencia clínica a largo plazo con leflunomida en artritis idiopática juvenil; no evalúa cloroquina |

Para la indicación general de artritis idiopática juvenil (predicciones relacionadas de rango 3 y 4) existen revisiones históricas que mencionan a la cloroquina como fármaco modificador de la enfermedad (p. ej., [PMID 2047820](https://pubmed.ncbi.nlm.nih.gov/2047820/), 1991, y [PMID 7409700](https://pubmed.ncbi.nlm.nih.gov/7409700/), 1980), así como un reporte de caso de bloqueo auriculoventricular de tercer grado bajo cloroquina ([PMID 9523387](https://pubmed.ncbi.nlm.nih.gov/9523387/), 1998). No se identificaron ensayos controlados de cloroquina en esta población.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19973372 (cancelado) | CLOROQUINA FOSFATO 250MG | Tableta | CLOROQUINA |
| 20305885 (cancelado) | CLOROQUINA TABLETAS 150 MG | Tableta | CLOROQUINA |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: epilepsia, porfiria (hereditaria y del metabolismo de porfirinas), enfermedad hepática, enfermedad de la vesícula biliar, enfermedades oculares y de la retina (retinitis, escotoma, trastornos de la visión, ceguera), trastornos de la audición, psoriasis y parapsoriasis, neutropenia, agranulocitosis y leucopenia, anemia (incluida macrocítica), deficiencia de G6PD, enfermedad por depósito de glucógeno, cistinuria, galactosemia y abuso o dependencia de sustancias.
- **Interacciones Farmacológicas**: se registran 467 interacciones. Entre las de nivel **mayor** figuran agalsidasa beta, bupropión, cisaprida, claritromicina, dolasetrón y granisetrón (varias con riesgo de prolongación del QT). Entre las de nivel moderado: famotidina, loperamida, aprepitant, metronidazol, antiácidos (hidróxido de aluminio, carbonato de calcio), cimetidina, sulfonilureas (glimepirida, glipizida, glibenclamida, clorpropamida, acetohexamida) e insulina humana (riesgo de hipoglucemia).
- **Señales de la literatura**: un caso de bloqueo AV completo y un caso de vitiligo asociados a cloroquina; la toxicidad cardíaca y ocular exige especial cautela en población pediátrica.

Para advertencias y contraindicaciones del prospecto, consultar el inserto aprobado por INVIMA.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo computacional (L5), sin ensayos clínicos y sin literatura que evalúe cloroquina en esta indicación. Además, los registros en Colombia están cancelados y existen señales de toxicidad cardíaca y ocular relevantes en niños.

**Para avanzar se necesita:**
- Revisión de literatura dirigida a cloroquina/hidroxicloroquina en artritis idiopática juvenil (preferiblemente ensayos controlados).
- Obtener el prospecto de INVIMA con advertencias y contraindicaciones.
- Confirmar el mecanismo de acción en DrugBank.
- Evaluar la viabilidad regulatoria, dado que no hay registros vigentes en Colombia, y comparar con la hidroxicloroquina, de perfil de seguridad más favorable.
- Plan de seguridad pediátrica (monitoreo oftalmológico, cardíaco y hematológico).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

