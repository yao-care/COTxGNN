---
layout: default
title: Biotin
parent: Solo Predicción del Modelo (L5)
nav_order: 107
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Biotin: nueva indicación predicha, Dispepsia (nivel de evidencia L5). Indicación original: Multivitaminas y elementos traza"
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

La biotina (vitamina B7) se registró en Colombia como parte de una preparación multivitamínica inyectable (CERNEVIT®), con indicación de "multivitaminas y elementos traza".
El modelo TxGNN predice que podría ser efectiva para **dispepsia**, pero hasta ahora **no hay ensayos clínicos** y solo **6 publicaciones**, todas de relevancia indirecta o baja, que respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Multivitaminas y elementos traza |
| Nueva Indicación Predicha | Dispepsia |
| Puntaje de Predicción TxGNN | 99.43% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la biotina es un cofactor de carboxilasas que participan en el metabolismo de carbohidratos, ácidos grasos y aminoácidos, y su eficacia como suplemento vitamínico en la corrección de deficiencias es conocida.

La relación con la dispepsia es débil e indirecta. La deficiencia de biotina puede causar síntomas gastrointestinales como náuseas y anorexia, por lo que cualquier beneficio probablemente sería la corrección de una deficiencia y no un efecto terapéutico directo sobre la dispepsia.

El puntaje del modelo es muy alto (0.994), pero se basa en la estructura del grafo de conocimiento. Los datos compilados no sustentan una vía biológica concreta que conecte la biotina con la dispepsia. Esta predicción debe considerarse una hipótesis sin validar.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [15863846](https://pubmed.ncbi.nlm.nih.gov/15863846/) | 2005 | Reporte de caso | The Journal of Dermatology | Deficiencia de biotina en un lactante de 5 meses alimentado solo con fórmula de aminoácidos, con diagnóstico neonatal de dispepsia; presentó alopecia y dermatitis, con biotina sérica y urinaria bajas |
| [21695955](https://pubmed.ncbi.nlm.nih.gov/21695955/) | 2011 | Revisión/Otro | Eksperimental'naia i klinicheskaia gastroenterologiia | Suplemento con prebióticos y vitaminas (incluida biotina) para alteraciones de la microbiota intestinal en pacientes con patología broncopulmonar tras antibióticos; evidencia indirecta |
| [25110039](https://pubmed.ncbi.nlm.nih.gov/25110039/) | 2014 | Observacional | International Journal of Molecular Medicine | Células endocrinas del antro gástrico en pacientes con síndrome de intestino irritable; la biotina no fue la intervención |
| [24891930](https://pubmed.ncbi.nlm.nih.gov/24891930/) | 2014 | Observacional | World Journal of Gastrointestinal Endoscopy | Células endocrinas de la mucosa oxíntica en síndrome de intestino irritable; la biotina no fue la intervención |
| [11304845](https://pubmed.ncbi.nlm.nih.gov/11304845/) | 2001 | Observacional | Journal of Clinical Pathology | Interleucina 10 en gastritis asociada a *Helicobacter pylori*; relación indirecta |
| [10354275](https://pubmed.ncbi.nlm.nih.gov/10354275/) | 1999 | Observacional | Kidney International | Linfocitos T del intestino delgado en nefropatía por IgA; no relacionado con el tratamiento de la dispepsia |

Ninguna de estas publicaciones evalúa la biotina como tratamiento de la dispepsia.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 215439 (cancelado) | CERNEVIT® | Polvo liofilizado para reconstituir a solución inyectable | Multivitaminas y elementos traza |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: el grafo de conocimiento asocia la biotina con las siguientes enfermedades como posibles contraindicaciones: enfermedad renal, piouréter, sarcoidosis, hiperparatiroidismo, osteítis fibrosa, hipercalcemia, nefrocalcinosis, trastornos del metabolismo del fósforo, nefrolitiasis (incluida la susceptibilidad asociada a SLC26A1), nefropatía aguda por uratos, estreñimiento y lesiones óseas metastásicas líticas. Estas asociaciones deben verificarse con fuentes clínicas, ya que no se basan en el texto de una etiqueta.
- **Interacciones farmacológicas**: no se encontraron interacciones registradas en la consulta realizada.

Para información de seguridad completa, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Aunque el puntaje de TxGNN es alto, no existen ensayos clínicos y la literatura disponible es indirecta o de baja relevancia (nivel de evidencia L5). Además, el único registro sanitario en Colombia está cancelado y no hay información de seguridad de prospecto, por lo que no es posible avanzar a una evaluación de seguridad.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), que es un vacío bloqueante para el cribado de seguridad
- Completar los datos del mecanismo de acción desde DrugBank
- Realizar una revisión sistemática de la literatura sobre biotina en síntomas gastrointestinales y dispepsia
- Evaluar la plausibilidad de un beneficio más allá de la corrección de una deficiencia nutricional
- Verificar las contraindicaciones del grafo de conocimiento (en particular las renales y del metabolismo del calcio y el fósforo) con fuentes clínicas
- Aclarar la situación regulatoria y la disponibilidad de productos con biotina en Colombia, dado que el único registro está cancelado
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

