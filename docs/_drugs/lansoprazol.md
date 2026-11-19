---
layout: default
title: Lansoprazol
parent: Solo Predicción del Modelo (L5)
nav_order: 379
evidence_level: L5
indication_count: 1
drugbank_id: DB00448
monitor_inn: "Lansoprazole"
predicted_indications: ["duodenal obstruction"]
last_modified_at: 2026-11-16
description: "Lansoprazol: nueva indicación predicha, Obstrucción duodenal (duodenal obstruction) (nivel de evidencia L5). Indicación original: LANSOPRAZOL"
---

# Lansoprazol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Lansoprazol: Obstrucción duodenal (duodenal obstruction)
{: .text-alpha }

## Resumen en Una Frase

Lansoprazol es un inhibidor de la bomba de protones que suprime la secreción de ácido gástrico.
El modelo TxGNN predice que podría ser útil para **obstrucción duodenal (duodenal obstruction)**,
pero actualmente no hay ensayos clínicos ni publicaciones que respalden esta dirección; es una predicción solo del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | LANSOPRAZOL |
| Nueva Indicación Predicha | Obstrucción duodenal (duodenal obstruction) |
| Puntaje de Predicción TxGNN | 0.9968 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 6 de 6) |
| Número de Registros Sanitarios | 6 (vigentes: 6) |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Lansoprazol (traducción no oficial): «El lansoprazol pertenece a una clase de compuestos antisecretores, los bencimidazoles sustituidos, que suprimen la secreción de ácido gástrico mediante la inhibición específica del sistema enzimático (H +, K + )-ATPasa en la superficie secretora de la célula parietal gástrica. Dado que este sistema enzimático se considera la bomba de ácido (de protones) dentro de la célula parietal, el lansoprazol se ha caracterizado como un inhibidor de la bomba de ácido gástrico, ya que bloquea el paso final de la producción de ácido.» Texto original en inglés: "Lansoprazole belongs to a class of antisecretory compounds, the substituted benzimidazoles, that suppress gastric acid secretion by specific inhibition of the (H +, K + )-ATPase enzyme system at the secretory surface of the gastric parietal cell. Because this enzyme system is regarded as the acid (proton) pump within the parietal cell, lansoprazole has been characterized as a gastric acid-pump inhibitor, in that it blocks the final step of acid production." ([DailyMed: Prevacid (lansoprazole) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=71ba78cb-7e46-43eb-9425-fa130f537f84), versión del 2025-07-08; consultado el 2026-11-19). Según la información conocida, el lansoprazol es un inhibidor de la bomba de protones (H+/K+-ATPasa) que reduce la producción de ácido gástrico.

Un vínculo indirecto plausible es que la supresión del ácido podría ayudar en la enfermedad ulcerosa péptica o en la inflamación duodenal, que son causas frecuentes de obstrucción duodenal (por ejemplo, estenosis o edema asociados a úlcera). En cambio, no aliviaría una obstrucción mecánica fija, como las de origen maligno, el páncreas anular o el síndrome de la arteria mesentérica superior.

Este razonamiento no puede verificarse con los datos disponibles. La predicción podría reflejar la cercanía del fármaco con enfermedades gastrointestinales relacionadas, como la úlcera duodenal, más que un efecto terapéutico real.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 20057384 | LANZOR® 30 MG CÁPSULA | Cápsula dura |
| 20093574 | LANGENIX® 30MG CÁPSULAS DE LIBERACIÓN RETARDADA | Cápsula de liberación prolongada |
| 20145955 | LANGENIX® 15MG CÁPSULAS DE LIBERACIÓN RETARDADA | Cápsula de liberación prolongada |
| 20172406 | DIZMOPRAZ® CÁPSULAS. MICROGRÁNULOS CON CUBIERTA ENTÉRICA | Cápsula dura |
| 19939607 | REFLUYET® | Cápsula dura |

Hay 6 registros sanitarios vigentes; la tabla muestra los 5 principales.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5): no hay ensayos clínicos ni literatura que estudien directamente la obstrucción duodenal, y el mecanismo propuesto solo aplicaría a causas inflamatorias o ulcerosas, no a obstrucciones mecánicas fijas.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA)
- Revisión de las advertencias y contraindicaciones del prospecto aprobado por INVIMA
- Búsqueda de estudios clínicos o de literatura que evalúen lansoprazol en obstrucción duodenal, precisando qué causas (ulcerosa, inflamatoria o mecánica) podrían beneficiarse
- Análisis de interacciones farmacológicas y de compatibilidad de vías de administración

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Prevacid (lansoprazole) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=71ba78cb-7e46-43eb-9425-fa130f537f84) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

