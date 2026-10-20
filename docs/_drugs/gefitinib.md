---
layout: default
title: Gefitinib
parent: Solo Predicción del Modelo (L5)
nav_order: 310
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Gefitinib: nueva indicación predicha, Fibromatosis gingival (nivel de evidencia L5). Indicación original: Gefitinib"
monitor_inn: "GEFITINIB"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "hamartoma of lung", "lung benign neoplasm", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome", "lung germ cell tumor", "pulmonary sulcus neoplasm", "junctional epidermolysis bullosa"]
---

# Gefitinib
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

# Gefitinib: De Cáncer de Pulmón (EGFR) a Fibromatosis Gingival

## Resumen en Una Frase

Gefitinib es un inhibidor de la tirosina quinasa del receptor EGFR. Los registros sanitarios colombianos solo indican "gefitinib" como indicación aprobada, sin detalle de la enfermedad.
El modelo TxGNN predice que podría ser efectivo para **fibromatosis gingival**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Es una predicción basada únicamente en el modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Gefitinib (el registro sanitario no detalla la enfermedad) |
| Nueva Indicación Predicha | Fibromatosis gingival |
| Puntaje de Predicción TxGNN | 99.89% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados (sin registros vigentes) |
| Número de Registros Sanitarios | 4 (todos cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, gefitinib es un inhibidor selectivo de la tirosina quinasa del receptor del factor de crecimiento epidérmico (EGFR), y su eficacia en el cáncer de pulmón de células no pequeñas con mutaciones de EGFR está documentada en la literatura revisada.

La señal de EGFR/ErbB tiene un papel teórico en la proliferación de fibroblastos, lo que podría vincularse de forma especulativa con la fibromatosis gingival, una condición de sobrecrecimiento del tejido conectivo de la encía. Sin embargo, no hay evidencia específica de encía, y la similitud con la indicación original no ha sido evaluada.

Por ello, esta predicción debe considerarse una hipótesis generada por el modelo, no un hallazgo respaldado por datos clínicos.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Otras Predicciones Evaluadas (Contexto)

Entre las 10 principales predicciones del modelo, ninguna supera el nivel L4. Todas tienen recomendación Hold:

| Rango | Enfermedad Predicha | Puntaje TxGNN | Nivel | Observación |
|------|------|------|------|------|
| 1 | Fibromatosis gingival | 99.89% | L5 | Solo predicción |
| 2 | Fibroma de pulmón | 99.86% | L5 | Solo predicción; probable inferencia desde el uso en cáncer de pulmón |
| 3 | Miopatía por cuerpos de inclusión con enfermedad de Paget y/o demencia frontotemporal | 99.86% | L5 | Causada por mutaciones de VCP; sin vínculo plausible con EGFR |
| 4 | Hamartoma de pulmón | 99.86% | L5 | Solo predicción |
| 5 | Carcinoma del hilio pulmonar | 99.86% | L4 | Un reporte de caso; dentro de la indicación establecida de cáncer de pulmón |
| 6 | Neoplasia benigna de pulmón | 99.85% | L4 | Literatura sobre CPNM maligno; evidencia indirecta |
| 7 | Síndrome de leucomelanodermia-infantilismo-discapacidad intelectual-hipodoncia-hipotricosis | 99.84% | L5 | La literatura trata sobre toxicidades de gefitinib, no sobre este síndrome |
| 8 | Tumor de células germinales de pulmón | 99.84% | L4 | Un ensayo con relevancia tangencial (NCT00068497) |
| 9 | Neoplasia del surco pulmonar | 99.84% | L4 | Evidencia indirecta; en gran parte dentro de la indicación de cáncer de pulmón |
| 10 | Epidermólisis bullosa de la unión | 99.84% | L5 | Solo predicción; las toxicidades cutáneas de gefitinib plantean un riesgo |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20178908 | GEFALTINIB® 250MG | Tableta recubierta | Gefitinib |
| 20211358 | GRACETIB® 250 MG | Tableta recubierta | Gefitinib |
| 20217433 | GEFBOOK® 250 | Tableta recubierta | Gefitinib |
| 20187314 | GEFTRA® 250 MG | Tableta recubierta | Gefitinib |

Los cuatro registros están cancelados; actualmente no hay productos con registro vigente.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasa de EGFR) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Función hepática, función respiratoria (síntomas de neumonitis/enfermedad pulmonar intersticial), hemograma; la literatura revisada también menciona vigilancia cardiaca (prolongación del QT) y toxicidad cutánea |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no del prospecto)**: enfermedad hepática, enfermedad de la vesícula biliar, enfermedad pulmonar intersticial, fibrosis pulmonar y fibrosis pulmonar postinflamatoria.
- **Riesgos descritos en la literatura**: neumonitis aguda/enfermedad pulmonar intersticial (con un caso fatal reportado), prolongación del QT, eventos cardiovasculares (un caso de infarto de miocardio recurrente) y reacciones cutáneas (erupción acneiforme, paroniquia, xerosis).
- **Interacciones farmacológicas**: se identificaron 100 interacciones en total. Las listadas son de nivel moderado e incluyen:
  - Antiácidos y reductores de ácido: famotidina, ranitidina, cimetidina, nizatidina, omeprazol, esomeprazol, lansoprazol, dexlansoprazol, pantoprazol y rabeprazol.
  - Otros: aprepitant, claritromicina, dexametasona, naltrexona, miconazol, clotrimazol y troglitazona.
  - Nivel desconocido: calcitriol y glimepirida.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal (fibromatosis gingival) solo cuenta con el puntaje del modelo, sin ensayos ni literatura, y no existe un vínculo mecanístico documentado. Además, no hay registros sanitarios vigentes en Colombia y el perfil de seguridad de gefitinib (neumonitis, toxicidad hepática y cutánea) exige una justificación sólida para cualquier nuevo uso.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA para obtener advertencias y contraindicaciones oficiales.
- Obtener datos del mecanismo de acción desde DrugBank.
- Realizar estudios preclínicos o de mecanismo sobre la señal EGFR en fibroblastos gingivales.
- Revisar si el sobrecrecimiento gingival tiene alternativas terapéuticas con mejor perfil de seguridad.
- Evaluar la viabilidad regulatoria, dado que todos los registros están cancelados.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

