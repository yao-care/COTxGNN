---
layout: default
title: Safinamide
parent: Solo Predicción del Modelo (L5)
nav_order: 578
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Safinamide: nueva indicación predicha, Encefalitis subaguda de Rasmussen (nivel de evidencia L5). Indicación original: SAFINAMIDA"
monitor_inn: "safinamide"
predicted_indications: ["Rasmussen subacute encephalitis", "myelitis", "PLA2G6-associated neurodegeneration"]
---

# Safinamide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Safinamida: De Enfermedad de Parkinson (SAFINAMIDA) a Encefalitis Subaguda de Rasmussen

## Resumen en Una Frase

Safinamida es un inhibidor reversible de la MAO-B; en el registro sanitario colombiano figura solo como "SAFINAMIDA", sin una indicación detallada.
El modelo TxGNN predice que podría ser efectivo para la **encefalitis subaguda de Rasmussen**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | SAFINAMIDA (el registro no detalla la indicación) |
| Nueva Indicación Predicha | Encefalitis subaguda de Rasmussen |
| Puntaje de Predicción TxGNN | 99.63% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo cancelado (sin registros vigentes) |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción original. Según la información conocida, safinamida es un inhibidor reversible de la MAO-B que además bloquea canales de sodio dependientes de voltaje e inhibe la liberación de glutamato. Estas propiedades podrían relacionarse, en teoría, con la excitotoxicidad y la actividad convulsiva de la encefalitis de Rasmussen.

Sin embargo, la relación es débil. La encefalitis de Rasmussen está causada principalmente por inflamación autoinmune mediada por linfocitos T, y safinamida no tiene una acción inmunomoduladora conocida. A lo sumo, podría ofrecer un efecto sintomático o neuroprotector secundario.

El único sustento es la puntuación del modelo TxGNN (0.996). La similitud con la indicación original no se ha evaluado, y la compatibilidad de vías de administración está pendiente (safinamida es de administración oral).

Otras predicciones del modelo, también solo con evidencia L5, son mielitis (99.46%) y neurodegeneración asociada a PLA2G6 (99.22%). Esta última tiene un vínculo sintomático algo más plausible por su componente parkinsoniano y dopaminérgico, aunque no modificaría la enfermedad de fondo.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20202462 | ZAFIMID 100MG. TABLETAS RECUBIERTAS | Tableta | SAFINAMIDA | Cancelado |
| 20202459 | ZAFIMID® 50MG | Tableta recubierta | SAFINAMIDA | Cancelado |

Ambos registros pertenecen a Laboratorios Legrand S.A. y están cancelados; actualmente no hay un producto vigente con safinamida en Colombia.

## Consideraciones de Seguridad

**Interacciones Farmacológicas**: se identificaron 110 interacciones en total. Entre las listadas:

- **Mayor**: bupropión.
- **Moderadas**: isometepteno, dietilpropión, fentermina, metoclopramida, rosuvastatina, y diversos antidiabéticos (clorpropamida, empagliflozina, glimepirida, nateglinida, repaglinida, acetohexamida) e insulinas (aspart, degludec, detemir, glargina, glulisina, humana isófana, humana regular e inhalada).

No se dispone de datos de advertencias ni de contraindicaciones del prospecto. Consultar el prospecto para esa información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (L5), sin ensayos clínicos ni literatura, y el mecanismo propuesto no aborda la causa autoinmune de la enfermedad. Además, no hay productos vigentes en Colombia y faltan datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA para las advertencias y contraindicaciones (brecha de seguridad bloqueante).
- Completar los datos del mecanismo de acción desde DrugBank.
- Buscar estudios preclínicos o series de casos de safinamida en encefalitis de Rasmussen y en las demás indicaciones predichas.
- Evaluar la viabilidad regulatoria y comercial, dado que los registros están cancelados.
- Valorar si neurodegeneración asociada a PLA2G6 sería una alternativa más plausible para un uso sintomático.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

