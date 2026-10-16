---
layout: default
title: Mesalazine
parent: Solo Predicción del Modelo (L5)
nav_order: 432
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Mesalazine: nueva indicación predicha, Hipotricosis congénita con distrofia macular juvenil (nivel de evidencia L5). Indicación original: Mesalazina"
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

# Mesalazina: De Mesalazina (indicación no detallada en el registro) a Hipotricosis congénita con distrofia macular juvenil

## Resumen en Una Frase

La mesalazina (ácido 5-aminosalicílico) es un antiinflamatorio intestinal que en Colombia contó con registros sanitarios bajo el nombre del principio activo; en la literatura se utiliza para la colitis ulcerosa y otras enfermedades inflamatorias intestinales.
El modelo TxGNN predice que podría ser efectivo para **hipotricosis congénita con distrofia macular juvenil**,
pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; es solo una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Mesalazina (el registro INVIMA no detalla la indicación; el uso clínico conocido es colitis ulcerosa y enfermedad inflamatoria intestinal) |
| Nueva Indicación Predicha | Hipotricosis congénita con distrofia macular juvenil |
| Puntaje de Predicción TxGNN | 99.65% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 4 (0 vigentes, 4 cancelados) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la mesalazina es un antiinflamatorio aminosalicilato cuya eficacia en la colitis ulcerosa está comprobada. Se le atribuye inhibición de la síntesis de prostaglandinas y leucotrienos, modulación de NF-kB y activación de PPAR-gamma (este último es la única interacción farmacológica registrada).

La hipotricosis congénita con distrofia macular juvenil es un trastorno genético raro, asociado a mutaciones en CDH3 que afectan la adhesión celular. El análisis realizado no identificó un vínculo mecanístico plausible: la acción antiinflamatoria de la mesalazina no tiene relevancia conocida para esta enfermedad.

Por tanto, el alto puntaje de TxGNN refleja únicamente asociaciones dentro del grafo de conocimiento y no una razón biológica o clínica demostrada. La predicción debe considerarse una hipótesis sin respaldo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Los cuatro registros están cancelados; actualmente no hay productos vigentes.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20065382 | MESILAX® | Suspensión para administrar por vía rectal | Mesalazina |
| 19999923 | MESAX 500 MG TABLETAS | Tableta con cubierta entérica con película | Mesalazina |
| 20041831 | SALOFALK® 3G | Gránulos | Mesalazina |
| 20235125 | MESALAZINA TABLETA RECUBIERTA X 500 MG | Tableta con recubrimiento entérico | Mesalazina |

## Consideraciones de Seguridad

- **Enfermedades asociadas a contraindicación en el grafo de conocimiento** (relaciones del grafo, no texto de prospecto): enfermedad renal, piouréter, enfermedad hepática, enfermedad de la vesícula biliar, neutropenia, agranulocitosis, anemia (incluida la macrocítica), estenosis pilórica, nefrosis lipoidea y nefritis intersticial.
- **Interacciones Farmacológicas**: se registró una interacción farmacológica de tipo farmacología (sin nivel de gravedad), con el receptor gamma activado por proliferadores de peroxisomas (PPARG).

Para información detallada de advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ensayos clínicos ni literatura, carece de vínculo mecanístico plausible y el producto no tiene registros vigentes en Colombia. Con evidencia de nivel L5, no hay base para avanzar.

**Para avanzar se necesita:**
- Datos de mecanismo de acción (MOA) de la mesalazina desde DrugBank
- Advertencias y contraindicaciones del prospecto de INVIMA (brecha bloqueante para el análisis de seguridad)
- Evidencia preclínica que relacione la acción de la mesalazina con la vía CDH3 o la patología de esta enfermedad
- Evaluar otras predicciones con algo más de respaldo, como la artritis reumatoide (nivel L4, evidencia indirecta basada en sulfasalazina), considerada una pregunta de investigación
- Determinar la viabilidad comercial dado que los cuatro registros están cancelados
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

