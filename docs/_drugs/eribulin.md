---
layout: default
title: Eribulin
parent: Solo Predicción del Modelo (L5)
nav_order: 261
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Eribulin: nueva indicación predicha, Fiebre mediterránea familiar autosómica recesiva (nivel de evidencia L5). Indicación original: Eribulina"
monitor_inn: "eribulin"
predicted_indications: ["autosomal recessive familial Mediterranean fever", "dermatofibrosarcoma protuberans", "pleural mesothelioma", "malignant peritoneal mesothelioma", "pleural adenomatoid tumor", "pleural biphasic mesothelioma", "fibroblastic neoplasm", "pleural epithelioid mesothelioma", "heart fibrosarcoma"]
---

# Eribulin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Eribulina: De Agente Antineoplásico a Fiebre Mediterránea Familiar Autosómica Recesiva

## Resumen en Una Frase

Eribulina es un quimioterapéutico citotóxico que inhibe la dinámica de los microtúbulos y se utiliza en oncología, por ejemplo en liposarcoma irresecable o metastásico.
El modelo TxGNN predice que podría ser efectivo para la **fiebre mediterránea familiar autosómica recesiva**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección. La predicción se apoya solo en el modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Eribulina (el registro sanitario solo indica el nombre del principio activo, sin detalle de la indicación) |
| Nueva Indicación Predicha | Fiebre mediterránea familiar autosómica recesiva |
| Puntaje de Predicción TxGNN | 99.82% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados (sin registro vigente) |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Eribulina es un inhibidor de la dinámica de los microtúbulos, análogo de la halicondrina. Bloquea el crecimiento de los microtúbulos, lo que detiene el ciclo celular en G2/M y provoca apoptosis. Los datos de mecanismo de acción no están disponibles en el campo estructurado, por lo que esta descripción proviene del análisis de la relación mecanística.

**La plausibilidad mecanística es débil.** La fiebre mediterránea familiar es una enfermedad autoinflamatoria causada por la desregulación del inflamasoma pirina (gen MEFV). Su tratamiento estándar es la colchicina, que también actúa sobre los microtúbulos. El puntaje alto del modelo probablemente refleja esa asociación de clase (agentes dirigidos a microtúbulos) y no una utilidad terapéutica real.

Además, la citotoxicidad de eribulina y su perfil de toxicidad (neutropenia, neuropatía) la hacen poco adecuada para una enfermedad inflamatoria crónica y benigna. No existen ensayos ni literatura que sustenten el uso.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20147815 (cancelado) | HALAVEN ® | Solución inyectable | ERIBULINA |

Fabricante: BIOTOSCANA FARMA S.A. No hay registros vigentes en Colombia.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (inhibidor de microtúbulos / antimitótico) |
| Riesgo de Mielosupresión | Alto (la neutropenia y la trombocitopenia figuran entre las contraindicaciones del grafo de conocimiento) |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial (neutrófilos y plaquetas), electrolitos (potasio), función hepática y renal, ECG por riesgo de prolongación del QT, signos de neuropatía periférica |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

- **Condiciones asociadas a contraindicación (grafo de conocimiento TxGNN, no texto de prospecto):** síndrome de QT largo (incluido el familiar), trombocitopenia, deficiencia de potasio, neutropenia, agranulocitosis, enfermedad del sistema nervioso periférico, neuropatía periférica y estreñimiento.
- **Interacciones farmacológicas:** se identificaron 375 interacciones. Entre las principales:
  - **Mayores:** dolasetrón y cisaprida.
  - **Moderadas:** ondansetrón, palonosetrón, claritromicina, levofloxacino, metronidazol, tinidazol, famotidina, loperamida, rosuvastatina, simvastatina, y varios laxantes y preparaciones de limpieza intestinal (bisacodilo, ácido picosulfúrico, polietilenglicol, lactulosa, lactitol, sulfato de sodio, aceite de ricino).

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ensayos clínicos ni literatura, y el mecanismo no es creíble para una enfermedad autoinflamatoria benigna. El perfil de toxicidad de eribulina (mielosupresión, neuropatía, riesgo de QT) desfavorece su uso crónico, y además el producto no tiene registro vigente en Colombia.

**Para avanzar se necesita:**
- Evidencia preclínica o clínica que vincule eribulina con la vía pirina/inflamasoma, y una comparación con colchicina que justifique cualquier uso.
- Datos estructurados del mecanismo de acción y del prospecto (advertencias y contraindicaciones), cuya ausencia impide completar el cribado de seguridad.
- Revisar candidatos alternativos del mismo análisis. La **neoplasia fibroblástica** (puesto 8 del modelo, puntaje 99.36%) tiene mayor respaldo: un ensayo de Fase 2 completado (NCT03840772, ERASING, tumor fibroso solitario avanzado, n=16) y estudios preclínicos en fibrosarcoma. Su evidencia se clasifica como L2 y puede considerarse una pregunta de investigación, siempre que se verifiquen primero los resultados de eficacia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

