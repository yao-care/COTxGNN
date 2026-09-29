---
layout: default
title: Valsartan
parent: Evidencia Moderada (L3-L4)
nav_order: 402
evidence_level: L4
indication_count: 7
---

# Valsartan
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **7** 
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

# Valsartán: De Valsartán y Diuréticos (combinación registrada) a Enfermedad Renal Hipertensiva Maligna

## Resumen en Una Frase

Valsartán está registrado en Colombia como componente de combinaciones con diuréticos (por ejemplo, Diovan HCT).
El modelo TxGNN predice que podría ser efectivo para **enfermedad renal hipertensiva maligna**,
pero actualmente hay **0 ensayos clínicos** y **1 publicación preclínica** (sobre otro fármaco, avosentán), por lo que la evidencia directa es muy limitada.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Valsartán y diuréticos |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, valsartán es un bloqueador del receptor de angiotensina II tipo 1 (ARA-II), su uso en hipertensión está establecido, y mecanísticamente podría ser aplicable a la enfermedad renal hipertensiva maligna.

La hipertensión maligna y la nefropatía hipertensiva se asocian con una sobreactivación del sistema renina-angiotensina-aldosterona (SRAA). Bloquear el receptor AT1 es, por tanto, un vínculo biológicamente plausible con la indicación original relacionada con la presión arterial.

Sin embargo, el vínculo es **indirecto**. La única publicación recuperada evaluó avosentán, un antagonista de endotelina, en ratas transgénicas con nefropatía hipertensiva. No evaluó valsartán. Por eso la plausibilidad se apoya en el mecanismo de clase y no en datos propios del fármaco.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [24368192](https://pubmed.ncbi.nlm.nih.gov/24368192/) | 2014 | Estudio preclínico (otro fármaco: avosentán) | Pharmacological Research | En ratas transgénicas con renina y angiotensinógeno humanos, avosentán protegió frente a la nefropatía hipertensiva con dosis que no causaron retención de líquidos. No involucra valsartán. |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19980966 | DIOVAN® HCT 320 / 12.5 MG (Novartis Pharma A.G.) | Tableta recubierta | Valsartán y diuréticos |

Nota: el paquete de datos indica 20 registros en total, pero las entradas recibidas corresponden todas al mismo registro (19980966), por lo que se muestra una sola vez.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto en TxGNN, pero no hay ensayos clínicos y la única publicación es preclínica y de otro fármaco. La evidencia es indirecta (nivel L4) y no basta para avanzar.

**Para avanzar se necesita:**
- Estudios preclínicos o clínicos que evalúen específicamente valsartán (o ARA-II de la misma clase) en nefropatía hipertensiva maligna
- Datos de mecanismo de acción confirmados desde DrugBank
- Advertencias y contraindicaciones del prospecto de INVIMA para completar el tamizaje de seguridad
- Confirmar el listado completo de los 20 registros sanitarios y sus indicaciones aprobadas

Como referencia, otra predicción del mismo análisis, hipertensión renovascular maligna, cuenta con un estudio preclínico de clase ARA-II (PMID 11560862) que apoya el mecanismo. También sigue sin tener ensayos clínicos con valsartán.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

