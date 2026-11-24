---
layout: default
title: Modafinil
parent: Solo Predicción del Modelo (L5)
nav_order: 452
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "MODAFINIL"
predicted_indications: ["insomnia (disease)"]
description: "Modafinil: nueva indicación predicha, insomnio (insomnia (disease)) (nivel de evidencia L5). Indicación original: MODAFINIL"
---

# Modafinil
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

## Modafinil: insomnio (insomnia (disease))
{: .text-alpha }

## Resumen en Una Frase

Modafinilo es un agente promotor de la vigilia, cuyo mecanismo de acción detallado no está disponible en los datos compilados para este informe.
El modelo TxGNN predice que podría ser efectivo para **insomnio (insomnia (disease))**, pero la evidencia es muy limitada: **2 ensayos clínicos** (uno terminado con solo 2 participantes y otro completado sin resultados publicados) y ninguna publicación que estudie directamente el insomnio. El nivel de evidencia es **L5**.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | MODAFINIL |
| Nueva Indicación Predicha | insomnio (insomnia (disease)) |
| Puntaje de Predicción TxGNN | 0.9985 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 2 de 2) |
| Número de Registros Sanitarios | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Modafinil (traducción no oficial): «Se desconoce el mecanismo o los mecanismos mediante los cuales el modafinilo promueve la vigilia. El modafinilo tiene acciones promotoras de la vigilia similares a las de los agentes simpaticomiméticos, incluidos la anfetamina y el metilfenidato, aunque el perfil farmacológico no es idéntico al de las aminas simpaticomiméticas.» Texto original en inglés: "The mechanism(s) through which modafinil promotes wakefulness is unknown. Modafinil has wake-promoting actions similar to sympathomimetic agents including amphetamine and methylphenidate, although the pharmacologic profile is not identical to that of the sympathomimetic amines." ([DailyMed: Provigil (modafinil) prescribing information, Apotex Corp](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0391f182-1958-9fef-a944-53b229ce99e7), versión del 2026-09-16; consultado el 2026-11-19). Modafinilo se conoce como un agente que promueve la vigilia, y en general se entiende que actúa mediante la inhibición del transportador de dopamina y la modulación de circuitos que favorecen la vigilia.

Este mecanismo es farmacológicamente opuesto al tratamiento del insomnio, ya que el fármaco favorece la vigilia y no el sueño. El puntaje alto del modelo (0,9985) probablemente refleja la cercanía en la red con trastornos del ciclo sueño-vigilia (narcolepsia, trastorno del sueño por trabajo en turnos, somnolencia en enfermedades neurológicas) más que un vínculo terapéutico real con el insomnio.

Por ello, la predicción debe interpretarse con mucha cautela: es mecanísticamente poco plausible y podría ser una clasificación errónea de una indicación relacionada con el ciclo sueño-vigilia.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00124384](https://clinicaltrials.gov/study/NCT00124384) | Fase 4 | Completado | 40 | Efectos de modafinilo, solo o con terapia cognitivo-conductual para el insomnio, sobre el funcionamiento diurno y la gravedad del insomnio en insomnio primario; sin resultados publicados |
| [NCT00626210](https://clinicaltrials.gov/study/NCT00626210) | Fase 4 | Terminado | 2 | Alteraciones del sueño/vigilia en adultos mayores; terminado con solo 2 participantes, sin evidencia interpretable |

## Evidencia de Literatura

Ninguna de las publicaciones identificadas estudia directamente el insomnio como efecto de modafinilo. Las más relevantes, de contexto, son:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [24312590](https://pubmed.ncbi.nlm.nih.gov/24312590/) | 2013 | Revisión sistemática/Metaanálisis | PloS one | Eficacia de modafinilo sobre la fatiga y la somnolencia diurna en trastornos neurológicos |
| [27010071](https://pubmed.ncbi.nlm.nih.gov/27010071/) | 2016 | Revisión sistemática/Metaanálisis | Parkinsonism & Related Disorders | Intervenciones farmacológicas para somnolencia diurna y trastornos del sueño en enfermedad de Parkinson |
| [18729534](https://pubmed.ncbi.nlm.nih.gov/18729534/) | 2008 | Revisión | Drugs | Revisión basada en evidencia de usos aprobados y en investigación de modafinilo |
| [21904092](https://pubmed.ncbi.nlm.nih.gov/21904092/) | 2011 | Revisión | Postgraduate Medicine | Trastorno por trabajo en turnos: somnolencia durante el trabajo y/o insomnio en el horario de descanso |
| [24138359](https://pubmed.ncbi.nlm.nih.gov/24138359/) | 2013 | Revisión | Medical Journal of Australia | Pérdida de sueño y alteración circadiana en trabajo por turnos |
| [17060310](https://pubmed.ncbi.nlm.nih.gov/17060310/) | 2006 | Serie de casos | Am J Hosp Palliat Care | Modafinilo reduce la fatiga en la enfermedad de Charcot-Marie-Tooth tipo 1A |

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 19968570 | VIGIA® 100 MG | CAPSULA BLANDA | MODAFINIL | Vigente |
| 19968571 | VIGIA ®200 MG | CAPSULA BLANDA | MODAFINIL | Vigente |

Se muestran los 2 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

<!-- review:begin co-lic-20261124b-modafinil-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "La lista de registros puede ser parcial." Eliminado: advertía que la lista de registros podría ser parcial. La tabla de Información de Mercado en Colombia se genera a partir de los datos del INVIMA (Código Único de Medicamentos, datos al 2026-11-23) e indica cuántos registros muestra del total. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261124b-modafinil-1 -->

## Consideraciones de Seguridad

- **Contraindicaciones en relaciones de condiciones clínicas registradas (no provienen del texto del prospecto):** hipertensión, insuficiencia hepática, trastornos de ansiedad, trastornos psicóticos y otros trastornos mentales, abuso/dependencia de sustancias, síndrome coronario agudo, infarto de miocardio, cardiopatía isquémica, enfermedad coronaria, prolapso de la válvula mitral y síndrome de taquicardia postural ortostática.
- **Interacciones farmacológicas (100 registradas; ejemplos principales):**
  - Moderadas: omeprazol, esomeprazol, rabeprazol, dexametasona, cisaprida, eliglustat, linagliptina.
  - Menores: hidrocortisona, pioglitazona, aprepitant, triamcinolona, betametasona, cimetidina, claritromicina, saxagliptina, dronabinol, clotrimazol, granisetrón, miconazol, naldemedina.

Consultar el prospecto para información de seguridad adicional.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay estudios que demuestren eficacia de modafinilo en el insomnio (el único ensayo directamente relacionado no tiene resultados publicados y el otro se terminó con 2 participantes), por lo que el nivel de evidencia es L5. Además, su mecanismo promotor de la vigilia es opuesto al objetivo terapéutico, y el puntaje alto del modelo probablemente refleja cercanía con otros trastornos del ciclo sueño-vigilia.

**Para avanzar se necesita:**
- Resultados publicados o ensayos controlados que evalúen modafinilo directamente en insomnio
- Datos detallados del mecanismo de acción
- Advertencias y contraindicaciones del prospecto de INVIMA
- Evaluación de seguridad cardiovascular y psiquiátrica, dadas las contraindicaciones registradas

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Provigil (modafinil) prescribing information, Apotex Corp](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0391f182-1958-9fef-a944-53b229ce99e7) |
| 2026-11-24 | Eliminado: "La lista de registros puede ser parcial." | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

