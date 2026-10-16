---
layout: default
title: Evolocumab
parent: Solo Predicción del Modelo (L5)
nav_order: 275
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Evolocumab: nueva indicación predicha, Forma sintomática de hemofilia en mujeres portadoras (nivel de evidencia L5). Indicación original: Evolocumab"
---

# Evolocumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Evolocumab: De Hipercolesterolemia (LDL-C elevado) a Forma sintomática de hemofilia en mujeres portadoras

## Resumen en Una Frase

Evolocumab es un anticuerpo monoclonal que inhibe PCSK9 y se utiliza para reducir el colesterol LDL en pacientes con hipercolesterolemia que no logran controlarlo con los tratamientos disponibles.
El modelo TxGNN predice que podría ser efectivo para la **forma sintomática de hemofilia en mujeres portadoras**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Evolocumab (el registro sanitario solo indica el nombre del principio activo; según la información farmacológica disponible, se usa en hipercolesterolemia) |
| Nueva Indicación Predicha | Forma sintomática de hemofilia en mujeres portadoras |
| Puntaje de Predicción TxGNN | 99.82% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registro vigente) |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción dentro de los datos compilados para este reporte. Según la información farmacológica conocida, evolocumab es un anticuerpo monoclonal dirigido contra la proproteína convertasa subtilisina/kexina tipo 9 (PCSK9). Al bloquearla, preserva los receptores hepáticos de LDL y reduce el colesterol LDL.

La relación con la nueva indicación es débil. La hemofilia en mujeres portadoras es un trastorno ligado al cromosoma X causado por deficiencia de factor VIII o IX, y no tiene un vínculo mecanístico plausible con la inhibición de PCSK9. El alto puntaje de TxGNN (0.998) parece ser un artefacto del grafo de conocimiento, sin sustento biológico.

Por lo tanto, esta predicción no debe interpretarse como una hipótesis terapéutica creíble sin evidencia adicional.

Otras indicaciones predichas, todas con evidencia L5 y recomendación Hold:

| Indicación Predicha | Puntaje TxGNN | Comentario |
|------|------|------|
| Deficiencia familiar de apolipoproteína C-II | 99.50% | Conexión tenue con el metabolismo lipídico; la inhibición de PCSK9 no corrige el defecto de activación de la lipoproteína lipasa |
| Púrpura trombocitopénica | 99.42% | Sin conexión mecanística conocida |
| Deficiencia de factor XI | 99.29% | Sin acción conocida sobre la cascada de coagulación |
| Hemofilia A con anomalía vascular | 99.22% | Vía no relacionada con PCSK9 |
| Enfermedad de actividad catalítica | 99.08% | Término inespecífico de ontología; no evaluable como indicación clínica |

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
| 20087350 | REPATHA® 140 MG/ML | Solución inyectable | EVOLOCUMAB | Cancelado |

El único registro sanitario (fabricante: Amgen Manufacturing Limited LLC) está cancelado, por lo que actualmente no hay producto vigente en Colombia.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: La consulta se completó con 1 registro, que corresponde a la interacción farmacológica con su diana, PCSK9 (proproteína convertasa subtilisina/kexina tipo 9). Es una relación de farmacología (unión del anticuerpo a su diana) y no una interacción medicamentosa clínica con nivel de gravedad asignado.

Para advertencias y contraindicaciones, consultar el prospecto, ya que no se dispone de esa información en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Las seis indicaciones predichas carecen de ensayos clínicos y de literatura (nivel L5), y no existe un vínculo mecanístico plausible entre la inhibición de PCSK9 y la hemofilia en portadoras. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), que es un vacío de información bloqueante para el tamizaje de seguridad
- Completar los datos del mecanismo de acción desde DrugBank
- Aclarar la indicación original aprobada, ya que el registro solo menciona el nombre del principio activo
- Reevaluar la utilidad de las predicciones; solo la deficiencia de apolipoproteína C-II tiene una conexión biológica tenue y podría justificar una revisión de literatura preliminar
- Confirmar la situación de comercialización en Colombia (registro cancelado)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

