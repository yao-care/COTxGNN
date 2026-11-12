---
layout: default
title: Mesalazine
parent: Solo Predicción del Modelo (L5)
nav_order: 432
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-12
description: "Mesalazine: nueva indicación predicha, Hipotricosis congénita con distrofia macular juvenil (nivel de evidencia L5). Indicación original: Mesalazina"
monitor_inn: "Mesalazine"
predicted_indications: ["congenital hypotrichosis with juvenile macular dystrophy", "osteoarthritis", "rheumatoid arthritis", "seborrheic keratosis", "vulvar inverted follicular keratosis", "pseudoachondroplasia"]
---

# Mesalazine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Mesalazina: De Mesalazina (indicación no detallada en el registro) a Hipotricosis congénita con distrofia macular juvenil
{: .text-alpha }

## Resumen en Una Frase

La mesalazina (ácido 5-aminosalicílico) es un antiinflamatorio intestinal; en la literatura se utiliza para la colitis ulcerosa y otras enfermedades inflamatorias intestinales.
El modelo TxGNN predice que podría ser efectivo para **hipotricosis congénita con distrofia macular juvenil**,
pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; es solo una predicción computacional.

<!-- review:begin co-lic-20261105-mesalazine-4 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La mesalazina (ácido 5-aminosalicílico) es un antiinflamatorio intestinal que en Colombia contó con registros sanitarios bajo el nombre del principio activo; en la literatura se utiliza para la colitis ulcerosa y otras enfermedades inflamatorias intestinales." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 17 registros sanitarios (vigentes: 14); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-mesalazine-4 -->

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Mesalazina (el registro INVIMA no detalla la indicación; el uso clínico conocido es colitis ulcerosa y enfermedad inflamatoria intestinal) |
| Nueva Indicación Predicha | Hipotricosis congénita con distrofia macular juvenil |
| Puntaje de Predicción TxGNN | 0.9965 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 14 de 17) |
| Número de Registros Sanitarios | 17 (vigentes: 14) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la mesalazina es un antiinflamatorio aminosalicilato cuya eficacia en la colitis ulcerosa está comprobada. Se le atribuye inhibición de la síntesis de prostaglandinas y leucotrienos, modulación de NF-kB y activación de PPAR-gamma (este último es la única interacción farmacológica registrada).

La hipotricosis congénita con distrofia macular juvenil es un trastorno genético raro, asociado a mutaciones en CDH3 que afectan la adhesión celular. El análisis realizado no identificó un vínculo mecanístico plausible: la acción antiinflamatoria de la mesalazina no tiene relevancia conocida para esta enfermedad.

Por tanto, el alto puntaje de TxGNN proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica ni una razón clínica demostrada. La predicción debe considerarse una hipótesis sin respaldo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

<!-- review:begin co-lic-20261105-mesalazine-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Los cuatro registros están cancelados; actualmente no hay productos vigentes." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 17 registros sanitarios (vigentes: 14); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-mesalazine-1 -->

## Información de Mercado en Colombia

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
La predicción no tiene ensayos clínicos ni literatura, carece de vínculo mecanístico plausible. Con evidencia de nivel L5, no hay base para avanzar.

<!-- review:begin co-lic-20261105-mesalazine-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción no tiene ensayos clínicos ni literatura, carece de vínculo mecanístico plausible y el producto no tiene registros vigentes en Colombia." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 17 registros sanitarios (vigentes: 14); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-mesalazine-2 -->

**Para avanzar se necesita:**
- Datos de mecanismo de acción (MOA) de la mesalazina desde DrugBank
- Advertencias y contraindicaciones del prospecto de INVIMA (brecha bloqueante para el análisis de seguridad)
- Evidencia preclínica que relacione la acción de la mesalazina con la vía CDH3 o la patología de esta enfermedad
- Evaluar otras predicciones con algo más de respaldo, como la artritis reumatoide (nivel L4, evidencia indirecta basada en sulfasalazina), considerada una pregunta de investigación
- Determinar la viabilidad comercial

<!-- review:begin co-lic-20261105-mesalazine-3 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Determinar la viabilidad comercial dado que los cuatro registros están cancelados" Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 17 registros sanitarios (vigentes: 14); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-mesalazine-3 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Los cuatro registros están cancelados; actualmente no hay productos vigentes" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "y el producto no tiene registros vigentes en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "dado que los cuatro registros están cancelados" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "que en Colombia contó con registros sanitarios bajo el nombre del principio activo" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

