---
layout: default
title: Maraviroc
parent: 僅模型預測 (L5)
nav_order: 166
evidence_level: L5
indication_count: 10
---

# Maraviroc
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

# Maraviroc: De Infección por VIH-1 a Neoplasia Endocrina Múltiple

## Resumen en Una Frase

Maraviroc es un antagonista selectivo del receptor de quimiocinas CCR5, aprobado internacionalmente para el tratamiento de la infección por VIH-1 en pacientes con virus CCR5-trópico. El modelo TxGNN predice que podría ser efectivo para **Neoplasia Endocrina Múltiple (MEN)**, con **0 ensayos clínicos** y **0 publicaciones** que actualmente respaldan esta dirección. La puntuación de predicción es muy alta (99.82%), pero la evidencia experimental es inexistente y la plausibilidad mecanística es débil.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección por VIH-1 con virus CCR5-trópico (aprobado internacionalmente; no comercializado en Colombia) |
| Nueva Indicación Predicha | Neoplasia Endocrina Múltiple |
| Puntaje de Predicción TxGNN | 99.82% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción desde las fuentes consultadas. Según la información conocida, Maraviroc es un antagonista selectivo y reversible del receptor de quimiocinas CCR5, un co-receptor presente en la superficie de las células CD4+. Al bloquear la unión de la glicoproteína gp120 del VIH-1 al co-receptor CCR5, impide la fusión viral y la entrada del virus a la célula huésped. Su eficacia en infección por VIH-1 CCR5-trópico está ampliamente documentada.

La neoplasia endocrina múltiple (MEN1 y MEN2) son síndromes hereditarios impulsados por mutaciones germinales en los genes *MEN1* o *RET*, respectivamente, que producen tumores en glándulas endocrinas como paratiroides, hipófisis y suprarrenales. No existe ninguna conexión directa y establecida entre el eje CCR5 y la fisiopatología de estos síndromes. El rationale interno del Evidence Pack indica que el alto puntaje del modelo posiblemente refleja conexiones distantes en el grafo de conocimiento a través de nodos de tumores endocrinos e inmunoregulación, sin respaldo en biología molecular directa.

En consecuencia, aunque TxGNN asigna una puntuación de 99.82%, la hipótesis carece de un mecanismo molecular articulado que conecte el bloqueo de CCR5 con MEN1/MEN2. Esta predicción se interpreta como un probable artefacto de propagación en el grafo de conocimiento (*graph leakage*) hasta que emerja evidencia experimental de soporte.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

Maraviroc no cuenta con registros sanitarios activos en Colombia. El fármaco está aprobado por la FDA (2007) y la EMA para el tratamiento de VIH-1, pero no ha sido registrado ante el INVIMA. Para cualquier uso clínico local sería necesario iniciar un proceso de registro sanitario desde cero.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ninguna evidencia experimental —ni ensayos clínicos ni publicaciones— que conecte Maraviroc con el tratamiento de neoplasia endocrina múltiple, y la plausibilidad mecanística es muy baja dado que el eje CCR5 no tiene un rol conocido en la fisiopatología de MEN1/MEN2.

**Para avanzar se necesita:**
- Datos completos del mecanismo de acción (MOA) desde DrugBank para fundamentar análisis de similitud mecanística
- Evidencia preclínica de expresión funcional de CCR5 en tejidos endocrinos afectados por MEN antes de considerar cualquier hipótesis de reposicionamiento
- Registro sanitario ante INVIMA como prerequisito para cualquier desarrollo clínico en Colombia
- Considerar priorizar la evaluación de indicaciones con mayor plausibilidad mecanística identificadas en este mismo Evidence Pack: en particular **Rank 3/5 — Linfoma T Cutáneo Primario** (con literatura sobre el eje CCR5/ACKR1 en tumores T) y **Rank 10 — Carcinoma de Mama HER2+** (con evidencia preclínica directa que demuestra que CCL5 autocrina → CCR5 → ERK activa resistencia a trastuzumab, constituyendo la hipótesis de reposicionamiento con mayor solidez mecanística del conjunto)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

