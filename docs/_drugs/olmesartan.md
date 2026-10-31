---
layout: default
title: Olmesartan
parent: Solo Predicción del Modelo (L5)
nav_order: 481
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-31
monitor_inn: "OLMESARTAN"
predicted_indications: ["Prinzmetal angina", "hypotrichosis simplex of the scalp", "migraine disorder", "alopecia", "pulmonary hypertension", "congenital hypotrichosis milia", "diffuse alopecia areata", "migraine with brainstem aura", "kyphoscoliotic heart disease", "open-angle glaucoma"]
description: "Olmesartan: nueva indicación predicha, Prinzmetal angina (nivel de evidencia L5). Indicación original: OLMERSARTAN MEDOXOMIL Y DIURETICOS"
---

# Olmesartan
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

## Olmesartan: Prinzmetal angina
{: .text-alpha }

## Resumen en Una Frase

Olmesartán (como olmesartán medoxomilo) es un bloqueador del receptor AT1 de angiotensina II, registrado en Colombia en una combinación con diuréticos.
El modelo TxGNN predice que podría ser efectivo para **angina de Prinzmetal**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta indicación específica; se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | OLMERSARTAN MEDOXOMIL Y DIURETICOS |
| Nueva Indicación Predicha | Prinzmetal angina |
| Puntaje de Predicción TxGNN | 0.9984 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 1) |
| Número de Registros Sanitarios | al menos 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, olmesartán es un antagonista del receptor AT1 de angiotensina II con efectos vasodilatadores y antihipertensivos. Su eficacia en hipertensión está establecida, y mecanísticamente podría relacionarse con el vasoespasmo coronario.

La relación entre la indicación original (hipertensión, tratada con la combinación con diuréticos) y la angina de Prinzmetal es indirecta: ambas implican regulación del tono vascular. Sin embargo, esta conexión es especulativa. Los bloqueadores de los canales de calcio y los nitratos son el tratamiento establecido para la angina vasoespástica, y no se recuperó evidencia clínica ni bibliográfica de olmesartán en esta enfermedad.

El puntaje alto del modelo (0.9984) debe interpretarse con cautela: proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica ni prueba de eficacia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta indicación.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20103712 | OLMEDOXTAN H® 40MG/12.5MG | Tableta recubierta | Olmesartán medoxomilo y diuréticos | Vigente |

El único registro sanitario está cancelado, por lo que no hay producto vigente con olmesartán en Colombia según los datos compilados.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 94 interacciones en total. Entre las principales:
  - **Mayores**: cloruro de potasio y bicarbonato de potasio (riesgo de hiperpotasemia).
  - **Moderadas**: insulinas (varias presentaciones), exenatida, hidrocortisona, eluxadolina y polietilenglicol con electrolitos.
- Para advertencias y contraindicaciones, consultar el prospecto, ya que no se dispone de esta información en los datos compilados.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos ni publicaciones para angina de Prinzmetal. Además, existen terapias establecidas para esta condición y el único registro local está cancelado.

**Para avanzar se necesita:**
- Revisión de la literatura sobre bloqueadores del receptor AT1 y vasoespasmo coronario
- Datos del mecanismo de acción y análisis de la relación mecanística
- Prospecto de INVIMA para advertencias y contraindicaciones
- Estudios preclínicos o clínicos pilotos que evalúen olmesartán en angina vasoespástica
- Análisis de la viabilidad comercial dado el estado cancelado del registro

---

### Nota sobre otras indicaciones predichas

Entre las demás predicciones, con base en la evidencia disponible:
- **Migraña** (puntaje 0.9964, nivel L3): existe una revisión sistemática de 2019 sobre IECA y ARA-II, y un estudio de 2006 sobre olmesartán en pacientes hipertensos. El diseño no está confirmado y el candesartán tiene mejor evidencia. Es la candidata con mayor respaldo y podría plantearse como pregunta de investigación.
- **Hipertensión pulmonar** (0.9961, nivel L4): solo evidencia preclínica en ratas y ratones, sin datos en humanos.
- **Glaucoma de ángulo abierto** (0.9940, nivel L4): solo una revisión general, sin datos específicos de olmesartán.
- El resto (alopecia, hipotricosis, entre otras) son solo predicciones del modelo, sin base mecanística clara.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

