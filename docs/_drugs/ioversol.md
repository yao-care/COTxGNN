---
layout: default
title: Ioversol
parent: Solo Predicción del Modelo (L5)
nav_order: 353
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ioversol: nueva indicación predicha, Susceptibilidad a la osteoartritis (nivel de evidencia L5). Indicación original: IOVERSOL"
monitor_inn: "IOVERSOL"
predicted_indications: ["osteoarthritis susceptibility", "osteoarthritis", "rheumatoid arthritis", "brachyolmia", "hemoglobinopathy", "brachyolmia-amelogenesis imperfecta syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "myosclerosis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "alopecia"]
---

# Ioversol
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

# Ioversol: De Agente de Contraste Yodado a Osteoartritis (Susceptibilidad)

## Resumen en Una Frase

Ioversol es un medio de contraste yodado para diagnóstico por imagen; en Colombia su registro sanitario figura con la indicación "IOVERSOL" y actualmente está cancelado.
El modelo TxGNN predice que podría ser efectivo para **susceptibilidad a la osteoartritis**, pero **no hay ensayos clínicos ni publicaciones** que respalden directamente esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | IOVERSOL (el registro no detalla una indicación clínica; es un medio de contraste yodado) |
| Nueva Indicación Predicha | Susceptibilidad a la osteoartritis |
| Puntaje de Predicción TxGNN | 99.67% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, ioversol es un medio de contraste yodado que se usa como ayuda diagnóstica en imagen (por ejemplo, angiografía y tomografía), no como agente terapéutico con actividad modificadora de enfermedad.

No se identificó un vínculo mecanístico entre ioversol y la susceptibilidad genética a la osteoartritis. El puntaje elevado del modelo TxGNN proviene de la proximidad en el grafo de conocimiento y no de evidencia farmacológica o clínica. Por ello, esta predicción debe considerarse una hipótesis computacional sin respaldo.

Otras predicciones del modelo (osteoartritis, artritis reumatoide, braquiolmia, hemoglobinopatía, alopecia, entre otras) tampoco cuentan con un mecanismo plausible. En el caso de la osteoartritis, la única publicación asociada trata de embolización de arterias geniculares con aceite etiodizado, donde el contraste yodado solo sería una ayuda de imagen y no un tratamiento.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Para la indicación principal (susceptibilidad a la osteoartritis) no hay literatura disponible. Para la indicación relacionada **osteoartritis** se identificó una publicación, de relevancia solo indirecta:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38102013](https://pubmed.ncbi.nlm.nih.gov/38102013/) | 2024 | Ensayo clínico (un solo brazo, procedimental) | Diagnostic and Interventional Imaging | Evalúa seguridad y eficacia de la embolización transitoria de arterias geniculares con emulsión de aceite etiodizado en osteoartritis de rodilla. Ioversol no es el agente terapéutico; no respalda su reposicionamiento. |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 52944 (cancelado) | OPTIRAY ® 350 | Solución inyectable | IOVERSOL |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. Entre las principales, de nivel **Mayor**: metformina, anfotericina B (incluidas las formulaciones lipídica, de sulfato de colesterilo y liposomal), mesalazina, balsalazida, olsalazina, sulfasalazina, vancomicina, kanamicina, neomicina, estreptomicina y polimixina B. De nivel **Moderado**: manitol. Además, hay interacciones de nivel no determinado con atropina, famotidina, ácido acetilsalicílico, morfina y omeprazol.
- **Consideración adicional**: los medios de contraste pueden plantear preocupaciones de seguridad en algunas hemoglobinopatías, como la anemia de células falciformes, por lo que cualquier uso en ese contexto requeriría una revisión de seguridad previa.

No se dispone de advertencias ni contraindicaciones del prospecto; consultar el prospecto para más información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo, sin ensayos clínicos ni literatura directa, y no se identifica un mecanismo plausible entre un medio de contraste diagnóstico y la susceptibilidad a la osteoartritis. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Datos del mecanismo de acción del fármaco (por ejemplo, desde DrugBank).
- Obtener y analizar el prospecto de INVIMA para advertencias y contraindicaciones.
- Evidencia preclínica o mecanística que respalde una acción terapéutica en osteoartritis.
- Revisión de la literatura para confirmar que la publicación identificada no respalda el reposicionamiento.
- Evaluar si existe algún producto con ioversol vigente en el mercado colombiano.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

