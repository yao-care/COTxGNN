---
layout: default
title: Panitumumab
parent: Solo Predicción del Modelo (L5)
nav_order: 497
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Panitumumab: nueva indicación predicha, Osteoporosis inducida por fármacos (drug-induced osteoporosis) (nivel de evidencia L5). Indicación original: Panitumumab"
monitor_inn: "PANITUMUMAB"
predicted_indications: ["drug-induced osteoporosis", "severe nonproliferative diabetic retinopathy"]
---

# Panitumumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Panitumumab: De Indicación Registrada (sin texto descriptivo) a Osteoporosis Inducida por Fármacos
{: .text-alpha }

## Resumen en Una Frase

Panitumumab es un anticuerpo monoclonal anti-EGFR; su registro sanitario en Colombia (Vectibix®) no incluye un texto de indicación descriptivo.
El modelo TxGNN predice que podría ser efectivo para **osteoporosis inducida por fármacos**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.

<!-- review:begin co-lic-20261105-panitumumab-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Panitumumab es un anticuerpo monoclonal anti-EGFR; su registro sanitario en Colombia (Vectibix®) no incluye un texto de indicación descriptivo y actualmente está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-panitumumab-1 -->

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Panitumumab (el registro solo repite el nombre del principio activo, sin indicación descrita) |
| Nueva Indicación Predicha | Osteoporosis inducida por fármacos (drug-induced osteoporosis) |
| Puntaje de Predicción TxGNN | 0.9913 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Panitumumab (traducción no oficial): «El EGFR es una glucoproteína transmembrana que pertenece a una subfamilia de receptores tirosina-cinasa de tipo I, que incluye EGFR, HER2, HER3 y HER4. El EGFR se expresa de forma constitutiva en los tejidos epiteliales normales, incluidos la piel y el folículo piloso. […] El panitumumab se une específicamente al EGFR tanto en las células normales como en las tumorales, e inhibe de forma competitiva la unión de los ligandos del EGFR.» Texto original en inglés: "The EGFR is a transmembrane glycoprotein that is a member of a subfamily of type I receptor tyrosine kinases, including EGFR, HER2, HER3, and HER4. EGFR is constitutively expressed in normal epithelial tissues, including the skin and hair follicle. […] Panitumumab binds specifically to EGFR on both normal and tumor cells, and competitively inhibits the binding of ligands for EGFR." ([DailyMed: Vectibix (panitumumab) prescribing information, Amgen, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e0fa4bca-f245-4d92-ae29-b0c630a315c2), versión del 2026-06-23; consultado el 2026-11-19). Según la información conocida, panitumumab es un anticuerpo monoclonal que bloquea el receptor del factor de crecimiento epidérmico (EGFR), usado en oncología.

La señalización de EGFR participa en la diferenciación de los osteoblastos y en la remodelación ósea, por lo que bloquearla podría afectar el metabolismo óseo. Sin embargo, este vínculo sugiere más bien un **posible efecto adverso** (por ejemplo, efectos óseos asociados a hipomagnesemia) que un beneficio terapéutico. La dirección del efecto (beneficio o daño) no está resuelta.

El puntaje alto de TxGNN (0.9913) es solo una predicción del modelo, sin respaldo de ensayos clínicos ni literatura. Por ello, debe interpretarse con cautela.

**Otra predicción del modelo:** retinopatía diabética no proliferativa grave (puntaje 0.9905, nivel L5, decisión Hold). Existe un vínculo especulativo por la transactivación de EGFR en la señalización vascular retiniana y las vías relacionadas con VEGF. Al ser un anticuerpo de administración sistémica con un perfil de toxicidad importante (dermatológica, hipomagnesemia) y sin datos oculares, el vínculo sigue siendo hipotético.

---

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 20025916 | VECTIBIX® 20 MG/ ML | SOLUCIÓN CONCENTRADA PARA INFUSIÓN | PANITUMUMAB | Vigente |

Se muestra el único registro sanitario de este principio activo en los datos del INVIMA, Código Único de Medicamentos.

<!-- licenses:end -->

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (anticuerpo monoclonal anti-EGFR) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Según la información conocida de la clase: electrolitos (especialmente magnesio y calcio), piel y función general; confirmar en el prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas:** se identificaron 27 interacciones; en los datos compilados se detallan 20.
  - **Mayores:** amiodarona, trióxido de arsénico, bevacizumab, dofetilida, dronedarona, droperidol, ácido aminolevulínico, irinotecán (incluido el liposomal) y levacetilmetadol.
  - **Moderadas:** inhibidores de la bomba de protones (rabeprazol, omeprazol, dexlansoprazol, esomeprazol, lansoprazol, pantoprazol), metoxaleno, ácido aminolevulínico tópico, disopiramida e idelalisib.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (L5), sin ensayos clínicos ni literatura. El vínculo mecanístico sugiere un posible daño óseo más que un beneficio.

<!-- review:begin co-lic-20261105-panitumumab-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "El vínculo mecanístico sugiere un posible daño óseo más que un beneficio, y el único registro sanitario en Colombia está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-panitumumab-2 -->

**Para avanzar se necesita:**
- Obtener y analizar el prospecto del INVIMA (advertencias y contraindicaciones), actualmente no disponible.
- Completar los datos del mecanismo de acción desde DrugBank.
- Aclarar la dirección del efecto (beneficio o daño) sobre el hueso mediante estudios preclínicos o revisión de la literatura.
- Verificar la situación regulatoria y la disponibilidad real del producto en Colombia.
- Evaluar la compatibilidad de vías de administración, ya que un anticuerpo sistémico podría no ser adecuado para las nuevas indicaciones.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "y actualmente está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "y el único registro sanitario en Colombia está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Vectibix (panitumumab) prescribing information, Amgen, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e0fa4bca-f245-4d92-ae29-b0c630a315c2) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

