---
layout: default
title: Ketoprofen
parent: Solo Predicción del Modelo (L5)
nav_order: 367
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-12
description: "Ketoprofen: nueva indicación predicha, Displasia acromesomélica, tipo Hunter-Thompson (nivel de evidencia L5). Indicación original: Ketoprofeno"
monitor_inn: "ketoprofen"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "WHIM syndrome", "juvenile arthritis due to defect in LACC1"]
---

# Ketoprofen
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

## Ketoprofeno: De Ketoprofeno (indicación registrada) a Displasia acromesomélica, tipo Hunter-Thompson
{: .text-alpha }

## Resumen en Una Frase

Ketoprofeno es un antiinflamatorio no esteroideo.
El modelo TxGNN predice que podría ser efectivo para **displasia acromesomélica tipo Hunter-Thompson**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata de una predicción puramente computacional.

<!-- review:begin co-lic-20261105-ketoprofen-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Ketoprofeno es un antiinflamatorio no esteroideo (AINE) registrado en Colombia bajo la indicación genérica "ketoprofeno" en su único registro sanitario, hoy cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 12 registros sanitarios (vigentes: 11); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-ketoprofen-1 -->

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Ketoprofeno (el texto del registro no detalla una indicación clínica específica) |
| Nueva Indicación Predicha | Displasia acromesomélica, tipo Hunter-Thompson |
| Puntaje de Predicción TxGNN | 0.9998 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 11 de 12) |
| Número de Registros Sanitarios | 12 (vigentes: 11) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Por conocimiento general, el ketoprofeno es un AINE que inhibe de forma no selectiva la COX-1 y la COX-2, reduciendo la síntesis de prostaglandinas, con efecto analgésico y antiinflamatorio.

La displasia acromesomélica tipo Hunter-Thompson es un trastorno esquelético causado por mutaciones de pérdida de función en CDMP1/GDF5, que alteran la condrogénesis. La inhibición de la COX no corrige de forma plausible el defecto subyacente en la señalización BMP/GDF.

En consecuencia, el puntaje alto proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no un respaldo biológico. **No se identificó un mecanismo establecido que justifique esta predicción.**

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
| 20158718 | BICERTO® 150 MG (75 MG de liberación inmediata + 75 MG de liberación prolongada) | Tableta de liberación modificada (oral) | KETOPROFENO | Vigente |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** hipertensión y trastornos hipertensivos, insuficiencia hepática, enfermedad renal, úlcera péptica (incluida la activa), trastornos de la coagulación, infarto de miocardio, trombosis coronaria, enfermedad cardiovascular y cardíaca, hemoglobinopatías y piouréter.
- **Interacciones farmacológicas:** se identificaron 226 interacciones. Entre las de nivel moderado se encuentran ácido acetilsalicílico, corticoides (hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona), metformina, mesalazina, balsalazida, glimepirida, clorpropamida, naltrexona y sales de potasio. Las de nivel menor incluyen famotidina, ranitidina, cimetidina y linaclotida.

No se dispone de advertencias ni contraindicaciones del prospecto; se recomienda consultarlo.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción carece de ensayos, literatura y plausibilidad mecanística (nivel L5). No hay base para avanzar.

<!-- review:begin co-lic-20261105-ketoprofen-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción carece de ensayos, literatura y plausibilidad mecanística (nivel L5), y el único registro sanitario en Colombia está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 12 registros sanitarios (vigentes: 11); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-ketoprofen-2 -->

**Para avanzar se necesita:**
- Datos del mecanismo de acción y un vínculo biológico creíble entre la inhibición de COX y la señalización CDMP1/GDF5.
- Advertencias y contraindicaciones del prospecto del INVIMA.
- Evidencia preclínica o clínica específica de ketoprofeno en esta indicación.

**Nota sobre otras predicciones:** entre las 10 predicciones, solo dos tienen una plausibilidad indirecta, basada en el uso de los AINE como clase en cuadros inflamatorios (nivel L4, "pregunta de investigación"): *susceptibilidad a espondiloartropatía* (puntaje 0.9986) y *artritis juvenil por defecto en LACC1* (0.9974). Ninguna cuenta con ensayos ni literatura específicos de ketoprofeno. El resto (displasias esqueléticas, miosclerosis, síndrome WHIM, entre otras) no tiene vínculo mecanístico plausible.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "(AINE) registrado en Colombia bajo la indicación genérica "ketoprofeno" en su único registro sanitario, hoy cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "y el único registro sanitario en Colombia está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

