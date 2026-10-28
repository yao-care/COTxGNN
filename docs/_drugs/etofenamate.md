---
layout: default
title: Etofenamate
parent: Solo Predicción del Modelo (L5)
nav_order: 268
evidence_level: L5
indication_count: 9
monitor_inn: "Etofenamate"
predicted_indications: ["ankylosing spondylitis", "rheumatoid vasculitis", "hypermobility of coccyx", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "pseudoachondroplasia", "myosclerosis", "polyarticular juvenile rheumatoid arthritis", "Kummell disease"]
last_modified_at: 2026-10-28
description: "Etofenamate: nueva indicación predicha, Espondilitis anquilosante (nivel de evidencia L5). Indicación original: No especificada en el registro (el texto solo indica \"ETOFENAMATO\")"
---

# Etofenamate
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

## Etofenamato: De la indicación registrada (etofenamato) a Espondilitis Anquilosante
{: .text-alpha }

## Resumen en Una Frase

Etofenamato es un antiinflamatorio no esteroideo (AINE) del grupo de los fenamatos, comercializado en Colombia como solución inyectable; el texto de su registro sanitario solo indica el nombre del principio activo, sin detallar una indicación clínica.
El modelo TxGNN predice que podría ser efectivo para **espondilitis anquilosante**, pero no hay **ningún ensayo clínico** y solo **1 publicación** (un estudio farmacocinético) que no evalúa directamente esta enfermedad.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto solo indica "ETOFENAMATO") |
| Nueva Indicación Predicha | Espondilitis anquilosante |
| Puntaje de Prediccion TxGNN | 1.0000 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 1) |
| Número de registros sanitarios | Al menos 1 (la lista puede ser parcial) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este fármaco. Según la información conocida, etofenamato es un éster del ácido flufenámico, un AINE de la clase de los fenamatos que inhibe la ciclooxigenasa y reduce la inflamación mediada por prostaglandinas.

Los AINE son tratamiento sintomático de primera línea en la espondilitis anquilosante, por lo que, desde la lógica de clase, la predicción es plausible. Sin embargo, este razonamiento se infiere de la clase farmacológica y no de datos propios del fármaco.

La única publicación disponible demuestra que etofenamato alcanza suero y líquido sinovial humanos tras iontoforesis, lo que apoya la penetración tisular, pero no demuestra eficacia clínica en espondiloartritis axial. Por ello, el nivel de evidencia se limita a L5: ningún estudio citado evalúa directamente la espondilitis anquilosante.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [11455681](https://pubmed.ncbi.nlm.nih.gov/11455681/) | 2001 | Estudio farmacocinético | Arzneimittel-Forschung | En 11 pacientes con lumbalgia y 13 con sinovitis de rodilla, la iontoforesis de gel de etofenamato (equivalente a 100 mg diarios durante 5 días) permitió detectar el fármaco en suero y líquido sinovial. No evalúa eficacia en espondilitis anquilosante. |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20069025 | ETOFENAMATO 1G/2ML | Solución inyectable | ETOFENAMATO (el texto del registro no detalla indicación) |

La lista puede ser parcial: se registra al menos 1 registro sanitario.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. En los datos compilados no constan interacciones farmacológicas registradas ni relaciones de contraindicación en el grafo de conocimiento.

## Otras Predicciones del Modelo

| Enfermedad predicha | Puntaje TxGNN | Evidencia | Comentario |
|------|------|------|------|
| Vasculitis reumatoide | 1.0000 | L5 | Enfermedad sistémica tratada con inmunosupresores; un AINE no modificaría la enfermedad |
| Hipermovilidad del coxis | 1.0000 | L5 | Analgesia local plausible, sin datos clínicos |
| Displasia acromesomélica tipo Hunter-Thompson | 1.0000 | L5 | Sin vínculo mecanístico creíble |
| Síndrome braquiolmia-amelogénesis imperfecta | 1.0000 | L5 | Sin vínculo mecanístico creíble |
| Pseudoacondroplasia | 1.0000 | L5 | A lo sumo alivio sintomático articular |
| Miosclerosis | 1.0000 | L5 | Sin evidencia sobre fibrosis |
| Artritis idiopática juvenil poliarticular | 1.0000 | L5 | Plausible por clase, sin datos pediátricos |
| Enfermedad de Kummell | 1.0000 | L5 | No aborda la patología isquémica o mecánica |

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para espondilitis anquilosante es mecanísticamente plausible por pertenecer a la clase de los AINE, pero ningún ensayo ni publicación estudia directamente esta enfermedad con etofenamato; solo existe un estudio farmacocinético. El texto del registro colombiano tampoco especifica una indicación clínica.

**Para avanzar se necesita:**
- Estudios clínicos o revisiones que evalúen etofenamato en espondilitis anquilosante o espondiloartritis axial
- Datos del mecanismo de acción del fármaco
- Texto completo del prospecto aprobado por INVIMA (advertencias, contraindicaciones e indicaciones)
- Evaluación de la compatibilidad de vía de administración (la presentación registrada es inyectable, mientras que la publicación disponible usa gel por iontoforesis)
- Confirmar si existen registros sanitarios adicionales, ya que la lista puede ser parcial
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

