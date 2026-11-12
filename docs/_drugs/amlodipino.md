---
noindex: true
sitemap: false
layout: default
title: Amlodipino
parent: Solo Predicción del Modelo (L5)
nav_order: 52
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Amlodipino
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

## AMLODIPINO: Evaluación de Reposicionamiento — Datos Insuficientes para Predicción
{: .text-alpha }

## Resumen en Una Frase

AMLODIPINO es un fármaco de la clase de bloqueadores de canales de calcio, reconocido en la práctica clínica internacional para el manejo de hipertensión y angina. Sin embargo, el presente Evidence Pack **no contiene indicaciones predichas por TxGNN**, por lo que no es posible realizar una evaluación completa de reposicionamiento en este momento. Se identificaron brechas de datos críticas —incluyendo la ausencia de datos de mecanismo de acción y advertencias del prospecto— que impiden avanzar en el análisis.

---

## Resumen Rápido

| Ítem | Contenido |
|------|-----------|
| Indicación Original | Sin datos disponibles en el sistema |
| Nueva Indicación Predicha | Sin predicciones disponibles |
| Puntaje de Predicción TxGNN | N/D |
| Nivel de Evidencia | N/D |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 19) |
| Número de Registros Sanitarios | al menos 20 |
| Decisión Recomendada | **Hold** |

---

## Por qué No se Generaron Predicciones

El modelo TxGNN no produjo indicaciones predichas para AMLODIPINO en este Evidence Pack. Las causas más probables son:

**Brecha bloqueante en seguridad (DG001):** No se recuperaron las advertencias ni contraindicaciones del prospecto oficial. Este dato tiene severidad *Bloqueante*, lo que significa que el pipeline no puede completar la evaluación de seguridad inicial (S1) necesaria como insumo para el modelo.

**Mecanismo de acción no disponible (DG002):** Aunque la consulta a DrugBank reportó 1 resultado en el log de consultas, el campo `original_moa` no fue poblado en el Evidence Pack. Sin este dato, el modelo carece de las relaciones mecanísticas necesarias para proyectar nuevas indicaciones con fundamento biológico.

<!-- review:begin co-lic-20261105-amlodipino-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "**Ausencia de registros regulatorios locales:** AMLODIPINO no figura con ningún registro sanitario en el sistema consultado (0 licencias), lo que reduce adicionalmente la información de contexto disponible para el análisis." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-amlodipino-1 -->

---

## Brechas de Datos Identificadas

| ID | Ítem Faltante | Severidad | Fuente de Remediación |
|----|--------------|-----------|----------------------|
| DG001 | Advertencias y contraindicaciones del prospecto oficial | Bloqueante | Descarga e interpretación del prospecto en PDF desde la fuente regulatoria oficial |
| DG002 | Mecanismo de acción (MOA) | Alta | Recuperación desde la API de DrugBank |

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El Evidence Pack no contiene indicaciones predichas por TxGNN ni registros regulatorios locales, lo que hace imposible completar la evaluación de reposicionamiento en esta etapa. Las brechas identificadas son remediables, pero deben resolverse antes de reanudar el análisis.

**Para avanzar se necesita:**
- **Resolver DG001:** Obtener y analizar el prospecto oficial para extraer advertencias, contraindicaciones e indicaciones aprobadas
- **Resolver DG002:** Recuperar el mecanismo de acción completo desde DrugBank y validar que se popule correctamente en el Evidence Pack
- **Re-ejecutar el pipeline TxGNN** con los datos completos para generar predicciones de nuevas indicaciones
- **Verificar el estado regulatorio de AMLODIPINO** en el sistema INVIMA de Colombia, ya que se trata de un fármaco con amplia trayectoria clínica internacional cuya ausencia de registros locales podría deberse a un error de consulta o nombre alternativo

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "**Ausencia de registros regulatorios locales:** AMLODIPINO no figura con ningún registro sanitario en el sistema consultado (0 licencias), l" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

