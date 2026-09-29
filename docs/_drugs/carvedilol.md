---
layout: default
title: Carvedilol
parent: Solo Predicción del Modelo (L5)
nav_order: 115
evidence_level: L5
indication_count: 5
---

# Carvedilol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Carvedilol: De Indicación Original No Especificada a Hipertensión Renovascular Maligna

## Resumen en Una Frase

Carvedilol es un betabloqueador no selectivo con bloqueo alfa-1 y efecto vasodilatador. El registro sanitario colombiano no especifica su indicación original, porque el campo solo repite el nombre del principio activo.
El modelo TxGNN predice que podría ser efectivo para **hipertensión renovascular maligna**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro solo dice "CARVEDILOL") |
| Nueva Indicación Predicha | Hipertensión renovascular maligna |
| Puntaje de Predicción TxGNN | 99.55% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según el conocimiento general, carvedilol bloquea los receptores beta y alfa-1 adrenérgicos, lo que dilata los vasos y reduce la presión arterial. Además, el bloqueo beta disminuye la liberación de renina, un mecanismo relevante en la hipertensión de origen renovascular.

Esto da una plausibilidad biológica razonable para bajar la presión arterial. Sin embargo, no hay ensayos ni literatura para esta indicación, así que el puntaje de 99.55% es solo una predicción del modelo. La hipertensión maligna es una emergencia hipertensiva que normalmente se maneja con fármacos intravenosos titulables, por lo que un fármaco oral como carvedilol difícilmente sería de primera línea.

Las dos primeras predicciones (hipertensión renovascular maligna y enfermedad renal hipertensiva maligna) tienen puntajes idénticos. Probablemente son nodos muy cercanos en el grafo de conocimiento y no deben contarse como señales independientes.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 218019 | DILATREND TABLETAS 6.25MG (CHEPLAPHARM ARZNEIMITTEL GMBH) | Tableta | No detallada (solo indica "CARVEDILOL") |

Se reportan 20 registros en total, pero los datos recibidos solo incluyen este registro (repetido cinco veces). Las formas farmacéuticas disponibles son orales: tableta y tableta recubierta.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ensayos clínicos ni literatura, por lo que se queda en nivel L5 como pregunta de investigación. Además, la hipertensión maligna se maneja normalmente con fármacos intravenosos, no con carvedilol oral.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA para completar advertencias y contraindicaciones, que hoy bloquean el tamizaje de seguridad.
- Completar los datos de mecanismo de acción (por ejemplo, desde DrugBank).
- Confirmar la indicación aprobada real de carvedilol en Colombia.
- Hacer una búsqueda dirigida de literatura sobre carvedilol e hipertensión renovascular o maligna. Los estudios recuperados para otras predicciones hablan de hipoxia en general y no mencionan carvedilol.
- Tener en cuenta que las otras cuatro predicciones también son L5. Las dos de hipertensión pulmonar y Braddock quedan en Hold, y en hipertensión pulmonar hay además una preocupación de seguridad por el bloqueo beta no selectivo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

