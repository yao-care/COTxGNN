---
layout: default
title: Oxaprozin
parent: Solo Predicción del Modelo (L5)
nav_order: 488
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-12
monitor_inn: "oxaprozin"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "rheumatoid nodulosis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome"]
description: "Oxaprozin: nueva indicación predicha, Displasia acromesomélica, tipo Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type) (nivel de evidencia L5). Indicación original: OXAPROZIN"
---

# Oxaprozin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

## Oxaprozin: Displasia acromesomélica, tipo Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type)
{: .text-alpha }

## Resumen en Una Frase

Oxaprozina es un antiinflamatorio no esteroideo (AINE) registrado en Colombia bajo la denominación "OXAPROZIN".
El modelo TxGNN predice que podría ser efectivo para **displasia acromesomélica tipo Hunter-Thompson**, aunque actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección. La predicción se basa únicamente en el modelo.

<!-- review:begin co-lic-20261105-oxaprozin-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Oxaprozina es un antiinflamatorio no esteroideo (AINE) registrado en Colombia bajo la denominación "OXAPROZIN", cuyos registros sanitarios están actualmente cancelados." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 2 registros sanitarios (vigentes: 2); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-oxaprozin-1 -->

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | OXAPROZIN |
| Nueva Indicación Predicha | Displasia acromesomélica, tipo Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type) |
| Puntaje de Predicción TxGNN | 0.9998 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 2 de 2) |
| Número de Registros Sanitarios | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Por conocimiento general de la clase, la oxaprozina es un AINE que inhibe las enzimas COX-1 y COX-2 y reduce la síntesis de prostaglandinas, con efecto analgésico y antiinflamatorio.

La displasia acromesomélica tipo Hunter-Thompson es una displasia esquelética genética causada por pérdida de función en GDF5 (CDMP1). **No existe un vínculo mecanístico creíble**: la inhibición de COX no corrige el defecto de señalización de GDF5. El puntaje elevado probablemente refleja cercanía en la red de conocimiento con términos musculoesqueléticos y no un mecanismo terapéutico real. El único beneficio plausible sería el alivio sintomático del dolor articular.

### Otras predicciones del modelo (referencia)

Entre las diez primeras predicciones, las más coherentes clínicamente son:
- Es más un refinamiento de indicación que un reposicionamiento real.
- **Nodulosis reumatoide** (0.9973, nivel L4): relación indirecta con la artritis reumatoide; solo cabría un beneficio sintomático.

El resto (braquiolmia, síndrome braquiolmia-amelogénesis imperfecta, pseudoacondroplasia, miosclerosis, entre otras) no muestra vínculo creíble y parece un artefacto del modelo TxGNN (aprendizaje profundo).

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20069202 | PORTENER | Tableta cubierta con película | OXAPROZIN |
| 19937141 | DILOX® | Tableta recubierta | OXAPROZIN |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: hipertensión y trastornos hipertensivos, insuficiencia hepática, enfermedad renal, enfermedad ulcerosa péptica (incluida la activa), trastornos de la coagulación, infarto de miocardio, trombosis coronaria, enfermedad cardiovascular y cardíaca, hemoglobinopatía y piouréter.
- **Interacciones Farmacológicas**: se identificaron 190 interacciones en total. Entre las listadas:
  - *Moderadas*: ácido acetilsalicílico, corticosteroides (hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida), metformina, mesalazina, balsalazida, clorpropamida, acetohexamida, exenatida, fenfluramina, dexfenfluramina, citrato de potasio, ácido picosulfúrico y polietilenglicol con electrolitos.
  - *Leves*: famotidina, ranitidina y cimetidina.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal carece de ensayos, literatura y vínculo mecanístico creíble (nivel L5). El perfil de seguridad del grupo de los AINE (riesgo cardiovascular, gastrointestinal, renal y hepático) añade cautela frente a un beneficio solo sintomático.

<!-- review:begin co-lic-20261105-oxaprozin-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción principal carece de ensayos, literatura y vínculo mecanístico creíble (nivel L5), y el fármaco no tiene registros vigentes en Colombia." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 2 registros sanitarios (vigentes: 2); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-oxaprozin-2 -->

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA para obtener advertencias y contraindicaciones oficiales.
- Obtener datos del mecanismo de acción desde DrugBank.
- Si se desea explorar el área, priorizar la artritis idiopática juvenil poliarticular o las espondiloartropatías, que son más coherentes clínicamente, mediante revisión de literatura específica de oxaprozina.
- Evaluar la viabilidad práctica dada la cancelación de los registros sanitarios.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "cuyos registros sanitarios están actualmente cancelados" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "y el fármaco no tiene registros vigentes en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

