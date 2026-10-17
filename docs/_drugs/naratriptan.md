---
layout: default
title: Naratriptan
parent: Evidencia Moderada (L3-L4)
nav_order: 462
evidence_level: L3
indication_count: 3
last_modified_at: 2026-10-14
description: "Naratriptan: nueva indicación predicha, Migraña con aura del tronco encefálico (nivel de evidencia L3). Indicación original: NARATRIPTAN"
monitor_inn: "naratriptan"
predicted_indications: ["atrophoderma vermiculata", "ulerythema ophryogenesis"]
---

# Naratriptan
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **3** 
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

# Naratriptán: De Migraña (indicación general) a Migraña con Aura del Tronco Encefálico

## Resumen en Una Frase

Naratriptán es un agonista selectivo de los receptores 5-HT1B/1D, originalmente registrado en Colombia como tratamiento de la migraña (el registro sanitario lista únicamente el nombre del principio activo).
El modelo TxGNN predice que podría ser efectivo para **migraña con aura del tronco encefálico**, pero no hay **ningún ensayo clínico** registrado para esta indicación y las **20 publicaciones** recopiladas tratan sobre la migraña en general, no sobre este subtipo específico.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | NARATRIPTAN (el registro no detalla el texto de la indicación; corresponde al tratamiento de la migraña) |
| Nueva Indicación Predicha | Migraña con aura del tronco encefálico |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción de DrugBank. Según la información conocida, naratriptán es un agonista selectivo de los receptores 5-HT1B/1D. Su acción abarca la vasoconstricción craneal, la inhibición de la liberación de neuropéptidos trigeminales (como CGRP) y la reducción de la transmisión nociceptiva trigeminovascular. Estos mecanismos son directamente relevantes para la fisiopatología de la migraña, incluidos los subtipos con aura.

La nueva indicación predicha pertenece a la misma área terapéutica que la original. Por ello, esto se interpreta mejor como un **refinamiento de la indicación** dentro de la migraña y no como un reposicionamiento en sentido estricto. El puntaje tan alto de TxGNN es coherente con esa superposición.

Hay una salvedad importante: la migraña con aura del tronco encefálico es un subtipo raro. Históricamente, los triptanes se han usado con cautela en auras que involucran síntomas del tronco encefálico o hemipléjicos, por preocupaciones vasculares teóricas. La literatura disponible aborda la migraña en general (guías de tratamiento agudo, comparación con sumatriptán, prevención en el pródromo, migraña menstrual), no este subtipo en particular.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Se priorizaron los ensayos aleatorizados, seguidos de las revisiones. Ninguna publicación estudia específicamente la migraña con aura del tronco encefálico.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10972634](https://pubmed.ncbi.nlm.nih.gov/10972634/) | 2000 | ECA | Clinical Therapeutics | Comparación doble ciego cruzada de naratriptán y sumatriptán en pacientes con migraña propensa a recurrencia |
| [10961768](https://pubmed.ncbi.nlm.nih.gov/10961768/) | 2000 | ECA | Cephalalgia | Naratriptán administrado durante el pródromo para prevenir la cefalea migrañosa |
| [11264684](https://pubmed.ncbi.nlm.nih.gov/11264684/) | 2001 | ECA (controlado con placebo) | Headache | Naratriptán 1 mg y 2.5 mg dos veces al día como profilaxis a corto plazo de la migraña asociada a la menstruación |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Revisión | Headache | Evaluación de la Sociedad Americana de Cefalea sobre la evidencia de las terapias farmacológicas para el tratamiento agudo de la migraña |
| [25841032](https://pubmed.ncbi.nlm.nih.gov/25841032/) | 2015 | Cohorte | Neurology | Menor eficacia de sumatriptán en migraña con aura frente a migraña sin aura |
| [14511276](https://pubmed.ncbi.nlm.nih.gov/14511276/) | 2003 | Revisión | Headache | Manejo de la migraña intratable con naratriptán |
| [16268666](https://pubmed.ncbi.nlm.nih.gov/16268666/) | 2005 | Revisión | CNS Drugs | Uso de triptanes en el manejo de la migraña menstrual |
| [25100506](https://pubmed.ncbi.nlm.nih.gov/25100506/) | 2014 | Revisión | Expert Opinion on Pharmacotherapy | Actualización sobre causas hormonales, profilaxis y tratamiento de la migraña menstrual |
| [15926020](https://pubmed.ncbi.nlm.nih.gov/15926020/) | 2005 | Estudio piloto abierto | Neurological Sciences | Naratriptán como profilaxis a corto plazo de la migraña menstrual pura |
| [23877022](https://pubmed.ncbi.nlm.nih.gov/23877022/) | 2014 | Reporte de caso | Brain & Development | Naratriptán mejoró cefaleas tipo migraña intratables en un paciente con síndrome de Sturge-Weber, con lamotrigina como profilaxis de aura visual |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 219084 (cancelado) | NARAMIG TABLETAS 2.5 MG | Tableta recubierta | NARATRIPTAN |

El único registro (GlaxoSmithKline Colombia S.A.) está cancelado, por lo que actualmente no hay productos vigentes con este principio activo en el registro consultado.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad de TxGNN/PrimeKG, no texto del prospecto):
  - Cardiovasculares: hipertensión, enfermedad coronaria, infarto de miocardio, isquemia miocárdica, angina de Prinzmetal, trombosis coronaria.
  - Cerebrovasculares: accidente cerebrovascular, infarto cerebral, ataque isquémico transitorio, insuficiencia vertebrobasilar.
  - Vasculares periféricos: enfermedad vascular periférica, enfermedad arterial periférica, claudicación intermitente.
  - Otras: insuficiencia hepática, diabetes mellitus, cetoacidosis diabética, obesidad, hemoglobinopatía.
  - Neurológicas: **migraña hemipléjica familiar o esporádica**, relevante por su cercanía con el subtipo de tronco encefálico predicho.
- **Interacciones farmacológicas** (39 registradas; ejemplos principales):
  - Gravedad **mayor**: lorcaserina, dolasetrón, palonosetrón, dexfenfluramina, fenfluramina, granisetrón, ondansetrón, sibutramina y azul de metileno (principalmente por riesgo de efectos serotoninérgicos).
  - Gravedad **moderada**: morfina (incluida la liposomal).
  - Gravedad **no clasificada**: lansoprazol, pantoprazol, omeprazol, prednisona, ranitidina, claritromicina, bupropión, budesonida y prometazina.

Para advertencias y contraindicaciones del texto oficial, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El mecanismo es plausible y el puntaje del modelo es muy alto, pero no existe evidencia específica para migraña con aura del tronco encefálico, y los triptanes se usan con cautela en auras con síntomas de tronco encefálico o hemipléjicos. Además, el único registro sanitario en Colombia está cancelado y la información del prospecto no está disponible.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), pues este vacío bloquea el tamizaje de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Revisar la literatura específica sobre triptanes en migraña con aura del tronco encefálico y su seguridad vascular.
- Evaluar con expertos en cefaleas si la indicación aporta valor frente al uso actual en migraña.
- Aclarar la situación regulatoria local, dado que no hay registro vigente.

**Nota sobre las otras predicciones:** *atrofodermia vermiculada* (99.74%) y *uleritema ofriógenes* (99.47%) no tienen ensayos clínicos ni literatura, y no se identificó un vínculo mecanístico plausible. Se trata de predicciones del modelo (nivel L5, decisión Hold), probablemente artefactos de proximidad en el grafo de conocimiento.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

