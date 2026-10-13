---
layout: default
title: Moxifloxacin
parent: Solo Predicción del Modelo (L5)
nav_order: 457
evidence_level: L5
indication_count: 10
---

# Moxifloxacin
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

# Moxifloxacino: De Dexametasona y Antiinfecciosos (Moxifloxacina) a Síndrome de Hiperviscosidad Policlonal

## Resumen en Una Frase

Moxifloxacino es un antibiótico fluoroquinolónico, registrado en Colombia en una solución oftálmica combinada con dexametasona y en tabletas recubiertas de 400 mg.
El modelo TxGNN predice que podría ser efectivo para **síndrome de hiperviscosidad policlonal**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta indicación; se trata únicamente de una predicción basada en el grafo de conocimiento.
Entre las demás predicciones, solo la **peste bubónica** muestra evidencia preclínica plausible (estudios in vitro y en animales).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dexametasona y antiinfecciosos (registro de la solución oftálmica); moxifloxacina (tabletas) |
| Nueva Indicación Predicha | Síndrome de hiperviscosidad policlonal |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, moxifloxacino es una fluoroquinolona antibacteriana que inhibe la ADN girasa y la topoisomerasa IV bacterianas. Su eficacia está establecida en infecciones bacterianas, no en trastornos de la viscosidad sanguínea.

La hiperviscosidad policlonal surge por un aumento de las inmunoglobulinas séricas. No se identifica un vínculo mecanístico plausible con un antibacteriano; el puntaje alto de TxGNN refleja probablemente la cercanía en el grafo de conocimiento y no una razón farmacológica.

Entre las otras predicciones del modelo, la **peste bubónica** (puntaje 99.41%) es la única biológicamente coherente: moxifloxacino es activo contra *Yersinia pestis* en modelos in vitro y en ratones. Otras indicaciones hematológicas (gammapatía monoclonal, trastornos hematológicos congénitos) solo tienen relación indirecta, como prevención o tratamiento de infecciones en pacientes con neutropenia o trasplante.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para síndrome de hiperviscosidad policlonal.

*Nota: para otras indicaciones predichas existen ensayos solo indirectamente relacionados (por ejemplo, [NCT00324324](https://clinicaltrials.gov/study/NCT00324324), Fase 3, terminado, 240 participantes, profilaxis antibacteriana tras trasplante alogénico de progenitores hematopoyéticos; y [NCT00062231](https://clinicaltrials.gov/study/NCT00062231), terminado, 351 participantes, terapia oral empírica de la fiebre en pacientes oncológicos neutropénicos). Ninguno evalúa la indicación principal.*

---

## Informacion de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20165941 (cancelado) | TQ OFTAMOX® D UD | Solución oftálmica | Dexametasona y antiinfecciosos |
| 20133598 (cancelado) | MOXFACIN® 400 MG TABLETA RECUBIERTA | Tableta recubierta | Moxifloxacina |

---

## Consideraciones de Seguridad

- **Contraindicaciones o condiciones de riesgo (según el grafo de conocimiento, no según el prospecto):** síndrome de QT largo (incluido el familiar), torsades de pointes, paro cardíaco súbito, enfermedades de la conducción cardíaca, isquemia miocárdica y enfermedad coronaria; epilepsia; miastenia gravis y enfermedades de la unión neuromuscular; neuropatía periférica y enfermedades del sistema nervioso periférico; tendinitis, periartritis y exostosis; cirrosis hepática y lesión hepática inducida por fármacos; deficiencia de potasio; colitis por *Clostridium difficile* y enterocolitis necrosante perinatal.
- **Interacciones farmacológicas:** se identificaron 336 interacciones. Entre las de nivel **mayor** figuran corticoesteroides (hidrocortisona, triamcinolona, dexametasona, betametasona), bupropión y clorpropamida. Entre las de nivel moderado: antidiabéticos (acarbosa, metformina, pioglitazona, alogliptina, canagliflozina, albiglutida), famotidina, loperamida, ácido acetilsalicílico, balsalazida, bisacodilo y sales de calcio y potasio.
- **Aviso relevante:** la predicción para "enfermedad hematológica asociada a neuropatía periférica adquirida" plantea una preocupación de seguridad, pues las fluoroquinolonas se asocian con neuropatía periférica.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para síndrome de hiperviscosidad policlonal es solo un resultado del modelo (L5), sin ensayos ni literatura, y sin mecanismo plausible. Además, no existen registros sanitarios vigentes en Colombia y el perfil de seguridad del fármaco es considerable.

**Para avanzar se necesita:**
- Obtener el prospecto del INVIMA para completar advertencias y contraindicaciones oficiales (brecha bloqueante).
- Obtener datos del mecanismo de acción desde DrugBank.
- Reorientar el análisis hacia la **peste bubónica**, la única indicación con respaldo preclínico plausible (L4), evaluando si hay interés clínico y regulatorio local.
- Confirmar la situación regulatoria (registros cancelados) antes de cualquier desarrollo en Colombia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

