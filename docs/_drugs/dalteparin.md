---
layout: default
title: Dalteparin
parent: Solo Predicción del Modelo (L5)
nav_order: 192
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-31
description: "Dalteparin: nueva indicación predicha, Trombofilia por deficiencia de proteína C, autosómica recesiva (nivel de evidencia L5). Indicación original: No especificada"
monitor_inn: "dalteparin"
predicted_indications: ["thrombophilia due to protein C deficiency, autosomal recessive", "primary release disorder of platelets", "pseudo-von Willebrand disease", "atypical hemolytic-uremic syndrome with thrombomodulin anomaly", "neuropathy, painful"]
---

# Dalteparin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Dalteparina: De Indicación No Especificada en el Registro a Trombofilia por Deficiencia de Proteína C, Autosómica Recesiva
{: .text-alpha }

## Resumen en Una Frase

Dalteparina es una heparina de bajo peso molecular (anticoagulante) comercializada en Colombia como Fragmin® 2500 UI solución inyectable; el texto del registro sanitario solo indica el nombre del principio activo, sin detallar una indicación.
El modelo TxGNN predice que podría ser efectiva para **trombofilia por deficiencia de proteína C (autosómica recesiva)**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; la evidencia es solo la predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro solo indica "Dalteparina") |
| Nueva Indicación Predicha | Trombofilia por deficiencia de proteína C, autosómica recesiva |
| Puntaje de Predicción TxGNN | 0.9988 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 1) |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la dalteparina es una heparina de bajo peso molecular que potencia la antitrombina e inhibe el factor Xa, por lo que su eficacia antitrombótica es conocida y, mecanísticamente, podría ser aplicable a estados de hipercoagulabilidad como la deficiencia de proteína C.

La deficiencia de proteína C es un trastorno trombofílico: la falta de este anticoagulante natural favorece la formación de trombos. Un anticoagulante como la dalteparina es biológicamente plausible para prevenir la trombosis en este contexto. De hecho, la anticoagulación (heparinas, antagonistas de vitamina K y concentrado de proteína C) ya se utiliza en esta condición, aunque los datos disponibles no contienen evidencia específica de dalteparina.

Una precaución importante: en la deficiencia homocigota grave, los antagonistas de vitamina K (warfarina) conllevan riesgo de necrosis cutánea, por lo que el papel de la dalteparina requeriría una evaluación dedicada. Además, el puntaje de 0.9988 es solo una predicción del modelo y no equivale a evidencia clínica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para la indicación principal predicha (trombofilia por deficiencia de proteína C).

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19905001 (cancelado) | FRAGMIN® 2500 UI SOLUCIÓN INYECTABLE (Pfizer S.A.S.) | Solución inyectable | Dalteparina |

---

## Consideraciones de Seguridad

- **Contraindicaciones sugeridas por el grafo de conocimiento** (relaciones fármaco-enfermedad de TxGNN, no texto de prospecto): insuficiencia hepática, enfermedades hematológicas, trombocitopenia (incluida la trombocitopenia inducida por heparina), trastornos de la coagulación, hemofilia, deficiencia de antitrombina III, defectos plaquetarios cualitativos (incluida la trombastenia de Glanzmann), hemorragia intracraneal e intracerebral, desprendimiento de placenta, úlcera péptica activa, enfermedad inflamatoria intestinal y colitis ulcerosa, enfermedad de las vías biliares, ictericia obstructiva, endocarditis infecciosa (incluida la subaguda bacteriana), retinopatía (diabética e hipertensiva), retinitis, osteoporosis (incluida la posmenopáusica) y arteriosclerosis obliterante.
- **Interacciones farmacológicas**: se identificaron 174 interacciones en total. Entre las de nivel **mayor** se encuentran ácido acetilsalicílico, ibuprofeno, ketorolaco, fondaparinux, abciximab, acalabrutinib, deferasirox, trastuzumab emtansina, ibritumomab tiuxetán y tositumomab (con o sin I-131). Entre las de nivel **moderado** figuran fluvoxamina, fosinopril, fenfluramina, dexfenfluramina, sibutramina, sugammadex y yoduro I-123/I-131.

El texto de advertencias y contraindicaciones del prospecto de INVIMA no está disponible; se debe consultar el prospecto para la información de seguridad completa.

---

## Otras Predicciones Evaluadas

| Indicación Predicha | Puntaje TxGNN | Evidencia | Observación | Decisión |
|------|------|------|------|------|
| Trastorno primario de liberación plaquetaria | 0.9967 | L5 | Trastorno hemorrágico; el anticoagulante podría agravarlo. La puntuación proviene del modelo TxGNN (deep learning) y puede reflejar similitudes aprendidas entre enfermedades relacionadas, no evidencia biológica | Hold |
| Pseudo-enfermedad de von Willebrand | 0.9952 | L5 | Trastorno hemorrágico; sin mecanismo de beneficio y con riesgo de empeorar el sangrado | Hold |
| Síndrome hemolítico urémico atípico con anomalía de trombomodulina | 0.9934 | L5 | Vínculo débil y especulativo; el estándar es la inhibición del complemento | Hold |
| Neuropatía dolorosa | 0.9919 | L5 | Sin mecanismo plausible; el único ensayo asociado (NCT00445328, Fase 4, terminado, n=84) compara dalteparina con heparina no fraccionada para prevenir tromboembolismo venoso y no aborda dolor neuropático | Hold |

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal es biológicamente plausible, pero se apoya únicamente en el modelo (L5), sin ensayos ni publicaciones específicas de dalteparina. Además, el único registro sanitario colombiano está cancelado y las demás predicciones carecen de respaldo mecanístico o implican riesgo hemorrágico.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de INVIMA (advertencias y contraindicaciones), que es un vacío de datos bloqueante para el tamizaje de seguridad
- Completar los datos del mecanismo de acción desde DrugBank
- Revisión sistemática de literatura sobre heparinas de bajo peso molecular en deficiencia de proteína C
- Evaluación específica del riesgo-beneficio en deficiencia homocigota grave y de la compatibilidad de la vía de administración
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

