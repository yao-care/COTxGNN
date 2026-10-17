---
layout: default
title: Finasteride
parent: Solo Predicción del Modelo (L5)
nav_order: 286
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Finasteride: nueva indicación predicha, Hipertricosis (la predicción de mayor puntaje fue Hipertricosis unive… (nivel de evidencia L5). Indicación original: Finasteride"
monitor_inn: "FINASTERIDE"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial isolated trichomegaly"]
---

# Finasteride
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Finasterida: De la indicación registrada (finasterida) a Hipertricosis

## Resumen en Una Frase

Finasterida es un inhibidor de la 5-alfa-reductasa tipo II, registrado en Colombia en tabletas orales, aunque el texto de indicación de los registros sanitarios solo repite el nombre del fármaco y no detalla la enfermedad aprobada.
El modelo TxGNN predice que podría ser efectivo para **Hipertricosis**, con **0 ensayos clínicos** y **4 publicaciones** de carácter general (revisiones y una herramienta de análisis del cabello) que solo ofrecen apoyo indirecto.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Finasteride (el registro no detalla la enfermedad; el texto solo repite el nombre del fármaco) |
| Nueva Indicación Predicha | Hipertricosis (la predicción de mayor puntaje fue Hipertricosis universal congénita tipo Ambras; se analiza la segunda por contar con literatura) |
| Puntaje de Predicción TxGNN | 99.99% (Hipertricosis); 99.99% (Ambras) |
| Nivel de Evidencia | L4 (Hipertricosis); L5 (Ambras) |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 4 (0 vigentes, 4 cancelados) |
| Decisión Recomendada | Hold |

**Nota sobre la selección:** la primera predicción por puntaje es la hipertricosis universal congénita tipo Ambras (99.994%), sin ningún ensayo ni publicación. Se presenta como foco la hipertricosis general (99.993%) porque es la única con literatura, aunque sea indirecta. Ambas se detallan abajo.

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, finasterida es un inhibidor de la 5-alfa-reductasa tipo II que reduce la dihidrotestosterona (DHT), y se usa en patologías dependientes de andrógenos, incluida la pérdida de cabello de patrón masculino.

La conexión con la hipertricosis es débil. La hipertricosis se define como un aumento del crecimiento del vello en zonas **no dependientes de andrógenos**, a diferencia del hirsutismo, que sí es dependiente de andrógenos y puede responder a la inhibición de la 5-alfa-reductasa. Por eso, un mecanismo antiandrogénico no es, en principio, el más adecuado. Las cuatro publicaciones encontradas (1999-2003) tratan de forma conjunta alopecia androgenética, hirsutismo e hipertricosis, y mencionan a finasterida en el contexto de enfermedades del cabello, pero los títulos y resúmenes no demuestran que se haya evaluado específicamente para hipertricosis.

En el caso de la hipertricosis tipo Ambras, se trata de una forma congénita rara asociada a reordenamientos genómicos que afectan la regulación de TRPS1, y su patogenia no es claramente androgeno-dependiente. La predicción es puramente computacional. Se debe revisar la literatura a nivel de resumen completo antes de subir el nivel de evidencia.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [12223963](https://pubmed.ncbi.nlm.nih.gov/12223963/) | 2002 | Revisión | Annales de Dermatologie et de Vénéréologie | Distingue hipertricosis (zonas no androgeno-dependientes; causas iatrogénicas, metabólicas, nutricionales o paraneoplásicas) de hirsutismo (zonas androgeno-dependientes); revisa evaluación y tratamiento |
| [10330884](https://pubmed.ncbi.nlm.nih.gov/10330884/) | 1999 | Revisión | Therapeutische Umschau | Repasa avances terapéuticos en alopecia androgenética e hirsutismo; el tratamiento oral de la alopecia de patrón masculino se discute en este marco |
| [12942187](https://pubmed.ncbi.nlm.nih.gov/12942187/) | 2003 | Revisión | Der Hautarzt | Describe finasterida para la pérdida de cabello de patrón masculino y láser para hipertricosis e hirsutismo; no la propone para hipertricosis |
| [12444520](https://pubmed.ncbi.nlm.nih.gov/12444520/) | 2002 | Metodología/tecnología | Der Hautarzt | Presenta TrichoScan, herramienta digital de análisis del cabello para medir respuesta al tratamiento; no evalúa eficacia de finasterida en hipertricosis |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20135117 | BINFIN® 5.0 MG TABLETA RECUBIERTA | Tableta recubierta | Finasteride | Cancelado |
| 20062982 | OPPTEST 5 MG TABLETAS RECUBIERTAS | Tableta recubierta | Finasterida | Cancelado |
| 19970940 | FINASTERIDE 5 MG | Tableta cubierta con película | Finasterida | Cancelado |
| 19981163 | FINASTERIDA 1 MG TABLETAS | Tableta recubierta | Finasteride | Cancelado |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (TxGNN/PrimeKG, no texto de prospecto)**: enfermedad hepática y enfermedad de la vesícula biliar.
- **Interacciones farmacológicas**: se identificaron 100 posibles interacciones en la consulta, todas con nivel de gravedad "Desconocido". Entre las primeras figuran calcitriol, doxiciclina, clotrimazol, dolasetrón, diciclomina, clorhexidina, famotidina, ácido acetilsalicílico, amoxicilina, bupropión, pantoprazol, glimepirida, mesalazina, acarbosa, morfina, metformina, omeprazol, sucralfato, palonosetrón y rosiglitazona. Sin clasificación de gravedad, no se puede valorar su relevancia clínica.
- **Desarrollo fetal**: los efectos conocidos de finasterida sobre el desarrollo genital masculino fetal suponen una preocupación de seguridad, en especial para indicaciones en contextos del desarrollo.

Consultar el prospecto para el resto de la información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto en TxGNN, pero no existen ensayos clínicos y la literatura es indirecta (revisiones generales, sin evaluación específica de finasterida en hipertricosis). Además, la hipertricosis es por definición independiente de andrógenos, lo que debilita la plausibilidad mecanística. Las demás predicciones (Ambras, síndromes malformativos, Dandy-Walker, anomalías del tallo piloso, tricomegalia familiar) son L5, sin evidencia y con base biológica débil o inexistente.

**Para avanzar se necesita:**
- Revisar los resúmenes completos de las publicaciones para confirmar si finasterida fue evaluada realmente en hipertricosis.
- Obtener datos de mecanismo de acción desde DrugBank para cruzar el vínculo mecanístico.
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones), pendiente y bloqueante para el tamizaje de seguridad.
- Aclarar la indicación aprobada de los registros, ya que los cuatro están cancelados y no hay producto vigente en Colombia.
- Clasificar la gravedad de las interacciones farmacológicas con una fuente que no devuelva "Desconocido".
- Evaluar la compatibilidad de vía de administración y la similitud con la indicación original, hoy pendientes.
- Valorar el riesgo en poblaciones pediátricas o en edad fértil antes de considerar cualquier indicación congénita.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

