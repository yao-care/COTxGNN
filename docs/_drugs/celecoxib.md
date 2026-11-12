---
layout: default
title: Celecoxib
parent: Solo Predicción del Modelo (L5)
nav_order: 146
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-12
description: "Celecoxib: nueva indicación predicha, Displasia acromesomélica, tipo Hunter-Thompson (nivel de evidencia L5). Indicación original: No especificada en los registros (solo figura \"Celecoxib\")"
monitor_inn: "CELECOXIB"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "hypermobility of coccyx", "brachyolmia", "rheumatoid nodulosis", "WHIM syndrome"]
---

# Celecoxib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

## Celecoxib: De Antiinflamatorio AINE (Inhibidor de COX-2) a Displasia acromesomélica, tipo Hunter-Thompson
{: .text-alpha }

## Resumen en Una Frase

Celecoxib es un antiinflamatorio no esteroideo (AINE) inhibidor selectivo de la COX-2, usado para el dolor y la inflamación. El registro sanitario colombiano solo menciona el nombre del principio activo, sin texto de indicación.
El modelo TxGNN predice que podría ser efectivo para la **displasia acromesomélica tipo Hunter-Thompson**, una enfermedad genética rara del esqueleto. Actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en los registros (solo figura "Celecoxib"); uso conocido como antiinflamatorio/analgésico |
| Nueva Indicación Predicha | Displasia acromesomélica, tipo Hunter-Thompson |
| Puntaje de Predicción TxGNN | 0.9988 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 12 de 13) |
| Número de Registros Sanitarios | 13 (vigentes: 12) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Por el conocimiento general, celecoxib inhibe la enzima COX-2 y reduce la producción de prostaglandinas que median la inflamación y el dolor.

Sin embargo, la relación entre esa acción y la nueva indicación es débil. La displasia acromesomélica tipo Hunter-Thompson es una displasia esquelética rara causada por mutaciones de pérdida de función en el gen *CDMP1/GDF5*, que alteran la señalización de las proteínas morfogenéticas óseas (BMP). La inhibición de la COX-2 no corrige ese defecto genético.

**No se identificó un vínculo mecanístico creíble.** El puntaje alto del modelo es una predicción computacional sin respaldo en estudios clínicos ni en la literatura, y debe interpretarse con mucha cautela.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

<!-- review:begin co-lic-20261105-celecoxib-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Los 7 registros sanitarios de celecoxib en Colombia figuran como **cancelados**. Actualmente no hay productos vigentes." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 13 registros sanitarios (vigentes: 12); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-celecoxib-1 -->

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20193169 | SOSEDOL® | Cápsula dura | CELECOXIB |
| 19933716 | CELECOXIB 200 MG CÁPSULA (Laboratorios La Santé) | Cápsula dura | CELECOXIB |
| 20127514 | CELECOXIB 200 MG CÁPSULA (Genfar) | Cápsula dura | CELECOXIB |
| 20028796 | MIODAR® 200 MG CÁPSULAS | Cápsula dura | CELECOXIB |
| 19936110 | CEFINIX 200 MG CÁPSULA | Cápsula dura | CELECOXIB |

---

## Consideraciones de Seguridad

- **Contraindicaciones o condiciones de riesgo según el grafo de conocimiento** (no provienen del prospecto): hipertensión, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, insuficiencia cardíaca congestiva, úlcera péptica (incluida la activa), asma (intrínseca y alérgica), abuso o dependencia de sustancias, accidente cerebrovascular y enfermedad cerebrovascular, infarto cerebral, infarto de miocardio y trombosis coronaria, enfermedad cardiovascular y cardíaca, hemoglobinopatías y anemia (incluida la macrocítica), y piouréter.
- **Interacciones farmacológicas**: se identificaron 100 interacciones. Entre las listadas en los datos disponibles:
  - **Mayor**: eliglustat.
  - **Moderadas** (ejemplos): hidrocortisona, metformina, antidiabéticos orales como glimepirida, glipizida, glibenclamida, clorpropamida, acetohexamida y nateglinida, exenatida, mesalazina, balsalazida, olsalazina, cimetidina, levofloxacino, metronidazol, kanamicina, naltrexona, fenfluramina y dexfenfluramina.

No se dispone de las advertencias del prospecto. Consultar el prospecto para la información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo computacional TxGNN (aprendizaje profundo), sin ensayos clínicos, sin literatura y sin un vínculo mecanístico plausible con una enfermedad de origen genético. Además, el medicamento está comercializado en este país y cuenta con 12 registros sanitarios vigentes.

<!-- review:begin co-lic-20261112-celecoxib-1 -->

> **Corrección de revisión (2026-11-12)**: Texto original: "7 registros sanitarios vigentes" Corregido según los datos del INVIMA (Código Único de Medicamentos, datos al 2026-11-05): 13 registros sanitarios, de los cuales 12 vigentes y 1 vigentes pero temporalmente no comercializados. Las cifras actuales están en el Resumen rápido. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261112-celecoxib-1 -->

**Para avanzar se necesita:**
- Un fundamento biológico que conecte la inhibición de COX-2 con la vía GDF5/BMP, mediante estudios preclínicos.
- Datos detallados del mecanismo de acción.
- Las advertencias y contraindicaciones del prospecto, y una nueva autorización sanitaria si se quisiera comercializar en Colombia.

**Nota:** Entre las otras predicciones del mismo análisis, la **espondilopatía inflamatoria** (espondiloartritis axial y espondilitis anquilosante) es la que cuenta con más respaldo. Reúne varios ensayos de Fase 3 y 4 completados con celecoxib, un ensayo aleatorizado publicado (CONSUL, PMID 38228361) y un nivel de evidencia L1 con recomendación "Proceed with Guardrails". Sin embargo, el celecoxib ya se usa en ese contexto, por lo que sería una confirmación de un uso establecido más que un reposicionamiento nuevo. Se recomienda evaluarla en un informe aparte.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Los 7 registros sanitarios de celecoxib en Colombia figuran como **cancelados**. Actualmente no hay productos vigentes" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-12 | Número de registros vigentes: 7 → 12 | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

