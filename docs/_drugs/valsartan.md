---
layout: default
title: Valsartan
parent: 僅模型預測 (L5)
nav_order: 234
evidence_level: L5
indication_count: 7
---

# Valsartan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Valsartan: De Hipertensión Arterial a Enfermedad Renal Hipertensiva Maligna

## Resumen en Una Frase

Valsartan es un bloqueador selectivo del receptor de angiotensina II tipo 1 (ARB), ampliamente utilizado a nivel mundial para el tratamiento de la hipertensión arterial, la insuficiencia cardíaca con fracción de eyección reducida y la cardioprotección post-infarto de miocardio.
El modelo TxGNN predice que podría ser efectivo para la **Enfermedad Renal Hipertensiva Maligna** (indicación #1 por puntaje), con **0 ensayos clínicos** y **1 publicación** que actualmente respaldan esta dirección.
Cabe destacar que la indicación **Cardiopatía Pulmonar Crónica** (rank 6) presenta la evidencia más sólida del análisis completo: **7 ensayos clínicos** y **20 publicaciones** (Nivel L2, recomendación: *Proceed with Guardrails*).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial (ARB de clase global; sin registro en base de datos local) |
| Nueva Indicación Predicha | Enfermedad Renal Hipertensiva Maligna |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos formales sobre el mecanismo de acción en la fuente de datos consultada. Sin embargo, Valsartan es un antagonista selectivo del receptor AT1 de angiotensina II, cuya acción principal consiste en interrumpir el eje renina-angiotensina-aldosterona (RAAS): al bloquear el AT1, inhibe la vasoconstricción, la secreción de aldosterona, la fibrosis renal mediada por TGF-β y la proliferación de células mesangiales. Su eficacia en hipertensión, insuficiencia cardíaca y nefroprotección ha sido documentada en múltiples ensayos controlados aleatorios de gran escala (IDNT, RENAAL, Val-HeFT, PARADIGM-HF).

La enfermedad renal hipertensiva maligna se caracteriza por una activación aberrante y autosostenida del RAAS: la hipertensión maligna genera isquemia renal que eleva renina y angiotensina II, perpetuando un ciclo de daño vascular (necrosis fibrinoide), proteinuria y deterioro progresivo de la función renal. Mecanísticamente, el bloqueo AT1 por valsartan podría interrumpir este ciclo al reducir la presión intraglomerular, limitar la fibrosis y disminuir la proteinuria, efectos que los ARBs han demostrado en nefropatía diabética e hipertensiva general.

El puntaje TxGNN de 99.97% refleja una alta coherencia mecanística entre el perfil farmacológico de valsartan y esta entidad clínica. No obstante, los ensayos IDNT y RENAAL evaluaron nefropatía hipertensiva general, no la forma maligna como entidad diferenciada, y la única publicación disponible en la búsqueda estudia avosentan (antagonista de endotelina) en un modelo animal de hipertensión maligna, sin datos directos sobre valsartan. La brecha entre coherencia mecanística y evidencia clínica directa justifica una evaluación cautelosa.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta indicación específica.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [24368192](https://pubmed.ncbi.nlm.nih.gov/24368192/) | 2014 | Experimental (animal) | Pharmacological Research | En ratas transgénicas con sobreexpresión de renina/angiotensinógeno humano, avosentan mostró efecto nefroprotector contra nefropatía hipertensiva a dosis sin retención de líquidos; respalda indirectamente que el bloqueo del RAAS es relevante en hipertensión renal maligna, aunque el fármaco estudiado **no es valsartan** |

> ⚠️ La publicación disponible estudia avosentan (antagonista de endotelina), no valsartan. La relevancia para la indicación predicha es de carácter mecanístico e indirecto.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El puntaje TxGNN es muy alto (99.97%) y la coherencia mecanística entre el bloqueo AT1 y el ciclo RAAS de la hipertensión renal maligna es sólida, pero la única publicación disponible estudia un fármaco diferente en modelos animales y no existe ningún ensayo clínico registrado para esta indicación específica, lo que limita el nivel de evidencia a L4 y no permite avanzar sin investigación adicional.

**Para avanzar se necesita:**
- Búsqueda dirigida de estudios observacionales, series de casos o reportes clínicos de ARBs en crisis hipertensivas con daño renal agudo o crónico (e.g., "malignant hypertension with AKI/CKD")
- Revisión de guías internacionales de manejo de emergencias hipertensivas con compromiso renal para identificar el rol actual de los ARBs
- Obtener datos formales de mecanismo de acción (MOA) y perfil de seguridad de Valsartan (advertencias, contraindicaciones) mediante consulta a DrugBank y ficha técnica oficial
- Verificar el estado real de comercialización en Colombia (INVIMA), ya que Valsartan tiene amplia distribución global y la ausencia de registros puede reflejar una limitación de la fuente de datos
- **Evaluar priorizar la indicación de Cardiopatía Pulmonar Crónica** (rank 6): con 7 ensayos clínicos (incluyendo Phase 4 RCT completados con sacubitril/valsartan) y 20 publicaciones —entre ellas análisis post-hoc de PARADIGM-HF y PARAGON-HF—, constituye la indicación con mayor evidencia disponible en este análisis y cuenta con recomendación *Proceed with Guardrails* (Nivel L2)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

