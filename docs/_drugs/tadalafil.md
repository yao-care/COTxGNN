---
layout: default
title: Tadalafil
parent: 僅模型預測 (L5)
nav_order: 219
evidence_level: L5
indication_count: 8
---

# Tadalafil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Tadalafil: De Hipertensión Arterial Pulmonar a Hipertricosis Universalis Congénita Tipo Ambras

## Resumen en Una Frase

Tadalafil es un inhibidor de la fosfodiesterasa tipo 5 (PDE5), ampliamente aprobado en mercados internacionales para disfunción eréctil, hipertensión arterial pulmonar (PAH) e hiperplasia prostática benigna, aunque actualmente no cuenta con registro sanitario activo en Colombia.
El modelo TxGNN predice **8 indicaciones candidatas**, siendo la de mayor rango la **Hipertricosis Universalis Congénita Tipo Ambras** con un puntaje del **99.98%**; sin embargo, ninguna de las 8 indicaciones cuenta con ensayos clínicos de soporte, y la única publicación identificada corresponde a un reporte de evento adverso — señal negativa para la indicación de rango 8.
Con base en el análisis de plausibilidad biológica y la ausencia de evidencia clínica, la recomendación global para este ciclo es **Hold**.

---

## Resumen Rápido

| Item | Contenido |
|------|-----------|
| Indicación Original | Hipertensión arterial pulmonar / Disfunción eréctil (aprobado en otros mercados; sin registro en Colombia) |
| Nueva Indicación Predicha (Rango 1) | Hipertricosis Universalis Congénita Tipo Ambras |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en este Evidence Pack. Según la información conocida, Tadalafil es un inhibidor selectivo de la fosfodiesterasa tipo 5 (PDE5), lo que incrementa los niveles de cGMP intracelular produciendo relajación del músculo liso vascular; su eficacia en hipertensión arterial pulmonar (Adcirca®) y disfunción eréctil ha sido ampliamente comprobada, y mecanísticamente podría ser aplicable a condiciones con componente de vasoconstricción patológica.

En cuanto a la indicación de rango 1, la Hipertricosis Universalis Congénita Tipo Ambras es una enfermedad genética ultrarara causada por mutaciones en el gen *TRPS1*, cuya patología involucra alteraciones en el desarrollo folicular sin relación conocida con la vía PDE5-cGMP. Este patrón se repite en los rangos 2 y 5 (otras enfermedades del cabello), lo que sugiere que estas predicciones probablemente sean un **artefacto del Knowledge Graph** por efecto de agrupación de nodos de enfermedades capilares en el grafo, sin representar una conexión biológica real.

La excepción más destacada del conjunto es la **enfermedad cardíaca por cifoescoliosis** (rango 7, 99.43%): la deformidad espinal severa puede causar HAP secundaria por restricción ventilatoria crónica e hipoxia, y Tadalafil ya está aprobado para esta misma vía fisiopatológica en HAP primaria. Esta es la única candidata con plausibilidad biológica indirecta, aunque carece de evidencia clínica específica para este fenotipo. Por el contrario, la indicación de rango 8 (migraña con aura del tronco encefálico) presenta una **señal activamente negativa**: la vía NO↑ → vasodilatación craneal es consistente con la inducción de migraña, no con su tratamiento.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para ninguna de las 8 indicaciones predichas.

---

## Evidencia de Literatura

La búsqueda sistemática en PubMed para las 8 indicaciones identificó únicamente 1 publicación (correspondiente al rango 8):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|----------------------|
| [17059442](https://pubmed.ncbi.nlm.nih.gov/17059442/) | 2006 | Reporte de Caso | *Cephalalgia* | **⚠️ SEÑAL NEGATIVA:** Documenta que Tadalafil indujo aura de migraña típica sin cefalea — registra el fármaco como **desencadenante** del evento, no como tratamiento |

> **Nota de interpretación:** Esta publicación no respalda la eficacia de Tadalafil en migraña; al contrario, la inhibición de PDE5 aumenta el óxido nítrico y produce vasodilatación craneal, mecanismo consistente con la inducción de crisis migrañosas.

---

## Información de Mercado en Colombia

Tadalafil no cuenta con registros sanitarios activos en Colombia (INVIMA). La consulta realizada el 2026-03-29 no arrojó ningún resultado, y el estado de mercado registrado es **no comercializado**.

---

## Resumen de las 8 Indicaciones Predichas

| Rango | Indicación | Puntaje TxGNN | Nivel de Evidencia | Plausibilidad Biológica | Decisión |
|-------|-----------|:------------:|:-----------------:|------------------------|:--------:|
| 1 | Hipertricosis Universalis Congénita Tipo Ambras | 99.98% | L5 | Muy baja — probable artefacto KG (nodos capilares) | Hold |
| 2 | Hipertricosis (enfermedad) | 99.98% | L5 | Muy baja — artefacto KG; no equiparable a Minoxidil (KATP ≠ PDE5) | Hold |
| 3 | Síndrome de malformación con componente dental/periodontal | 99.97% | L5 | Muy baja — anomalía estructural del desarrollo; sin rol conocido de cGMP | Hold |
| 4 | Síndrome con malformación de Dandy-Walker como rasgo mayor | 99.97% | L5 | Muy baja — malformación cerebral estructural embrionaria, no reversible con fármacos | Hold |
| 5 | Anomalía genética aislada del tallo piloso | 99.96% | L5 | Muy baja — defecto de proteína estructural; PDE5 no corrige tallo piloso | Hold |
| 6 | Tricromegalia familiar aislada | 99.65% | L5 | Baja — dirección inversa: prostaglandinas/análogos *causan* tricromegalia, no la tratan | Hold |
| 7 | Enfermedad cardíaca por cifoescoliosis | 99.43% | L5 | **Moderada** — HAP secundaria → vía PDE5 con aprobación vigente (Adcirca®) | Research Question |
| 8 | Migraña con aura del tronco encefálico | 99.08% | L4 | **Negativa** — única literatura disponible documenta inducción de aura como evento adverso | Hold |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

> Los datos de advertencias clave, contraindicaciones e interacciones farmacológicas no estaban disponibles en este Evidence Pack. Antes de cualquier evaluación clínica se recomienda revisar la monografía completa de DrugBank (DB00820) y la información de prescripción aprobada de Adcirca® (HAP) y Cialis® (DE/HPB), prestando especial atención a contraindicaciones con nitratos y antihipertensivos.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Las 8 indicaciones predichas por TxGNN para Tadalafil carecen de evidencia clínica de soporte; el patrón de predicciones de rango 1–6 (enfermedades del cabello y malformaciones estructurales) es consistente con sesgo por agrupación de nodos en el Knowledge Graph, y la única publicación disponible constituye una señal adversa, no de eficacia. La enfermedad cardíaca por cifoescoliosis (rango 7) es la única candidata con plausibilidad biológica indirecta vía HAP secundaria, y merece seguimiento como pregunta de investigación.

**Para avanzar se necesita:**
- Completar datos de mecanismo de acción (MOA) y perfil de seguridad completo desde DrugBank DB00820 y prospecto oficial
- Verificar si Tadalafil tiene tramitado registro INVIMA para sus indicaciones aprobadas internacionalmente (HAP, DE, HPB)
- Para la indicación de rango 7: buscar estudios de Tadalafil en HAP asociada a enfermedades pulmonares restrictivas (cifoescoliosis, fibrosis pulmonar, síndrome de obesidad-hipoventilación)
- Auditar el nodo de enfermedades del cabello en el Knowledge Graph TxGNN para descartar sesgo sistemático de agrupación antes de procesar candidatos similares en futuros ciclos
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

