---
layout: default
title: Clenbuterol
parent: Solo Predicción del Modelo (L5)
nav_order: 164
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-12
description: "Clenbuterol: nueva indicación predicha, Trastorno de migraña (migraine disorder) (nivel de evidencia L5). Indicación original: Combinaciones"
monitor_inn: "clenbuterol"
predicted_indications: ["migraine disorder", "migraine with brainstem aura"]
---

# Clenbuterol
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

## Clenbuterol: De Combinaciones (Indicación No Especificada) a Trastorno de Migraña
{: .text-alpha }

## Resumen en Una Frase

Clenbuterol figura en registros sanitarios colombianos únicamente como componente de jarabes combinados, cuya indicación aprobada aparece solo como "COMBINACIONES". El modelo TxGNN predice que podría ser efectivo para **trastorno de migraña**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; la predicción se basa únicamente en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Combinaciones (el registro no detalla una indicación específica) |
| Nueva Indicación Predicha | Trastorno de migraña (migraine disorder) |
| Puntaje de Predicción TxGNN | 0.9919 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 5 de 5) |
| Número de Registros Sanitarios | 5 (vigentes: 5) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, clenbuterol es un agonista adrenérgico beta-2, y su uso en Colombia se limitó a jarabes combinados (como Mucosolvan Compositum y Broncochem F), de tipo respiratorio. Esa clasificación se infiere de los nombres de los productos, no de una indicación registrada.

Mecanísticamente, la señalización beta-adrenérgica podría relacionarse con el tono vascular y la regulación neurovascular en la migraña. Sin embargo, esta relación es especulativa: la profilaxis de la migraña se hace con betabloqueadores, que son antagonistas, por lo que la dirección del efecto de un agonista es incierta y podría ser contraria a la terapéutica.

La segunda predicción, **migraña con aura del tronco encefálico** (puntaje 0.9904), probablemente está impulsada por su cercanía ontológica con el término "trastorno de migraña" y no por evidencia independiente. Ambas predicciones no deben considerarse señales independientes.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 1980176 | MUCOSOLVAN COMPOSITUM JARABE ADULTOS | Jarabe | Combinaciones | Vigente |
| 204457 | BRONCOCHEM® F JARABE ADULTOS | Solución oral | Combinaciones | Vigente |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (nivel L5), sin ensayos ni publicaciones. Además, el mecanismo beta-agonista va en sentido opuesto al de los tratamientos profilácticos establecidos (betabloqueadores).

<!-- review:begin co-lic-20261105-clenbuterol-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, el mecanismo beta-agonista va en sentido opuesto al de los tratamientos profilácticos establecidos (betabloqueadores), y no hay productos vigentes en Colombia." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 5 registros sanitarios (vigentes: 5); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-clenbuterol-1 -->

**Para avanzar se necesita:**
- Obtener el mecanismo de acción desde DrugBank y analizar el vínculo mecanístico con la migraña, incluida la dirección del efecto.
- Descargar y analizar el prospecto de INVIMA para completar advertencias y contraindicaciones, un paso necesario antes del tamizaje de seguridad.
- Buscar evidencia preclínica o clínica sobre agonistas beta-2 en migraña.
- Tratar la migraña con aura del tronco encefálico como parte de la misma señal, no como evidencia adicional.

<!-- review:begin co-lic-20261105-clenbuterol-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Aclarar la indicación real de los productos combinados cancelados y evaluar la compatibilidad de vías de administración. / Tratar la migraña con aura del tronco encefálico como parte de la misma señal, no como evidencia adicional." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 5 registros sanitarios (vigentes: 5); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-clenbuterol-2 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "y no hay productos vigentes en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Aclarar la indicación real de los productos combinados cancelados y evaluar la compatibilidad de vías de administración" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

