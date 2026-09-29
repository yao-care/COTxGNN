---
layout: default
title: Penciclovir
parent: Solo Predicción del Modelo (L5)
nav_order: 321
evidence_level: L5
indication_count: 1
---

# Penciclovir
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

# Penciclovir: De Indicación Original No Especificada a Fascioliasis

## Resumen en Una Frase

Penciclovir es un análogo nucleósido de la guanosina con acción antiviral, comercializado en Colombia como crema tópica. El registro sanitario no detalla su indicación original.
El modelo TxGNN predice que podría ser efectivo para **fascioliasis**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto solo repite el nombre del principio activo, "Penciclovir") |
| Nueva Indicación Predicha | Fascioliasis |
| Puntaje de Predicción TxGNN | 99.06% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

**Esta predicción no tiene un fundamento biológico creíble con los datos disponibles.** Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro. Por farmacología general, penciclovir es un análogo nucleósido de la guanosina. La timidina quinasa viral lo fosforila y luego inhibe la ADN polimerasa de los herpesvirus.

La fascioliasis es una infección causada por trematodos parásitos del género *Fasciola*. Estos organismos no tienen timidina quinasa viral ni ADN polimerasa viral, así que el mecanismo antiviral de penciclovir no aplica. El tratamiento estándar de la fascioliasis es el triclabendazol, que actúa por un mecanismo distinto.

El puntaje de 0.99 proviene solo de una predicción de grafo de conocimiento. Puede reflejar artefactos de la topología del grafo y no una relación farmacológica real. Además, la única presentación registrada en Colombia es una crema tópica. La fascioliasis es una infección sistémica del hígado y las vías biliares, por lo que la vía de administración tampoco sería compatible.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20205701 | PENCIVIRAL® CREMA (PHARMA LASER LTDA) | Crema tópica | Solo indica el principio activo: Penciclovir |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. La consulta de interacciones farmacológicas no arrojó resultados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos, sin literatura y sin un mecanismo plausible. El mecanismo antiviral de penciclovir no aplica a un parásito, y la crema tópica no es compatible con una infección sistémica.

**Para avanzar se necesita:**
- Un vínculo mecanístico plausible entre penciclovir y *Fasciola*, por ejemplo con estudios preclínicos in vitro o in vivo
- Evidencia publicada o ensayos que respalden la asociación
- Datos de mecanismo de acción confirmados desde DrugBank
- El prospecto del INVIMA con advertencias y contraindicaciones
- Una evaluación de la vía de administración, ya que la presentación registrada es solo tópica
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

