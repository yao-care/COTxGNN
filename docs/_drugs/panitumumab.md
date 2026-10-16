---
layout: default
title: Panitumumab
parent: Solo Predicción del Modelo (L5)
nav_order: 497
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Panitumumab: nueva indicación predicha, Osteoporosis inducida por fármacos (drug-induced osteoporosis) (nivel de evidencia L5). Indicación original: Panitumumab"
monitor_inn: "PANITUMUMAB"
predicted_indications: ["drug-induced osteoporosis", "severe nonproliferative diabetic retinopathy"]
---

# Panitumumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Panitumumab: De Indicación Registrada (sin texto descriptivo) a Osteoporosis Inducida por Fármacos

## Resumen en Una Frase

Panitumumab es un anticuerpo monoclonal anti-EGFR; su registro sanitario en Colombia (Vectibix®) no incluye un texto de indicación descriptivo y actualmente está cancelado.
El modelo TxGNN predice que podría ser efectivo para **osteoporosis inducida por fármacos**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Panitumumab (el registro solo repite el nombre del principio activo, sin indicación descrita) |
| Nueva Indicación Predicha | Osteoporosis inducida por fármacos (drug-induced osteoporosis) |
| Puntaje de Predicción TxGNN | 99.13% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, panitumumab es un anticuerpo monoclonal que bloquea el receptor del factor de crecimiento epidérmico (EGFR), usado en oncología.

La señalización de EGFR participa en la diferenciación de los osteoblastos y en la remodelación ósea, por lo que bloquearla podría afectar el metabolismo óseo. Sin embargo, este vínculo sugiere más bien un **posible efecto adverso** (por ejemplo, efectos óseos asociados a hipomagnesemia) que un beneficio terapéutico. La dirección del efecto (beneficio o daño) no está resuelta.

El puntaje alto de TxGNN (99.13%) es solo una predicción del modelo, sin respaldo de ensayos clínicos ni literatura. Por ello, debe interpretarse con cautela.

**Otra predicción del modelo:** retinopatía diabética no proliferativa grave (puntaje 99.05%, nivel L5, decisión Hold). Existe un vínculo especulativo por la transactivación de EGFR en la señalización vascular retiniana y las vías relacionadas con VEGF. Al ser un anticuerpo de administración sistémica con un perfil de toxicidad importante (dermatológica, hipomagnesemia) y sin datos oculares, el vínculo sigue siendo hipotético.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20025916 | VECTIBIX® 20 MG/ML (Amgen Europe B.V.) | Solución concentrada para infusión | PANITUMUMAB | Cancelado |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (anticuerpo monoclonal anti-EGFR) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Según la información conocida de la clase: electrolitos (especialmente magnesio y calcio), piel y función general; confirmar en el prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas:** se identificaron 27 interacciones; en los datos compilados se detallan 20.
  - **Mayores:** amiodarona, trióxido de arsénico, bevacizumab, dofetilida, dronedarona, droperidol, ácido aminolevulínico, irinotecán (incluido el liposomal) y levacetilmetadol.
  - **Moderadas:** inhibidores de la bomba de protones (rabeprazol, omeprazol, dexlansoprazol, esomeprazol, lansoprazol, pantoprazol), metoxaleno, ácido aminolevulínico tópico, disopiramida e idelalisib.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (L5), sin ensayos clínicos ni literatura. El vínculo mecanístico sugiere un posible daño óseo más que un beneficio, y el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto del INVIMA (advertencias y contraindicaciones), actualmente no disponible.
- Completar los datos del mecanismo de acción desde DrugBank.
- Aclarar la dirección del efecto (beneficio o daño) sobre el hueso mediante estudios preclínicos o revisión de la literatura.
- Verificar la situación regulatoria y la disponibilidad real del producto en Colombia.
- Evaluar la compatibilidad de vías de administración, ya que un anticuerpo sistémico podría no ser adecuado para las nuevas indicaciones.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

