---
layout: default
title: Romiplostim
parent: Solo Predicción del Modelo (L5)
nav_order: 570
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
monitor_inn: "romiplostim"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "fetal and neonatal alloimmune thrombocytopenia", "Scott syndrome", "hemorrhagic disorder due to a constitutional thrombocytopenia", "bleeding diathesis due to a collagen receptor defect", "platelet-type bleeding disorder", "autosomal dominant macrothrombocytopenia", "Ehlers-Danlos syndrome, fibronectinemic type"]
description: "Romiplostim: nueva indicación predicha, Primary release disorder of platelets (nivel de evidencia L5). Indicación original: ROMIPLOSTIM"
---

# Romiplostim
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Romiplostim: Primary release disorder of platelets
{: .text-alpha }

## Resumen en Una Frase

Romiplostim es un agonista del receptor de trombopoyetina (MPL) que se utiliza para aumentar el recuento de plaquetas en la púrpura trombocitopénica inmune (PTI) crónica; en el registro sanitario colombiano su indicación figura únicamente como "ROMIPLOSTIM".
El modelo TxGNN predice que podría ser efectivo para el **trastorno de liberación primaria de plaquetas**, pero **no hay ensayos clínicos** y solo **1 publicación** de mecanismo (sobre PTI, no sobre esta enfermedad) relacionada con esta predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | ROMIPLOSTIM |
| Nueva Indicación Predicha | Primary release disorder of platelets |
| Puntaje de Predicción TxGNN | 1.0000 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información farmacológica conocida, romiplostim es un péptido agonista del receptor de trombopoyetina (MPL) que estimula la producción de plaquetas, y su uso establecido es la PTI crónica.

Sin embargo, el trastorno de liberación primaria de plaquetas es un defecto **cualitativo** de la función plaquetaria, que normalmente cursa con recuento de plaquetas normal. Aumentar el número de plaquetas difícilmente corregiría el defecto. La única publicación recuperada (PMID 25682608) trata de autoanticuerpos antiplaquetarios en PTI, no de este trastorno. El vínculo mecanístico es indirecto y el puntaje tan alto del modelo no está respaldado por evidencia clínica.

Otras predicciones del mismo análisis muestran un patrón similar: la mayoría son defectos funcionales de plaquetas (trombastenia de Glanzmann, seudoenfermedad de von Willebrand, síndrome de Scott, defecto del receptor de colágeno), donde el mecanismo no es claramente aplicable. Las más plausibles mecanísticamente son las trombocitopenias cuantitativas: la trombocitopenia aloinmune fetal y neonatal (puntaje 0.9999, evidencia L4, solo indirecta), la trombocitopenia constitucional hemorrágica y la macrotrombocitopenia autosómica dominante. Estas se clasifican como "Research Question", sin ensayos específicos.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [25682608](https://pubmed.ncbi.nlm.nih.gov/25682608/) | 2015 | Investigación básica/mecanística (PTI) | Haematologica | Los autoanticuerpos antiplaquetarios inhiben la formación de proplaquetas por los megacariocitos y reducen la producción de plaquetas in vitro en PTI. No aborda el trastorno de liberación plaquetaria. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|-----|
| 20027769 | NPLATE® 250 MCG (AMGEN EUROPE B.V.) | Polvo liofilizado para reconstituir a solución inyectable | ROMIPLOSTIM | Vigente |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 2 registros. Con **carfilzomib** existe una interacción de nivel **Mayor** (fuente: DDInter). El segundo registro corresponde a la relación farmacológica con su diana, el receptor de trombopoyetina (MPL), y no a una interacción clínica con otro fármaco.

Consultar el prospecto para información sobre advertencias y contraindicaciones.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5): no hay ensayos clínicos y la única publicación trata de otra enfermedad (PTI). Además, el defecto es de función plaquetaria con recuento normal, por lo que el mecanismo de romiplostim no es claramente aplicable.

<!-- review:begin co-lic-20261105-romiplostim-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, el defecto es de función plaquetaria con recuento normal, por lo que el mecanismo de romiplostim no es claramente aplicable. El único registro sanitario en Colombia está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-romiplostim-1 -->

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) y del texto del prospecto (advertencias y contraindicaciones) obtenidos de fuentes oficiales.
- Evidencia clínica o preclínica específica en trastornos de liberación plaquetaria; de lo contrario, no priorizar esta indicación.
- Reorientar la evaluación hacia las trombocitopenias cuantitativas (trombocitopenia aloinmune fetal y neonatal, trombocitopenias constitucionales, macrotrombocitopenia autosómica dominante), comenzando por la seguridad, en especial la transferencia placentaria y la seguridad fetal.

<!-- review:begin co-lic-20261105-romiplostim-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Reorientar la evaluación hacia las trombocitopenias cuantitativas (trombocitopenia aloinmune fetal y neonatal, trombocitopenias constitucionales, macrotrombocitopenia autosómica dominante), comenzando por la seguridad, en especial la transferencia placentaria y la seguridad fetal. / Aclarar la situación regulatoria: el registro está cancelado, por lo que se requeriría un nuevo registro o una vía de importación." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-romiplostim-2 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "El único registro sanitario en Colombia está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Aclarar la situación regulatoria: el registro está cancelado, por lo que se requeriría un nuevo registro o una vía de importación" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

