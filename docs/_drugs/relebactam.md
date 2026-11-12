---
layout: default
title: Relebactam
parent: Solo Predicción del Modelo (L5)
nav_order: 554
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-12
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

## Relebactam: Nueva indicación predicha, Hiperamilasemia
{: .text-alpha }

## Resumen en Una Frase

Relebactam es un inhibidor de beta-lactamasas que se utiliza únicamente en combinación con imipenem/cilastatina (RECARBRIO®), originalmente para infecciones bacterianas resistentes.
El modelo TxGNN predice que podría ser efectivo para **hiperamilasemia**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata de una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Imipenem. Cilastatina. Relebactam (el registro no detalla el texto de la indicación) |
| Nueva Indicación Predicha | Hiperamilasemia |
| Puntaje de Predicción TxGNN | 0.9922 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, relebactam es un inhibidor de beta-lactamasas de serina (clases A y C) que se administra solo junto con imipenem/cilastatina para proteger al antibiótico de la degradación por bacterias resistentes. Su eficacia se asocia a infecciones bacterianas, no a trastornos metabólicos o pancreáticos.

**La predicción no tiene un fundamento mecanístico plausible.** No existe una vía conocida que conecte la inhibición de beta-lactamasas con la regulación de la amilasa o con la patología pancreática o salival. Además, la hiperamilasemia es un hallazgo de laboratorio y no una enfermedad blanco clásica, por lo que es más probable que sea un artefacto del modelo TxGNN (aprendizaje profundo) o una señal de evento adverso que una oportunidad terapéutica.

Otras predicciones del modelo con el mismo perfil (sin evidencia ni vínculo mecanístico) fueron el síndrome de hiperviscosidad policlonal (0.9922, idéntico puntaje al de hiperamilasemia, lo que sugiere una asociación genérica del modelo) y la analbuminemia congénita (0.9908).

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20212212 | RECARBRIO® (Merck Sharp and Dohme Corp) | Polvo para solución inyectable | Imipenem. Cilastatina. Relebactam |

## Consideraciones de Seguridad

No se dispone de datos de advertencias, contraindicaciones ni interacciones farmacológicas en los datos compilados para este informe. Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (nivel L5), sin ensayos ni publicaciones, y sin un vínculo mecanístico plausible.

<!-- review:begin co-lic-20261105-relebactam-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción se apoya solo en el puntaje del modelo (nivel L5), sin ensayos ni publicaciones, y sin un vínculo mecanístico plausible. Además, el único registro sanitario en Colombia está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-relebactam-2 -->

**Para avanzar se necesita:**
- Obtener los datos del mecanismo de acción (por ejemplo, desde DrugBank) y reevaluar si existe algún vínculo biológico
- Descargar y revisar el prospecto de INVIMA para completar advertencias y contraindicaciones (brecha de datos bloqueante para el cribado de seguridad)
- Evaluar si la hiperamilasemia corresponde a una señal de evento adverso y no a una indicación terapéutica
- Considerar priorizar otras candidatas con evidencia clínica o mecanística real

<!-- review:begin co-lic-20261031-relebactam-1 -->

> **Corrección de revisión (2026-10-31)**: Texto original: "Confirmar la situación regulatoria del producto en Colombia (registro cancelado) / Considerar priorizar otras candidatas con evidencia clínica o mecanística real" Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-10-31. El medicamento tiene 1 registro sanitario (vigentes: 1); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261031-relebactam-1 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-10-31 | Eliminado: "Confirmar la situación regulatoria del producto en Colombia (registro cancelado)" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "Además, el único registro sanitario en Colombia está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

