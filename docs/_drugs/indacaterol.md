---
layout: default
title: Indacaterol
parent: 僅模型預測 (L5)
nav_order: 92
evidence_level: L5
indication_count: 10
---

# Indacaterol
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

Usando el skill `txgnn-pipeline` como contexto de proyecto. Procedo a generar el informe a partir del Evidence Pack proporcionado.

---

# Indacaterol: De EPOC/Asma a Síndrome Nefrogénico de Antidiuresis Inapropiada

## Resumen en Una Frase

Indacaterol es un agonista β₂-adrenérgico de acción ultralarga (ultra-LABA) aprobado internacionalmente para el tratamiento de la Enfermedad Pulmonar Obstructiva Crónica (EPOC) y el asma, aunque actualmente no se encuentra registrado en Colombia.
El modelo TxGNN predice que podría ser efectivo para el **Síndrome Nefrogénico de Antidiuresis Inapropiada (NSIAD)**,
con **0 ensayos clínicos** y **0 publicaciones** que respalden actualmente esta dirección; la predicción se basa exclusivamente en conexiones del grafo de conocimiento biomédico.

---

## Resumen Rápido

| Ítem | Contenido |
|------|-----------|
| Indicación Original | EPOC / Asma (ultra-LABA de acción prolongada; clase farmacológica establecida) |
| Nueva Indicación Predicha | Síndrome Nefrogénico de Antidiuresis Inapropiada (NSIAD) |
| Puntaje de Predicción TxGNN | 99.54% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción desde las fuentes regulatorias colombianas. Con base en el conocimiento farmacológico establecido, Indacaterol es un agonista β₂-adrenérgico de acción ultralarga (ultra-LABA) cuyo mecanismo central consiste en la activación de receptores β₂ en el músculo liso bronquial: esto eleva el AMP cíclico (AMPc) intracelular, activa la proteína quinasa A (PKA) y produce relajación muscular con broncodilatación sostenida de 24 horas. Es parte de combinaciones de dosis fija ampliamente estudiadas (IND/GLY, IND/GLY/MOM) para EPOC y asma.

El Síndrome Nefrogénico de Antidiuresis Inapropiada (NSIAD) es una enfermedad de origen genético causada por mutaciones de ganancia de función en el receptor de vasopresina tipo 2 (AVPR2), que mantiene el receptor constitutivamente activo, elevando de forma sostenida el AMPc independientemente de la vasopresina. La conexión hipotética explorada por TxGNN se apoya en que la señalización β₂ → AMPc↑ → PKA podría, teóricamente, cruzarse con la vía downstream ya activa del receptor AVPR2, ya que ambas convergen en el segundo mensajero AMPc.

Sin embargo, esta intersección de señalización nunca ha sido validada en el contexto específico del NSIAD, ni existen datos preclínicos o hipótesis clínicas formales al respecto. La marcada discrepancia entre el altísimo puntaje TxGNN (99.54%) y la ausencia total de evidencia real coloca esta predicción en la categoría clásica de **"predicción exclusiva por grafo" (graph-predicted only)**, sin respaldo experimental independiente.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados con NSIAD e Indacaterol registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada con NSIAD e Indacaterol disponible.

---

## Información de Mercado en Colombia

Indacaterol no cuenta con ningún registro sanitario activo en Colombia. El fármaco no se encuentra comercializado en el mercado colombiano a la fecha de corte de este informe (2026-05-05).

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
A pesar del altísimo puntaje TxGNN (99.54%), la predicción para NSIAD carece por completo de evidencia clínica o preclínica de respaldo. La conexión mecanística propuesta entre la señalización β₂ y el receptor constitutivamente activo AVPR2 es puramente hipotética y ningún estudio la ha explorado, lo que impide avanzar con confianza hacia investigación traslacional o clínica.

**Para avanzar se necesita:**
- **Estudios preclínicos**: modelos celulares o animales de NSIAD que validen la hipótesis de interacción β₂ → AMPc / AVPR2 como concepto de prueba
- **Datos de MOA completos**: consultar DrugBank (DB05039) para confirmar el perfil de receptor y los efectos sistémicos conocidos
- **Información de seguridad**: obtener advertencias, contraindicaciones y perfil de interacciones farmacológicas desde el prospecto oficial (TFDA/EMA/FDA)
- **Evaluación de viabilidad de ruta de administración**: Indacaterol es un fármaco inhalado con biodisponibilidad sistémica muy baja (<2%); sería necesario evaluar si este perfil farmacocinético permite alcanzar concentraciones renales terapéuticas o si se requeriría una formulación alternativa
- **Gestión de registro sanitario en Colombia**: el fármaco no está comercializado en el país; cualquier investigación requeriría aprobación de INVIMA para uso en investigación

> **Nota clínica adicional**: Entre las 10 indicaciones predichas por TxGNN para Indacaterol, la indicación **"bronchial disease" (rango 7)** presenta el nivel de evidencia más alto (L1), con más de 37 ensayos clínicos y 20 publicaciones, y una recomendación de **"Proceed with Guardrails"**. Esta corresponde esencialmente al uso broncodilatador ya establecido del fármaco (EPOC/asma), lo que valida el modelo pero no constituye reposicionamiento propiamente dicho. Las demás indicaciones nuevas predichas (rangos 1–6 y 8–10) son todas L5/Hold sin evidencia de respaldo.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

