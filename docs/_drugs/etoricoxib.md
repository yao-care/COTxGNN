---
layout: default
title: Etoricoxib
parent: 僅模型預測 (L5)
nav_order: 74
evidence_level: L5
indication_count: 10
---

# Etoricoxib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

---

# Etoricoxib: De Artritis y Dolor Musculoesquelético a Trastorno de Migraña

## Resumen en Una Frase

Etoricoxib es un inhibidor selectivo de la ciclooxigenasa-2 (COX-2) aprobado globalmente para el tratamiento del dolor e inflamación en condiciones musculoesqueléticas como osteoartritis, artritis reumatoide y espondilitis anquilosante, aunque actualmente no cuenta con ningún registro sanitario en Colombia.
El modelo TxGNN predice que podría ser efectivo para el **Trastorno de Migraña** con un puntaje de **99.90%**,
sin embargo, no existe ningún ensayo clínico ni publicación que respalde directamente esta dirección (Nivel de Evidencia L5); indicaciones relacionadas como el trastorno de cefalea (rank 9 del pack) cuentan con evidencia observacional publicada que refuerza la plausibilidad biológica de la predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sin registros en Colombia (globalmente: artritis y dolor musculoesquelético) |
| Nueva Indicación Predicha | Trastorno de Migraña (migraine disorder) |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Aunque los datos formales del mecanismo de acción (MOA) no están disponibles en el Evidence Pack actual, etoricoxib es conocido farmacológicamente como un inhibidor altamente selectivo de la ciclooxigenasa-2 (COX-2). Al bloquear esta enzima, reduce la síntesis de prostaglandina E2 (PGE2) en tejidos inflamados. Su selectividad por COX-2 le confiere un perfil gastrointestinal más favorable que los AINEs no selectivos —como la indometacina— al preservar la actividad gastroprotectora de COX-1.

La migraña es un trastorno neurovascular en el que la PGE2 desempeña un rol reconocido: participa en la activación del sistema trigeminovascular y en los procesos de sensibilización central que perpetúan y cronifican el dolor. Bajo esta lógica, la inhibición de COX-2 con reducción de PGE2 constituye una base mecanística plausible para el alivio del dolor migrañoso. Esta hipótesis se ve indirectamente reforzada por la evidencia disponible en el propio pack: para la indicación de **trastorno de cefalea** (rank 9), existen reportes de caso y series clínicas donde etoricoxib demostró eficacia en cefaleas respondedoras a indometacina (cefalea punzante primaria, cefalea tusígena secundaria), condiciones que comparten vías fisiopatológicas de PGE2 con la migraña.

Sin embargo, la predicción específica para el trastorno de migraña carece de evidencia clínica directa. El puntaje TxGNN refleja proximidad en la red biológica enfermedad–fármaco, no datos de ensayos controlados. Adicionalmente, el mecanismo COX-2/PGE2 en la migraña sigue siendo una hipótesis de trabajo: los triptanes y otros agentes específicos antimigrañosos actúan sobre dianas distintas (serotonina 5-HT1B/1D, CGRP), lo que sugiere que la inhibición de COX-2 podría ser útil como coadyuvante analgésico más que como tratamiento de primera línea.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para etoricoxib en trastorno de migraña.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para etoricoxib en trastorno de migraña.

---

## Información de Mercado en Colombia

Etoricoxib no cuenta con ningún registro sanitario activo en Colombia. El fármaco no se encuentra comercializado bajo este principio activo en el mercado colombiano. No existen fichas de registro INVIMA disponibles para consulta.

> **Nota:** A nivel global, etoricoxib (Arcoxia®) está aprobado en más de 80 países para osteoartritis, artritis reumatoide, espondilitis anquilosante, artritis gotosa aguda y dolor musculoesquelético crónico. Sin embargo, la FDA de EE. UU. rechazó su aprobación, lo que puede ser relevante para la evaluación de riesgos regulatorios en Colombia.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

> **Nota importante:** Los datos de seguridad de etoricoxib (advertencias, contraindicaciones e interacciones farmacológicas) no están disponibles en el Evidence Pack actual. Se recomienda obtener la ficha técnica oficial y el prospecto aprobado en países de referencia (EMA, ANVISA) antes de cualquier evaluación clínica. Como inhibidor selectivo de COX-2, etoricoxib comparte el perfil de riesgo cardiovascular de la clase (infarto, accidente cerebrovascular), que debe evaluarse cuidadosamente en pacientes migrañosos, quienes ya presentan mayor prevalencia de eventos cerebrovasculares.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
A pesar de un puntaje TxGNN de 99.90%, la evidencia clínica directa para etoricoxib en trastorno de migraña es completamente inexistente (Nivel L5 — solo predicción de modelo), el fármaco no está comercializado en Colombia, y los datos de seguridad locales no están disponibles; en conjunto, estos factores impiden avanzar a una evaluación clínica formal en este momento.

**Para avanzar se necesita:**
- Obtener datos formales del mecanismo de acción (MOA) desde DrugBank API (remediación identificada en DG002)
- Recuperar la ficha técnica y prospecto aprobados (EMA/ANVISA) para documentar contraindicaciones y advertencias de seguridad (remediación identificada en DG001)
- Considerar como punto de entrada más viable la indicación de **trastorno de cefalea** (rank 9 del pack, Nivel L3), que ya cuenta con publicaciones clínicas directas con etoricoxib y reduciría el riesgo regulatorio y de desarrollo
- Diseñar un estudio piloto de Fase 2 específico para migraña episódica moderada-severa si la revisión de seguridad es favorable
- Evaluar con especial cuidado el riesgo cardiovascular de etoricoxib en la población migrañosa, dado que la migraña con aura es un factor de riesgo independiente de accidente cerebrovascular
- Iniciar el proceso de registro sanitario en INVIMA como prerequisito para cualquier investigación clínica en Colombia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

