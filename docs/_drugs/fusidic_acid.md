---
layout: default
title: Fusidic Acid
parent: Solo Predicción del Modelo (L5)
nav_order: 305
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-25
description: "Fusidic Acid: nueva indicación predicha, Queratitis por exposición (nivel de evidencia L5). Indicación original: Ácido fusídico (crema tópica)"
monitor_inn: "fusidic acid"
predicted_indications: ["exposure keratitis", "non-human animal disease", "otitis externa", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "parasitic eyelid infestation"]
---

# Fusidic Acid
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Ácido fusídico: De Infecciones Cutáneas (Ácido Fusídico Tópico) a Queratitis por Exposición
{: .text-alpha }

## Resumen en Una Frase

El ácido fusídico es un antibiótico tópico, registrado en Colombia en crema al 2 % (sola o combinada con hidrocortisona).
El modelo TxGNN predice que podría ser efectivo para **queratitis por exposición**,
pero actualmente no hay ensayos clínicos y solo hay **1 publicación** (una serie de casos sobre infecciones oculares por *Tsukamurella*, que no estudia el ácido fusídico) vinculada a esta predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Ácido fusídico (crema tópica) |
| Nueva Indicación Predicha | Queratitis por exposición |
| Puntaje de Predicción TxGNN | 0.9995 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 13 de 19) |
| Número de Registros Sanitarios | 19 (vigentes: 13) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según ChEMBL (EMBL-EBI), el mecanismo de acción registrado para Fusidic Acid es (traducción no oficial): «Inhibidor del factor de elongación G». Texto original en inglés: "Elongation factor G inhibitor" ([ChEMBL CHEMBL374975 (fusidic acid): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL374975), CC BY-SA 3.0; consultado el 2026-11-19). Según el conocimiento general, el ácido fusídico inhibe la síntesis proteica bacteriana al bloquear el factor de elongación G (EF-G), lo que le da actividad contra bacterias Gram-positivas como *Staphylococcus*.

La relación con la queratitis por exposición es **indirecta**. Esta enfermedad es principalmente un trastorno mecánico o por desecación de la córnea, no infeccioso. El ácido fusídico podría ayudar, a lo sumo, en una infección bacteriana secundaria de una córnea expuesta.

La única publicación vinculada es una serie de casos de infecciones oculares por *Tsukamurella*, que no evalúa el ácido fusídico. Por ello, la puntuación proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31246677](https://pubmed.ncbi.nlm.nih.gov/31246677/) | 2019 | Serie de casos | Cornea | Describe las manifestaciones oftálmicas de infecciones por *Tsukamurella* (espectro clínico, factores de riesgo, tratamiento y desenlace) y el primer reporte de infección de implante ocular tras enucleación. No evalúa ácido fusídico. |

---

## Información de Mercado en Colombia

Hay registros sanitarios vigentes; el medicamento está comercializado.

<!-- review:begin co-lic-20261112-fusidic_acid-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "Hay 7 registros sanitarios vigentes" Corregido: el número de registros sanitarios escrito en el texto no coincidía con los datos del INVIMA (Código Único de Medicamentos, datos al 2026-11-23); el texto ya no indica una cifra fija. Las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261112-fusidic_acid-1 -->

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 11697 | ACIDO FUSIDICO CREMA 2% | CREMA TOPICA | FUSIDICO ACIDO | Vigente |
| 19939301 | TOPISEPT® | CREMA TOPICA | FUSIDICO ACIDO | Vigente |
| 20005814 | ACIDO FUSÍDICO 2% CREMA | CREMA TOPICA | FUSIDICO ACIDO | Vigente |
| 20047268 | FUCIFAR 2% CREMA | CREMA TOPICA | FUSIDICO ACIDO | Vigente |
| 20054634 | ACIDO FUSIDICO 2 % CREMA | CREMA TOPICA | FUSIDICO ACIDO | Vigente |

Se muestran 5 de 19 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

<!-- review:begin co-lic-20261124b-fusidic_acid-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "*Se listan 5 de los 7 registros (los otros dos corresponden a TOPISEPT® y FUCIDIN® H CREMA, este último combinado con hidrocortisona).*" Eliminado: describía la tabla de registros anterior (número de filas, un solo titular o fabricante, o registros que no se mostraban), reemplazada por la tabla generada a partir de los datos del INVIMA (Código Único de Medicamentos, datos al 2026-11-23). Los registros, titulares y estados actuales están en la tabla de Información de Mercado en Colombia y en el Resumen rápido. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261124b-fusidic_acid-1 -->

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** el grafo asocia el fármaco con contraindicaciones en enfermedades hepáticas y renales (insuficiencia hepática, enfermedad renal), oculares (glaucoma, glaucoma de ángulo abierto, hipertensión ocular, queratitis por herpes simple, conjuntivitis, infecciones oculares), gastrointestinales (colitis, colitis por *Clostridium difficile*), cardiovasculares (fibrilación auricular, bloqueo auriculoventricular, síndrome de Wolff-Parkinson-White, síndrome de Adams-Stokes), metabólicas (diabetes mellitus, cetoacidosis diabética, hipercalcemia, deficiencia de potasio) y neuromusculares (miastenia gravis, insuficiencia respiratoria), entre otras. Estas relaciones son orientativas y deben verificarse con fuentes oficiales, ya que parte de ellas probablemente reflejan otros fármacos o clases terapéuticas.
- **Relevancia para la indicación propuesta:** varias contraindicaciones oculares del grafo (glaucoma, infecciones oculares, conjuntivitis) coinciden con el ámbito de uso predicho, por lo que requieren revisión cuidadosa.

Consultar el prospecto para información de advertencias, contraindicaciones e interacciones farmacológicas.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos y la única publicación vinculada no evalúa el ácido fusídico. El mecanismo es solo indirectamente plausible, y hay registros sanitarios vigentes en Colombia.

<!-- review:begin co-lic-20261112-fusidic_acid-2 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "hay 7 registros sanitarios vigentes" Corregido: el número de registros sanitarios escrito en el texto no coincidía con los datos del INVIMA (Código Único de Medicamentos, datos al 2026-11-23); el texto ya no indica una cifra fija. Las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261112-fusidic_acid-2 -->

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones) para completar el tamizaje de seguridad.
- Confirmar el mecanismo de acción en DrugBank.
- Buscar evidencia clínica o preclínica del ácido fusídico en infecciones de la superficie ocular o en queratitis por exposición con sobreinfección.
- Evaluar la viabilidad de una formulación oftálmica y la situación regulatoria.
- Como alternativa, priorizar la indicación de **otitis externa** (puntaje 0.9984, L4, plausibilidad microbiológica por *S. aureus*), aunque la literatura es mayormente veterinaria y no ofrece datos de eficacia clínica en humanos.

<!-- review:begin co-lic-20261105-fusidic_acid-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Evaluar la viabilidad de una formulación oftálmica y la situación regulatoria, dado que no hay registros vigentes." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Las cifras actuales de registros sanitarios están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-fusidic_acid-1 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "dado que no hay registros vigentes" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-24 | Número de registros sanitarios corregido (sin cifra fija; ver Resumen rápido) | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-24 | Número de registros sanitarios corregido (sin cifra fija; ver Resumen rápido) | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente (revisado el 2026-11-20; la versión anterior se guarda en el registro) | [ChEMBL CHEMBL374975 (fusidic acid): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL374975) |
| 2026-11-24 | Eliminado: "Se listan 5 de los 7 registros…" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

