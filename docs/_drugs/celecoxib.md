---
layout: default
title: Celecoxib
parent: Solo Predicción del Modelo (L5)
nav_order: 146
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Celecoxib: nueva indicación predicha, Displasia acromesomélica, tipo Hunter-Thompson (nivel de evidencia L5). Indicación original: No especificada en los registros (solo figura \"Celecoxib\")"
monitor_inn: "CELECOXIB"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "hypermobility of coccyx", "brachyolmia", "rheumatoid nodulosis", "inflammatory spondylopathy", "WHIM syndrome"]
---

# Celecoxib
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

# Celecoxib: De Antiinflamatorio AINE (Inhibidor de COX-2) a Displasia Acromesomélica tipo Hunter-Thompson

## Resumen en Una Frase

Celecoxib es un antiinflamatorio no esteroideo (AINE) inhibidor selectivo de la COX-2, usado para el dolor y la inflamación. El registro sanitario colombiano solo menciona el nombre del principio activo, sin texto de indicación.
El modelo TxGNN predice que podría ser efectivo para la **displasia acromesomélica tipo Hunter-Thompson**, una enfermedad genética rara del esqueleto. Actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en los registros (solo figura "Celecoxib"); uso conocido como antiinflamatorio/analgésico |
| Nueva Indicación Predicha | Displasia acromesomélica, tipo Hunter-Thompson |
| Puntaje de Predicción TxGNN | 99.88% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 7 (todos cancelados) |
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

---

## Información de Mercado en Colombia

Los 7 registros sanitarios de celecoxib en Colombia figuran como **cancelados**. Actualmente no hay productos vigentes.

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
La predicción se basa solo en el modelo computacional (L5), sin ensayos clínicos, sin literatura y sin un vínculo mecanístico plausible con una enfermedad de origen genético. Además, todos los registros sanitarios en Colombia están cancelados.

**Para avanzar se necesita:**
- Un fundamento biológico que conecte la inhibición de COX-2 con la vía GDF5/BMP, mediante estudios preclínicos.
- Datos detallados del mecanismo de acción.
- Las advertencias y contraindicaciones del prospecto, y una nueva autorización sanitaria si se quisiera comercializar en Colombia.

**Nota:** Entre las otras predicciones del mismo análisis, la **espondilopatía inflamatoria** (espondiloartritis axial y espondilitis anquilosante) es la que cuenta con más respaldo. Reúne varios ensayos de Fase 3 y 4 completados con celecoxib, un ensayo aleatorizado publicado (CONSUL, PMID 38228361) y un nivel de evidencia L1 con recomendación "Proceed with Guardrails". Sin embargo, el celecoxib ya se usa en ese contexto, por lo que sería una confirmación de un uso establecido más que un reposicionamiento nuevo. Se recomienda evaluarla en un informe aparte.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

