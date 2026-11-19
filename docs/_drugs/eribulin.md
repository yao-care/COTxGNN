---
layout: default
title: Eribulin
parent: Solo Predicción del Modelo (L5)
nav_order: 261
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-12
description: "Eribulin: nueva indicación predicha, Fiebre mediterránea familiar autosómica recesiva (nivel de evidencia L5). Indicación original: Eribulina"
monitor_inn: "eribulin"
predicted_indications: ["autosomal recessive familial Mediterranean fever", "dermatofibrosarcoma protuberans", "pleural mesothelioma", "malignant peritoneal mesothelioma", "pleural adenomatoid tumor", "pleural biphasic mesothelioma", "fibroblastic neoplasm", "pleural epithelioid mesothelioma", "heart fibrosarcoma"]
---

# Eribulin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Eribulina: De Agente Antineoplásico a Fiebre Mediterránea Familiar Autosómica Recesiva
{: .text-alpha }

## Resumen en Una Frase

Eribulina es un quimioterapéutico citotóxico que inhibe la dinámica de los microtúbulos y se utiliza en oncología, por ejemplo en liposarcoma irresecable o metastásico.
El modelo TxGNN predice que podría ser efectivo para la **fiebre mediterránea familiar autosómica recesiva**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección. La predicción se apoya solo en el modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Eribulina (el registro sanitario solo indica el nombre del principio activo, sin detalle de la indicación) |
| Nueva Indicación Predicha | Fiebre mediterránea familiar autosómica recesiva |
| Puntaje de Predicción TxGNN | 0.9982 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Eribulina es un inhibidor de la dinámica de los microtúbulos, análogo de la halicondrina. Bloquea el crecimiento de los microtúbulos, lo que detiene el ciclo celular en G2/M y provoca apoptosis. Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Eribulin (traducción no oficial): «La eribulina inhibe la fase de crecimiento de los microtúbulos sin afectar la fase de acortamiento y secuestra la tubulina en agregados no productivos. La eribulina ejerce sus efectos mediante un mecanismo antimitótico basado en la tubulina que conduce al bloqueo del ciclo celular en G 2 /M, a la desorganización de los husos mitóticos y, en última instancia, a la muerte celular por apoptosis tras un bloqueo mitótico prolongado.» Texto original en inglés: "Eribulin inhibits the growth phase of microtubules without affecting the shortening phase and sequesters tubulin into nonproductive aggregates. Eribulin exerts its effects via a tubulin-based antimitotic mechanism leading to G 2 /M cell-cycle block, disruption of mitotic spindles, and, ultimately, apoptotic cell death after prolonged mitotic blockage." ([DailyMed: Halaven (eribulin mesylate) prescribing information, Eisai Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=31ce4750-ded5-4a0b-95e9-f229fa6bc822), versión del 2025-11-07; consultado el 2026-11-19).

**La plausibilidad mecanística es débil.** La fiebre mediterránea familiar es una enfermedad autoinflamatoria causada por la desregulación del inflamasoma pirina (gen MEFV). Su tratamiento estándar es la colchicina, que también actúa sobre los microtúbulos. El puntaje alto del modelo probablemente refleja esa asociación de clase (agentes dirigidos a microtúbulos) y no una utilidad terapéutica real.

Además, la citotoxicidad de eribulina y su perfil de toxicidad (neutropenia, neuropatía) la hacen poco adecuada para una enfermedad inflamatoria crónica y benigna. No existen ensayos ni literatura que sustenten el uso.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

<!-- review:begin co-lic-20261105-eribulin-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Fabricante: BIOTOSCANA FARMA S.A. No hay registros vigentes en Colombia." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-eribulin-1 -->

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20147815 | HALAVEN ® | Solución inyectable | ERIBULINA |

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
La predicción no tiene ensayos clínicos ni literatura, y el mecanismo no es creíble para una enfermedad autoinflamatoria benigna. El perfil de toxicidad de eribulina (mielosupresión, neuropatía, riesgo de QT) desfavorece su uso crónico.

<!-- review:begin co-lic-20261105-eribulin-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "El perfil de toxicidad de eribulina (mielosupresión, neuropatía, riesgo de QT) desfavorece su uso crónico, y además el producto no tiene registro vigente en Colombia." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-eribulin-2 -->

**Para avanzar se necesita:**
- Evidencia preclínica o clínica que vincule eribulina con la vía pirina/inflamasoma, y una comparación con colchicina que justifique cualquier uso.
- Datos estructurados del mecanismo de acción y del prospecto (advertencias y contraindicaciones), cuya ausencia impide completar el cribado de seguridad.
- Revisar candidatos alternativos del mismo análisis. La **neoplasia fibroblástica** (puesto 8 del modelo, puntaje 0.9936) tiene mayor respaldo: un ensayo de Fase 2 completado (NCT03840772, ERASING, tumor fibroso solitario avanzado, n=16) y estudios preclínicos en fibrosarcoma. Su evidencia se clasifica como L2 y puede considerarse una pregunta de investigación, siempre que se verifiquen primero los resultados de eficacia.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Fabricante: BIOTOSCANA FARMA S.A. No hay registros vigentes en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "y además el producto no tiene registro vigente en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Halaven (eribulin mesylate) prescribing information, Eisai Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=31ce4750-ded5-4a0b-95e9-f229fa6bc822) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

