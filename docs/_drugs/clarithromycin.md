---
layout: default
title: Clarithromycin
parent: Solo Predicción del Modelo (L5)
nav_order: 129
evidence_level: L5
indication_count: 5
---

# Clarithromycin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Claritromicina: De Antibiótico Macrólido a Síndrome de Hiperviscosidad Policlonal

## Resumen en Una Frase

Claritromicina es un antibiótico macrólido comercializado en Colombia (por ejemplo, como Klaricid). El registro sanitario local no detalla la indicación aprobada; solo repite el nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de hiperviscosidad policlonal**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción. Es una señal puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro solo indica «CLARITROMICINA») |
| Nueva Indicación Predicha | Síndrome de hiperviscosidad policlonal |
| Puntaje de Predicción TxGNN | 99.35% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, claritromicina es un antibiótico de la clase de los macrólidos y su uso en infecciones bacterianas está bien establecido. Estos fármacos también tienen efectos inmunomoduladores y antiinflamatorios descritos.

El síndrome de hiperviscosidad policlonal se relaciona con un exceso de inmunoglobulinas policlonales en sangre. Los datos disponibles no conectan el efecto inmunomodulador de la claritromicina con ese mecanismo. El puntaje alto del modelo (99.35%) proviene solo de patrones en un grafo de conocimiento y no constituye evidencia biológica ni clínica.

Por ahora, la predicción no tiene un fundamento mecanístico que se pueda evaluar. Para valorarla haría falta conocer el mecanismo de acción del fármaco y establecer una relación causal con la producción o el efecto de las inmunoglobulinas.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20179259 | KLARICID® SUSPENSION 125 MG/ 5 ML | Gránulos | CLARITROMICINA |

Los datos traen 20 registros en total, pero las cinco entradas detalladas corresponden todas al mismo registro (20179259), por lo que se muestra una sola vez. Además de los gránulos para suspensión, hay presentaciones de tableta de liberación modificada por vía oral.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es de nivel L5: no tiene ensayos, literatura ni un vínculo mecanístico plausible, y solo se apoya en el puntaje del modelo. Los datos de seguridad locales y el mecanismo de acción tampoco están disponibles.

**Para avanzar se necesita:**
- Obtener el mecanismo de acción desde DrugBank.
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones), porque sin él no se puede pasar al tamizaje de seguridad.
- Buscar de forma dirigida literatura o estudios preclínicos que relacionen macrólidos con hiperviscosidad o hipergammaglobulinemia.
- Aclarar la indicación aprobada en el registro sanitario, ya que hoy solo figura el nombre del principio activo.

**Otras predicciones del modelo, para priorizar:**
- **Queratoconjuntivitis epitelial punteada** (99.11%): es la única con una hipótesis razonable. Los macrólidos se usan en meibomitis y disfunción de las glándulas de Meibomio. Hay una publicación de 2024 (PMID [38472959](https://pubmed.ncbi.nlm.nih.gov/38472959/)) sobre queratoconjuntivitis relacionada con meibomitis. Su diseño y el uso específico de claritromicina se dedujeron solo del título, así que el nivel L3 debe verificarse con el texto completo antes de apoyarse en él.
- **Hiperamilasemia** (99.35%): la única publicación es un reporte de caso de 2004 sobre infección por *M. abscessus* con macroamilasemia (PMID [15228140](https://pubmed.ncbi.nlm.nih.gov/15228140/)). Probablemente la claritromicina se usó contra la infección y no contra la hiperamilasemia.
- **Analbuminemia congénita** y **incompatibilidad de grupo sanguíneo**: no tienen evidencia ni fundamento mecanístico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

