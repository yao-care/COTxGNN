---
layout: default
title: Levothyroxine
parent: Solo Predicción del Modelo (L5)
nav_order: 402
evidence_level: L5
indication_count: 4
monitor_inn: "levothyroxine"
predicted_indications: ["renal hypodysplasia/aplasia", "bilateral renal agenesis", "Potter sequence", "Carney complex"]
last_modified_at: 2026-10-28
description: "Levothyroxine: nueva indicación predicha, Hipodisplasia/aplasia renal (nivel de evidencia L5). Indicación original: Levotiroxina de sodio"
---

# Levothyroxine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

## Levotiroxina: De Levotiroxina de sodio (indicación registrada) a Hipodisplasia/aplasia renal
{: .text-alpha }

## Resumen en Una Frase

Levotiroxina (levotiroxina de sodio) es una hormona tiroidea sintética que cuenta en Colombia con un registro sanitario vigente de INVIMA, cuyo texto de indicación solo indica el nombre del principio activo.
El modelo TxGNN predice que podría ser efectiva para **hipodisplasia/aplasia renal**, pero **no existen ensayos clínicos ni publicaciones** en los datos compilados que respalden esta dirección; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Levotiroxina de sodio (el registro no detalla la indicación clínica) |
| Nueva Indicación Predicha | Hipodisplasia/aplasia renal |
| Puntaje de Predicción TxGNN | 0.9967 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 1) |
| Número de Registros Sanitarios | Al menos 1 (la lista puede ser parcial) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la levotiroxina es un reemplazo de la hormona tiroidea, y la hormona tiroidea participa en el desarrollo y la función normal del riñón.

Sin embargo, no se establece un vínculo mecanístico directo. La hipodisplasia/aplasia renal es una malformación estructural congénita, generalmente causada por variantes genéticas (por ejemplo, PAX2, HNF1B, RET) que alteran la nefrogénesis. La levotiroxina administrada después del nacimiento no cabría esperar que restaure tejido renal ausente o displásico.

El puntaje alto (0.9967) es solo una predicción del modelo TxGNN (aprendizaje profundo), sin respaldo de ensayos ni literatura. Otras predicciones del mismo modelo (aplasia renal bilateral, secuencia de Potter) pueden reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica ni un blanco terapéutico tratable. La cuarta predicción, el complejo de Carney, tiene solo un vínculo indirecto débil con el eje tiroideo y tampoco cuenta con evidencia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

La lista proviene de un recuento parcial; pueden existir más registros.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19992452 | EUTIROX® 150 MCG | Tableta (vía oral) | Levotiroxina de sodio |

## Consideraciones de Seguridad

- **Relaciones de contraindicación registradas en el grafo de conocimiento** (no provienen del texto del prospecto): hipertensión y trastornos hipertensivos; hipopituitarismo y deficiencias hormonales hipofisarias (incluido el síndrome de Sheehan); hipogonadismo hipogonadotrópico y síndrome de Kallmann; deficiencia aislada de hormona de crecimiento; osteoporosis y osteoporosis posmenopáusica; diabetes mellitus y cetoacidosis diabética; enfermedad coronaria e infarto de miocardio; enfermedad del timo.
- **Interacciones farmacológicas**: se identificaron 666 interacciones. Entre las listadas, la mayoría son de nivel moderado:
  - Antidiabéticos: acarbosa, metformina, pioglitazona, alogliptina, albiglutida, dulaglutida, canagliflozina, dapagliflozina, empagliflozina, clorpropamida.
  - Inhibidores de la bomba de protones: omeprazol, rabeprazol, dexlansoprazol.
  - Sales de calcio y magnesio: fosfato de calcio, acetato de calcio, óxido de magnesio.
  - Otros: epinefrina, isometepteno, dietilpropión.
  - Cimetidina: interacción de nivel menor.

Consultar el prospecto para las advertencias y contraindicaciones oficiales, que no se pudieron obtener para este informe.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ensayos clínicos ni publicaciones que la respalden (nivel L5), y la biología de una malformación renal congénita estructural no sugiere que la levotiroxina pueda corregirla. El puntaje alto del modelo no sustituye la evidencia real.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones).
- Obtener datos del mecanismo de acción desde DrugBank.
- Revisión sistemática de literatura que evalúe un posible papel de la hormona tiroidea en el desarrollo renal y en estas malformaciones.
- Evidencia preclínica o clínica que sustente un beneficio en la indicación predicha antes de reconsiderar la decisión.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

