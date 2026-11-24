---
layout: default
title: Terconazole
parent: Solo Predicción del Modelo (L5)
nav_order: 617
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-24
monitor_inn: "terconazole"
predicted_indications: ["trichomonal vulvovaginitis", "vulvitis", "postmenopausal atrophic vaginitis", "herpetic vulvovaginitis", "ulceration of vulva", "vulvar neoplasm", "vaginal discharge", "bacterial vaginosis"]
description: "Terconazole: nueva indicación predicha, Vulvovaginitis tricomonásica (trichomonal vulvovaginitis) (nivel de evidencia L5). Indicación original: TERCONAZOL - DEXAMETASONA"
---

# Terconazole
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

## Terconazole: Vulvovaginitis tricomonásica (trichomonal vulvovaginitis)
{: .text-alpha }

## Resumen en Una Frase

Terconazol es un antifúngico triazólico de uso tópico vaginal, comercializado en Colombia en cremas vaginales.
El modelo TxGNN predice que podría ser efectivo para **vulvovaginitis tricomonásica (trichomonal vulvovaginitis)**,
pero actualmente **no hay ensayos clínicos** y solo hay **2 publicaciones** generales, sin datos específicos sobre esta enfermedad.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | TERCONAZOL - DEXAMETASONA; DEXAMETASONA Y ANTIBIOTICOS |
| Nueva Indicación Predicha | Vulvovaginitis tricomonásica (trichomonal vulvovaginitis) |
| Puntaje de Predicción TxGNN | 0.9986 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 3 de 3) |
| Número de Registros Sanitarios | 3 (vigentes: 3) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Terconazol es un antifúngico triazólico que inhibe la CYP51 fúngica (lanosterol 14-alfa-desmetilasa) y, con ello, la síntesis de ergosterol. Según las secciones «Mechanism of Action» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Terconazole (traducción no oficial): «El terconazol es un agente antifúngico. […] El terconazol inhibe la enzima citocromo P450 14α-desmetilasa, lo que conduce a la inhibición de la síntesis de ergosterol, un componente esencial de la membrana celular fúngica Actividad in vitro El terconazol presenta actividad fungicida in vitro frente a Candida albicans.» Texto original en inglés: "Terconazole is an antifungal agent. […] Terconazole inhibits the enzyme cytochrome P450 14α-demethylase which leads to inhibition of ergosterol synthesis, an essential component of the fungal cell membrane Activity in vitro Terconazole exhibits fungicidal activity in vitro against Candida albicans." ([DailyMed: Terconazole Vaginal Cream 0.8% (terconazole) prescribing information, E. Fougera & Co. a division of Fougera Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f59448bd-f730-46d2-a785-c2d6205579ff), versión del 2026-01-28; consultado el 2026-11-19).

*Trichomonas vaginalis* es un protozoo y este tipo de blanco dependiente de ergosterol no le aplica de la misma manera, por lo que el vínculo mecanístico es débil. El puntaje elevado probablemente refleja cercanía en la red de relaciones del modelo con cuadros vaginales infecciosos, más que un efecto antiprotozoario real.

Las dos publicaciones disponibles son revisiones generales, sin datos específicos sobre tricomonas. La predicción debe considerarse una hipótesis sin respaldo clínico.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10546257](https://pubmed.ncbi.nlm.nih.gov/10546257/) | 1999 | Revisión | The Nurse Practitioner | Revisión general de infecciones vaginales de origen bacteriano, fúngico y protozoario; no aporta datos de terconazol en esta enfermedad |
| [6617296](https://pubmed.ncbi.nlm.nih.gov/6617296/) | 1983 | Revisión | Chemotherapy | Describe terconazol como triazol de amplio espectro, activo in vitro frente a levaduras y hongos filamentosos; sin datos sobre protozoos |

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 20013336 | VAGICORT® CREMA VAGINAL | CREMA VAGINAL | TERCONAZOL - DEXAMETASONA | Vigente |
| 20135424 | TEREX-3 | CREMA VAGINAL | DEXAMETASONA Y ANTIBIOTICOS | Vigente |
| 20265420 | DECADRON T® | CREMA VAGINAL | TERCONAZOL - DEXAMETASONA | Vigente |

Se muestran los 3 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El puntaje del modelo es alto, pero no existen ensayos clínicos ni literatura específica, y el mecanismo antifúngico del fármaco no explica un efecto sobre un protozoo. La evidencia se limita a la predicción del modelo (L5).

**Para avanzar se necesita:**
- Estudios in vitro que evalúen la actividad de terconazol frente a *Trichomonas vaginalis*
- Datos detallados del mecanismo de acción
- Información de seguridad del prospecto (advertencias y contraindicaciones)
- Comparación con los tratamientos antiprotozoarios habituales antes de considerar cualquier ensayo clínico

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Terconazole Vaginal Cream 0.8% (terconazole) prescribing information, E. Fougera & Co. a division of Fougera Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f59448bd-f730-46d2-a785-c2d6205579ff) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

