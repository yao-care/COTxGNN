---
layout: default
title: Metformin
parent: Solo Predicción del Modelo (L5)
nav_order: 434
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-12
description: "Metformin: nueva indicación predicha, Síndrome de la persona rígida clásico (nivel de evidencia L5). Indicación original: METFORMINA"
monitor_inn: "Metformin"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy"]
---

# Metformin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Metformina: De Metformina (indicación sin detallar) a Síndrome de la Persona Rígida Clásico
{: .text-alpha }

## Resumen en Una Frase

Metformina está registrada en Colombia con una indicación aprobada que solo figura como "METFORMINA", sin detalle de la enfermedad tratada.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de la persona rígida clásico**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | METFORMINA (el registro sanitario no detalla la enfermedad; el texto aprobado solo repite el nombre del fármaco) |
| Nueva Indicación Predicha | Síndrome de la persona rígida clásico |
| Puntaje de Predicción TxGNN | 0.9945 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 20) |
| Número de Registros Sanitarios | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Metformin (traducción no oficial): «La metformina es un antihiperglucemiante que mejora la tolerancia a la glucosa en pacientes con diabetes mellitus de tipo 2 y reduce tanto la glucosa plasmática basal como la posprandial. La metformina disminuye la producción hepática de glucosa, disminuye la absorción intestinal de glucosa y mejora la sensibilidad a la insulina al aumentar la captación y la utilización periféricas de glucosa.» Texto original en inglés: "Metformin is an antihyperglycemic agent which improves glucose tolerance in patients with type 2 diabetes mellitus, lowering both basal and postprandial plasma glucose. Metformin decreases hepatic glucose production, decreases intestinal absorption of glucose, and improves insulin sensitivity by increasing peripheral glucose uptake and utilization." ([DailyMed: Metformin Hydrochloride Er (metformin hydrochloride) prescribing information, Leading Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3dca884d-ec44-496f-9eeb-31fd8fa3f574), versión del 2026-09-21; consultado el 2026-11-19). Según la información conocida, metformina es un antidiabético oral cuya acción se asocia a la activación de AMPK, y podría tener efectos inmunomoduladores de forma especulativa.

El síndrome de la persona rígida es un trastorno neurológico autoinmune, típicamente asociado a anticuerpos anti-GAD65, con alteración de la señalización GABAérgica. No se ha establecido un vínculo mecanístico directo con metformina. Además, este síndrome suele coexistir con diabetes tipo 1, lo cual es un factor de confusión y no una evidencia a favor.

El puntaje alto (0.994) es solo una predicción computacional. La variante "síndrome de la extremidad rígida focal" tiene exactamente el mismo puntaje, lo que sugiere que la predicción proviene de la similitud entre nodos de enfermedad y no de evidencia independiente.

**Otras predicciones del modelo (todas L5, sin evidencia, recomendación Hold):**

| Enfermedad | Puntaje TxGNN | Comentario |
|------|------|------|
| Síndrome de la extremidad rígida focal | 0.9945 | Variante del espectro de la persona rígida; misma justificación especulativa |
| Opsismodisplasia | 0.9940 | Displasia esquelética por mutaciones en INPPL1; posible solapamiento especulativo en rutas PI3K/AKT/mTOR |
| Síndrome de disfunción sensible a tiamina | 0.9940 | Metformina solo podría aliviar el componente diabético; además se asocia a alteración de vitamina B12 |
| Lipodistrofia localizada inducida por fármacos | 0.9906 | Racional indirecto por uso en otras lipodistrofias; sin evidencia para la forma localizada |

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20235551 | WILMETINA 500 MG TABLETAS RECUBIERTAS | Tableta recubierta | METFORMINA | Vigente |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** insuficiencia hepática y enfermedad hepática, enfermedad renal, pancreatitis, enfermedad de la vesícula biliar, insuficiencia cardíaca congestiva, insuficiencia adrenocortical, enfermedad del timo, piouréter, y diversos déficits hipofisarios e hipogonadismos hipogonadotróficos (incluido el síndrome de Kallmann y el síndrome de Sheehan).
- **Interacciones farmacológicas:** se identificaron 100 interacciones; entre las mostradas, las de nivel **mayor** son:
  - Acetazolamida
  - Etanol (alcohol)

  Entre las de nivel moderado se encuentran dolutegravir, abemaciclib, fenilefrina, ranitidina, formoterol, pseudoefedrina, ketorolaco, nifedipino, epinefrina, ibuprofeno, etinilestradiol, hidrocortisona, salbutamol, hidroclorotiazida y acetohexamida.
- Las advertencias y contraindicaciones del prospecto no están disponibles; consultar el prospecto para esa información.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo computacional (nivel L5), sin ensayos clínicos, literatura ni vínculo mecanístico establecido. Además, la indicación original no está detallada.

<!-- review:begin co-lic-20261105-metformin-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, el único registro sanitario en Colombia está cancelado y la indicación original no está detallada." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-metformin-1 -->

**Para avanzar se necesita:**
- Obtener y analizar el prospecto del INVIMA (advertencias y contraindicaciones), requisito para la evaluación de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Buscar y verificar literatura preclínica o clínica sobre metformina en síndrome de la persona rígida (considerando el sesgo por la comorbilidad con diabetes tipo 1).
- Aclarar la indicación original aprobada y la situación regulatoria actual.
- Evaluar la compatibilidad de vías de administración y la similitud con la indicación original (actualmente pendientes).

<!-- review:begin co-lic-20261105-metformin-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Aclarar la indicación original aprobada y la situación regulatoria actual, dado que no hay registros vigentes." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-metformin-2 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "el único registro sanitario en Colombia está cancelado y" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "dado que no hay registros vigentes" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Metformin Hydrochloride Er (metformin hydrochloride) prescribing information, Leading Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3dca884d-ec44-496f-9eeb-31fd8fa3f574) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

