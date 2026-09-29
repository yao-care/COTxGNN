---
layout: default
title: Lorlatinib
parent: Solo Predicción del Modelo (L5)
nav_order: 264
evidence_level: L5
indication_count: 10
---

# Lorlatinib
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

# Lorlatinib: De Cáncer de Pulmón de Células No Pequeñas ALK-positivo a Fibromatosis Gingival

## Resumen en Una Frase

Lorlatinib es un inhibidor macrocíclico de tirosina quinasa (ALK/ROS1) de tercera generación, usado originalmente para el cáncer de pulmón de células no pequeñas (CPCNP) ALK-positivo.
El modelo TxGNN predice que podría ser efectivo para **fibromatosis gingival**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | CPCNP ALK-positivo (el registro sanitario solo consigna el texto "LORLATINIB", sin indicación explícita) |
| Nueva Indicación Predicha | Fibromatosis gingival |
| Puntaje de Predicción TxGNN | 99.81% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 8 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, lorlatinib es un inhibidor de las quinasas ALK y ROS1. Su eficacia en el CPCNP con reordenamientos de ALK o ROS1 está bien documentada.

**No se identificó un vínculo mecanístico** con la fibromatosis gingival. Esta es una enfermedad de sobrecrecimiento fibroso de las encías y no se conoce como un proceso impulsado por ALK o ROS1. El puntaje alto de TxGNN (0.998; posición 2110 en el ranking del modelo) proviene solo de patrones del grafo de conocimiento. No lo respalda ningún estudio clínico ni publicación.

Por lo tanto, esta predicción debe tratarse como una hipótesis sin sustento actual. Que el puntaje sea alto no equivale a que exista evidencia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

El fabricante de ambos registros es PFIZER S.A.S. El Evidence Pack repite varias veces el registro 20210581, por lo que aquí aparece una sola vez. El total informado es de 8 registros sanitarios.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20210581 | LORBRENA® 25 MG | Tableta recubierta | LORLATINIB (el registro solo indica el principio activo) |
| 20209759 | LORBRENA® 100 MG | Tableta recubierta | LORLATINIB (el registro solo indica el principio activo) |

## Citotoxicidad

Lorlatinib se clasifica como antineoplásico por su uso en cáncer de pulmón.

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasa ALK/ROS1) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | La literatura recuperada describe hiperlipidemia y alteraciones metabólicas, toxicidad pulmonar (incluido síndrome de dificultad respiratoria aguda), síndrome nefrótico y efectos sobre el sistema nervioso central. Se sugiere vigilar perfil lipídico, función renal, síntomas respiratorios y estado neurocognitivo, según el prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto y las regulaciones locales de manejo de antineoplásicos |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No hay datos de interacciones farmacológicas en la consulta realizada.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ensayos clínicos ni publicaciones que la respalden (nivel L5). Además, no existe un vínculo mecanístico plausible entre la inhibición de ALK/ROS1 y la fibromatosis gingival.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA para completar el tamizaje de seguridad (brecha bloqueante)
- Complementar los datos de mecanismo de acción desde DrugBank
- Buscar evidencia preclínica que relacione las vías ALK/ROS1 con la fibromatosis gingival
- Considerar otras predicciones del mismo fármaco con mejor sustento. Por ejemplo, "carcinoma del hilio pulmonar" (L4) se apoya en un reporte de caso de lorlatinib neoadyuvante en cáncer de pulmón ALK-positivo. Aun así, esta es una pregunta de investigación sobre un uso ya aprobado y no un reposicionamiento a una enfermedad nueva.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

