---
layout: default
title: Leflunomide
parent: Solo Predicción del Modelo (L5)
nav_order: 386
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Leflunomide: nueva indicación predicha, Síndrome de braquidactilia-sindactilia (nivel de evidencia L5). Indicación original: Leflunomida"
monitor_inn: "Leflunomide"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
---

# Leflunomide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Leflunomida: De Leflunomida (indicación no detallada en el registro) a Síndrome de Braquidactilia-Sindactilia

## Resumen en Una Frase

Leflunomida es un fármaco oral inmunomodulador que se ha utilizado en artritis reumatoide activa y en la prevención del rechazo de trasplantes; en los registros sanitarios colombianos, sin embargo, solo figura el nombre del principio activo como indicación.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de braquidactilia-sindactilia**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.
La predicción se basa únicamente en el modelo, y existen argumentos biológicos que la contradicen.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Leflunomida (el registro no detalla la indicación; en la literatura farmacológica: artritis reumatoide activa) |
| Nueva Indicación Predicha | Síndrome de braquidactilia-sindactilia |
| Puntaje de Predicción TxGNN | 99.93% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 4 (0 vigentes, 4 cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según el conocimiento farmacológico general, la leflunomida (a través de su metabolito activo, la teriflunomida) inhibe la enzima dihidroorotato deshidrogenasa (DHODH). Esto reduce la síntesis de pirimidinas y frena la proliferación de linfocitos activados, lo que explica su uso en enfermedades autoinmunes.

El síndrome de braquidactilia-sindactilia es una malformación congénita de las extremidades, de origen genético y del desarrollo, que no depende de la proliferación linfocitaria. Por ello, **no se identifica un vínculo mecanístico validado** entre la indicación original y la nueva. El puntaje alto de TxGNN (0.9993) es solo una predicción basada en un grafo de conocimiento y no aporta una explicación biológica.

Además, hay señales en sentido contrario: la inhibición de DHODH se asocia con malformaciones de las extremidades (por ejemplo, el síndrome de Miller, causado por pérdida de función de DHODH), y la leflunomida es un teratógeno conocido. Esto sugiere un riesgo más que un beneficio terapéutico en un trastorno del desarrollo de las extremidades.

La segunda predicción del modelo, el síndrome de microftalmia colobomatosa-displasia rizomélica (puntaje 99.93%), presenta la misma situación: es un trastorno congénito raro, sin vínculo mecanístico establecido, sin evidencia clínica y con los mismos motivos de preocupación por teratogenicidad.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

Todos los registros sanitarios de leflunomida en Colombia están cancelados; actualmente no hay productos vigentes.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20127508 | ZORATOMIN® 20 MG TABLETAS RECUBIERTAS | Tableta recubierta | Leflunomide |
| 20152814 | LEFLUNOMIDA 20 MG TABLETA RECUBIERTA | Tableta recubierta | Leflunomide |
| 230658 | ARAVA® TABLETAS RECUBIERTAS 20 MG | Tableta recubierta | Leflunomide |
| 20252398 | INFLAXEN® | Tableta recubierta | Leflunomide |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: el grafo de conocimiento asocia la leflunomida con contraindicación en las siguientes condiciones:
  - Hepáticas: insuficiencia hepática, enfermedad hepática, enfermedad de la vesícula biliar, infección crónica por virus de la hepatitis B y C.
  - Renales: enfermedad renal, piouréter.
  - Hematológicas: trombocitopenia, neutropenia (incluidas diversas formas congénitas, como el síndrome de Kostmann y la neutropenia idiopática del adulto), agranulocitosis, pancitopenia, anemia (incluida la macrocítica), neutropenia cíclica.
  - Neurológicas: enfermedad del sistema nervioso periférico, neuropatía periférica.
  - Pulmonares e infecciosas: enfermedad pulmonar intersticial, neumocistosis, aspergilosis.
- **Interacciones Farmacológicas**: solo se registra la interacción farmacológica con su diana, la dihidroorotato deshidrogenasa (DHODH, quinona), que corresponde al mecanismo de acción y no a una interacción clínica con otros fármacos.
- **Teratogenicidad**: la leflunomida es un teratógeno conocido, lo cual es especialmente relevante para un trastorno del desarrollo como el propuesto.

No se dispone de las advertencias y contraindicaciones del prospecto del INVIMA; consultar el prospecto para información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (nivel L5), sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico validado. Además, la teratogenicidad conocida de la leflunomida y la relación de DHODH con malformaciones de las extremidades argumentan en contra de un beneficio terapéutico. Los registros sanitarios en Colombia están todos cancelados.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank.
- Prospecto del INVIMA con advertencias y contraindicaciones para completar la evaluación de seguridad.
- Evidencia biológica o preclínica que justifique un vínculo entre la inhibición de DHODH y el síndrome de braquidactilia-sindactilia.
- Revisión de la plausibilidad de la predicción por expertos, dada la señal de teratogenicidad.
- Aclaración del estado regulatorio, ya que no hay productos vigentes en Colombia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

