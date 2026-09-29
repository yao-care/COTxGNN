---
layout: default
title: Ranibizumab
parent: Solo Predicción del Modelo (L5)
nav_order: 340
evidence_level: L5
indication_count: 10
---

# Ranibizumab
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

# Ranibizumab: De Indicación Original No Especificada a Retinopatía Diabética No Proliferativa Grave

## Resumen en Una Frase

Ranibizumab es un anticuerpo (fragmento) anti-VEGF que se comercializa en Colombia como solución inyectable (Lucentis®). El texto de indicación del registro solo repite el nombre del fármaco y DrugBank no aporta indicaciones originales, por lo que no se puede identificar la indicación original.
El modelo TxGNN predice que podría ser efectivo para la **retinopatía diabética no proliferativa grave**, con **6 ensayos clínicos** y **19 publicaciones** que respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (el registro solo dice "RANIBIZUMAB") |
| Nueva Indicación Predicha | Retinopatía diabética no proliferativa grave |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L1 (con salvedades, ver más abajo) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 15 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información conocida, ranibizumab neutraliza el VEGF-A, el factor que impulsa la fuga vascular, la falta de perfusión retiniana y la neovascularización en la retina.

En la retinopatía diabética, el VEGF está elevado en el vítreo y en el suero. Por eso el vínculo mecanístico es directo: bloquear el VEGF puede frenar la progresión de la enfermedad hacia complicaciones que amenazan la visión.

Además, ya existe evidencia de Fase 3. Destaca el ensayo PAVILION, publicado en 2025, que probó ranibizumab con el Sistema de Entrega por Puerto frente a observación en retinopatía diabética no proliferativa sin edema macular.

**Advertencia:** como no hay indicaciones originales registradas, no está claro si esto es un reposicionamiento real o un uso que ya figura en la etiqueta. Hay que confirmarlo con el etiquetado vigente antes de presentarlo como candidato nuevo.

**Sobre el nivel L1:** se asigna por el número de ensayos de Fase 3 completados. Solo NCT04503551 coincide directamente en fármaco y enfermedad. Los otros ensayos de Fase 3 estudian edema macular diabético o probablemente otro agente anti-VEGF.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04503551](https://clinicaltrials.gov/study/NCT04503551) | Fase 3 | Completado | 174 | Ranibizumab con Sistema de Entrega por Puerto frente a monitoreo en retinopatía diabética sin edema macular central. Coincidencia directa de fármaco y enfermedad |
| [NCT00444600](https://clinicaltrials.gov/study/NCT00444600) | Fase 3 | Completado | 691 | Ranibizumab o triamcinolona con láser en edema macular diabético. Mismo fármaco, pero la condición principal no es la retinopatía grave |
| [NCT02634333](https://clinicaltrials.gov/study/NCT02634333) | Fase 3 | Completado | 399 | Anti-VEGF intravítreo para prevenir complicaciones que amenazan la visión en retinopatía diabética. Respalda el efecto de clase; el agente probado probablemente no es ranibizumab |
| [NCT03452657](https://clinicaltrials.gov/study/NCT03452657) | Fase 3 | Desconocido | 118 | Ranibizumab intravítreo frente a inyección simulada para prevenir retinopatía diabética de alto riesgo |
| [NCT02834663](https://clinicaltrials.gov/study/NCT02834663) | Fase 4 | Completado | 25 | Ranibizumab en edema macular con retinopatía no proliferativa, sobre microaneurismas y área no perfundida. Estudio piloto pequeño de 6 meses |
| [NCT05222633](https://clinicaltrials.gov/study/NCT05222633) | N/A | Desconocido | 1000 | Estudio observacional de terapia anti-VEGF en condiciones reales. Poco relevante para retinopatía diabética |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [40048178](https://pubmed.ncbi.nlm.nih.gov/40048178/) | 2025 | ECA | JAMA Ophthalmol | Ensayo PAVILION: ranibizumab con Sistema de Entrega por Puerto frente a monitoreo en retinopatía no proliferativa sin edema macular |
| [39673354](https://pubmed.ncbi.nlm.nih.gov/39673354/) | 2024 | Revisión sistemática y metaanálisis | Health Technol Assess | Compara fármacos anti-VEGF con fotocoagulación láser en retinopatía diabética |
| [40347224](https://pubmed.ncbi.nlm.nih.gov/40347224/) | 2025 | Revisión sistemática y análisis económico | Health Technol Assess | Anti-VEGF frente a láser en retinopatía diabética, con evaluación económica |
| [32606578](https://pubmed.ncbi.nlm.nih.gov/32606578/) | 2020 | Análisis post hoc de ECA | Clin Ophthalmol | Predictores de regresión temprana de la retinopatía con ranibizumab en RIDE y RISE |
| [36774994](https://pubmed.ncbi.nlm.nih.gov/36774994/) | 2023 | Metaanálisis (post hoc de ECA) | Ophthalmol Retina | Relación entre la gravedad basal de la retinopatía y el tiempo de resolución del edema macular con ranibizumab |
| [35417296](https://pubmed.ncbi.nlm.nih.gov/35417296/) | 2022 | Análisis post hoc de ECA | Ophthalmic Surg Lasers Imaging Retina | Curso de la retinopatía en ojos contralaterales sin tratar en RIDE y RISE |
| [36161830](https://pubmed.ncbi.nlm.nih.gov/36161830/) | 2022 | Análisis de extensión abierta de ECA | BMJ Open Ophthalmol | Cambios en la escala de gravedad de la retinopatía con ranibizumab menos frecuente en RIDE y RISE |
| [30234859](https://pubmed.ncbi.nlm.nih.gov/30234859/) | 2018 | Análisis de ECA (DRCR.net Protocolo I) | Retina | Cambios a 5 años en la gravedad de la retinopatía en ojos tratados con ranibizumab por edema macular |
| [33966556](https://pubmed.ncbi.nlm.nih.gov/33966556/) | 2021 | Revisión | Expert Opin Biol Ther | Revisión del uso de ranibizumab en retinopatía diabética |
| [30973596](https://pubmed.ncbi.nlm.nih.gov/30973596/) | 2019 | Cohorte / análisis de imágenes | JAMA Ophthalmol | Características de la no perfusión retiniana en retinopatía no proliferativa grave y proliferativa |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19977793 | LUCENTIS® 10 MG/ML SOLUCIÓN INYECTABLE (Novartis Pharma AG) | Solución inyectable | Solo figura "RANIBIZUMAB" (sin texto de indicación) |

Los datos muestran 15 registros en total. Las cinco filas disponibles corresponden al mismo número de registro, así que se muestra una sola.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay un ensayo de Fase 3 completado con coincidencia directa (NCT04503551), un ECA publicado (PAVILION), revisiones sistemáticas y varios análisis de ECA con ranibizumab. La evidencia es sólida, pero no está claro si esta indicación ya está aprobada, y faltan los datos de seguridad locales.

**Para avanzar se necesita:**
- Confirmar con el etiquetado vigente de INVIMA si la retinopatía diabética ya es una indicación aprobada.
- Descargar y analizar el prospecto de INVIMA para completar advertencias y contraindicaciones.
- Obtener el mecanismo de acción desde DrugBank.
- Definir medidas de control: administración solo intravítrea, vigilancia de endoftalmitis y de presión intraocular, y evaluación de la adherencia a largo plazo y del costo.

**Nota sobre otras predicciones:** el resto de las predicciones de TxGNN (cataratas de distintos tipos y enfermedad hemorrágica del recién nacido) no tiene sustento mecanístico ni clínico. Se recomienda mantenerlas en Hold. Un estudio sobre catarata cortical y un reporte de caso apuntan más bien a un posible riesgo del lente que a un beneficio.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

