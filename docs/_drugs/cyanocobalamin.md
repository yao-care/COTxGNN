---
layout: default
title: Cyanocobalamin
parent: Solo Predicción del Modelo (L5)
nav_order: 182
evidence_level: L5
indication_count: 1
---

# Cyanocobalamin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Cianocobalamina: De Multivitamínicos / Complejo B a Enfermedad Metabólica de la Biotina

## Resumen en Una Frase

La cianocobalamina (vitamina B12) se comercializó en Colombia dentro de productos multivitamínicos y de complejo B.
El modelo TxGNN predice que podría ser efectiva para la **enfermedad metabólica de la biotina**,
pero actualmente no hay ensayos clínicos registrados y solo hay **1 publicación** de carácter general (una revisión sobre producción biotecnológica de vitaminas), por lo que la evidencia es únicamente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Multivitaminas y otros minerales, incluidas combinaciones |
| Nueva Indicación Predicha | Enfermedad metabólica de la biotina |
| Puntaje de Predicción TxGNN | 99.60% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, la cianocobalamina es una forma de vitamina B12, cofactor de la metionina sintasa y de la metilmalonil-CoA mutasa. Su uso se ha dado en productos multivitamínicos y de complejo B.

La biotina, por su parte, es cofactor de carboxilasas (como la propionil-CoA carboxilasa y la piruvato carboxilasa). Ambas vitaminas participan en rutas relacionadas, como el metabolismo del propionato y del metilmalonato, lo que podría explicar la asociación detectada por el modelo basado en grafos de conocimiento.

Sin embargo, esta relación es una inferencia computacional por cercanía de rutas y no está validada clínicamente. La vitamina B12 no corrige la deficiencia de biotinidasa ni la de holocarboxilasa sintetasa, cuyo tratamiento estándar es la suplementación con biotina. Por ello, la plausibilidad mecanística es limitada.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [1368195](https://pubmed.ncbi.nlm.nih.gov/1368195/) | 1992 | Revisión | Journal of Chemical Technology and Biotechnology | Revisión sobre la producción biotecnológica de vitaminas, coenzimas y bioquímicos relacionados; no evalúa eficacia clínica en enfermedad metabólica de la biotina |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19908281 (cancelado) | SUPRAVITAL | Cápsula blanda | Multivitaminas y otros minerales, incluidas combinaciones |
| 32856 (cancelado) | ANTIDOL B12® AMPOLLAS | Solución inyectable | Complejo B |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. Entre las analizadas, la mayoría son de nivel **menor**, principalmente con antiácidos y reductores de la acidez gástrica (famotidina, ranitidina, cimetidina, nizatidina, omeprazol, esomeprazol, lansoprazol, dexlansoprazol, pantoprazol, rabeprazol), además de cloruro de potasio. Otras interacciones tienen nivel no clasificado, entre ellas metformina, glimepirida, acarbosa, rosiglitazona, morfina, mesalazina, doxiciclina y sucralfato.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (puntaje alto, pero sin ensayos clínicos y con una única revisión general sin relación directa). Además, el tratamiento estándar de los trastornos del metabolismo de la biotina es la biotina misma, y no hay registros sanitarios vigentes en Colombia.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de la cianocobalamina que sustenten el vínculo con el metabolismo de la biotina
- Revisión sistemática de literatura específica sobre vitamina B12 y trastornos del metabolismo de la biotina
- Prospecto con advertencias y contraindicaciones (INVIMA u otra fuente)
- Verificación de la situación regulatoria actual, dado que ambos registros están cancelados
- Evaluación de compatibilidad de vías de administración
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

