---
layout: default
title: Nifurtimox
parent: 僅模型預測 (L5)
nav_order: 178
evidence_level: L5
indication_count: 7
---

# Nifurtimox
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

# Nifurtimox: De Enfermedad de Chagas a Analbuminemia Congénita

## Resumen en Una Frase

Nifurtimox es un fármaco antiparasitario utilizado para el tratamiento de la Enfermedad de Chagas (tripanosomiasis americana) y la tripanosomiasis africana, cuyo mecanismo conocido consiste en la activación de nitroredutasas que generan especies reactivas de oxígeno (ROS) con efecto citotóxico sobre los parásitos. El modelo TxGNN predice como primera indicación la **analbuminemia congénita**, con un puntaje de confianza del **99.58%**; sin embargo, no existe ningún ensayo clínico ni publicación científica que respalde esta asociación, y el análisis mecanístico la identifica como **probable falso positivo del modelo**. En total, las **7 indicaciones predichas** presentan nivel de evidencia L5 (solo predicción computacional), sin respaldo experimental ni clínico para ninguna de ellas.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad de Chagas (Tripanosomiasis Americana) |
| Nueva Indicación Predicha | Analbuminemia Congénita |
| Puntaje de Predicción TxGNN | 99.58% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por Qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack (brecha de datos identificada como DG002). No obstante, a partir del análisis mecanístico contenido en los razonamientos de reposicionamiento, se sabe que Nifurtimox es un compuesto nitrofurano que actúa mediante la **activación de nitroredutasas** presentes en los parásitos, generando radicales libres y ROS que producen daño oxidativo al ADN y otras macromoléculas del parásito, con efecto citotóxico selectivo sobre *Trypanosoma cruzi* y *T. brucei*.

La analbuminemia congénita es una enfermedad genética rara causada por mutaciones en el gen *ALB*, que resulta en una deficiencia severa en la síntesis de albúmina hepática. **No existe ninguna intersección bioquímica conocida** entre la vía ROS/nitroredutasa de Nifurtimox y las vías de síntesis de proteínas plasmáticas. El propio análisis interno del paquete de evidencia señala que el alto puntaje del modelo (0.9958) es sospechoso de derivar de **conexiones indirectas en el grafo de conocimiento** entre nodos de metabolismo de proteínas plasmáticas, constituyendo un desplazamiento de nodos por asociación indirecta (*indirect node linking bias*).

En conclusión, aunque TxGNN asigna un puntaje extremadamente alto a esta predicción, la evaluación mecanística no sustenta ninguna relación plausible entre Nifurtimox y la analbuminemia congénita. Este caso ilustra la importancia de la interpretación crítica humana como capa de validación posterior al modelo computacional.

---

## Resumen Comparativo de Todas las Indicaciones Predichas

Dado que la totalidad de las indicaciones predichas presentan nivel L5 sin evidencia externa, se incluye a continuación un panorama comparativo de las 7 predicciones para facilitar la priorización:

| Rango | Indicación | Puntaje TxGNN | Recomendación | Evaluación Mecanística |
|-------|-----------|:------------:|:-------------:|----------------------|
| 1 | Analbuminemia congénita | 99.58% | Hold | Falso positivo probable — sin intersección MOA/ALB |
| 2 | Hiperamylasemia | 99.47% | Hold | Falso positivo probable — toxicidad GI como confundidor en KG |
| 3 | Síndrome de hiperviscosidad policlonal | 99.47% | Hold | Contaminación probable por nodo inflamatorio de Chagas |
| 4 | Incompatibilidad de grupo sanguíneo | 99.24% | Hold | Artefacto de agrupamiento en grafo — sin mecanismo aplicable |
| 5 | Gamapatía monoclonal | 99.16% | Research Question | Hipótesis ROS → citotoxicidad en células plasmáticas; requiere datos preclínicos |
| 6 | Enfermedad hematológica premaligna | 99.11% | Research Question | Hipótesis ROS → toxicidad selectiva en células con defectos de reparación de ADN |
| 7 | Enfermedad hematológica con neuropatía periférica | 99.06% | Hold | ⚠️ Inversión de efecto adverso — Nifurtimox **causa** neuropatía periférica |

> **Nota de seguridad crítica (Rango 7):** La indicación de rango 7 representa un caso de *adverse effect inversion* — el modelo confundió el nodo de efecto adverso de Nifurtimox (neuropatía periférica documentada con uso prolongado) con una asociación terapéutica. Utilizar Nifurtimox en esta indicación conllevaría un riesgo significativo de **inducir o agravar** la neuropatía periférica. Este caso debe marcarse como falso positivo por contaminación de efectos adversos en el grafo de conocimiento.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para ninguna de las 7 indicaciones predichas. (Búsqueda realizada en ClinicalTrials.gov e ICTRP el 2026-04-20.)

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para ninguna de las 7 indicaciones predichas. (Búsqueda realizada en PubMed el 2026-04-20.)

---

## Información de Mercado en Colombia

Nifurtimox **no está comercializado en Colombia**. La consulta al INVIMA realizada el 2026-03-29 no arrojó ningún registro sanitario activo. La adquisición actual se realiza por vía de importación directa o a través de programas de acceso especial (Bayer AG es el fabricante de Lampit®, el producto de referencia).

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad completa.

> **Alerta prioritaria:** El análisis de la indicación de rango 7 documenta que Nifurtimox es causa conocida de **neuropatía periférica sensitiva y motora** con uso prolongado (especialmente >90 días), efecto adverso de relevancia regulatoria señalado por la FDA. Cualquier evaluación clínica futura en indicaciones que involucren el sistema nervioso debe considerar este riesgo como limitante principal.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Todas las 7 indicaciones predichas por TxGNN presentan nivel de evidencia L5, sin respaldo en ensayos clínicos ni literatura científica para ninguna de ellas. El análisis mecanístico identifica 5 de las 7 predicciones como probables falsos positivos derivados de artefactos en el grafo de conocimiento (bias por nodos indirectos, contaminación por efectos adversos, agrupamiento de nodos de enfermedades hematológicas). Solo las indicaciones de gamapatía monoclonal (rango 5) y enfermedad hematológica premaligna (rango 6) presentan una hipótesis mecanística teóricamente plausible vía citotoxicidad por ROS, catalogadas como "Research Question" pendientes de validación preclínica.

**Para avanzar se necesita:**
- Obtener datos de MOA completos desde DrugBank (DG002) para confirmar el perfil de actividad ROS/nitroredutasa aplicable a células hematológicas
- Realizar estudios de citotoxicidad *in vitro* en líneas celulares de células plasmáticas (para rango 5) y líneas de MDS/smoldering myeloma (para rango 6) como primer paso de validación preclínica
- Evaluar el perfil de hematotoxicidad de Nifurtimox antes de cualquier exploración en indicaciones hematológicas, dado el riesgo de mielosupresión potencial
- Verificar mecanismos de acceso regulatorio al INVIMA para investigación clínica, ya que el fármaco no está comercializado en Colombia
- Marcar las predicciones de rangos 1–4 y 7 como **candidatas a falso positivo** para retroalimentación al pipeline de TxGNN, con especial énfasis en el caso de rango 7 como ejemplo de *adverse effect node contamination*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

