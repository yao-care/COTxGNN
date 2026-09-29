---
layout: default
title: Prednisolone
parent: Solo Predicción del Modelo (L5)
nav_order: 331
evidence_level: L5
indication_count: 10
---

# Prednisolone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Prednisolona: De Antiinflamatorio e Inmunosupresor Sistémico a Alopecia Areata

## Resumen en Una Frase

La prednisolona es un glucocorticoide sintético usado como antiinflamatorio e inmunosupresor en asma, colitis ulcerosa, artritis reumatoide y lupus, entre otras enfermedades inflamatorias.
El modelo TxGNN predice que podría ser efectiva para **alopecia areata**.
La respaldan **18 ensayos clínicos registrados** (ninguno prueba prednisolona directamente en esta indicación) y **20 publicaciones**, entre ellas un ensayo aleatorizado controlado con placebo de prednisolona oral en pulsos.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | El texto del registro sanitario solo dice "PREDNISOLONA" (nombre del principio activo, sin indicación). Uso clínico según farmacología: antiinflamatorio e inmunosupresor en enfermedades inflamatorias |
| Nueva Indicación Predicha | Alopecia areata |
| Puntaje de Predicción TxGNN | 99.99% (posición 230) |
| Nivel de Evidencia | L2 (un ECA pequeño, sin fase declarada, tratado como equivalente a Fase 2) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos detallados sobre el mecanismo de acción en el campo específico del Evidence Pack. Los datos farmacológicos sí muestran que la prednisolona actúa sobre el **receptor de glucocorticoides (NR3C1)** y el **receptor de mineralocorticoides (NR3C2)**. Como agonista glucocorticoide, suprime la inflamación y la respuesta inmunitaria.

La alopecia areata es una enfermedad autoinmune en la que los linfocitos T atacan el folículo piloso. El efecto inmunosupresor de los glucocorticoides es, por tanto, un vínculo mecanístico directo con la enfermedad. Un estudio publicado sobre corticoides orales en pulsos propone además que reducen el factor de necrosis tumoral alfa (TNF-α), una citoquina implicada en la alopecia areata (PMID 30294905).

Hay límites importantes. La enfermedad suele recaer al suspender el tratamiento, y el uso prolongado de esteroides acumula toxicidad. Los inhibidores de JAK ya cuentan con datos de Fase 3. La prednisolona queda mejor posicionada como terapia de ciclo corto o en pulsos, con vigilancia de recaídas y eventos adversos.

---

## Evidencia de Ensayos Clínicos

De los 18 ensayos registrados, solo 3 se relacionan con alopecia areata o con corticoides en esta condición. Los otros 15 son de lupus eritematoso sistémico, cáncer de próstata y cefalea, y no aportan evidencia sobre prednisolona en alopecia. Por eso no se listan.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01167946](https://clinicaltrials.gov/study/NCT01167946) | Fase 4 | Completado | 42 | Metilprednisolona oral en mega-pulsos para alopecia areata grave resistente al tratamiento. Es un corticoide sistémico cercano, no prednisolona; evidencia de apoyo de clase |
| [NCT07101471](https://clinicaltrials.gov/study/NCT07101471) | N/A (observacional) | Completado | 296 | Seguridad y efectividad de tofacitinib en alopecia, con o sin prednisolona adyuvante. Sin datos propios de prednisolona |
| [NCT01017510](https://clinicaltrials.gov/study/NCT01017510) | N/A | Desconocido | 20 | Compara dos técnicas de inyección intralesional de esteroide (Dermojet frente a jeringa) en alopecia areata. Sin relevancia asignada |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [15692475](https://pubmed.ncbi.nlm.nih.gov/15692475/) | 2005 | ECA | J Am Acad Dermatol | Terapia oral con prednisolona en pulsos controlada con placebo en alopecia areata. El resumen disponible no reporta resultados |
| [37870096](https://pubmed.ncbi.nlm.nih.gov/37870096/) | 2023 | Metaanálisis en red (Cochrane) | Cochrane Database Syst Rev | Compara tratamientos para alopecia areata: inmunosupresores, estimulantes del crecimiento e inmunoterapia de contacto |
| [30191561](https://pubmed.ncbi.nlm.nih.gov/30191561/) | 2019 | Revisión sistemática | Australas J Dermatol | Evalúa la evidencia de los tratamientos sistémicos en alopecia areata, totalis y universalis. La eficacia es variable según el tratamiento |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Revisión | Dermatol Pract Concept | Revisa eficacia, tasas de recaída, efectos adversos y factores pronósticos de la terapia corticoide en pulsos |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Revisión | Pediatr Dermatol | Regímenes de corticoides en pulsos en niños con alopecia areata. Las dosis no están bien establecidas |
| [21572877](https://pubmed.ncbi.nlm.nih.gov/21572877/) | 2009 | Estudio clínico | Dermato-endocrinology | Prednisolona en pulsos de dosis media. Parece eficaz en etapas tempranas, pero los efectos adversos pueden llevar a suspenderla |
| [35986630](https://pubmed.ncbi.nlm.nih.gov/35986630/) | 2022 | Cohorte retrospectiva | Dermatol Ther | 26 pacientes con alopecia areata extensa. Compara metilprednisolona sola con metilprednisolona más metotrexato |
| [32779249](https://pubmed.ncbi.nlm.nih.gov/32779249/) | 2020 | Estudio retrospectivo | J Eur Acad Dermatol Venereol | Tasas de continuación de azatioprina, metotrexato y ciclosporina como ahorradores de esteroides en 138 pacientes con alopecia areata crónica |
| [28140540](https://pubmed.ncbi.nlm.nih.gov/28140540/) | 2017 | Estudio clínico | J Dtsch Dermatol Ges | Corticoides sistémicos secuenciales (dosis alta y luego baja) en alopecia areata infantil grave. Las recaídas tras suspender son inevitables |
| [30294905](https://pubmed.ncbi.nlm.nih.gov/30294905/) | 2019 | Estudio de mecanismo | J Cosmet Dermatol | Cambios en TNF-α sérico y tisular como posible mecanismo de los esteroides orales en pulsos |

---

## Información de Mercado en Colombia

El Evidence Pack lista 20 registros. Aquí se muestran los registros únicos de la muestra, porque el pack repite las mismas filas.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20009756 | PREDNIOFTAL F® | Suspensión oftálmica | Solo indica "Prednisolona" (sin texto de indicación) |
| 19997234 | DIETYSOLONE PLUS SUSPENSIÓN OFTÁLMICA | Suspensión oftálmica | Solo indica "Fenilefrina combinaciones" (sin texto de indicación) |

Los productos de la muestra son oftálmicos. También existe la forma oral (tableta), que es la relevante para pulsos sistémicos en alopecia areata.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Según el análisis del Evidence Pack, el principal riesgo en esta indicación es la toxicidad acumulada por esteroides con uso prolongado y la recaída al suspender.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un ECA controlado con placebo de prednisolona oral en pulsos en alopecia areata, además de revisiones sistemáticas y un ensayo de Fase 4 con un corticoide cercano. Ese ECA es pequeño y sin fase declarada, y los inhibidores de JAK tienen datos más sólidos, por lo que se recomienda avanzar con condiciones.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones), que hoy es un vacío de datos bloqueante.
- Confirmar el mecanismo de acción en DrugBank.
- Confirmar la compatibilidad de vía y forma (tableta oral) para regímenes de pulso en Colombia.
- Definir un esquema de ciclo corto o pulsos, con monitoreo de recaídas y eventos adversos.
- Comparar con los inhibidores de JAK como alternativa de referencia.

**Nota sobre otras predicciones:** el síndrome nefrótico idiopático sensible a esteroides (L1) es un uso ya establecido, no un reposicionamiento nuevo. Las demás indicaciones predichas (mucinosis folicular, efluvio telógeno, foliculitis decalvante y otras) quedan en Hold o Research Question por evidencia insuficiente.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

