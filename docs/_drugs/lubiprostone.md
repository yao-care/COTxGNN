---
layout: default
title: Lubiprostone
parent: Solo Predicción del Modelo (L5)
nav_order: 268
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Lubiprostona: De Indicación No Especificada en el Registro a Alopecia

## Resumen en Una Frase

Lubiprostona es un activador del canal de cloruro ClC-2, derivado bicíclico del ácido graso PGE1, comercializado en Colombia como MOVIPROST® 8 mcg. El registro sanitario solo consigna el nombre del principio activo y no incluye el texto de la indicación original.
El modelo TxGNN predice que podría ser efectivo para **alopecia**, pero hay **0 ensayos clínicos** y **0 publicaciones** que lo respalden. Se trata de una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro solo indica "LUBIPROSTONE") |
| Nueva Indicación Predicha | Alopecia |
| Puntaje de Predicción TxGNN | 99.93% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos formales del mecanismo de acción original en el Evidence Pack. Según el análisis de razonamiento incluido, lubiprostona es un activador del canal de cloruro ClC-2 y un ácido graso bicíclico derivado de la PGE1, con acción local en el intestino y absorción sistémica mínima.

El único vínculo especulativo es que los análogos de prostaglandinas de receptor FP (por ejemplo, bimatoprost) pueden influir en el crecimiento del cabello. Sin embargo, lubiprostona no tiene actividad establecida sobre el receptor FP ni sobre el folículo piloso. Por eso el puntaje de 99.93% debe leerse como una asociación del grafo de conocimiento y no como evidencia farmacológica.

Las demás predicciones del modelo tampoco tienen respaldo real. Incluyen otras formas de alopecia e hipotricosis, hipertensión pulmonar, enfermedad de Raynaud, enfermedad vascular periférica, feocromocitoma y cardiopatía cifoescoliótica. Todas están en nivel L5 y sin literatura. El único ensayo vinculado, en hipertensión pulmonar (NCT02813369), corresponde a otro fármaco (naloxegol) y no es utilizable como evidencia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Los cinco registros devueltos corresponden al mismo número de registro sanitario, por lo que se muestra una sola fila. El total informado es de 20 registros.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20057095 | MOVIPROST® 8 MCG (TECNOQUÍMICAS S.A.) | Cápsula blanda | Solo figura el nombre "LUBIPROSTONE", sin texto de indicación |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún ensayo ni publicación para alopecia, y el vínculo mecanístico es especulativo. La absorción sistémica mínima de lubiprostona hace poco probable un efecto sobre el folículo piloso. La predicción no tiene respaldo más allá del modelo (L5).

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA (advertencias y contraindicaciones), un vacío bloqueante para el tamizaje de seguridad
- Completar el mecanismo de acción desde DrugBank
- Confirmar la indicación original aprobada en Colombia, ya que el registro solo trae el nombre
- Realizar estudios preclínicos, por ejemplo en folículo piloso o modelos de alopecia, antes de considerar cualquier ensayo clínico
- Evaluar la compatibilidad de vía de administración, hoy pendiente, ya que el producto es oral y la alopecia suele requerir acción tópica o sistémica

*Estos resultados son solo para referencia de investigación y no constituyen consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

