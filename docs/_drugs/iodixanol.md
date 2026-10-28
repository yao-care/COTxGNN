---
layout: default
title: Iodixanol
parent: Solo Predicción del Modelo (L5)
nav_order: 351
evidence_level: L5
indication_count: 2
monitor_inn: "IODIXANOL"
predicted_indications: ["osteoarthritis", "rheumatoid arthritis"]
last_modified_at: 2026-10-23
description: "Iodixanol: nueva indicación predicha, Osteoartritis (nivel de evidencia L5). Indicación original: IODIXANOL"
---

# Iodixanol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Iodixanol: De Medio de Contraste Radiológico a Osteoartritis
{: .text-alpha }

## Resumen en Una Frase

Iodixanol es un medio de contraste yodado, no iónico e iso-osmolar, registrado en Colombia bajo la denominación "IODIXANOL" y utilizado en imagenología diagnóstica. El modelo TxGNN predice que podría ser efectivo para **osteoartritis**, pero **no hay ensayos clínicos** y solo **5 publicaciones**, todas sobre su uso como agente de imagen y no como tratamiento. La predicción carece de respaldo terapéutico.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | IODIXANOL (el registro sanitario no detalla una indicación clínica más específica) |
| Nueva Indicación Predicha | Osteoartritis |
| Puntaje de Predicción TxGNN | 0.9907 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, iodixanol es un medio de contraste radiográfico yodado, no iónico e iso-osmolar, sin actividad conocida de modificación de la enfermedad en la osteoartritis.

La literatura recuperada describe su uso como agente de diagnóstico: tomografía computarizada con contraste del cartílago, y estudios de difusión y transporte de solutos a través del cartílago y la interfase osteocondral. Ninguno evalúa un efecto terapéutico. Un estudio in vitro halló que los contrastes yodados no afectan la función del plasma rico en plaquetas, lo cual es un hallazgo de compatibilidad y no de eficacia.

El puntaje alto de TxGNN (0.9907) proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica ni un efecto farmacológico. Por ello, la predicción no tiene un vínculo mecanístico que la sustente.

Para la segunda predicción del modelo, **artritis reumatoide** (99.00%), tampoco existen ensayos clínicos. La única publicación es un reporte de caso sobre desensibilización a otro contraste (iohexol), sin relación con la eficacia de iodixanol, que no tiene actividad antiinflamatoria o inmunomoduladora conocida.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39012563](https://pubmed.ncbi.nlm.nih.gov/39012563/) | 2024 | Imagen/Preclínico | Annals of Biomedical Engineering | Imagen de difusión de nanopartículas por TC y modelado de elementos finitos para estudiar la función del cartílago; no evalúa tratamiento |
| [40155520](https://pubmed.ncbi.nlm.nih.gov/40155520/) | 2025 | Imagen/Preclínico | Annals of Biomedical Engineering | Agente de contraste dual en TC de conteo de fotones para evaluar la salud del cartílago articular |
| [28063646](https://pubmed.ncbi.nlm.nih.gov/28063646/) | 2017 | Modelado computacional | Journal of Biomechanics | Uso de iodixanol como contraste difusivo para estudiar la permeabilidad de la interfase cartílago-hueso subcondral |
| [27793406](https://pubmed.ncbi.nlm.nih.gov/27793406/) | 2016 | Modelado computacional | Journal of Biomechanics | Transporte de solutos neutros a través de la interfase osteocondral mediante TC y elementos finitos |
| [30374787](https://pubmed.ncbi.nlm.nih.gov/30374787/) | 2018 | In vitro | Journal of Experimental Orthopaedics | Los contrastes yodados no alteraron la función del plasma rico en plaquetas in vitro en una fase temprana |

Ninguna de estas publicaciones estudia a iodixanol como tratamiento de la osteoartritis.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20155256 | IODIXANOL SOLUCION INYECTABLE | Solución inyectable | IODIXANOL |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se registraron 100 interacciones en total. Entre las principales, de nivel **mayor**: metformina, anfotericina B (y sus formulaciones lipídicas, de sulfato de colesterilo y liposomal), mesalazina, balsalazida, olsalazina, sulfasalazina, vancomicina, kanamicina, neomicina, estreptomicina y polimixina B. De nivel **moderado**: manitol. Otras interacciones tienen nivel no definido (por ejemplo, famotidina, ácido acetilsalicílico, morfina, omeprazol y prednisona).

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni estudios que evalúen a iodixanol como tratamiento de la osteoartritis. La literatura solo lo describe como agente de imagen, y el puntaje alto proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica ni actividad terapéutica. El nivel de evidencia es L5.

**Para avanzar se necesita:**
- Evidencia preclínica que demuestre un efecto terapéutico real en osteoartritis, ya que hoy solo existen estudios de imagen y transporte.
- Datos del mecanismo de acción.
- Revisión del prospecto de INVIMA para advertencias y contraindicaciones.
- Evaluación de la vía de administración y su compatibilidad, dado que el producto registrado es una solución inyectable diseñada para uso diagnóstico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

