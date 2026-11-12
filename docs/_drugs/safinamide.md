---
layout: default
title: Safinamide
parent: Solo Predicción del Modelo (L5)
nav_order: 578
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-12
monitor_inn: "safinamide"
predicted_indications: ["Rasmussen subacute encephalitis", "myelitis", "PLA2G6-associated neurodegeneration"]
description: "Safinamide: nueva indicación predicha, Encefalitis subaguda de Rasmussen (Rasmussen subacute encephalitis) (nivel de evidencia L5). Indicación original: SAFINAMIDA"
---

# Safinamide
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

## Safinamide: Encefalitis subaguda de Rasmussen (Rasmussen subacute encephalitis)
{: .text-alpha }

## Resumen en Una Frase

Safinamida es un inhibidor reversible de la MAO-B; en el registro sanitario colombiano figura solo como "SAFINAMIDA", sin una indicación detallada.
El modelo TxGNN predice que podría ser efectivo para la **encefalitis subaguda de Rasmussen**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | SAFINAMIDA |
| Nueva Indicación Predicha | Encefalitis subaguda de Rasmussen (Rasmussen subacute encephalitis) |
| Puntaje de Predicción TxGNN | 0.9963 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 2 de 2) |
| Número de Registros Sanitarios | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción original. Según la información conocida, safinamida es un inhibidor reversible de la MAO-B que además bloquea canales de sodio dependientes de voltaje e inhibe la liberación de glutamato. Estas propiedades podrían relacionarse, en teoría, con la excitotoxicidad y la actividad convulsiva de la encefalitis de Rasmussen.

Sin embargo, la relación es débil. La encefalitis de Rasmussen está causada principalmente por inflamación autoinmune mediada por linfocitos T, y safinamida no tiene una acción inmunomoduladora conocida. A lo sumo, podría ofrecer un efecto sintomático o neuroprotector secundario.

El único sustento es la puntuación del modelo TxGNN (0.9963). La similitud con la indicación original no se ha evaluado, y la compatibilidad de vías de administración está pendiente (safinamida es de administración oral).

Otras predicciones del modelo, también solo con evidencia L5, son mielitis (0.9946) y neurodegeneración asociada a PLA2G6 (0.9922). Esta última tiene un vínculo sintomático algo más plausible por su componente parkinsoniano y dopaminérgico, aunque no modificaría la enfermedad de fondo.

<!-- review:begin co-lic-20261105-safinamide-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Ambos registros pertenecen a Laboratorios Legrand S.A. y están cancelados; actualmente no hay un producto vigente con safinamida en Colombia." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 2 registros sanitarios (vigentes: 2); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-safinamide-1 -->

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20202462 | ZAFIMID 100MG. TABLETAS RECUBIERTAS | Tableta | SAFINAMIDA | Vigente |
| 20202459 | ZAFIMID® 50MG | Tableta recubierta | SAFINAMIDA | Vigente |

## Consideraciones de Seguridad

**Interacciones Farmacológicas**: se identificaron 110 interacciones en total. Entre las listadas:

- **Mayor**: bupropión.
- **Moderadas**: isometepteno, dietilpropión, fentermina, metoclopramida, rosuvastatina, y diversos antidiabéticos (clorpropamida, empagliflozina, glimepirida, nateglinida, repaglinida, acetohexamida) e insulinas (aspart, degludec, detemir, glargina, glulisina, humana isófana, humana regular e inhalada).

No se dispone de datos de advertencias ni de contraindicaciones del prospecto. Consultar el prospecto para esa información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (L5), sin ensayos clínicos ni literatura, y el mecanismo propuesto no aborda la causa autoinmune de la enfermedad. Además, faltan datos de seguridad del prospecto.

<!-- review:begin co-lic-20261105-safinamide-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Además, no hay productos vigentes en Colombia y faltan datos de seguridad del prospecto." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 2 registros sanitarios (vigentes: 2); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-safinamide-2 -->

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA para las advertencias y contraindicaciones (brecha de seguridad bloqueante).
- Completar los datos del mecanismo de acción desde DrugBank.
- Buscar estudios preclínicos o series de casos de safinamida en encefalitis de Rasmussen y en las demás indicaciones predichas.
- Evaluar la viabilidad regulatoria y comercial.
- Valorar si neurodegeneración asociada a PLA2G6 sería una alternativa más plausible para un uso sintomático.

<!-- review:begin co-lic-20261105-safinamide-3 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Evaluar la viabilidad regulatoria y comercial, dado que los registros están cancelados." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 2 registros sanitarios (vigentes: 2); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-safinamide-3 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Ambos registros pertenecen a Laboratorios Legrand S.A. y están cancelados; actualmente no hay un producto vigente con safinamida en Colombia" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "no hay productos vigentes en Colombia y" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "dado que los registros están cancelados" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

