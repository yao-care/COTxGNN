---
layout: default
title: Ravulizumab
parent: Solo Predicción del Modelo (L5)
nav_order: 342
evidence_level: L5
indication_count: 10
---

# Ravulizumab
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

# Ravulizumab: De Indicación No Detallada en el Registro a Neutropenia Congénita Grave Autosómica Recesiva por Deficiencia de G6PC3

## Resumen en Una Frase

Ravulizumab es un inhibidor de acción prolongada del componente C5 del complemento. En Colombia se comercializa como ULTOMIRIS®, pero el registro no detalla su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **neutropenia congénita grave autosómica recesiva por deficiencia de G6PC3**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección. Se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto de INVIMA solo indica «RAVULIZUMAB») |
| Nueva Indicación Predicha | Neutropenia congénita grave autosómica recesiva por deficiencia de G6PC3 |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 4 (todos con el mismo número de registro, 20224196) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información conocida, ravulizumab es un inhibidor de C5 de acción prolongada. Su uso establecido es en enfermedades mediadas por complemento, como la hemoglobinuria paroxística nocturna (HPN).

**La predicción no tiene un vínculo mecanístico establecido.** La deficiencia de G6PC3 causa neutropenia por alteración del metabolismo de la glucosa-6-fosfato y por apoptosis de los neutrófilos. No es una enfermedad por desregulación del complemento. El puntaje alto de TxGNN proviene del grafo de conocimiento y no de evidencia biológica o clínica.

Además, el bloqueo del complemento terminal aumenta el riesgo de infecciones por bacterias encapsuladas, con advertencia en recuadro por enfermedad meningocócica. En pacientes que ya son neutropénicos, este riesgo es una preocupación de seguridad importante.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20224196 | ULTOMIRIS® (ASTRAZENECA COLOMBIA S.A.S.) | Solución concentrada para infusión | Solo figura «RAVULIZUMAB»; el registro no detalla la indicación |

Los 4 registros contabilizados corresponden al mismo número y al mismo producto, por eso se presenta una sola fila.

## Consideraciones de Seguridad

- **Advertencia principal (según el análisis del Evidence Pack)**: el bloqueo del complemento terminal conlleva advertencia en recuadro por infección meningocócica grave y mayor riesgo de infecciones por bacterias encapsuladas.
- **Poblaciones de riesgo**: en pacientes neutropénicos o con inmunodeficiencias primarias, este riesgo podría representar un daño neto.

Para advertencias y contraindicaciones completas, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (L5), sin ensayos ni literatura, y no existe un vínculo mecanístico plausible entre la inhibición de C5 y la neutropenia por deficiencia de G6PC3. Además, el riesgo de infección por el bloqueo del complemento es especialmente preocupante en esta población. Las otras 9 indicaciones predichas también son L5 y están en Hold.

**Para avanzar se necesita:**
- Un vínculo mecanístico demostrado, con estudios preclínicos que justifiquen la inhibición de C5 en esta enfermedad
- Obtener y revisar el prospecto de INVIMA (advertencias y contraindicaciones), pendiente
- Confirmar la indicación aprobada en Colombia, ya que el registro solo muestra el nombre del principio activo
- Datos del mecanismo de acción desde DrugBank
- Una evaluación de riesgo-beneficio de la infección por bacterias encapsuladas en pacientes neutropénicos
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

