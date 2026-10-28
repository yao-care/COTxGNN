---
layout: default
title: Gadoxetic Acid
parent: Solo Predicción del Modelo (L5)
nav_order: 306
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Gadoxetic Acid: nueva indicación predicha, Hipertiroidismo (nivel de evidencia L5). Indicación original: Medios de contraste paramagnético (gadolinio)"
monitor_inn: "gadoxetic acid"
predicted_indications: ["hyperthyroidism", "resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "hyperthyroxinemia", "Prinzmetal angina", "infectious bovine rhinotracheitis", "malignant catarrh", "conjunctivitis", "cytomegalovirus infection", "conjunctivitis (disease)", "thrombotic disease"]
---

# Gadoxetic Acid
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

## Ácido gadoxético: De Medio de Contraste Paramagnético a Hipertiroidismo
{: .text-alpha }

## Resumen en Una Frase

El ácido gadoxético (Primovist®) es un medio de contraste paramagnético a base de gadolinio, utilizado originalmente para obtener imágenes por resonancia magnética.
El modelo TxGNN predice que podría ser efectivo para **hipertiroidismo**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.
La predicción se basa únicamente en el modelo computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Medios de contraste paramagnético (gadolinio) |
| Nueva Indicación Predicha | Hipertiroidismo |
| Puntaje de Predicción TxGNN | 0.9989 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, el ácido gadoxético es un agente de contraste hepatoespecífico a base de gadolinio: los hepatocitos lo captan mediante los transportadores OATP1B1/B3 y se excreta por la bilis.

No se identifica un vínculo mecanístico creíble con el hipertiroidismo. El fármaco no actúa sobre la síntesis ni la señalización de las hormonas tiroideas. Es un agente diagnóstico, no terapéutico, por lo que la relación con la indicación original (imagenología) es nula en términos de tratamiento.

El puntaje alto de TxGNN (0.9989) proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. Debe interpretarse con mucha cautela.

Otras predicciones del modelo TxGNN (deep learning) muestran el mismo patrón: resistencia a la hormona tiroidea por mutación en el receptor beta, hipertiroxinemia, angina de Prinzmetal, conjuntivitis, infección por citomegalovirus y enfermedades veterinarias (rinotraqueítis infecciosa bovina, catarro maligno). Sus puntajes pueden reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Para la indicación principal (hipertiroidismo) no hay literatura disponible. La única literatura encontrada corresponde a otra predicción (enfermedad trombótica) y es de uso diagnóstico, no terapéutico:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37246973](https://pubmed.ncbi.nlm.nih.gov/37246973/) | 2023 | Cohorte (precisión diagnóstica) | Abdominal Radiology | Concordancia entre observadores y precisión de LI-RADS v2018 para diferenciar trombo tumoral de trombo bland con RM potenciada con ácido gadoxético |
| [39809606](https://pubmed.ncbi.nlm.nih.gov/39809606/) | 2025 | Cohorte (modelo predictivo) | Academic Radiology | Modelo para predecir insuficiencia hepática tras quimioembolización, con RM con ácido gadoxético y puntaje funcional hepático (FLIS) |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20030187 (cancelado) | PRIMOVIST® SOLUCIÓN INYECTABLE | Solución inyectable | Medios de contraste paramagnético (gadolinio) |

---

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: se identificaron 33 interacciones, todas de nivel moderado en la muestra revisada (fuente: DDInter). Las principales incluyen:
  - Betabloqueadores: acebutolol, atenolol, betaxolol, bisoprolol, carvedilol, nadolol, labetalol, y los oftálmicos (timolol, carteolol, levobunolol, metipranolol).
  - Bloqueadores de canales de calcio: nifedipino, amlodipino, levamlodipino, diltiazem, verapamilo, clevidipino, isradipino.
  - Otros: rifabutina.

No se dispone de datos de advertencias ni contraindicaciones del prospecto. Consultar el prospecto para esa información.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo computacional (L5), sin ensayos ni literatura que la sustenten, y no existe un mecanismo plausible que vincule un agente de contraste con el hipertiroidismo. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (DrugBank) para confirmar la ausencia de vínculo con la vía tiroidea
- Advertencias y contraindicaciones del prospecto de INVIMA
- Evidencia preclínica o clínica que respalde la indicación, si se decide continuar
- Valorar si conviene priorizar otros candidatos, dado que todas las predicciones revisadas carecen de respaldo mecanístico
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

