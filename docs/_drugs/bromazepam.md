---
layout: default
title: Bromazepam
parent: Solo Predicción del Modelo (L5)
nav_order: 117
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Bromazepam: nueva indicación predicha, Trastorno de migraña (nivel de evidencia L5). Indicación original: Bromazepam"
monitor_inn: "BROMAZEPAM"
predicted_indications: ["migraine disorder"]
---

# Bromazepam
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

## Bromazepam: De Indicación Registrada (Bromazepam) a Trastorno de Migraña
{: .text-alpha }

## Resumen en Una Frase

Bromazepam es una benzodiazepina, cuya indicación registrada figura solo con el nombre del propio principio activo.
El modelo TxGNN predice que podría ser efectivo para **trastorno de migraña**, pero actualmente **no hay ensayos clínicos ni publicaciones** en los datos compilados que respalden esta dirección.

<!-- review:begin co-lic-20261105-bromazepam-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Bromazepam es una benzodiazepina que contó con registros sanitarios en Colombia, hoy cancelados, cuya indicación registrada figura solo con el nombre del propio principio activo." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 2 registros sanitarios (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-bromazepam-1 -->

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Bromazepam (el registro no detalla una indicación clínica específica) |
| Nueva Indicación Predicha | Trastorno de migraña |
| Puntaje de Predicción TxGNN | 0.9906 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 2) |
| Número de Registros Sanitarios | 2 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según ChEMBL (EMBL-EBI), el mecanismo de acción registrado para Bromazepam es (traducción no oficial): «Modulador alostérico positivo de la subunidad alfa-2 del receptor GABA». Texto original en inglés: "GABA receptor alpha-2 subunit positive allosteric modulator" ([ChEMBL CHEMBL277062 (bromazepam): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL277062), CC BY-SA 3.0; consultado el 2026-11-19). Según el conocimiento general de la clase, bromazepam es una benzodiazepina que potencia la señalización del receptor GABA-A, lo que produce efectos ansiolíticos, sedantes y relajantes musculares.

Un posible vínculo con la migraña sería la reducción de la hiperexcitabilidad cortical y trigeminovascular, además del alivio de la ansiedad o la tensión muscular que suelen acompañar a la migraña. Este razonamiento es especulativo y no proviene de evidencia directa.

Conviene ser prudente: el puntaje de 0.9906 es solo una predicción del modelo. Las benzodiazepinas no son terapias establecidas para la migraña y su uso conlleva riesgos de dependencia, sedación y cefalea por abuso de medicación. La similitud con la indicación original y la compatibilidad de vías de administración aún están pendientes de evaluar.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

<!-- licenses:begin -->

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Descripción ATC | Estado |
|---------|------|------|------|------|
| 227603 | BROMAZEPAM 6 MG TABLETA | TABLETA | BROMAZEPAM | Vigente |
| 19920700 | LEXOTAN TABLETAS 3 MG | TABLETA | BROMAZEPAM | Temp. no comerc - Vigente |

Se muestran los 2 registros sanitarios de este principio activo en los datos del INVIMA, Código Único de Medicamentos; primero los vigentes.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

No se encontraron interacciones farmacológicas registradas en la consulta realizada.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura de respaldo. Además, las benzodiazepinas no son terapia establecida para migraña, con riesgos relevantes de dependencia y cefalea por abuso de medicación.

<!-- review:begin co-lic-20261105-bromazepam-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, los dos registros sanitarios en Colombia están cancelados y las benzodiazepinas no son terapia establecida para migraña, con riesgos relevantes de dependencia y cefalea por abuso de medicación." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 2 registros sanitarios (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-bromazepam-2 -->

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), pues sin esta información no es posible avanzar al tamizaje de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una revisión sistemática de la literatura sobre benzodiazepinas en migraña.
- Evaluar la similitud con la indicación original y la compatibilidad de vías de administración.
- Aclarar el estado regulatorio, dado que no existen registros vigentes en Colombia.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "que contó con registros sanitarios en Colombia, hoy cancelados" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "los dos registros sanitarios en Colombia están cancelados y" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente (revisado el 2026-11-20; la versión anterior se guarda en el registro) | [ChEMBL CHEMBL277062 (bromazepam): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL277062) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

