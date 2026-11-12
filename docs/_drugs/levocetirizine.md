---
layout: default
title: Levocetirizine
parent: Solo Predicción del Modelo (L5)
nav_order: 398
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-12
description: "Levocetirizine: nueva indicación predicha, Artritis reumatoide (nivel de evidencia L5). Indicación original: LEVOCETIRIZINA"
monitor_inn: "Levocetirizine"
predicted_indications: ["rheumatoid arthritis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome"]
---

# Levocetirizine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Levocetirizina: De Levocetirizina (indicación sin detallar) a Artritis Reumatoide
{: .text-alpha }

## Resumen en Una Frase

Levocetirizina es un antihistamínico antagonista selectivo del receptor H1, registrado en Colombia bajo el nombre del principio activo, sin que el texto de indicación aprobado detalle la enfermedad específica.
El modelo TxGNN predice que podría ser efectivo para **artritis reumatoide**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; es solo una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | LEVOCETIRIZINA (el registro no especifica una enfermedad; se usa como antihistamínico) |
| Nueva Indicación Predicha | Artritis reumatoide |
| Puntaje de Predicción TxGNN | 0.9973 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 3 de 3) |
| Número de Registros Sanitarios | 3 (vigentes: 3) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este reporte no incluyen información detallada sobre el mecanismo de acción. Según la información conocida, levocetirizina es un antagonista selectivo del receptor H1 de histamina, y su uso establecido es el control de síntomas alérgicos. Mecanísticamente, podría ser aplicable a la artritis reumatoide de forma limitada.

La histamina está presente en la sinovial reumatoide y podría contribuir a la permeabilidad vascular, a la inflamación mediada por mastocitos y a la modulación de citocinas. Por eso, un vínculo mecanístico es plausible. Sin embargo, el bloqueo H1 no es un mecanismo establecido de modificación de la enfermedad en artritis reumatoide.

El puntaje alto de TxGNN (0.9973) es solo una predicción del modelo. No hay ensayos ni literatura que respalden la relación, por lo que la plausibilidad biológica no se puede verificar con los datos disponibles.

**Otras predicciones del modelo (sin sustento mecanístico aparente):**

| Posición | Enfermedad predicha | Puntaje TxGNN | Comentario |
|------|------|------|------|
| 2 | Síndrome de microftalmía colobomatosa-displasia rizomélica | 0.9959 | Trastorno del desarrollo de causa genética; no hay vínculo claro con el bloqueo H1 |
| 3 | Síndrome de braquidactilia-sindactilia | 0.9952 | Malformación congénita de las extremidades; un antihistamínico sintomático no modificaría una anomalía estructural |

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
| 20126402 | RIZIN® TABLETAS | Tableta recubierta | LEVOCETIRIZINA | Vigente |
| 20232631 | Levocetirizina diclorhidrato 5 mg tabletas recubiertas | Tableta recubierta | LEVOCETIRIZINA | Vigente |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** enfermedad renal, piouréter, enfermedad renal crónica, síndrome de insuficiencia renal crónica e insuficiencia renal terminal.
- **Interacciones farmacológicas:** se identificaron 100 interacciones, casi todas de nivel moderado (una de nivel menor). Entre las principales:
  - Depresores del sistema nervioso central y opioides: morfina (incluida la liposomal), fentanilo, dihidrocodeína, opio, difenoxina, difenoxilato, loperamida.
  - Otros fármacos sedantes o con efecto central: etanol, prometazina, clorfeniramina, dronabinol, nabilona.
  - Otros: bupropión, metoclopramida, sibutramina, histamina, yoduro I-131, yoduro I-123 (moderadas) e hialuronidasa (menor).

Para advertencias y contraindicaciones del prospecto, consultar el prospecto del producto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para artritis reumatoide se basa solo en el modelo (L5), sin ensayos clínicos ni literatura. Además, el bloqueo H1 no es un mecanismo establecido de modificación de la enfermedad en esta patología.

<!-- review:begin co-lic-20261105-levocetirizine-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, en Colombia no hay registros sanitarios vigentes para levocetirizina, y el bloqueo H1 no es un mecanismo establecido de modificación de la enfermedad en esta patología." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 3 registros sanitarios (vigentes: 3); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-levocetirizine-2 -->

**Para avanzar se necesita:**
- Revisión de literatura y ensayos sobre antihistamínicos H1 en artritis reumatoide, o estudios preclínicos y de mecanismo.
- Datos detallados del mecanismo de acción desde DrugBank.
- Prospecto de INVIMA con advertencias y contraindicaciones, necesario para el tamizaje de seguridad.
- Evaluar la compatibilidad de la vía de administración (actualmente solo forma oral) y la seguridad en pacientes con enfermedad renal.

<!-- review:begin co-lic-20261031-levocetirizine-1 -->

> **Corrección de revisión (2026-10-31)**: Texto original: "Aclarar la situación regulatoria (registros cancelados) y la viabilidad de comercialización en Colombia. / Evaluar la compatibilidad de la vía de administración (actualmente solo forma oral) y la seguridad en pacientes con enfermedad renal." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-10-31. El medicamento tiene 3 registros sanitarios (vigentes: 3); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261031-levocetirizine-1 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-10-31 | Eliminado: "Aclarar la situación regulatoria (registros cancelados) y la viabilidad de comercialización en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "en Colombia no hay registros sanitarios vigentes para levocetirizina, y" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

