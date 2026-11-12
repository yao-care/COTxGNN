---
noindex: true
sitemap: false
layout: default
title: Alcaftadina
parent: Solo Predicción del Modelo (L5)
nav_order: 33
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Alcaftadina
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **0** 
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

## ALCAFTADINA: Evaluación de Reposicionamiento – Datos Insuficientes para Análisis Completo
{: .text-alpha }

## Resumen en Una Frase

ALCAFTADINA es un fármaco identificado en DrugBank, pero el paquete de evidencia actual no contiene indicaciones originales documentadas ni predicciones TxGNN de nuevas indicaciones. Sin estos datos fundamentales, no es posible completar una evaluación de reposicionamiento; se requiere recolección adicional de información antes de continuar.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sin datos disponibles en este paquete |
| Nueva Indicación Predicha | Sin predicciones generadas |
| Puntaje de Predicción TxGNN | Sin datos disponibles |
| Nivel de Evidencia | L5 – Solo identificación del fármaco, sin estudios |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Esta sección no aplica en el estado actual del análisis.

El campo `predicted_indications` está vacío, lo que indica que el pipeline TxGNN no ha generado predicciones para este fármaco. Adicionalmente, el mecanismo de acción (MOA) está marcado como brecha de datos de severidad **Alta**, lo que impide realizar el análisis de plausibilidad mecanística que normalmente sustenta esta sección.

Para que esta evaluación pueda avanzar, es necesario ejecutar el modelo TxGNN con los datos de ALCAFTADINA y obtener su perfil farmacológico completo desde DrugBank.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

La consulta a la base de datos regulatoria no arrojó licencias vigentes para este principio activo.

<!-- review:begin co-lic-20261105-alcaftadina-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "ALCAFTADINA no cuenta con registros sanitarios activos en Colombia. La consulta a la base de datos regulatoria no arrojó licencias vigentes para este principio activo." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-alcaftadina-1 -->

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

> **Nota:** Las advertencias principales y contraindicaciones están marcadas como brechas de datos bloqueantes (DG001). La consulta al prospecto oficial está pendiente de procesamiento, a pesar de que el log registra una extracción exitosa del documento (`tfda_package_insert`, resultado: 1). Se recomienda revisar manualmente el contenido obtenido.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El paquete de evidencia carece de los tres elementos fundamentales para una evaluación de reposicionamiento: indicaciones originales documentadas, predicciones TxGNN de nuevas indicaciones, y datos de seguridad (advertencias y contraindicaciones). Sin esta información no es posible emitir una recomendación clínica o regulatoria fundada.

**Para avanzar se necesita:**
- Extraer y estructurar el contenido del prospecto ya descargado (`tfda_package_insert`, 2026-03-29) para obtener indicaciones aprobadas, advertencias y contraindicaciones
- Consultar DrugBank con el resultado disponible (`drugbank`, resultado: 1) para obtener el mecanismo de acción (MOA), categorías farmacológicas e indicaciones originales
- Ejecutar el pipeline TxGNN con los datos completos del fármaco para generar predicciones de nuevas indicaciones
- Evaluar la viabilidad de registro en Colombia (INVIMA) una vez obtenidas las indicaciones y el perfil de seguridad

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "ALCAFTADINA no cuenta con registros sanitarios activos en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

