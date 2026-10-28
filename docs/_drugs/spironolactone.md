---
layout: default
title: Spironolactone
parent: Solo Predicción del Modelo (L5)
nav_order: 591
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Spironolactone: nueva indicación predicha, Hipotricosis simple del cuero cabelludo (nivel de evidencia L5). Indicación original: ESPIRONOLACTONA"
monitor_inn: "Spironolactone"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia"]
---

# Spironolactone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Espironolactona: De Espironolactona (registro INVIMA) a Hipotricosis simple del cuero cabelludo
{: .text-alpha }

## Resumen en Una Frase

La espironolactona es un antagonista del receptor de mineralocorticoides, registrado en Colombia bajo el nombre del principio activo (sin una indicación detallada en los registros). Se utiliza clínicamente en hipertensión, hipopotasemia, síndrome de Conn e insuficiencia cardíaca.
El modelo TxGNN predice que podría ser efectiva para **hipotricosis simple del cuero cabelludo**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección (solo predicción del modelo).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | ESPIRONOLACTONA (el registro INVIMA no detalla la indicación) |
| Nueva Indicación Predicha | Hipotricosis simple del cuero cabelludo |
| Puntaje de Predicción TxGNN | 0.9926 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 2) |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados no incluyen una descripción detallada del mecanismo de acción. Según la información farmacológica disponible, la espironolactona actúa sobre el receptor de mineralocorticoides (gen NR3C2) y se usa en hipertensión de renina baja, hipopotasemia, síndrome de Conn e insuficiencia cardíaca de clase III-IV.

Además, tiene actividad antiandrogénica (bloqueo del receptor de andrógenos y menor síntesis de andrógenos). Por eso se emplea fuera de indicación en alopecia androgenética y pérdida de cabello de patrón femenino, lo que da un vínculo plausible pero indirecto con las condiciones de pérdida de cabello.

Sin embargo, la hipotricosis simple del cuero cabelludo es un trastorno hereditario raro causado por variantes genéticas (por ejemplo, CDSN, APCDD1, RPL21), y su patogénesis no depende de andrógenos. El puntaje alto de TxGNN (0.9926) es solo una predicción del modelo; no hay datos mecanísticos que respalden un beneficio antiandrogénico en esta condición. Otra predicción del modelo, la hipotricosis congénita con milia (puntaje 0.9904), tiene un vínculo igualmente especulativo y probablemente refleja la cercanía en la red entre fenotipos de hipotricosis más que un mecanismo validado.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 19933407 | DOXICLAT® TABLETA. | Tableta | ESPIRONOLACTONA | Vigente |
| 49664 | ALDACTONE® TABLETAS 25 MG | Tableta | ESPIRONOLACTONA | Vigente |

Ningún registro se encuentra vigente actualmente.

---

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no según el prospecto):** enfermedad renal, anuria, pancreatitis, lupus eritematoso sistémico (incluido el pediátrico), deficiencia de potasio, diabetes mellitus, cetoacidosis diabética, hiperuricemia, gota, hiperparatiroidismo, osteítis fibrosa, coma hepático, encefalopatía hepática, ictericia neonatal, hipercalcemia, nefrocalcinosis, trastornos del metabolismo del fósforo y piouréter.
- **Interacciones farmacológicas:** solo se registra la interacción farmacológica con el receptor de mineralocorticoides (su blanco terapéutico), sin nivel de gravedad asignado. No hay datos de interacciones con otros fármacos.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura. Además, la patogénesis genética de la hipotricosis simple no es androgénica, por lo que el vínculo mecanístico es débil. Los registros colombianos están cancelados.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones) para completar la evaluación de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una revisión de literatura y de registros de ensayos sobre espironolactona en hipotricosis hereditarias.
- Evaluar la compatibilidad de vías de administración (probablemente tópica para el cuero cabelludo, frente a la forma oral disponible).
- Aclarar la situación regulatoria, dado que ambos registros están cancelados.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

