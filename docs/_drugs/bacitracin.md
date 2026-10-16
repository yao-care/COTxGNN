---
layout: default
title: Bacitracin
parent: Solo Predicción del Modelo (L5)
nav_order: 88
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Bacitracin: nueva indicación predicha, Queratoconjuntivitis epitelial punteada (nivel de evidencia L5). Indicación original: Dexametasona y antiinfecciosos"
monitor_inn: "bacitracin"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "exposure keratitis", "non-human animal disease", "otitis externa", "postinfectious vasculitis", "post-bacterial disorder", "infective urethral stricture", "post-infectious syndrome", "infection-related hemolytic uremic syndrome", "Chagas cardiomyopathy"]
---

# Bacitracin
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

# Bacitracina: De Dexametasona y Antiinfecciosos a Queratoconjuntivitis Epitelial Punteada

## Resumen en Una Frase

La bacitracina es un antibiótico polipeptídico de uso tópico, registrado en Colombia en una pomada oftálmica combinada con dexametasona y antiinfecciosos.
El modelo TxGNN predice que podría ser efectiva para **queratoconjuntivitis epitelial punteada**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción específica; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dexametasona y antiinfecciosos |
| Nueva Indicación Predicha | Queratoconjuntivitis epitelial punteada |
| Puntaje de Predicción TxGNN | 99.999% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo cancelado (sin registros vigentes) |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado en los datos compilados para este informe. Según la información conocida, la bacitracina es un antibiótico polipeptídico tópico con actividad contra bacterias Gram-positivas y se utiliza en formulaciones oftálmicas.

La queratoconjuntivitis epitelial punteada suele tener origen viral o tóxico, por lo que un mecanismo antibacteriano tiene una relevancia mecanística débil. La relación con la indicación original (una pomada oftálmica con corticoide y antiinfecciosos) es únicamente la localización ocular, y no existe un vínculo mecanístico sólido.

El puntaje elevado de TxGNN es una predicción computacional sin respaldo de estudios reales. Por ello, la plausibilidad de esta predicción es baja y debe interpretarse con cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19987850 (cancelado) | ALTRACINE - A UNGÜENTO | Ungüento oftálmico | Dexametasona y antiinfecciosos |

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento (no provienen del prospecto):** epilepsia, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, queratitis por herpes simple, insuficiencia suprarrenal/enfermedad de Addison, glaucoma de ángulo abierto, hipertensión ocular, diabetes mellitus y cetoacidosis diabética, insuficiencia respiratoria, miastenia gravis y enfermedades de la unión neuromuscular, atrofia cutánea, telangiectasia, enfermedad vascular periférica, bloqueo auriculoventricular, e infecciones oculares (conjuntivitis, infecciones fúngicas o virales del ojo). Varias de estas probablemente reflejan el componente corticoide de la combinación original y no la bacitracina sola.
- **Interacciones farmacológicas:** se identificaron 84 interacciones. Las de nivel **mayor** incluyen kanamicina, neomicina, estreptomicina (riesgo aditivo de nefrotoxicidad/ototoxicidad con aminoglucósidos), deferasirox y medios de contraste yodados (diatrizoato, iodipamida, iodixanol, iohexol). Las de nivel **moderado** incluyen mesalazina, balsalazida, olsalazina, sulfasalazina, exenatida, vancomicina y ácido picosulfúrico.
- **Nefrotoxicidad:** la bacitracina de uso parenteral tiene nefrotoxicidad conocida, lo que genera preocupación si se considerara cualquier uso con exposición sistémica.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5), sin ensayos ni literatura, y el mecanismo antibacteriano tiene poca relación con una queratoconjuntivitis de origen mayormente viral o tóxico. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y del prospecto (advertencias y contraindicaciones) del producto.
- Evidencia clínica o preclínica que vincule la bacitracina con esta enfermedad.
- Confirmar la situación regulatoria, dado que no hay registros vigentes.
- Como alternativa, priorizar la indicación de **otitis externa** (nivel L4), que cuenta con un estudio clínico de una pomada con polimixina B y bacitracina, aunque con evidencia indirecta y basada en combinaciones.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

