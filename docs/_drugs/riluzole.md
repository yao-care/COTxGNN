---
layout: default
title: Riluzole
parent: Solo Predicción del Modelo (L5)
nav_order: 562
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Riluzole: nueva indicación predicha, Polimicrogiria parieto-occipital parasagital bilateral (nivel de evidencia L5). Indicación original: RILUZOL"
---

# Riluzole
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Riluzol: De Esclerosis Lateral Amiotrófica a Polimicrogiria Parieto-occipital Parasagital Bilateral

## Resumen en Una Frase

Riluzol es un fármaco con registros sanitarios en Colombia, cuyo texto de indicación aprobada figura solo como "RILUZOL". Se conoce por su uso en la esclerosis lateral amiotrófica (ELA).
El modelo TxGNN predice que podría ser efectivo para **polimicrogiria parieto-occipital parasagital bilateral**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción. Se trata de una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | RILUZOL (el registro no detalla la indicación; el texto coincide con el nombre del principio activo) |
| Nueva Indicación Predicha | Polimicrogiria parieto-occipital parasagital bilateral |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 5 (todos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, el riluzol modula la transmisión glutamatérgica y reduce la excitotoxicidad, y se utiliza como neuroprotector en la ELA.

Para esta predicción concreta, el vínculo mecanístico es débil. La polimicrogiria es una malformación del desarrollo cortical, de carácter estructural, y es poco probable que responda a un agente neuroprotector sintomático. El análisis disponible considera que el puntaje alto probablemente es un artefacto de proximidad en el grafo de conocimiento y no refleja una relación biológica demostrada.

Por tanto, la predicción no cuenta con respaldo mecanístico ni clínico. Debe tratarse como una señal del modelo que requiere validación independiente antes de cualquier inversión adicional.

### Otras predicciones del modelo

Entre las 10 principales predicciones, las más coherentes biológicamente son las relacionadas con enfermedad de motoneurona, por su cercanía con la ELA:

| Enfermedad predicha | Puntaje TxGNN | Evidencia | Recomendación |
|------|------|------|------|
| ELA, susceptibilidad a | 99.98% | L4 (solo revisiones y estudios mecanísticos; reetiquetado de la indicación original) | Pregunta de investigación |
| Síndrome de motoneurona inferior de inicio tardío en adultos | 99.99% | L5 | Pregunta de investigación |
| Amiotrofia monomélica | 99.99% | L5 | Pregunta de investigación |
| Síndrome de Mills | 99.98% | L5 | Pregunta de investigación |
| ELA tipo 22 | 99.98% | L5 | Pregunta de investigación |

El resto (displasia espondilometafisaria axial, síndrome de tricomegalia-degeneración pigmentaria de la retina-enanismo, síndrome letal de artrogriposis-enfermedad de células del asta anterior, miopatía mitocondrial autosómica dominante) no muestra un vínculo mecanístico claro y se recomienda mantenerlos en espera (Hold).

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para la polimicrogiria parieto-occipital parasagital bilateral.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal predicha.

Como referencia, para la predicción de ELA (puesto 8) se compilaron publicaciones, sobre todo revisiones y estudios mecanísticos:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [9178165](https://pubmed.ncbi.nlm.nih.gov/9178165/) | 1997 | Revisión | Journal of Neurology | Hipótesis del glutamato y excitotoxicidad en la ELA, base del mecanismo del riluzol |
| [21128691](https://pubmed.ncbi.nlm.nih.gov/21128691/) | 2011 | Revisión | CNS Drugs | Fisiopatología, diagnóstico y manejo de la ELA; el riluzol es el único fármaco que prolonga modestamente la supervivencia |
| [16723044](https://pubmed.ncbi.nlm.nih.gov/16723044/) | 2006 | Revisión | Expert Reviews in Molecular Medicine | Mecanismos propuestos en la ELA: estrés oxidativo, excitotoxicidad, disfunción mitocondrial |
| [22763933](https://pubmed.ncbi.nlm.nih.gov/22763933/) | 2012 | Revisión | Praxis | Diagnóstico y tratamiento de la ELA |
| [42161327](https://pubmed.ncbi.nlm.nih.gov/42161327/) | 2026 | Cohorte | Brain | Variantes de CYP2D6 en ELA y su asociación con riesgo y supervivencia; el beneficio del riluzol varía entre pacientes |
| [8061281](https://pubmed.ncbi.nlm.nih.gov/8061281/) | 1994 | Preclínico | Neuroreport | Efecto neuroprotector del riluzol frente a la toxicidad del LCR de pacientes con ELA |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20080854 | RILUZOL 50 MG TABLETAS (Actifarma) | Tableta | RILUZOL (cancelado) |
| 20254040 | DOLVIO 50 (Alkem Laboratories) | Tableta recubierta | RILUZOL (cancelado) |
| 20201114 | RILUZOL 50 MG TABLETAS (Actifarma) | Tableta | RILUZOL (cancelado) |
| 206956 | RILUTEK® TABLETAS X 50MG (Sanofi-Aventis) | Tableta recubierta | RILUZOL (cancelado) |
| 20204277 | TEGLUTIK® SUSPENSIÓN ORAL 5 MG/ML (Italfarmaco) | Suspensión oral | RILUZOL (cancelado) |

Los cinco registros están cancelados; actualmente no hay ningún registro vigente.

---

## Consideraciones de Seguridad

- **Contraindicaciones y condiciones de riesgo según el grafo de conocimiento** (relaciones fármaco-enfermedad del grafo PrimeKG, no texto del prospecto): neutropenia, agranulocitosis, abuso o dependencia de sustancias, hiperbilirrubinemia (incluida la hereditaria), síndrome de Gilbert, enfermedad pulmonar intersticial y lesión hepática inducida por fármacos.
- **Interacciones farmacológicas**: se identificaron 44 interacciones. Entre las de nivel moderado figuran: ácido obeticólico, naltrexona, deferasirox, osilodrostat, anagrelida, asparaginasa de *E. coli*, brentuximab vedotina, clofarabina, metotrexato y epirrubicina. Entre las de nivel menor: omeprazol, cafeína, teofilina y aminofilina.
- **Función hepática**: una publicación compilada (PMID 32040174) señala que alrededor del 50 % de los pacientes con ELA que toman riluzol oral presentan ALT por encima del límite superior normal, 8 % por encima de 3× y 2 % por encima de 5×. Se recomienda vigilancia hepática.

Para advertencias y contraindicaciones del prospecto, consultar el prospecto del producto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal (polimicrogiria parieto-occipital parasagital bilateral) carece de ensayos clínicos y de literatura, y no tiene un vínculo mecanístico plausible; el puntaje alto probablemente es un artefacto del modelo. Además, no hay registros sanitarios vigentes en Colombia.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) del riluzol desde DrugBank.
- Información de advertencias y contraindicaciones del prospecto en INVIMA, requisito para el tamizaje de seguridad.
- Priorizar la evaluación de las predicciones en enfermedades de motoneurona (síndrome de motoneurona inferior de inicio tardío, amiotrofia monomélica, síndrome de Mills, ELA tipo 22) mediante revisión sistemática y búsqueda de estudios específicos.
- Aclarar la situación regulatoria: confirmar por qué los cinco registros están cancelados y si hay interés en una nueva solicitud.
- Plan de monitoreo hepático y hematológico para cualquier estudio futuro.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

