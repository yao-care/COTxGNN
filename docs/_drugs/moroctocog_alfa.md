---
layout: default
title: Moroctocog Alfa
parent: Solo Predicción del Modelo (L5)
nav_order: 455
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-12
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

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Moroctocog alfa: De Deficiencia de Factor VIII a Trastorno Primario de Liberación Plaquetaria
{: .text-alpha }

## Resumen en Una Frase

Moroctocog alfa es un factor VIII de coagulación recombinante (con dominio B eliminado), originalmente utilizado para reponer el factor VIII en la coagulación.
El modelo TxGNN predice que podría ser efectivo para **trastorno primario de liberación plaquetaria**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Coagulación factores VIII |
| Nueva Indicación Predicha | Trastorno primario de liberación plaquetaria |
| Puntaje de Predicción TxGNN | 0.9997 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 4 de 4) |
| Número de Registros Sanitarios | 4 (vigentes: 4) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, moroctocog alfa es un factor VIII recombinante que sustituye al factor VIII en la vía intrínseca de la coagulación, y su uso en la deficiencia de factor VIII está respaldado por su registro sanitario en Colombia.

Los trastornos de liberación plaquetaria son defectos de la función de los gránulos plaquetarios, no una deficiencia de factor VIII. Por ello, **no existe una justificación mecanística clara**. El puntaje muy alto de TxGNN (0.9997) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

Otras indicaciones predichas por el modelo, todas con evidencia de nivel L5 y sin ensayos ni literatura:

| Indicación predicha | Puntaje TxGNN | Plausibilidad mecanística |
|------|------|------|
| Pseudoenfermedad de von Willebrand | 0.9997 | Vínculo teórico por el eje VWF-FVIII, pero el defecto primario es plaquetario (GPIbα) |
| Trombastenia de Glanzmann | 0.9996 | Débil: el defecto es de la integrina αIIbβ3; el tratamiento estándar no es FVIII |
| Deficiencia adquirida de factores de coagulación | 0.9988 | La más plausible (p. ej., hemofilia A adquirida), pero los inhibidores autoinmunes neutralizarían el producto y la categoría es muy heterogénea |
| Síndrome de Scott | 0.9986 | Especulativa: el defecto de exposición de fosfatidilserina no se corrige con más FVIII |
| Diátesis hemorrágica por defecto del receptor de colágeno | 0.9973 | Sin justificación directa: defecto independiente de la cascada dependiente de FVIII |
| Trastorno hemorrágico por trombocitopenia constitucional | 0.9972 | Sin justificación: la hemorragia se debe a déficit de plaquetas |
| "Flood factor deficiency" | 0.9911 | Entidad no reconocida; posible error de datos u ontología, debe verificarse |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20046519 | XYNTHA® 2000 UI | Polvo liofilizado para reconstituir a solución inyectable | Coagulación factores VIII | Vigente |
| 20005016 | XYNTHA® 500 UI | Polvo liofilizado para reconstituir a solución inyectable | Coagulación factores VIII | Vigente |
| 20046518 | XYNTHA® 1000 UI | Polvo liofilizado para reconstituir a solución inyectable | Coagulación factores VIII | Vigente |
| 20005015 | XYNTHA® 250 UI | Polvo liofilizado para reconstituir a solución inyectable | Coagulación factores VIII | Vigente |

Todos los registros pertenecen a PFIZER S.A.S.

<!-- review:begin co-lic-20261105-moroctocog_alfa-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Todos los registros pertenecen a PFIZER S.A.S. y se encuentran cancelados; actualmente no hay presentaciones vigentes en Colombia." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 4 registros sanitarios (vigentes: 4); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-moroctocog_alfa-2 -->

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

En la consulta de interacciones farmacológicas no se encontraron interacciones registradas.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (L5), sin ensayos clínicos ni literatura, y la fisiopatología de los trastornos plaquetarios no responde a la reposición de factor VIII.

<!-- review:begin co-lic-20261105-moroctocog_alfa-3 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción se basa únicamente en el modelo (L5), sin ensayos clínicos ni literatura, y la fisiopatología de los trastornos plaquetarios no responde a la reposición de factor VIII. Además, los registros sanitarios en Colombia están todos cancelados, lo que limita la viabilidad local." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 4 registros sanitarios (vigentes: 4); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-moroctocog_alfa-3 -->

**Para avanzar se necesita:**
- Obtener y analizar el prospecto (advertencias y contraindicaciones) desde INVIMA para completar la evaluación de seguridad.
- Completar los datos del mecanismo de acción del fármaco.
- Si se desea explorar alguna línea, priorizar un subtipo específico de deficiencia adquirida de factores de coagulación y verificar la identidad de la entidad "flood factor deficiency".
- Realizar una búsqueda dirigida de literatura y ensayos para las indicaciones predichas, ya que no se aportó evidencia clínica.

<!-- review:begin co-lic-20261031-moroctocog_alfa-1 -->

> **Corrección de revisión (2026-10-31)**: Texto original: "Aclarar la situación comercial del producto en Colombia (registros cancelados) y su disponibilidad. / Si se desea explorar alguna línea, priorizar un subtipo específico de deficiencia adquirida de factores de coagulación y verificar la identidad de la entidad "flood factor deficiency"." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-10-31. El medicamento tiene 4 registros sanitarios (vigentes: 4); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261031-moroctocog_alfa-1 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-10-31 | Eliminado: "Aclarar la situación comercial del producto en Colombia (registros cancelados) y su disponibilidad" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "y se encuentran cancelados; actualmente no hay presentaciones vigentes en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Además, los registros sanitarios en Colombia están todos cancelados, lo que limita la viabilidad local" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

