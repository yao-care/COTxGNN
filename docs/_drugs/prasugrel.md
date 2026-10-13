---
layout: default
title: Prasugrel
parent: Solo Predicción del Modelo (L5)
nav_order: 527
evidence_level: L5
indication_count: 10
---

# Prasugrel
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

# Prasugrel: De Indicación Original (Prasugrel) a Hipertensión Pulmonar

## Resumen en Una Frase

Prasugrel es un antiagregante plaquetario de la clase de las tienopiridinas (antagonista del receptor P2Y12), comercializado en Colombia como EFFIENT® 10 MG; el texto de indicación del registro sanitario solo dice "PRASUGREL", sin detallar la enfermedad.
El modelo TxGNN predice que podría ser efectivo para **hipertensión pulmonar**, pero **no hay ensayos clínicos** y solo **2 publicaciones** poco relacionadas, por lo que la evidencia es únicamente computacional.
La predicción con mayor respaldo indirecto entre las 10 candidatas es **migraña** (2 ensayos clínicos de contexto y 2 estudios en tienopiridinas), que se comenta en la conclusión.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | PRASUGREL (el registro no detalla la enfermedad; el uso conocido es la prevención de eventos aterotrombóticos) |
| Nueva Indicación Predicha | Hipertensión pulmonar |
| Puntaje de Predicción TxGNN | 99.88% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registro vigente) |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, prasugrel es una tienopiridina que inhibe el receptor plaquetario P2Y12 y, con ello, la agregación plaquetaria. Su eficacia se ha establecido en el contexto cardiovascular, y mecanísticamente podría ser aplicable a la hipertensión pulmonar.

La relación con la nueva indicación es teórica: la activación plaquetaria y la trombosis in situ participan en el remodelado vascular pulmonar. Sin embargo, no hay datos directos que respalden el uso de prasugrel en esta enfermedad.

Las dos publicaciones recuperadas tratan sobre la adherencia a clopidogrel en síndrome coronario agudo y sobre la terapia de base en comorbilidades y mortalidad por COVID-19. Ninguna evalúa prasugrel en hipertensión pulmonar, por lo que no refuerzan la hipótesis.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para hipertensión pulmonar.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [21241206](https://pubmed.ncbi.nlm.nih.gov/21241206/) | 2011 | Cohorte | Current Medical Research and Opinion | Factores asociados con el uso y la adherencia a clopidogrel tras intervención coronaria percutánea en síndrome coronario agudo; no evalúa hipertensión pulmonar. |
| [34713782](https://pubmed.ncbi.nlm.nih.gov/34713782/) | 2021 | Cohorte | Kardiologiia | Influencia de la terapia de base previa a la infección sobre el riesgo de muerte por COVID-19 (registro ACTIVE); no evalúa prasugrel en hipertensión pulmonar. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20006437 (cancelado) | EFFIENT® 10 MG | Tableta recubierta | PRASUGREL |

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento (no provienen del prospecto):** insuficiencia hepática, trastornos hipotensivos, enfermedades de la coagulación, accidente cerebrovascular y trastornos cerebrovasculares, susceptibilidad a infarto cerebral isquémico, infarto cerebral, lesiones (traumatismos), púrpura trombocitopénica, hemorragia intracraneal, ataque isquémico transitorio e insuficiencia vertebrobasilar.
- **Interacciones farmacológicas:** se identificaron 191 interacciones en total; las más relevantes entre las listadas son:
  - **Mayor:** deferasirox, ibritumomab tiuxetán.
  - **Moderada:** morfina, ácido acetilsalicílico, opio, fenfluramina, dexfenfluramina, sibutramina.
  - **Menor:** antiácidos y antiulcerosos como famotidina, ranitidina, cimetidina, nizatidina y los inhibidores de la bomba de protones (omeprazol, esomeprazol, lansoprazol, dexlansoprazol, pantoprazol, rabeprazol); también bupropión.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para hipertensión pulmonar solo existe una predicción del modelo (L5), sin ensayos clínicos ni literatura pertinente. Además, no hay registro sanitario vigente en Colombia y el perfil de riesgo hemorrágico es relevante. Entre las demás candidatas, la migraña (L3) cuenta con un contexto clínico más sólido (ensayo de fase 3 en curso sobre terapia dirigida al foramen oval permeable, y estudios retrospectivos y piloto con tienopiridinas), pero con evidencia indirecta y no específica de prasugrel; se sugiere tratarla como pregunta de investigación.

**Para avanzar se necesita:**
- Obtener los datos del mecanismo de acción desde DrugBank.
- Obtener y analizar el prospecto del INVIMA (advertencias y contraindicaciones), indispensable para el cribado de seguridad.
- Aclarar la situación del registro cancelado (EFFIENT® 10 MG) y la disponibilidad real del fármaco en Colombia.
- Realizar estudios preclínicos o clínicos de prasugrel en hipertensión pulmonar antes de considerar cualquier avance.
- Evaluar de forma prioritaria la migraña asociada a foramen oval permeable, verificando si prasugrel forma parte de algún brazo del ensayo NCT07629635 y valorando un estudio específico con prasugrel.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

