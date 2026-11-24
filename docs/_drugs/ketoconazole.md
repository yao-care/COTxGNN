---
layout: default
title: Ketoconazole
parent: Evidencia Moderada (L3-L4)
nav_order: 366
evidence_level: L4
indication_count: 1
last_modified_at: 2026-11-24
description: "Ketoconazole: nueva indicación predicha, Acné (nivel de evidencia L4). Indicación original: Ketoconazol"
monitor_inn: "ketoconazole"
predicted_indications: ["acne (disease)"]
---

# Ketoconazole
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

## Ketoconazol: De Ketoconazol (indicación sin detallar) a Acné
{: .text-alpha }

## Resumen en Una Frase

Ketoconazol es un antifúngico azólico autorizado en Colombia en tabletas orales y en champú.
El modelo TxGNN predice que podría ser efectivo para **acné**, pero la evidencia es limitada: **1 ensayo clínico** (formulación tópica, sin resultados) y **publicaciones mayormente indirectas**, sin estudios clínicos sólidos que respalden esta dirección.

<!-- review:begin co-lic-20261105-ketoconazole-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Ketoconazol es un antifúngico azólico autorizado en Colombia en tabletas orales y en champú, cuyos tres registros sanitarios están hoy cancelados." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-ketoconazole-1 -->

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Ketoconazol (el registro no detalla la indicación; solo menciona el nombre del principio activo) |
| Nueva Indicación Predicha | Acné |
| Puntaje de Predicción TxGNN | 0.9980 |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 18) |
| Número de Registros Sanitarios | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Ketoconazole (traducción no oficial): «El ketoconazol bloquea la síntesis de ergosterol, un componente clave de la membrana celular fúngica, mediante la inhibición de la enzima dependiente del citocromo P-450 lanosterol 14α-desmetilasa, responsable de la conversión del lanosterol en ergosterol en la membrana celular fúngica. Esto da lugar a una acumulación de precursores de esteroles metilados y a una depleción de ergosterol en la membrana celular, lo que debilita la estructura y la función de la membrana celular fúngica.» Texto original en inglés: "Ketoconazole blocks the synthesis of ergosterol, a key component of the fungal cell membrane, through the inhibition of cytochrome P-450 dependent enzyme lanosterol 14α-demethylase responsible for the conversion of lanosterol to ergosterol in the fungal cell membrane. This results in an accumulation of methylated sterol precursors and a depletion of ergosterol within the cell membrane thus weakening the structure and function of the fungal cell membrane." ([DailyMed: ketoconazole prescribing information, Bryant Ranch Prepack](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4baebcab-a237-42c0-9183-6f447a44e371), versión del 2025-11-18; consultado el 2026-11-19). Según la información conocida, el ketoconazol es un antifúngico azólico que inhibe la enzima fúngica CYP51 (lanosterol 14-alfa-demetilasa), y también tiene actividad antiinflamatoria.

Para el acné existen dos vías plausibles, ambas con evidencia indirecta. La primera: el ketoconazol suprime la levadura *Malassezia* (*Pityrosporum*), implicada en erupciones foliculares y acneiformes como la foliculitis por *Malassezia* y la pustulosis cefálica neonatal. Además, estudios de laboratorio indican que inhibe el crecimiento y la actividad de la lipasa de *Propionibacterium acnes*, una bacteria asociada al acné vulgar. La segunda: inhibe la enzima humana CYP17A1 y otras enzimas de la esteroidogénesis, lo que reduce la síntesis de andrógenos y, en teoría, la producción de sebo en acné hiperandrogénico (por ejemplo, en síndrome de ovario poliquístico).

Conviene no mezclar ambos mecanismos: la crema tópica y el efecto sistémico sobre la esteroidogénesis son exposiciones distintas. El puntaje de 0.9980 de TxGNN es una predicción computacional, no evidencia clínica. Además, el uso sistémico conlleva riesgos graves de hepatotoxicidad y supresión adrenal, lo que dificultaría justificarlo para el acné.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT07237763](https://clinicaltrials.gov/study/NCT07237763) | No aplica (NA) | Activo, sin reclutar | 52 | Ensayo aleatorizado que compara crema de ketoconazol al 2% con crema de adapaleno al 2% en acné leve comedoniano y papulopustular durante 12 semanas. Sin resultados disponibles; el comparador activo no permite aislar el efecto del ketoconazol frente a placebo. |

Este ensayo es solo una señal de interés clínico y no sustenta evidencia de nivel L1 o L2. Se recomienda verificar la indicación exacta, pues el título aparece truncado.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [12566804](https://pubmed.ncbi.nlm.nih.gov/12566804/) | 2003 | Revisión | Dermatology | Actualización del tratamiento sistémico del acné; antibióticos como tetraciclinas y macrólidos son de elección en el acné papulopustular. |
| [28111792](https://pubmed.ncbi.nlm.nih.gov/28111792/) | 2017 | Estudio de laboratorio | Microbiol Immunol | El ketoconazol inhibe la actividad de la lipasa de *P. acnes* y su crecimiento; podría ser alternativa ante la resistencia a antibióticos. |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | Estudio in vitro | Biol Pharm Bull | Actividad in vitro de antifúngicos azólicos contra *P. acnes* aislado de pacientes con acné vulgar. |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | Estudio clínico | Clin Exp Dermatol | Foliculitis por *Pityrosporum* (62 pacientes en Arabia Saudita), frecuentemente confundida con acné vulgar; se evaluaron ensayos terapéuticos. |
| [8629828](https://pubmed.ncbi.nlm.nih.gov/8629828/) | 1996 | Reporte de caso | Arch Dermatol | Asociación entre erupciones papulopustulares neonatales y la infección por *Malassezia furfur*. |
| [8255067](https://pubmed.ncbi.nlm.nih.gov/8255067/) | 1993 | Revisión | Keio J Med | *Pityrosporum ovale* como patógeno oportunista asociado a pitiriasis versicolor, foliculitis y dermatitis seborreica. |
| [19445767](https://pubmed.ncbi.nlm.nih.gov/19445767/) | 2009 | Revisión | BMJ Clin Evid | El síndrome de ovario poliquístico se asocia con hirsutismo, infertilidad y acné. |
| [8090657](https://pubmed.ncbi.nlm.nih.gov/8090657/) | 1993 | Revisión | Pol Tyg Lek | Tratamiento de manifestaciones hiperandrogénicas del SOP; reducción de acné y seborrea en 3 meses con terapia hormonal. |

La mayoría de estas publicaciones aportan respaldo indirecto (mecanismo, contexto o diagnóstico diferencial) y no demuestran eficacia clínica del ketoconazol en acné.

---

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 19900428 | DERMATREX® CREMA | CREMA TOPICA | DEXAMETASONA Y ANTIBIOTICOS | Vigente |
| 19902578 | SHAMPOO CON KETOCONAZOL 1 % | EMULSION (CHAMPOO) | KETOCONAZOL | Vigente |
| 19918847 | KETOCONAZOL TABLETAS 200 MG | TABLETA | KETOCONAZOL | Vigente |
| 19931135 | KETOMED® CHAMPU | EMULSION (CHAMPOO) | KETOCONAZOL | Vigente |
| 19937307 | KETOCONAZOLCREMA | CREMA TOPICA | KETOCONAZOL | Vigente |

Se muestran 5 de al menos 20 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes. Los datos de este informe solo incluyen parte de los registros.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

- **Contraindicaciones sugeridas por el grafo de conocimiento** (relaciones fármaco-enfermedad de TxGNN, no texto de prospecto): síndrome de QT largo (incluido el familiar), torsades de pointes, enfermedad hepática, enfermedad de la vesícula biliar, insuficiencia adrenocortical (enfermedad de Addison), atrofia cutánea, telangiectasia (incluida la telangiectasia hemorrágica hereditaria), enfermedad capilar, enfermedad vascular periférica (claudicación intermitente, enfermedad arterial periférica) y aclorhidria.
- **Interacciones farmacológicas**: se registran 658 interacciones. Entre las de nivel **mayor** figuran loperamida, triamcinolona y budesonida. Entre las de nivel moderado figuran famotidina, ranitidina, rabeprazol, omeprazol, hidrocortisona, dexametasona, betametasona, pioglitazona, alosetrón, aprepitant, atropina, hiosciamina, metescopolamina y bisacodilo. Con anfotericina B (incluido el complejo lipídico) la interacción es menor.
- **Riesgos del uso sistémico**: hepatotoxicidad y supresión adrenal, que dificultarían justificar su uso oral en acné.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya sobre todo en el puntaje computacional y en evidencia indirecta (laboratorio y contexto), con un solo ensayo pequeño de formulación tópica sin resultados. Además, el perfil de seguridad sistémico es desfavorable.

<!-- review:begin co-lic-20261105-ketoconazole-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, los tres registros colombianos están cancelados y el perfil de seguridad sistémico es desfavorable." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-ketoconazole-2 -->

**Para avanzar se necesita:**
- Resultados del ensayo NCT07237763 y, de ser posible, ensayos controlados con placebo de ketoconazol tópico en acné.
- Definir la vía de administración (tópica frente a sistémica) y verificar su compatibilidad con los productos disponibles.
- Obtener las advertencias y contraindicaciones del prospecto de INVIMA.
- Completar los datos del mecanismo de acción desde DrugBank.
- Aclarar la situación regulatoria en Colombia (el medicamento está comercializado y cuenta con al menos 18 registros vigentes) y evaluar si se requiere un nuevo registro.
- Evaluar el riesgo de hepatotoxicidad, supresión adrenal, prolongación del QT e interacciones antes de cualquier uso sistémico.

<!-- review:begin co-lic-20261112-ketoconazole-1 -->

> **Corrección de revisión (2026-11-12)**: Texto original: "3 registros vigentes" Corregido según los datos del INVIMA (Código Único de Medicamentos, datos al 2026-11-05): al menos 18 registros sanitarios vigentes (la lista de los datos está limitada a 20 registros). Las cifras actuales están en el Resumen rápido. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261112-ketoconazole-1 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "cuyos tres registros sanitarios están hoy cancelados" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "los tres registros colombianos están cancelados y" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-12 | Número de registros vigentes: 3 → al menos 18 | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: ketoconazole prescribing information, Bryant Ranch Prepack](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4baebcab-a237-42c0-9183-6f447a44e371) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

