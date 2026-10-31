---
layout: default
title: Adapalene
parent: Solo Predicción del Modelo (L5)
nav_order: 28
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-31
description: "Adapalene: nueva indicación predicha, Zinc plasmático elevado (nivel de evidencia L5). Indicación original: Adapaleno"
monitor_inn: "ADAPALENE"
predicted_indications: ["zinc, elevated plasma"]
---

# Adapalene
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

## Adapaleno: De Indicación Dermatológica Tópica a Zinc Plasmático Elevado
{: .text-alpha }

## Resumen en Una Frase

Adapaleno es un retinoide tópico de tercera generación, comercializado en Colombia en geles tópicos (por ejemplo, Differin® Gel).
El modelo TxGNN predice que podría ser efectivo para **zinc plasmático elevado**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Adapaleno (el registro sanitario no detalla la indicación; solo menciona el principio activo) |
| Nueva Indicación Predicha | Zinc plasmático elevado |
| Puntaje de Predicción TxGNN | 0.9951 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 2) |
| Número de Registros Sanitarios | al menos 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, el adapaleno es un retinoide tópico que se une selectivamente a los receptores RAR-beta y RAR-gamma, y modula la diferenciación de los queratinocitos y la inflamación cutánea.

La relación con la nueva indicación es débil. El zinc plasmático elevado es un hallazgo sistémico (por ejemplo, por suplementación excesiva, hemoconcentración o alteraciones renales o del transporte de zinc) y no una enfermedad con una vía evidente que responda a retinoides. Una posible conexión indirecta, como la interacción entre el retinol, su proteína transportadora y el zinc, es especulativa y no tiene respaldo en los datos disponibles.

Además, el adapaleno tópico tiene baja absorción sistémica, lo que hace aún menos plausible un efecto sobre el zinc plasmático. El puntaje del modelo TxGNN (aprendizaje profundo) (0.9951) puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica, y no existe un vínculo mecanístico establecido.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 208651 | Differin® Gel | Gel tópico | Adapalene | Vigente |
| 19996391 | Zudenina® Plus Gel | Gel tópico | Adapaleno. Combinaciones | Vigente |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: respuesta fotoparoxística, enfermedad por fotosensibilidad, dermatitis exfoliativa y dermatitis.
- **Interacciones farmacológicas**: se identificaron 58 interacciones potenciales, todas con nivel de gravedad no clasificado ("desconocido"). Entre las incluidas en los datos figuran:
  - Antibióticos: doxiciclina, tetraciclina, minociclina, metronidazol
  - Inhibidores de la bomba de protones y antiácidos: omeprazol, pantoprazol, rabeprazol, ranitidina
  - Corticoides: prednisona, triamcinolona, budesonida
  - Antihistamínicos: cetirizina, loratadina, fexofenadina
  - Otros: ibuprofeno, fluconazol, clopidogrel, bupropión, loperamida, escopolamina

Para advertencias y contraindicaciones según la etiqueta, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico plausible entre un retinoide tópico de baja absorción sistémica y el zinc plasmático elevado. Además, los dos registros sanitarios en Colombia están cancelados.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones)
- Completar los datos del mecanismo de acción desde DrugBank
- Revisión de literatura que explore una posible relación entre retinoides y homeostasis del zinc
- Evaluar si la vía tópica es compatible con una indicación sistémica, dada la baja absorción
- Confirmar la relevancia clínica de la indicación predicha antes de invertir en estudios adicionales
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

