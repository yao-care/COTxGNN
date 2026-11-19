---
layout: default
title: Chloramphenicol
parent: Solo Predicción del Modelo (L5)
nav_order: 151
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-03
monitor_inn: "chloramphenicol"
predicted_indications: ["diffuse scleroderma", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "punctate epithelial keratoconjunctivitis"]
description: "Chloramphenicol: nueva indicación predicha, Esclerodermia difusa (diffuse scleroderma) (nivel de evidencia L5). Indicación original: CLORAMFENICOL"
---

# Chloramphenicol
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

## Chloramphenicol: Esclerodermia difusa (diffuse scleroderma)
{: .text-alpha }

## Resumen en Una Frase

Cloranfenicol es un antibiótico de uso sistémico que actúa contra bacterias, con registro sanitario vigente en Colombia.
El modelo TxGNN predice que podría ser efectivo para **esclerodermia difusa (diffuse scleroderma)**, pero actualmente no hay ensayos clínicos y solo existen **4 publicaciones** de investigación básica in vitro, sin evidencia de que el fármaco actúe sobre esta enfermedad.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | CLORAMFENICOL |
| Nueva Indicación Predicha | Esclerodermia difusa (diffuse scleroderma) |
| Puntaje de Predicción TxGNN | 0.9965 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según las secciones «Clinical Pharmacology» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Chloramphenicol (traducción no oficial): «El cloranfenicol es un antibiótico de amplio espectro aislado originalmente de Streptomyces venezuelae. Inhibe la síntesis de proteínas bacterianas al interferir en la transferencia de aminoácidos activados desde el ARN soluble a los ribosomas.» Texto original en inglés: "Chloramphenicol is a broad-spectrum antibiotic originally isolated from Streptomyces venezuelae. It inhibits bacterial protein synthesis by interfering with the transfer of activated amino acids from soluble RNA to ribosomes." ([DailyMed: chloramphenicol sodium succinate prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=aed29594-211d-49ef-813f-131975a8d0e3), versión del 2024-10-10; consultado el 2026-11-19). Según la información conocida, el cloranfenicol es un antibiótico que inhibe la síntesis de proteínas bacterianas, y su uso se ha centrado en infecciones bacterianas.

Las publicaciones recuperadas describen la transcripción del gen del procolágeno α1(I) y la señalización TGF-beta/Smad3 en fibroblastos de esclerodermia. No muestran que el cloranfenicol actúe sobre estas vías. Al parecer, la relación aparece por el uso del ensayo reportero CAT (cloranfenicol acetiltransferasa) en estudios de promotores, y no por un efecto terapéutico.

No hay evidencia clínica, y un antibiótico sistémico con toxicidad hematológica no tiene una justificación plausible para esta enfermedad. El puntaje alto probablemente es un artefacto de la predicción.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [8702443](https://pubmed.ncbi.nlm.nih.gov/8702443/) | 1996 | Investigación básica (in vitro) | Arthritis and Rheumatism | Regulación transcripcional del gen COL1A1 en fibroblastos dérmicos de esclerosis sistémica difusa; papel de secuencias intrónicas |
| [9811061](https://pubmed.ncbi.nlm.nih.gov/9811061/) | 1998 | Investigación básica (in vitro) | Arthritis and Rheumatism | Elementos del promotor de COL1A1 implicados en su expresión aumentada en esclerosis sistémica |
| [11229480](https://pubmed.ncbi.nlm.nih.gov/11229480/) | 2001 | Investigación básica (in vitro) | Arthritis and Rheumatism | El bloqueo de la señal de TGF-beta evita el aumento de síntesis de colágeno en fibroblastos de esclerodermia |
| [16319104](https://pubmed.ncbi.nlm.nih.gov/16319104/) | 2006 | Investigación básica (in vitro) | Rheumatology (Oxford) | Smad3 fosforilado de forma constitutiva interactúa con Sp1 y p300 en fibroblastos de esclerodermia |

Ninguno de estos estudios evalúa el cloranfenicol como tratamiento.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19987544 | CLORAFENICOL 250 MG | Cápsula dura | CLORAMFENICOL |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 478 interacciones en total. Entre las de nivel mayor figuran cisaprida y naloxegol. Entre las de nivel moderado figuran aprepitant, metronidazol, budesonida, hierro, rosuvastatina, simvastatina y varias sulfonilureas (clorpropamida, glimepirida, glipizida, glibenclamida).

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el puntaje del modelo. No hay ensayos clínicos y la literatura es de investigación básica in vitro, donde el cloranfenicol aparece probablemente como herramienta de laboratorio (ensayo CAT). Además, su toxicidad hematológica es una preocupación importante en una enfermedad crónica.

**Para avanzar se necesita:**
- Datos del mecanismo de acción que justifiquen una relación con la fibrosis o la señalización TGF-beta
- Estudios preclínicos que muestren un efecto del fármaco en modelos de esclerodermia
- Revisión del prospecto del INVIMA para advertencias y contraindicaciones
- Evaluación de la relación riesgo-beneficio frente a la toxicidad hematológica antes de cualquier estudio clínico

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: chloramphenicol sodium succinate prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=aed29594-211d-49ef-813f-131975a8d0e3) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

