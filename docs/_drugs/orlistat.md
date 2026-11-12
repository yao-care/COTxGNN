---
layout: default
title: Orlistat
parent: Solo Predicción del Modelo (L5)
nav_order: 486
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
description: "Orlistat: nueva indicación predicha, Hipervitaminosis (nivel de evidencia L5). Indicación original: Orlistat"
monitor_inn: "ORLISTAT"
predicted_indications: ["hypervitaminosis"]
---

# Orlistat
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Orlistat: De Obesidad (Inhibición de Lipasas) a Hipervitaminosis
{: .text-alpha }

## Resumen en Una Frase

Orlistat es un inhibidor de las lipasas gástrica y pancreática.
El modelo TxGNN predice que podría ser efectivo para **hipervitaminosis**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; es solo una predicción computacional.

<!-- review:begin co-lic-20261105-orlistat-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Orlistat es un inhibidor de las lipasas gástrica y pancreática, que en Colombia contaba con registros sanitarios como medicamento de un solo principio activo (todos hoy cancelados)." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 15 registros sanitarios (vigentes: 14); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-orlistat-1 -->

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Orlistat (el texto de indicación del registro solo indica el nombre del principio activo) |
| Nueva Indicación Predicha | Hipervitaminosis |
| Puntaje de Predicción TxGNN | 0.9942 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 14 de 15) |
| Número de Registros Sanitarios | 15 (vigentes: 14) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen una descripción formal del mecanismo de acción. Según la información conocida, orlistat inhibe las lipasas gástrica y pancreática y reduce la absorción de grasa de la dieta en alrededor de un 30 %.

Las vitaminas liposolubles (A, D, E y K) se absorben junto con la grasa de la dieta, por lo que orlistat disminuye su absorción. Esto es precisamente lo que explica su efecto adverso conocido: la deficiencia de vitaminas liposolubles. Mecanísticamente, esa misma propiedad podría ser útil para reducir la sobrecarga de vitaminas liposolubles en la hipervitaminosis.

El puntaje alto de TxGNN probablemente refleja este vínculo farmacológico, pero sigue siendo una predicción computacional. Además, la hipervitaminosis es heterogénea: el exceso de vitaminas hidrosolubles no se vería afectado por la inhibición de lipasas. El uso clínico también estaría limitado por el tratamiento estándar actual (suspender la fuente de la vitamina y dar cuidados de soporte), por los efectos adversos gastrointestinales y por el riesgo de provocar deficiencia de otras vitaminas liposolubles.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20102710 | FINOBES ® 120 MG. (vigente) | Cápsula dura | Orlistat |
| 19979566 | ORLISTAT 120 MG CÁPSULAS (vigente) | Cápsula dura | Orlistat |
| 20091755 | ANGIOSTAT 120 MG CÁPSULAS (vigente) | Cápsula dura | Orlistat |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (TxGNN/PrimeKG, no provienen del prospecto):** insuficiencia hepática, hiperoxaluria primaria, anorexia nerviosa, bulimia nerviosa, trastornos por deficiencia vitamínica, colestasis (incluida la colestasis intrahepática recurrente benigna y la familiar) y lesión hepática inducida por fármacos.
- **Interacciones farmacológicas:** se identificaron 100 interacciones en total; entre las revisadas, la mayoría son de nivel moderado. Ejemplos:
  - Antirretrovirales: abacavir, lamivudina, atazanavir, emtricitabina.
  - Antidiabéticos: acarbosa, albiglutida, alogliptina, metformina, canagliflozina, clorpropamida.
  - Otros: amiodarona, asparaginasa, brentuximab vedotina, calaspargasa pegol, cannabidiol, clofarabina.
  - De nivel menor: colecalciferol, calcifediol y calcitriol (relevantes por su relación con las vitaminas liposolubles).

Para advertencias y contraindicaciones del prospecto, consultar el prospecto del producto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo y en un vínculo farmacológico plausible, sin ensayos clínicos ni literatura que la respalden (nivel L5). Además, existe riesgo de deficiencias vitamínicas y otros problemas de seguridad.

<!-- review:begin co-lic-20261105-orlistat-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, los registros sanitarios en Colombia están todos cancelados y existe riesgo de deficiencias vitamínicas y otros problemas de seguridad." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 15 registros sanitarios (vigentes: 14); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-orlistat-2 -->

**Para avanzar se necesita:**
- Revisión de la literatura preclínica y clínica sobre orlistat y los niveles de vitaminas liposolubles.
- Datos del mecanismo de acción confirmados por fuentes como DrugBank.
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones).
- Definir qué tipos de hipervitaminosis (vitaminas liposolubles) serían objetivo y compararlos con el tratamiento estándar.
- Aclarar la situación regulatoria, dado que el medicamento está comercializado y cuenta con 14 licencias vigentes, y evaluar la compatibilidad de vías de administración y formulaciones.

<!-- review:begin co-lic-20261112-orlistat-1 -->

> **Corrección de revisión (2026-11-12)**: Texto original: "3 licencias vigentes" Corregido según los datos del INVIMA (Código Único de Medicamentos, datos al 2026-11-05): 15 registros sanitarios, de los cuales 14 vigentes y 1 vigentes pero temporalmente no comercializados. Las cifras actuales están en el Resumen rápido. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261112-orlistat-1 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "que en Colombia contaba con registros sanitarios como medicamento de un solo principio activo (todos hoy cancelados)" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "los registros sanitarios en Colombia están todos cancelados y" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-12 | Número de registros vigentes: 3 → 14 | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

