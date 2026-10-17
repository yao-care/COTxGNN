---
layout: default
title: Metformin
parent: Solo Predicción del Modelo (L5)
nav_order: 434
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
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

# Metformina: De Metformina (indicación sin detallar) a Síndrome de la Persona Rígida Clásico

## Resumen en Una Frase

Metformina está registrada en Colombia con una indicación aprobada que solo figura como "METFORMINA", sin detalle de la enfermedad tratada.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de la persona rígida clásico**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | METFORMINA (el registro sanitario no detalla la enfermedad; el texto aprobado solo repite el nombre del fármaco) |
| Nueva Indicación Predicha | Síndrome de la persona rígida clásico |
| Puntaje de Predicción TxGNN | 99.45% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, metformina es un antidiabético oral cuya acción se asocia a la activación de AMPK, y podría tener efectos inmunomoduladores de forma especulativa.

El síndrome de la persona rígida es un trastorno neurológico autoinmune, típicamente asociado a anticuerpos anti-GAD65, con alteración de la señalización GABAérgica. No se ha establecido un vínculo mecanístico directo con metformina. Además, este síndrome suele coexistir con diabetes tipo 1, lo cual es un factor de confusión y no una evidencia a favor.

El puntaje alto (0.994) es solo una predicción computacional. La variante "síndrome de la extremidad rígida focal" tiene exactamente el mismo puntaje, lo que sugiere que la predicción proviene de la similitud entre nodos de enfermedad y no de evidencia independiente.

**Otras predicciones del modelo (todas L5, sin evidencia, recomendación Hold):**

| Enfermedad | Puntaje TxGNN | Comentario |
|------|------|------|
| Síndrome de la extremidad rígida focal | 99.45% | Variante del espectro de la persona rígida; misma justificación especulativa |
| Opsismodisplasia | 99.40% | Displasia esquelética por mutaciones en INPPL1; posible solapamiento especulativo en rutas PI3K/AKT/mTOR |
| Síndrome de disfunción sensible a tiamina | 99.40% | Metformina solo podría aliviar el componente diabético; además se asocia a alteración de vitamina B12 |
| Lipodistrofia localizada inducida por fármacos | 99.06% | Racional indirecto por uso en otras lipodistrofias; sin evidencia para la forma localizada |

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
| 20235551 | WILMETINA 500 MG TABLETAS RECUBIERTAS | Tableta recubierta | METFORMINA | Cancelado |

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
La predicción se basa solo en el modelo computacional (nivel L5), sin ensayos clínicos, literatura ni vínculo mecanístico establecido. Además, el único registro sanitario en Colombia está cancelado y la indicación original no está detallada.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto del INVIMA (advertencias y contraindicaciones), requisito para la evaluación de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Buscar y verificar literatura preclínica o clínica sobre metformina en síndrome de la persona rígida (considerando el sesgo por la comorbilidad con diabetes tipo 1).
- Aclarar la indicación original aprobada y la situación regulatoria actual, dado que no hay registros vigentes.
- Evaluar la compatibilidad de vías de administración y la similitud con la indicación original (actualmente pendientes).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

