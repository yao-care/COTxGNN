---
layout: default
title: Gefitinib
parent: 僅模型預測 (L5)
nav_order: 84
evidence_level: L5
indication_count: 10
---

# Gefitinib
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

# GEFITINIB: De Cáncer de Pulmón de Células No Pequeñas a Fibromatosis Gingival

## Resumen en Una Frase

Gefitinib (Iressa) es un inhibidor de tirosina quinasa del receptor del factor de crecimiento epidérmico (EGFR-TKI de primera generación), originalmente utilizado para el tratamiento del cáncer de pulmón de células no pequeñas (NSCLC) con mutaciones activadoras del EGFR.
El modelo TxGNN predice que podría ser efectivo para **Fibromatosis Gingival**,
sin embargo, actualmente **no existen ensayos clínicos ni publicaciones científicas** que respalden directamente esta aplicación.

---

## Resumen Rápido

| Ítem | Contenido |
|------|------|
| Indicación Original | Cáncer de pulmón de células no pequeñas (NSCLC) con mutación EGFR |
| Nueva Indicación Predicha | Fibromatosis Gingival |
| Puntaje de Predicción TxGNN | 99.89% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, Gefitinib es un inhibidor selectivo de la tirosina quinasa del EGFR (receptor del factor de crecimiento epidérmico), aprobado globalmente para el tratamiento de primera línea del NSCLC con mutaciones activadoras (exones 19 y 21). Su mecanismo consiste en bloquear competitivamente el sitio de unión al ATP del dominio intracelular del EGFR, inhibiendo la fosforilación del receptor y las cascadas de señalización aguas abajo (RAS/MAPK, PI3K/AKT) que promueven la proliferación celular, angiogénesis y supervivencia tumoral.

La fibromatosis gingival es una condición caracterizada por la proliferación excesiva de fibroblastos gingivales, que puede ser hereditaria o inducida por fármacos. Dado que la señalización del EGFR participa en la regulación general de la proliferación de fibroblastos, existe una conexión teórica por la cual un EGFR-TKI podría suprimir esta hiperproliferación. El razonamiento del modelo apunta a que la inhibición de EGFR modularía el ciclo de vida del fibroblasto gingival.

No obstante, esta relación es indirecta y altamente especulativa. No hay evidencia de que los fibroblastos gingivales sobreexpresen o dependan críticamente del EGFR en el contexto de la fibromatosis gingival. La ausencia total de estudios clínicos y preclínicos que respalden esta hipótesis ubica esta predicción en el nivel de evidencia más bajo (L5), y la recomendación de decisión es **Hold** hasta que existan datos básicos de validación.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Citotoxicidad

| Ítem | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (EGFR-TKI de primera generación, clase quinazolinamina) |
| Riesgo de Mielosupresión | Bajo (los EGFR-TKI tienen potencial mielosupresor mínimo en comparación con quimioterapia citotóxica convencional) |
| Clasificación de Emetogenicidad | Baja |
| Ítems de Monitoreo | Función hepática (ALT/AST/bilirrubina), función renal, monitoreo pulmonar activo por riesgo de Enfermedad Pulmonar Intersticial (EPI/ILD), intervalo QTc basal y periódico, reacciones cutáneas (erupción acneiforme, xerosis, paroniquia) |
| Protección en Manejo | Seguir precauciones estándar para agentes antineoplásicos orales; almacenamiento y disposición según normativa vigente de medicamentos citotóxicos |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La conexión mecanística propuesta entre la inhibición del EGFR y la fibromatosis gingival es puramente teórica, sin respaldo de ningún estudio clínico ni preclínico. Adicionalmente, Gefitinib no cuenta con registro sanitario en Colombia (0 registros), lo que representa una barrera regulatoria significativa para cualquier desarrollo en este mercado.

**Para avanzar se necesita:**
- Estudios preclínicos (in vitro/in vivo) que confirmen la expresión funcional de EGFR en fibroblastos gingivales en modelos de fibromatosis gingival
- Evaluación del mecanismo de acción detallado de Gefitinib en fibroblastos no epiteliales
- Obtener datos completos de seguridad: advertencias INVIMA/EMA, contraindicaciones e interacciones farmacológicas relevantes
- Definir una vía regulatoria en Colombia (registro sanitario o uso bajo protocolo de investigación)
- Análisis de expresión génica y proteómica en tejido gingival fibromatoso para validar la diana EGFR
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

