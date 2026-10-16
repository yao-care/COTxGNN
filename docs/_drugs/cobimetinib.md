---
layout: default
title: Cobimetinib
parent: Solo Predicción del Modelo (L5)
nav_order: 177
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Cobimetinib: nueva indicación predicha, Esclerosis lateral amiotrófica (nivel de evidencia L5). Indicación original: No especificada en el registro"
monitor_inn: "cobimetinib"
predicted_indications: ["amyotrophic lateral sclerosis", "bilateral parasagittal parieto-occipital polymicrogyria", "axial spondylometaphyseal dysplasia", "Mills syndrome", "amyotrophic lateral sclerosis, susceptibility to", "lower motor neuron syndrome with late-adult onset", "trichomegaly-retina pigmentary degeneration-dwarfism syndrome", "lethal arthrogryposis-anterior horn cell disease syndrome", "amyotrohpic lateral sclerosis type 22", "monomelic amyotrophy"]
---

# Cobimetinib
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

# Cobimetinib: De Indicación Original No Especificada a Esclerosis Lateral Amiotrófica

## Resumen en Una Frase

Cobimetinib es un inhibidor de MEK1/2 (según la farmacología conocida) que cuenta con un registro sanitario en Colombia, actualmente cancelado. El modelo TxGNN predice que podría ser efectivo para **esclerosis lateral amiotrófica (ELA)**, con **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto de indicación del registro sanitario solo indica "COBIMETINIB") |
| Nueva Indicación Predicha | Esclerosis lateral amiotrófica |
| Puntaje de Predicción TxGNN | 99.73% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 1 (0 vigentes, 1 cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción del fármaco. Según la farmacología conocida, cobimetinib es un inhibidor de MEK1/2 que bloquea la vía MAPK/ERK, y se emplea en oncología por vía oral.

La vía MAPK/ERK se ha vinculado con la neuroinflamación y las respuestas de estrés de las motoneuronas en modelos de ELA, por lo que existe una relación plausible pero no validada. El puntaje alto de TxGNN es solo una predicción computacional y no hay ensayos ni literatura que la respalden.

Hay un factor que debilita el argumento: la penetración de cobimetinib a través de la barrera hematoencefálica es limitada (es sustrato de la glicoproteína P), lo que reduce la razón de ser en el sistema nervioso central.

Las otras nueve predicciones principales corresponden a enfermedades raras, en su mayoría trastornos de motoneurona (síndrome de Mills, ELA tipo 22, síndrome de motoneurona inferior de inicio tardío, amiotrofia monomélica, entre otras) y a síndromes del desarrollo o esqueléticos sin vínculo mecanístico claro (como la polimicrogiria parieto-occipital parasagital bilateral y la displasia espondilometafisaria axial). Varias parecen reflejar cercanía en el grafo de conocimiento más que una justificación farmacológica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20119351 (cancelado) | COTELLIC® (COBIMETINIB) 20 MG TABLETAS RECUBIERTAS | Tableta recubierta | COBIMETINIB |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de MEK1/2) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar el prospecto; por la toxicidad conocida de la clase MEK, considerar examen oftalmológico, CK, función cardíaca (fracción de eyección), función hepática y vigilancia dermatológica |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 266 interacciones. Entre las de nivel **Mayor** figuran aprepitant, dexametasona, claritromicina, cobicistat y lexidronam de samario (153Sm). Entre las de nivel **Moderado** figuran cimetidina, clotrimazol, eliglustat, metreleptina, miconazol, naltrexona, rolapitant, troglitazona, deferasirox, palifermina, cloruro de estroncio Sr-89, fostamatinib, ticagrelor, quinina e ivacaftor.
- **Toxicidades de clase a considerar** (según el análisis de las predicciones): retinopatía serosa, erupción cutánea, diarrea, elevación de CK/rabdomiólisis y cardiomiopatía. La toxicidad retiniana preocupa especialmente en el síndrome de tricomegalia-degeneración pigmentaria retiniana-enanismo, y la toxicidad muscular en enfermedades neuromusculares como la amiotrofia monomélica.

No se dispone de advertencias ni contraindicaciones del prospecto; consultar el prospecto para esa información.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para ELA se basa solo en el modelo (nivel L5), sin ensayos ni literatura, con penetración limitada al sistema nervioso central y un perfil de toxicidad relevante para enfermedades neuromusculares. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Revisión sistemática de la literatura preclínica sobre inhibición de MEK/ERK en modelos de ELA
- Datos de mecanismo de acción y de penetración en el sistema nervioso central (barrera hematoencefálica, glicoproteína P)
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones)
- Aclarar la situación regulatoria del registro cancelado y la viabilidad de comercialización en Colombia
- Evaluación de la relación riesgo-beneficio (retinopatía, CK, toxicidad cardíaca) en poblaciones con ELA
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

