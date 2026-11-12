---
layout: default
title: Hesperidin
parent: Solo Predicción del Modelo (L5)
nav_order: 326
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-12
description: "Hesperidin: nueva indicación predicha, Neoplasia mieloproliferativa (nivel de evidencia L5). Indicación original: Combinaciones de diosmina"
monitor_inn: "hesperidin"
predicted_indications: ["myeloproliferative neoplasm", "monocytic leukemia", "spermatocytic seminoma", "tubular variant testicular seminoma", "gestational trophoblastic neoplasm"]
---

# Hesperidin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Hesperidina: De Combinaciones de Diosmina a Neoplasia Mieloproliferativa
{: .text-alpha }

## Resumen en Una Frase

Hesperidina es un flavonoide que en Colombia se registró en un producto de combinaciones de diosmina (VEDIPAL® comprimidos recubiertos).
El modelo TxGNN predice que podría ser efectivo para **neoplasia mieloproliferativa**,
pero **no hay ensayos clínicos** y solo **1 publicación** (un estudio computacional in silico) respalda esta dirección.

<!-- review:begin co-lic-20261105-hesperidin-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Hesperidina es un flavonoide que en Colombia se registró en un producto de combinaciones de diosmina (VEDIPAL® comprimidos recubiertos), cuyo registro sanitario está actualmente cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 5 registros sanitarios (vigentes: 4); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-hesperidin-1 -->

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Combinaciones de diosmina |
| Nueva Indicación Predicha | Neoplasia mieloproliferativa |
| Puntaje de Predicción TxGNN | 0.9947 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 4 de 5) |
| Número de Registros Sanitarios | 5 (vigentes: 4) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la hesperidina es un flavonoide que se ha usado en combinaciones con diosmina, y su uso original está ligado a ese tipo de preparados. No hay datos que permitan establecer un vínculo mecanístico firme con la nueva indicación.

El único respaldo es un estudio computacional de 2019 que buscó fármacos reposicionables contra el dominio quinasa de BCR-ABL en la leucemia mieloide crónica (una neoplasia mieloproliferativa). En ese estudio la hesperidina apareció como un resultado de acoplamiento molecular (docking), no como un inhibidor validado. No hay datos experimentales, preclínicos ni clínicos.

El puntaje de 0.9947 del modelo TxGNN es solo una predicción computacional. Sin conocer el mecanismo original, no es posible contrastar su plausibilidad biológica.

### Otras indicaciones predichas (para referencia)

| Posición | Enfermedad | Puntaje TxGNN | Evidencia disponible |
|------|------|------|------|
| 2 | Leucemia monocítica | 0.9940 | Un estudio in vitro de 2003 (PMID 14505793) sobre flavonoides y apoptosis en células HL-60; sugiere que el grupo rutinósido, presente en la hesperidina, atenúa la actividad proapoptótica, lo que más bien va en contra de la eficacia |
| 3 | Seminoma espermatocítico | 0.9934 | Ninguna |
| 4 | Seminoma testicular variante tubular | 0.9931 | Ninguna |
| 5 | Neoplasia trofoblástica gestacional | 0.9903 | Ninguna |

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31759365](https://pubmed.ncbi.nlm.nih.gov/31759365/) | 2019 | Estudio in silico / computacional | Asian Pacific Journal of Cancer Prevention | Cribado computacional de fármacos para reposicionamiento contra el dominio quinasa de BCR-ABL en leucemia mieloide crónica, orientado a la proteína Grb-2; la hesperidina aparece como candidata por acoplamiento molecular, sin validación experimental |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20004470 | VEDIPAL® COMPRIMIDOS RECUBIERTOS | Tableta recubierta | Combinaciones de diosmina |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

No se encontraron interacciones farmacológicas registradas para este fármaco en los datos compilados para este informe.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa casi por completo en el modelo TxGNN (nivel de evidencia L5); el único apoyo es un estudio de acoplamiento molecular sin validación experimental. Además, no hay datos de seguridad ni de mecanismo de acción.

<!-- review:begin co-lic-20261105-hesperidin-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, el único registro sanitario en Colombia está cancelado y no hay datos de seguridad ni de mecanismo de acción." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 5 registros sanitarios (vigentes: 4); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-hesperidin-2 -->

**Para avanzar se necesita:**
- Obtener el mecanismo de acción desde DrugBank para evaluar la plausibilidad mecanística
- Descargar y analizar el prospecto de INVIMA para completar advertencias y contraindicaciones (brecha bloqueante para el cribado de seguridad)
- Validación experimental in vitro (por ejemplo, en líneas celulares con BCR-ABL o mutaciones JAK2) de la actividad de la hesperidina
- Revisar la evidencia en contra (efecto atenuante del grupo rutinósido sobre la apoptosis en células leucémicas)
- Aclarar la situación regulatoria

<!-- review:begin co-lic-20261105-hesperidin-3 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Aclarar la situación regulatoria, dado que no hay registros vigentes en Colombia" Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 5 registros sanitarios (vigentes: 4); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-hesperidin-3 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "cuyo registro sanitario está actualmente cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "el único registro sanitario en Colombia está cancelado y" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "dado que no hay registros vigentes en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

