---
layout: default
title: Avibactam
parent: Solo Predicción del Modelo (L5)
nav_order: 79
evidence_level: L5
indication_count: 4
monitor_inn: "avibactam"
predicted_indications: ["ureter tuberculosis", "urinary schistosomiasis", "polyclonal hyperviscosity syndrome", "hyperamylasemia"]
last_modified_at: 2026-10-28
description: "Avibactam: nueva indicación predicha, Tuberculosis del uréter (ureter tuberculosis) (nivel de evidencia L5). Indicación original: CEFTAZIDIMA E INHIBIDOR DE BETALACTAMASA"
---

# Avibactam
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

## Avibactam: Tuberculosis del uréter (ureter tuberculosis)
{: .text-alpha }

## Resumen en Una Frase

Avibactam es un inhibidor de betalactamasas que se utiliza únicamente en combinación con ceftazidima (producto ZAVICEFTA) para el tratamiento de infecciones bacterianas.
El modelo TxGNN predice que podría ser efectivo para **tuberculosis del uréter**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | CEFTAZIDIMA E INHIBIDOR DE BETALACTAMASA |
| Nueva Indicación Predicha | Tuberculosis del uréter (ureter tuberculosis) |
| Puntaje de Predicción TxGNN | 0.9911 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, avibactam es un inhibidor de betalactamasas de la familia de los diazabiciclooctanos, que se usa solo junto con ceftazidima y no tiene actividad antibacteriana intrínseca relevante frente a la mayoría de los organismos.

El vínculo con la tuberculosis del uréter es débil y especulativo. Algunos trabajos de laboratorio (in vitro) sugieren que avibactam puede inhibir la betalactamasa BlaC de *Mycobacterium tuberculosis*, lo que en teoría podría restaurar la actividad de los betalactámicos. Sin embargo, es una observación de laboratorio, sin respaldo de datos clínicos en tuberculosis del tracto urinario.

Es probable que el puntaje alto del modelo se deba a la asociación en la red de conocimiento con indicaciones de infección urinaria, y no a la biología de la tuberculosis. Por ello, el puntaje debe interpretarse con mucha cautela.

Otras predicciones del modelo, con la misma ausencia de evidencia, son:
- **Esquistosomiasis urinaria** (0.9906): no se identificó un vínculo mecanístico plausible; probablemente refleja el contexto urinario compartido.
- **Síndrome de hiperviscosidad policlonal** (0.9901): sin vínculo mecanístico; probable artefacto del modelo TxGNN (aprendizaje profundo).
- **Hiperamilasemia** (0.9901): es un hallazgo de laboratorio, no una enfermedad tratable con un inhibidor antibacteriano; posible relación espuria o señal de evento adverso.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20157002 | ZAVICEFTA | Polvo estéril para reconstituir a solución inyectable | Ceftazidima e inhibidor de betalactamasa |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún ensayo clínico ni publicación que estudie esta enfermedad con avibactam; la predicción se apoya solo en el modelo (nivel L5) y el vínculo mecanístico es especulativo. Además, avibactam se usa exclusivamente en combinación con ceftazidima.

**Para avanzar se necesita:**
- Datos del mecanismo de acción desde DrugBank
- Prospecto de INVIMA con advertencias y contraindicaciones
- Estudios preclínicos que confirmen la actividad frente a *M. tuberculosis* (inhibición de BlaC) en el contexto urinario
- Evidencia clínica o ensayos en tuberculosis genitourinaria antes de considerar cualquier avance
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

