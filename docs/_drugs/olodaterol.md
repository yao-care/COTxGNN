---
layout: default
title: Olodaterol
parent: Evidencia Moderada (L3-L4)
nav_order: 305
evidence_level: L4
indication_count: 2
---

# Olodaterol
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **2** 
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

# Olodaterol: De EPOC a Bronquitis

## Resumen en Una Frase

Olodaterol es un broncodilatador beta2-agonista de acción prolongada (LABA), comercializado en Colombia en combinación con bromuro de tiotropio (Spiolto® Respimat®) y usado en la enfermedad pulmonar obstructiva crónica (EPOC).
El modelo TxGNN predice que podría ser efectivo para **bronquitis**,
pero solo hay **3 ensayos clínicos** y **2 publicaciones** relacionados, y ninguno evalúa la bronquitis como indicación propia (todos tratan la EPOC en general).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Olodaterol y bromuro de tiotropio (texto del registro INVIMA; no detalla la indicación explícitamente, aunque el uso establecido es EPOC) |
| Nueva Indicación Predicha | Bronquitis |
| Puntaje de Predicción TxGNN | 99.84% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 8 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos. Según la información conocida, olodaterol es un agonista selectivo de los receptores beta2-adrenérgicos de acción prolongada. Relaja el músculo liso de las vías respiratorias y produce broncodilatación sostenida. En Colombia se comercializa combinado con el antimuscarínico tiotropio.

La bronquitis crónica es un fenotipo dentro de la EPOC, por lo que existe un vínculo plausible: un broncodilatador eficaz en la EPOC podría aliviar la obstrucción en pacientes con bronquitis crónica.

Sin embargo, todos los estudios y publicaciones encontrados abordan la EPOC en su conjunto, no la bronquitis como indicación diferenciada. No hay evidencia directa para la bronquitis aguda, donde el beneficio de un broncodilatador no está demostrado. El puntaje tan alto del modelo (99.84%) probablemente refleja el solapamiento con la EPOC y es solo una predicción.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03333018](https://clinicaltrials.gov/study/NCT03333018) | N/A | Completado | 22155 | Estudio de utilización de aclidinio (otro fármaco) en usuarios nuevos con EPOC en Europa; relación solo tangencial con olodaterol |
| [NCT02850978](https://clinicaltrials.gov/study/NCT02850978) | N/A | Completado | 1335 | Vigilancia poscomercialización en Japón del uso prolongado de tiotropio + olodaterol en EPOC (bronquitis crónica, enfisema); observacional, aporta datos de seguridad y efectividad |
| [NCT05127304](https://clinicaltrials.gov/study/NCT05127304) | N/A | Completado | 11316 | Uso de recursos sanitarios y costos al iniciar tiotropio/olodaterol frente a fluticasona/umeclidinio/vilanterol en EPOC; sin evidencia de eficacia en bronquitis |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [27354040](https://pubmed.ncbi.nlm.nih.gov/27354040/) | 2016 | Revisión | Am J Health Syst Pharm | Revisión de la farmacología, farmacocinética, eficacia y seguridad de olodaterol, LABA de una dosis diaria, en EPOC |
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Guía/Revisión | Basic Clin Pharmacol Toxicol | Guía finlandesa de diagnóstico y farmacoterapia de la EPOC estable, orientada a atención primaria |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20082364 | SPIOLTO® RESPIMAT® (Boehringer Ingelheim International GmbH) | Solución para inhalación | Olodaterol y bromuro de tiotropio |

El Evidence Pack informa 8 registros en total, pero solo 5 entradas, todas con el mismo número de registro (20082364), por lo que se muestra una sola vez.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos ni literatura que evalúen la bronquitis como indicación propia; toda la evidencia corresponde a la EPOC, y el puntaje del modelo es solo una predicción. Además, el beneficio de un broncodilatador en la bronquitis aguda no está demostrado.

**Para avanzar se necesita:**
- Estudios clínicos o revisiones que evalúen específicamente la bronquitis crónica (y no solo la EPOC en general)
- Confirmar la indicación aprobada y la dosis en el prospecto de INVIMA, que hoy no está disponible en los datos
- Datos del mecanismo de acción desde DrugBank
- Información de advertencias y contraindicaciones del prospecto, para el cribado de seguridad (en particular, seguridad cardiovascular de los LABA)

**Nota:** Para el análisis de la EPOC (segunda predicción, con nivel de evidencia L1 y varios ensayos de Fase 3), se trataría de la confirmación de un uso ya establecido y no de un reposicionamiento real.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

