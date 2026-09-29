---
layout: default
title: Mesalazine
parent: Solo Predicción del Modelo (L5)
nav_order: 277
evidence_level: L5
indication_count: 7
---

# Mesalazine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Mesalazina: De Colitis Ulcerosa a Hipotricosis Congénita con Distrofia Macular Juvenil

## Resumen en Una Frase

La mesalazina (5-ASA) es un antiinflamatorio aminosalicilato usado originalmente para tratar la colitis ulcerosa y otras enfermedades inflamatorias intestinales.
El modelo TxGNN predice que podría ser efectiva para **hipotricosis congénita con distrofia macular juvenil**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción: es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Colitis ulcerosa (según datos de farmacología; el texto del registro INVIMA solo indica «Mesalazina») |
| Nueva Indicación Predicha | Hipotricosis congénita con distrofia macular juvenil |
| Puntaje de Predicción TxGNN | 99.65% (posición 3412 en el ranking del modelo) |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la mesalazina es el componente activo de la sulfasalazina y se usa para tratar la colitis ulcerosa activa, prevenir recaídas y manejar otras enfermedades inflamatorias intestinales como la enfermedad de Crohn. La base de datos de farmacología asocia el fármaco con el receptor PPARγ (gen *PPARG*), pero esto no explica por sí solo un efecto en la nueva indicación.

La hipotricosis congénita con distrofia macular juvenil es una enfermedad genética rara que afecta el cabello y la retina. No guarda una relación clínica ni mecanística evidente con las enfermedades inflamatorias intestinales.

No se identificó ningún vínculo mecanístico. El puntaje alto de TxGNN proviene únicamente de la estructura del grafo de conocimiento y no de estudios reales. Por eso debe interpretarse como una hipótesis sin respaldo, no como un indicio de eficacia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Otras Indicaciones Predichas con Evidencia Disponible

Aunque la indicación principal no tiene evidencia, el modelo predijo otras indicaciones con algo de respaldo. Ninguna supera el nivel L4.

**Osteoartritis** (puntaje 99.63%, L4, recomendación: pregunta de investigación). Solo hay evidencia preclínica:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38310093](https://pubmed.ncbi.nlm.nih.gov/38310093/) | 2024 | Preclínico (in vitro/animal) | Nature Communications | El 5-ASA suprime la osteoartritis a través del eje OSCAR-PPARγ |
| [38491514](https://pubmed.ncbi.nlm.nih.gov/38491514/) | 2024 | Análisis computacional/transcriptómico | Journal of Translational Medicine | Identificación de dianas terapéuticas en osteoartritis mediante datos transcriptómicos y perfiles de expresión inducidos por fármacos |
| [1673814](https://pubmed.ncbi.nlm.nih.gov/1673814/) | 1991 | Estudio mecanístico in vitro | Wiener Klinische Wochenschrift | La sulfasalazina y sus metabolitos modifican la liberación de prostaglandinas y leucotrienos en tejido sinovial humano |

**Artritis reumatoide** (puntaje 99.57%, L4, Hold). La evidencia existente corresponde a la sulfasalazina, no a la mesalazina. El ensayo de Fase 3 [NCT02930343](https://clinicaltrials.gov/study/NCT02930343) (136 pacientes, terminado anticipadamente) comparó combinaciones de FAME basadas en sulfasalazina. Además, el estudio [2860942](https://pubmed.ncbi.nlm.nih.gov/2860942/) (BMJ, 1985) indica que el componente activo en artritis reumatoide es la sulfapiridina, mientras que el 5-ASA mostró solo un efecto débil. Esto va en contra de trasladar el beneficio de la sulfasalazina a la mesalazina.

## Información de Mercado en Colombia

Se consolidaron los registros repetidos (el 19999923 aparecía cuatro veces con datos idénticos). El registro sanitario indica solo el nombre del principio activo, sin texto de indicación.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20065382 | MESILAX® | Suspensión para administrar por vía rectal | Mesalazina |
| 19999923 | MESAX 500 MG TABLETAS | Tableta con cubierta entérica con película | Mesalazina |

Según el registro, el fármaco también se presenta en gránulos y en tabletas con recubrimiento entérico. En total hay 20 registros sanitarios.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: La consulta se completó, pero el único resultado es una asociación farmacológica con el receptor PPARγ (diana), no una interacción medicamentosa con relevancia clínica.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación predicha no tiene ensayos clínicos ni literatura, y no se identificó ningún vínculo mecanístico (nivel L5). El puntaje alto de TxGNN proviene solo del grafo de conocimiento y no basta para avanzar.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA para completar advertencias y contraindicaciones (brecha de datos que bloquea la evaluación de seguridad)
- Completar los datos del mecanismo de acción desde DrugBank
- Definir una hipótesis biológica que conecte la mesalazina con la hipotricosis congénita con distrofia macular juvenil y buscar evidencia preclínica
- Si se busca una línea con más sustento, priorizar la osteoartritis (evidencia preclínica del eje OSCAR-PPARγ) como pregunta de investigación
- Confirmar la compatibilidad de vías de administración, hoy pendiente

*Este informe es solo de referencia para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

