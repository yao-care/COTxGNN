---
layout: default
title: Oxaprozin
parent: Solo Predicción del Modelo (L5)
nav_order: 488
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Oxaprozin: nueva indicación predicha, Displasia acromesomélica, tipo Hunter-Thompson (nivel de evidencia L5). Indicación original: OXAPROZIN"
monitor_inn: "oxaprozin"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "spondyloarthropathy, susceptibility to", "pseudoachondroplasia", "rheumatoid nodulosis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome"]
---

# Oxaprozin
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

## Oxaprozina: De Oxaprozina (AINE) a Displasia Acromesomélica tipo Hunter-Thompson
{: .text-alpha }

## Resumen en Una Frase

Oxaprozina es un antiinflamatorio no esteroideo (AINE) registrado en Colombia bajo la denominación "OXAPROZIN", cuyos registros sanitarios están actualmente cancelados.
El modelo TxGNN predice que podría ser efectivo para **displasia acromesomélica tipo Hunter-Thompson**, aunque actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección. La predicción se basa únicamente en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | OXAPROZIN (el registro no detalla la indicación; se trata de un AINE) |
| Nueva Indicación Predicha | Displasia acromesomélica, tipo Hunter-Thompson |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Por conocimiento general de la clase, la oxaprozina es un AINE que inhibe las enzimas COX-1 y COX-2 y reduce la síntesis de prostaglandinas, con efecto analgésico y antiinflamatorio.

La displasia acromesomélica tipo Hunter-Thompson es una displasia esquelética genética causada por pérdida de función en GDF5 (CDMP1). **No existe un vínculo mecanístico creíble**: la inhibición de COX no corrige el defecto de señalización de GDF5. El puntaje elevado probablemente refleja cercanía en la red de conocimiento con términos musculoesqueléticos y no un mecanismo terapéutico real. El único beneficio plausible sería el alivio sintomático del dolor articular.

### Otras predicciones del modelo (referencia)

Entre las diez primeras predicciones, las más coherentes clínicamente son:
- **Artritis idiopática juvenil poliarticular con factor reumatoide positivo** (99.67%, nivel L4): mecanísticamente plausible, ya que los AINE son terapia sintomática estándar, pero no son modificadores de la enfermedad (predominan FAME y biológicos). Es más un refinamiento de indicación que un reposicionamiento real.
- **Espondiloartropatía (susceptibilidad)** (99.93%, nivel L4): plausible por efecto de clase, pero se trata de un fenotipo de susceptibilidad y no de una enfermedad establecida.
- **Nodulosis reumatoide** (99.73%, nivel L4): relación indirecta con la artritis reumatoide; solo cabría un beneficio sintomático.

El resto (braquiolmia, síndrome braquiolmia-amelogénesis imperfecta, pseudoacondroplasia, miosclerosis, entre otras) no muestra vínculo creíble y parece un artefacto del grafo de conocimiento.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20069202 (cancelado) | PORTENER | Tableta cubierta con película | OXAPROZIN |
| 19937141 (cancelado) | DILOX® | Tableta recubierta | OXAPROZIN |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: hipertensión y trastornos hipertensivos, insuficiencia hepática, enfermedad renal, enfermedad ulcerosa péptica (incluida la activa), trastornos de la coagulación, infarto de miocardio, trombosis coronaria, enfermedad cardiovascular y cardíaca, hemoglobinopatía y piouréter.
- **Interacciones Farmacológicas**: se identificaron 190 interacciones en total. Entre las listadas:
  - *Moderadas*: ácido acetilsalicílico, corticosteroides (hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida), metformina, mesalazina, balsalazida, clorpropamida, acetohexamida, exenatida, fenfluramina, dexfenfluramina, citrato de potasio, ácido picosulfúrico y polietilenglicol con electrolitos.
  - *Leves*: famotidina, ranitidina y cimetidina.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal carece de ensayos, literatura y vínculo mecanístico creíble (nivel L5), y el fármaco no tiene registros vigentes en Colombia. El perfil de seguridad del grupo de los AINE (riesgo cardiovascular, gastrointestinal, renal y hepático) añade cautela frente a un beneficio solo sintomático.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA para obtener advertencias y contraindicaciones oficiales.
- Obtener datos del mecanismo de acción desde DrugBank.
- Si se desea explorar el área, priorizar la artritis idiopática juvenil poliarticular o las espondiloartropatías, que son más coherentes clínicamente, mediante revisión de literatura específica de oxaprozina.
- Evaluar la viabilidad práctica dada la cancelación de los registros sanitarios.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

