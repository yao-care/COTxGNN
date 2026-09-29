---
layout: default
title: Leuprolide
parent: Solo Predicción del Modelo (L5)
nav_order: 252
evidence_level: L5
indication_count: 2
---

# Leuprolide
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

# Leuprolida: De Cáncer de Próstata Avanzado a Osteoartritis

## Resumen en Una Frase

Leuprolida es un agonista de la hormona liberadora de gonadotropinas (GnRH), usado originalmente para el cáncer de próstata avanzado, los miomas uterinos, la endometriosis y la pubertad precoz.
El modelo TxGNN predice que podría ser efectivo para **osteoartritis**, pero solo hay **1 ensayo clínico** y **1 publicación** asociados, y ninguno estudia esta enfermedad.
La predicción se apoya únicamente en el modelo, sin respaldo clínico real.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | El registro sanitario solo dice "Leuprorelina acetato", sin indicación explícita. Según farmacología: cáncer de próstata avanzado, miomas uterinos, endometriosis y pubertad precoz |
| Nueva Indicación Predicha | Osteoartritis |
| Puntaje de Predicción TxGNN | 99.70% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 16 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro. Según la información farmacológica conocida, leuprolida actúa sobre el receptor GnRH1 (gen *GNRHR*) y suprime los esteroides sexuales gonadales. Su eficacia en cáncer de próstata avanzado, endometriosis y pubertad precoz está establecida.

Con los datos disponibles **no se identifica un vínculo mecanístico creíble** con la osteoartritis. La supresión de hormonas sexuales se asocia, en general, con efectos adversos óseos y articulares, no con protección del cartílago. El puntaje de 99.70% parece un artefacto del grafo de conocimiento y no un indicio clínico.

La segunda predicción del modelo, la pseudoacondroplasia (puntaje 99.69%), tampoco tiene ensayos ni literatura. Es una displasia esquelética causada por mutaciones en COMP, y la supresión puberal con agonistas de GnRH no actúa sobre esa patología. Cualquier vínculo es puramente especulativo.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00002881](https://clinicaltrials.gov/study/NCT00002881) | Fase 3 | Completado | No disponible | Orquiectomía/análogo de LHRH + flutamida + suramina + hidrocortisona vs. el mismo esquema sin suramina ni hidrocortisona, en cáncer de próstata metastásico. **No estudia osteoartritis** (relevancia: C). La coincidencia probablemente se debe a un nodo de fármaco compartido |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [20133250](https://pubmed.ncbi.nlm.nih.gov/20133250/) | 2010 | Reporte de caso | Clinical Breast Cancer | Adenocarcinoma prostático metastásico que simulaba un carcinoma inflamatorio de mama en un hombre de 78 años. No guarda relación con osteoartritis |

## Información de Mercado en Colombia

Los datos entregados muestran el mismo registro repetido cinco veces. Se presenta una sola vez. El total declarado es de 16 registros.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19956218 | ELIGARD® 22.5 MG (Tolmar Inc.) | Polvo liofilizado para reconstituir a solución inyectable | Leuprorelina acetato (sin indicación detallada) |

También figura la forma "polvo estéril para reconstituir a suspensión inyectable".

## Citotoxicidad

Leuprolida se usa en cáncer de próstata, por lo que se incluye esta sección. No es un citotóxico convencional.

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia hormonal (agonista de GnRH), no citotóxico convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es de nivel L5: solo puntaje del modelo, sin estudios reales sobre osteoartritis. El único ensayo y la única publicación encontrados tratan de cáncer de próstata. Además, la supresión de esteroides sexuales sugiere más bien riesgo que beneficio para hueso y articulación.

**Para avanzar se necesita:**
- Evidencia directa (preclínica o clínica) de leuprolida u otros agonistas de GnRH en osteoartritis.
- Una hipótesis mecanística plausible que explique el puntaje del modelo.
- Descargar y analizar el prospecto de INVIMA para completar advertencias y contraindicaciones.
- Completar los datos de mecanismo de acción (DrugBank).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

