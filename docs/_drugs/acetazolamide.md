---
layout: default
title: Acetazolamide
parent: Solo Predicción del Modelo (L5)
nav_order: 23
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Acetazolamide: nueva indicación predicha, Hipertermia maligna inducida por ejercicio (nivel de evidencia L5). Indicación original: Acetazolamida"
---

# Acetazolamide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Acetazolamida: De Acetazolamida (indicación registrada sin detalle) a Hipertermia Maligna Inducida por Ejercicio

## Resumen en Una Frase

Acetazolamida es un inhibidor de la anhidrasa carbónica, utilizado clásicamente en glaucoma, epilepsia y edema; en Colombia su registro sanitario solo indica "ACETAZOLAMIDA" como indicación.
El modelo TxGNN predice que podría ser efectivo para **hipertermia maligna inducida por ejercicio**, pero **no existen ensayos clínicos ni publicaciones** que respalden esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Acetazolamida (el registro no detalla la indicación) |
| Nueva Indicación Predicha | Hipertermia maligna inducida por ejercicio |
| Puntaje de Predicción TxGNN | 99.95% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, acetazolamida inhibe varias isoenzimas de la anhidrasa carbónica (CA1, CA4, CA7, CA12, CA14 en humanos), lo que explica su uso como diurético y para reducir la presión intraocular, y su efecto antiepiléptico se atribuye a la inhibición de esta enzima en el cerebro.

La relación con la nueva indicación es solo teórica: al modificar el equilibrio ácido-base y el manejo de iones, el fármaco podría influir en la fisiología muscular. Sin embargo, no hay un vínculo mecanístico directo establecido en los datos; el puntaje alto proviene únicamente de la predicción computacional del modelo.

Otras predicciones del modelo (por ejemplo, miocardiopatía hipertrófica, miocardiopatía y obstrucción intestinal) tampoco cuentan con evidencia clínica favorable. Para obstrucción intestinal, la literatura describe más bien un riesgo (íleo adinámico inducido por acetazolamida).

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para hipertermia maligna inducida por ejercicio.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 19973358 | VICLEAR® | Tableta | ACETAZOLAMIDA | Cancelado |

---

## Consideraciones de Seguridad

- **Contraindicaciones sugeridas por el grafo de conocimiento (no provienen del prospecto):** insuficiencia o enfermedad hepática, enfermedad renal, acidosis tubular renal, enfermedades hematológicas, enfermedad de la vesícula biliar, gota, diabetes mellitus tipo 1 y tipo 2, cetoacidosis diabética, insuficiencia respiratoria, enfermedad de Addison e insuficiencia suprarrenal (incluidas hiperplasia suprarrenal congénita y otras formas de insuficiencia adrenocortical) y piouréter.
- **Señales de seguridad en la literatura (indicaciones alternativas):** un reporte de caso de edema pulmonar no cardiogénico tras acetazolamida intravenosa y un reporte de íleo adinámico inducido por acetazolamida.
- **Interacciones:** la consulta no identificó interacciones fármaco-fármaco clínicas; solo se registraron dianas farmacológicas (anhidrasas carbónicas 1, 4, 7, 12, 13 y 14).

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura específica, y el único registro sanitario en Colombia está cancelado. Además, existen señales de seguridad y múltiples contraindicaciones potenciales.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), ya que su ausencia impide el tamizaje de seguridad.
- Completar los datos del mecanismo de acción (por ejemplo, desde DrugBank) y analizar el vínculo mecanístico con la hipertermia maligna inducida por ejercicio.
- Realizar una revisión de literatura preclínica dirigida a esta indicación.
- Aclarar la situación regulatoria: confirmar si existen otras presentaciones vigentes de acetazolamida en Colombia.
- Evaluar candidatas alternativas con mayor soporte, dado el perfil de seguridad y la falta de evidencia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

