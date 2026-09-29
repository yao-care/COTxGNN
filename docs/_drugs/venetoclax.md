---
layout: default
title: Venetoclax
parent: Evidencia Moderada (L3-L4)
nav_order: 404
evidence_level: L4
indication_count: 10
---

# Venetoclax
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

# Venetoclax: De Indicación Original No Declarada en el Registro a Leucemia Linfocítica Crónica/Linfoma Linfocítico de Células Pequeñas (Subtipo de Pre-Centro Germinal)

## Resumen en Una Frase

Venetoclax es un inhibidor selectivo de BCL-2 que se comercializa en Colombia como tabletas recubiertas. El registro sanitario consultado no incluye un texto de indicación aprobada, solo el nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para la **leucemia linfocítica crónica/linfoma linfocítico de células pequeñas del subtipo pre-centro germinal**, pero hoy la evidencia es mínima: **0 ensayos clínicos** y **1 publicación** indirecta.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el texto del registro solo dice "VENETOCLAX") |
| Nueva Indicación Predicha | Leucemia linfocítica crónica/linfoma linfocítico de células pequeñas de pre-centro germinal |
| Puntaje de Predicción TxGNN | 99,55 % |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone en DrugBank de datos detallados sobre el mecanismo de acción. Según el análisis del paquete de evidencia, venetoclax es un inhibidor selectivo de BCL-2 (mimético de BH3). Las células de LLC/LLP dependen de la sobreexpresión de BCL-2 para sobrevivir, de modo que el mecanismo encaja bien con esta enfermedad.

Hay un punto que conviene aclarar antes de tratar esto como reposicionamiento. El paquete indica que venetoclax suele estar autorizado para LLC/LLP. Por eso esta entrada probablemente corresponde a un subtipo de una indicación ya existente y no a un reposicionamiento genuino. Como el registro colombiano no lista la indicación, esta conclusión debe verificarse contra la etiqueta oficial.

La única publicación disponible es una revisión sobre la estructura y función del receptor de células B (BCR) en la LLC. Distingue el subtipo de pre-centro germinal (IGHV no mutado, peor pronóstico) del de post-centro germinal (IGHV mutado, mejor pronóstico). Esa revisión aporta contexto biológico, pero no evalúa venetoclax.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35158929](https://pubmed.ncbi.nlm.nih.gov/35158929/) | 2022 | Revisión / análisis biológico | Cancers | Revisa la estructura y función del BCR tumoral en LLC. Describe los subtipos de pre-centro germinal (IGHV no mutado, mal pronóstico) y post-centro germinal (IGHV mutado, buen pronóstico). No evalúa venetoclax directamente. |

*Actualmente no hay ensayos clínicos relacionados registrados para esta indicación específica.*

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20139971 | VENCLEXTA® 100 MG | Tableta recubierta | VENETOCLAX (solo se lista el principio activo) |
| 20139971 | VENCLEXTA® 10 MG | Tableta recubierta | VENETOCLAX (solo se lista el principio activo) |

Titular: ABBVIE S.A.S. Vía de administración: oral. Las cinco filas del paquete corresponden al mismo número de registro, repetido por presentación, por lo que aquí se muestran las dos presentaciones distintas.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de BCL-2) |
| Riesgo de Mielosupresión | Presente. La literatura del paquete señala la mielosupresión y el síndrome de lisis tumoral como los eventos más comunes con venetoclax. |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial (citopenias), signos de síndrome de lisis tumoral, función hepática y renal, electrolitos |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos para este subtipo y la única publicación es una revisión biológica indirecta. La predicción de TxGNN es plausible por el mecanismo, pero este paquete no basta para respaldarla. Además, la entrada probablemente ya está cubierta por la indicación general de LLC/LLP, por lo que no está claro que sea un reposicionamiento real.

**Para avanzar se necesita:**
- Descargar y revisar el prospecto de INVIMA para confirmar la indicación autorizada (¿ya incluye LLC/LLP?) y obtener advertencias y contraindicaciones. Sin esto no se puede pasar al tamizaje de seguridad.
- Completar los datos de mecanismo de acción desde DrugBank.
- Buscar literatura y ensayos específicos de venetoclax en LLC/LLP con IGHV no mutado, por ejemplo el estudio MURANO (PMID 40009494), que aparece en el paquete bajo otra entrada.
- Nota: el paquete contiene otras indicaciones predichas con más respaldo, como leucemia mieloide (L1, Phase 3 con VIALE-A) y linfoma folicular (L2), que conviene evaluar en informes separados.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

