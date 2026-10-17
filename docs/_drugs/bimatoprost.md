---
layout: default
title: Bimatoprost
parent: Solo Predicción del Modelo (L5)
nav_order: 106
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Bimatoprost: nueva indicación predicha, Síndrome de malformación con componente odontal y/o periodontal (nivel de evidencia L5). Indicación original: Solución oftálmica"
monitor_inn: "BIMATOPROST"
predicted_indications: ["malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "genetic alopecia", "pulmonary arteriovenous malformation (disease)"]
---

# Bimatoprost
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Bimatoprost: De Solución Oftálmica para Glaucoma a Síndrome de Malformación con Componente Odontal y/o Periodontal

## Resumen en Una Frase

Bimatoprost es un análogo sintético de prostamida F2α, utilizado originalmente como solución oftálmica para la hipertensión ocular y el glaucoma de ángulo abierto.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de malformación con componente odontal y/o periodontal**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción: se basa únicamente en el modelo computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Solución oftálmica (el texto del registro solo menciona el nombre del principio activo; el uso conocido es glaucoma e hipertensión ocular) |
| Nueva Indicación Predicha | Síndrome de malformación con componente odontal y/o periodontal |
| Puntaje de Predicción TxGNN | 99.997% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 1 (0 vigentes, 1 cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Bimatoprost es un análogo de prostamida F2α. En oftalmología reduce la presión intraocular. Los datos compilados para este informe no incluyen una descripción detallada de su mecanismo de acción, más allá de su clasificación como análogo de prostamida F2α.

**En este caso, la predicción no tiene un vínculo mecanístico identificable.** Bimatoprost es un análogo de prostamida F2α y no se conoce ninguna vía que lo conecte con este síndrome de malformación del desarrollo. El puntaje alto de TxGNN (posición 64 en su clasificación) refleja solo una asociación en el grafo de conocimiento. No hay ensayos ni literatura que lo respalden.

La similitud entre la indicación original (glaucoma) y la nueva indicación (malformación con componente dental/periodontal) no ha sido evaluada. Por lo tanto, esta predicción debe considerarse una hipótesis computacional sin sustento clínico ni biológico demostrado.

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
| 19923968 | LUMIGAN ® SOLUCION OFTALMICA (ABBVIE INC) | Solución oftálmica | BIMATOPROST (el registro no detalla la indicación) | Cancelado |

Bimatoprost no tiene actualmente ningún registro sanitario vigente en Colombia. La única presentación disponible en la ruta oftálmica es la solución oftálmica.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (TxGNN/PrimeKG, no provienen del prospecto):** enfermedad hepática, enfermedad de la vesícula biliar, uveítis, enfermedad del iris, enfermedad del cuerpo ciliar, panuveítis, edema macular retiniano, edema macular quístico e iritis.
- **Interacciones farmacológicas:** se identificaron 66 posibles interacciones, todas con nivel de gravedad no clasificado. Algunos ejemplos son calcitriol, fentermina, pantoprazol, morfina, metformina, omeprazol, palonosetrón, rosiglitazona, lansoprazol, vancomicina, prednisona, prednisolona, triamcinolona, simvastatina y ondansetrón. Se requiere revisión clínica antes de cualquier uso combinado.

Consultar el prospecto para las advertencias y contraindicaciones oficiales.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto en el modelo, pero no cuenta con ensayos clínicos, literatura ni un vínculo mecanístico plausible (nivel L5). Además, el fármaco no tiene registros vigentes en Colombia, por lo que no se recomienda avanzar con esta indicación.

**Para avanzar se necesita:**
- Una hipótesis biológica que conecte la vía de prostamida/receptor FP con la patología de esta malformación.
- Estudios preclínicos o de mecanismo que respalden la plausibilidad.
- Datos de mecanismo de acción detallados y las advertencias oficiales del prospecto.
- Evaluación de la viabilidad de la vía de administración para esta indicación.

**Nota sobre otras indicaciones predichas con más sustento:** entre las demás predicciones, **alopecia** (puntaje TxGNN 99.993%) y **alopecia genética** (99.966%) tienen nivel de evidencia L2 y recomendación *Proceed with Guardrails*. Los respaldan varios ensayos de Fase 2 completados en alopecia androgenética (por ejemplo NCT01325337, NCT01325350 y NCT01904721, con más de 240 participantes cada uno) y estudios de Fase 1 de farmacocinética y tolerabilidad en cuero cabelludo. La eficacia en el cuero cabelludo parece modesta frente a minoxidil y no hay ensayo de Fase 3. La alopecia es la línea de reposicionamiento con más soporte para este fármaco y justificaría un informe propio.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

