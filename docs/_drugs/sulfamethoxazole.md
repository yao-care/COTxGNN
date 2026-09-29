---
layout: default
title: Sulfamethoxazole
parent: Evidencia Moderada (L3-L4)
nav_order: 366
evidence_level: L4
indication_count: 1
---

# Sulfamethoxazole
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **1** 
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

# Sulfametoxazol: De Sulfametoxazol y Trimetoprima (indicación no detallada en el registro) a Conjuntivitis Contagiosa Aguda

## Resumen en Una Frase

Sulfametoxazol es un antibacteriano de la clase de las sulfonamidas. En Colombia se comercializa en combinación con trimetoprima, y el registro sanitario no detalla su indicación original.
El modelo TxGNN predice que podría ser efectivo para **conjuntivitis contagiosa aguda**, pero hoy solo cuenta con **0 ensayos clínicos** y **1 publicación** observacional indirecta, que no evalúa el fármaco.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sulfametoxazol y trimetoprima (el registro solo indica la composición, no una indicación clínica) |
| Nueva Indicación Predicha | Conjuntivitis contagiosa aguda |
| Puntaje de Predicción TxGNN | 99.63% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Sulfametoxazol inhibe la enzima bacteriana dihidropteroato sintasa y bloquea la síntesis de folato, por lo que es plausible que actúe contra las bacterias que causan la conjuntivitis bacteriana aguda. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro de origen. Este mecanismo proviene de la justificación mecanística de la predicción y no pudo contrastarse con una fuente primaria.

La relación con la indicación original es indirecta, porque el registro colombiano no especifica para qué se aprobó el producto. El puntaje de 0.996 es únicamente una predicción del modelo.

Hay varias limitaciones:
- Las formas virales y alérgicas de conjuntivitis contagiosa no responderían a un antibacteriano.
- El estudio citado no muestra que se haya probado sulfametoxazol.
- El sulfametoxazol sistémico no es un tratamiento estándar de la conjuntivitis, y cualquier uso ocular de sulfonamidas sería tópico.
- Las presentaciones registradas en Colombia son solo orales (suspensión y tableta), y la compatibilidad de vía de administración aún está pendiente de evaluar.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31788487](https://pubmed.ncbi.nlm.nih.gov/31788487/) | 2019 | Observacional (vigilancia bacteriológica y de sensibilidad antimicrobiana, pediátrica) | Medical Hypothesis, Discovery & Innovation Ophthalmology Journal | Análisis retrospectivo de casos de conjuntivitis bacteriana aguda presunta en un hospital pediátrico de Patras (Grecia occidental). Describe la bacteriología y los patrones de sensibilidad a antibióticos, y confirma que la enfermedad suele tratarse de forma empírica con antibióticos tópicos de amplio espectro. El resumen disponible está truncado y no muestra datos sobre sulfametoxazol. |

## Información de Mercado en Colombia

Las entradas de la lista se repetían, por lo que se muestran solo los registros únicos (de un total de 20).

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20077704 | MEDIPRIM F SUSPENSION | Suspensión oral | Sulfametoxazol y trimetoprima |
| 19985112 | MEDIPRIM F (R) TABLETA | Tableta | Sulfametoxazol y trimetoprima |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo y en un estudio observacional indirecto que no evalúa sulfametoxazol, sin ensayos clínicos registrados. Además, faltan la información de seguridad del prospecto y la indicación original, y no hay una vía de administración compatible con uso ocular.

**Para avanzar se necesita:**
- Descargar y revisar el prospecto de INVIMA (advertencias y contraindicaciones), un dato bloqueante para el tamizaje de seguridad.
- Obtener el mecanismo de acción y las indicaciones originales desde DrugBank.
- Buscar evidencia directa del uso de sulfametoxazol (o sulfonamidas tópicas) en conjuntivitis bacteriana, incluidos ensayos clínicos y datos de sensibilidad.
- Evaluar la compatibilidad de vía y formulación, ya que los productos colombianos son solo orales.
- Aclarar qué formas de conjuntivitis contagiosa (bacteriana, viral, alérgica) serían el objetivo real.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

