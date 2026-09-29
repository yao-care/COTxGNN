---
layout: default
title: Evolocumab
parent: Solo Predicción del Modelo (L5)
nav_order: 193
evidence_level: L5
indication_count: 6
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

# Evolocumab: De Reducción de LDL-C a Forma Sintomática de Hemofilia en Mujeres Portadoras

## Resumen en Una Frase

Evolocumab es un anticuerpo monoclonal que inhibe PCSK9 y se usa para reducir el colesterol LDL (LDL-C).
El modelo TxGNN predice que podría ser efectivo para la **forma sintomática de hemofilia en mujeres portadoras**,
pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción, que se basa solo en el grafo de conocimiento.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No registrada de forma explícita (el campo de indicación en INVIMA solo repite "EVOLOCUMAB"); por su mecanismo, reducción de LDL-C |
| Nueva Indicación Predicha | Forma sintomática de hemofilia en mujeres portadoras |
| Puntaje de Predicción TxGNN | 99.82% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 14 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

El registro del fármaco no incluye datos del mecanismo de acción ni de la indicación original. Según lo que se sabe del fármaco, evolocumab es un anticuerpo monoclonal que neutraliza PCSK9. Con ello favorece el reciclaje del receptor de LDL y reduce el LDL-C.

**No se identifica un vínculo mecanístico plausible** con la nueva indicación. Evolocumab no tiene efecto conocido sobre los niveles de factor VIII o IX ni sobre la cascada de coagulación, que son la base de la hemofilia. El puntaje alto (0.998) refleja cercanía en el grafo de conocimiento, no una razón biológica ni datos clínicos.

Por eso esta predicción debe leerse como una señal computacional sin respaldo, no como una hipótesis terapéutica.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20087350 | REPATHA® 140 MG/ML (AMGEN MANUFACTURING LIMITED LLC) | Solución inyectable | Solo figura el nombre del principio activo (EVOLOCUMAB); no hay texto de indicación |

Nota: el sistema reporta 14 registros en total, pero los datos recibidos solo contienen entradas duplicadas del registro 20087350, por lo que se muestra una sola vez.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos ni literatura para esta indicación (nivel L5), y tampoco hay un mecanismo biológico que la sustente. El puntaje TxGNN por sí solo no basta para avanzar. Las otras cinco predicciones del modelo también tienen nivel L5 y ninguna cuenta con evidencia clínica.

**Para avanzar se necesita:**
- Un vínculo mecanístico plausible entre la inhibición de PCSK9 y la hemofilia, que hoy no existe
- Búsqueda dirigida de estudios preclínicos o clínicos que relacionen PCSK9 con la coagulación
- Datos del prospecto de INVIMA (advertencias y contraindicaciones), pendientes de obtener
- Datos del mecanismo de acción desde DrugBank para completar el registro
- Texto real de la indicación aprobada en Colombia, ya que el campo actual solo contiene el nombre del fármaco
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

