---
layout: default
title: Teprotumumab
parent: Solo Predicción del Modelo (L5)
nav_order: 614
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Teprotumumab: nueva indicación predicha, Monosomía X (nivel de evidencia L5). Indicación original: No especificada en el registro (el texto aprobado solo repite el nomb…"
monitor_inn: "TEPROTUMUMAB"
predicted_indications: ["monosomy X", "esophageal varices without bleeding", "esophageal varices with bleeding", "mixed gonadal dysgenesis", "mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies", "Turner syndrome due to structural X chromosome anomalies", "mosaic monosomy X", "sex chromosome disorder of sex development", "varicose disease", "X chromosome number anomaly"]
---

# Teprotumumab
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

# Teprotumumab: De Indicación No Especificada a Monosomía X

## Resumen en Una Frase

Teprotumumab es un anticuerpo monoclonal anti-IGF-1R que contó con un registro sanitario en Colombia (TEPEZZA®), actualmente cancelado; en los datos compilados la indicación aprobada figura solo como el nombre del fármaco, sin texto descriptivo.
El modelo TxGNN predice que podría ser efectivo para **monosomía X** (síndrome de Turner), pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto aprobado solo repite el nombre "Teprotumumab"); la evaluación mecanística lo describe como aprobado para enfermedad ocular tiroidea |
| Nueva Indicación Predicha | Monosomía X |
| Puntaje de Predicción TxGNN | 99.79% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Teprotumumab es un anticuerpo monoclonal que bloquea el receptor del factor de crecimiento similar a la insulina tipo 1 (IGF-1R). No se dispone de datos detallados del mecanismo de acción en los datos compilados, pero este perfil farmacológico es el conocido para el fármaco, aprobado internacionalmente para la enfermedad ocular tiroidea.

**En este caso la razonabilidad biológica es débil.** No se identificó un vínculo mecanístico plausible entre el bloqueo de IGF-1R y la monosomía X. El tratamiento del síndrome de Turner se basa en hormona de crecimiento y reemplazo estrogénico, y el eje IGF-1/IGF-1R favorece el crecimiento; por ello, bloquear IGF-1R sería esperablemente contraproducente frente a la terapia de crecimiento.

El puntaje alto (0.998) refleja una señal basada en el grafo de conocimiento, probablemente por cercanía con otras entidades del grupo del síndrome de Turner, y no un mecanismo biológico demostrado. Lo mismo aplica a otras predicciones del modelo (síndrome de Turner por anomalías estructurales del X, monosomía X en mosaico, disgenesia gonadal mixta, varices esofágicas, enfermedad varicosa, entre otras), todas de nivel L5 y sin evidencia clínica.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20234945 (cancelado) | TEPEZZA® 500MG (AMGEN BIOTECNOLOGICA S.A.S.) | Polvo liofilizado para reconstituir a solución inyectable | TEPROTUMUMAB |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 45 interacciones potenciales, todas de nivel moderado en las muestras disponibles (fuente: DDInter). Corresponden sobre todo a antidiabéticos, entre ellos acarbosa, metformina, pioglitazona, glimepirida, glipizida, glibenclamida, insulina humana, inhibidores de SGLT2 (canagliflozina, dapagliflozina, empagliflozina, ertugliflozina), inhibidores de DPP-4 (alogliptina, saxagliptina, linagliptina) y agonistas de GLP-1 (albiglutida, dulaglutida, exenatida, semaglutida). Esto sugiere vigilar el control glucémico si se usa en pacientes diabéticos.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el puntaje del modelo (nivel L5), sin ensayos clínicos ni literatura. Además, el mecanismo (bloqueo de IGF-1R) iría en contra de la terapia de crecimiento usada en síndrome de Turner. El único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Revisión del mecanismo de acción y de un posible vínculo biológico con la monosomía X, o priorizar otras predicciones con mejor sustento
- Búsqueda sistemática de literatura y ensayos clínicos (incluidos estudios preclínicos)
- Obtención del prospecto de INVIMA para evaluar advertencias y contraindicaciones
- Aclarar la situación regulatoria (registro cancelado) y la disponibilidad del producto en Colombia
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

