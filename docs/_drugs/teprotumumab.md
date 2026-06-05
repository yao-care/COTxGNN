---
layout: default
title: Teprotumumab
parent: 僅模型預測 (L5)
nav_order: 222
evidence_level: L5
indication_count: 10
---

# Teprotumumab
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

# Teprotumumab: De Oftalmopatía Tiroidea a Monosomy X

## Resumen en Una Frase

Teprotumumab es un anticuerpo monoclonal inhibidor del receptor IGF-1R (receptor del factor de crecimiento similar a la insulina tipo 1), aprobado por la FDA para el tratamiento de la oftalmopatía tiroidea activa de moderada a grave (enfermedad ocular de Graves).
El modelo TxGNN predice que podría ser efectivo para **Monosomy X** (síndrome de Turner 45,X), con un puntaje de predicción del **99.79%**.
Sin embargo, no existe ningún ensayo clínico ni publicación científica que respalde esta dirección, y el análisis mecanístico sugiere que la predicción es un falso positivo generado por la estructura del grafo de conocimiento.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Oftalmopatía tiroidea activa (enfermedad ocular de Graves) |
| Nueva Indicación Predicha | Monosomy X (síndrome de Turner 45,X) |
| Puntaje de Predicción TxGNN | 99.79% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, Teprotumumab actúa como antagonista del IGF-1R, bloqueando la señalización del factor de crecimiento similar a la insulina en tejidos orbitarios inflamados. Su eficacia en oftalmopatía tiroidea ha sido demostrada en ensayos clínicos de Fase 2 y 3, y fue aprobado por la FDA en 2020 bajo el nombre comercial Tepezza.

El modelo TxGNN vincula Teprotumumab con Monosomy X (síndrome de Turner 45,X) a través del eje IGF-1R/IGF-1, ya que las pacientes con síndrome de Turner presentan disfunción del eje GH/IGF-1 como característica central de su fisiopatología. Sin embargo, existe una contradicción mecanística fundamental: el tratamiento estándar del síndrome de Turner busca **activar** el eje GH/IGF-1 mediante suplementación de hormona de crecimiento, mientras que Teprotumumab **inhibe** IGF-1R. Usar este fármaco en Turner sería potencialmente antagonista del tratamiento de referencia.

El alto puntaje TxGNN (99.79%) refleja casi con certeza un efecto de proximidad nodal en el grafo de conocimiento: los nodos relacionados con el cromosoma X y la señalización de IGF-1R quedan adyacentes en la red sin que exista una relación terapéutica real. Este patrón se replica en 6 de las 10 indicaciones predichas, que pertenecen al espectro Turner (45,X, monosomy X mosaico, anomalías estructurales del cromosoma X, DSD de cromosomas sexuales), confirmando un agrupamiento artificial de nodos.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para Teprotumumab en Monosomy X.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para Teprotumumab en Monosomy X.

---

## Información de Mercado en Colombia

Teprotumumab no cuenta con registros sanitarios INVIMA vigentes en Colombia. El fármaco no está comercializado en el país.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
A pesar de que TxGNN asigna un puntaje extremadamente alto (99.79%), el análisis mecanístico demuestra que la inhibición de IGF-1R se opone directamente al tratamiento estándar del síndrome de Turner, que requiere activar el eje GH/IGF-1. La ausencia total de ensayos clínicos y literatura, combinada con la contradicción terapéutica, indica que esta predicción es un falso positivo estructural del grafo de conocimiento y no una oportunidad real de reposicionamiento.

**Nota sobre el patrón global de predicciones:**
De las 10 indicaciones predichas, 6 corresponden al espectro Turner/anomalías del cromosoma X (monosomy X, mosaic monosomy X, Turner estructural, mixed gonadal dysgenesis, sex chromosome DSD, X chromosome number anomaly) y 3 corresponden a patología vascular (esophageal varices sin/con sangrado, varicose disease). Todas comparten nivel de evidencia L5 y recomendación Hold. Este patrón sistemático refuerza la hipótesis de agrupamiento nodal artificial en el grafo TxGNN para este fármaco.

**Para avanzar se necesita:**
- Datos completos del mecanismo de acción (MOA) de Teprotumumab desde DrugBank o la ficha técnica oficial
- Información de seguridad completa: advertencias, contraindicaciones e interacciones farmacológicas (actualmente no disponibles)
- Registro sanitario INVIMA previo a cualquier evaluación de uso en Colombia
- Evidencia preclínica que demuestre beneficio neto de la inhibición de IGF-1R en el contexto de síndrome de Turner antes de considerar cualquier ensayo clínico
- Descarte formal de interacción antagónica con hormona de crecimiento exógena en modelos animales Turner
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

