---
layout: default
title: Tipiracil
parent: Solo Predicción del Modelo (L5)
nav_order: 628
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Tipiracil: nueva indicación predicha, Adenoma velloso del ciego (nivel de evidencia L5). Indicación original: Trifluridina y tipiracilo"
monitor_inn: "tipiracil"
predicted_indications: ["cecum villous adenoma", "lipoma of colon", "rectosigmoid junction neoplasm", "cecum neuroendocrine tumor G1", "colonic lymphangioma", "cecal disease", "colon leiomyoma", "benign neoplasm of cecum", "cavernous hemangioma of colon", "colorectal gastrointestinal stromal tumor"]
---

# Tipiracil
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

# Tipiracilo: De Trifluridina y Tipiracilo a Adenoma Velloso del Ciego

## Resumen en Una Frase

Tipiracilo es un componente de la combinación trifluridina/tipiracilo (LONSURF®), utilizada originalmente en el tratamiento del cáncer colorrectal metastásico.
El modelo TxGNN predice que podría ser efectivo para **adenoma velloso del ciego**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección específica.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trifluridina y tipiracilo (el registro sanitario no detalla la patología) |
| Nueva Indicación Predicha | Adenoma velloso del ciego |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registro vigente) |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, tipiracilo es un inhibidor de la timidina fosforilasa que se combina con trifluridina (un análogo de nucleósido citotóxico). Al inhibir la degradación de trifluridina, tipiracilo aumenta su exposición. La combinación se usa en cáncer colorrectal metastásico y está en evaluación en cáncer gástrico metastásico.

La relación con la nueva indicación es lejana: el adenoma velloso del ciego es una lesión premaligna del colon, anatómicamente cercana al cáncer colorrectal. Sin embargo, los adenomas se manejan con resección endoscópica, no con quimioterapia sistémica, por lo que no existe una justificación clínica sólida para usar el fármaco.

El puntaje tan alto del modelo probablemente refleja la proximidad en el grafo de conocimiento con el cáncer colorrectal, más que un vínculo mecanístico real. Debe interpretarse con cautela.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20245134 (cancelado) | LONSURF® (trifluridina 20 mg + tipiracilo 8,19 mg) | Tableta cubierta con película | Trifluridina y tipiracilo |

El fabricante es Les Laboratoires Servier. No existe actualmente ningún registro vigente en Colombia.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (análogo de nucleósido/antimetabolito, combinado con un inhibidor de la timidina fosforilasa) |
| Riesgo de Mielosupresión | Alto (según la clase del fármaco; la literatura recuperada describe leucopenia y neutropenia como efectos adversos de la combinación) |
| Clasificación de Emetogenicidad | Baja a moderada (según la clase del fármaco) |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 14 registros de interacción. Trece son de gravedad moderada: cimetidina, tafenoquina, ketoconazol, brigatinib, crizotinib, encorafenib, etinilestradiol, lenvatinib, acetato de medroxiprogesterona, acetato de megestrol, ribociclib, rucaparib y vandetanib. El registro restante es una interacción farmacológica con la proteína no estructural 15 de coronavirus (SARS-CoV-2), sin nivel de gravedad asignado.
- **Reporte de caso**: se describió vasculitis leucocitoclástica con púrpura de Henoch-Schönlein de aparición tardía tras el tratamiento con trifluridina/tipiracilo en un paciente con cáncer apendicular metastásico.

No se dispone de advertencias ni contraindicaciones del prospecto. Consultar el prospecto para el resto de la información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (L5), sin ensayos clínicos ni literatura específica. Además, el adenoma velloso se maneja con resección endoscópica, por lo que la quimioterapia sistémica citotóxica carece de justificación clínica y presenta un perfil de riesgo desfavorable. El producto tampoco cuenta con registro vigente en Colombia.

**Para avanzar se necesita:**
- Obtener el prospecto con advertencias y contraindicaciones (brecha de seguridad que bloquea el avance).
- Datos detallados del mecanismo de acción.
- Evidencia preclínica o clínica específica en adenomas colónicos.
- Valorar si otras predicciones del listado (p. ej., neoplasia de la unión rectosigmoidea, que probablemente corresponde a la indicación original de cáncer colorrectal) merecen priorizarse.
- Confirmar la situación regulatoria del producto en Colombia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

