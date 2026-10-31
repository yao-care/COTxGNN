---
layout: default
title: Aprepitant
parent: Solo Predicción del Modelo (L5)
nav_order: 62
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-31
description: "Aprepitant: nueva indicación predicha, Síndrome nefrogénico de antidiuresis inapropiada (nivel de evidencia L5). Indicación original: No disponible"
monitor_inn: "APREPITANT"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "hypertrichosis (disease)", "pulmonary hypertension", "leprosy", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "kyphoscoliotic heart disease", "syndrome with a Dandy-Walker malformation as major feature", "subarachnoid hemorrhage (disease)", "isolated genetic hair shaft abnormality"]
---

# Aprepitant
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

## Aprepitant: De Indicación Registrada (sin texto descriptivo) a Síndrome Nefrogénico de Antidiuresis Inapropiada
{: .text-alpha }

## Resumen en Una Frase

Aprepitant es un antagonista del receptor NK1 registrado en Colombia bajo el nombre comercial EMEND®; el texto de indicación del registro sanitario solo repite el nombre del principio activo, por lo que no se dispone de una indicación original descrita.
El modelo TxGNN predice que podría ser efectivo para **síndrome nefrogénico de antidiuresis inapropiada (NSIAD)**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, de modo que se trata de una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (el registro INVIMA solo indica "APREPITANT") |
| Nueva Indicación Predicha | Síndrome nefrogénico de antidiuresis inapropiada |
| Puntaje de Predicción TxGNN | 0.9997 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 1 de 1) |
| Número de Registros Sanitarios | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Aprepitant es un antagonista del receptor NK1 de la sustancia P. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos compilada, pero la clase farmacológica es conocida: el bloqueo de la señalización de la sustancia P/NK1.

Existen reportes de que la señalización sustancia P/NK1 puede modular vías relacionadas con la vasopresina y el manejo renal del agua, lo que ofrece un vínculo mecanístico débil con el NSIAD. Sin embargo, no existe una relación establecida con las mutaciones activadoras del receptor V2 que causan esta enfermedad.

En resumen, el puntaje de TxGNN es alto (0.9997), pero es una predicción puramente computacional, sin ensayos ni literatura de respaldo. Debe tratarse como una hipótesis que requiere validación preclínica antes de cualquier consideración clínica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 19945183 | EMEND® 80 MG/125 MG | Cápsula dura | APREPITANT | Vigente |

---

## Consideraciones de Seguridad

- **Contraindicaciones (según grafo de conocimiento, no según prospecto)**: el grafo de conocimiento TxGNN (PrimeKG) asocia aprepitant con contraindicación en **insuficiencia hepática**.
- **Interacciones Farmacológicas**: se identificaron 100 interacciones registradas. Entre las de mayor gravedad (nivel Mayor) se encuentran:
  - Fentanilo
  - Alfentanilo
  - Acalabrutinib

  Entre las de nivel Moderado se incluyen paclitaxel, abemaciclib, nifedipino, ibuprofeno, levonorgestrel, hidrocortisona, albendazol, fluvoxamina, fosamprenavir, fosfenitoína, fostamatinib y gefitinib. La carga de interacciones, vinculada al metabolismo por CYP3A4, es una preocupación práctica en pacientes polimedicados.

Para advertencias y contraindicaciones del prospecto, consultar el documento oficial.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto en TxGNN, pero no cuenta con ensayos clínicos, literatura ni un mecanismo plausible establecido (nivel L5). Además, el producto no tiene registro sanitario vigente en Colombia.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y análisis mecanístico específico de la vía NK1/vasopresina en NSIAD
- Estudios preclínicos o de mecanismo que respalden la hipótesis
- Obtención y revisión del prospecto de INVIMA (advertencias y contraindicaciones)
- Evaluación del riesgo de interacciones (CYP3A4) y de la contraindicación en insuficiencia hepática

---

### Nota sobre otras indicaciones predichas

Las demás predicciones del modelo (hipertricosis, hipertensión pulmonar, lepra, hemorragia subaracnoidea, entre otras) también están en nivel L5 y recomendación Hold. En hipertensión pulmonar, la única publicación recuperada (PMID 28261651, un ensayo de fase I de pazopanib con cisplatino) no es relevante para aprepitant ni para esa enfermedad.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

