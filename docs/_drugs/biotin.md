---
layout: default
title: Biotin
parent: Solo Predicción del Modelo (L5)
nav_order: 91
evidence_level: L5
indication_count: 2
---

# Biotin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Biotina: De Multivitaminas y Elementos Traza a Dispepsia

## Resumen en Una Frase

La biotina (vitamina B7) se comercializa en Colombia como componente de una preparación de multivitaminas y elementos traza de uso parenteral.
El modelo TxGNN predice que podría ser útil para la **dispepsia**, pero solo hay **2 ensayos clínicos** y **7 publicaciones** asociados, y ninguno evalúa la biotina para esta condición.
Por ahora la predicción se apoya únicamente en el modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Multivitaminas y elementos traza |
| Nueva Indicación Predicha | Dispepsia |
| Puntaje de Predicción TxGNN | 99.43% |
| Nivel de Evidencia | L5 (sin estudios directos; el paquete de datos indica L4, pero no aporta estudios preclínicos ni de mecanismo) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la biotina es cofactor de carboxilasas que participan en el metabolismo de ácidos grasos, glucosa y aminoácidos. En Colombia se usa como parte de una combinación de multivitaminas y elementos traza, es decir, como aporte nutricional.

No existe un mecanismo establecido que conecte la biotina con la dispepsia. Solo hay dos vías indirectas posibles: corregir una deficiencia que cause síntomas digestivos y modular la microbiota intestinal. Los datos disponibles no respaldan ninguna de las dos.

El puntaje de 99.43% proviene únicamente de la predicción del grafo de conocimiento y no equivale a evidencia clínica. Sin datos de mecanismo de acción no se puede contrastar la hipótesis. Hay una segunda predicción, gastroparesia (puntaje 99.42%), sin ensayos ni literatura asociados.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03360435](https://clinicaltrials.gov/study/NCT03360435) | N/A | Completado | 99 | Absorción de vitaminas transdérmicas en pacientes tras cirugía bariátrica. La biotina podría ser una de las vitaminas, pero la población y los desenlaces no son de dispepsia (relevancia indirecta, grado C). |
| [NCT05389813](https://clinicaltrials.gov/study/NCT05389813) | Fase 2/3 | Desconocido | 150 | Oxicodona vs. pregabalina como analgesia preventiva posoperatoria. No involucra biotina ni dispepsia; probable coincidencia espuria (grado C). |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [15863846](https://pubmed.ncbi.nlm.nih.gov/15863846/) | 2005 | Reporte de caso | J Dermatol | Deficiencia de biotina en un lactante alimentado solo con fórmula de aminoácidos, diagnosticado de neonato con dispepsia. Es una relación circunstancial, no un efecto terapéutico. |
| [25384804](https://pubmed.ncbi.nlm.nih.gov/25384804/) | 2014 | Estudio clínico abierto | Minerva Gastroenterol Dietol | Suplemento (alginato, calcio, piña, papaya, jengibre, α-galactosidasa, hinojo) en dispepsia funcional tras tratar *H. pylori*. No se verificó el diseño ni que contenga biotina. |
| [21695955](https://pubmed.ncbi.nlm.nih.gov/21695955/) | 2011 | Revisión | Eksp Klin Gastroenterol | Fructooligosacáridos y microbiota intestinal en pacientes con patología broncopulmonar; el suplemento estudiado incluye biotina entre otras vitaminas. No es dispepsia. |
| [25110039](https://pubmed.ncbi.nlm.nih.gov/25110039/) | 2014 | Observacional | Int J Mol Med | Células endocrinas del antro gástrico en síndrome de intestino irritable. Sin intervención con biotina. |
| [24891930](https://pubmed.ncbi.nlm.nih.gov/24891930/) | 2014 | Observacional | World J Gastrointest Endosc | Células endocrinas de la mucosa oxíntica en síndrome de intestino irritable. No relacionado con biotina. |
| [11304845](https://pubmed.ncbi.nlm.nih.gov/11304845/) | 2001 | Observacional | J Clin Pathol | Interleucina 10 en gastritis asociada a *H. pylori*. No relacionado con biotina. |
| [10354275](https://pubmed.ncbi.nlm.nih.gov/10354275/) | 1999 | Observacional | Kidney Int | Linfocitos T del intestino delgado en nefropatía por IgA. No relacionado. |

Ninguna publicación demuestra un beneficio de la biotina en la dispepsia.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 215439 | CERNEVIT® (CLINTEC PARENTERAL S.A.) | Polvo liofilizado para reconstituir a solución inyectable | Multivitaminas y elementos traza |

Se reportan 20 registros en total. Las cinco filas disponibles en los datos corresponden al mismo registro (215439), por lo que se muestra una sola vez.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene respaldo clínico ni mecanístico. Los dos ensayos son indirectos o no relacionados, y la literatura no evalúa la biotina en dispepsia. Además, aún no se han revisado la seguridad ni el mecanismo de acción.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA (advertencias y contraindicaciones), un vacío que bloquea el tamizaje de seguridad.
- Consultar el mecanismo de acción en DrugBank para evaluar el vínculo mecanístico.
- Buscar estudios que evalúen la biotina en síntomas digestivos, o deficiencia de biotina como causa de dispepsia.
- Evaluar la compatibilidad de vía de administración, ya que el único producto registrado es inyectable.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

