---
layout: default
title: Cysteine
parent: Evidencia Moderada (L3-L4)
nav_order: 187
evidence_level: L4
indication_count: 7
last_modified_at: 2026-10-28
description: "Cysteine: nueva indicación predicha, Síndrome de ojo seco (nivel de evidencia L4). Indicación original: Combinaciones"
monitor_inn: "Cysteine"
predicted_indications: ["dry eye syndrome", "closed-angle glaucoma", "nasal cavity disease", "acute laryngopharyngitis", "pharyngitis", "exercise-induced malignant hyperthermia", "angle-closure glaucoma"]
---

# Cysteine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **7** 
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

## Cisteína: De Combinaciones (Nutrición Parenteral) a Síndrome de Ojo Seco
{: .text-alpha }

## Resumen en Una Frase

La cisteína es un aminoácido que en Colombia estuvo registrado como componente de una emulsión inyectable de nutrición (NUMETA® G 19% E), cuya indicación aprobada figura solo como "combinaciones".
El modelo TxGNN predice que podría ser efectiva para el **síndrome de ojo seco**, pero **no hay ensayos clínicos** y la literatura recuperada es casi toda preclínica o indirecta (formulaciones con derivados de cisteína, mecanismos de estrés oxidativo).
La evidencia es débil y se considera una pregunta de investigación.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Combinaciones (texto del registro INVIMA) |
| Nueva Indicación Predicha | Síndrome de ojo seco |
| Puntaje de Predicción TxGNN | 0.9998 |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 1) |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la cisteína es un aminoácido con grupo tiol y precursor del glutatión, y en Colombia se registró como parte de una emulsión de nutrición parenteral. Su uso aprobado no guarda relación directa con enfermedades oculares.

El vínculo mecanístico propuesto es el siguiente: en el ojo seco, el exceso de especies reactivas de oxígeno (ROS) y la inflamación mediada por el inflamasoma NLRP3 contribuyen a la enfermedad. El grupo tiol de la cisteína podría aportar capacidad antioxidante y de amortiguación redox en la superficie ocular. Además, los polímeros tiolados (tiómeros) construidos con conjugados de cisteína tienen buena mucoadhesión, lo que podría prolongar el tiempo de permanencia del fármaco en el ojo.

Es importante precisar que la mayoría de los estudios recuperados usan la cisteína como componente de formulación o como concepto redox, no como agente terapéutico administrado directamente. Por ello, la razonabilidad es plausible pero especulativa.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Se listan las publicaciones más pertinentes (no hay ECA ni estudios clínicos en ojo seco; todas son preclínicas, revisiones o de mecanismo).

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [40123221](https://pubmed.ncbi.nlm.nih.gov/40123221/) | 2025 | Preclínico | Advanced Materials | Nanoformulación en gotas oculares de catalasa con quitosano modificado con cisteína para tratar el ojo seco mediante eliminación de ROS |
| [36581034](https://pubmed.ncbi.nlm.nih.gov/36581034/) | 2023 | Preclínico | Int J Biol Macromol | Conjugado de condroitín sulfato y L-cisteína en portadores lipídicos con dexametasona; mayor retención y permeación corneal |
| [41485487](https://pubmed.ncbi.nlm.nih.gov/41485487/) | 2026 | Preclínico | J Control Release | Profármaco de persulfuro sensible a superóxido para ojo seco, orientado a eliminar ROS |
| [26606856](https://pubmed.ncbi.nlm.nih.gov/26606856/) | 2015 | Preclínico | Ther Deliv | Ácido hialurónico modificado con éster etílico de cisteína como lubricante mucoadhesivo para ojo seco |
| [24993428](https://pubmed.ncbi.nlm.nih.gov/24993428/) | 2014 | Revisión | J Control Release | Revisión de tiómeros: la unión de grupos tiol mejora la mucoadhesión |
| [31028759](https://pubmed.ncbi.nlm.nih.gov/31028759/) | 2019 | Revisión | Adv Drug Deliv Rev | Revisión de polímeros tiolados y sus propiedades mucoadhesivas |
| [36626177](https://pubmed.ncbi.nlm.nih.gov/36626177/) | 2023 | Preclínico | Invest Ophthalmol Vis Sci | La deficiencia de acuaporina 5 agrava la piroptosis mediada por ROS/NLRP3 en glándulas lagrimales |
| [25701684](https://pubmed.ncbi.nlm.nih.gov/25701684/) | 2015 | Observacional/mecanístico | Exp Eye Res | Los inflamasomas NLRP3 activados por ROS inician inflamación en células corneales y pacientes con ojo seco |
| [24836981](https://pubmed.ncbi.nlm.nih.gov/24836981/) | 2014 | Preclínico | Exp Eye Res | Los inflamasomas NLRP3 activados por ROS participan en el ojo seco murino |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20057807 (cancelado) | NUMETA® G 19% E | Emulsión inyectable | Combinaciones |

---

## Consideraciones de Seguridad

- **Posibles contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad del modelo, no texto de prospecto): úlcera péptica, trastornos hipotensivos, insuficiencia respiratoria, asma, enfermedad bronquial, várices esofágicas, fenilcetonuria y trastornos del metabolismo de la fenilalanina.

No se encontraron interacciones farmacológicas registradas. Para el resto de la información de seguridad, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de TxGNN es muy alta, pero no hay ensayos clínicos y la literatura es preclínica o indirecta, con la cisteína usada sobre todo como componente de formulación. Además, el único registro sanitario en Colombia está cancelado y la vía de administración original (emulsión inyectable) no es compatible con un uso oftálmico.

**Para avanzar se necesita:**
- Estudios preclínicos que evalúen la cisteína (o un derivado) como agente activo en modelos de ojo seco
- Datos del mecanismo de acción y de la relación con la indicación original
- Definir la formulación y vía de administración (por ejemplo, tópica ocular) y su compatibilidad regulatoria
- Revisar el prospecto de INVIMA para completar advertencias y contraindicaciones
- Confirmar con el equipo de datos que las entradas duplicadas de glaucoma de ángulo cerrado se fusionen; ambas tienen evidencia L5 y no sustentan una justificación terapéutica
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

