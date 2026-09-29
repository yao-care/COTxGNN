---
layout: default
title: Olanzapine
parent: Solo Predicción del Modelo (L5)
nav_order: 302
evidence_level: L5
indication_count: 3
---

# Olanzapine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Olanzapina: De Antipsicótico (Esquizofrenia y Trastorno Bipolar) a Tortícolis Paroxística Benigna de la Infancia

## Resumen en Una Frase

La olanzapina es un antipsicótico utilizado para tratar la esquizofrenia y el trastorno bipolar.
El modelo TxGNN predice que podría ser efectiva para la **tortícolis paroxística benigna de la infancia**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es solo una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | El registro sanitario solo dice "Olanzapina", sin indicación específica. Según la fuente farmacológica: esquizofrenia, otras enfermedades psicóticas y trastorno bipolar |
| Nueva Indicación Predicha | Tortícolis paroxística benigna de la infancia |
| Puntaje de Predicción TxGNN | 99.54% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción formal de la olanzapina. Los datos farmacológicos muestran que el fármaco interactúa con varios receptores: serotonina (5-HT1A, 1B, 1D, 1E, 1F, 2A, 2C, 6 y 7), dopamina D2, histamina H1 y adrenérgicos α1A y α1D. Solo se documenta expresamente el antagonismo del receptor α1A, asociado a la hipotensión ortostática.

La tortícolis paroxística benigna de la infancia es una condición pediátrica rara y autolimitada. Suele asociarse a variantes del gen CACNA1A y al espectro de la migraña. No hay una relación mecanística clara con el uso original de la olanzapina, que son las enfermedades psiquiátricas del adulto.

Por eso el puntaje de 99.54% proviene únicamente de la predicción basada en grafos de conocimiento del modelo, sin estudios que lo respalden. Además, usar un antipsicótico en lactantes plantearía preocupaciones de seguridad importantes, por lo que requeriría una justificación muy sólida.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

Se muestran los registros distintos entre los 5 primeros devueltos (el registro 19974414 aparecía repetido).

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19974414 | OLANZAPINA 5 MG TABLETAS RECUBIERTAS (Laboratorios La Santé S.A.) | Tableta recubierta | OLANZAPINA (el texto del registro no detalla la indicación) |
| 19968710 | PROLANZ® FAST 10 MG (Eurofarma Colombia S.A.S) | Tableta dispersable | OLANZAPINA (el texto del registro no detalla la indicación) |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la consulta se completó con 13 registros, pero corresponden a unión con receptores (datos farmacológicos), no a interacciones con otros medicamentos. Los receptores son 5-HT1A, 5-HT1B, 5-HT1D, 5-HT1E, 5-HT1F, 5-HT2A, 5-HT2C, 5-HT6, 5-HT7, α1A, α1D, D2 y H1. El antagonismo α1A se asocia con hipotensión ortostática (datos en ratas).
- **Población pediátrica**: el uso de un antipsicótico en lactantes exigiría una evaluación de seguridad muy rigurosa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni publicaciones, no existe una justificación mecanística y la indicación afecta a lactantes, donde el perfil de seguridad de un antipsicótico es preocupante. El puntaje del modelo por sí solo no basta para avanzar.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA para obtener advertencias y contraindicaciones (brecha bloqueante para el tamizaje de seguridad).
- Obtener el mecanismo de acción desde DrugBank.
- Buscar evidencia mecanística que conecte la olanzapina con la tortícolis paroxística benigna (variantes de CACNA1A, espectro de migraña).
- Evaluar la seguridad en población pediátrica antes de cualquier consideración clínica.
- Priorizar las otras indicaciones predichas para este fármaco, que tienen más respaldo: **agorafobia** (L3, con un ensayo abierto de 12 semanas en trastorno de pánico resistente y reportes de caso) y **trastorno distímico** (L4, evidencia indirecta). Ambas figuran como "Research Question".

*Este informe es solo de referencia para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

