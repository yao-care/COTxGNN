---
layout: default
title: Iodixanol
parent: Solo Predicción del Modelo (L5)
nav_order: 351
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Iodixanol: nueva indicación predicha, Susceptibilidad a osteoartritis (nivel de evidencia L5). Indicación original: IODIXANOL"
monitor_inn: "IODIXANOL"
predicted_indications: ["osteoarthritis susceptibility", "osteoarthritis", "rheumatoid arthritis"]
---

# Iodixanol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Iodixanol: De Medio de Contraste Radiográfico a Susceptibilidad a Osteoartritis

## Resumen en Una Frase

Iodixanol es un medio de contraste yodado, no iónico e iso-osmolar, utilizado en imagenología diagnóstica; en Colombia su registro sanitario no especifica una indicación detallada.
El modelo TxGNN predice que podría ser efectivo para **susceptibilidad a osteoartritis**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección para esa indicación.
La predicción se basa únicamente en el modelo, sin estudios terapéuticos reales.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | IODIXANOL (el registro no detalla la indicación; uso conocido como medio de contraste radiográfico) |
| Nueva Indicación Predicha | Susceptibilidad a osteoartritis |
| Puntaje de Predicción TxGNN | 99.16% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo cancelado (sin registros vigentes) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, iodixanol es un medio de contraste yodado, no iónico e iso-osmolar, que se usa para visualizar estructuras en estudios de imagen. No tiene una farmacología conocida que modifique enfermedades.

La "susceptibilidad" a osteoartritis es un concepto genético o de riesgo, y un agente de contraste no tiene una vía plausible para alterarla. Por ello, no se ha establecido un vínculo mecanístico. Aunque el puntaje del modelo es muy alto (0.99), se trata de una predicción basada en el grafo de conocimiento, y probablemente es un artefacto de cercanía en ese grafo.

Las otras dos predicciones del modelo tienen puntajes similares, pero tampoco cuentan con respaldo terapéutico:

- **Osteoartritis (99.07%)**: se encontraron 5 publicaciones, todas sobre iodixanol como herramienta de imagen o sonda experimental, no como tratamiento. Incluyen imagenología por tomografía de cartílago con difusión de nanopartículas, modelos de transporte de solutos en la interfaz osteocondral, tomografía de conteo de fotones con doble contraste y un estudio *in vitro* que indica que los contrastes yodados no afectan la función del plasma rico en plaquetas. Esto muestra utilidad diagnóstica en la investigación de la osteoartritis, no un efecto terapéutico.
- **Artritis reumatoide (99.00%)**: solo hay un reporte de caso sobre desensibilización a otro contraste yodado (iohexol), que no aporta evidencia de actividad antirreumática.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Para la indicación principal (susceptibilidad a osteoartritis) actualmente no hay literatura relacionada disponible. Como referencia, se presenta la literatura de la predicción cercana de osteoartritis; todos los estudios son preclínicos, de imagen o de modelado, no terapéuticos:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39012563](https://pubmed.ncbi.nlm.nih.gov/39012563/) | 2024 | Estudio preclínico de imagen | Annals of Biomedical Engineering | Imagenología por TC con difusión de nanopartículas para evaluar la función del cartílago articular |
| [27793406](https://pubmed.ncbi.nlm.nih.gov/27793406/) | 2016 | Modelo computacional | Journal of Biomechanics | Modelo de elementos finitos del transporte de solutos neutros a través de la interfaz osteocondral |
| [40155520](https://pubmed.ncbi.nlm.nih.gov/40155520/) | 2025 | Estudio preclínico de imagen | Annals of Biomedical Engineering | Agente de doble contraste en TC de conteo de fotones para evaluar la salud del cartílago |
| [28063646](https://pubmed.ncbi.nlm.nih.gov/28063646/) | 2017 | Estudio ex vivo/computacional | Journal of Biomechanics | Uso de iodixanol como contraste difusor para estudiar la permeabilidad de la interfaz osteocondral |
| [30374787](https://pubmed.ncbi.nlm.nih.gov/30374787/) | 2018 | Estudio in vitro | Journal of Experimental Orthopaedics | Los contrastes yodados no alteran la función del plasma rico en plaquetas en etapas tempranas |
| [36628042](https://pubmed.ncbi.nlm.nih.gov/36628042/) | 2022 | Reporte de caso | Cureus | Desensibilización a iohexol en una paciente con amiloidosis secundaria a artritis reumatoide (otra molécula; sin evidencia antirreumática) |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20155256 (cancelado) | IODIXANOL SOLUCION INYECTABLE | Solución inyectable | IODIXANOL |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. Las principales, de nivel **Mayor**, incluyen:
  - Metformina
  - Anfotericina B (incluidas las formulaciones lipídica, de sulfato de colesterilo y liposomal)
  - Mesalazina, balsalazida, olsalazina y sulfasalazina
  - Vancomicina
  - Aminoglucósidos: kanamicina, neomicina y estreptomicina
  - Polimixina B

  Con nivel **Moderado** figura el manitol. Otras interacciones (famotidina, ácido acetilsalicílico, morfina, omeprazol, prednisona) tienen nivel desconocido.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Aunque el puntaje de TxGNN es muy alto, no existe ningún ensayo clínico ni literatura terapéutica que lo respalde, y no hay un mecanismo plausible por el cual un medio de contraste modifique la susceptibilidad a la osteoartritis. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y una hipótesis biológica que justifique un efecto terapéutico
- Evidencia preclínica que demuestre un efecto sobre el cartílago o la progresión de la osteoartritis (más allá de su uso como herramienta de imagen)
- Información de seguridad del prospecto (advertencias y contraindicaciones), actualmente no disponible
- Evaluación de la vía de administración y de la viabilidad regulatoria, dado que no hay registros vigentes en Colombia
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

