---
layout: default
title: Moroctocog Alfa
parent: Solo Predicción del Modelo (L5)
nav_order: 455
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
description: "Moroctocog Alfa: nueva indicación predicha, Trastorno primario de liberación plaquetaria (nivel de evidencia L5). Indicación original: Coagulación factores VIII"
monitor_inn: "MOROCTOCOG ALFA"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "acquired coagulation factor deficiency", "Scott syndrome", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "flood factor deficiency"]
---

# Moroctocog Alfa
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

# Moroctocog alfa: De Deficiencia de Factor VIII a Trastorno Primario de Liberación Plaquetaria

## Resumen en Una Frase

Moroctocog alfa es un factor VIII de coagulación recombinante (con dominio B eliminado), originalmente utilizado para reponer el factor VIII en la coagulación.
El modelo TxGNN predice que podría ser efectivo para **trastorno primario de liberación plaquetaria**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Coagulación factores VIII |
| Nueva Indicación Predicha | Trastorno primario de liberación plaquetaria |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 4 (todos cancelados) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, moroctocog alfa es un factor VIII recombinante que sustituye al factor VIII en la vía intrínseca de la coagulación, y su uso en la deficiencia de factor VIII está respaldado por su registro sanitario en Colombia.

Los trastornos de liberación plaquetaria son defectos de la función de los gránulos plaquetarios, no una deficiencia de factor VIII. Por ello, **no existe una justificación mecanística clara**. El puntaje muy alto de TxGNN (99.97%) proviene de una predicción basada en grafos, probablemente influida por nodos de red compartidos relacionados con la hemostasia.

Otras indicaciones predichas por el modelo, todas con evidencia de nivel L5 y sin ensayos ni literatura:

| Indicación predicha | Puntaje TxGNN | Plausibilidad mecanística |
|------|------|------|
| Pseudoenfermedad de von Willebrand | 99.97% | Vínculo teórico por el eje VWF-FVIII, pero el defecto primario es plaquetario (GPIbα) |
| Trombastenia de Glanzmann | 99.96% | Débil: el defecto es de la integrina αIIbβ3; el tratamiento estándar no es FVIII |
| Deficiencia adquirida de factores de coagulación | 99.88% | La más plausible (p. ej., hemofilia A adquirida), pero los inhibidores autoinmunes neutralizarían el producto y la categoría es muy heterogénea |
| Síndrome de Scott | 99.86% | Especulativa: el defecto de exposición de fosfatidilserina no se corrige con más FVIII |
| Diátesis hemorrágica por defecto del receptor de colágeno | 99.73% | Sin justificación directa: defecto independiente de la cascada dependiente de FVIII |
| Trastorno hemorrágico por trombocitopenia constitucional | 99.72% | Sin justificación: la hemorragia se debe a déficit de plaquetas |
| "Flood factor deficiency" | 99.11% | Entidad no reconocida; posible error de datos u ontología, debe verificarse |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20046519 | XYNTHA® 2000 UI | Polvo liofilizado para reconstituir a solución inyectable | Coagulación factores VIII | Cancelado |
| 20005016 | XYNTHA® 500 UI | Polvo liofilizado para reconstituir a solución inyectable | Coagulación factores VIII | Cancelado |
| 20046518 | XYNTHA® 1000 UI | Polvo liofilizado para reconstituir a solución inyectable | Coagulación factores VIII | Cancelado |
| 20005015 | XYNTHA® 250 UI | Polvo liofilizado para reconstituir a solución inyectable | Coagulación factores VIII | Cancelado |

Todos los registros pertenecen a PFIZER S.A.S. y se encuentran cancelados; actualmente no hay presentaciones vigentes en Colombia.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

En la consulta de interacciones farmacológicas no se encontraron interacciones registradas.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (L5), sin ensayos clínicos ni literatura, y la fisiopatología de los trastornos plaquetarios no responde a la reposición de factor VIII. Además, los registros sanitarios en Colombia están todos cancelados, lo que limita la viabilidad local.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto (advertencias y contraindicaciones) desde INVIMA para completar la evaluación de seguridad.
- Completar los datos del mecanismo de acción del fármaco.
- Aclarar la situación comercial del producto en Colombia (registros cancelados) y su disponibilidad.
- Si se desea explorar alguna línea, priorizar un subtipo específico de deficiencia adquirida de factores de coagulación y verificar la identidad de la entidad "flood factor deficiency".
- Realizar una búsqueda dirigida de literatura y ensayos para las indicaciones predichas, ya que no se aportó evidencia clínica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

