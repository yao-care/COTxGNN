---
layout: default
title: Clarithromycin
parent: Solo Predicción del Modelo (L5)
nav_order: 162
evidence_level: L5
indication_count: 5
monitor_inn: "Clarithromycin"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "punctate epithelial keratoconjunctivitis", "blood group incompatibility"]
last_modified_at: 2026-11-24
description: "Clarithromycin: nueva indicación predicha, Síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome) (nivel de evidencia L5). Indicación original: CLARITROMICINA"
---

# Clarithromycin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Claritromicina: antibiótico macrólido → síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome)
{: .text-alpha }

## Resumen en Una Frase

Claritromicina es un antibiótico macrólido con registros sanitarios locales en Colombia.
El modelo TxGNN predice que podría ser efectivo para **síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | CLARITROMICINA |
| Nueva Indicación Predicha | Síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome) |
| Puntaje de Predicción TxGNN | 0,9935 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 18) |
| Número de Registros Sanitarios | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según las secciones «Mechanism of Action» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Clarithromycin (traducción no oficial): «La claritromicina es un fármaco antimicrobiano macrólido. […] La claritromicina ejerce su acción antibacteriana al unirse a la subunidad ribosómica 50S de las bacterias sensibles, lo que da lugar a la inhibición de la síntesis de proteínas.» Texto original en inglés: "Clarithromycin is a macrolide antimicrobial drug. […] Clarithromycin exerts its antibacterial action by binding to the 50S ribosomal subunit of susceptible bacteria resulting in inhibition of protein synthesis." ([DailyMed: clarithromycin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ba216276-b0bd-420a-9e0d-090bdfcc2460), versión del 2026-11-12; consultado el 2026-11-19). Según la información conocida, la claritromicina es un antibiótico macrólido con efectos inmunomoduladores, como la supresión de citocinas proinflamatorias.

La hiperviscosidad policlonal surge por un exceso de inmunoglobulinas, por ejemplo en enfermedades autoinmunes o infecciones crónicas. No existe evidencia de que la claritromicina modifique los niveles de inmunoglobulinas ni la viscosidad sérica.

Por ello no se identifica un vínculo mecanístico claro. El puntaje del modelo es muy alto (0,9935), pero proviene únicamente de una predicción basada en relaciones entre datos y no está respaldado por estudios reales.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 14446 | CLARITROMICINA 500 MG TABLETAS RECUBIERTAS | TABLETA RECUBIERTA | CLARITROMICINA | Vigente |
| 19901371 | CLARITROMICINA 500 MG TABLETAS RECUBIERTAS | TABLETA RECUBIERTA | CLARITROMICINA | Vigente |
| 19906258 | KLAMICINA® TABLETAS RECUBIERTAS 500 MG | TABLETA RECUBIERTA | CLARITROMICINA | Vigente |
| 19911016 | CIRIDAC ® 500 MG. TABLETAS | TABLETA | CLARITROMICINA | Vigente |
| 19915103 | CLARITROMICINA500MG | TABLETA RECUBIERTA | CLARITROMICINA | Vigente |

Se muestran 5 de al menos 20 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes. Los datos de este informe solo incluyen parte de los registros.

<!-- licenses:end -->

<!-- review:begin co-lic-20261124b-clarithromycin-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "Los datos locales de estos registros pueden estar incompletos (lista parcial)." Eliminado: advertía que la lista de registros podría ser parcial. La tabla de Información de Mercado en Colombia se genera a partir de los datos del INVIMA (Código Único de Medicamentos, datos al 2026-11-23) e indica cuántos registros muestra y que los datos de este informe solo incluyen parte de los registros. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261124b-clarithromycin-1 -->

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se consultaron 100 interacciones. Entre las de nivel mayor figuran abemaciclib, fentanilo y acalabrutinib. Entre las de nivel moderado figuran paclitaxel, tramadol, famotidina, formoterol, nifedipino, adenosina, etinilestradiol e hidrocortisona. Entre las de nivel menor figuran dolutegravir, zidovudina y loratadina.

No se dispone de texto de prospecto con advertencias ni contraindicaciones; consultar el prospecto para el resto de la información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni publicaciones sobre esta enfermedad, y no se identifica un mecanismo plausible que conecte la claritromicina con la hiperviscosidad policlonal. El puntaje alto del modelo no es suficiente por sí solo.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) de la claritromicina
- Evidencia preclínica o clínica que relacione el fármaco con los niveles de inmunoglobulinas o la viscosidad sérica
- Advertencias y contraindicaciones del prospecto de INVIMA
- Verificación del estado vigente de los registros sanitarios

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: clarithromycin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ba216276-b0bd-420a-9e0d-090bdfcc2460) |
| 2026-11-24 | Eliminado: "Los datos locales de estos registros pueden estar incompletos (lista parcial)." | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

