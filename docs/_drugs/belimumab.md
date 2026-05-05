---
layout: default
title: Belimumab
parent: 僅模型預測 (L5)
nav_order: 66
evidence_level: L5
indication_count: 6
---

# Belimumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Belimumab: De Lupus Eritematoso Sistémico a Trastorno Primario de Liberación Plaquetaria

## Resumen en Una Frase

Belimumab es un anticuerpo monoclonal humano que inhibe BLyS (estimulador de linfocitos B), aprobado internacionalmente para el lupus eritematoso sistémico (LES) y la nefritis lúpica, aunque sin registro vigente en Colombia. El modelo TxGNN predice que podría ser efectivo para el **Trastorno Primario de Liberación Plaquetaria**; sin embargo, el único ensayo clínico identificado no guarda relación con esta indicación y no existe literatura de respaldo, lo que resulta en una evidencia de nivel **L5** y una recomendación de **Hold**.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Lupus eritematoso sistémico (aprobación internacional; sin registro en Colombia) |
| Nueva Indicación Predicha | Trastorno primario de liberación plaquetaria |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos formales sobre el mecanismo de acción en el sistema de evaluación. Con base en la información conocida, Belimumab es un anticuerpo monoclonal IgG1λ que bloquea la unión de BLyS (B-Lymphocyte Stimulator / BAFF) a sus receptores en los linfocitos B. Al suprimir esta señal de supervivencia, reduce la proliferación de células B autorreactivas y la producción de autoanticuerpos patogénicos. Este mecanismo sustenta su eficacia comprobada en el lupus eritematoso sistémico.

El trastorno primario de liberación plaquetaria —como la deficiencia de gránulos densos— es una enfermedad funcional o estructural de las plaquetas, no mediada por linfocitos B ni por autoanticuerpos. El eje BLyS/B-células no interviene en los mecanismos de degranulación o secreción plaquetaria, por lo que la inhibición de BLyS carece de vía biológica directa sobre este tipo de defecto.

El análisis de la racionalidad de reposicionamiento indica que el alto puntaje TxGNN refleja muy probablemente un **efecto de proximidad en el grafo de conocimiento** —es decir, características compartidas entre nodos de enfermedades hematológicas— y no una conexión biológica real. Esta predicción debe interpretarse como una señal exploratoria sin sustento mecanístico sólido, y no como evidencia de eficacia potencial.

---

## Evidencia de Ensayos Clínicos

> ⚠️ **Advertencia de relevancia:** El único ensayo identificado en la búsqueda corresponde a una enfermedad renal (glomerulonefritis membranosa idiopática), **completamente distinta** al trastorno primario de liberación plaquetaria. Fue clasificado internamente como **Grado C (no relevante)** y no constituye evidencia de soporte para esta indicación. Se incluye en la tabla únicamente por transparencia del proceso de búsqueda.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01610492](https://clinicaltrials.gov/study/NCT01610492) | Fase 2 | Completado | 14 | Estudio mecanístico de belimumab en glomerulonefritis membranosa idiopática con anticuerpos anti-PLA2R positivos. **Sin relación con trastorno plaquetario.** |

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación predicha.

---

## Información de Mercado en Colombia

Belimumab no cuenta con registros sanitarios vigentes en Colombia (0 registros ante INVIMA). No se dispone de tabla de licencias aprobadas.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad completa.

> **Nota clínica relevante identificada durante la evaluación:** La racionalidad de reposicionamiento de este expediente registra una **advertencia de recuadro negro (black box warning) de la FDA** que contraindica el uso de belimumab durante el embarazo. Al ser un anticuerpo IgG1, puede transferirse activamente a través de la placenta vía FcRn, con riesgo de depleción de células B en el neonato. Este dato es especialmente crítico para la indicación de rango 4 de este expediente (trombocitopenia aloinmune fetal y neonatal) y deberá considerarse en cualquier evaluación clínica futura.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción TxGNN para el trastorno primario de liberación plaquetaria carece de sustento mecanístico: esta condición es un defecto funcional o estructural plaquetario no mediado por el eje BLyS/linfocitos B. El único ensayo clínico identificado es irrelevante para la indicación predicha, y no existe ninguna publicación científica de respaldo. El alto puntaje del modelo (99.96%) es probablemente un artefacto del grafo de conocimiento, no una señal biológica real.

**Para avanzar se necesita:**
- Completar el registro del mecanismo de acción (MOA) formal de belimumab en la base de datos (DrugBank API)
- Obtener y analizar el prospecto aprobado para documentar advertencias clave, contraindicaciones e interacciones farmacológicas
- Evaluar de forma separada la indicación de rango 4 (*trombocitopenia aloinmune fetal y neonatal*), que presenta la racionalidad mecanística más plausible de este expediente, pero requiere análisis de seguridad materno-fetal especializado antes de cualquier avance
- Gestionar el trámite de registro sanitario ante INVIMA si se contempla investigación clínica local con este compuesto
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

