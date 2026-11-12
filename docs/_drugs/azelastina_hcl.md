---
noindex: true
sitemap: false
layout: default
title: Azelastina Hcl
parent: Solo Predicción del Modelo (L5)
nav_order: 84
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Azelastina Hcl
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

## Azelastina HCL: Evaluación No Disponible — Sin Indicaciones Predichas
{: .text-alpha }

## Resumen en Una Frase

Azelastina HCL es un antihistamínico de segunda generación conocido por su uso en rinitis alérgica y conjuntivitis alérgica.
Sin embargo, el presente Evidence Pack **no contiene indicaciones predichas por TxGNN**, lo que impide realizar el análisis de reposicionamiento.
Adicionalmente, existen brechas críticas de datos en mecanismo de acción, seguridad y registro regulatorio en Colombia, por lo que la evaluación no puede completarse en esta versión.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | No disponible en el Evidence Pack |
| Nueva Indicación Predicha | Sin datos (predicted_indications vacío) |
| Puntaje de Predicción TxGNN | No disponible |
| Nivel de Evidencia | L5 — Sin estudios reales ni predicción del modelo disponible |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 3 de 3) |
| Número de Registros Sanitarios | 3 (vigentes: 3) |
| Decisión Recomendada | **Hold** |

---

## Por qué No Es Posible Completar la Evaluación

El Evidence Pack recibido presenta dos bloqueos estructurales que impiden el análisis estándar de reposicionamiento:

**1. Ausencia de predicciones del modelo TxGNN:** El campo `predicted_indications` está vacío. Sin una indicación candidata generada por el modelo, no es posible construir el análisis de plausibilidad mecanística ni la búsqueda de evidencia clínica. Este es el insumo central del flujo de evaluación.

**2. Brechas de datos de nivel Blocking y High:** Según el propio meta del Evidence Pack, existen dos brechas activas:
- **DG001 (Blocking):** Falta la ficha técnica/prospecto de INVIMA con advertencias y contraindicaciones. Sin este dato no puede iniciarse la evaluación de seguridad (S1).
- **DG002 (High):** El mecanismo de acción (MOA) está marcado como `[Data Gap]`. Esto impide el análisis de relación mecanística entre indicación original y nueva indicación.

Ambas brechas tienen rutas de remediación definidas (consulta a INVIMA y DrugBank respectivamente) y deben completarse antes de reintentar el pipeline.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

*(No existe indicación predicha contra la cual buscar evidencia clínica.)*

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

*(No existe indicación predicha contra la cual buscar publicaciones.)*

---

## Información de Mercado en Colombia

El campo `total_licenses` es 0 y no se recuperaron licencias en la consulta a TFDA/INVIMA del 2026-03-29.

<!-- review:begin co-lic-20261105-azelastina_hcl-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Azelastina HCL no cuenta con registros sanitarios activos en Colombia según los datos disponibles. El campo `total_licenses` es 0 y no se recuperaron licencias en la consulta a TFDA/INVIMA del 2026-03-29." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 3 registros sanitarios (vigentes: 3); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-azelastina_hcl-1 -->

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

*(Todos los campos de advertencias, contraindicaciones e interacciones farmacológicas están marcados como `[Data Gap]`. La consulta DDI arrojó `not_found`. Se requiere obtener la ficha técnica oficial antes de continuar.)*

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El Evidence Pack de Azelastina HCL no contiene indicaciones predichas por TxGNN ni datos regulatorios o de seguridad suficientes, por lo que no es posible generar un informe de reposicionamiento válido en esta versión.

**Para avanzar se necesita:**

1. **Resolver DG001 (Blocking):** Descargar y parsear el prospecto oficial de INVIMA para Azelastina HCL y extraer advertencias, contraindicaciones y poblaciones especiales.
2. **Resolver DG002 (High):** Consultar DrugBank (ID pendiente de confirmación) para obtener el mecanismo de acción (antagonismo H1 selectivo y propiedades antiinflamatorias adicionales).
3. **Reejecutar el pipeline TxGNN:** Con el DrugBank ID confirmado, regenerar las predicciones de indicaciones candidatas (`predicted_indications`) para que el análisis de reposicionamiento pueda completarse.
4. **Verificar presencia en mercado colombiano:** Explorar si existen registros bajo nombres comerciales alternativos (p. ej. Allergodil, Azep) que no hayan sido capturados bajo el INN exacto "AZELASTINA HCL".

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Azelastina HCL no cuenta con registros sanitarios activos en Colombia según los datos disponibles" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

