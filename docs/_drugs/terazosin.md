---
layout: default
title: Terazosin
parent: Solo Predicción del Modelo (L5)
nav_order: 615
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
description: "Terazosin: nueva indicación predicha, Hipotricosis simple del cuero cabelludo (nivel de evidencia L5). Indicación original: TERAZOSINA"
monitor_inn: "terazosin"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "migraine disorder", "migraine with brainstem aura", "Raynaud disease", "Ambras type hypertrichosis universalis congenita", "manic bipolar affective disorder", "kyphoscoliotic heart disease"]
---

# Terazosin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Terazosina: De Indicación No Especificada en el Registro (Terazosina) a Hipotricosis Simple del Cuero Cabelludo
{: .text-alpha }

## Resumen en Una Frase

Terazosina es un bloqueador alfa-1 adrenérgico, comercializado en Colombia como HYTRIN® tabletas 5 mg; el registro sanitario disponible solo indica "terazosina" como indicación, sin detallar el uso aprobado.
El modelo TxGNN predice que podría ser efectivo para **hipotricosis simple del cuero cabelludo**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción.
Entre las demás predicciones, las que cuentan con algo de respaldo son **migraña** (2 publicaciones) y **enfermedad de Raynaud** (1 publicación), ambas antiguas y de baja calidad.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | TERAZOSINA (el registro no detalla la indicación aprobada) |
| Nueva Indicación Predicha | Hipotricosis simple del cuero cabelludo |
| Puntaje de Predicción TxGNN | 0.9997 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 2 de 2) |
| Número de Registros Sanitarios | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, terazosina es un bloqueador alfa-1 adrenérgico que produce vasodilatación y reduce la presión arterial.

La relación con la hipotricosis simple del cuero cabelludo es solo especulativa: se ha planteado que una vasodilatación que mejore la perfusión del cuero cabelludo podría favorecer el crecimiento del cabello, como ocurre con minoxidil. Sin embargo, esta condición es hereditaria y no hay evidencia que sustente que el bloqueo alfa-1 corrija el defecto subyacente. El puntaje alto proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

Cabe señalar que el modelo también predice otras indicaciones del grupo capilar (alopecia, alopecia areata difusa, hipotricosis congénita con milia e incluso hipertricosis de Ambras, que es de dirección opuesta), lo que indica que esta señal es poco específica y debe interpretarse con cautela.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para hipotricosis simple del cuero cabelludo.

Como referencia, en otras indicaciones predichas hay evidencia limitada:

| PMID | Año | Tipo | Revista | Indicación | Hallazgos Principales |
|------|-----|------|------|------|---------|
| [9273472](https://pubmed.ncbi.nlm.nih.gov/9273472/) | 1997 | Estudio clínico pequeño (diseño no verificado) | Minerva Cardioangiologica | Enfermedad de Raynaud | Terazosina redujo el número, la intensidad y la duración de los ataques vasoespásticos en las manos, con mejoría en termografía y ecografía |
| [7911406](https://pubmed.ncbi.nlm.nih.gov/7911406/) | 1994 | Estudio clínico abierto pequeño | La Clinica Terapeutica | Migraña | Estudio abierto en 46 pacientes con hemicránea sin aura; evaluó terazosina y buflomedil como profilaxis |
| [9074296](https://pubmed.ncbi.nlm.nih.gov/9074296/) | 1997 | Revisión / serie de casos | Headache | Migraña | Con terazosina o doxazosina en 10 pacientes, 9 mejoraron, pero 5 suspendieron por efectos secundarios |
| [34779371](https://pubmed.ncbi.nlm.nih.gov/34779371/) | 2022 | Revisión | Current Cardiology Reviews | Alopecia | Revisión sobre efectos extracardíacos de medicamentos cardiovasculares; evidencia indirecta (por ejemplo, minoxidil) |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1980002 | HYTRIN® TABLETAS 5 MG | Tableta | TERAZOSINA |

Fabricante: Laboratorio Franco Colombiano Lafrancol S.A.S.

<!-- review:begin co-lic-20261105-terazosin-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Fabricante: Laboratorio Franco Colombiano Lafrancol S.A.S. No hay registros vigentes." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 2 registros sanitarios (vigentes: 2); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-terazosin-1 -->

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** atrofia multisistémica, síndrome de taquicardia postural ortostática, hipotensión ortostática, priapismo y síndrome del iris flácido intraoperatorio.
- **Interacciones Farmacológicas:** se identificaron 137 interacciones potenciales. Las de nivel moderado incluyen corticosteroides (hidrocortisona, triamcinolona, dexametasona, betametasona, budesonida, prednisona, prednisolona), bupropión, morfina (incluida la liposomal), opio, inhibidores de SGLT2 (canagliflozina, dapagliflozina, empagliflozina, ertugliflozina) y cannabinoides (dronabinol, nabilona). Para calcitriol, pantoprazol y glimepirida el nivel de interacción es desconocido.
- Para el uso en hipotricosis, cardiopatías u otras indicaciones, el riesgo de hipotensión es una preocupación relevante, sobre todo en pacientes con compromiso cardiopulmonar.

No se dispone de advertencias ni contraindicaciones del prospecto; consultar el prospecto para información de seguridad adicional.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para hipotricosis simple del cuero cabelludo es solo del modelo (nivel L5), sin ensayos ni publicaciones. Las indicaciones con algo más de respaldo (migraña y Raynaud, nivel L3) se apoyan en estudios antiguos, pequeños y de diseño no verificado, y existen alternativas mejor establecidas.

<!-- review:begin co-lic-20261105-terazosin-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción para hipotricosis simple del cuero cabelludo es solo del modelo (nivel L5), sin ensayos ni publicaciones, y el único registro sanitario en Colombia está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 2 registros sanitarios (vigentes: 2); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-terazosin-2 -->

**Para avanzar se necesita:**
- Obtener y analizar el prospecto del INVIMA (advertencias y contraindicaciones), actualmente faltante.
- Obtener datos del mecanismo de acción desde DrugBank.
- Aclarar la indicación aprobada original, ya que el registro solo dice "terazosina".
- Evaluar si conviene priorizar migraña o enfermedad de Raynaud, que tienen algo de evidencia, mediante una revisión sistemática de la literatura.
- Confirmar la situación regulatoria.
- Definir, si se avanza, una vía de administración adecuada (probablemente tópica para el cuero cabelludo) y evaluar su viabilidad.

<!-- review:begin co-lic-20261105-terazosin-3 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Confirmar la situación regulatoria, dado que no hay registros vigentes en Colombia." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 2 registros sanitarios (vigentes: 2); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-terazosin-3 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "No hay registros vigentes" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "y el único registro sanitario en Colombia está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "dado que no hay registros vigentes en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

