---
layout: default
title: Fusidic Acid
parent: Solo Predicción del Modelo (L5)
nav_order: 305
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-31
description: "Fusidic Acid: nueva indicación predicha, Queratitis por exposición (nivel de evidencia L4). Indicación original: Ácido fusídico (crema tópica)"
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
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 7) |
| Número de Registros Sanitarios | al menos 7 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según el conocimiento general, el ácido fusídico inhibe la síntesis proteica bacteriana al bloquear el factor de elongación G (EF-G), lo que le da actividad contra bacterias Gram-positivas como *Staphylococcus*.

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

Hay 7 registros sanitarios vigentes; el medicamento está comercializado.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20047268 | FUCIFAR 2% CREMA | Crema tópica | Ácido fusídico |
| 11697 | ÁCIDO FUSÍDICO CREMA 2% | Crema tópica | Ácido fusídico |
| 20054634 | ÁCIDO FUSÍDICO 2 % CREMA | Crema tópica | Ácido fusídico |
| 20066035 | ÁCIDO FUSÍDICO 2% CREMA | Crema tópica | Ácido fusídico |
| 20139241 | FUCILIX® CREMA | Crema tópica | Ácido fusídico |

*Se listan 5 de los 7 registros (los otros dos corresponden a TOPISEPT® y FUCIDIN® H CREMA, este último combinado con hidrocortisona).*

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** el grafo asocia el fármaco con contraindicaciones en enfermedades hepáticas y renales (insuficiencia hepática, enfermedad renal), oculares (glaucoma, glaucoma de ángulo abierto, hipertensión ocular, queratitis por herpes simple, conjuntivitis, infecciones oculares), gastrointestinales (colitis, colitis por *Clostridium difficile*), cardiovasculares (fibrilación auricular, bloqueo auriculoventricular, síndrome de Wolff-Parkinson-White, síndrome de Adams-Stokes), metabólicas (diabetes mellitus, cetoacidosis diabética, hipercalcemia, deficiencia de potasio) y neuromusculares (miastenia gravis, insuficiencia respiratoria), entre otras. Estas relaciones son orientativas y deben verificarse con fuentes oficiales, ya que parte de ellas probablemente reflejan otros fármacos o clases terapéuticas.
- **Relevancia para la indicación propuesta:** varias contraindicaciones oculares del grafo (glaucoma, infecciones oculares, conjuntivitis) coinciden con el ámbito de uso predicho, por lo que requieren revisión cuidadosa.

Consultar el prospecto para información de advertencias, contraindicaciones e interacciones farmacológicas.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos y la única publicación vinculada no evalúa el ácido fusídico. El mecanismo es solo indirectamente plausible, y hay 7 registros sanitarios vigentes en Colombia.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones) para completar el tamizaje de seguridad.
- Confirmar el mecanismo de acción en DrugBank.
- Buscar evidencia clínica o preclínica del ácido fusídico en infecciones de la superficie ocular o en queratitis por exposición con sobreinfección.
- Evaluar la viabilidad de una formulación oftálmica y la situación regulatoria, dado que no hay registros vigentes.
- Como alternativa, priorizar la indicación de **otitis externa** (puntaje 0.9984, L4, plausibilidad microbiológica por *S. aureus*), aunque la literatura es mayormente veterinaria y no ofrece datos de eficacia clínica en humanos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

