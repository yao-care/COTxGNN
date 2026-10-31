---
layout: default
title: Agomelatine
parent: Solo Predicción del Modelo (L5)
nav_order: 31
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-31
description: "Agomelatine: nueva indicación predicha, Tortícolis paroxística benigna de la infancia (nivel de evidencia L5). Indicación original: AGOMELATINA"
monitor_inn: "Agomelatine"
predicted_indications: ["benign paroxysmal torticollis of infancy", "agoraphobia", "neurotic disorder", "Ohdo syndrome and variants", "ligneous conjunctivitis", "blepharophimosis - intellectual disability syndrome, Ohdo type", "Keppen-Lubinsky syndrome"]
---

# Agomelatine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

## Agomelatina: De Antidepresivo (AGOMELATINA) a Tortícolis Paroxística Benigna de la Infancia
{: .text-alpha }

## Resumen en Una Frase

Agomelatina es un antidepresivo que actúa sobre los receptores de melatonina (MT1/MT2) y serotonina (5-HT2C), registrado en Colombia bajo el nombre comercial Valdoxan®.
El modelo TxGNN predice que podría ser efectivo para **tortícolis paroxística benigna de la infancia**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | AGOMELATINA (el registro sanitario no detalla la indicación; el uso conocido es el trastorno depresivo mayor) |
| Nueva Indicación Predicha | Tortícolis paroxística benigna de la infancia |
| Puntaje de Predicción TxGNN | 0.9996 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 1) |
| Número de Registros Sanitarios | al menos 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, agomelatina es agonista de los receptores de melatonina MT1 y MT2 y antagonista del receptor serotoninérgico 5-HT2C. Estos blancos también aparecen en los datos farmacológicos de interacciones (5-HT2A, 5-HT2B, 5-HT2C, MT1 y MT2).

**La predicción tiene una plausibilidad mecanística muy baja.** La tortícolis paroxística benigna de la infancia es un trastorno pediátrico autolimitado, a menudo asociado a variantes genéticas de canales iónicos (frecuentemente CACNA1A). No se identificó ninguna superposición con las vías melatoninérgicas o serotoninérgicas.

El puntaje alto del modelo (0.9996) refleja una predicción basada en la red de conocimiento, sin respaldo clínico o experimental. Debe interpretarse con cautela.

### Otras predicciones del modelo (contexto)

Estas candidatas se mencionan solo como contexto; no son el foco del informe:

| Indicación predicha | Puntaje TxGNN | Nivel | Comentario |
|------|------|------|------|
| Agorafobia | 0.9995 | L5 | Plausibilidad indirecta por la actividad ansiolítica en ansiedad generalizada; sin evidencia específica |
| Trastorno neurótico | 0.9990 | L4 | Categoría amplia y antigua; solo una revisión general de antidepresivos |

Las predicciones restantes (síndrome de Ohdo y variantes, conjuntivitis leñosa, síndrome de Keppen-Lubinsky) son solo predicciones sin vínculo mecanístico ni evidencia.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para tortícolis paroxística benigna de la infancia.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20014920 | VALDOXAN® 25 MG (LES LABORATOIRES SERVIER) | Comprimido | AGOMELATINA | Vigente |

---

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: la consulta se completó y devolvió 5 registros, todos de farmacología de blancos (no interacciones con otros medicamentos): receptores 5-HT2A, 5-HT2B, 5-HT2C, MT1 y MT2. No se identificaron interacciones medicamentosas con nivel de gravedad asignado.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no cuenta con ensayos clínicos ni literatura, carece de un vínculo mecanístico plausible con la enfermedad y el único registro sanitario en Colombia está cancelado. No hay base para avanzar.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA) y una hipótesis biológica que relacione los receptores MT1/MT2/5-HT2C con la fisiopatología de la enfermedad
- Obtención y revisión del prospecto de INVIMA (advertencias y contraindicaciones), necesaria antes de cualquier evaluación de seguridad
- Búsqueda de evidencia preclínica o clínica específica para esta indicación
- Verificación del estado regulatorio de agomelatina en otras jurisdicciones
- Considerar priorizar las indicaciones dentro del área depresiva (melancolía, distimia), que tienen evidencia indirecta de nivel L4, aunque no constituyen reposicionamiento real al estar cerca de la indicación original
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

