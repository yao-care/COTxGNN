---
layout: default
title: Brigatinib
parent: Solo Predicción del Modelo (L5)
nav_order: 114
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Brigatinib: nueva indicación predicha, Fibromatosis gingival (nivel de evidencia L5). Indicación original: Brigatinib"
monitor_inn: "BRIGATINIB"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung benign neoplasm", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "pulmonary sulcus neoplasm", "lung germ cell tumor", "junctional epidermolysis bullosa", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome"]
---

# Brigatinib
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

## Brigatinib: De la indicación registrada (sin texto descriptivo) a Fibromatosis gingival
{: .text-alpha }

## Resumen en Una Frase

Brigatinib es un inhibidor de la quinasa del linfoma anaplásico (ALK), conocido por su uso en cáncer de pulmón no microcítico (CPNM) ALK positivo; en Colombia, sus registros sanitarios solo consignan el nombre del principio activo como indicación.
El modelo TxGNN predice que podría ser efectivo para **fibromatosis gingival**, pero esta predicción no cuenta con **ningún ensayo clínico ni publicación** que la respalde.
Se trata de una predicción del modelo TxGNN (aprendizaje profundo), sin evidencia real; la puntuación puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Brigatinib (el registro sanitario solo consigna el nombre del principio activo, sin texto de indicación) |
| Nueva Indicación Predicha | Fibromatosis gingival |
| Puntaje de Predicción TxGNN | 0.9989 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: 2 de 2) |
| Número de Registros Sanitarios | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la literatura conocida, brigatinib es un inhibidor de tirosina quinasas de nueva generación, con actividad principal frente a ALK y, según el análisis del modelo, también frente a EGFR y FAK. Su eficacia en CPNM ALK positivo está respaldada por el ensayo de fase 3 ALTA-1L.

Sin embargo, el análisis de los datos compilados **no identificó un vínculo mecanístico plausible** entre la inhibición de estas quinasas y la fibromatosis gingival, una condición de crecimiento excesivo del tejido gingival, generalmente benigno. La alta puntuación proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no una relación biológica demostrada.

Además, el perfil de toxicidad de un inhibidor de quinasas difícilmente se justificaría para una lesión benigna como esta, salvo que existiera evidencia clínica sólida, que hoy no existe.

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
| 20193913 | ALUNBRIG® 90MG | Tableta recubierta | BRIGATINIB | Vigente |
| 20193910 | ALUNBRIG® 30MG | Tableta recubierta | BRIGATINIB | Vigente |

Ambos registros pertenecen a Takeda Colombia S.A.S. y se encuentran cancelados; actualmente no hay registros vigentes.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasas, ALK) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto; como práctica general, hemograma, función hepática y renal |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 posibles interacciones. Entre las principales:
  - **Mayores**: aprepitant, dexametasona, claritromicina.
  - **Moderadas**: antiácidos y supresores de ácido (famotidina, ranitidina, rabeprazol, cimetidina), antidiabéticos (metformina, pioglitazona, alogliptina, acarbosa, canagliflozina, dapagliflozina, clorpropamida, acetohexamida, albiglutida), loperamida, morfina, cisaprida y clotrimazol.

Para advertencias y contraindicaciones, consultar el prospecto. Un reporte de caso en la literatura compilada describe un síndrome de lisis tumoral fatal asociado a brigatinib en un paciente con adenocarcinoma de pulmón.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para fibromatosis gingival es solo una puntuación del modelo (nivel L5), sin ensayos, sin publicaciones y sin un vínculo mecanístico identificable. Además, los registros sanitarios en Colombia están cancelados.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank.
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), pendiente y bloqueante para el cribado de seguridad.
- Revisión de literatura biológica que conecte las vías ALK/EGFR/FAK con la fibromatosis gingival.
- Confirmar la situación regulatoria y la disponibilidad real del producto en Colombia.

**Observación sobre otras predicciones del modelo:** de las predicciones adicionales, la asociada al síndrome de leucomelanodermia-infantilismo-discapacidad intelectual-hipodoncia-hipotricosis presenta literatura que en realidad corresponde a la **schwannomatosis relacionada con NF2**. Allí hay un reporte clínico (NEJM 2024) y un estudio preclínico que muestran reducción tumoral con brigatinib, probablemente mediante inhibición de FAK. Es una señal de reposicionamiento creíble, pero debe reasignarse a la schwannomatosis relacionada con NF2 para una evaluación formal, y no atribuirse al síndrome listado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

