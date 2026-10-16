---
layout: default
title: Travoprost
parent: Solo Predicción del Modelo (L5)
nav_order: 640
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Travoprost: nueva indicación predicha, Calcifilaxis visceral (nivel de evidencia L5). Indicación original: Travoprost"
monitor_inn: "TRAVOPROST"
predicted_indications: ["visceral calciphylaxis", "arterial thoracic outlet syndrome", "venous thoracic outlet syndrome", "neurogenic thoracic outlet syndrome", "vascular disease", "angiodysplasia of stomach", "blue toe syndrome", "idiopathic spontaneous coronary artery dissection", "lymphangiectasis", "hemangioendothelioma"]
---

# Travoprost
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Travoprost: De Glaucoma/Hipertensión Ocular a Calcifilaxis Visceral

## Resumen en Una Frase

Travoprost es un análogo de la prostaglandina F2-alfa que se aplica en gotas oftálmicas y cuyo uso conocido es reducir la presión intraocular (glaucoma e hipertensión ocular); en los registros sanitarios colombianos solo figura el nombre del principio activo como indicación.
El modelo TxGNN predice que podría ser efectivo para **calcifilaxis visceral**, pero no hay **ningún ensayo clínico** ni **ninguna publicación** que respalde esta dirección: es una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Travoprost (el registro solo indica el nombre del principio activo; el uso conocido es glaucoma e hipertensión ocular) |
| Nueva Indicación Predicha | Calcifilaxis visceral |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 4 (todos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, travoprost es un agonista del receptor FP (análogo de la prostaglandina F2-alfa), con efecto vasodilatador propio de su clase. En el ojo reduce la presión intraocular al aumentar el drenaje uveoescleral.

La relación con la nueva indicación es débil. No se ha establecido un vínculo plausible entre la activación del receptor FP y la calcificación vascular o la patología de la calcifilaxis. Además, la aplicación ocular tópica produce una exposición sistémica mínima, lo que hace aún menos probable un efecto en una enfermedad visceral o sistémica.

La puntuación del modelo es muy alta (99.99%), pero sin ensayos, literatura ni racional mecanístico, debe interpretarse solo como una hipótesis que requiere validación preclínica antes de cualquier consideración clínica.

### Otras predicciones del modelo (todas con evidencia L5, salvo indicación)

| Posición | Enfermedad predicha | Puntaje TxGNN | Nivel | Comentario |
|---|---|---|---|---|
| 2 | Síndrome del desfiladero torácico arterial | 99.99% | L5 | Problema principalmente de compresión mecánica |
| 3 | Síndrome del desfiladero torácico venoso | 99.99% | L5 | Requiere anticoagulación, trombólisis o descompresión quirúrgica |
| 4 | Síndrome del desfiladero torácico neurogénico | 99.99% | L5 | Sin vínculo con el agonismo FP |
| 5 | Enfermedad vascular | 99.99% | L4 | Señal probablemente artefacto semántico de efectos vasculares oculares (hiperemia) |
| 6 | Angiodisplasia de estómago | 99.99% | L5 | Posible daño por efecto vasoactivo |
| 7 | Síndrome del dedo azul | 99.99% | L5 | Causado por microembolias; exposición sistémica insignificante |
| 8 | Disección coronaria espontánea idiopática | 99.99% | L5 | Sin vínculo mecanístico |
| 9 | Linfangiectasia | 99.99% | L5 | Hipótesis especulativa sobre biología linfática |
| 10 | Hemangioendotelioma | 99.99% | L4 | Solo un reporte de caso de efecto adverso |

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para **calcifilaxis visceral**.

Para contexto, la predicción de rango 5 (enfermedad vascular) tiene ensayos asociados. Todos son estudios en glaucoma o hipertensión ocular, no tratamientos de enfermedad vascular. El único con un criterio de fisiología vascular es el siguiente:

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00308945](https://clinicaltrials.gov/study/NCT00308945) | Fase 4 | Completado | 20 | Compara travoprost y latanoprost sobre el diámetro vascular retiniano y el flujo sanguíneo coroideo en pacientes con glaucoma; es hemodinámica ocular local, no tratamiento de enfermedad vascular |

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para **calcifilaxis visceral**.

Como contexto, la literatura asociada a otras predicciones se centra en el uso ocular y la seguridad:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31335731](https://pubmed.ncbi.nlm.nih.gov/31335731/) | 2019 | Revisión | Medicine | Evaluación sistemática de la eficacia de travoprost en glaucoma |
| [22167538](https://pubmed.ncbi.nlm.nih.gov/22167538/) | 2012 | Metaanálisis | Eur J Ophthalmol | Eficacia y tolerabilidad de combinaciones fijas de prostaglandina-timolol |
| [23231442](https://pubmed.ncbi.nlm.nih.gov/23231442/) | 2013 | Metaanálisis | J Ocul Pharmacol Ther | Análogos de prostaglandina con timolol, fijos vs. no fijos, en glaucoma de ángulo abierto |
| [19019922](https://pubmed.ncbi.nlm.nih.gov/19019922/) | 2009 | Metaanálisis de ECA | Br J Ophthalmol | Hiperemia conjuntival con latanoprost frente a travoprost y bimatoprost |
| [19107053](https://pubmed.ncbi.nlm.nih.gov/19107053/) | 2008 | Reporte de caso | J Fr Ophtalmol | Efusión uveal inducida por travoprost tópico en un paciente con síndrome de Sturge-Weber-Krabbe (señal de seguridad) |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20219978 | GLAUCOPROST Solución Oftálmica Estéril | Solución oftálmica | Travoprost | Cancelado |
| 19950508 | GLAUCOPROST Solución Oftálmica | Solución oftálmica | Travoprost | Cancelado |
| 20087519 | FOCUS® | Solución oftálmica | Travoprost | Cancelado |
| 20236408 | BRISTRIO® | Solución oftálmica | Travoprost | Cancelado |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no son texto de prospecto)**: uveítis, enfermedad del iris, enfermedad del cuerpo ciliar, panuveítis, iritis, edema macular cistoide y edema macular retiniano.
- **Interacciones Farmacológicas**: se identificaron 49 posibles interacciones, todas con nivel de gravedad desconocido. Entre las principales figuran calcitriol, pantoprazol, sucralfato, morfina, metformina, omeprazol, prednisona, prednisolona, triamcinolona, simvastatina y ácido acetilsalicílico.
- **Señal de seguridad relevante**: un reporte de caso describe efusión uveal con desprendimiento de retina exudativo inducido por travoprost tópico en un paciente con malformación vascular (síndrome de Sturge-Weber-Krabbe), lo que sugiere precaución en pacientes con vasculatura anómala.
- **Efecto adverso conocido de la clase**: hiperemia conjuntival, descrita en los ensayos y la literatura revisada.

Para advertencias y contraindicaciones del prospecto, consultar el prospecto del producto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para calcifilaxis visceral se basa solo en el modelo, sin ensayos ni literatura, sin vínculo mecanístico plausible y con exposición sistémica mínima por la vía ocular. Además, el mercado colombiano no tiene registros vigentes de travoprost.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y un racional biológico que conecte la señalización del receptor FP con la calcificación vascular.
- Estudios preclínicos in vitro o en modelos animales de calcifilaxis.
- Evaluar la viabilidad de una vía de administración sistémica, ya que la vía oftálmica no alcanzaría exposición suficiente.
- Obtener las advertencias y contraindicaciones del prospecto en INVIMA.
- Revisar la situación regulatoria: los cuatro registros están cancelados.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

