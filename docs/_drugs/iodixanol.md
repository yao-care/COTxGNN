---
layout: default
title: Iodixanol
parent: Solo Predicción del Modelo (L5)
nav_order: 226
evidence_level: L5
indication_count: 3
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

# Iodixanol: De Medio de Contraste Yodado a Susceptibilidad a Osteoartritis

## Resumen en Una Frase

Iodixanol es un medio de contraste yodado iso-osmolar, usado como ayuda diagnóstica en imágenes. No tiene una indicación terapéutica original registrada en los datos disponibles.
El modelo TxGNN predice que podría ser efectivo para **susceptibilidad a osteoartritis**, pero hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción específica. Es una señal solo del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sin indicación terapéutica definida (el registro solo repite el nombre "IODIXANOL"; se trata de un medio de contraste) |
| Nueva Indicación Predicha | Susceptibilidad a osteoartritis |
| Puntaje de Predicción TxGNN | 99.16% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 12 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Iodixanol es un agente de contraste yodado iso-osmolar, farmacológicamente inerte, cuyo uso conocido es la visualización en imágenes diagnósticas, no el tratamiento de una enfermedad.

**No se identificó un vínculo mecanístico** con la osteoartritis. Además, "susceptibilidad" describe un fenotipo de riesgo, no una enfermedad tratable. El puntaje alto de TxGNN (99.16%) probablemente refleja la cercanía en el grafo de conocimiento entre iodixanol y la literatura de imágenes articulares, y no una señal real de tratamiento.

Las predicciones vecinas del modelo, **osteoartritis** (99.07%) y **artritis reumatoide** (99.00%), tampoco tienen respaldo terapéutico. Los estudios encontrados usan iodixanol o agentes similares como herramienta de imagen o trazador, no como tratamiento.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Para la indicación principal (susceptibilidad a osteoartritis) actualmente no hay literatura relacionada disponible.

Para la predicción vecina **osteoartritis** se recuperaron 7 publicaciones. Todas son estudios preclínicos, computacionales o in vitro, en los que iodixanol funciona como herramienta de diagnóstico o trazador y no como tratamiento:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [40155520](https://pubmed.ncbi.nlm.nih.gov/40155520/) | 2025 | Estudio preclínico de imagen | Annals of Biomedical Engineering | Agente de contraste dual (nanopartículas y componente molecular) en TC de conteo de fotones para evaluar la salud del cartílago articular |
| [39012563](https://pubmed.ncbi.nlm.nih.gov/39012563/) | 2024 | Estudio preclínico de imagen | Annals of Biomedical Engineering | Imagen de difusión de nanopartículas por TC y elementos finitos para estudiar la función del cartílago |
| [30145230](https://pubmed.ncbi.nlm.nih.gov/30145230/) | 2018 | Biomecánica ex vivo (animal) | Osteoarthritis and Cartilage | El envejecimiento no cambia la rigidez a la compresión del cartílago condilar mandibular en caballos |
| [30374787](https://pubmed.ncbi.nlm.nih.gov/30374787/) | 2018 | Estudio in vitro | Journal of Experimental Orthopaedics | Los contrastes yodados no afectan la función del plasma rico en plaquetas en etapa temprana (observación de compatibilidad, no de eficacia) |
| [28063646](https://pubmed.ncbi.nlm.nih.gov/28063646/) | 2017 | Computacional / transporte ex vivo | Journal of Biomechanics | Uso de iodixanol como contraste de difusión para estudiar la permeabilidad de la interfaz cartílago-hueso subcondral |
| [28518064](https://pubmed.ncbi.nlm.nih.gov/28518064/) | 2017 | Protocolo experimental y de elementos finitos | JoVE | Protocolo para estudiar el transporte de solutos neutros y cargados a través del cartílago articular |
| [27793406](https://pubmed.ncbi.nlm.nih.gov/27793406/) | 2016 | Modelado computacional | Journal of Biomechanics | Modelo de elementos finitos del transporte de solutos neutros a través de la interfaz osteocondral |

Para **artritis reumatoide** solo se recuperó un reporte de caso ([PMID 36628042](https://pubmed.ncbi.nlm.nih.gov/36628042/), Cureus, 2022). Trata la desensibilización a otro contraste (iohexol) y no aporta evidencia de eficacia de iodixanol.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20155256 | IODIXANOL SOLUCION INYECTABLE (UNIQUE PHARMACEUTICAL LABORATORIES) | Solución inyectable | IODIXANOL |

Nota: los datos listan el mismo registro (20155256) repetido varias veces. Se muestra una sola fila. El total informado es de 12 registros.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5). No hay ensayos clínicos ni literatura terapéutica, y no se identificó un mecanismo plausible: iodixanol es un contraste inerte y "susceptibilidad" no es una indicación tratable. La literatura vecina sobre osteoartritis (L4) solo muestra uso diagnóstico.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank.
- Advertencias y contraindicaciones del prospecto de INVIMA, necesarias para el tamizaje de seguridad.
- Una hipótesis biológica concreta, con una indicación tratable definida (por ejemplo, osteoartritis y no "susceptibilidad").
- Evidencia preclínica o clínica de un efecto terapéutico, no solo de uso como agente de imagen.
- Evaluación de la compatibilidad de la vía de administración (actualmente pendiente).

*Este informe es solo para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

