---
layout: default
title: Bromazepam
parent: Solo Predicción del Modelo (L5)
nav_order: 99
evidence_level: L5
indication_count: 1
---

# Bromazepam
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Bromazepam: De Ansiolítico (benzodiacepina) a Trastorno de Migraña

## Resumen en Una Frase

Bromazepam es una benzodiacepina comercializada en Colombia como Lexotan. El registro sanitario solo repite el nombre del fármaco y no detalla la indicación aprobada. El modelo TxGNN predice que podría ser efectivo para **trastorno de migraña**, pero solo hay **1 ensayo clínico** indirecto y **ninguna publicación** que respalde esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto solo dice "BROMAZEPAM"); por su clase, se entiende como ansiolítico |
| Nueva Indicación Predicha | Trastorno de migraña |
| Puntaje de Predicción TxGNN | 99.06% |
| Nivel de Evidencia | L5 (el paquete de evidencia indica L4, pero no hay estudios preclínicos ni de mecanismo; el único ensayo es indirecto) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 13 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Bromazepam es una benzodiacepina. Esta clase suele entenderse como moduladora alostérica positiva de los receptores GABA-A, con efectos ansiolíticos, sedantes y relajantes musculares.

Un vínculo con la migraña solo sería indirecto, por ejemplo a través de la ansiolisis, la relajación muscular o la sedación. Los datos disponibles no respaldan ningún mecanismo específico para migraña, y las benzodiacepinas no están establecidas como tratamiento de esta enfermedad.

El puntaje de 0.99 es solo una predicción computacional y no está corroborado por evidencia clínica. Por eso conviene tratarlo como una hipótesis inicial, no como una señal de eficacia.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04410536](https://clinicaltrials.gov/study/NCT04410536) | Fase 4 | Completado | 25 | Programa de retirada domiciliaria con abordaje conductual en cefalea por abuso de medicación durante la emergencia de Covid-19; evalúa recaídas al año |

Este ensayo es evidencia indirecta (relevancia C). Trata la cefalea por abuso de medicación, una condición relacionada con la migraña. Los datos no muestran que bromazepam sea el fármaco en estudio ni que se haya probado como tratamiento de migraña. Además, es pequeño y no es un ECA de Fase 2 o 3.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19920700 | LEXOTAN TABLETAS 3 MG (CHEPLAPHARM ARZNEIMITTEL GMBH) | Tableta | BROMAZEPAM (el registro no detalla la indicación) |

Los datos reportan 13 registros en total. Los listados recibidos corresponden al mismo número de registro, 19920700, repetido, por lo que aquí se muestra una sola vez.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas en la consulta realizada.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo. El único ensayo es indirecto, pequeño y no evalúa bromazepam para migraña, y no hay literatura ni mecanismo específico que lo sustente.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), requisito previo al tamizaje de seguridad.
- Completar los datos de mecanismo de acción desde DrugBank y analizar el vínculo con la migraña.
- Buscar literatura y ensayos que evalúen directamente bromazepam u otras benzodiacepinas en migraña.
- Confirmar la indicación aprobada real del producto en Colombia, ya que el registro solo indica el nombre del fármaco.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

