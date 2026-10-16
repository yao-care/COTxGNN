---
layout: default
title: Tobramycin
parent: Evidencia Moderada (L3-L4)
nav_order: 629
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Tobramycin: nueva indicación predicha, Queratitis por exposición (nivel de evidencia L4). Indicación original: Dexametasona y antiinfecciosos (combinación oftálmica)"
---

# Tobramycin
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Tobramicina: De Antiinfecciosos Oftálmicos en Combinación a Queratitis por Exposición

## Resumen en Una Frase

La tobramicina es un antibiótico aminoglucósido que en Colombia se registró en productos oftálmicos, solos o combinados con dexametasona, para infecciones oculares.
El modelo TxGNN predice que podría ser efectiva para **queratitis por exposición**, pero actualmente hay **0 ensayos clínicos** y solo **8 publicaciones** de apoyo indirecto (sobre queratitis bacteriana y toxicidad corneal), por lo que la evidencia es muy débil.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dexametasona y antiinfecciosos (combinación oftálmica) |
| Nueva Indicación Predicha | Queratitis por exposición |
| Puntaje de Predicción TxGNN | 99.93% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 3 (0 vigentes, 3 cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, la tobramicina es un aminoglucósido con actividad contra bacterias Gram negativas y *Staphylococcus*, y se usa por vía tópica en la queratitis bacteriana y la conjuntivitis. Su eficacia en infecciones oculares superficiales es conocida.

La queratitis por exposición es un daño de la superficie corneal por cierre ocular insuficiente. Sobre ese epitelio dañado pueden aparecer infecciones bacterianas secundarias, de modo que la tobramicina podría servir de forma indirecta como profilaxis o tratamiento de la sobreinfección. El vínculo es plausible, pero indirecto: la literatura recuperada trata la queratitis bacteriana y no la queratitis por exposición en sí.

Hay además una señal de alerta: un estudio in vitro muestra toxicidad de los aminoglucósidos sobre el epitelio corneal. En una córnea ya comprometida, esto sería un problema de seguridad importante.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para queratitis por exposición.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [42842711](https://pubmed.ncbi.nlm.nih.gov/42842711/) | 2026 | Cohorte retrospectiva | Cornea | Compara características clínicas, sensibilidad antimicrobiana y desenlaces de queratitis por *S. aureus* resistente y sensible a meticilina |
| [2707046](https://pubmed.ncbi.nlm.nih.gov/2707046/) | 1989 | Estudio in vitro | Current Eye Research | Evalúa la citotoxicidad de neomicina, gentamicina, tobramicina y amikacina en cultivos de epitelio corneal de conejo |
| [11581057](https://pubmed.ncbi.nlm.nih.gov/11581057/) | 2001 | Reporte de caso | Ophthalmology | Queratitis por *Bacillus cereus* asociada al uso de lentes de contacto |
| [34987857](https://pubmed.ncbi.nlm.nih.gov/34987857/) | 2021 | Reporte de caso | Oxford Medical Case Reports | Queratitis por *Shewanella algae* multirresistente en un paciente que no podía cerrar los ojos |
| [12861116](https://pubmed.ncbi.nlm.nih.gov/12861116/) | 2003 | Reporte de caso | Eye & Contact Lens | Queratitis bilateral por SARM tras queratectomía fotorrefractiva |
| [17228760](https://pubmed.ncbi.nlm.nih.gov/17228760/) | 2006 | Estudio in vitro | Nippon Ganka Gakkai Zasshi | Concentración inhibitoria mínima y efecto postantibiótico de colirios sobre aislados de queratitis infecciosa en Japón |
| [42358321](https://pubmed.ncbi.nlm.nih.gov/42358321/) | 2026 | Estudio in vitro (veterinario) | Frontiers in Veterinary Science | Efecto de la fluorometolona sobre la sensibilidad antibiótica de patógenos oculares caninos |
| [14574976](https://pubmed.ncbi.nlm.nih.gov/14574976/) | 2003 | Reporte de caso | Yan Ke Xue Bao | Dellen corneal paracentral como signo raro de oftalmopatía de Graves |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20148323 | OPHTHABRACIN-D UNGUENTO (cancelado) | Ungüento oftálmico | Dexametasona y antiinfecciosos |
| 19983161 | TQ TOBRAOFTAL D® Suspensión oftálmica estéril (cancelado) | Suspensión oftálmica | Antibióticos en combinación con otros fármacos |
| 19929503 | TOBRACORT 0.3% (cancelado) | Suspensión oftálmica | Dexametasona y antiinfecciosos |

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (relaciones fármaco-enfermedad del modelo, no texto de prospecto): enfermedad renal, queratitis por herpes simple, glaucoma (incluido el de ángulo abierto) e hipertensión ocular, miastenia gravis y otras enfermedades de la unión neuromuscular, enfermedad de Parkinson, diabetes mellitus y cetoacidosis diabética, infecciones oculares virales y fúngicas, tuberculosis ocular, herpes zóster oftálmico, colitis por *Clostridium difficile*, enterocolitis necrosante perinatal e hipercalcemia, entre otras. Varias son relevantes para el uso oftálmico, sobre todo las infecciones virales o fúngicas del ojo y el glaucoma, que corresponden más a la dexametasona de las combinaciones.
- **Toxicidad corneal**: un estudio in vitro describe toxicidad de los aminoglucósidos sobre el epitelio corneal, lo que preocupa en una superficie ocular ya dañada.
- **Interacciones**: la única entrada recuperada es una interacción farmacológica con el receptor del gusto TAS2R20 (objetivo molecular, no una interacción clínicamente relevante). La literatura señala que con el uso sistémico debe vigilarse la nefrotoxicidad.

No se obtuvieron advertencias ni contraindicaciones del prospecto de INVIMA; consultar el prospecto para esa información.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto, pero no hay ensayos clínicos y la literatura no evalúa la tobramicina en queratitis por exposición. El mecanismo es solo indirecto (prevención de sobreinfección) y existe una señal de toxicidad sobre el epitelio corneal. Además, los tres registros sanitarios en Colombia están cancelados.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), pendiente y bloqueante para el tamizaje de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar estudios específicos de tobramicina en queratitis por exposición (por ejemplo, profilaxis de infección secundaria) y evaluar el balance entre beneficio antibacteriano y toxicidad epitelial.
- Evaluar la viabilidad comercial, dado que no hay productos vigentes en Colombia.

**Nota sobre otras predicciones:** entre las demás indicaciones predichas, la otitis externa tiene mayor respaldo (nivel L3, literatura microbiológica y de casos con tobramicina; marcada como pregunta de investigación). Debe cuidarse la ototoxicidad con perforación timpánica. El resto tiene evidencia nula o indirecta, o conflicto con el perfil de riesgo, como el síndrome urémico hemolítico asociado a infección.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

