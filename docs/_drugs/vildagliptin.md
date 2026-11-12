---
layout: default
title: Vildagliptin
parent: Solo Predicción del Modelo (L5)
nav_order: 659
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-12
monitor_inn: "Vildagliptin"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "thiamine-responsive dysfunction syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
description: "Vildagliptin: nueva indicación predicha, Focal stiff limb syndrome (nivel de evidencia L5). Indicación original: METFORMINA / VILDAGLIPTINA"
---

# Vildagliptin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Vildagliptin: Focal stiff limb syndrome
{: .text-alpha }

## Resumen en Una Frase

Vildagliptina es un inhibidor de la dipeptidil peptidasa 4 (DPP-4), utilizado en el manejo de la diabetes tipo 2. En Colombia se registró en combinación con metformina (Galvus® Met).
El modelo TxGNN predice que podría ser efectivo para el **síndrome de rigidez focal de extremidad**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Es una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | METFORMINA / VILDAGLIPTINA |
| Nueva Indicación Predicha | Focal stiff limb syndrome |
| Puntaje de Predicción TxGNN | 0.9988 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 15 de 17) |
| Número de Registros Sanitarios | 17 (vigentes: 15) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado. Según la información conocida, vildagliptina inhibe la enzima DPP-4, lo que aumenta las hormonas incretinas (GLP-1 y GIP) y mejora el control de la glucosa en la diabetes tipo 2. Su eficacia en esa indicación está comprobada, pero no existe un vínculo mecanístico reconocido con la nueva indicación.

El síndrome de rigidez focal de extremidad es un trastorno neuromuscular emparentado con el síndrome de la persona rígida. Este último se asocia con autoinmunidad (anticuerpos anti-GAD) y con la diabetes tipo 1. Es probable que el puntaje alto refleje la cercanía en la red de conocimiento con nodos de diabetes o autoinmunidad, y no un efecto farmacológico real.

Vildagliptina no tiene efectos conocidos sobre las vías GABAérgicas ni sobre la patología mediada por anti-GAD. Por ello, la predicción debe considerarse una hipótesis sin respaldo clínico ni mecanístico.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 19998394 | GALVUS® MET comprimidos recubiertos con película 50 mg / 1000 mg (Novartis Pharma AG) | Tableta cubierta con película | Metformina / Vildagliptina | Vigente |

---

## Consideraciones de Seguridad

- **Interacciones farmacológicas:** La consulta se completó y devolvió 4 registros. Corresponden a dianas farmacológicas de vildagliptina, no a interacciones con otros medicamentos: DPP-4 (diana principal), DPP-8, DPP-9 y TRPV4. La inhibición de DPP-8 y DPP-9 es relevante para el perfil de selectividad y tolerabilidad.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto (0.9988), pero no cuenta con ensayos clínicos ni literatura, y no hay un mecanismo plausible que vincule la inhibición de DPP-4 con esta enfermedad.

<!-- review:begin co-lic-20261105-vildagliptin-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "La predicción tiene un puntaje alto (0.9988), pero no cuenta con ensayos clínicos ni literatura, y no hay un mecanismo plausible que vincule la inhibición de DPP-4 con esta enfermedad. Además, el único registro sanitario en Colombia está cancelado." Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 17 registros sanitarios (vigentes: 15); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-vildagliptin-1 -->

**Nota:** Entre las predicciones compiladas para este fármaco, la diabetes mellitus tipo 1 tiene la evidencia más sólida (nivel L2). Incluye 7 ensayos clínicos, entre ellos un ensayo Fase 3 pequeño de estado desconocido (NCT01559025, n=44) y un ECA doble ciego de rapamicina más vildagliptina (PMID 33124663). Si se busca una vía de reposicionamiento con respaldo real, esa indicación merece una evaluación aparte.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank
- Una hipótesis mecanística plausible que conecte la inhibición de DPP-4 con la patología del síndrome de rigidez focal
- Revisión de la literatura específica sobre el síndrome de rigidez de extremidad y fármacos incretínicos
- Descarga y análisis del prospecto de INVIMA para completar el tamizaje de seguridad
- Un plan regulatorio

<!-- review:begin co-lic-20261105-vildagliptin-2 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Un plan regulatorio, dado que el registro sanitario está cancelado" Eliminado: afirmaba que el medicamento no tiene registro sanitario o que sus registros están cancelados o vencidos, lo que no coincide con los datos del INVIMA (Código Único de Medicamentos) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 17 registros sanitarios (vigentes: 15); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en Colombia. Fuente: [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json).

<!-- review:end co-lic-20261105-vildagliptin-2 -->

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (INVIMA, Código Único de Medicamentos). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Además, el único registro sanitario en Colombia está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |
| 2026-11-05 | Eliminado: "dado que el registro sanitario está cancelado" | Corregido | [INVIMA: Código Único de Medicamentos (datos.gov.co)](https://www.datos.gov.co/resource/i7cb-raxc.json) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

