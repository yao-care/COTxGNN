---
layout: default
title: Lubiprostone
parent: Solo Predicción del Modelo (L5)
nav_order: 416
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Lubiprostone: nueva indicación predicha, Alopecia (nivel de evidencia L5). Indicación original: Lubiprostona"
monitor_inn: "LUBIPROSTONE"
predicted_indications: ["alopecia", "congenital hypotrichosis milia", "hypotrichosis simplex of the scalp", "diffuse alopecia areata", "pulmonary hypertension", "kyphoscoliotic heart disease", "Raynaud disease", "pulmonary hypertension, primary, autosomal recessive", "phaeochromocytoma", "peripheral vascular disease"]
---

# Lubiprostone
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

## Lubiprostona: De Estreñimiento Crónico a Alopecia
{: .text-alpha }

## Resumen en Una Frase

Lubiprostona es un activador del canal de cloruro ClC-2, conocido como agente de la clase de las prostonas, que cuenta con registros sanitarios en Colombia (actualmente cancelados) y cuyo uso clínico conocido es el tratamiento del estreñimiento crónico y del síndrome de intestino irritable.
El modelo TxGNN predice que podría ser efectivo para **alopecia**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Lubiprostona (el registro sanitario solo consigna el nombre del principio activo, sin texto de indicación detallado) |
| Nueva Indicación Predicha | Alopecia |
| Puntaje de Predicción TxGNN | 0.9993 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 2) |
| Número de Registros Sanitarios | 2 (0 vigentes, 2 cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este reporte. Según la información farmacológica conocida, lubiprostona es un activador del canal de cloruro ClC-2 (gen CLCN2), derivado de un metabolito de la prostaglandina E1, y se usa en estreñimiento crónico y síndrome de intestino irritable.

La relación con la alopecia es especulativa. La señalización de las prostaglandinas influye en el ciclo del cabello (los análogos de PGF2α favorecen el crecimiento y la PGD2 lo inhibe), pero no existe evidencia directa que vincule la activación de ClC-2 con la biología del folículo piloso. El puntaje alto de TxGNN refleja únicamente proximidad en la red de conocimiento.

Otras predicciones de la lista (hipotricosis congénita, hipotricosis simple del cuero cabelludo y alopecia areata difusa) parecen derivarse de la cercanía con otros fenotipos de pérdida de cabello. En la alopecia areata, de naturaleza autoinmune (vía JAK/STAT), lubiprostona no tiene acción inmunomoduladora conocida. Para hipertensión pulmonar, enfermedad de Raynaud y enfermedad vascular periférica existe un argumento débil por la clase de las prostanoides vasodilatadores, pero lubiprostona tiene absorción sistémica mínima y no se ha demostrado que actúe sobre receptores IP ni que produzca vasodilatación.

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
| 20057095 | MOVIPROST® 8 MCG | Cápsula blanda | LUBIPROSTONE | Vigente |
| 20028573 | MODULEX 24 MCG | Cápsula blanda | CARBONO DIOXIDO PRODUCTOS FARMACOLOGICOS | Vigente |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: Se identificó una interacción de nivel **moderado** con **idelalisib** (fuente: DDInter). Además, la base farmacológica confirma como blanco principal el canal ClC-2 (CLCN2), sin que esto constituya una interacción con otro fármaco.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para alopecia se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y sin vínculo mecanístico directo entre la activación de ClC-2 y el folículo piloso. Además, no hay registros sanitarios vigentes en Colombia.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA para completar la revisión de advertencias y contraindicaciones (vacío bloqueante para el tamizaje de seguridad)
- Completar los datos del mecanismo de acción desde DrugBank
- Estudios preclínicos que evalúen el efecto de lubiprostona o de la vía ClC-2/prostanoides en el folículo piloso
- Evaluar la compatibilidad de vía de administración (la forma actual es oral en cápsula blanda, mientras que la alopecia suele requerir abordaje tópico o dirigido)
- Aclarar la situación regulatoria, dado que los dos registros están cancelados
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

