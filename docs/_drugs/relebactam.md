---
layout: default
title: Relebactam
parent: Solo Predicción del Modelo (L5)
nav_order: 554
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Relebactam: nueva indicación predicha, Hiperamilasemia (nivel de evidencia L5). Indicación original: Imipenem. Cilastatina. Relebactam"
monitor_inn: "relebactam"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia"]
---

# Relebactam
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Relebactam: De Infecciones Bacterianas Resistentes (Combinación Imipenem/Cilastatina/Relebactam) a Hiperamilasemia
{: .text-alpha }

## Resumen en Una Frase

Relebactam es un inhibidor de beta-lactamasas que se utiliza únicamente en combinación con imipenem/cilastatina (RECARBRIO®), originalmente para infecciones bacterianas resistentes.
El modelo TxGNN predice que podría ser efectivo para **hiperamilasemia**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata de una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Imipenem. Cilastatina. Relebactam (el registro no detalla el texto de la indicación) |
| Nueva Indicación Predicha | Hiperamilasemia |
| Puntaje de Predicción TxGNN | 99.22% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, relebactam es un inhibidor de beta-lactamasas de serina (clases A y C) que se administra solo junto con imipenem/cilastatina para proteger al antibiótico de la degradación por bacterias resistentes. Su eficacia se asocia a infecciones bacterianas, no a trastornos metabólicos o pancreáticos.

**La predicción no tiene un fundamento mecanístico plausible.** No existe una vía conocida que conecte la inhibición de beta-lactamasas con la regulación de la amilasa o con la patología pancreática o salival. Además, la hiperamilasemia es un hallazgo de laboratorio y no una enfermedad blanco clásica, por lo que es más probable que sea un artefacto del grafo de conocimiento o una señal de evento adverso que una oportunidad terapéutica.

Otras predicciones del modelo con el mismo perfil (sin evidencia ni vínculo mecanístico) fueron el síndrome de hiperviscosidad policlonal (99.22%, idéntico puntaje al de hiperamilasemia, lo que sugiere una asociación genérica del modelo) y la analbuminemia congénita (99.08%).

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20212212 (cancelado) | RECARBRIO® (Merck Sharp and Dohme Corp) | Polvo para solución inyectable | Imipenem. Cilastatina. Relebactam |

## Consideraciones de Seguridad

No se dispone de datos de advertencias, contraindicaciones ni interacciones farmacológicas en los datos compilados para este informe. Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (nivel L5), sin ensayos ni publicaciones, y sin un vínculo mecanístico plausible. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Obtener los datos del mecanismo de acción (por ejemplo, desde DrugBank) y reevaluar si existe algún vínculo biológico
- Descargar y revisar el prospecto de INVIMA para completar advertencias y contraindicaciones (brecha de datos bloqueante para el cribado de seguridad)
- Evaluar si la hiperamilasemia corresponde a una señal de evento adverso y no a una indicación terapéutica
- Confirmar la situación regulatoria del producto en Colombia (registro cancelado)
- Considerar priorizar otras candidatas con evidencia clínica o mecanística real
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

