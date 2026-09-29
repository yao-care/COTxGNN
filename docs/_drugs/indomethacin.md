---
layout: default
title: Indomethacin
parent: Solo Predicción del Modelo (L5)
nav_order: 222
evidence_level: L5
indication_count: 10
---

# Indomethacin
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

# Indometacina: De Afecciones Inflamatorias Reumáticas a Síndrome de Braquidactilia-Sindactilia

## Resumen en Una Frase

La indometacina es un antiinflamatorio no esteroideo (AINE), usado ampliamente en afecciones inflamatorias como artritis reumatoide, osteoartritis, espondilitis anquilosante, bursitis/tendinitis y gota aguda.
El modelo TxGNN predice que podría ser efectiva para el **síndrome de braquidactilia-sindactilia**, con un puntaje muy alto (99.97%) pero **0 ensayos clínicos** y **0 publicaciones** que lo respalden. Es una predicción sin sustento mecanístico.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Afecciones inflamatorias reumáticas (según datos farmacológicos; el registro INVIMA solo dice "Indometacina", sin indicación detallada) |
| Nueva Indicación Predicha | Síndrome de braquidactilia-sindactilia |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

**No es razonable con la información disponible.** No hay datos formales de mecanismo de acción (MOA) en el paquete de evidencia. Aun así, los datos farmacológicos muestran que la indometacina inhibe COX-1 y COX-2, es decir, es un inhibidor no selectivo de la ciclooxigenasa. Reduce la síntesis de prostaglandinas y, con ello, la inflamación, el dolor y la fiebre. También aparecen como dianas el receptor DP2, el receptor PPAR-γ y el transportador de folato acoplado a protones (SLC46A1).

El síndrome de braquidactilia-sindactilia es una malformación congénita del desarrollo de las extremidades y no tiene un componente inflamatorio. Por eso no se identifica un vínculo plausible entre la inhibición de COX y esta enfermedad. El puntaje alto del modelo es solo una predicción computacional.

Las predicciones que ocupan los primeros puestos (rango 1 a 7) son síndromes genéticos del desarrollo o de displasia esquelética, como el síndrome de microftalmia colobomatosa, la displasia acromesomélica, la braquiolmia y el síndrome WHIM. Ninguna tiene un mecanismo plausible con la indometacina ni evidencia real.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Otras Predicciones con Respaldo Parcial

Entre las 10 predicciones evaluadas, solo estas tienen alguna evidencia. Todas están relacionadas con artritis o afecciones reumáticas.

| Enfermedad Predicha | Puntaje TxGNN | Nivel | Observación |
|------|------|------|------|
| Artritis idiopática juvenil (AIJ) | 99.84% | L3 | 20 publicaciones (se dispusieron 10). Mecanismo coherente con la inhibición de COX. Sin ensayos registrados |
| AIJ poliarticular con factor reumatoide positivo | 99.84% | L4 | Sin evidencia propia. Apoyo indirecto vía AIJ |
| Nodulosis reumatoide | 99.83% | L4 | Literatura antigua e indirecta. Los nódulos no responden a la inhibición de COX |

Publicaciones más relevantes para AIJ:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [362571](https://pubmed.ncbi.nlm.nih.gov/362571/) | 1978 | ECA | S Afr Med J | Estudio doble ciego cruzado en 30 niños con artritis crónica juvenil: ketoprofeno vs. indometacina. Ambos fueron seguros y eficaces. La indometacina resultó el fármaco preferido |
| [1379157](https://pubmed.ncbi.nlm.nih.gov/1379157/) | 1992 | Revisión | Drugs | Los AINE, incluida la indometacina, forman parte del manejo farmacológico de la artritis reumatoide juvenil |
| [8422565](https://pubmed.ncbi.nlm.nih.gov/8422565/) | 1993 | Revisión | Br J Rheumatol | Salicilatos e indometacina se usan para la fiebre de la AIJ sistémica. No son más eficaces que otros AINE y son más tóxicos |
| [19078081](https://pubmed.ncbi.nlm.nih.gov/19078081/) | 1996 | Encuesta | J Clin Rheumatol | Reumatólogos pediátricos: indometacina usada en 11% de los pacientes con AR juvenil, lejos del naproxeno (48%) |

La evidencia es antigua. La práctica actual usa FAME y biológicos, y los AINE quedan como apoyo sintomático. Además, la AIJ podría ser un uso ya establecido y no un reposicionamiento real, dado que no hay indicaciones originales registradas. Hay que verificarlo en el prospecto.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20056703 | NB PEXAIL CÁPSULA BLANDA 25 MG | Cápsula blanda | Indometacina (el registro no detalla indicaciones) |

Fabricante: Nature's Blend de Colombia Ltda.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Las 5 entradas del análisis de interacciones (DP2, PPAR-γ, SLC46A1, COX-1, COX-2) son dianas farmacológicas, no interacciones con otros medicamentos. No hay datos de interacciones farmacológicas reales.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal (síndrome de braquidactilia-sindactilia) solo tiene puntaje del modelo, sin ensayos ni literatura, y no hay vínculo mecanístico plausible con la inhibición de COX. La única línea con respaldo, la AIJ (L3), tiene evidencia antigua y podría ser un uso ya establecido.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones), que es un vacío bloqueante para el tamizaje de seguridad.
- Confirmar el MOA formal en DrugBank.
- Verificar si la AIJ ya figura como indicación en el prospecto o en otras autorizaciones.
- Recuperar las 10 publicaciones restantes sobre AIJ y revisar si existen ensayos en registros internacionales.
- Priorizar la AIJ sobre las demás predicciones si se decide continuar la evaluación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

