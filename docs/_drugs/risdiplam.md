---
layout: default
title: Risdiplam
parent: Solo Predicción del Modelo (L5)
nav_order: 565
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
description: "Risdiplam: nueva indicación predicha, Acné (nivel de evidencia L5). Indicación original: Risdiplam"
monitor_inn: "RISDIPLAM"
predicted_indications: ["acne (disease)"]
---

# Risdiplam
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

## Risdiplam: De Atrofia Muscular Espinal a Acné
{: .text-alpha }

## Resumen en Una Frase

Risdiplam es un modificador del empalme del pre-ARNm de SMN2, utilizado originalmente para el tratamiento de la atrofia muscular espinal. El modelo TxGNN predice que podría ser efectivo para **acné**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Risdiplam (el registro sanitario solo consigna el nombre del principio activo, sin texto de indicación detallado) |
| Nueva Indicación Predicha | Acné |
| Puntaje de Predicción TxGNN | 0.9945 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Risdiplam es un modificador del empalme del pre-ARNm de SMN2. Favorece la inclusión del exón 7 y, con ello, aumenta la producción de proteína SMN completa. Está aprobado para la atrofia muscular espinal. Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción, por lo que no es posible validar de forma cruzada esta información.

No se identificó una conexión mecanística establecida entre este mecanismo y la patogénesis del acné (producción de sebo, hiperqueratinización folicular, colonización por *Cutibacterium acnes* e inflamación). La relación entre la indicación original (una enfermedad neuromuscular de origen genético) y el acné (una enfermedad inflamatoria dermatológica) es muy distante.

El puntaje alto de TxGNN (0.9945) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. No está respaldado por ningún estudio. Cualquier vínculo sería especulativo, por ejemplo, mediante efectos de empalme fuera de la diana en genes relacionados con la piel o las glándulas sebáceas, y no tiene sustento en los datos disponibles.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20197087 | EVRYSDI | Polvo para reconstituir a solución oral | Risdiplam |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (2 interacciones de nivel moderado según DDInter):
  - Metformina: moderada
  - Metilnaltrexona: moderada

No se dispone de datos de advertencias ni de contraindicaciones del prospecto. Consultar el prospecto para esta información.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos ni literatura, y no se identificó un vínculo mecanístico plausible con el acné. Además, faltan datos de seguridad del prospecto.

<!-- review:begin co-lic-20261105-risdiplam-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, el único registro sanitario en Colombia está cancelado y faltan datos de seguridad del prospecto." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-risdiplam-2 -->

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), indispensable para cualquier evaluación de seguridad
- Completar los datos del mecanismo de acción desde DrugBank
- Realizar una revisión de literatura y estudios preclínicos que sustenten un vínculo entre el empalme de SMN2 (o efectos fuera de la diana) y la biología de la piel o las glándulas sebáceas
- Evaluar la compatibilidad de la vía de administración (actualmente solo oral; la vía requerida para el acné está pendiente de definir)

<!-- review:begin co-lic-20261031-risdiplam-1 -->

> **Corrección de revisión (2026-10-31)**: Texto original: "Aclarar la situación regulatoria actual del producto en Colombia (registro cancelado) / Evaluar la compatibilidad de la vía de administración (actualmente solo oral; la vía requerida para el acné está pendiente de definir)" Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-10-31. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261031-risdiplam-1 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-10-31 | Eliminado: "Aclarar la situación regulatoria actual del producto en Colombia (registro cancelado)" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "el único registro sanitario en Colombia está cancelado y" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

